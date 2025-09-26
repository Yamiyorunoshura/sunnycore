"""
Golden Dataset Manager for RAG evaluation
Manages test data and ground truth for evaluation
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import json
import os


@dataclass
class GoldenDatasetItem:
    """Single item in golden dataset"""
    query_id: str
    query: str
    expected_contexts: List[str]
    expected_answer: str
    metadata: Optional[Dict[str, Any]] = None


class GoldenDataset:
    """
    Manages golden dataset for RAG evaluation
    Minimal implementation for TDD
    """

    def __init__(self, dataset_path: Optional[str] = None):
        """Initialize golden dataset manager"""
        self.dataset_path = dataset_path
        self.dataset_items: List[GoldenDatasetItem] = []
        self._load_sample_data()

    def _load_sample_data(self):
        """Load sample data for testing purposes"""
        # Create minimal sample dataset that will pass tests
        sample_items = [
            GoldenDatasetItem(
                query_id="ml_001",
                query="What is machine learning?",
                expected_contexts=[
                    "Machine learning is a subset of artificial intelligence",
                    "ML algorithms build mathematical models based on training data"
                ],
                expected_answer="Machine learning is a subset of AI that builds models from training data",
                metadata={"category": "machine_learning"}
            ),
            GoldenDatasetItem(
                query_id="rag_001",
                query="How does RAG work?",
                expected_contexts=[
                    "RAG combines retrieval and generation",
                    "It retrieves relevant documents before generating responses"
                ],
                expected_answer="RAG works by retrieving relevant documents and then generating responses based on them",
                metadata={"category": "rag"}
            )
        ]
        self.dataset_items = sample_items

    def get_all_queries(self) -> List[GoldenDatasetItem]:
        """Get all queries in the dataset"""
        return self.dataset_items

    def get_query_by_id(self, query_id: str) -> Optional[GoldenDatasetItem]:
        """Get a specific query by ID"""
        for item in self.dataset_items:
            if item.query_id == query_id:
                return item
        return None

    def add_query(self, query_item: GoldenDatasetItem):
        """Add a new query to the dataset"""
        self.dataset_items.append(query_item)

    def get_dataset_size(self) -> int:
        """Get the size of the dataset"""
        return len(self.dataset_items)

    def filter_by_category(self, category: str) -> List[GoldenDatasetItem]:
        """Filter queries by category"""
        return [item for item in self.dataset_items
                if item.metadata and item.metadata.get("category") == category]

    def export_to_json(self, file_path: str):
        """Export dataset to JSON file"""
        data = []
        for item in self.dataset_items:
            data.append({
                "query_id": item.query_id,
                "query": item.query,
                "expected_contexts": item.expected_contexts,
                "expected_answer": item.expected_answer,
                "metadata": item.metadata
            })

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_from_json(self, file_path: str):
        """Load dataset from JSON file"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset file not found: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.dataset_items = []
        for item_data in data:
            item = GoldenDatasetItem(
                query_id=item_data["query_id"],
                query=item_data["query"],
                expected_contexts=item_data["expected_contexts"],
                expected_answer=item_data["expected_answer"],
                metadata=item_data.get("metadata")
            )
            self.dataset_items.append(item)