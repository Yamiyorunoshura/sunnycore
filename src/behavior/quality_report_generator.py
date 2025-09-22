import json
import os
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timezone
import logging
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class QualityReportConfig:
    """Configuration for quality report generation"""
    include_charts: bool = True
    include_recommendations: bool = True
    include_trends: bool = True
    include_executive_summary: bool = True
    output_formats: List[str] = None
    chart_resolution: str = "medium"  # low, medium, high

    def __post_init__(self):
        if self.output_formats is None:
            self.output_formats = ["markdown", "html", "json"]


class QualityReportGenerator:
    """
    Quantitative Quality Report Generator

    Generates comprehensive quality reports with quantitative metrics,
    trend analysis, executive summaries, and actionable recommendations.
    """

    def __init__(self, config: Optional[QualityReportConfig] = None):
        """
        Initialize Quality Report Generator

        Args:
            config: Configuration for report generation
        """
        self.config = config or QualityReportConfig()
        self.logger = logging.getLogger(__name__)

        # Report templates
        self.templates = {
            'markdown': self._get_markdown_template(),
            'html': self._get_html_template(),
            'json': self._get_json_template()
        }

    def generate_comprehensive_report(self,
                                    metrics_data: Dict[str, Any],
                                    trend_data: Optional[Dict[str, Any]] = None,
                                    architecture_data: Optional[Dict[str, Any]] = None,
                                    requirement_data: Optional[Dict[str, Any]] = None,
                                    output_dir: str = "reports") -> Dict[str, str]:
        """
        Generate comprehensive quality report

        Args:
            metrics_data: Quality metrics data
            trend_data: Optional trend analysis data
            architecture_data: Optional architecture validation data
            requirement_data: Optional requirement mapping data
            output_dir: Output directory for reports

        Returns:
            Dictionary mapping file formats to file paths
        """
        try:
            # Prepare report data
            report_data = self._prepare_report_data(
                metrics_data, trend_data, architecture_data, requirement_data
            )

            # Generate executive summary
            if self.config.include_executive_summary:
                report_data['executive_summary'] = self._generate_executive_summary(report_data)

            # Generate recommendations
            if self.config.include_recommendations:
                report_data['recommendations'] = self._generate_recommendations(report_data)

            # Generate charts
            if self.config.include_charts:
                report_data['charts'] = self._generate_charts_data(report_data)

            # Create output directory
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

            # Generate reports in different formats
            generated_files = {}
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

            for format_type in self.config.output_formats:
                if format_type in self.templates:
                    filename = f"quality_report_{timestamp}.{format_type}"
                    filepath = output_path / filename

                    report_content = self.templates[format_type](report_data)

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(report_content)

                    generated_files[format_type] = str(filepath)
                    self.logger.info(f"Generated {format_type} report: {filepath}")

            return generated_files

        except Exception as e:
            self.logger.error(f"Failed to generate comprehensive report: {e}")
            raise

    def _prepare_report_data(self,
                            metrics_data: Dict[str, Any],
                            trend_data: Optional[Dict[str, Any]],
                            architecture_data: Optional[Dict[str, Any]],
                            requirement_data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Prepare and normalize report data

        Args:
            metrics_data: Quality metrics data
            trend_data: Optional trend analysis data
            architecture_data: Optional architecture validation data
            requirement_data: Optional requirement mapping data

        Returns:
            Normalized report data dictionary
        """
        report_data = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'metadata': {
                'report_version': '1.0',
                'generated_by': 'QualityReportGenerator',
                'configuration': asdict(self.config)
            }
        }

        # Process metrics data
        report_data['metrics'] = self._process_metrics_data(metrics_data)

        # Process trend data
        if trend_data:
            report_data['trends'] = self._process_trend_data(trend_data)

        # Process architecture data
        if architecture_data:
            report_data['architecture'] = self._process_architecture_data(architecture_data)

        # Process requirement data
        if requirement_data:
            report_data['requirements'] = self._process_requirement_data(requirement_data)

        return report_data

    def _process_metrics_data(self, metrics_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process and normalize metrics data

        Args:
            metrics_data: Raw metrics data

        Returns:
            Processed metrics data
        """
        processed = {
            'composite_score': metrics_data.get('composite_score', 0.0),
            'quality_level': metrics_data.get('quality_level', 'unknown'),
            'individual_metrics': {},
            'thresholds': {},
            'test_count': metrics_data.get('test_count', 0)
        }

        # Process individual metrics
        individual_metrics = metrics_data.get('individual_metrics', {})
        for metric_name, metric_value in individual_metrics.items():
            processed['individual_metrics'][metric_name] = {
                'value': metric_value,
                'status': self._get_metric_status(metric_name, metric_value),
                'trend': 'stable'  # Default, can be updated with trend data
            }

        # Process thresholds
        thresholds = metrics_data.get('thresholds', {})
        for metric_name, threshold_value in thresholds.items():
            processed['thresholds'][metric_name] = threshold_value

        return processed

    def _process_trend_data(self, trend_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process trend analysis data

        Args:
            trend_data: Raw trend data

        Returns:
            Processed trend data
        """
        return {
            'overall_trend': trend_data.get('trend', 'unknown'),
            'slope': trend_data.get('slope', 0.0),
            'correlation': trend_data.get('correlation', 0.0),
            'confidence': trend_data.get('confidence', 0.0),
            'score_change': trend_data.get('score_change', 0.0),
            'recent_score': trend_data.get('recent_score', 0.0),
            'oldest_score': trend_data.get('oldest_score', 0.0)
        }

    def _process_architecture_data(self, architecture_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process architecture validation data

        Args:
            architecture_data: Raw architecture data

        Returns:
            Processed architecture data
        """
        return {
            'overall_f1_score': architecture_data.get('overall_f1_score', 0.0),
            'component_scores': architecture_data.get('component_f1_scores', {}),
            'validation_summary': architecture_data.get('validation_summary', {}),
            'architecture_issues': architecture_data.get('architecture_issues', [])
        }

    def _process_requirement_data(self, requirement_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process requirement mapping data

        Args:
            requirement_data: Raw requirement data

        Returns:
            Processed requirement data
        """
        return {
            'total_requirements': requirement_data.get('total_requirements', 0),
            'covered_requirements': requirement_data.get('covered_requirements', 0),
            'fully_covered_requirements': requirement_data.get('fully_covered_requirements', 0),
            'coverage_percentage': self._calculate_coverage_percentage(requirement_data),
            'coverage_distribution': requirement_data.get('coverage_distribution', {}),
            'requirement_details': requirement_data.get('requirement_mappings', {})
        }

    def _calculate_coverage_percentage(self, requirement_data: Dict[str, Any]) -> float:
        """
        Calculate coverage percentage from requirement data

        Args:
            requirement_data: Requirement data

        Returns:
            Coverage percentage
        """
        total = requirement_data.get('total_requirements', 0)
        covered = requirement_data.get('covered_requirements', 0)

        if total == 0:
            return 0.0

        return covered / total

    def _get_metric_status(self, metric_name: str, metric_value: float) -> str:
        """
        Get status for a metric based on its value

        Args:
            metric_name: Name of the metric
            metric_value: Value of the metric

        Returns:
            Status string
        """
        # Default thresholds
        default_thresholds = {
            'accuracy': 0.85,
            'completeness': 0.90,
            'consistency': 0.80,
            'performance': 0.95,
            'reliability': 0.99
        }

        threshold = default_thresholds.get(metric_name, 0.8)

        if metric_value >= threshold:
            return 'pass'
        elif metric_value >= threshold * 0.8:
            return 'warning'
        else:
            return 'fail'

    def _generate_executive_summary(self, report_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate executive summary

        Args:
            report_data: Report data

        Returns:
            Executive summary dictionary
        """
        metrics = report_data.get('metrics', {})
        trends = report_data.get('trends', {})
        requirements = report_data.get('requirements', {})

        composite_score = metrics.get('composite_score', 0.0)
        quality_level = metrics.get('quality_level', 'unknown')
        coverage_percentage = requirements.get('coverage_percentage', 0.0)
        overall_trend = trends.get('overall_trend', 'stable')

        # Determine overall health
        health_score = self._calculate_health_score(report_data)

        # Generate components
        highlights = self._generate_highlights(report_data)
        concerns = self._generate_concerns(report_data)

        # Generate executive message with computed data
        executive_data = {
            'executive_summary': {
                'overall_health': health_score,
                'quality_assessment': quality_level,
                'key_metrics': {
                    'composite_score': composite_score,
                    'requirement_coverage': coverage_percentage,
                    'trend_direction': overall_trend
                },
                'highlights': highlights,
                'concerns': concerns
            }
        }

        executive_message = self._generate_executive_message(executive_data)

        return {
            'overall_health': health_score,
            'quality_assessment': quality_level,
            'key_metrics': {
                'composite_score': composite_score,
                'requirement_coverage': coverage_percentage,
                'trend_direction': overall_trend
            },
            'highlights': highlights,
            'concerns': concerns,
            'executive_message': executive_message
        }

    def _calculate_health_score(self, report_data: Dict[str, Any]) -> float:
        """
        Calculate overall health score

        Args:
            report_data: Report data

        Returns:
            Health score (0-1)
        """
        metrics = report_data['metrics']
        requirements = report_data.get('requirements', {})

        # Weight factors
        weights = {
            'composite_score': 0.4,
            'requirement_coverage': 0.3,
            'architecture_alignment': 0.2,
            'trend_stability': 0.1
        }

        composite_score = metrics['composite_score']
        coverage_percentage = requirements.get('coverage_percentage', 0.0)

        # Calculate architecture alignment (simplified)
        architecture = report_data.get('architecture', {})
        f1_score = architecture.get('overall_f1_score', 0.0)

        # Calculate trend stability
        trends = report_data.get('trends', {})
        trend_score = 1.0 if trends.get('overall_trend') == 'stable' else 0.7

        # Calculate weighted health score
        health_score = (
            composite_score * weights['composite_score'] +
            coverage_percentage * weights['requirement_coverage'] +
            f1_score * weights['architecture_alignment'] +
            trend_score * weights['trend_stability']
        )

        return round(health_score, 3)

    def _generate_highlights(self, report_data: Dict[str, Any]) -> List[str]:
        """
        Generate positive highlights

        Args:
            report_data: Report data

        Returns:
            List of highlight strings
        """
        highlights = []
        metrics = report_data['metrics']
        requirements = report_data.get('requirements', {})

        # Check for strong metrics
        if metrics['composite_score'] >= 0.9:
            highlights.append(f"Excellent overall quality score: {metrics['composite_score']:.1%}")

        if requirements.get('coverage_percentage', 0.0) >= 0.95:
            highlights.append(f"Outstanding requirement coverage: {requirements['coverage_percentage']:.1%}")

        # Check for good individual metrics
        for metric_name, metric_info in metrics['individual_metrics'].items():
            if metric_info['value'] >= 0.95:
                highlights.append(f"Strong {metric_name} performance: {metric_info['value']:.1%}")

        return highlights

    def _generate_concerns(self, report_data: Dict[str, Any]) -> List[str]:
        """
        Generate concerns and issues

        Args:
            report_data: Report data

        Returns:
            List of concern strings
        """
        concerns = []
        metrics = report_data['metrics']
        trends = report_data.get('trends', {})

        # Check for declining trends
        if trends.get('overall_trend') == 'declining':
            concerns.append("Quality metrics showing declining trend")

        # Check for poor individual metrics
        for metric_name, metric_info in metrics['individual_metrics'].items():
            if metric_info['value'] < 0.7:
                concerns.append(f"Low {metric_name} score: {metric_info['value']:.1%}")

        # Check for low requirement coverage
        requirements = report_data.get('requirements', {})
        coverage_percentage = requirements.get('coverage_percentage', 0.0)
        if coverage_percentage < 0.8:
            concerns.append(f"Insufficient requirement coverage: {coverage_percentage:.1%}")

        return concerns

    def _generate_executive_message(self, report_data: Dict[str, Any]) -> str:
        """
        Generate executive summary message

        Args:
            report_data: Report data

        Returns:
            Executive message string
        """
        health_score = report_data.get('executive_summary', {}).get('overall_health', 0.0)
        quality_level = report_data.get('metrics', {}).get('quality_level', 'unknown')
        trend = report_data.get('trends', {}).get('overall_trend', 'stable')

        if health_score >= 0.9:
            message = f"System demonstrates excellent quality with {health_score:.1%} overall health. {quality_level.upper()} quality level maintained with {trend} trend."
        elif health_score >= 0.8:
            message = f"System shows good quality performance with {health_score:.1%} overall health. {quality_level.upper()} quality level with {trend} trend. Some areas may need attention."
        elif health_score >= 0.7:
            message = f"System quality is acceptable but requires attention. {health_score:.1%} overall health with {quality_level.upper()} quality level. Address identified concerns to prevent degradation."
        else:
            message = f"System quality requires immediate attention. {health_score:.1%} overall health with concerning {trend} trend. Implement quality improvement initiatives urgently."

        return message

    def _generate_recommendations(self, report_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate actionable recommendations

        Args:
            report_data: Report data

        Returns:
            List of recommendation dictionaries
        """
        recommendations = []
        metrics = report_data['metrics']
        requirements = report_data.get('requirements', {})
        architecture = report_data.get('architecture', {})

        # Analyze metrics for recommendations
        for metric_name, metric_info in metrics['individual_metrics'].items():
            if metric_info['status'] == 'fail':
                recommendations.append({
                    'category': 'quality_improvement',
                    'priority': 'high',
                    'metric': metric_name,
                    'issue': f"Low {metric_name} score: {metric_info['value']:.1%}",
                    'recommendation': self._get_metric_recommendation(metric_name),
                    'expected_impact': 'medium'
                })

        # Analyze requirement coverage
        coverage_percentage = requirements.get('coverage_percentage', 0.0)
        if coverage_percentage < 0.9:
            recommendations.append({
                'category': 'requirement_coverage',
                'priority': 'high',
                'metric': 'requirement_coverage',
                'issue': f"Low requirement coverage: {coverage_percentage:.1%}",
                'recommendation': "Increase test coverage for uncovered requirements",
                'expected_impact': 'high'
            })

        # Analyze architecture alignment
        f1_score = architecture.get('overall_f1_score', 0.0)
        if f1_score < 0.9:
            recommendations.append({
                'category': 'architecture_alignment',
                'priority': 'medium',
                'metric': 'architecture_f1_score',
                'issue': f"Low architecture F1 score: {f1_score:.3f}",
                'recommendation': "Improve component alignment with target architecture",
                'expected_impact': 'medium'
            })

        return recommendations

    def _get_metric_recommendation(self, metric_name: str) -> str:
        """
        Get specific recommendation for a metric

        Args:
            metric_name: Name of the metric

        Returns:
            Recommendation string
        """
        recommendations = {
            'accuracy': "Improve test case accuracy through better prompt engineering and model fine-tuning",
            'completeness': "Ensure all required output fields are included in responses and tests",
            'consistency': "Implement consistency checks and reduce response variance through standardized approaches",
            'performance': "Optimize execution time through caching, algorithm improvements, and resource management",
            'reliability': "Improve error handling, timeout management, and system stability"
        }

        return recommendations.get(metric_name, "Review and improve this metric area")

    def _generate_charts_data(self, report_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate chart data for visualization

        Args:
            report_data: Report data

        Returns:
            Chart data dictionary
        """
        charts_data = {}

        # Metrics radar chart
        charts_data['metrics_radar'] = self._generate_metrics_radar_data(report_data)

        # Trend line chart
        charts_data['trend_line'] = self._generate_trend_line_data(report_data)

        # Coverage pie chart
        charts_data['coverage_pie'] = self._generate_coverage_pie_data(report_data)

        # Component F1 scores bar chart
        charts_data['component_f1_bars'] = self._generate_component_f1_bars_data(report_data)

        return charts_data

    def _generate_metrics_radar_data(self, report_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate radar chart data for metrics"""
        metrics = report_data['metrics']
        individual_metrics = metrics['individual_metrics']

        labels = []
        values = []
        thresholds = []

        for metric_name, metric_info in individual_metrics.items():
            labels.append(metric_name.capitalize())
            values.append(metric_info['value'])
            thresholds.append(metrics['thresholds'].get(metric_name, 0.8))

        return {
            'type': 'radar',
            'title': 'Quality Metrics Comparison',
            'labels': labels,
            'datasets': [
                {
                    'label': 'Actual Values',
                    'data': values,
                    'color': 'rgba(54, 162, 235, 0.8)'
                },
                {
                    'label': 'Thresholds',
                    'data': thresholds,
                    'color': 'rgba(255, 99, 132, 0.8)'
                }
            ]
        }

    def _generate_trend_line_data(self, report_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate trend line chart data"""
        # This would normally use historical data
        # For now, generate sample trend data
        return {
            'type': 'line',
            'title': 'Quality Trend Analysis',
            'labels': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            'datasets': [
                {
                    'label': 'Composite Score',
                    'data': [0.75, 0.78, 0.82, 0.85],
                    'color': 'rgba(75, 192, 192, 0.8)'
                }
            ]
        }

    def _generate_coverage_pie_data(self, report_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate coverage pie chart data"""
        requirements = report_data.get('requirements', {})
        distribution = requirements.get('coverage_distribution', {})

        labels = []
        values = []
        colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']

        for label, value in distribution.items():
            labels.append(label)
            values.append(value)

        return {
            'type': 'pie',
            'title': 'Requirement Coverage Distribution',
            'labels': labels,
            'datasets': [
                {
                    'data': values,
                    'colors': colors[:len(labels)]
                }
            ]
        }

    def _generate_component_f1_bars_data(self, report_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate component F1 scores bar chart data"""
        architecture = report_data.get('architecture', {})
        component_scores = architecture.get('component_scores', {})

        labels = []
        values = []

        for component, score in component_scores.items():
            labels.append(component)
            values.append(score)

        return {
            'type': 'bar',
            'title': 'Component Architecture F1 Scores',
            'labels': labels,
            'datasets': [
                {
                    'label': 'F1 Score',
                    'data': values,
                    'color': 'rgba(153, 102, 255, 0.8)'
                }
            ]
        }

    def _get_markdown_template(self):
        """Get markdown template function"""
        def template(report_data: Dict[str, Any]) -> str:
            """Generate markdown report"""

            executive_summary = report_data.get('executive_summary', {})
            metrics = report_data['metrics']
            trends = report_data.get('trends', {})
            requirements = report_data.get('requirements', {})
            architecture = report_data.get('architecture', {})
            recommendations = report_data.get('recommendations', [])

            report_lines = []
            report_lines.append("# Quality Report")
            report_lines.append(f"**Generated:** {report_data['timestamp']}")
            report_lines.append(f"**Version:** {report_data['metadata']['report_version']}")
            report_lines.append("")

            # Executive Summary
            if executive_summary:
                report_lines.append("## Executive Summary")
                report_lines.append(f"**Overall Health:** {executive_summary['overall_health']:.1%}")
                report_lines.append(f"**Quality Assessment:** {executive_summary['quality_assessment'].upper()}")
                report_lines.append("")
                report_lines.append(f"{executive_summary['executive_message']}")
                report_lines.append("")

                # Highlights
                if executive_summary.get('highlights'):
                    report_lines.append("### Highlights")
                    for highlight in executive_summary['highlights']:
                        report_lines.append(f"- {highlight}")
                    report_lines.append("")

                # Concerns
                if executive_summary.get('concerns'):
                    report_lines.append("### Concerns")
                    for concern in executive_summary['concerns']:
                        report_lines.append(f"- {concern}")
                    report_lines.append("")

            # Quality Metrics
            report_lines.append("## Quality Metrics")
            report_lines.append(f"**Composite Score:** {metrics['composite_score']:.3f} ({metrics['quality_level'].upper()})")
            report_lines.append(f"**Test Count:** {metrics['test_count']}")
            report_lines.append("")

            report_lines.append("### Individual Metrics")
            for metric_name, metric_info in metrics['individual_metrics'].items():
                status_icon = "✓" if metric_info['status'] == 'pass' else "⚠️" if metric_info['status'] == 'warning' else "✗"
                threshold = metrics['thresholds'].get(metric_name, 0.8)
                report_lines.append(f"- {status_icon} **{metric_name.capitalize()}:** {metric_info['value']:.3f} (threshold: {threshold:.3f})")
            report_lines.append("")

            # Trend Analysis
            if trends:
                report_lines.append("## Trend Analysis")
                report_lines.append(f"**Overall Trend:** {trends['overall_trend'].upper()}")
                report_lines.append(f"**Trend Slope:** {trends['slope']:.6f}")
                report_lines.append(f"**Confidence:** {trends['confidence']:.3f}")
                report_lines.append(f"**Score Change:** {trends['score_change']:+.3f}")
                report_lines.append("")

            # Requirement Coverage
            if requirements:
                report_lines.append("## Requirement Coverage")
                coverage_percentage = requirements.get('coverage_percentage', 0.0)
                report_lines.append(f"**Total Requirements:** {requirements['total_requirements']}")
                report_lines.append(f"**Covered Requirements:** {requirements['covered_requirements']}")
                report_lines.append(f"**Fully Covered:** {requirements['fully_covered_requirements']}")
                report_lines.append(f"**Coverage Percentage:** {coverage_percentage:.1%}")
                report_lines.append("")

                # Coverage Distribution
                distribution = requirements.get('coverage_distribution', {})
                if distribution:
                    report_lines.append("### Coverage Distribution")
                    for range_label, count in distribution.items():
                        report_lines.append(f"- **{range_label}:** {count} requirements")
                    report_lines.append("")

            # Architecture Alignment
            if architecture:
                report_lines.append("## Architecture Alignment")
                report_lines.append(f"**Overall F1 Score:** {architecture['overall_f1_score']:.3f}")
                report_lines.append("")

                # Component Scores
                component_scores = architecture.get('component_scores', {})
                if component_scores:
                    report_lines.append("### Component F1 Scores")
                    for component, score in component_scores.items():
                        status = "✓" if score >= 0.9 else "⚠️" if score >= 0.8 else "✗"
                        report_lines.append(f"- {status} **{component}:** {score:.3f}")
                    report_lines.append("")

            # Recommendations
            if recommendations:
                report_lines.append("## Recommendations")
                for rec in recommendations:
                    priority_icon = "🔴" if rec['priority'] == 'high' else "🟡" if rec['priority'] == 'medium' else "🟢"
                    report_lines.append(f"### {priority_icon} {rec['category'].replace('_', ' ').title()}")
                    report_lines.append(f"**Issue:** {rec['issue']}")
                    report_lines.append(f"**Recommendation:** {rec['recommendation']}")
                    report_lines.append(f"**Expected Impact:** {rec['expected_impact']}")
                    report_lines.append("")

            return "\n".join(report_lines)

        return template

    def _get_html_template(self):
        """Get HTML template function"""
        def template(report_data: Dict[str, Any]) -> str:
            """Generate HTML report"""

            # This is a simplified HTML template
            # In a real implementation, this would generate a more comprehensive HTML report
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quality Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
        .section {{ margin: 20px 0; }}
        .metric {{ margin: 10px 0; }}
        .pass {{ color: green; }}
        .warning {{ color: orange; }}
        .fail {{ color: red; }}
        .recommendation {{ background-color: #f9f9f9; padding: 15px; margin: 10px 0; border-left: 4px solid #007cba; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Quality Report</h1>
        <p>Generated: {report_data['timestamp']}</p>
        <p>Version: {report_data['metadata']['report_version']}</p>
    </div>

    <div class="section">
        <h2>Executive Summary</h2>
        <p>Overall Health: {report_data.get('executive_summary', {}).get('overall_health', 0):.1%}</p>
        <p>Quality Assessment: {report_data['metrics']['quality_level'].upper()}</p>
    </div>

    <div class="section">
        <h2>Quality Metrics</h2>
        <p>Composite Score: {report_data['metrics']['composite_score']:.3f}</p>
        <p>Test Count: {report_data['metrics']['test_count']}</p>
    </div>

    <!-- Additional sections would be generated here -->

</body>
</html>
            """

            return html_content.strip()

        return template

    def _get_json_template(self):
        """Get JSON template function"""
        def template(report_data: Dict[str, Any]) -> str:
            """Generate JSON report"""
            return json.dumps(report_data, indent=2, ensure_ascii=False)

        return template