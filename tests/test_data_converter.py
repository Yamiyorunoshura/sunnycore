"""
Test cases for Data Converter functionality - Task 5 brownfield improvement
Tests for data format conversion between different RAG integration structures
"""

import pytest
import json
import tempfile
import os
from typing import List, Dict, Any

from src.rag_integration.data_converter import DataConverter, StandardizedQuery


class TestDataConverter:
    """Test suite for DataConverter functionality"""

    @pytest.fixture
    def data_converter(self):
        """Create DataConverter instance"""
        return DataConverter()

    def test_initialization(self, data_converter):
        """Test data converter initialization"""
        assert data_converter.supported_formats == ["json", "dict", "list"]
        assert len(data_converter.supported_formats) == 3

    def test_convert_dict_to_standardized_single_query(self, data_converter):
        """Test converting single query dict to standardized format"""
        raw_data = {
            "query_id": "test_001",
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence"
        }

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 1, "Should return one standardized query"
        assert isinstance(result[0], StandardizedQuery), "Should return StandardizedQuery object"
        assert result[0].query_id == "test_001", "Query ID should be preserved"
        assert result[0].query == "What is AI?", "Query text should be preserved"
        assert result[0].contexts == ["AI is artificial intelligence"], "Contexts should be preserved"
        assert result[0].answer == "AI stands for artificial intelligence", "Answer should be preserved"
        assert result[0].ground_truth == "AI is artificial intelligence", "Ground truth should be preserved"

    def test_convert_dict_to_standardized_multiple_queries(self, data_converter):
        """Test converting multiple queries dict to standardized format"""
        raw_data = {
            "queries": [
                {
                    "query_id": "test_001",
                    "query": "What is AI?",
                    "contexts": ["AI is artificial intelligence"],
                    "answer": "AI stands for artificial intelligence",
                    "ground_truth": "AI is artificial intelligence"
                },
                {
                    "query_id": "test_002",
                    "query": "What is ML?",
                    "contexts": ["ML is machine learning"],
                    "answer": "ML stands for machine learning",
                    "ground_truth": "ML is machine learning"
                }
            ]
        }

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 2, "Should return two standardized queries"
        assert result[0].query_id == "test_001", "First query ID should be preserved"
        assert result[1].query_id == "test_002", "Second query ID should be preserved"

    def test_convert_list_to_standardized(self, data_converter):
        """Test converting list of queries to standardized format"""
        raw_data = [
            {
                "query_id": "test_001",
                "query": "What is AI?",
                "contexts": ["AI is artificial intelligence"],
                "answer": "AI stands for artificial intelligence",
                "ground_truth": "AI is artificial intelligence"
            },
            {
                "query_id": "test_002",
                "query": "What is ML?",
                "contexts": ["ML is machine learning"],
                "answer": "ML stands for machine learning",
                "ground_truth": "ML is machine learning"
            }
        ]

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 2, "Should return two standardized queries"
        assert all(isinstance(item, StandardizedQuery) for item in result), "All items should be StandardizedQuery"

    def test_convert_json_string_to_standardized(self, data_converter):
        """Test converting JSON string to standardized format"""
        json_data = json.dumps({
            "query_id": "test_001",
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence"
        })

        result = data_converter.convert_to_standardized_format(json_data)

        assert len(result) == 1, "Should return one standardized query"
        assert isinstance(result[0], StandardizedQuery), "Should return StandardizedQuery object"
        assert result[0].query_id == "test_001", "Query ID should be preserved"

    def test_convert_invalid_json_string(self, data_converter):
        """Test handling of invalid JSON string"""
        invalid_json = "invalid json string"

        with pytest.raises(ValueError, match="Invalid JSON string provided"):
            data_converter.convert_to_standardized_format(invalid_json)

    def test_convert_unsupported_format(self, data_converter):
        """Test handling of unsupported format"""
        unsupported_data = 123  # Integer input

        with pytest.raises(ValueError):
            data_converter.convert_to_standardized_format(unsupported_data)

    def test_convert_with_metadata(self, data_converter):
        """Test conversion with metadata preservation"""
        raw_data = {
            "query_id": "test_001",
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence",
            "metadata": {"category": "AI", "difficulty": "easy"}
        }

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 1, "Should return one standardized query"
        assert result[0].metadata == {"category": "AI", "difficulty": "easy"}, "Metadata should be preserved"

    def test_convert_with_missing_fields(self, data_converter):
        """Test conversion with missing required fields"""
        # Test with minimal data
        minimal_data = {
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence"
        }

        result = data_converter.convert_to_standardized_format(minimal_data)

        assert len(result) == 1, "Should still return one standardized query"
        assert result[0].query_id.startswith("query_"), "Missing query_id should get generated hash value"
        assert result[0].ground_truth == "", "Missing ground_truth should default to empty string"

    def test_standardized_query_dataclass_functionality(self):
        """Test StandardizedQuery dataclass functionality"""
        query = StandardizedQuery(
            query_id="test_001",
            query="What is AI?",
            contexts=["AI is artificial intelligence"],
            answer="AI stands for artificial intelligence",
            ground_truth="AI is artificial intelligence",
            metadata={"category": "AI"}
        )

        # Test dataclass properties
        assert query.query_id == "test_001"
        assert query.query == "What is AI?"
        assert query.contexts == ["AI is artificial intelligence"]
        assert query.answer == "AI stands for artificial intelligence"
        assert query.ground_truth == "AI is artificial intelligence"
        assert query.metadata == {"category": "AI"}

    def test_empty_list_conversion(self, data_converter):
        """Test conversion of empty list"""
        result = data_converter.convert_to_standardized_format([])
        assert len(result) == 0, "Empty list should return empty result"

    def test_convert_with_none_values(self, data_converter):
        """Test conversion with None values"""
        raw_data = {
            "query_id": None,
            "query": None,
            "contexts": None,
            "answer": None,
            "ground_truth": None
        }

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 1, "Should return one standardized query"
        assert result[0].query_id is None, "None values should be preserved"

    def test_large_dataset_conversion_performance(self, data_converter):
        """Test performance with large dataset"""
        # Create large dataset
        large_data = [
            {
                "query_id": f"test_{i:03d}",
                "query": f"What is concept {i}?",
                "contexts": [f"Context about concept {i}"],
                "answer": f"Answer about concept {i}",
                "ground_truth": f"Truth about concept {i}"
            }
            for i in range(100)
        ]

        import time
        start_time = time.time()
        result = data_converter.convert_to_standardized_format(large_data)
        end_time = time.time()

        assert len(result) == 100, "Should convert all 100 items"
        assert end_time - start_time < 1.0, "Conversion should complete within 1 second"
        assert all(isinstance(item, StandardizedQuery) for item in result), "All items should be StandardizedQuery"

    def test_nested_metadata_handling(self, data_converter):
        """Test handling of nested metadata structures"""
        raw_data = {
            "query_id": "test_001",
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence",
            "metadata": {
                "category": "AI",
                "tags": ["technology", "computer_science"],
                "difficulty": {"level": "easy", "score": 1}
            }
        }

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 1, "Should return one standardized query"
        assert result[0].metadata["category"] == "AI", "Top-level metadata should be preserved"
        assert result[0].metadata["tags"] == ["technology", "computer_science"], "List metadata should be preserved"
        assert result[0].metadata["difficulty"]["level"] == "easy", "Nested metadata should be preserved"

    def test_export_to_json(self, data_converter):
        """Test JSON export functionality"""
        query = StandardizedQuery(
            query_id="test_001",
            query="What is AI?",
            contexts=["AI is artificial intelligence"],
            answer="AI stands for artificial intelligence",
            ground_truth="AI is artificial intelligence",
            metadata={"category": "AI"}
        )

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            file_path = f.name

        try:
            data_converter.export_to_json([query], file_path)

            # Verify file was created and contains correct data
            with open(file_path, 'r') as f:
                exported_data = json.load(f)

            assert len(exported_data) == 1
            assert exported_data[0]["query_id"] == "test_001"
            assert exported_data[0]["query"] == "What is AI?"
        finally:
            os.unlink(file_path)

    def test_export_to_json_dict_data(self, data_converter):
        """Test JSON export with dictionary data"""
        dict_data = {"key": "value", "number": 42}

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            file_path = f.name

        try:
            data_converter.export_to_json(dict_data, file_path)

            # Verify file was created and contains correct data
            with open(file_path, 'r') as f:
                exported_data = json.load(f)

            assert exported_data["key"] == "value"
            assert exported_data["number"] == 42
        finally:
            os.unlink(file_path)

    def test_load_from_json(self, data_converter):
        """Test JSON load functionality"""
        test_data = {
            "query_id": "test_001",
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence"
        }

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump(test_data, f)
            file_path = f.name

        try:
            result = data_converter.load_from_json(file_path)

            assert len(result) == 1
            assert result[0].query_id == "test_001"
            assert result[0].query == "What is AI?"
        finally:
            os.unlink(file_path)

    def test_load_from_json_file_not_found(self, data_converter):
        """Test handling of file not found error"""
        with pytest.raises(FileNotFoundError, match="File not found: nonexistent.json"):
            data_converter.load_from_json("nonexistent.json")

    def test_load_from_json_invalid_json(self, data_converter):
        """Test handling of invalid JSON file"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            f.write("invalid json content")
            file_path = f.name

        try:
            with pytest.raises(ValueError, match="Invalid JSON file"):
                data_converter.load_from_json(file_path)
        finally:
            os.unlink(file_path)

    def test_validate_data_format_valid(self, data_converter):
        """Test data format validation with valid data"""
        valid_data = {
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence"  # Include to avoid warning
        }

        result = data_converter.validate_data_format(valid_data)

        assert result["is_valid"] is True
        assert len(result["errors"]) == 0
        assert len(result["warnings"]) == 0

    def test_validate_data_format_missing_fields(self, data_converter):
        """Test data format validation with missing required fields"""
        invalid_data = {
            "query": "What is AI?"
            # Missing 'contexts' and 'answer'
        }

        result = data_converter.validate_data_format(invalid_data)

        assert result["is_valid"] is False
        assert len(result["errors"]) == 2
        assert any("Missing required field: contexts" in error for error in result["errors"])
        assert any("Missing required field: answer" in error for error in result["errors"])

    def test_validate_data_format_invalid_types(self, data_converter):
        """Test data format validation with invalid field types"""
        invalid_data = {
            "query": 123,  # Should be string
            "contexts": "not a list",  # Should be list
            "answer": ["not", "a", "string"]  # Should be string
        }

        result = data_converter.validate_data_format(invalid_data)

        assert result["is_valid"] is False
        assert len(result["errors"]) == 3
        assert any("Query must be a string" in error for error in result["errors"])
        assert any("Contexts must be a list" in error for error in result["errors"])
        assert any("Answer must be a string" in error for error in result["errors"])

    def test_validate_data_format_missing_ground_truth(self, data_converter):
        """Test data format validation with missing ground truth (warning only)"""
        data_without_ground_truth = {
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence"
            # Missing ground_truth
        }

        result = data_converter.validate_data_format(data_without_ground_truth)

        assert result["is_valid"] is True
        assert len(result["errors"]) == 0
        assert len(result["warnings"]) == 1
        assert "Ground truth not provided" in result["warnings"][0]

    def test_merge_datasets(self, data_converter):
        """Test dataset merging functionality"""
        dataset1 = [
            StandardizedQuery("q1", "query1", ["ctx1"], "ans1", "truth1"),
            StandardizedQuery("q2", "query2", ["ctx2"], "ans2", "truth2")
        ]
        dataset2 = [
            StandardizedQuery("q3", "query3", ["ctx3"], "ans3", "truth3"),
            StandardizedQuery("q4", "query4", ["ctx4"], "ans4", "truth4")
        ]

        merged = data_converter.merge_datasets([dataset1, dataset2])

        assert len(merged) == 4
        assert merged[0].query_id == "q1"
        assert merged[1].query_id == "q2"
        assert merged[2].query_id == "q3"
        assert merged[3].query_id == "q4"

    def test_merge_empty_datasets(self, data_converter):
        """Test merging empty datasets"""
        empty_dataset = []
        result = data_converter.merge_datasets([empty_dataset])

        assert result == []

    def test_filter_dataset_by_length(self, data_converter):
        """Test dataset filtering by query length"""
        queries = [
            StandardizedQuery("q1", "short", ["ctx"], "ans", "truth"),
            StandardizedQuery("q2", "this is a longer query", ["ctx"], "ans", "truth"),
            StandardizedQuery("q3", "medium length query", ["ctx"], "ans", "truth")
        ]

        # Filter by minimum length
        filtered = data_converter.filter_dataset(queries, {"query_length_min": 10})
        assert len(filtered) == 2
        assert all(len(q.query) >= 10 for q in filtered)

        # Filter by maximum length
        filtered = data_converter.filter_dataset(queries, {"query_length_max": 15})
        assert len(filtered) == 1  # Only "short" (5 chars) <= 15
        assert all(len(q.query) <= 15 for q in filtered)

    def test_filter_dataset_by_category(self, data_converter):
        """Test dataset filtering by category"""
        queries = [
            StandardizedQuery("q1", "query1", ["ctx"], "ans", "truth", {"category": "AI"}),
            StandardizedQuery("q2", "query2", ["ctx"], "ans", "truth", {"category": "ML"}),
            StandardizedQuery("q3", "query3", ["ctx"], "ans", "truth", {"category": "AI"})
        ]

        filtered = data_converter.filter_dataset(queries, {"category": "AI"})
        assert len(filtered) == 2
        assert all(q.metadata["category"] == "AI" for q in filtered)

    def test_filter_dataset_no_matches(self, data_converter):
        """Test dataset filtering with no matches"""
        queries = [
            StandardizedQuery("q1", "short", ["ctx"], "ans", "truth", {"category": "AI"})
        ]

        filtered = data_converter.filter_dataset(queries, {"query_length_min": 100})
        assert len(filtered) == 0

    def test_get_dataset_statistics_empty(self, data_converter):
        """Test statistics generation with empty dataset"""
        stats = data_converter.get_dataset_statistics([])

        assert stats["total_queries"] == 0

    def test_get_dataset_statistics_with_data(self, data_converter):
        """Test statistics generation with data"""
        queries = [
            StandardizedQuery("q1", "short", ["ctx1", "ctx2"], "short answer", "truth", {"category": "AI"}),
            StandardizedQuery("q2", "much longer query text", ["ctx"], "much longer answer text", "truth", {"category": "AI"}),
            StandardizedQuery("q3", "medium", ["ctx1", "ctx2", "ctx3"], "medium answer", "truth", {"category": "ML"})
        ]

        stats = data_converter.get_dataset_statistics(queries)

        assert stats["total_queries"] == 3
        assert stats["query_length_stats"]["min"] == 5  # "short"
        assert stats["query_length_stats"]["max"] == 22  # "much longer query text"
        assert stats["context_count_stats"]["min"] == 1
        assert stats["context_count_stats"]["max"] == 3
        assert stats["categories"]["AI"] == 2
        assert stats["categories"]["ML"] == 1

    def test_alternative_field_names(self, data_converter):
        """Test conversion with alternative field names"""
        raw_data = {
            "query": "What is AI?",
            "expected_contexts": ["AI is artificial intelligence"],  # Alternative to "contexts"
            "generated_answer": "AI stands for artificial intelligence",  # Alternative to "answer"
            "expected_answer": "AI is artificial intelligence"  # Alternative to "ground_truth"
        }

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 1
        assert result[0].contexts == ["AI is artificial intelligence"]
        assert result[0].answer == "AI stands for artificial intelligence"
        assert result[0].ground_truth == "AI is artificial intelligence"

    def test_empty_contexts_handling(self, data_converter):
        """Test handling of empty contexts"""
        raw_data = {
            "query": "What is AI?",
            "contexts": [],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence"
        }

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 1
        assert result[0].contexts == []

    def test_hash_based_query_id_generation(self, data_converter):
        """Test query ID generation using hash when not provided"""
        raw_data = {
            "query": "What is AI?",
            "contexts": ["AI is artificial intelligence"],
            "answer": "AI stands for artificial intelligence",
            "ground_truth": "AI is artificial intelligence"
        }

        result = data_converter.convert_to_standardized_format(raw_data)

        assert len(result) == 1
        assert result[0].query_id.startswith("query_")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])