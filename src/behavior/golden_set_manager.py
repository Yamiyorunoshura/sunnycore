import json
import os
import copy
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Union
import hashlib
import shutil
import logging

class GoldenSetManager:
    """
    Golden Set Manager - Repository Pattern Implementation

    Manages version-controlled golden sets for behavioral testing with
    comprehensive test case management and validation capabilities.
    """

    def __init__(self, golden_set_path: str, backup_dir: Optional[str] = None):
        """
        Initialize Golden Set Manager

        Args:
            golden_set_path: Path to the golden set JSON file
            backup_dir: Directory for version backups (optional)
        """
        self.golden_set_path = golden_set_path
        self.backup_dir = backup_dir or os.path.join(os.path.dirname(golden_set_path), 'backups')
        self.logger = logging.getLogger(__name__)

        # Ensure backup directory exists
        os.makedirs(self.backup_dir, exist_ok=True)

        # Initialize version tracking
        self.version_history = []
        self.current_version = None

        # Load existing golden set or create new one
        self._initialize_golden_set()

    def _initialize_golden_set(self):
        """Initialize golden set file if it doesn't exist"""
        if not os.path.exists(self.golden_set_path):
            self._create_initial_golden_set()
        else:
            self._load_version_history()

    def _create_initial_golden_set(self):
        """Create initial golden set structure"""
        initial_golden_set = {
            "version": "1.0.0",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "test_cases": [],
            "metadata": {
                "total_cases": 0,
                "coverage_target": 0.95,
                "last_updated": datetime.now(timezone.utc).isoformat(),
                "categories": {},
                "priorities": {}
            }
        }

        self._save_golden_set(initial_golden_set)
        self.current_version = "1.0.0"

    def _load_version_history(self):
        """Load version history from backups"""
        if os.path.exists(self.backup_dir):
            for filename in os.listdir(self.backup_dir):
                if filename.endswith('.json'):
                    version = filename.replace('golden_set_v', '').replace('.json', '')
                    if version != 'current':
                        self.version_history.append({
                            'version': version,
                            'timestamp': datetime.fromtimestamp(
                                os.path.getmtime(os.path.join(self.backup_dir, filename))
                            ).isoformat()
                        })

        # Sort by version (simple string comparison for now)
        self.version_history.sort(key=lambda x: x['version'], reverse=True)

    def load_golden_set(self) -> Dict[str, Any]:
        """
        Load golden set from file

        Returns:
            Dict containing golden set data
        """
        try:
            with open(self.golden_set_path, 'r', encoding='utf-8') as f:
                golden_set = json.load(f)

            self.current_version = golden_set.get('version', '1.0.0')
            return golden_set
        except (json.JSONDecodeError, FileNotFoundError) as e:
            self.logger.error(f"Error loading golden set: {e}")
            raise

    def _save_golden_set(self, golden_set: Dict[str, Any]):
        """Save golden set to file with backup"""
        # Create backup before saving
        self._create_backup(golden_set)

        # Save current version
        with open(self.golden_set_path, 'w', encoding='utf-8') as f:
            json.dump(golden_set, f, indent=2, ensure_ascii=False)

    def _create_backup(self, golden_set: Dict[str, Any]):
        """Create backup of current golden set"""
        version = golden_set.get('version', 'unknown')
        backup_filename = f'golden_set_v{version}.json'
        backup_path = os.path.join(self.backup_dir, backup_filename)

        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(golden_set, f, indent=2, ensure_ascii=False)

    def get_current_version(self) -> str:
        """
        Get current golden set version

        Returns:
            Current version string
        """
        if not self.current_version:
            golden_set = self.load_golden_set()
            self.current_version = golden_set.get('version', '1.0.0')

        return self.current_version

    def create_version(self, new_version: str, description: str = "") -> str:
        """
        Create new version of golden set

        Args:
            new_version: New version number
            description: Version description

        Returns:
            New version string
        """
        golden_set = self.load_golden_set()

        # Update version and metadata
        golden_set['version'] = new_version
        golden_set['metadata']['last_updated'] = datetime.now(timezone.utc).isoformat()
        golden_set['metadata']['version_description'] = description

        # Save and update current version
        self._save_golden_set(golden_set)
        self.current_version = new_version

        # Update version history
        self.version_history.append({
            'version': new_version,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'description': description
        })

        self.logger.info(f"Created new version: {new_version}")
        return new_version

    def get_version_history(self) -> List[Dict[str, Any]]:
        """
        Get version history

        Returns:
            List of version information dictionaries
        """
        return self.version_history

    def get_all_test_cases(self) -> List[Dict[str, Any]]:
        """
        Get all test cases from golden set

        Returns:
            List of all test cases
        """
        golden_set = self.load_golden_set()
        return golden_set.get('test_cases', [])

    def get_test_cases_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Get test cases filtered by category

        Args:
            category: Category to filter by

        Returns:
            List of test cases in specified category
        """
        test_cases = self.get_all_test_cases()
        return [tc for tc in test_cases if tc.get('category') == category]

    def get_test_cases_by_priority(self, priority: str) -> List[Dict[str, Any]]:
        """
        Get test cases filtered by priority

        Args:
            priority: Priority to filter by

        Returns:
            List of test cases with specified priority
        """
        test_cases = self.get_all_test_cases()
        return [tc for tc in test_cases if tc.get('priority') == priority]

    def add_test_case(self, test_case: Dict[str, Any]) -> bool:
        """
        Add new test case to golden set

        Args:
            test_case: Test case dictionary

        Returns:
            True if successful, False otherwise
        """
        # Validate test case structure
        if not self._validate_test_case(test_case):
            return False

        golden_set = self.load_golden_set()

        # Check for duplicate ID
        existing_ids = [tc['id'] for tc in golden_set['test_cases']]
        if test_case['id'] in existing_ids:
            self.logger.warning(f"Test case ID {test_case['id']} already exists")
            return False

        # Add test case
        golden_set['test_cases'].append(test_case)
        golden_set['metadata']['total_cases'] = len(golden_set['test_cases'])

        # Update category and priority counts
        category = test_case.get('category', 'unknown')
        priority = test_case.get('priority', 'medium')

        # Ensure categories and priorities dictionaries exist
        if 'categories' not in golden_set['metadata']:
            golden_set['metadata']['categories'] = {}
        if 'priorities' not in golden_set['metadata']:
            golden_set['metadata']['priorities'] = {}

        if category not in golden_set['metadata']['categories']:
            golden_set['metadata']['categories'][category] = 0
        golden_set['metadata']['categories'][category] += 1

        if priority not in golden_set['metadata']['priorities']:
            golden_set['metadata']['priorities'][priority] = 0
        golden_set['metadata']['priorities'][priority] += 1

        # Update timestamp
        golden_set['metadata']['last_updated'] = datetime.now(timezone.utc).isoformat()

        # Save golden set
        self._save_golden_set(golden_set)

        self.logger.info(f"Added test case: {test_case['id']}")
        return True

    def _validate_test_case(self, test_case: Dict[str, Any]) -> bool:
        """
        Validate test case structure

        Args:
            test_case: Test case to validate

        Returns:
            True if valid, False otherwise
        """
        required_fields = ['id', 'description', 'input', 'expected_output']

        for field in required_fields:
            if field not in test_case:
                self.logger.error(f"Missing required field: {field}")
                return False

        # Validate ID format
        if not isinstance(test_case['id'], str) or not test_case['id'].strip():
            self.logger.error("Test case ID must be a non-empty string")
            return False

        return True

    def remove_test_case(self, test_case_id: str) -> bool:
        """
        Remove test case from golden set

        Args:
            test_case_id: ID of test case to remove

        Returns:
            True if successful, False otherwise
        """
        golden_set = self.load_golden_set()

        # Find and remove test case
        original_count = len(golden_set['test_cases'])
        golden_set['test_cases'] = [
            tc for tc in golden_set['test_cases']
            if tc['id'] != test_case_id
        ]

        if len(golden_set['test_cases']) == original_count:
            self.logger.warning(f"Test case {test_case_id} not found")
            return False

        # Update metadata
        golden_set['metadata']['total_cases'] = len(golden_set['test_cases'])
        golden_set['metadata']['last_updated'] = datetime.now(timezone.utc).isoformat()

        # Save golden set
        self._save_golden_set(golden_set)

        self.logger.info(f"Removed test case: {test_case_id}")
        return True

    def calculate_coverage(self) -> float:
        """
        Calculate test coverage (placeholder for integration with CoverageAnalyzer)

        Returns:
            Coverage percentage
        """
        # This would integrate with CoverageAnalyzer
        # For now, return a placeholder value
        return 0.95

    def validate_test_result(self, test_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate test result against expected output

        Args:
            test_result: Test result dictionary

        Returns:
            Validation result dictionary
        """
        test_case_id = test_result.get('test_case_id')
        actual_output = test_result.get('actual_output')

        # Find the expected output
        expected_test_case = None
        for tc in self.get_all_test_cases():
            if tc['id'] == test_case_id:
                expected_test_case = tc
                break

        if not expected_test_case:
            return {
                'passed': False,
                'confidence': 0.0,
                'error': f'Test case {test_case_id} not found'
            }

        expected_output = expected_test_case['expected_output']

        # Simple comparison (can be enhanced with semantic similarity)
        if actual_output == expected_output:
            return {
                'passed': True,
                'confidence': 1.0,
                'similarity_score': 1.0
            }
        else:
            # Calculate similarity score (placeholder)
            similarity_score = self._calculate_similarity(actual_output, expected_output)

            return {
                'passed': False,
                'confidence': similarity_score,
                'similarity_score': similarity_score,
                'expected': expected_output,
                'actual': actual_output
            }

    def _calculate_similarity(self, output1: Any, output2: Any) -> float:
        """
        Calculate similarity between two outputs (placeholder)

        Args:
            output1: First output
            output2: Second output

        Returns:
            Similarity score between 0 and 1
        """
        # Simple string similarity for now
        if isinstance(output1, dict) and isinstance(output2, dict):
            # Convert to JSON string for comparison
            str1 = json.dumps(output1, sort_keys=True)
            str2 = json.dumps(output2, sort_keys=True)
        else:
            str1 = str(output1)
            str2 = str(output2)

        # Simple edit distance calculation
        distance = self._levenshtein_distance(str1, str2)
        max_length = max(len(str1), len(str2))

        if max_length == 0:
            return 1.0

        return 1.0 - (distance / max_length)

    def _levenshtein_distance(self, s1: str, s2: str) -> int:
        """
        Calculate Levenshtein distance between two strings

        Args:
            s1: First string
            s2: Second string

        Returns:
            Edit distance
        """
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get golden set statistics

        Returns:
            Statistics dictionary
        """
        golden_set = self.load_golden_set()
        test_cases = golden_set['test_cases']

        stats = {
            'total_test_cases': len(test_cases),
            'version': golden_set['version'],
            'last_updated': golden_set['metadata']['last_updated'],
            'coverage_target': golden_set['metadata']['coverage_target'],
            'categories': golden_set['metadata']['categories'],
            'priorities': golden_set['metadata']['priorities']
        }

        return stats