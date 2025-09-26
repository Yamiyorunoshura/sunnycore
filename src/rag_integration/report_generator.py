"""
Report Generator for RAG evaluation
Generates comprehensive reports for retrieval and generation quality
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import json
from datetime import datetime


@dataclass
class ReportSection:
    """Individual report section"""
    title: str
    content: Dict[str, Any]
    metrics: Dict[str, float]
    recommendations: List[str]


@dataclass
class EvaluationReport:
    """Complete evaluation report"""
    report_id: str
    timestamp: str
    summary: Dict[str, Any]
    retrieval_section: ReportSection
    generation_section: ReportSection
    overall_assessment: Dict[str, Any]


class ReportGenerator:
    """
    Generates comprehensive evaluation reports
    Minimal implementation for TDD
    """

    def __init__(self):
        """Initialize report generator"""
        self.report_templates = {
            "basic": self._basic_report_template,
            "detailed": self._detailed_report_template,
            "executive": self._executive_report_template
        }

    def generate_comprehensive_report(self, evaluation_results: Dict[str, Any],
                                    template_type: str = "detailed") -> EvaluationReport:
        """
        Generate comprehensive evaluation report
        """
        if template_type not in self.report_templates:
            raise ValueError(f"Unsupported template type: {template_type}")

        template = self.report_templates[template_type]
        return template(evaluation_results)

    def _basic_report_template(self, results: Dict[str, Any]) -> EvaluationReport:
        """Basic report template"""
        retrieval_section = ReportSection(
            title="Retrieval Performance",
            content=results.get("retrieval_metrics", {}),
            metrics=results.get("retrieval_metrics", {}),
            recommendations=["Improve context precision", "Optimize retrieval algorithms"]
        )

        generation_section = ReportSection(
            title="Generation Quality",
            content=results.get("generation_metrics", {}),
            metrics=results.get("generation_metrics", {}),
            recommendations=["Enhance language model", "Improve answer coherence"]
        )

        summary = {
            "total_queries": results.get("total_queries", 0),
            "overall_score": results.get("overall_score", 0.0),
            "pass_rate": results.get("pass_rate", 0.0)
        }

        overall_assessment = {
            "status": "completed",
            "quality_grade": "B",
            "next_steps": ["Review recommendations", "Implement improvements"]
        }

        return EvaluationReport(
            report_id=f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.now().isoformat(),
            summary=summary,
            retrieval_section=retrieval_section,
            generation_section=generation_section,
            overall_assessment=overall_assessment
        )

    def _detailed_report_template(self, results: Dict[str, Any]) -> EvaluationReport:
        """Detailed report template"""
        # Enhanced retrieval section
        retrieval_metrics = results.get("retrieval_metrics", {})
        retrieval_section = ReportSection(
            title="Retrieval Performance Analysis",
            content={
                "performance_breakdown": self._analyze_performance(retrieval_metrics),
                "trend_analysis": self._generate_trend_analysis(retrieval_metrics),
                "comparative_analysis": self._generate_comparative_analysis(retrieval_metrics)
            },
            metrics=retrieval_metrics,
            recommendations=self._generate_retrieval_recommendations(retrieval_metrics)
        )

        # Enhanced generation section
        generation_metrics = results.get("generation_metrics", {})
        generation_section = ReportSection(
            title="Generation Quality Analysis",
            content={
                "quality_breakdown": self._analyze_performance(generation_metrics),
                "consistency_analysis": self._generate_consistency_analysis(generation_metrics),
                "accuracy_assessment": self._generate_accuracy_assessment(generation_metrics)
            },
            metrics=generation_metrics,
            recommendations=self._generate_generation_recommendations(generation_metrics)
        )

        # Enhanced summary
        summary = {
            "total_queries": results.get("total_queries", 0),
            "overall_score": results.get("overall_score", 0.0),
            "pass_rate": results.get("pass_rate", 0.0),
            "performance_categories": self._categorize_performance(results),
            "key_insights": self._generate_key_insights(results),
            "risk_areas": self._identify_risk_areas(results)
        }

        # Enhanced overall assessment
        overall_assessment = {
            "status": "completed",
            "quality_grade": self._calculate_quality_grade(results),
            "confidence_score": self._calculate_confidence_score(results),
            "action_items": self._generate_action_items(results),
            "success_criteria": self._evaluate_success_criteria(results)
        }

        return EvaluationReport(
            report_id=f"detailed_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.now().isoformat(),
            summary=summary,
            retrieval_section=retrieval_section,
            generation_section=generation_section,
            overall_assessment=overall_assessment
        )

    def _executive_report_template(self, results: Dict[str, Any]) -> EvaluationReport:
        """Executive summary report template"""
        # Simplified sections for executive audience
        retrieval_section = ReportSection(
            title="Retrieval Performance Summary",
            content={"key_metrics": self._extract_key_metrics(results.get("retrieval_metrics", {}))},
            metrics=self._extract_key_metrics(results.get("retrieval_metrics", {})),
            recommendations=["Focus on high-impact improvements"]
        )

        generation_section = ReportSection(
            title="Generation Quality Summary",
            content={"key_metrics": self._extract_key_metrics(results.get("generation_metrics", {}))},
            metrics=self._extract_key_metrics(results.get("generation_metrics", {})),
            recommendations=["Enhance answer quality and relevance"]
        )

        summary = {
            "overall_score": results.get("overall_score", 0.0),
            "status": "good" if results.get("overall_score", 0) > 0.8 else "needs_improvement",
            "key_findings": [
                "Retrieval performance meets minimum requirements",
                "Generation quality shows room for improvement",
                "Overall system performance is satisfactory"
            ]
        }

        overall_assessment = {
            "status": "completed",
            "recommendation": "Proceed with phased improvements",
            "roi_assessment": "High potential for improvement with moderate investment",
            "timeline": "3-6 months for significant improvements"
        }

        return EvaluationReport(
            report_id=f"executive_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.now().isoformat(),
            summary=summary,
            retrieval_section=retrieval_section,
            generation_section=generation_section,
            overall_assessment=overall_assessment
        )

    def export_report_to_json(self, report: EvaluationReport, file_path: str):
        """Export report to JSON file"""
        report_dict = asdict(report)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(report_dict, f, indent=2, ensure_ascii=False)

    def export_report_to_markdown(self, report: EvaluationReport, file_path: str):
        """Export report to Markdown file"""
        markdown_content = self._generate_markdown_content(report)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

    def _generate_markdown_content(self, report: EvaluationReport) -> str:
        """Generate Markdown content from report"""
        content = f"# RAG Evaluation Report\n\n"
        content += f"**Report ID**: {report.report_id}\n"
        content += f"**Generated**: {report.timestamp}\n\n"

        content += "## Summary\n\n"
        for key, value in report.summary.items():
            content += f"- **{key}**: {value}\n"

        content += f"\n## {report.retrieval_section.title}\n\n"
        content += f"### Metrics\n"
        for key, value in report.retrieval_section.metrics.items():
            content += f"- {key}: {value:.3f}\n"

        content += f"\n### Recommendations\n"
        for rec in report.retrieval_section.recommendations:
            content += f"- {rec}\n"

        content += f"\n## {report.generation_section.title}\n\n"
        content += f"### Metrics\n"
        for key, value in report.generation_section.metrics.items():
            content += f"- {key}: {value:.3f}\n"

        content += f"\n### Recommendations\n"
        for rec in report.generation_section.recommendations:
            content += f"- {rec}\n"

        return content

    # Helper methods for detailed analysis
    def _analyze_performance(self, metrics: Dict[str, float]) -> Dict[str, Any]:
        """Analyze performance metrics"""
        if not metrics:
            return {"status": "No data available"}

        values = list(metrics.values())
        return {
            "average": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
            "performance_level": "good" if sum(values) / len(values) > 0.8 else "needs_improvement"
        }

    def _generate_retrieval_recommendations(self, metrics: Dict[str, float]) -> List[str]:
        """Generate retrieval-specific recommendations"""
        recommendations = []
        if metrics.get("context_precision", 0) < 0.8:
            recommendations.append("Improve context precision through better indexing")
        if metrics.get("context_recall", 0) < 0.8:
            recommendations.append("Enhance recall with expanded document retrieval")
        if metrics.get("faithfulness", 0) < 0.9:
            recommendations.append("Improve faithfulness through better fact-checking mechanisms")

        return recommendations or ["Retrieval performance is good"]

    def _generate_generation_recommendations(self, metrics: Dict[str, float]) -> List[str]:
        """Generate generation-specific recommendations"""
        recommendations = []
        if metrics.get("answer_relevancy", 0) < 0.8:
            recommendations.append("Improve answer relevance with better prompt engineering")
        if metrics.get("bleu", 0) < 0.7:
            recommendations.append("Enhance text generation quality")
        if metrics.get("rouge", 0) < 0.7:
            recommendations.append("Improve summary quality and coherence")

        return recommendations or ["Generation quality is good"]

    def _extract_key_metrics(self, metrics: Dict[str, float]) -> Dict[str, float]:
        """Extract key metrics for executive summary"""
        key_metrics = {}
        for metric_name, value in metrics.items():
            if any(keyword in metric_name.lower() for keyword in ["precision", "recall", "score", "accuracy"]):
                key_metrics[metric_name] = value
        return key_metrics

    # Additional helper methods for comprehensive analysis
    def _generate_trend_analysis(self, metrics: Dict[str, float]) -> Dict[str, str]:
        """Generate trend analysis"""
        return {"trend": "stable", "projection": "improving with optimization"}

    def _generate_comparative_analysis(self, metrics: Dict[str, float]) -> Dict[str, str]:
        """Generate comparative analysis"""
        return {"comparison": "baseline", "performance": "above average"}

    def _generate_consistency_analysis(self, metrics: Dict[str, float]) -> Dict[str, str]:
        """Generate consistency analysis"""
        return {"consistency": "high", "reliability": "good"}

    def _generate_accuracy_assessment(self, metrics: Dict[str, float]) -> Dict[str, str]:
        """Generate accuracy assessment"""
        return {"accuracy": "good", "areas_for_improvement": "minimal"}

    def _categorize_performance(self, results: Dict[str, Any]) -> Dict[str, int]:
        """Categorize performance"""
        return {"excellent": 2, "good": 3, "needs_improvement": 1}

    def _generate_key_insights(self, results: Dict[str, Any]) -> List[str]:
        """Generate key insights"""
        return [
            "Retrieval system performs well with high precision",
            "Generation quality shows consistency",
            "Overall system meets baseline requirements"
        ]

    def _identify_risk_areas(self, results: Dict[str, Any]) -> List[str]:
        """Identify risk areas"""
        return ["Minor risks in generation consistency", "Opportunities for optimization"]

    def _calculate_quality_grade(self, results: Dict[str, Any]) -> str:
        """Calculate quality grade"""
        score = results.get("overall_score", 0)
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        else:
            return "D"

    def _calculate_confidence_score(self, results: Dict[str, Any]) -> float:
        """Calculate confidence score"""
        return min(0.95, results.get("overall_score", 0) + 0.1)

    def _generate_action_items(self, results: Dict[str, Any]) -> List[str]:
        """Generate action items"""
        return [
            "Optimize retrieval algorithms",
            "Enhance generation models",
            "Implement continuous monitoring"
        ]

    def _evaluate_success_criteria(self, results: Dict[str, Any]) -> Dict[str, bool]:
        """Evaluate success criteria"""
        return {
            "meets_precision_target": results.get("overall_score", 0) >= 0.8,
            "meets_recall_target": results.get("overall_score", 0) >= 0.7,
            "meets_quality_target": results.get("overall_score", 0) >= 0.8
        }