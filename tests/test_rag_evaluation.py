"""
Test cases for RAG Evaluation Framework - Task 5
Tests for retrieval layer quality assessment and RAGAs integration
"""

import pytest
import time
import json
from typing import List, Dict, Any
from dataclasses import dataclass

# Import the classes to be tested (will fail initially)
from src.rag_evaluation.ragevaluator import RAGEvaluator
from src.rag_evaluation.golden_dataset import GoldenDataset, GoldenDatasetItem
from src.rag_evaluation.metrics import MetricsCalculator
from src.rag_integration.ragas_integrator import RAGAsIntegrator


@dataclass
class TestQuery:
    """Test query data structure"""
    query: str
    expected_context: List[str]
    expected_answer: str
    query_id: str


class TestRAGEvaluation:
    """Test suite for RAG Evaluation Framework"""

    @pytest.fixture
    def sample_golden_dataset(self):
        """Create sample golden dataset for testing"""
        return [
            TestQuery(
                query="What is machine learning?",
                expected_context=[
                    "Machine learning is a subset of artificial intelligence",
                    "ML algorithms build mathematical models based on training data"
                ],
                expected_answer="Machine learning is a subset of AI that builds models from training data",
                query_id="ml_001"
            ),
            TestQuery(
                query="How does RAG work?",
                expected_context=[
                    "RAG combines retrieval and generation",
                    "It retrieves relevant documents before generating responses"
                ],
                expected_answer="RAG works by retrieving relevant documents and then generating responses based on them",
                query_id="rag_001"
            )
        ]

    @pytest.fixture
    def rag_evaluator(self):
        """Create RAGEvaluator instance"""
        return RAGEvaluator()

    @pytest.fixture
    def metrics_calculator(self):
        """Create MetricsCalculator instance"""
        return MetricsCalculator()

    @pytest.fixture
    def ragas_integrator(self):
        """Create RAGAsIntegrator instance"""
        return RAGAsIntegrator()

    def test_top_k_retrieval_hit_rate_meets_target(self, rag_evaluator, sample_golden_dataset):
        """
        Test: Top-k檢索命中率≥85%
        Method: Integration test with sample dataset
        Success metric: precision@k ≥ 0.85
        """
        # Test retrieval hit rate
        hit_rate = rag_evaluator.calculate_retrieval_hit_rate(
            queries=sample_golden_dataset,
            k=5
        )

        # Assert meets target (should fail initially)
        assert hit_rate >= 0.85, f"Retrieval hit rate {hit_rate} is below target 0.85"

    def test_context_relevance_score_meets_target(self, metrics_calculator):
        """
        Test: 上下文相關性評分≥0.8
        Method: Unit test with sample contexts
        Success metric: relevance_score ≥ 0.8
        """
        query = "What is artificial intelligence?"
        contexts = [
            "AI is the simulation of human intelligence in machines",
            "Machine learning is a subset of AI",
            "Deep learning uses neural networks"
        ]

        relevance_score = metrics_calculator.calculate_context_relevance(
            query=query,
            contexts=contexts
        )

        # Assert meets target (should fail initially)
        assert relevance_score >= 0.8, f"Context relevance score {relevance_score} is below target 0.8"

    def test_answer_faithfulness_score_meets_target(self, metrics_calculator):
        """
        Test: 答案忠誠度評分≥0.9
        Method: Unit test with sample answer and context
        Success metric: faithfulness_score ≥ 0.9
        """
        answer = "Machine learning is a subset of artificial intelligence"
        contexts = [
            "Machine learning is a subset of artificial intelligence",
            "ML algorithms learn patterns from data"
        ]

        faithfulness_score = metrics_calculator.calculate_answer_faithfulness(
            answer=answer,
            contexts=contexts
        )

        # Assert meets target (should fail initially)
        assert faithfulness_score >= 0.9, f"Answer faithfulness score {faithfulness_score} is below target 0.9"

    def test_retrieval_latency_meets_target(self, rag_evaluator):
        """
        Test: 檢索延遲<500ms
        Method: Performance test with timing
        Success metric: p95_latency < 500ms
        """
        query = "Test query for latency measurement"

        # Measure retrieval latency
        start_time = time.time()
        result = rag_evaluator.retrieve_context(query)
        end_time = time.time()

        latency_ms = (end_time - start_time) * 1000

        # Assert meets target (should fail initially)
        assert latency_ms < 500, f"Retrieval latency {latency_ms}ms exceeds target 500ms"

    def test_full_test_suite_performance_target(self, rag_evaluator, sample_golden_dataset):
        """
        Test: Performance目標：p95延遲<5000ms for full test suite
        Method: Load test with full dataset
        Success metric: Full suite execution < 5000ms
        """
        start_time = time.time()

        # Execute full test suite
        for query in sample_golden_dataset:
            rag_evaluator.evaluate_retrieval_quality(query)

        end_time = time.time()
        total_time_ms = (end_time - start_time) * 1000

        # Assert meets target (should fail initially)
        assert total_time_ms < 5000, f"Full test suite time {total_time_ms}ms exceeds target 5000ms"

    def test_ragas_integration_success_rate(self, ragas_integrator, sample_golden_dataset):
        """
        Test: RAGAs集成成功率100%
        Method: Integration test with RAGAs tool
        Success metric: integration_success_rate = 100%
        """
        successful_integrations = 0
        total_integrations = len(sample_golden_dataset)

        for query in sample_golden_dataset:
            try:
                result = ragas_integrator.evaluate_with_ragas(query)
                if result is not None:
                    successful_integrations += 1
            except Exception:
                # Integration failed
                pass

        success_rate = successful_integrations / total_integrations

        # Assert meets target (should fail initially)
        assert success_rate == 1.0, f"RAGAs integration success rate {success_rate} is below target 1.0"

    def test_independent_retrieval_generation_metrics(self, ragas_integrator):
        """
        Test: 獨立指標計算
        Method: Unit test for separated metrics
        Success metric: retrieval_generation_separation = true
        """
        query = "Test query for metric separation"

        # Get separated metrics
        metrics = ragas_integrator.get_separated_metrics(query)

        # Assert both retrieval and generation metrics are present and separate
        assert "retrieval_metrics" in metrics, "Retrieval metrics not found"
        assert "generation_metrics" in metrics, "Generation metrics not found"
        assert isinstance(metrics["retrieval_metrics"], dict), "Retrieval metrics should be a dictionary"
        assert isinstance(metrics["generation_metrics"], dict), "Generation metrics should be a dictionary"

    def test_data_standardization_compliance(self, ragas_integrator):
        """
        Test: 標準化數據集
        Method: Validation test for data format
        Success metric: data_standardization_compliance = 100%
        """
        sample_data = {
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence"
        }

        # Test data standardization
        standardized = ragas_integrator.standardize_data_format(sample_data)

        # Check required fields
        required_fields = ["query", "contexts", "answer", "ground_truth"]
        for field in required_fields:
            assert field in standardized, f"Required field {field} missing from standardized data"

    def test_report_separation_accuracy(self, ragas_integrator):
        """
        Test: 分離式報告生成
        Method: Output test for report structure
        Success metric: report_separation_accuracy = 100%
        """
        query = "Test query for report separation"

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


class TestRAGEvaluationEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_empty_query_handling(self):
        """Test handling of empty queries"""
        rag_evaluator = RAGEvaluator()
        with pytest.raises(ValueError):
            rag_evaluator.evaluate_retrieval_quality("")

    def test_empty_context_handling(self):
        """Test handling of empty contexts"""
        metrics_calculator = MetricsCalculator()
        query = "What is AI?"
        contexts = []

        relevance_score = metrics_calculator.calculate_context_relevance(query, contexts)
        assert relevance_score == 0.0, "Empty contexts should return relevance score of 0"

    def test_single_context_scenario(self):
        """Test scenario with single context"""
        metrics_calculator = MetricsCalculator()
        query = "What is AI?"
        contexts = ["AI stands for artificial intelligence"]

        relevance_score = metrics_calculator.calculate_context_relevance(query, contexts)
        assert 0.0 <= relevance_score <= 1.0, "Relevance score should be between 0 and 1"

    def test_large_dataset_performance(self):
        """Test performance with larger dataset"""
        rag_evaluator = RAGEvaluator()
        # Create large dataset
        large_dataset = [
            TestQuery(
                query=f"Test query {i}",
                expected_context=[f"Context {i}"],
                expected_answer=f"Answer {i}",
                query_id=f"test_{i}"
            )
            for i in range(100)
        ]

        start_time = time.time()
        hit_rate = rag_evaluator.calculate_retrieval_hit_rate(large_dataset, k=5)
        end_time = time.time()

        execution_time = end_time - start_time

        # Should complete within reasonable time (adjust based on requirements)
        assert execution_time < 30.0, f"Large dataset processing took {execution_time}s, too slow"
        assert 0.0 <= hit_rate <= 1.0, "Hit rate should be between 0 and 1"


