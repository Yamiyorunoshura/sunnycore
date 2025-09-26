"""
Test cases for Report Generator functionality - Task 5 brownfield improvement
Tests for report generation and formatting for RAG evaluation results
"""

import pytest
import json
import tempfile
import os
from typing import List, Dict, Any
from dataclasses import dataclass

from src.rag_integration.report_generator import ReportGenerator, ReportSection, EvaluationReport
from src.rag_integration.data_converter import StandardizedQuery


class TestReportGenerator:
    """Test suite for ReportGenerator functionality"""

    @pytest.fixture
    def report_generator(self):
        """Create ReportGenerator instance"""
        return ReportGenerator()

    @pytest.fixture
    def sample_evaluation_results(self):
        """Create sample evaluation results for testing"""
        return {
            "retrieval_metrics": {
                "hit_rate": 0.85,
                "precision": 0.80,
                "recall": 0.75,
                "f1_score": 0.77,
                "ndcg": 0.82
            },
            "generation_metrics": {
                "faithfulness": 0.92,
                "relevance": 0.78,
                "coherence": 0.88
            },
            "performance_metrics": {
                "latency_ms": 2.5,
                "throughput_qps": 100
            }
        }

    def test_initialization(self, report_generator):
        """Test report generator initialization"""
        assert hasattr(report_generator, 'generate_comprehensive_report')
        assert "basic" in report_generator.report_templates
        assert "detailed" in report_generator.report_templates
        assert "executive" in report_generator.report_templates

    def test_generate_comprehensive_report_basic(self, report_generator, sample_evaluation_results):
        """Test basic comprehensive report generation"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        assert isinstance(report, EvaluationReport), "Should return EvaluationReport object"
        assert report.report_id, "Report should have an ID"
        assert report.timestamp, "Report should have timestamp"
        assert report.summary, "Report should have summary"
        assert report.retrieval_section, "Report should have retrieval section"
        assert report.generation_section, "Report should have generation section"
        assert report.overall_assessment, "Report should have overall assessment"

    def test_generate_comprehensive_report_with_templates(self, report_generator, sample_evaluation_results):
        """Test comprehensive report generation with different templates"""
        # Test basic template
        basic_report = report_generator.generate_comprehensive_report(sample_evaluation_results, "basic")
        assert isinstance(basic_report, EvaluationReport)

        # Test detailed template
        detailed_report = report_generator.generate_comprehensive_report(sample_evaluation_results, "detailed")
        assert isinstance(detailed_report, EvaluationReport)

        # Test executive template
        executive_report = report_generator.generate_comprehensive_report(sample_evaluation_results, "executive")
        assert isinstance(executive_report, EvaluationReport)

    def test_report_section_creation(self):
        """Test ReportSection dataclass functionality"""
        section = ReportSection(
            title="Test Section",
            content={"metric1": 0.85, "metric2": 0.92},
            metrics={"hit_rate": 0.85, "faithfulness": 0.92},
            recommendations=["Improve retrieval", "Enhance generation"]
        )

        assert section.title == "Test Section"
        assert section.content["metric1"] == 0.85
        assert section.metrics["hit_rate"] == 0.85
        assert len(section.recommendations) == 2

    def test_evaluation_report_structure(self, report_generator, sample_evaluation_results):
        """Test EvaluationReport structure"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        # Test retrieval section
        retrieval_section = report.retrieval_section
        assert isinstance(retrieval_section, ReportSection)
        assert retrieval_section.title, "Retrieval section should have title"
        assert isinstance(retrieval_section.content, dict), "Retrieval content should be dict"
        assert isinstance(retrieval_section.metrics, dict), "Retrieval metrics should be dict"
        assert isinstance(retrieval_section.recommendations, list), "Retrieval recommendations should be list"

        # Test generation section
        generation_section = report.generation_section
        assert isinstance(generation_section, ReportSection)
        assert generation_section.title, "Generation section should have title"

    def test_invalid_template_handling(self, report_generator, sample_evaluation_results):
        """Test handling of invalid template type"""
        with pytest.raises(ValueError):
            report_generator.generate_comprehensive_report(sample_evaluation_results, "invalid_template")

    def test_empty_evaluation_results_handling(self, report_generator):
        """Test handling of empty evaluation results"""
        empty_results = {}

        report = report_generator.generate_comprehensive_report(empty_results)

        assert isinstance(report, EvaluationReport), "Should handle empty results gracefully"
        assert report.report_id, "Should still generate report ID"
        assert report.timestamp, "Should still generate timestamp"

    def test_partial_evaluation_results_handling(self, report_generator):
        """Test handling of partial evaluation results"""
        partial_results = {
            "retrieval_metrics": {
                "hit_rate": 0.85,
                "precision": 0.80
            }
            # Missing generation_metrics and performance_metrics
        }

        report = report_generator.generate_comprehensive_report(partial_results)

        assert isinstance(report, EvaluationReport), "Should handle partial results gracefully"
        assert report.retrieval_section, "Should have retrieval section even with partial data"

    def test_comprehensive_report_summary_content(self, report_generator, sample_evaluation_results):
        """Test that comprehensive report contains meaningful summary"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        summary = report.summary
        assert isinstance(summary, dict), "Summary should be a dictionary"

        # Summary should contain overall assessment
        if "overall_score" in summary:
            assert 0.0 <= summary["overall_score"] <= 1.0, "Overall score should be between 0 and 1"

    def test_comprehensive_report_recommendations(self, report_generator, sample_evaluation_results):
        """Test that comprehensive report contains recommendations"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        # Check retrieval recommendations
        retrieval_recs = report.retrieval_section.recommendations
        assert isinstance(retrieval_recs, list), "Retrieval recommendations should be a list"

        # Check generation recommendations
        generation_recs = report.generation_section.recommendations
        assert isinstance(generation_recs, list), "Generation recommendations should be a list"

    def test_comprehensive_report_metrics_calculation(self, report_generator, sample_evaluation_results):
        """Test that metrics are properly calculated and stored"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        # Check retrieval metrics
        retrieval_metrics = report.retrieval_section.metrics
        assert isinstance(retrieval_metrics, dict), "Retrieval metrics should be a dictionary"

        # Check generation metrics
        generation_metrics = report.generation_section.metrics
        assert isinstance(generation_metrics, dict), "Generation metrics should be a dictionary"

        # Metrics should be within valid ranges
        for metric_name, metric_value in retrieval_metrics.items():
            assert 0.0 <= metric_value <= 1.0, f"Retrieval metric {metric_name} should be between 0 and 1"

        for metric_name, metric_value in generation_metrics.items():
            assert 0.0 <= metric_value <= 1.0, f"Generation metric {metric_name} should be between 0 and 1"

    def test_comprehensive_report_overall_assessment(self, report_generator, sample_evaluation_results):
        """Test overall assessment in comprehensive report"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        overall_assessment = report.overall_assessment
        assert isinstance(overall_assessment, dict), "Overall assessment should be a dictionary"

        # Should contain performance indicators
        if "performance_rating" in overall_assessment:
            assert isinstance(overall_assessment["performance_rating"], str), "Performance rating should be string"

        if "key_findings" in overall_assessment:
            assert isinstance(overall_assessment["key_findings"], list), "Key findings should be a list"

    def test_multiple_report_generation_consistency(self, report_generator, sample_evaluation_results):
        """Test that multiple reports generated with same data are consistent"""
        report1 = report_generator.generate_comprehensive_report(sample_evaluation_results)
        report2 = report_generator.generate_comprehensive_report(sample_evaluation_results)

        # Reports should have same structure (IDs may be same if generated in same second)
        assert report1.retrieval_section.title == report2.retrieval_section.title, "Structure should be consistent"
        assert report1.generation_section.title == report2.generation_section.title, "Structure should be consistent"
        assert report1.summary.keys() == report2.summary.keys(), "Summary structure should be consistent"

    def test_report_dataclass_serialization(self, report_generator, sample_evaluation_results):
        """Test that report dataclasses can be serialized"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        # Test that dataclass can be converted to dict
        report_dict = report.__dict__
        assert isinstance(report_dict, dict), "Report should be convertible to dictionary"

        # Test that sections can be serialized
        retrieval_dict = report.retrieval_section.__dict__
        assert isinstance(retrieval_dict, dict), "Retrieval section should be serializable"

        generation_dict = report.generation_section.__dict__
        assert isinstance(generation_dict, dict), "Generation section should be serializable"

    def test_export_report_to_json(self, report_generator, sample_evaluation_results):
        """Test JSON export functionality"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            file_path = f.name

        try:
            report_generator.export_report_to_json(report, file_path)

            # Verify file was created and contains valid JSON
            with open(file_path, 'r') as f:
                exported_data = json.load(f)

            assert "report_id" in exported_data
            assert "timestamp" in exported_data
            assert "summary" in exported_data
            assert "retrieval_section" in exported_data
            assert "generation_section" in exported_data
            assert "overall_assessment" in exported_data

            # Verify data integrity
            assert exported_data["report_id"] == report.report_id
            assert exported_data["timestamp"] == report.timestamp
        finally:
            os.unlink(file_path)

    def test_export_report_to_markdown(self, report_generator, sample_evaluation_results):
        """Test Markdown export functionality"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            file_path = f.name

        try:
            report_generator.export_report_to_markdown(report, file_path)

            # Verify file was created and contains markdown content
            with open(file_path, 'r') as f:
                markdown_content = f.read()

            assert "# RAG Evaluation Report" in markdown_content
            assert report.report_id in markdown_content
            assert report.timestamp in markdown_content
            assert "## Summary" in markdown_content
            assert f"## {report.retrieval_section.title}" in markdown_content
            assert f"## {report.generation_section.title}" in markdown_content
        finally:
            os.unlink(file_path)

    def test_analyze_performance_with_metrics(self, report_generator):
        """Test performance analysis with metrics"""
        metrics = {"precision": 0.85, "recall": 0.75, "f1_score": 0.80}

        analysis = report_generator._analyze_performance(metrics)

        assert analysis["average"] == (0.85 + 0.75 + 0.80) / 3
        assert analysis["min"] == 0.75
        assert analysis["max"] == 0.85
        assert analysis["performance_level"] in ["good", "needs_improvement"]

    def test_analyze_performance_empty_metrics(self, report_generator):
        """Test performance analysis with empty metrics"""
        analysis = report_generator._analyze_performance({})

        assert analysis["status"] == "No data available"

    def test_generate_retrieval_recommendations(self, report_generator):
        """Test retrieval-specific recommendations generation"""
        # Test with low precision
        low_precision_metrics = {"context_precision": 0.7, "context_recall": 0.85, "faithfulness": 0.92}
        recommendations = report_generator._generate_retrieval_recommendations(low_precision_metrics)

        assert any("context precision" in rec.lower() for rec in recommendations)

        # Test with low recall
        low_recall_metrics = {"context_precision": 0.85, "context_recall": 0.7, "faithfulness": 0.92}
        recommendations = report_generator._generate_retrieval_recommendations(low_recall_metrics)

        assert any("recall" in rec.lower() for rec in recommendations)

        # Test with low faithfulness
        low_faithfulness_metrics = {"context_precision": 0.85, "context_recall": 0.85, "faithfulness": 0.8}
        recommendations = report_generator._generate_retrieval_recommendations(low_faithfulness_metrics)

        assert any("faithfulness" in rec.lower() for rec in recommendations)

        # Test with good metrics
        good_metrics = {"context_precision": 0.85, "context_recall": 0.85, "faithfulness": 0.92}
        recommendations = report_generator._generate_retrieval_recommendations(good_metrics)

        assert len(recommendations) == 1
        assert "good" in recommendations[0].lower()

    def test_generate_generation_recommendations(self, report_generator):
        """Test generation-specific recommendations generation"""
        # Test with low relevance
        low_relevance_metrics = {"answer_relevancy": 0.7, "bleu": 0.8, "rouge": 0.85}
        recommendations = report_generator._generate_generation_recommendations(low_relevance_metrics)

        assert any("relevance" in rec.lower() for rec in recommendations)

        # Test with low BLEU
        low_bleu_metrics = {"answer_relevancy": 0.85, "bleu": 0.6, "rouge": 0.85}
        recommendations = report_generator._generate_generation_recommendations(low_bleu_metrics)

        assert any("bleu" in rec.lower() or "generation" in rec.lower() for rec in recommendations)

        # Test with low ROUGE
        low_rouge_metrics = {"answer_relevancy": 0.85, "bleu": 0.8, "rouge": 0.6}
        recommendations = report_generator._generate_generation_recommendations(low_rouge_metrics)

        assert any("rouge" in rec.lower() or "summary" in rec.lower() for rec in recommendations)

        # Test with good metrics
        good_metrics = {"answer_relevancy": 0.85, "bleu": 0.8, "rouge": 0.85}
        recommendations = report_generator._generate_generation_recommendations(good_metrics)

        assert len(recommendations) == 1
        assert "good" in recommendations[0].lower()

    def test_extract_key_metrics(self, report_generator):
        """Test key metrics extraction"""
        all_metrics = {
            "precision": 0.85,
            "recall": 0.75,
            "accuracy": 0.90,
            "f1_score": 0.80,
            "some_other_metric": 0.70,
            "custom_score": 0.65
        }

        key_metrics = report_generator._extract_key_metrics(all_metrics)

        # Should include metrics with keywords like precision, recall, accuracy, score
        assert "precision" in key_metrics
        assert "recall" in key_metrics
        assert "accuracy" in key_metrics
        assert "f1_score" in key_metrics
        assert "custom_score" in key_metrics  # Contains "score"

        # Should not include metrics without keywords
        assert "some_other_metric" not in key_metrics

    def test_extract_key_metrics_empty(self, report_generator):
        """Test key metrics extraction with empty metrics"""
        key_metrics = report_generator._extract_key_metrics({})
        assert key_metrics == {}

    def test_helper_methods_detailed_report(self, report_generator, sample_evaluation_results):
        """Test helper methods for detailed report"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results, "detailed")

        # Test trend analysis
        trend_analysis = report_generator._generate_trend_analysis(sample_evaluation_results["retrieval_metrics"])
        assert "trend" in trend_analysis
        assert "projection" in trend_analysis

        # Test comparative analysis
        comparative_analysis = report_generator._generate_comparative_analysis(sample_evaluation_results["retrieval_metrics"])
        assert "comparison" in comparative_analysis
        assert "performance" in comparative_analysis

        # Test consistency analysis
        consistency_analysis = report_generator._generate_consistency_analysis(sample_evaluation_results["generation_metrics"])
        assert "consistency" in consistency_analysis
        assert "reliability" in consistency_analysis

        # Test accuracy assessment
        accuracy_assessment = report_generator._generate_accuracy_assessment(sample_evaluation_results["generation_metrics"])
        assert "accuracy" in accuracy_assessment
        assert "areas_for_improvement" in accuracy_assessment

    def test_quality_grade_calculation(self, report_generator):
        """Test quality grade calculation"""
        # Test A grade
        results_a = {"overall_score": 0.95}
        grade = report_generator._calculate_quality_grade(results_a)
        assert grade == "A"

        # Test B grade
        results_b = {"overall_score": 0.85}
        grade = report_generator._calculate_quality_grade(results_b)
        assert grade == "B"

        # Test C grade
        results_c = {"overall_score": 0.75}
        grade = report_generator._calculate_quality_grade(results_c)
        assert grade == "C"

        # Test D grade
        results_d = {"overall_score": 0.65}
        grade = report_generator._calculate_quality_grade(results_d)
        assert grade == "D"

    def test_confidence_score_calculation(self, report_generator):
        """Test confidence score calculation"""
        # Test with high score
        results_high = {"overall_score": 0.95}
        confidence = report_generator._calculate_confidence_score(results_high)
        assert confidence == 0.95  # Should be capped at 0.95

        # Test with medium score
        results_medium = {"overall_score": 0.75}
        confidence = report_generator._calculate_confidence_score(results_medium)
        assert confidence == 0.85  # 0.75 + 0.1

        # Test with low score
        results_low = {"overall_score": 0.3}
        confidence = report_generator._calculate_confidence_score(results_low)
        assert confidence == 0.4  # 0.3 + 0.1

    def test_action_items_generation(self, report_generator):
        """Test action items generation"""
        results = {"overall_score": 0.75}
        action_items = report_generator._generate_action_items(results)

        assert isinstance(action_items, list)
        assert len(action_items) > 0
        assert all(isinstance(item, str) for item in action_items)

    def test_success_criteria_evaluation(self, report_generator):
        """Test success criteria evaluation"""
        # Test with high score
        good_results = {"overall_score": 0.85}
        success_criteria = report_generator._evaluate_success_criteria(good_results)

        assert success_criteria["meets_precision_target"] is True
        assert success_criteria["meets_recall_target"] is True
        assert success_criteria["meets_quality_target"] is True

        # Test with medium score
        medium_results = {"overall_score": 0.75}
        success_criteria = report_generator._evaluate_success_criteria(medium_results)

        assert success_criteria["meets_precision_target"] is False
        assert success_criteria["meets_recall_target"] is True
        assert success_criteria["meets_quality_target"] is False

        # Test with low score
        poor_results = {"overall_score": 0.65}
        success_criteria = report_generator._evaluate_success_criteria(poor_results)

        assert success_criteria["meets_precision_target"] is False
        assert success_criteria["meets_recall_target"] is False
        assert success_criteria["meets_quality_target"] is False

    def test_categorize_performance(self, report_generator):
        """Test performance categorization"""
        results = {"overall_score": 0.85}
        categories = report_generator._categorize_performance(results)

        assert isinstance(categories, dict)
        assert "excellent" in categories
        assert "good" in categories
        assert "needs_improvement" in categories

        # Check that values are integers
        for count in categories.values():
            assert isinstance(count, int)

    def test_key_insights_generation(self, report_generator):
        """Test key insights generation"""
        results = {"overall_score": 0.85}
        insights = report_generator._generate_key_insights(results)

        assert isinstance(insights, list)
        assert len(insights) > 0
        assert all(isinstance(insight, str) for insight in insights)

    def test_risk_areas_identification(self, report_generator):
        """Test risk areas identification"""
        results = {"overall_score": 0.85}
        risk_areas = report_generator._identify_risk_areas(results)

        assert isinstance(risk_areas, list)
        assert len(risk_areas) > 0
        assert all(isinstance(risk, str) for risk in risk_areas)

    def test_report_content_integrity(self, report_generator, sample_evaluation_results):
        """Test report content integrity across different templates"""
        templates = ["basic", "detailed", "executive"]

        for template in templates:
            report = report_generator.generate_comprehensive_report(sample_evaluation_results, template)

            # Check basic structure integrity
            assert report.report_id, f"Report should have ID for {template} template"
            assert report.timestamp, f"Report should have timestamp for {template} template"
            assert report.summary, f"Report should have summary for {template} template"
            assert report.retrieval_section, f"Report should have retrieval section for {template} template"
            assert report.generation_section, f"Report should have generation section for {template} template"
            assert report.overall_assessment, f"Report should have overall assessment for {template} template"

            # Check section content
            assert report.retrieval_section.title, f"Retrieval section should have title for {template} template"
            assert report.generation_section.title, f"Generation section should have title for {template} template"

            # Check metrics are present
            assert isinstance(report.retrieval_section.metrics, dict), f"Retrieval metrics should be dict for {template} template"
            assert isinstance(report.generation_section.metrics, dict), f"Generation metrics should be dict for {template} template"

    def test_report_with_performance_metrics(self, report_generator):
        """Test report generation with performance metrics"""
        results_with_performance = {
            "retrieval_metrics": {"precision": 0.85, "recall": 0.80},
            "generation_metrics": {"faithfulness": 0.92, "relevance": 0.78},
            "performance_metrics": {"latency_ms": 2.5, "throughput_qps": 100}
        }

        report = report_generator.generate_comprehensive_report(results_with_performance)

        # Performance metrics should not break report generation
        assert report is not None
        assert report.summary is not None

    def test_markdown_content_structure(self, report_generator, sample_evaluation_results):
        """Test markdown content structure"""
        report = report_generator.generate_comprehensive_report(sample_evaluation_results)
        markdown_content = report_generator._generate_markdown_content(report)

        # Check required sections
        required_sections = [
            "# RAG Evaluation Report",
            "## Summary",
            f"## {report.retrieval_section.title}",
            f"## {report.generation_section.title}"
        ]

        for section in required_sections:
            assert section in markdown_content, f"Missing section: {section}"

        # Check report metadata
        assert f"**Report ID**: {report.report_id}" in markdown_content
        assert f"**Generated**: {report.timestamp}" in markdown_content

        # Check metrics sections
        assert "### Metrics" in markdown_content
        assert "### Recommendations" in markdown_content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])