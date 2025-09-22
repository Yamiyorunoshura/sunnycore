import json
import time
from typing import Dict, List, Any, Optional, Union, Tuple
from datetime import datetime, timezone
import logging
import statistics
import math
from dataclasses import dataclass


@dataclass
class MetricResult:
    """Result of metric calculation"""
    name: str
    value: float
    unit: str
    timestamp: str
    metadata: Dict[str, Any]


class QualityMetricsCalculator:
    """
    Quality Metrics Calculator

    Calculates and aggregates quality metrics for behavioral testing,
    including performance, accuracy, consistency, and reliability measures.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize Metrics Calculator

        Args:
            config: Configuration for metrics calculation
        """
        self.config = config or {}
        self.logger = logging.getLogger(__name__)

        # Default metric weights
        self.default_weights = {
            'accuracy': 0.3,
            'completeness': 0.2,
            'consistency': 0.2,
            'performance': 0.15,
            'reliability': 0.15
        }

        # Metric thresholds
        self.thresholds = self.config.get('thresholds', {
            'accuracy': 0.85,
            'completeness': 0.90,
            'consistency': 0.80,
            'performance': 0.95,
            'reliability': 0.99
        })

    def calculate_composite_score(self, test_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate composite quality score from test results

        Args:
            test_results: List of test result dictionaries

        Returns:
            Composite score results
        """
        try:
            # Calculate individual metrics
            metrics = self._calculate_individual_metrics(test_results)

            # Apply weights
            weights = self.config.get('weights', self.default_weights)
            weighted_score = 0.0

            for metric_name, metric_value in metrics.items():
                weight = weights.get(metric_name, 0.0)
                weighted_score += metric_value * weight

            # Normalize to 0-1 range
            weighted_score = max(0.0, min(1.0, weighted_score))

            # Determine quality level
            quality_level = self._determine_quality_level(weighted_score)

            return {
                'composite_score': round(weighted_score, 3),
                'quality_level': quality_level,
                'individual_metrics': metrics,
                'weights_used': weights,
                'thresholds': self.thresholds,
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'test_count': len(test_results)
            }

        except Exception as e:
            self.logger.error(f"Failed to calculate composite score: {e}")
            return {
                'composite_score': 0.0,
                'quality_level': 'unknown',
                'error': str(e)
            }

    def _calculate_individual_metrics(self, test_results: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        Calculate individual quality metrics

        Args:
            test_results: List of test results

        Returns:
            Dictionary of metric values
        """
        metrics = {}

        try:
            # Accuracy metric
            metrics['accuracy'] = self._calculate_accuracy_metric(test_results)

            # Completeness metric
            metrics['completeness'] = self._calculate_completeness_metric(test_results)

            # Consistency metric
            metrics['consistency'] = self._calculate_consistency_metric(test_results)

            # Performance metric
            metrics['performance'] = self._calculate_performance_metric(test_results)

            # Reliability metric
            metrics['reliability'] = self._calculate_reliability_metric(test_results)

        except Exception as e:
            self.logger.error(f"Failed to calculate individual metrics: {e}")

        return metrics

    def _calculate_accuracy_metric(self, test_results: List[Dict[str, Any]]) -> float:
        """
        Calculate accuracy metric

        Args:
            test_results: List of test results

        Returns:
            Accuracy score (0-1)
        """
        if not test_results:
            return 0.0

        accurate_tests = 0
        total_tests = len(test_results)

        for test_result in test_results:
            # Check if test passed
            if test_result.get('passed', False):
                accurate_tests += 1
            elif 'similarity_score' in test_result:
                # Use similarity score if available
                if test_result['similarity_score'] >= 0.8:  # 80% similarity threshold
                    accurate_tests += 1

        return accurate_tests / total_tests if total_tests > 0 else 0.0

    def _calculate_completeness_metric(self, test_results: List[Dict[str, Any]]) -> float:
        """
        Calculate completeness metric

        Args:
            test_results: List of test results

        Returns:
            Completeness score (0-1)
        """
        if not test_results:
            return 0.0

        completeness_scores = []

        for test_result in test_results:
            score = 0.0

            # Check for required fields
            required_fields = ['test_id', 'actual_output', 'expected_output']
            present_fields = sum(1 for field in required_fields if field in test_result)
            field_completeness = present_fields / len(required_fields)

            # Check output completeness
            actual_output = test_result.get('actual_output', {})
            expected_output = test_result.get('expected_output', {})

            if isinstance(actual_output, dict) and isinstance(expected_output, dict):
                # Calculate field coverage
                expected_fields = set(expected_output.keys())
                actual_fields = set(actual_output.keys())
                field_coverage = len(expected_fields.intersection(actual_fields)) / len(expected_fields) if expected_fields else 1.0
            else:
                field_coverage = 1.0

            # Combine completeness measures
            score = (field_completeness + field_coverage) / 2
            completeness_scores.append(score)

        return statistics.mean(completeness_scores) if completeness_scores else 0.0

    def _calculate_consistency_metric(self, test_results: List[Dict[str, Any]]) -> float:
        """
        Calculate consistency metric

        Args:
            test_results: List of test results

        Returns:
            Consistency score (0-1)
        """
        if not test_results:
            return 0.0

        consistency_scores = []

        for test_result in test_results:
            consistency_score = 1.0  # Default perfect consistency

            # Check for LLM judge consistency if available
            if 'llm_evaluation' in test_result:
                eval_data = test_result['llm_evaluation']
                consistency_score = eval_data.get('consistency_score', 1.0)

            # Check for response variance if multiple runs
            if 'multiple_runs' in test_result:
                runs = test_result['multiple_runs']
                if len(runs) > 1:
                    # Calculate variance in outputs
                    outputs = [run.get('output', '') for run in runs]
                    variance = self._calculate_output_variance(outputs)
                    consistency_score = max(0.0, 1.0 - variance)

            consistency_scores.append(consistency_score)

        return statistics.mean(consistency_scores) if consistency_scores else 0.0

    def _calculate_performance_metric(self, test_results: List[Dict[str, Any]]) -> float:
        """
        Calculate performance metric

        Args:
            test_results: List of test results

        Returns:
            Performance score (0-1)
        """
        if not test_results:
            return 0.0

        performance_scores = []

        for test_result in test_results:
            execution_time = test_result.get('execution_time', 0.0)

            # Score based on execution time (lower is better)
            if execution_time <= 1.0:  # 1 second or less
                score = 1.0
            elif execution_time <= 3.0:  # 3 seconds or less
                score = 0.8
            elif execution_time <= 5.0:  # 5 seconds or less
                score = 0.6
            elif execution_time <= 10.0:  # 10 seconds or less
                score = 0.4
            else:  # Over 10 seconds
                score = 0.2

            performance_scores.append(score)

        return statistics.mean(performance_scores) if performance_scores else 0.0

    def _calculate_reliability_metric(self, test_results: List[Dict[str, Any]]) -> float:
        """
        Calculate reliability metric

        Args:
            test_results: List of test results

        Returns:
            Reliability score (0-1)
        """
        if not test_results:
            return 0.0

        total_tests = len(test_results)
        reliable_tests = 0

        for test_result in test_results:
            # Check for reliability indicators
            is_reliable = True

            # No errors
            if 'error' in test_result:
                is_reliable = False

            # Completed execution
            if not test_result.get('completed', True):
                is_reliable = False

            # Reasonable execution time
            execution_time = test_result.get('execution_time', 0.0)
            if execution_time > 30.0:  # Over 30 seconds
                is_reliable = False

            if is_reliable:
                reliable_tests += 1

        return reliable_tests / total_tests if total_tests > 0 else 0.0

    def _calculate_output_variance(self, outputs: List[str]) -> float:
        """
        Calculate variance between multiple outputs

        Args:
            outputs: List of output strings

        Returns:
            Variance score (0-1, higher means more variance)
        """
        if len(outputs) < 2:
            return 0.0

        # Simple variance calculation based on output length and content
        lengths = [len(output) for output in outputs]
        length_variance = statistics.variance(lengths) if len(lengths) > 1 else 0.0

        # Normalize variance to 0-1 range
        max_variance = 1000.0  # Arbitrary maximum
        normalized_variance = min(length_variance / max_variance, 1.0)

        return normalized_variance

    def _determine_quality_level(self, score: float) -> str:
        """
        Determine quality level based on score

        Args:
            score: Composite score (0-1)

        Returns:
            Quality level string
        """
        if score >= 0.95:
            return 'excellent'
        elif score >= 0.85:
            return 'good'
        elif score >= 0.70:
            return 'fair'
        elif score >= 0.50:
            return 'poor'
        else:
            return 'very_poor'

    def calculate_trend_analysis(self, historical_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate trend analysis from historical data

        Args:
            historical_data: List of historical composite scores

        Returns:
            Trend analysis results
        """
        if len(historical_data) < 2:
            return {
                'trend': 'insufficient_data',
                'slope': 0.0,
                'confidence': 0.0
            }

        try:
            # Extract scores and timestamps
            scores = [data['composite_score'] for data in historical_data]
            timestamps = [datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
                        for data in historical_data]

            # Calculate trend using simple linear regression
            x_values = [(ts - timestamps[0]).total_seconds() / 3600 for ts in timestamps]  # Hours

            slope, intercept = self._calculate_linear_regression(x_values, scores)
            correlation = self._calculate_correlation(x_values, scores)

            # Determine trend direction
            if abs(slope) < 0.001:
                trend = 'stable'
            elif slope > 0:
                trend = 'improving'
            else:
                trend = 'declining'

            # Calculate confidence based on correlation strength
            confidence = abs(correlation)

            return {
                'trend': trend,
                'slope': round(slope, 6),
                'correlation': round(correlation, 3),
                'confidence': round(confidence, 3),
                'recent_score': scores[-1],
                'oldest_score': scores[0],
                'score_change': round(scores[-1] - scores[0], 3)
            }

        except Exception as e:
            self.logger.error(f"Failed to calculate trend analysis: {e}")
            return {
                'trend': 'error',
                'error': str(e)
            }

    def _calculate_linear_regression(self, x_values: List[float], y_values: List[float]) -> Tuple[float, float]:
        """
        Calculate simple linear regression

        Args:
            x_values: Independent variable values
            y_values: Dependent variable values

        Returns:
            Tuple of (slope, intercept)
        """
        if len(x_values) != len(y_values) or len(x_values) < 2:
            return 0.0, 0.0

        n = len(x_values)
        sum_x = sum(x_values)
        sum_y = sum(y_values)
        sum_xy = sum(x * y for x, y in zip(x_values, y_values))
        sum_x2 = sum(x * x for x in x_values)

        # Calculate slope
        numerator = n * sum_xy - sum_x * sum_y
        denominator = n * sum_x2 - sum_x * sum_x

        if denominator == 0:
            return 0.0, sum_y / n

        slope = numerator / denominator
        intercept = (sum_y - slope * sum_x) / n

        return slope, intercept

    def _calculate_correlation(self, x_values: List[float], y_values: List[float]) -> float:
        """
        Calculate Pearson correlation coefficient

        Args:
            x_values: First variable values
            y_values: Second variable values

        Returns:
            Correlation coefficient (-1 to 1)
        """
        if len(x_values) != len(y_values) or len(x_values) < 2:
            return 0.0

        n = len(x_values)
        sum_x = sum(x_values)
        sum_y = sum(y_values)
        sum_xy = sum(x * y for x, y in zip(x_values, y_values))
        sum_x2 = sum(x * x for x in x_values)
        sum_y2 = sum(y * y for y in y_values)

        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y))

        if denominator == 0:
            return 0.0

        return numerator / denominator

    def generate_quality_report(self, composite_score: Dict[str, Any],
                               trend_analysis: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate human-readable quality report

        Args:
            composite_score: Composite score results
            trend_analysis: Optional trend analysis results

        Returns:
            Formatted report string
        """
        report = []
        report.append("=== Quality Metrics Report ===")
        report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
        report.append(f"Test Count: {composite_score.get('test_count', 0)}")
        report.append("")

        # Overall score
        score = composite_score.get('composite_score', 0.0)
        level = composite_score.get('quality_level', 'unknown')
        report.append(f"Composite Quality Score: {score:.3f} ({level.upper()})")
        report.append("")

        # Individual metrics
        report.append("Individual Metrics:")
        individual_metrics = composite_score.get('individual_metrics', {})
        for metric_name, metric_value in individual_metrics.items():
            threshold = self.thresholds.get(metric_name, 0.0)
            status = "✓" if metric_value >= threshold else "✗"
            report.append(f"  {metric_name.capitalize()}: {metric_value:.3f} {status} (threshold: {threshold:.3f})")
        report.append("")

        # Trend analysis
        if trend_analysis and trend_analysis.get('trend') != 'insufficient_data':
            report.append("Trend Analysis:")
            trend = trend_analysis.get('trend', 'unknown')
            score_change = trend_analysis.get('score_change', 0.0)
            report.append(f"  Trend: {trend.upper()}")
            report.append(f"  Score Change: {score_change:+.3f}")
            report.append(f"  Confidence: {trend_analysis.get('confidence', 0.0):.3f}")
            report.append("")

        # Recommendations
        report.append("Recommendations:")
        recommendations = self._generate_recommendations(composite_score)
        for rec in recommendations:
            report.append(f"  • {rec}")

        return "\n".join(report)

    def _generate_recommendations(self, composite_score: Dict[str, Any]) -> List[str]:
        """
        Generate recommendations based on metrics

        Args:
            composite_score: Composite score results

        Returns:
            List of recommendation strings
        """
        recommendations = []
        individual_metrics = composite_score.get('individual_metrics', {})

        # Analyze each metric
        for metric_name, metric_value in individual_metrics.items():
            threshold = self.thresholds.get(metric_name, 0.0)

            if metric_value < threshold:
                if metric_name == 'accuracy':
                    recommendations.append("Improve response accuracy through better prompt engineering or model fine-tuning")
                elif metric_name == 'completeness':
                    recommendations.append("Ensure all required output fields are included in responses")
                elif metric_name == 'consistency':
                    recommendations.append("Implement consistency checks and reduce response variance")
                elif metric_name == 'performance':
                    recommendations.append("Optimize execution time through caching or algorithm improvements")
                elif metric_name == 'reliability':
                    recommendations.append("Improve error handling and system stability")

        # Overall recommendations
        overall_score = composite_score.get('composite_score', 0.0)
        if overall_score < 0.7:
            recommendations.append("Consider comprehensive system review and testing strategy overhaul")

        if not recommendations:
            recommendations.append("System performance is within acceptable thresholds")

        return recommendations