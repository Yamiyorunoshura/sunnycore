"""
Security Testing Monitoring System

This module provides comprehensive monitoring capabilities for security testing,
including real-time alerts, metrics collection, and performance tracking.
"""

import json
import threading
import time
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any, Callable, Dict, List, Optional

from .types import SecurityAlert, SecurityTestResult, SeverityLevel


@dataclass
class MetricsSnapshot:
    """Snapshot of security testing metrics"""

    timestamp: datetime
    total_tests: int
    vulnerabilities_detected: int
    critical_vulnerabilities: int
    high_vulnerabilities: int
    medium_vulnerabilities: int
    low_vulnerabilities: int
    average_execution_time: float
    tests_per_second: float
    error_rate: float


class MonitoringSystem:
    """
    Real-time monitoring system for security testing operations.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the monitoring system.

        Args:
            config: Configuration dictionary for monitoring parameters
        """
        self.config = config or {}
        self.monitoring_interval = self.config.get("monitoring_interval", 10)
        self.alert_thresholds = self.config.get("alert_thresholds", {})
        self.max_history_size = self.config.get("max_history_size", 1000)

        # Initialize monitoring data structures
        self.test_results: List[SecurityTestResult] = []
        self.alerts: List[SecurityAlert] = []
        self.metrics_history: deque = deque(maxlen=self.max_history_size)
        self.performance_metrics = defaultdict(list)

        # Threading for background monitoring
        self._monitoring_thread = None
        self._stop_monitoring = threading.Event()
        self._callbacks: List[Callable] = []

        # Initialize default alert thresholds
        self._init_default_thresholds()

        # Start background monitoring
        self.start_monitoring()

    def _init_default_thresholds(self):
        """Initialize default alert thresholds."""
        self.alert_thresholds = {
            "critical_vulnerability_count": 1,
            "high_vulnerability_count": 3,
            "error_rate": 0.1,  # 10%
            "average_execution_time": 5.0,  # 5 seconds
            "vulnerability_detection_rate": 0.05,  # 5%
            "consecutive_failures": 5,
            **self.alert_thresholds,
        }

    def record_test_result(self, result: SecurityTestResult):
        """
        Record a security test result.

        Args:
            result: The test result to record
        """
        self.test_results.append(result)

        # Update performance metrics
        self.performance_metrics["execution_times"].append(result.execution_time)
        if result.status.name == "FAILED":
            self.performance_metrics["errors"].append(result)

        # Check for alert conditions
        self._check_alert_conditions(result)

        # Notify callbacks
        self._notify_callbacks(result)

    def start_monitoring(self):
        """Start the background monitoring thread."""
        if self._monitoring_thread is None or not self._monitoring_thread.is_alive():
            self._stop_monitoring.clear()
            self._monitoring_thread = threading.Thread(
                target=self._monitoring_loop, daemon=True, name="SecurityMonitoring"
            )
            self._monitoring_thread.start()

    def stop_monitoring(self):
        """Stop the background monitoring thread."""
        if self._monitoring_thread and self._monitoring_thread.is_alive():
            self._stop_monitoring.set()
            self._monitoring_thread.join(timeout=5.0)

    def _monitoring_loop(self):
        """Background monitoring loop."""
        while not self._stop_monitoring.is_set():
            try:
                # Collect current metrics snapshot
                snapshot = self._collect_metrics_snapshot()
                self.metrics_history.append(snapshot)

                # Perform periodic health checks
                self._perform_health_checks()

                # Clean up old data
                self._cleanup_old_data()

                # Sleep for monitoring interval
                time.sleep(self.monitoring_interval)

            except Exception as e:
                # Create alert for monitoring error
                alert = SecurityAlert(
                    alert_id=f"MON-{int(time.time())}",
                    alert_type="Monitoring Error",
                    severity=SeverityLevel.MEDIUM,
                    message=f"Monitoring system error: {str(e)}",
                    timestamp=datetime.now(),
                    source_component="MonitoringSystem",
                    details={"error": str(e)},
                )
                self.alerts.append(alert)

    def _collect_metrics_snapshot(self) -> MetricsSnapshot:
        """Collect current metrics snapshot."""
        if not self.test_results:
            return MetricsSnapshot(
                timestamp=datetime.now(),
                total_tests=0,
                vulnerabilities_detected=0,
                critical_vulnerabilities=0,
                high_vulnerabilities=0,
                medium_vulnerabilities=0,
                low_vulnerabilities=0,
                average_execution_time=0.0,
                tests_per_second=0.0,
                error_rate=0.0,
            )

        # Count vulnerabilities by severity
        detected_results = [r for r in self.test_results if r.detected]
        critical_count = sum(
            1 for r in detected_results if r.severity == SeverityLevel.CRITICAL
        )
        high_count = sum(
            1 for r in detected_results if r.severity == SeverityLevel.HIGH
        )
        medium_count = sum(
            1 for r in detected_results if r.severity == SeverityLevel.MEDIUM
        )
        low_count = sum(1 for r in detected_results if r.severity == SeverityLevel.LOW)

        # Calculate performance metrics
        execution_times = self.performance_metrics["execution_times"]
        avg_execution_time = (
            sum(execution_times) / len(execution_times) if execution_times else 0.0
        )

        error_count = len(self.performance_metrics["errors"])
        total_count = len(self.test_results)
        error_rate = error_count / total_count if total_count > 0 else 0.0

        # Calculate tests per second (for recent tests)
        recent_tests = [
            r
            for r in self.test_results
            if r.timestamp > datetime.now() - timedelta(minutes=1)
        ]
        tests_per_second = len(recent_tests) / 60.0

        return MetricsSnapshot(
            timestamp=datetime.now(),
            total_tests=total_count,
            vulnerabilities_detected=len(detected_results),
            critical_vulnerabilities=critical_count,
            high_vulnerabilities=high_count,
            medium_vulnerabilities=medium_count,
            low_vulnerabilities=low_count,
            average_execution_time=avg_execution_time,
            tests_per_second=tests_per_second,
            error_rate=error_rate,
        )

    def _check_alert_conditions(self, result: SecurityTestResult):
        """Check for alert conditions based on test result."""
        alerts_to_create = []

        # Check for critical vulnerabilities
        if result.detected and result.severity == SeverityLevel.CRITICAL:
            alerts_to_create.append(self._create_vulnerability_alert(result))

        # Check for high vulnerability count threshold
        recent_high_vulns = [
            r
            for r in self.test_results[-100:]  # Last 100 tests
            if r.detected and r.severity == SeverityLevel.HIGH
        ]
        if len(recent_high_vulns) >= self.alert_thresholds["high_vulnerability_count"]:
            alerts_to_create.append(
                SecurityAlert(
                    alert_id=f"HIGH-VULN-{int(time.time())}",
                    alert_type="High Vulnerability Threshold Exceeded",
                    severity=SeverityLevel.HIGH,
                    message=f"High vulnerability count threshold exceeded: {len(recent_high_vulns)}",
                    timestamp=datetime.now(),
                    source_component="MonitoringSystem",
                    details={
                        "threshold": self.alert_thresholds["high_vulnerability_count"],
                        "actual_count": len(recent_high_vulns),
                        "time_window": "last 100 tests",
                    },
                )
            )

        # Check for slow execution
        if result.execution_time > self.alert_thresholds["average_execution_time"]:
            alerts_to_create.append(
                SecurityAlert(
                    alert_id=f"SLOW-EXEC-{int(time.time())}",
                    alert_type="Slow Execution Detected",
                    severity=SeverityLevel.MEDIUM,
                    message=f"Test execution time exceeded threshold: {result.execution_time:.2f}s",
                    timestamp=datetime.now(),
                    source_component="MonitoringSystem",
                    details={
                        "threshold": self.alert_thresholds["average_execution_time"],
                        "actual_time": result.execution_time,
                        "test_id": result.test_id,
                    },
                )
            )

        # Add all alerts
        self.alerts.extend(alerts_to_create)

    def _create_vulnerability_alert(self, result: SecurityTestResult) -> SecurityAlert:
        """Create a vulnerability detection alert."""
        return SecurityAlert(
            alert_id=f"VULN-{int(time.time())}",
            alert_type="Vulnerability Detected",
            severity=result.severity,
            message=f"{result.vulnerability_type.value} detected in test {result.test_id}",
            timestamp=datetime.now(),
            source_component=result.test_name,
            details={
                "test_id": result.test_id,
                "vulnerability_type": result.vulnerability_type.value,
                "confidence_score": result.confidence_score,
                "description": result.description,
            },
        )

    def _perform_health_checks(self):
        """Perform periodic health checks."""
        # Check for memory leaks (simplified)
        if len(self.test_results) > 10000:
            # Keep only recent test results
            self.test_results = self.test_results[-5000:]

        # Check for high error rates
        if self.test_results:
            recent_results = self.test_results[-100:]  # Last 100 tests
            error_count = sum(1 for r in recent_results if r.status.name == "FAILED")
            error_rate = error_count / len(recent_results)

            if error_rate > self.alert_thresholds["error_rate"]:
                alert = SecurityAlert(
                    alert_id=f"HIGH-ERROR-{int(time.time())}",
                    alert_type="High Error Rate Detected",
                    severity=SeverityLevel.HIGH,
                    message=f"Error rate threshold exceeded: {error_rate:.2%}",
                    timestamp=datetime.now(),
                    source_component="MonitoringSystem",
                    details={
                        "threshold": self.alert_thresholds["error_rate"],
                        "actual_rate": error_rate,
                        "recent_tests": len(recent_results),
                        "error_count": error_count,
                    },
                )
                self.alerts.append(alert)

    def _cleanup_old_data(self):
        """Clean up old monitoring data."""
        # Keep only recent alerts (last 24 hours)
        cutoff_time = datetime.now() - timedelta(hours=24)
        self.alerts = [a for a in self.alerts if a.timestamp > cutoff_time]

        # Keep only recent performance metrics
        for key in self.performance_metrics:
            if len(self.performance_metrics[key]) > 1000:
                self.performance_metrics[key] = self.performance_metrics[key][-500:]

    def get_current_metrics(self) -> Dict[str, Any]:
        """Get current monitoring metrics."""
        snapshot = self._collect_metrics_snapshot()

        return {
            "timestamp": snapshot.timestamp.isoformat(),
            "total_tests": snapshot.total_tests,
            "vulnerabilities_detected": snapshot.vulnerabilities_detected,
            "severity_breakdown": {
                "critical": snapshot.critical_vulnerabilities,
                "high": snapshot.high_vulnerabilities,
                "medium": snapshot.medium_vulnerabilities,
                "low": snapshot.low_vulnerabilities,
            },
            "performance": {
                "average_execution_time": snapshot.average_execution_time,
                "tests_per_second": snapshot.tests_per_second,
                "error_rate": snapshot.error_rate,
            },
            "alerts_count": len(self.alerts),
            "active_alerts": len([a for a in self.alerts if not a.resolved]),
        }

    def get_alerts(
        self, severity: Optional[SeverityLevel] = None, resolved: Optional[bool] = None
    ) -> List[SecurityAlert]:
        """
        Get alerts with optional filtering.

        Args:
            severity: Filter by severity level
            resolved: Filter by resolution status

        Returns:
            List[SecurityAlert]: Filtered alerts
        """
        filtered_alerts = self.alerts

        if severity:
            filtered_alerts = [a for a in filtered_alerts if a.severity == severity]

        if resolved is not None:
            filtered_alerts = [a for a in filtered_alerts if a.resolved == resolved]

        return sorted(filtered_alerts, key=lambda x: x.timestamp, reverse=True)

    def resolve_alert(self, alert_id: str) -> bool:
        """
        Resolve an alert by ID.

        Args:
            alert_id: ID of the alert to resolve

        Returns:
            bool: True if alert was found and resolved
        """
        for alert in self.alerts:
            if alert.alert_id == alert_id and not alert.resolved:
                alert.resolved = True
                alert.resolved_at = datetime.now()
                return True
        return False

    def get_metrics_history(self, hours: int = 24) -> List[Dict[str, Any]]:
        """
        Get historical metrics data.

        Args:
            hours: Number of hours of history to retrieve

        Returns:
            List[Dict[str, Any]]: Historical metrics
        """
        cutoff_time = datetime.now() - timedelta(hours=hours)
        relevant_snapshots = [
            s for s in self.metrics_history if s.timestamp > cutoff_time
        ]

        return [
            {
                "timestamp": s.timestamp.isoformat(),
                "total_tests": s.total_tests,
                "vulnerabilities_detected": s.vulnerabilities_detected,
                "critical_vulnerabilities": s.critical_vulnerabilities,
                "high_vulnerabilities": s.high_vulnerabilities,
                "medium_vulnerabilities": s.medium_vulnerabilities,
                "low_vulnerabilities": s.low_vulnerabilities,
                "average_execution_time": s.average_execution_time,
                "tests_per_second": s.tests_per_second,
                "error_rate": s.error_rate,
            }
            for s in relevant_snapshots
        ]

    def add_callback(self, callback: Callable[[SecurityTestResult], None]):
        """
        Add a callback function to be called when test results are recorded.

        Args:
            callback: Function to call with test results
        """
        self._callbacks.append(callback)

    def remove_callback(self, callback: Callable[[SecurityTestResult], None]):
        """
        Remove a callback function.

        Args:
            callback: Function to remove
        """
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def _notify_callbacks(self, result: SecurityTestResult):
        """Notify all registered callbacks of a test result."""
        for callback in self._callbacks:
            try:
                callback(result)
            except Exception as e:
                # Log callback error but continue with other callbacks
                print(f"Callback error: {e}")

    def export_metrics(self, format: str = "json") -> str:
        """
        Export current metrics in specified format.

        Args:
            format: Export format ('json' or 'csv')

        Returns:
            str: Exported metrics data
        """
        metrics = self.get_current_metrics()

        if format.lower() == "json":
            return json.dumps(metrics, indent=2, default=str)
        elif format.lower() == "csv":
            # Flatten metrics for CSV export
            flat_metrics = self._flatten_dict(metrics)
            headers = list(flat_metrics.keys())
            values = [str(flat_metrics[h]) for h in headers]
            return ",".join(headers) + "\n" + ",".join(values)
        else:
            raise ValueError(f"Unsupported export format: {format}")

    def _flatten_dict(
        self, d: Dict[str, Any], parent_key: str = "", sep: str = "."
    ) -> Dict[str, Any]:
        """Flatten nested dictionary for CSV export."""
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def reset_metrics(self):
        """Reset all monitoring metrics and history."""
        self.test_results.clear()
        self.alerts.clear()
        self.metrics_history.clear()
        self.performance_metrics.clear()

    def __del__(self):
        """Cleanup when monitoring system is destroyed."""
        self.stop_monitoring()