class TestGoldenDataset:
    """Test suite for GoldenDataset functionality"""

    @pytest.fixture
    def golden_dataset(self):
        """Create GoldenDataset instance"""
        return GoldenDataset()

    def test_initialization_with_sample_data(self, golden_dataset):
        """Test golden dataset initialization loads sample data"""
        items = golden_dataset.get_all_queries()
        assert len(items) == 2, "Should have 2 sample items"
        assert items[0].query_id == "ml_001", "First item should be ml_001"
        assert items[1].query_id == "rag_001", "Second item should be rag_001"

    def test_get_query_by_id_existing(self, golden_dataset):
        """Test getting existing query by ID"""
        query = golden_dataset.get_query_by_id("ml_001")
        assert query is not None, "Should find query with ml_001"
        assert query.query == "What is machine learning?", "Should return correct query"

    def test_get_query_by_id_nonexistent(self, golden_dataset):
        """Test getting nonexistent query by ID"""
        query = golden_dataset.get_query_by_id("nonexistent")
        assert query is None, "Should return None for nonexistent ID"

    def test_add_query(self, golden_dataset):
        """Test adding a new query to dataset"""
        initial_size = golden_dataset.get_dataset_size()

        new_item = GoldenDatasetItem(
            query_id="test_001",
            query="Test query?",
            expected_contexts=["Test context"],
            expected_answer="Test answer"
        )

        golden_dataset.add_query(new_item)
        new_size = golden_dataset.get_dataset_size()

        assert new_size == initial_size + 1, "Dataset size should increase by 1"

        added_query = golden_dataset.get_query_by_id("test_001")
        assert added_query is not None, "Should find newly added query"
        assert added_query.query == "Test query?", "Should have correct query text"

    def test_filter_by_category(self, golden_dataset):
        """Test filtering queries by category"""
        ml_items = golden_dataset.filter_by_category("machine_learning")
        rag_items = golden_dataset.filter_by_category("rag")
        nonexistent_items = golden_dataset.filter_by_category("nonexistent")

        assert len(ml_items) == 1, "Should find 1 machine learning item"
        assert ml_items[0].query_id == "ml_001", "Should find correct ML item"

        assert len(rag_items) == 1, "Should find 1 RAG item"
        assert rag_items[0].query_id == "rag_001", "Should find correct RAG item"

        assert len(nonexistent_items) == 0, "Should find no items for nonexistent category"

    def test_export_to_json(self, golden_dataset, tmp_path):
        """Test exporting dataset to JSON file"""
        export_file = tmp_path / "test_export.json"
        golden_dataset.export_to_json(str(export_file))

        assert export_file.exists(), "Export file should be created"

        # Verify file content
        with open(export_file, 'r') as f:
            data = json.load(f)

        assert len(data) == 2, "Export should have 2 items"
        assert data[0]["query_id"] == "ml_001", "First item should be ml_001"
        assert data[1]["query_id"] == "rag_001", "Second item should be rag_001"

    def test_load_from_json(self, tmp_path):
        """Test loading dataset from JSON file"""
        # Create test data file
        test_data = [
            {
                "query_id": "test_001",
                "query": "Test query from file?",
                "expected_contexts": ["Test context from file"],
                "expected_answer": "Test answer from file",
                "metadata": {"category": "test"}
            }
        ]

        data_file = tmp_path / "test_data.json"
        with open(data_file, 'w') as f:
            json.dump(test_data, f)

        # Load dataset
        dataset = GoldenDataset()
        dataset.load_from_json(str(data_file))

        items = dataset.get_all_queries()
        assert len(items) == 1, "Should have 1 item from file"
        assert items[0].query_id == "test_001", "Should have correct query ID"
        assert items[0].query == "Test query from file?", "Should have correct query text"

    def test_load_from_json_nonexistent_file(self):
        """Test loading from nonexistent file raises error"""
        dataset = GoldenDataset()
        with pytest.raises(FileNotFoundError):
            dataset.load_from_json("/nonexistent/file.json")

    def test_filter_by_category_no_metadata(self, golden_dataset):
        """Test filtering when item has no metadata"""
        # Add item without metadata
        item_no_metadata = GoldenDatasetItem(
            query_id="no_meta_001",
            query="Query without metadata",
            expected_contexts=["Context"],
            expected_answer="Answer",
            metadata=None
        )
        golden_dataset.add_query(item_no_metadata)

        # Should not be included in any category filter
        ml_items = golden_dataset.filter_by_category("machine_learning")
        assert len(ml_items) == 1, "Should still only find original ML item"


