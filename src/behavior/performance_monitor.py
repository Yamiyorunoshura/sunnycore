"""
Performance Monitoring System for Behavior Testing Layer

Provides comprehensive metrics collection, monitoring, and alerting
for all behavior testing components.
"""

import time
import json
import threading
import logging
from typing import Dict, List, Any, Optional, Callable, Union
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
import statistics
import psutil
import redis


@dataclass
class PerformanceMetric:
    """Individual performance metric data point"""
    timestamp: float
    component: str
    metric_name: str
    value: float
    unit: str
    tags: Dict[str, str]


@dataclass
class AlertThreshold:
    """Alert threshold configuration"""
    metric_name: str
    component: str
    warning_threshold: float
    critical_threshold: float
    comparison: str  # 'gt', 'lt', 'eq'
    duration: int  # seconds


@dataclass
class Alert:
    """Alert data structure"""
    id: str
    metric_name: str
    component: str
    severity: str  # 'warning', 'critical'
    message: str
    timestamp: float
    value: float
    threshold: float
    resolved: bool = False
    resolved_at: Optional[float] = None


class PerformanceMonitor:
    """
    Performance monitoring system for behavior testing components
    """

    def __init__(self,
                 redis_host: str = 'localhost',
                 redis_port: int = 6379,
                 redis_db: int = 0,
                 retention_hours: int = 24):
        """
        Initialize performance monitor

        Args:
            redis_host: Redis host for metrics storage
            redis_port: Redis port
            redis_db: Redis database number
            retention_hours: Data retention period in hours
        """
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.retention_hours = retention_hours

        self.logger = logging.getLogger(__name__)

        # In-memory metrics cache
        self.metrics_cache = defaultdict(lambda: deque(maxlen=1000))
        self.alerts = {}
        self.alert_thresholds = []

        # Performance tracking
        self.component_timers = defaultdict(float)
        self.component_call_counts = defaultdict(int)

        # Redis connection (lazy initialization)
        self._redis_client = None

        # Background monitoring thread
        self._monitoring_thread = None
        self._stop_monitoring = False

        # Initialize default thresholds
        self._initialize_default_thresholds()

    @property
    def redis_client(self):
        """Lazy Redis client initialization"""
        if self._redis_client is None:
            try:
                self._redis_client = redis.Redis(
                    host=self.redis_host,
                    port=self.redis_port,
                    db=self.redis_db,
                    decode_responses=True
                )
                # Test connection
                self._redis_client.ping()
                self.logger.info("Connected to Redis for performance monitoring")
            except Exception as e:
                self.logger.warning(f"Failed to connect to Redis: {e}")
                self._redis_client = None

        return self._redis_client

    def _initialize_default_thresholds(self):
        """Initialize default alert thresholds"""
        default_thresholds = [
            # Golden Set Manager thresholds
            AlertThreshold(
                metric_name="validation_time",
                component="golden_set_manager",
                warning_threshold=3.0,
                critical_threshold=5.0,
                comparison="gt",
                duration=60
            ),
            AlertThreshold(
                metric_name="test_case_add_time",
                component="golden_set_manager",
                warning_threshold=0.1,
                critical_threshold=0.5,
                comparison="gt",
                duration=60
            ),

            # Promptfoo Integration thresholds
            AlertThreshold(
                metric_name="evaluation_time",
                component="promptfoo_integration",
                warning_threshold=5.0,
                critical_threshold=10.0,
                comparison="gt",
                duration=60
            ),
            AlertThreshold(
                metric_name="quality_score",
                component="promptfoo_integration",
                warning_threshold=0.7,
                critical_threshold=0.5,
                comparison="lt",
                duration=120
            ),

            # DeepEval Integration thresholds
            AlertThreshold(
                metric_name="f1_score_calculation_time",
                component="deepeval_integration",
                warning_threshold=1.0,
                critical_threshold=2.0,
                comparison="gt",
                duration=60
            ),
            AlertThreshold(
                metric_name="architecture_validation_time",
                component="deepeval_integration",
                warning_threshold=2.0,
                critical_threshold=4.0,
                comparison="gt",
                duration=60
            ),

            # System thresholds
            AlertThreshold(
                metric_name="memory_usage_mb",
                component="system",
                warning_threshold=500.0,
                critical_threshold=1000.0,
                comparison="gt",
                duration=300
            ),
            AlertThreshold(
                metric_name="cpu_usage_percent",
                component="system",
                warning_threshold=70.0,
                critical_threshold=90.0,
                comparison="gt",
                duration=300
            )
        ]

        self.alert_thresholds.extend(default_thresholds)

    def record_metric(self,
                    component: str,
                    metric_name: str,
                    value: float,
                    unit: str = "seconds",
                    tags: Optional[Dict[str, str]] = None):
        """
        Record a performance metric

        Args:
            component: Component name
            metric_name: Metric name
            value: Metric value
            unit: Unit of measurement
            tags: Additional metadata tags
        """
        timestamp = time.time()
        tags = tags or {}

        metric = PerformanceMetric(
            timestamp=timestamp,
            component=component,
            metric_name=metric_name,
            value=value,
            unit=unit,
            tags=tags
        )

        # Add to cache
        cache_key = f"{component}:{metric_name}"
        self.metrics_cache[cache_key].append(metric)

        # Store in Redis if available
        if self.redis_client:
            try:
                metric_data = {
                    'timestamp': timestamp,
                    'component': component,
                    'metric_name': metric_name,
                    'value': value,
                    'unit': unit,
                    'tags': tags
                }

                # Store in time-series format
                key = f"metrics:{component}:{metric_name}"
                self.redis_client.zadd(key, {json.dumps(metric_data): timestamp})

                # Set expiration
                self.redis_client.expireat(
                    key,
                    int(timestamp + self.retention_hours * 3600)
                )

            except Exception as e:
                self.logger.error(f"Failed to store metric in Redis: {e}")

        # Check for alerts
        self._check_metric_thresholds(metric)

    def time_function(self, component: str, metric_name: str):
        """
        Decorator to time function execution

        Args:
            component: Component name
            metric_name: Metric name for timing

        Returns:
            Decorator function
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    execution_time = time.time() - start_time

                    # Record successful execution time
                    self.record_metric(
                        component=component,
                        metric_name=metric_name,
                        value=execution_time,
                        unit="seconds",
                        tags={"status": "success"}
                    )

                    return result
                except Exception as e:
                    execution_time = time.time() - start_time

                    # Record failed execution time
                    self.record_metric(
                        component=component,
                        metric_name=metric_name,
                        value=execution_time,
                        unit="seconds",
                        tags={"status": "error", "error": str(e)}
                    )

                    raise

            return wrapper
        return decorator

    def record_system_metrics(self):
        """Record system-level metrics"""
        try:
            # Memory usage
            memory_info = psutil.virtual_memory()
            self.record_metric(
                component="system",
                metric_name="memory_usage_mb",
                value=memory_info.used / (1024 * 1024),
                unit="MB"
            )

            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            self.record_metric(
                component="system",
                metric_name="cpu_usage_percent",
                value=cpu_percent,
                unit="percent"
            )

            # Disk usage
            disk_info = psutil.disk_usage('/')
            self.record_metric(
                component="system",
                metric_name="disk_usage_percent",
                value=disk_info.percent,
                unit="percent"
            )

        except Exception as e:
            self.logger.error(f"Failed to record system metrics: {e}")

    def get_metrics(self,
                  component: Optional[str] = None,
                  metric_name: Optional[str] = None,
                  start_time: Optional[float] = None,
                  end_time: Optional[float] = None,
                  limit: int = 100) -> List[PerformanceMetric]:
        """
        Retrieve metrics with optional filtering

        Args:
            component: Filter by component
            metric_name: Filter by metric name
            start_time: Start timestamp
            end_time: End timestamp
            limit: Maximum number of metrics to return

        Returns:
            List of matching metrics
        """
        metrics = []

        # Build cache key
        cache_key = None
        if component and metric_name:
            cache_key = f"{component}:{metric_name}"
        elif component:
            # Search all metrics for component
            for key in self.metrics_cache.keys():
                if key.startswith(f"{component}:"):
                    metrics.extend(list(self.metrics_cache[key]))
        else:
            # Return all metrics
            for cache_metrics in self.metrics_cache.values():
                metrics.extend(list(cache_metrics))

        # If specific component and metric requested
        if cache_key and cache_key in self.metrics_cache:
            metrics = list(self.metrics_cache[cache_key])

        # Apply time filters
        if start_time:
            metrics = [m for m in metrics if m.timestamp >= start_time]
        if end_time:
            metrics = [m for m in metrics if m.timestamp <= end_time]

        # Sort by timestamp and limit
        metrics.sort(key=lambda x: x.timestamp, reverse=True)
        return metrics[:limit]

    def get_metric_statistics(self,
                             component: str,
                             metric_name: str,
                             time_window: int = 3600) -> Dict[str, float]:
        """
        Calculate statistics for a metric over a time window

        Args:
            component: Component name
            metric_name: Metric name
            time_window: Time window in seconds (default: 1 hour)

        Returns:
            Dictionary with statistics
        """
        end_time = time.time()
        start_time = end_time - time_window

        metrics = self.get_metrics(
            component=component,
            metric_name=metric_name,
            start_time=start_time,
            end_time=end_time
        )

        if not metrics:
            return {}

        values = [m.value for m in metrics]

        return {
            'count': len(values),
            'min': min(values),
            'max': max(values),
            'mean': statistics.mean(values),
            'median': statistics.median(values),
            'stdev': statistics.stdev(values) if len(values) > 1 else 0.0,
            'p95': statistics.quantiles(values, n=20)[18] if len(values) > 1 else values[0],
            'p99': statistics.quantiles(values, n=100)[98] if len(values) > 1 else values[0]
        }

    def add_alert_threshold(self, threshold: AlertThreshold):
        """
        Add or update an alert threshold

        Args:
            threshold: Alert threshold configuration
        """
        # Remove existing threshold for same metric/component
        self.alert_thresholds = [
            t for t in self.alert_thresholds
            if not (t.metric_name == threshold.metric_name and
                   t.component == threshold.component)
        ]

        self.alert_thresholds.append(threshold)
        self.logger.info(f"Added alert threshold for {threshold.component}:{threshold.metric_name}")

    def _check_metric_thresholds(self, metric: PerformanceMetric):
        """
        Check if metric triggers any alert thresholds

        Args:
            metric: Metric to check
        """
        for threshold in self.alert_thresholds:
            if (threshold.metric_name == metric.metric_name and
                threshold.component == metric.component):

                triggered = False

                if threshold.comparison == 'gt' and metric.value > threshold.critical_threshold:
                    severity = 'critical'
                    triggered = True
                elif threshold.comparison == 'lt' and metric.value < threshold.critical_threshold:
                    severity = 'critical'
                    triggered = True
                elif threshold.comparison == 'gt' and metric.value > threshold.warning_threshold:
                    severity = 'warning'
                    triggered = True
                elif threshold.comparison == 'lt' and metric.value < threshold.warning_threshold:
                    severity = 'warning'
                    triggered = True

                if triggered:
                    self._create_alert(metric, threshold, severity)

    def _create_alert(self, metric: PerformanceMetric, threshold: AlertThreshold, severity: str):
        """
        Create an alert if conditions are met

        Args:
            metric: Triggering metric
            threshold: Alert threshold
            severity: Alert severity
        """
        alert_id = f"{metric.component}_{metric.metric_name}_{severity}_{int(metric.timestamp)}"

        # Check if similar alert already exists and is not resolved
        existing_alert = None
        for alert_id_existing, alert_existing in self.alerts.items():
            if (alert_existing.metric_name == metric.metric_name and
                alert_existing.component == metric.component and
                not alert_existing.resolved):
                existing_alert = alert_existing
                break

        if existing_alert:
            # Update existing alert
            existing_alert.timestamp = metric.timestamp
            existing_alert.value = metric.value
            self.logger.info(f"Updated alert {existing_alert.id}")
        else:
            # Create new alert
            alert = Alert(
                id=alert_id,
                metric_name=metric.metric_name,
                component=metric.component,
                severity=severity,
                message=f"{metric.metric_name} {severity}: {metric.value} {metric.unit} (threshold: {threshold.critical_threshold if severity == 'critical' else threshold.warning_threshold})",
                timestamp=metric.timestamp,
                value=metric.value,
                threshold=threshold.critical_threshold if severity == 'critical' else threshold.warning_threshold
            )

            self.alerts[alert_id] = alert
            self.logger.warning(f"Created alert: {alert.message}")

            # Send notification (implement based on your notification system)
            self._send_alert_notification(alert)

    def _send_alert_notification(self, alert: Alert):
        """
        Send alert notification (placeholder implementation)

        Args:
            alert: Alert to send notification for
        """
        # This is a placeholder - implement based on your notification system
        # Examples: email, Slack, PagerDuty, etc.
        self.logger.info(f"Alert notification sent: {alert.message}")

    def resolve_alert(self, alert_id: str):
        """
        Resolve an alert

        Args:
            alert_id: Alert identifier
        """
        if alert_id in self.alerts:
            alert = self.alerts[alert_id]
            alert.resolved = True
            alert.resolved_at = time.time()
            self.logger.info(f"Resolved alert: {alert_id}")

    def get_active_alerts(self) -> List[Alert]:
        """
        Get all active (unresolved) alerts

        Returns:
            List of active alerts
        """
        return [alert for alert in self.alerts.values() if not alert.resolved]

    def get_alert_history(self, component: Optional[str] = None, limit: int = 100) -> List[Alert]:
        """
        Get alert history with optional filtering

        Args:
            component: Filter by component
            limit: Maximum number of alerts to return

        Returns:
            List of alerts
        """
        alerts = list(self.alerts.values())

        if component:
            alerts = [a for a in alerts if a.component == component]

        # Sort by timestamp (newest first)
        alerts.sort(key=lambda x: x.timestamp, reverse=True)
        return alerts[:limit]

    def start_monitoring(self, interval: int = 30):
        """
        Start background monitoring thread

        Args:
            interval: Monitoring interval in seconds
        """
        if self._monitoring_thread and self._monitoring_thread.is_alive():
            self.logger.warning("Monitoring thread already running")
            return

        self._stop_monitoring = False
        self._monitoring_thread = threading.Thread(
            target=self._monitoring_loop,
            args=(interval,),
            daemon=True
        )
        self._monitoring_thread.start()
        self.logger.info(f"Started performance monitoring with {interval}s interval")

    def stop_monitoring(self):
        """Stop background monitoring thread"""
        self._stop_monitoring = True
        if self._monitoring_thread and self._monitoring_thread.is_alive():
            self._monitoring_thread.join(timeout=5)
        self.logger.info("Stopped performance monitoring")

    def _monitoring_loop(self, interval: int):
        """
        Background monitoring loop

        Args:
            interval: Monitoring interval in seconds
        """
        while not self._stop_monitoring:
            try:
                # Record system metrics
                self.record_system_metrics()

                # Clean up old alerts
                self._cleanup_old_alerts()

                # Clean up old metrics from Redis
                if self.redis_client:
                    self._cleanup_old_metrics()

                # Sleep for interval
                time.sleep(interval)

            except Exception as e:
                self.logger.error(f"Error in monitoring loop: {e}")
                time.sleep(interval)

    def _cleanup_old_alerts(self):
        """Clean up resolved alerts older than retention period"""
        retention_time = time.time() - (self.retention_hours * 3600)

        alert_ids_to_remove = []
        for alert_id, alert in self.alerts.items():
            if alert.resolved and alert.resolved_at and alert.resolved_at < retention_time:
                alert_ids_to_remove.append(alert_id)

        for alert_id in alert_ids_to_remove:
            del self.alerts[alert_id]
            self.logger.debug(f"Cleaned up old alert: {alert_id}")

    def _cleanup_old_metrics(self):
        """Clean up old metrics from Redis"""
        if not self.redis_client:
            return

        try:
            # Get all metric keys
            keys = self.redis_client.keys("metrics:*")

            cutoff_time = int(time.time() - (self.retention_hours * 3600))

            for key in keys:
                # Remove old metrics
                self.redis_client.zremrangebyscore(key, 0, cutoff_time)

                # Remove key if empty
                if self.redis_client.zcard(key) == 0:
                    self.redis_client.delete(key)

        except Exception as e:
            self.logger.error(f"Failed to cleanup old metrics: {e}")

    def generate_performance_report(self,
                                 time_window: int = 3600) -> Dict[str, Any]:
        """
        Generate comprehensive performance report

        Args:
            time_window: Time window in seconds (default: 1 hour)

        Returns:
            Performance report dictionary
        """
        end_time = time.time()
        start_time = end_time - time_window

        report = {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'time_window_seconds': time_window,
            'start_time': datetime.fromtimestamp(start_time, timezone.utc).isoformat(),
            'end_time': datetime.fromtimestamp(end_time, timezone.utc).isoformat(),
            'components': {},
            'alerts': {
                'active': len(self.get_active_alerts()),
                'total_generated': len(self.alerts)
            }
        }

        # Get all unique components
        components = set()
        for cache_key in self.metrics_cache.keys():
            if ':' in cache_key:
                component = cache_key.split(':')[0]
                components.add(component)

        # Generate component statistics
        for component in components:
            component_metrics = {}

            # Get all metric names for this component
            metric_names = set()
            for cache_key in self.metrics_cache.keys():
                if cache_key.startswith(f"{component}:"):
                    metric_name = cache_key.split(':')[1]
                    metric_names.add(metric_name)

            # Calculate statistics for each metric
            for metric_name in metric_names:
                stats = self.get_metric_statistics(
                    component=component,
                    metric_name=metric_name,
                    time_window=time_window
                )
                if stats:
                    component_metrics[metric_name] = stats

            if component_metrics:
                report['components'][component] = component_metrics

        return report

    def export_metrics(self,
                      component: Optional[str] = None,
                      metric_name: Optional[str] = None,
                      start_time: Optional[float] = None,
                      end_time: Optional[float] = None,
                      format: str = 'json') -> str:
        """
        Export metrics in specified format

        Args:
            component: Filter by component
            metric_name: Filter by metric name
            start_time: Start timestamp
            end_time: End timestamp
            format: Export format ('json', 'csv')

        Returns:
            Formatted export data
        """
        metrics = self.get_metrics(
            component=component,
            metric_name=metric_name,
            start_time=start_time,
            end_time=end_time,
            limit=10000
        )

        if format == 'json':
            return json.dumps([asdict(metric) for metric in metrics], indent=2)
        elif format == 'csv':
            import io
            import csv

            output = io.StringIO()
            writer = csv.writer(output)

            # Write header
            writer.writerow(['timestamp', 'component', 'metric_name', 'value', 'unit', 'tags'])

            # Write data
            for metric in metrics:
                writer.writerow([
                    metric.timestamp,
                    metric.component,
                    metric.metric_name,
                    metric.value,
                    metric.unit,
                    json.dumps(metric.tags)
                ])

            return output.getvalue()
        else:
            raise ValueError(f"Unsupported export format: {format}")

    def cleanup(self):
        """Cleanup resources"""
        self.stop_monitoring()

        if self.redis_client:
            try:
                self.redis_client.close()
            except:
                pass


# Global performance monitor instance
_performance_monitor = None


def get_performance_monitor() -> PerformanceMonitor:
    """Get the global performance monitor instance"""
    global _performance_monitor
    if _performance_monitor is None:
        _performance_monitor = PerformanceMonitor()
    return _performance_monitor


def monitor_performance(component: str, metric_name: str):
    """
    Decorator for automatic performance monitoring

    Args:
        component: Component name
        metric_name: Metric name

    Returns:
        Decorator function
    """
    monitor = get_performance_monitor()
    return monitor.time_function(component, metric_name)