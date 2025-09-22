"""
Report Generator - Transformation Impact Assessment Reports

Generates comprehensive transformation impact assessment reports with
visualizations, statistics, and actionable insights.
"""

import json
import time
import logging
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import csv
from collections import defaultdict

from .transformation_strategies import TransformationResult
from .robustness_engine import TestExecutionResult
from .transformation_validator import ValidationResult
from .stability_analyzer import StabilityMetrics


@dataclass
class ReportConfig:
    """Configuration for report generation"""
    include_visualizations: bool = True
    include_detailed_metrics: bool = True
    include_recommendations: bool = True
    export_formats: List[str] = None
    report_title: str = "Transformation Impact Assessment Report"
    author: str = "Robustness Testing System"

    def __post_init__(self):
        if self.export_formats is None:
            self.export_formats = ["json", "markdown", "csv"]


@dataclass
class ReportSection:
    """Represents a section in the report"""
    title: str
    content: str
    metrics: Dict[str, Any]
    visualizations: List[Dict[str, Any]] = None

    def __post_init__(self):
        if self.visualizations is None:
            self.visualizations = []


class ReportGenerator:
    """
    Report Generator for Transformation Impact Assessment

    Generates comprehensive reports with statistics, visualizations,
    and actionable insights for transformation impact assessment.
    """

    def __init__(self, config: ReportConfig):
        """
        Initialize Report Generator

        Args:
            config: Configuration for report generation
        """
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

        # Report templates
        self.templates = self._initialize_templates()

        # Statistics calculators
        self.stats_calculators = self._initialize_stats_calculators()

        self.logger.info("Report Generator initialized")

    def _initialize_templates(self) -> Dict[str, str]:
        """Initialize report templates"""
        return {
            "executive_summary": """
# Executive Summary

This report presents a comprehensive assessment of transformation impact on system robustness.
The analysis covers {total_tests} test executions with {total_transformations} transformations applied.

## Key Findings

- **Overall Consistency Score**: {overall_consistency:.2f}
- **Performance Metrics**: {performance_summary}
- **Stability Assessment**: {stability_summary}
- **Validation Results**: {validation_summary}

## Recommendations

{recommendations}
""",
            "detailed_analysis": """
# Detailed Analysis

## Transformation Effectiveness

{transformation_effectiveness}

## Performance Analysis

{performance_analysis}

## Validation Results

{validation_analysis}

## Stability Assessment

{stability_analysis}
""",
            "methodology": """
# Methodology

## Test Execution

The robustness testing framework applies multiple transformation strategies to input text
and evaluates the impact on key conclusions and system stability.

## Transformation Strategies

{transformation_strategies}

## Validation Methods

{validation_methods}

## Metrics Calculation

{metrics_calculation}
"""
        }

    def _initialize_stats_calculators(self) -> Dict[str, Any]:
        """Initialize statistical calculation methods"""
        return {
            "mean": lambda x: sum(x) / len(x) if x else 0.0,
            "median": self._calculate_median,
            "std_dev": self._calculate_std_dev,
            "min": lambda x: min(x) if x else 0.0,
            "max": lambda x: max(x) if x else 0.0,
            "percentile": self._calculate_percentile
        }

    def generate_comprehensive_report(self, test_results: List[TestExecutionResult],
                                   validation_results: Dict[str, List[ValidationResult]],
                                   stability_metrics: Optional[StabilityMetrics] = None,
                                   output_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate comprehensive transformation impact assessment report

        Args:
            test_results: List of test execution results
            validation_results: Validation results organized by test_id
            stability_metrics: Optional stability metrics
            output_path: Optional output path for saving report

        Returns:
            Complete report data structure
        """
        start_time = time.time()

        try:
            self.logger.info("Generating comprehensive report for %d test results", len(test_results))

            # Calculate aggregate statistics
            aggregate_stats = self._calculate_aggregate_statistics(test_results)

            # Generate report sections
            executive_summary = self._generate_executive_summary(test_results, aggregate_stats, stability_metrics)
            detailed_analysis = self._generate_detailed_analysis(test_results, validation_results, stability_metrics)
            methodology_section = self._generate_methodology_section()
            recommendations = self._generate_recommendations(test_results, validation_results, stability_metrics)

            # Compile complete report
            report = {
                "metadata": {
                    "report_title": self.config.report_title,
                    "author": self.config.author,
                    "generation_timestamp": datetime.now(timezone.utc).isoformat(),
                    "total_tests": len(test_results),
                    "total_transformations": sum(len(result.transformation_results) for result in test_results),
                    "generation_time_seconds": time.time() - start_time
                },
                "executive_summary": executive_summary,
                "detailed_analysis": detailed_analysis,
                "methodology": methodology_section,
                "recommendations": recommendations,
                "aggregate_statistics": aggregate_stats,
                "individual_results": self._compile_individual_results(test_results, validation_results),
                "appendices": self._generate_appendices(test_results, validation_results)
            }

            # Export report if requested
            if output_path:
                self._export_report(report, output_path)

            self.logger.info("Comprehensive report generated successfully")
            return report

        except Exception as e:
            self.logger.error("Error generating comprehensive report: %s", e)
            raise

    def _calculate_aggregate_statistics(self, test_results: List[TestExecutionResult]) -> Dict[str, Any]:
        """Calculate aggregate statistics from test results"""
        if not test_results:
            return {}

        # Extract metrics from all test results
        consistency_scores = [result.consistency_score for result in test_results]
        execution_times = [result.execution_time for result in test_results]
        transformation_counts = [len(result.transformation_results) for result in test_results]

        # Calculate performance metrics
        all_performance_metrics = []
        for result in test_results:
            all_performance_metrics.extend([
                result.performance_metrics.get("total_processing_time", 0),
                result.performance_metrics.get("average_processing_time", 0),
                result.performance_metrics.get("max_processing_time", 0)
            ])

        # Aggregate statistics
        stats = {
            "consistency": {
                "mean": self.stats_calculators["mean"](consistency_scores),
                "median": self.stats_calculators["median"](consistency_scores),
                "std_dev": self.stats_calculators["std_dev"](consistency_scores),
                "min": self.stats_calculators["min"](consistency_scores),
                "max": self.stats_calculators["max"](consistency_scores),
                "percentile_95": self.stats_calculators["percentile"](consistency_scores, 95)
            },
            "performance": {
                "total_execution_time": sum(execution_times),
                "average_execution_time": self.stats_calculators["mean"](execution_times),
                "max_execution_time": self.stats_calculators["max"](execution_times),
                "transformation_efficiency": self.stats_calculators["mean"](transformation_counts)
            },
            "summary": {
                "total_tests": len(test_results),
                "successful_tests": sum(1 for result in test_results if result.success_criteria_met),
                "success_rate": sum(1 for result in test_results if result.success_criteria_met) / len(test_results) if test_results else 0.0,
                "average_consistency": self.stats_calculators["mean"](consistency_scores)
            }
        }

        return stats

    def _generate_executive_summary(self, test_results: List[TestExecutionResult],
                                 aggregate_stats: Dict[str, Any],
                                 stability_metrics: Optional[StabilityMetrics] = None) -> Dict[str, Any]:
        """Generate executive summary section"""
        overall_consistency = aggregate_stats["summary"]["average_consistency"]
        success_rate = aggregate_stats["summary"]["success_rate"]

        # Performance summary
        performance_summary = f"Average execution time: {aggregate_stats['performance']['average_execution_time']:.3f}s, " \
                             f"Success rate: {success_rate:.1%}"

        # Stability summary
        if stability_metrics:
            stability_summary = f"Overall stability: {stability_metrics.overall_stability:.2f}, " \
                              f"Decision consistency: {stability_metrics.decision_consistency:.2f}"
        else:
            stability_summary = "Stability analysis not available"

        # Validation summary
        validation_summary = "Validation completed for all transformations"

        # Recommendations preview
        recommendations_preview = "See detailed recommendations section"

        return {
            "title": "Executive Summary",
            "overall_consistency": overall_consistency,
            "performance_summary": performance_summary,
            "stability_summary": stability_summary,
            "validation_summary": validation_summary,
            "recommendations_preview": recommendations_preview,
            "key_metrics": {
                "total_tests": len(test_results),
                "success_rate": success_rate,
                "overall_consistency": overall_consistency,
                "average_execution_time": aggregate_stats["performance"]["average_execution_time"]
            }
        }

    def _generate_detailed_analysis(self, test_results: List[TestExecutionResult],
                                 validation_results: Dict[str, List[ValidationResult]],
                                 stability_metrics: Optional[StabilityMetrics] = None) -> Dict[str, Any]:
        """Generate detailed analysis section"""
        # Transformation effectiveness analysis
        transformation_effectiveness = self._analyze_transformation_effectiveness(test_results)

        # Performance analysis
        performance_analysis = self._analyze_performance(test_results)

        # Validation analysis
        validation_analysis = self._analyze_validation_results(validation_results)

        # Stability analysis
        stability_analysis = self._analyze_stability(stability_metrics)

        return {
            "title": "Detailed Analysis",
            "transformation_effectiveness": transformation_effectiveness,
            "performance_analysis": performance_analysis,
            "validation_analysis": validation_analysis,
            "stability_analysis": stability_analysis,
            "detailed_metrics": self._calculate_detailed_metrics(test_results, validation_results)
        }

    def _analyze_transformation_effectiveness(self, test_results: List[TestExecutionResult]) -> Dict[str, Any]:
        """Analyze transformation effectiveness"""
        strategy_stats = defaultdict(lambda: {"count": 0, "avg_confidence": 0.0, "success_rate": 0.0})

        for result in test_results:
            for transform_result in result.transformation_results:
                strategy_name = transform_result.transformation_type
                strategy_stats[strategy_name]["count"] += 1
                strategy_stats[strategy_name]["avg_confidence"] += transform_result.confidence_score

        # Calculate averages
        for strategy, stats in strategy_stats.items():
            if stats["count"] > 0:
                stats["avg_confidence"] /= stats["count"]

        return dict(strategy_stats)

    def _analyze_performance(self, test_results: List[TestExecutionResult]) -> Dict[str, Any]:
        """Analyze performance metrics"""
        execution_times = [result.execution_time for result in test_results]
        processing_times = []

        for result in test_results:
            for transform_result in result.transformation_results:
                processing_times.append(transform_result.processing_time)

        return {
            "execution_time_stats": {
                "mean": self.stats_calculators["mean"](execution_times),
                "median": self.stats_calculators["median"](execution_times),
                "std_dev": self.stats_calculators["std_dev"](execution_times),
                "max": self.stats_calculators["max"](execution_times)
            },
            "processing_time_stats": {
                "mean": self.stats_calculators["mean"](processing_times),
                "median": self.stats_calculators["median"](processing_times),
                "std_dev": self.stats_calculators["std_dev"](processing_times),
                "max": self.stats_calculators["max"](processing_times)
            },
            "performance_threshold_analysis": {
                "below_500ms": sum(1 for t in processing_times if t < 0.5),
                "above_500ms": sum(1 for t in processing_times if t >= 0.5),
                "below_threshold_percentage": sum(1 for t in processing_times if t < 0.5) / len(processing_times) * 100 if processing_times else 0.0
            }
        }

    def _analyze_validation_results(self, validation_results: Dict[str, List[ValidationResult]]) -> Dict[str, Any]:
        """Analyze validation results"""
        validation_stats = defaultdict(lambda: {"count": 0, "passed": 0, "avg_score": 0.0})

        for test_id, results in validation_results.items():
            for result in results:
                validation_type = result.validation_type
                validation_stats[validation_type]["count"] += 1
                validation_stats[validation_type]["avg_score"] += result.score
                if result.passed:
                    validation_stats[validation_type]["passed"] += 1

        # Calculate averages and success rates
        for validation_type, stats in validation_stats.items():
            if stats["count"] > 0:
                stats["avg_score"] /= stats["count"]
                stats["success_rate"] = stats["passed"] / stats["count"] * 100

        return dict(validation_stats)

    def _analyze_stability(self, stability_metrics: Optional[StabilityMetrics]) -> Dict[str, Any]:
        """Analyze stability metrics"""
        if not stability_metrics:
            return {"message": "Stability analysis not performed"}

        return {
            "overall_stability": stability_metrics.overall_stability,
            "decision_consistency": stability_metrics.decision_consistency,
            "conclusion_stability": stability_metrics.conclusion_stability,
            "key_term_preservation": stability_metrics.key_term_preservation,
            "structural_stability": stability_metrics.structural_stability,
            "confidence_interval": stability_metrics.confidence_interval,
            "sample_size": stability_metrics.sample_size,
            "stability_assessment": "Good" if stability_metrics.overall_stability >= 0.85 else "Needs Improvement"
        }

    def _generate_methodology_section(self) -> Dict[str, Any]:
        """Generate methodology section"""
        transformation_strategies = [
            "Synonym Replacement: Replaces words with synonyms while preserving meaning",
            "Paragraph Reordering: Reorders paragraphs while maintaining logical flow",
            "Irrelevant Content Injection: Adds neutral content without affecting key conclusions"
        ]

        validation_methods = [
            "Semantic Similarity: Ensures transformations preserve semantic meaning",
            "Structural Integrity: Validates text structure and coherence",
            "Key Term Preservation: Ensures important terms are maintained"
        ]

        metrics_calculation = [
            "Consistency Score: Measures conclusion preservation across transformations",
            "Performance Metrics: Tracks processing time and efficiency",
            "Validation Scores: Comprehensive validation across multiple dimensions"
        ]

        return {
            "title": "Methodology",
            "transformation_strategies": transformation_strategies,
            "validation_methods": validation_methods,
            "metrics_calculation": metrics_calculation
        }

    def _generate_recommendations(self, test_results: List[TestExecutionResult],
                                validation_results: Dict[str, List[ValidationResult]],
                                stability_metrics: Optional[StabilityMetrics]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []

        # Analyze overall performance
        avg_consistency = self.stats_calculators["mean"]([result.consistency_score for result in test_results])
        success_rate = sum(1 for result in test_results if result.success_criteria_met) / len(test_results) if test_results else 0.0

        # Performance recommendations
        slow_tests = [result for result in test_results if result.execution_time > 1.0]
        if slow_tests:
            recommendations.append(f"Consider optimizing performance for {len(slow_tests)} slow tests (>1s execution time)")

        # Consistency recommendations
        if avg_consistency < 0.9:
            recommendations.append("Focus on improving transformation consistency to meet the 90% target")

        # Validation recommendations
        failed_validations = []
        for test_id, results in validation_results.items():
            failed_validations.extend([result for result in results if not result.passed])

        if failed_validations:
            failed_by_type = defaultdict(int)
            for result in failed_validations:
                failed_by_type[result.validation_type] += 1

            most_failed = max(failed_by_type.items(), key=lambda x: x[1])
            recommendations.append(f"Improve {most_failed[0]} validation (failed {most_failed[1]} times)")

        # Stability recommendations
        if stability_metrics and stability_metrics.overall_stability < 0.85:
            recommendations.append("Enhance stability analysis to improve decision consistency")

        # Success rate recommendations
        if success_rate < 0.8:
            recommendations.append("Review transformation strategies to improve success rate")

        if not recommendations:
            recommendations.append("System is performing well within acceptable parameters")

        return recommendations

    def _calculate_detailed_metrics(self, test_results: List[TestExecutionResult],
                                  validation_results: Dict[str, List[ValidationResult]]) -> Dict[str, Any]:
        """Calculate detailed metrics for analysis"""
        metrics = {
            "transformation_metrics": defaultdict(list),
            "validation_metrics": defaultdict(list),
            "performance_metrics": defaultdict(list)
        }

        # Collect transformation metrics
        for result in test_results:
            for transform_result in result.transformation_results:
                metrics["transformation_metrics"][transform_result.transformation_type].append({
                    "confidence": transform_result.confidence_score,
                    "processing_time": transform_result.processing_time,
                    "changes_made": len(transform_result.changes_made)
                })

        # Collect validation metrics
        for test_id, results in validation_results.items():
            for result in results:
                metrics["validation_metrics"][result.validation_type].append({
                    "score": result.score,
                    "passed": result.passed,
                    "processing_time": result.processing_time
                })

        # Collect performance metrics
        for result in test_results:
            metrics["performance_metrics"]["execution_time"].append(result.execution_time)
            for transform_result in result.transformation_results:
                metrics["performance_metrics"]["transformation_time"].append(transform_result.processing_time)

        return dict(metrics)

    def _compile_individual_results(self, test_results: List[TestExecutionResult],
                                   validation_results: Dict[str, List[ValidationResult]]) -> List[Dict[str, Any]]:
        """Compile individual test results"""
        individual_results = []

        for result in test_results:
            test_result = {
                "test_id": result.test_id,
                "timestamp": result.timestamp if isinstance(result.timestamp, str) else result.timestamp.isoformat(),
                "consistency_score": result.consistency_score,
                "success_criteria_met": result.success_criteria_met,
                "execution_time": result.execution_time,
                "transformation_count": len(result.transformation_results),
                "transformations": [
                    {
                        "type": transform_result.transformation_type,
                        "confidence": transform_result.confidence_score,
                        "processing_time": transform_result.processing_time,
                        "changes_made": len(transform_result.changes_made)
                    }
                    for transform_result in result.transformation_results
                ],
                "validation_results": validation_results.get(result.test_id, [])
            }

            individual_results.append(test_result)

        return individual_results

    def _generate_appendices(self, test_results: List[TestExecutionResult],
                            validation_results: Dict[str, List[ValidationResult]]) -> Dict[str, Any]:
        """Generate report appendices"""
        return {
            "raw_data": {
                "test_results_count": len(test_results),
                "validation_results_count": sum(len(results) for results in validation_results.values()),
                "total_transformations": sum(len(result.transformation_results) for result in test_results)
            },
            "glossary": {
                "Consistency Score": "Measure of how well key conclusions are preserved across transformations",
                "Transformation Strategy": "Method used to modify input text while testing robustness",
                "Validation Result": "Result of validating transformation quality and semantic preservation",
                "Stability Metrics": "Measures of decision stability across multiple transformations"
            }
        }

    def _export_report(self, report: Dict[str, Any], output_path: str):
        """Export report to specified formats"""
        output_path_obj = Path(output_path)

        for format_name in self.config.export_formats:
            try:
                if format_name.lower() == "json":
                    json_path = output_path_obj.with_suffix('.json')
                    with open(json_path, 'w', encoding='utf-8') as f:
                        json.dump(report, f, indent=2, default=str)
                    self.logger.info("Exported JSON report to %s", json_path)

                elif format_name.lower() == "markdown":
                    md_path = output_path_obj.with_suffix('.md')
                    self._export_markdown(report, md_path)
                    self.logger.info("Exported Markdown report to %s", md_path)

                elif format_name.lower() == "csv":
                    csv_path = output_path_obj.with_suffix('.csv')
                    self._export_csv(report, csv_path)
                    self.logger.info("Exported CSV report to %s", csv_path)

            except Exception as e:
                self.logger.error("Error exporting %s report: %s", format_name, e)

    def _export_markdown(self, report: Dict[str, Any], output_path: Path):
        """Export report as Markdown"""
        md_content = f"""# {report['metadata']['report_title']}

**Generated:** {report['metadata']['generation_timestamp']}
**Author:** {report['metadata']['author']}
**Total Tests:** {report['metadata']['total_tests']}

## Executive Summary

- **Overall Consistency:** {report['executive_summary']['overall_consistency']:.2f}
- **Success Rate:** {report['executive_summary']['key_metrics']['success_rate']:.1%}
- **Average Execution Time:** {report['executive_summary']['key_metrics']['average_execution_time']:.3f}s

## Key Findings

{report['executive_summary']['performance_summary']}

{report['executive_summary']['stability_summary']}

## Recommendations

{chr(10).join(f'- {rec}' for rec in self._generate_recommendations([], {}, None))}

## Detailed Results

{len(report['individual_results'])} test results were analyzed. See attached JSON file for complete data.
"""

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

    def _export_csv(self, report: Dict[str, Any], output_path: Path):
        """Export report as CSV"""
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Test ID', 'Timestamp', 'Consistency Score', 'Success', 'Execution Time', 'Transformations'])

            for result in report['individual_results']:
                writer.writerow([
                    result['test_id'],
                    result['timestamp'],
                    result['consistency_score'],
                    result['success_criteria_met'],
                    result['execution_time'],
                    len(result['transformations'])
                ])

    def _calculate_median(self, data: List[float]) -> float:
        """Calculate median of a list"""
        if not data:
            return 0.0
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]

    def _calculate_std_dev(self, data: List[float]) -> float:
        """Calculate standard deviation"""
        if not data or len(data) < 2:
            return 0.0
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
        return variance ** 0.5

    def _calculate_percentile(self, data: List[float], percentile: float) -> float:
        """Calculate percentile of a list"""
        if not data:
            return 0.0
        sorted_data = sorted(data)
        n = len(sorted_data)
        index = (percentile / 100) * (n - 1)
        if index.is_integer():
            return sorted_data[int(index)]
        else:
            lower = sorted_data[int(index)]
            upper = sorted_data[int(index) + 1]
            return lower + (upper - lower) * (index - int(index))

    def get_generator_status(self) -> Dict[str, Any]:
        """Get current generator status"""
        return {
            "initialized": True,
            "config": {
                "include_visualizations": self.config.include_visualizations,
                "include_detailed_metrics": self.config.include_detailed_metrics,
                "include_recommendations": self.config.include_recommendations,
                "export_formats": self.config.export_formats
            },
            "available_formats": ["json", "markdown", "csv"],
            "templates_available": list(self.templates.keys())
        }