class TestMetricsCalculator:
    """Test suite for MetricsCalculator functionality"""

    @pytest.fixture
    def metrics_calculator(self):
        """Create MetricsCalculator instance"""
        return MetricsCalculator()

    def test_precision_at_k_calculation(self, metrics_calculator):
        """Test precision@k calculation"""
        retrieved_docs = ["doc1", "doc2", "doc3", "doc4", "doc5"]
        relevant_docs = ["doc1", "doc3", "doc5"]

        # Test precision@5
        precision_5 = metrics_calculator.calculate_precision_at_k(retrieved_docs, relevant_docs, 5)
        assert precision_5 == 0.6, "Precision@5 should be 3/5 = 0.6"

        # Test precision@3
        precision_3 = metrics_calculator.calculate_precision_at_k(retrieved_docs, relevant_docs, 3)
        assert precision_3 == 0.6666666666666666, "Precision@3 should be 2/3 ≈ 0.67"

        # Test edge case: k=0
        precision_0 = metrics_calculator.calculate_precision_at_k(retrieved_docs, relevant_docs, 0)
        assert precision_0 == 0.0, "Precision@0 should be 0"

    def test_recall_at_k_calculation(self, metrics_calculator):
        """Test recall@k calculation"""
        retrieved_docs = ["doc1", "doc2", "doc3"]
        relevant_docs = ["doc1", "doc3", "doc5", "doc7"]

        recall_3 = metrics_calculator.calculate_recall_at_k(retrieved_docs, relevant_docs, 3)
        assert recall_3 == 0.5, "Recall@3 should be 2/4 = 0.5"

        # Test when all relevant docs are retrieved
        recall_all = metrics_calculator.calculate_recall_at_k(relevant_docs, relevant_docs, 10)
        assert recall_all == 1.0, "Recall should be 1.0 when all relevant docs retrieved"

    def test_f1_score_calculation(self, metrics_calculator):
        """Test F1 score calculation"""
        # Test perfect F1
        f1_perfect = metrics_calculator.calculate_f1_score(1.0, 1.0)
        assert f1_perfect == 1.0, "F1 score should be 1.0 for perfect precision and recall"

        # Test zero case
        f1_zero = metrics_calculator.calculate_f1_score(0.0, 0.0)
        assert f1_zero == 0.0, "F1 score should be 0.0 for zero precision and recall"

        # Test balanced case
        f1_balanced = metrics_calculator.calculate_f1_score(0.8, 0.8)
        assert abs(f1_balanced - 0.8) < 0.001, "F1 score should equal precision and recall when they're equal"

    def test_normalized_dcg_calculation(self, metrics_calculator):
        """Test Normalized DCG calculation"""
        retrieved_docs = ["doc1", "doc2", "doc3", "doc4", "doc5"]
        relevant_docs = ["doc1", "doc3", "doc5"]

        ndcg_5 = metrics_calculator.calculate_normalized_dcg(retrieved_docs, relevant_docs, 5)
        assert 0.0 <= ndcg_5 <= 1.0, "NDCG should be between 0 and 1"

        # Test with perfect ranking
        perfect_ranking = ["doc1", "doc3", "doc5", "doc2", "doc4"]
        ndcg_perfect = metrics_calculator.calculate_normalized_dcg(perfect_ranking, relevant_docs, 5)
        assert ndcg_perfect == 1.0, "NDCG should be 1.0 for perfect ranking"

        # Test with no relevant docs
        ndcg_none = metrics_calculator.calculate_normalized_dcg(retrieved_docs, [], 5)
        assert ndcg_none == 0.0, "NDCG should be 0.0 when no relevant docs"

    def test_comprehensive_metrics_calculation(self, metrics_calculator):
        """Test comprehensive metrics calculation"""
        query = "What is artificial intelligence?"
        retrieved_contexts = ["AI is machine intelligence", "ML is subset of AI", "Neural networks mimic brain"]
        expected_contexts = ["AI is machine intelligence", "ML is subset of AI"]
        answer = "AI is machine intelligence"

        metrics = metrics_calculator.calculate_comprehensive_metrics(
            query, retrieved_contexts, expected_contexts, answer
        )

        # Verify all metric types are present
        assert "context_relevance" in metrics, "Should have context relevance metric"
        assert "answer_faithfulness" in metrics, "Should have answer faithfulness metric"
        assert "retrieval_quality" in metrics, "Should have retrieval quality metric"

        # Verify metric structure
        for metric_name, metric_result in metrics.items():
            assert hasattr(metric_result, 'score'), f"Metric {metric_name} should have score"
            assert hasattr(metric_result, 'details'), f"Metric {metric_name} should have details"
            assert hasattr(metric_result, 'confidence'), f"Metric {metric_name} should have confidence"
            assert 0.0 <= metric_result.score <= 1.0, f"Metric {metric_name} score should be between 0 and 1"

    def test_metrics_threshold_validation(self, metrics_calculator):
        """Test metrics threshold validation"""
        query = "What is AI?"
        retrieved_contexts = ["AI is artificial intelligence"]
        expected_contexts = ["AI is artificial intelligence"]
        answer = "AI is artificial intelligence"

        metrics = metrics_calculator.calculate_comprehensive_metrics(
            query, retrieved_contexts, expected_contexts, answer
        )

        validation = metrics_calculator.validate_metrics_thresholds(metrics)

        # Check validation structure
        assert "relevance_passed" in validation, "Should have relevance validation"
        assert "faithfulness_passed" in validation, "Should have faithfulness validation"
        assert "retrieval_passed" in validation, "Should have retrieval validation"

        # All should pass with good data
        assert all(validation.values()), "All metrics should pass with good data"

    def test_empty_input_handling(self, metrics_calculator):
        """Test handling of empty inputs"""
        # Test empty contexts
        relevance_empty = metrics_calculator.calculate_context_relevance("query", [])
        assert relevance_empty == 0.0, "Empty contexts should return relevance 0.0"

        # Test empty answer
        faithfulness_empty = metrics_calculator.calculate_answer_faithfulness("", ["context"])
        assert faithfulness_empty == 0.0, "Empty answer should return faithfulness 0.0"

        # Test precision with empty retrieved docs
        precision_empty = metrics_calculator.calculate_precision_at_k([], ["relevant"], 5)
        assert precision_empty == 0.0, "Empty retrieved docs should return precision 0.0"

        # Test recall with empty relevant docs
        recall_empty = metrics_calculator.calculate_recall_at_k(["doc"], [], 5)
        assert recall_empty == 0.0, "Empty relevant docs should return recall 0.0"


