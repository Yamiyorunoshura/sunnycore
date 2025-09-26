"""
Data Converter for RAG integration
Handles format conversion between different data structures
"""

from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, asdict
import json


@dataclass
class StandardizedQuery:
    """Standardized query format"""
    query_id: str
    query: str
    contexts: List[str]
    answer: str
    ground_truth: str
    metadata: Optional[Dict[str, Any]] = None


class DataConverter:
    """
    Converts data between different formats for RAG integration
    Minimal implementation for TDD
    """

    def __init__(self):
        """Initialize data converter"""
        self.supported_formats = ["json", "dict", "list"]

    def convert_to_standardized_format(self, raw_data: Union[Dict, List, str]) -> List[StandardizedQuery]:
        """
        Convert various input formats to standardized query format
        """
        if isinstance(raw_data, str):
            # Assume JSON string
            try:
                data = json.loads(raw_data)
                return self._convert_dict_to_standardized(data)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON string provided")

        elif isinstance(raw_data, dict):
            return self._convert_dict_to_standardized(raw_data)

        elif isinstance(raw_data, list):
            return self._convert_list_to_standardized(raw_data)

        else:
            raise ValueError(f"Unsupported data type: {type(raw_data)}")

    def _convert_dict_to_standardized(self, data: Dict) -> List[StandardizedQuery]:
        """Convert dictionary to standardized format"""
        if "queries" in data:
            # Multiple queries format
            queries = []
            for item in data["queries"]:
                query = self._create_standardized_query(item)
                queries.append(query)
            return queries
        else:
            # Single query format
            return [self._create_standardized_query(data)]

    def _convert_list_to_standardized(self, data: List) -> List[StandardizedQuery]:
        """Convert list to standardized format"""
        queries = []
        for item in data:
            if isinstance(item, dict):
                query = self._create_standardized_query(item)
                queries.append(query)
            else:
                raise ValueError("List items must be dictionaries")
        return queries

    def _create_standardized_query(self, data: Dict) -> StandardizedQuery:
        """Create standardized query from dictionary"""
        return StandardizedQuery(
            query_id=data.get("query_id", f"query_{hash(data.get('query', ''))}"),
            query=data.get("query", ""),
            contexts=data.get("contexts", data.get("expected_contexts", [])),
            answer=data.get("answer", data.get("generated_answer", "")),
            ground_truth=data.get("ground_truth", data.get("expected_answer", "")),
            metadata=data.get("metadata", {})
        )

    def convert_to_ragas_format(self, standardized_queries: List[StandardizedQuery]) -> List[Dict[str, Any]]:
        """
        Convert standardized format to RAGAs format
        """
        ragas_data = []
        for query in standardized_queries:
            ragas_item = {
                "question": query.query,
                "contexts": query.contexts,
                "answer": query.answer,
                "ground_truth": query.ground_truth
            }
            ragas_data.append(ragas_item)

        return ragas_data

    def convert_to_deepeval_format(self, standardized_queries: List[StandardizedQuery]) -> List[Dict[str, Any]]:
        """
        Convert standardized format to DeepEval format
        """
        deepeval_data = []
        for query in standardized_queries:
            deepeval_item = {
                "input": query.query,
                "actual_output": query.answer,
                "expected_output": query.ground_truth,
                "context": query.contexts,
                "additional_metadata": query.metadata
            }
            deepeval_data.append(deepeval_item)

        return deepeval_data

    def export_to_json(self, data: Union[List[StandardizedQuery], Dict], file_path: str):
        """
        Export data to JSON file
        """
        if isinstance(data, list) and data and isinstance(data[0], StandardizedQuery):
            # Convert standardized queries to dict
            export_data = [asdict(query) for query in data]
        else:
            export_data = data

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

    def load_from_json(self, file_path: str) -> List[StandardizedQuery]:
        """
        Load data from JSON file and convert to standardized format
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return self.convert_to_standardized_format(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON file: {file_path}")

    def validate_data_format(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate data format and return validation result
        """
        validation_result = {
            "is_valid": True,
            "errors": [],
            "warnings": []
        }

        # Check required fields
        required_fields = ["query", "contexts", "answer"]
        for field in required_fields:
            if field not in data:
                validation_result["errors"].append(f"Missing required field: {field}")
                validation_result["is_valid"] = False

        # Check field types
        if "query" in data and not isinstance(data["query"], str):
            validation_result["errors"].append("Query must be a string")
            validation_result["is_valid"] = False

        if "contexts" in data and not isinstance(data["contexts"], list):
            validation_result["errors"].append("Contexts must be a list")
            validation_result["is_valid"] = False

        if "answer" in data and not isinstance(data["answer"], str):
            validation_result["errors"].append("Answer must be a string")
            validation_result["is_valid"] = False

        # Check for warnings
        if "ground_truth" not in data:
            validation_result["warnings"].append("Ground truth not provided - some metrics may not work")

        return validation_result

    def merge_datasets(self, datasets: List[List[StandardizedQuery]]) -> List[StandardizedQuery]:
        """
        Merge multiple datasets into one
        """
        merged = []
        for dataset in datasets:
            merged.extend(dataset)
        return merged

    def filter_dataset(self, queries: List[StandardizedQuery],
                      filter_criteria: Dict[str, Any]) -> List[StandardizedQuery]:
        """
        Filter dataset based on criteria
        """
        filtered = []
        for query in queries:
            include = True

            # Apply filters
            if "query_length_min" in filter_criteria:
                if len(query.query) < filter_criteria["query_length_min"]:
                    include = False

            if "query_length_max" in filter_criteria:
                if len(query.query) > filter_criteria["query_length_max"]:
                    include = False

            if "category" in filter_criteria and query.metadata:
                if query.metadata.get("category") != filter_criteria["category"]:
                    include = False

            if include:
                filtered.append(query)

        return filtered

    def get_dataset_statistics(self, queries: List[StandardizedQuery]) -> Dict[str, Any]:
        """
        Get basic statistics about the dataset
        """
        if not queries:
            return {"total_queries": 0}

        query_lengths = [len(q.query) for q in queries]
        context_counts = [len(q.contexts) for q in queries]
        answer_lengths = [len(q.answer) for q in queries]

        categories = {}
        for query in queries:
            if query.metadata and "category" in query.metadata:
                category = query.metadata["category"]
                categories[category] = categories.get(category, 0) + 1

        return {
            "total_queries": len(queries),
            "query_length_stats": {
                "min": min(query_lengths),
                "max": max(query_lengths),
                "avg": sum(query_lengths) / len(query_lengths)
            },
            "context_count_stats": {
                "min": min(context_counts),
                "max": max(context_counts),
                "avg": sum(context_counts) / len(context_counts)
            },
            "answer_length_stats": {
                "min": min(answer_lengths),
                "max": max(answer_lengths),
                "avg": sum(answer_lengths) / len(answer_lengths)
            },
            "categories": categories
        }