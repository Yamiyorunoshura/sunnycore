"""
Test cases for RAGAs Integration - Task 5.2
Tests for RAGAs tool integration and data format conversion
"""

import pytest
import tempfile
import os
from typing import List, Dict, Any
from dataclasses import dataclass

# Import the classes to be tested
from src.rag_integration.ragas_integrator import RAGAsIntegrator
from src.rag_integration.data_converter import DataConverter
from src.rag_integration.report_generator import ReportGenerator


@dataclass
class TestDataQuery:
    """Test query data structure"""
    query: str
    contexts: List[str]
    answer: str
    ground_truth: str
    query_id: str


class TestRAGAsIntegration:
    """Test suite for RAGAs Integration"""

    @pytest.fixture
    def sample_queries(self):
        """Create sample test queries"""
        return [
            TestDataQuery(
                query="What is machine learning?",
                contexts=[
                    "Machine learning is a subset of artificial intelligence",
                    "ML algorithms build mathematical models based on training data"
                ],
                answer="Machine learning is a subset of AI that builds models from training data",
                ground_truth="Machine learning is a subset of artificial intelligence",
                query_id="ml_001"
            ),
            TestDataQuery(
                query="How does RAG work?",
                contexts=[
                    "RAG combines retrieval and generation",
                    "It retrieves relevant documents before generating responses"
                ],
                answer="RAG works by retrieving relevant documents and then generating responses based on them",
                ground_truth="RAG retrieves documents and generates responses",
                query_id="rag_001"
            )
        ]

    @pytest.fixture
    def ragas_integrator(self):
        """Create RAGAsIntegrator instance"""
        return RAGAsIntegrator()

    @pytest.fixture
    def data_converter(self):
        """Create DataConverter instance"""
        return DataConverter()

    @pytest.fixture
    def report_generator(self):
        """Create ReportGenerator instance"""
        return ReportGenerator()

    def test_ragas_integration_success_rate(self, ragas_integrator, sample_queries):
        """
        Test: RAGAs集成成功率100%
        Success metric: integration_success_rate = 100%
        """
        successful_evaluations = 0
        total_queries = len(sample_queries)

        for query in sample_queries:
            result = ragas_integrator.evaluate_with_ragas(query)
            if result is not None:
                successful_evaluations += 1

        success_rate = successful_evaluations / total_queries
        assert success_rate == 1.0, f"Integration success rate {success_rate} is below 100%"

    def test_independent_retrieval_generation_metrics(self, ragas_integrator, sample_queries):
        """
        Test: 獨立指標計算
        Success metric: retrieval_generation_separation = true
        """
        query = sample_queries[0]

        # Get separated metrics
        metrics = ragas_integrator.get_separated_metrics(query)

        # Assert both retrieval and generation metrics are present and separate
        assert "retrieval_metrics" in metrics, "Retrieval metrics not found"
        assert "generation_metrics" in metrics, "Generation metrics not found"
        assert isinstance(metrics["retrieval_metrics"], dict), "Retrieval metrics should be a dictionary"
        assert isinstance(metrics["generation_metrics"], dict), "Generation metrics should be a dictionary"

        # Ensure no overlap between metric names
        retrieval_keys = set(metrics["retrieval_metrics"].keys())
        generation_keys = set(metrics["generation_metrics"].keys())
        overlap = retrieval_keys.intersection(generation_keys)
        assert len(overlap) == 0, f"Found overlapping metric names: {overlap}"

    def test_data_standardization_compliance(self, data_converter, sample_queries):
        """
        Test: 標準化數據集
        Success metric: data_standardization_compliance = 100%
        """
        query = sample_queries[0]
        raw_data = {
            "query": query.query,
            "contexts": query.contexts,
            "answer": query.answer
        }

        # Test data standardization - use the correct method
        standardized_list = data_converter.convert_to_standardized_format(raw_data)
        assert len(standardized_list) == 1
        standardized = standardized_list[0]

        # Check required fields
        assert hasattr(standardized, "query"), "Query field missing"
        assert hasattr(standardized, "contexts"), "Contexts field missing"
        assert hasattr(standardized, "answer"), "Answer field missing"
        assert hasattr(standardized, "ground_truth"), "Ground truth field missing"

        # Check data types
        assert isinstance(standardized.query, str), "Query should be a string"
        assert isinstance(standardized.contexts, list), "Contexts should be a list"
        assert isinstance(standardized.answer, str), "Answer should be a string"
        assert isinstance(standardized.ground_truth, str), "Ground truth should be a string"

    def test_report_separation_accuracy(self, ragas_integrator, sample_queries):
        """
        Test: 分離式報告生成
        Success metric: report_separation_accuracy = 100%
        """
        query = sample_queries[0]

        # Generate separated report
        report = ragas_integrator.generate_separated_report(query)

        # Assert report has separated sections
        assert "retrieval_report" in report, "Retrieval report section missing"
        assert "generation_report" in report, "Generation report section missing"
        assert "summary" in report, "Summary section missing"

        # Validate separation accuracy
        retrieval_content = report["retrieval_report"]
        generation_content = report["generation_report"]

        # Ensure no overlap between sections
        retrieval_keys = set(retrieval_content.keys())
        generation_keys = set(generation_content.keys())

        overlap = retrieval_keys.intersection(generation_keys)
        assert len(overlap) == 0, f"Found overlapping keys between sections: {overlap}"

    def test_data_conversion_formats(self, data_converter, sample_queries):
        """Test various data format conversions"""
        # Test dict conversion
        query = sample_queries[0]
        dict_data = {
            "query_id": query.query_id,
            "query": query.query,
            "contexts": query.contexts,
            "answer": query.answer,
            "ground_truth": query.ground_truth
        }

        standardized = data_converter.convert_to_standardized_format(dict_data)
        assert len(standardized) == 1
        assert standardized[0].query == query.query

        # Test list conversion - wrap in queries structure
        list_data = {"queries": [dict_data]}
        standardized_from_list = data_converter.convert_to_standardized_format(list_data)
        assert len(standardized_from_list) == 1

        # Test JSON conversion - wrap in queries structure
        import json
        json_data = json.dumps({"queries": [dict_data]})
        standardized_from_json = data_converter.convert_to_standardized_format(json_data)
        assert len(standardized_from_json) == 1

    def test_ragas_format_conversion(self, data_converter, sample_queries):
        """Test conversion to RAGAs format"""
        query = sample_queries[0]
        standardized = data_converter.convert_to_standardized_format({
            "query_id": query.query_id,
            "query": query.query,
            "contexts": query.contexts,
            "answer": query.answer,
            "ground_truth": query.ground_truth
        })
        ragas_data = data_converter.convert_to_ragas_format(standardized)

        assert len(ragas_data) == 1
        ragas_item = ragas_data[0]

        required_ragas_fields = ["question", "contexts", "answer", "ground_truth"]
        for field in required_ragas_fields:
            assert field in ragas_item, f"Required RAGAs field {field} missing"

    def test_deepeval_format_conversion(self, data_converter, sample_queries):
        """Test conversion to DeepEval format"""
        query = sample_queries[0]
        standardized = data_converter.convert_to_standardized_format({
            "query_id": query.query_id,
            "query": query.query,
            "contexts": query.contexts,
            "answer": query.answer,
            "ground_truth": query.ground_truth
        })
        deepeval_data = data_converter.convert_to_deepeval_format(standardized)

        assert len(deepeval_data) == 1
        deepeval_item = deepeval_data[0]

        required_deepeval_fields = ["input", "actual_output", "expected_output", "context"]
        for field in required_deepeval_fields:
            assert field in deepeval_item, f"Required DeepEval field {field} missing"

    def test_report_generation_templates(self, report_generator, sample_queries):
        """Test different report generation templates"""
        evaluation_results = {
            "retrieval_metrics": {"precision": 0.85, "recall": 0.80},
            "generation_metrics": {"bleu": 0.75, "rouge": 0.80},
            "overall_score": 0.82,
            "total_queries": len(sample_queries)
        }

        # Test basic template
        basic_report = report_generator.generate_comprehensive_report(evaluation_results, "basic")
        assert basic_report.summary["overall_score"] == 0.82

        # Test detailed template
        detailed_report = report_generator.generate_comprehensive_report(evaluation_results, "detailed")
        assert detailed_report.overall_assessment["quality_grade"] in ["A", "B", "C", "D"]

        # Test executive template
        executive_report = report_generator.generate_comprehensive_report(evaluation_results, "executive")
        assert executive_report.summary["status"] in ["good", "needs_improvement"]

    def test_batch_evaluation(self, ragas_integrator, sample_queries):
        """Test batch evaluation functionality"""
        results = ragas_integrator.batch_evaluate(sample_queries)

        assert len(results) == len(sample_queries)
        for result in results:
            assert result is not None
            assert result.overall_score > 0

    def test_configuration_validation(self, ragas_integrator):
        """Test configuration validation"""
        # Test valid configuration
        ragas_integrator.configure_evaluation({"model": "gpt-4", "metrics": ["retrieval"]})
        validation = ragas_integrator.validate_configuration()
        assert validation["is_valid"] is True

        # Test invalid configuration - set config directly to missing required fields
        ragas_integrator.config = {"model": "gpt-4"}  # Missing metrics
        validation = ragas_integrator.validate_configuration()
        assert validation["is_valid"] is False
        assert len(validation["errors"]) > 0

    def test_data_validation(self, data_converter):
        """Test data format validation"""
        # Test valid data
        valid_data = {
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence"
        }
        validation = data_converter.validate_data_format(valid_data)
        assert validation["is_valid"] is True

        # Test invalid data (missing required field)
        invalid_data = {
            "query": "What is AI?",
            "answer": "AI stands for artificial intelligence"
        }
        validation = data_converter.validate_data_format(invalid_data)
        assert validation["is_valid"] is False
        assert len(validation["errors"]) > 0

    def test_dataset_statistics(self, data_converter, sample_queries):
        """Test dataset statistics generation"""
        query = sample_queries[0]
        standardized = data_converter.convert_to_standardized_format({
            "query_id": query.query_id,
            "query": query.query,
            "contexts": query.contexts,
            "answer": query.answer,
            "ground_truth": query.ground_truth
        })
        stats = data_converter.get_dataset_statistics(standardized)

        assert stats["total_queries"] == 1
        assert "query_length_stats" in stats
        assert "context_count_stats" in stats
        assert "answer_length_stats" in stats

    def test_dataset_filtering(self, data_converter, sample_queries):
        """Test dataset filtering functionality"""
        query = sample_queries[0]
        standardized = data_converter.convert_to_standardized_format({
            "query_id": query.query_id,
            "query": query.query,
            "contexts": query.contexts,
            "answer": query.answer,
            "ground_truth": query.ground_truth,
            "metadata": {"category": "test"}
        })

        # Test length filtering
        filtered = data_converter.filter_dataset(standardized, {"query_length_min": 10})
        assert len(filtered) <= len(standardized)

        # Test category filtering
        filtered_by_category = data_converter.filter_dataset(standardized, {"category": "test"})
        assert len(filtered_by_category) == len(standardized)


class TestRAGAsIntegrationEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_empty_query_handling(self):
        """Test handling of empty queries"""
        ragas_integrator = RAGAsIntegrator()
        result = ragas_integrator.evaluate_with_ragas(None)
        assert result is None

    def test_empty_data_handling(self):
        """Test handling of empty data"""
        data_converter = DataConverter()
        result = data_converter.convert_to_standardized_format([])
        assert result == []

    def test_invalid_json_handling(self):
        """Test handling of invalid JSON"""
        data_converter = DataConverter()
        with pytest.raises(ValueError):
            data_converter.convert_to_standardized_format("invalid json")

    def test_unsupported_template_handling(self):
        """Test handling of unsupported report template"""
        report_generator = ReportGenerator()
        with pytest.raises(ValueError):
            report_generator.generate_comprehensive_report({}, "unsupported_template")

    def test_large_dataset_performance(self):
        """Test performance with large dataset"""
        ragas_integrator = RAGAsIntegrator()
        # Create large dataset
        large_dataset = [
            TestDataQuery(
                query=f"Test query {i}",
                contexts=[f"Context {i}"],
                answer=f"Answer {i}",
                ground_truth=f"Ground truth {i}",
                query_id=f"test_{i}"
            )
            for i in range(50)
        ]

        import time
        start_time = time.time()
        results = ragas_integrator.batch_evaluate(large_dataset)
        end_time = time.time()

        execution_time = end_time - start_time
        assert execution_time < 10.0, f"Large dataset processing took {execution_time}s, too slow"
        assert len(results) == len(large_dataset)

    def test_empty_batch_evaluation(self):
        """Test batch evaluation with empty dataset"""
        ragas_integrator = RAGAsIntegrator()
        results = ragas_integrator.batch_evaluate([])
        assert results == []

    def test_batch_evaluation_with_mixed_data(self):
        """Test batch evaluation with mixed valid and invalid data"""
        ragas_integrator = RAGAsIntegrator()
        valid_query = TestDataQuery(
            query="Valid query",
            contexts=["Context"],
            answer="Answer",
            ground_truth="Ground truth",
            query_id="valid_001"
        )
        invalid_query = None

        results = ragas_integrator.batch_evaluate([valid_query, invalid_query])
        # Should only return results for valid queries
        assert len(results) == 1
        assert results[0] is not None

    def test_integration_success_rate_empty_dataset(self):
        """Test integration success rate calculation with empty dataset"""
        ragas_integrator = RAGAsIntegrator()
        success_rate = ragas_integrator.calculate_integration_success_rate([])
        assert success_rate == 0.0

    def test_integration_success_rate_all_failures(self):
        """Test integration success rate calculation with all failures"""
        ragas_integrator = RAGAsIntegrator()
        invalid_queries = [None, None, None]
        success_rate = ragas_integrator.calculate_integration_success_rate(invalid_queries)
        assert success_rate == 0.0

    def test_integration_success_rate_partial_success(self):
        """Test integration success rate calculation with partial success"""
        ragas_integrator = RAGAsIntegrator()
        queries = [
            TestDataQuery("Query 1", ["ctx"], "ans", "truth", "q1"),  # Valid
            None,  # Invalid
            TestDataQuery("Query 2", ["ctx"], "ans", "truth", "q2"),  # Valid
            None   # Invalid
        ]
        success_rate = ragas_integrator.calculate_integration_success_rate(queries)
        assert success_rate == 0.5  # 2 out of 4 successful

    def test_get_supported_metrics(self):
        """Test getting supported metrics"""
        ragas_integrator = RAGAsIntegrator()
        metrics = ragas_integrator.get_supported_metrics()

        assert "retrieval_metrics" in metrics
        assert "generation_metrics" in metrics
        assert isinstance(metrics["retrieval_metrics"], list)
        assert isinstance(metrics["generation_metrics"], list)
        assert len(metrics["retrieval_metrics"]) > 0
        assert len(metrics["generation_metrics"]) > 0

    def test_configuration_update(self):
        """Test configuration updates"""
        ragas_integrator = RAGAsIntegrator()

        # Test initial configuration
        assert ragas_integrator.config["model"] == "default"
        assert "metrics" in ragas_integrator.config

        # Test configuration update
        new_config = {
            "model": "gpt-4",
            "metrics": ["retrieval", "generation", "custom"],
            "language": "chinese"
        }
        ragas_integrator.configure_evaluation(new_config)

        assert ragas_integrator.config["model"] == "gpt-4"
        assert ragas_integrator.config["metrics"] == ["retrieval", "generation", "custom"]
        assert ragas_integrator.config["language"] == "chinese"

    def test_configuration_partial_update(self):
        """Test partial configuration update"""
        ragas_integrator = RAGAsIntegrator()
        original_language = ragas_integrator.config["language"]

        # Update only one field
        ragas_integrator.configure_evaluation({"model": "new-model"})

        assert ragas_integrator.config["model"] == "new-model"
        assert ragas_integrator.config["language"] == original_language  # Unchanged

    def test_configuration_validation_missing_model(self):
        """Test configuration validation with missing model"""
        ragas_integrator = RAGAsIntegrator()
        ragas_integrator.config = {"metrics": ["retrieval"]}  # Missing model

        validation = ragas_integrator.validate_configuration()
        assert validation["is_valid"] is False
        assert any("model" in error for error in validation["errors"])

    def test_configuration_validation_missing_metrics(self):
        """Test configuration validation with missing metrics"""
        ragas_integrator = RAGAsIntegrator()
        ragas_integrator.config = {"model": "gpt-4"}  # Missing metrics

        validation = ragas_integrator.validate_configuration()
        assert validation["is_valid"] is False
        assert any("metrics" in error for error in validation["errors"])

    def test_configuration_validation_valid(self):
        """Test configuration validation with valid configuration"""
        ragas_integrator = RAGAsIntegrator()
        ragas_integrator.config = {
            "model": "gpt-4",
            "metrics": ["retrieval", "generation"],
            "language": "english"
        }

        validation = ragas_integrator.validate_configuration()
        assert validation["is_valid"] is True
        assert len(validation["errors"]) == 0

    def test_standardize_data_format_with_minimal_data(self):
        """Test data standardization with minimal data"""
        ragas_integrator = RAGAsIntegrator()
        raw_data = {"query": "What is AI?"}  # Minimal data

        standardized = ragas_integrator.standardize_data_format(raw_data)

        assert standardized["query"] == "What is AI?"
        assert standardized["contexts"] == []
        assert standardized["answer"] == ""
        assert standardized["ground_truth"] == ""
        assert "metadata" in standardized

    def test_standardize_data_format_with_all_fields(self):
        """Test data standardization with all fields"""
        ragas_integrator = RAGAsIntegrator()
        raw_data = {
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence",
            "metadata": {"category": "test"}
        }

        standardized = ragas_integrator.standardize_data_format(raw_data)

        assert standardized["query"] == "What is AI?"
        assert standardized["contexts"] == ["AI is artificial intelligence"]
        assert standardized["answer"] == "AI stands for artificial intelligence"
        assert standardized["ground_truth"] == "AI is artificial intelligence"
        assert standardized["metadata"] == {"category": "test"}

    def test_standardize_data_format_with_expected_answer_alias(self):
        """Test data standardization with expected_answer alias"""
        ragas_integrator = RAGAsIntegrator()
        raw_data = {
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "expected_answer": "AI is artificial intelligence"  # Alias for ground_truth
        }

        standardized = ragas_integrator.standardize_data_format(raw_data)

        assert standardized["ground_truth"] == "AI is artificial intelligence"

    def test_separated_report_with_none_result(self):
        """Test separated report generation with None result"""
        ragas_integrator = RAGAsIntegrator()
        report = ragas_integrator.generate_separated_report(None)

        assert report["retrieval_report"] == {}
        assert report["generation_report"] == {}
        assert "error" in report["summary"]
        assert report["summary"]["error"] == "No evaluation result"

    def test_evaluation_result_structure(self):
        """Test evaluation result structure and content"""
        ragas_integrator = RAGAsIntegrator()
        query = TestDataQuery(
            query="What is AI?",
            contexts=["AI is artificial intelligence"],
            answer="AI stands for artificial intelligence",
            ground_truth="AI is artificial intelligence",
            query_id="test_001"
        )

        result = ragas_integrator.evaluate_with_ragas(query)

        assert result is not None
        assert hasattr(result, 'retrieval_metrics')
        assert hasattr(result, 'generation_metrics')
        assert hasattr(result, 'overall_score')
        assert hasattr(result, 'metadata')

        # Check metrics are within valid range
        for metric_value in result.retrieval_metrics.values():
            assert 0.0 <= metric_value <= 1.0

        for metric_value in result.generation_metrics.values():
            assert 0.0 <= metric_value <= 1.0

        assert 0.0 <= result.overall_score <= 1.0

    def test_separated_report_content_structure(self):
        """Test separated report content structure"""
        ragas_integrator = RAGAsIntegrator()
        query = TestDataQuery(
            query="What is AI?",
            contexts=["AI is artificial intelligence"],
            answer="AI stands for artificial intelligence",
            ground_truth="AI is artificial intelligence",
            query_id="test_001"
        )

        report = ragas_integrator.generate_separated_report(query)

        # Check retrieval report structure
        retrieval_report = report["retrieval_report"]
        assert "retrieval_metrics" in retrieval_report
        assert "retrieval_performance" in retrieval_report
        assert "retrieval_recommendations" in retrieval_report

        # Check generation report structure
        generation_report = report["generation_report"]
        assert "generation_metrics" in generation_report
        assert "generation_performance" in generation_report
        assert "generation_recommendations" in generation_report

        # Check summary structure
        summary = report["summary"]
        assert "overall_score" in summary
        assert "evaluation_status" in summary
        assert "total_metrics" in summary
        assert "processing_time_ms" in summary

    def test_metadata_content(self):
        """Test metadata content in evaluation results"""
        ragas_integrator = RAGAsIntegrator()
        query = TestDataQuery(
            query="What is AI?",
            contexts=["AI is artificial intelligence"],
            answer="AI stands for artificial intelligence",
            ground_truth="AI is artificial intelligence",
            query_id="test_001"
        )

        result = ragas_integrator.evaluate_with_ragas(query)

        assert result.metadata is not None
        assert "model_used" in result.metadata
        assert "evaluation_type" in result.metadata
        assert "query_processed" in result.metadata
        assert result.metadata["query_processed"] is True

    def test_metric_separation_ensure_no_overlap(self):
        """Test that retrieval and generation metrics are properly separated"""
        ragas_integrator = RAGAsIntegrator()
        query = TestDataQuery(
            query="What is AI?",
            contexts=["AI is artificial intelligence"],
            answer="AI stands for artificial intelligence",
            ground_truth="AI is artificial intelligence",
            query_id="test_001"
        )

        metrics = ragas_integrator.get_separated_metrics(query)

        retrieval_keys = set(metrics["retrieval_metrics"].keys())
        generation_keys = set(metrics["generation_metrics"].keys())

        # Ensure no overlap between metric names
        overlap = retrieval_keys.intersection(generation_keys)
        assert len(overlap) == 0, f"Found overlapping metric names: {overlap}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])