class TestRAGEvaluatorExtended:
    """Extended test suite for RAGEvaluator uncovered methods"""

    @pytest.fixture
    def rag_evaluator(self):
        """Create RAGEvaluator instance"""
        return RAGEvaluator()

    def test_empty_queries_handling(self, rag_evaluator):
        """Test handling of empty queries list"""
        hit_rate = rag_evaluator.calculate_retrieval_hit_rate([], k=5)
        assert hit_rate == 0.0, "Empty queries should return hit rate 0.0"

    def test_invalid_k_value_handling(self, rag_evaluator):
        """Test handling of invalid k values"""
        queries = ["query1", "query2"]

        # Test k=0
        with pytest.raises(ValueError, match="k must be greater than 0"):
            rag_evaluator.calculate_retrieval_hit_rate(queries, k=0)

        # Test negative k
        with pytest.raises(ValueError, match="k must be greater than 0"):
            rag_evaluator.calculate_retrieval_hit_rate(queries, k=-1)

    def test_empty_query_relevance_calculation(self, rag_evaluator):
        """Test relevance calculation for empty query"""
        relevance = rag_evaluator._calculate_query_relevance("")
        assert relevance == 0.0, "Empty query should return relevance 0.0"

        relevance_none = rag_evaluator._calculate_query_relevance(None)
        assert relevance_none == 0.0, "None query should return relevance 0.0"

    def test_empty_string_query_handling(self, rag_evaluator):
        """Test handling of empty string queries in retrieve_context"""
        with pytest.raises(ValueError, match="Query cannot be empty"):
            rag_evaluator.retrieve_context("")

        with pytest.raises(ValueError, match="Query cannot be empty"):
            rag_evaluator.retrieve_context("   ")

    def test_evaluate_retrieval_quality_with_empty_query(self, rag_evaluator):
        """Test evaluate_retrieval_quality with empty query"""
        with pytest.raises(ValueError, match="Query cannot be empty"):
            rag_evaluator.evaluate_retrieval_quality("")

    def test_full_pipeline_with_empty_queries(self, rag_evaluator):
        """Test full pipeline evaluation with empty queries"""
        result = rag_evaluator.evaluate_full_pipeline([])

        # Should return zero metrics for empty input
        assert result.retrieval_hit_rate == 0.0
        assert result.context_relevance == 0.0
        assert result.answer_faithfulness == 0.0
        assert result.latency_ms == 0.0
        assert result.metrics == {}

    def test_full_pipeline_latency_calculation(self, rag_evaluator):
        """Test that full pipeline correctly calculates latency"""
        queries = ["test query 1", "test query 2"]

        result = rag_evaluator.evaluate_full_pipeline(queries)

        # Verify latency is calculated and positive
        assert result.latency_ms > 0.0, "Latency should be positive"

        # Verify metrics include query count
        assert "queries_processed" in result.metrics
        assert result.metrics["queries_processed"] == len(queries)

        # Verify average latency is calculated
        assert "average_latency_per_query" in result.metrics
        expected_avg = result.latency_ms / len(queries)
        assert abs(result.metrics["average_latency_per_query"] - expected_avg) < 0.001

    def test_retrieval_latency_measurement(self, rag_evaluator):
        """Test retrieval latency measurement method"""
        query = "test query for latency"

        latency = rag_evaluator.calculate_retrieval_latency(query)

        # Latency should be positive and reasonable
        assert latency > 0.0, "Retrieval latency should be positive"
        assert latency < 100.0, f"Retrieval latency {latency}ms seems too high"

    def test_calculate_query_relevance_length_factor(self, rag_evaluator):
        """Test query relevance calculation with different query lengths"""
        # Short query
        short_relevance = rag_evaluator._calculate_query_relevance("AI")

        # Long query
        long_query = "What is artificial intelligence and how does it relate to machine learning and deep learning?"
        long_relevance = rag_evaluator._calculate_query_relevance(long_query)

        # Longer queries should generally have higher relevance (due to length factor)
        assert long_relevance >= short_relevance, "Longer queries should have higher or equal relevance"

        # Both should be within valid range
        assert 0.0 <= short_relevance <= 1.0, "Short query relevance should be between 0 and 1"
        assert 0.0 <= long_relevance <= 1.0, "Long query relevance should be between 0 and 1"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])