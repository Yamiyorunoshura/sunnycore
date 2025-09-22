import json
import re
from typing import Dict, List, Any, Optional, Union, Tuple, Set
from datetime import datetime, timezone
import logging
from dataclasses import dataclass


@dataclass
class RequirementMapping:
    """Mapping between requirements and implementation"""
    requirement_id: str
    requirement_type: str
    implementation_locations: List[str]
    coverage_percentage: float
    test_coverage: List[str]
    validation_status: str


class RequirementMapper:
    """
    Requirement Mapping Validation System

    Maps and validates requirements against implementation,
    providing comprehensive coverage analysis and validation.
    """

    def __init__(self, requirements_path: Optional[str] = None):
        """
        Initialize Requirement Mapper

        Args:
            requirements_path: Path to requirements specification file
        """
        self.requirements_path = requirements_path
        self.logger = logging.getLogger(__name__)

        # Requirement mappings
        self.requirement_mappings = {}
        self.test_mappings = {}

        # Load requirements if path provided
        if requirements_path:
            self.load_requirements(requirements_path)

    def load_requirements(self, requirements_path: str) -> Dict[str, Any]:
        """
        Load requirements from file

        Args:
            requirements_path: Path to requirements file

        Returns:
            Requirements dictionary
        """
        try:
            with open(requirements_path, 'r') as f:
                if requirements_path.endswith('.json'):
                    requirements = json.load(f)
                else:
                    # Assume YAML format
                    import yaml
                    requirements = yaml.safe_load(f)

            self._process_requirements(requirements)
            return requirements

        except Exception as e:
            self.logger.error(f"Failed to load requirements: {e}")
            raise

    def _process_requirements(self, requirements: Dict[str, Any]):
        """
        Process requirements and initialize mappings

        Args:
            requirements: Requirements dictionary
        """
        # Process functional requirements
        functional_reqs = requirements.get('functional', {})
        for req_id, req_details in functional_reqs.items():
            self.requirement_mappings[req_id] = RequirementMapping(
                requirement_id=req_id,
                requirement_type='functional',
                implementation_locations=[],
                coverage_percentage=0.0,
                test_coverage=[],
                validation_status='pending'
            )

        # Process non-functional requirements
        non_functional_reqs = requirements.get('non_functional', {})
        for req_id, req_details in non_functional_reqs.items():
            self.requirement_mappings[req_id] = RequirementMapping(
                requirement_id=req_id,
                requirement_type='non_functional',
                implementation_locations=[],
                coverage_percentage=0.0,
                test_coverage=[],
                validation_status='pending'
            )

    def analyze_implementation_coverage(self, implementation_files: List[str]) -> Dict[str, Any]:
        """
        Analyze implementation files for requirement coverage

        Args:
            implementation_files: List of implementation file paths

        Returns:
            Coverage analysis results
        """
        try:
            # Read and analyze each implementation file
            for file_path in implementation_files:
                self._analyze_implementation_file(file_path)

            # Calculate coverage statistics
            coverage_stats = self._calculate_coverage_statistics()

            return {
                'total_requirements': len(self.requirement_mappings),
                'covered_requirements': sum(1 for mapping in self.requirement_mappings.values()
                                        if mapping.coverage_percentage > 0),
                'fully_covered_requirements': sum(1 for mapping in self.requirement_mappings.values()
                                            if mapping.coverage_percentage >= 0.9),
                'coverage_statistics': coverage_stats,
                'requirement_mappings': self._serialize_mappings()
            }

        except Exception as e:
            self.logger.error(f"Failed to analyze implementation coverage: {e}")
            return {
                'error': str(e),
                'total_requirements': 0,
                'covered_requirements': 0
            }

    def _analyze_implementation_file(self, file_path: str):
        """
        Analyze single implementation file for requirement coverage

        Args:
            file_path: Path to implementation file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract requirement references
            requirement_refs = self._extract_requirement_references(content)

            # Update mappings
            for req_id in requirement_refs:
                if req_id in self.requirement_mappings:
                    mapping = self.requirement_mappings[req_id]
                    if file_path not in mapping.implementation_locations:
                        mapping.implementation_locations.append(file_path)

        except Exception as e:
            self.logger.error(f"Failed to analyze file {file_path}: {e}")

    def _extract_requirement_references(self, content: str) -> Set[str]:
        """
        Extract requirement references from code content

        Args:
            content: File content

        Returns:
            Set of requirement IDs found
        """
        requirement_refs = set()

        # Common requirement reference patterns
        patterns = [
            r'F-\d+',      # Functional requirements
            r'N-\d+',      # Non-functional requirements
            r'REQ-\d+',    # Generic requirements
            r'#\s*[A-Za-z]-\d+',  # Commented requirements
            r'//\s*[A-Za-z]-\d+',  # C++ style comments
            r'/\*.*?[A-Za-z]-\d+.*?\*/',  # C style comments
            r'requirement.*?([A-Za-z]-\d+)',  # Requirement statements
            r'req.*?([A-Za-z]-\d+)',  # Short requirement references
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                # Extract the requirement ID
                req_id = match.group(1) if match.groups() else match.group(0)
                req_id = req_id.strip().upper()
                requirement_refs.add(req_id)

        return requirement_refs

    def _calculate_coverage_statistics(self) -> Dict[str, Any]:
        """
        Calculate coverage statistics for all requirements

        Returns:
            Coverage statistics dictionary
        """
        stats = {
            'functional_requirements': {'total': 0, 'covered': 0, 'fully_covered': 0},
            'non_functional_requirements': {'total': 0, 'covered': 0, 'fully_covered': 0},
            'coverage_distribution': {'0%': 0, '1-25%': 0, '26-50%': 0, '51-75%': 0, '76-99%': 0, '100%': 0}
        }

        for mapping in self.requirement_mappings.values():
            req_type = mapping.requirement_type
            coverage = mapping.coverage_percentage

            # Update type-specific statistics
            if req_type == 'functional':
                stats['functional_requirements']['total'] += 1
                if coverage > 0:
                    stats['functional_requirements']['covered'] += 1
                if coverage >= 0.9:
                    stats['functional_requirements']['fully_covered'] += 1
            elif req_type == 'non_functional':
                stats['non_functional_requirements']['total'] += 1
                if coverage > 0:
                    stats['non_functional_requirements']['covered'] += 1
                if coverage >= 0.9:
                    stats['non_functional_requirements']['fully_covered'] += 1

            # Update coverage distribution
            if coverage == 0:
                stats['coverage_distribution']['0%'] += 1
            elif coverage <= 0.25:
                stats['coverage_distribution']['1-25%'] += 1
            elif coverage <= 0.50:
                stats['coverage_distribution']['26-50%'] += 1
            elif coverage <= 0.75:
                stats['coverage_distribution']['51-75%'] += 1
            elif coverage < 1.0:
                stats['coverage_distribution']['76-99%'] += 1
            else:
                stats['coverage_distribution']['100%'] += 1

        return stats

    def map_tests_to_requirements(self, test_files: List[str]) -> Dict[str, Any]:
        """
        Map test files to requirements

        Args:
            test_files: List of test file paths

        Returns:
            Test mapping results
        """
        try:
            # Analyze each test file
            for test_file in test_files:
                self._analyze_test_file(test_file)

            # Calculate test coverage statistics
            test_stats = self._calculate_test_coverage_statistics()

            return {
                'total_test_files': len(test_files),
                'test_mappings': self.test_mappings,
                'test_coverage_statistics': test_stats
            }

        except Exception as e:
            self.logger.error(f"Failed to map tests to requirements: {e}")
            return {
                'error': str(e),
                'total_test_files': 0
            }

    def _analyze_test_file(self, test_file_path: str):
        """
        Analyze test file for requirement coverage

        Args:
            test_file_path: Path to test file
        """
        try:
            with open(test_file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract requirement references from test
            requirement_refs = self._extract_requirement_references(content)

            # Update test mappings
            for req_id in requirement_refs:
                if req_id not in self.test_mappings:
                    self.test_mappings[req_id] = []
                if test_file_path not in self.test_mappings[req_id]:
                    self.test_mappings[req_id].append(test_file_path)

                # Update requirement mapping
                if req_id in self.requirement_mappings:
                    mapping = self.requirement_mappings[req_id]
                    if test_file_path not in mapping.test_coverage:
                        mapping.test_coverage.append(test_file_path)

        except Exception as e:
            self.logger.error(f"Failed to analyze test file {test_file_path}: {e}")

    def _calculate_test_coverage_statistics(self) -> Dict[str, Any]:
        """
        Calculate test coverage statistics

        Returns:
            Test coverage statistics
        """
        stats = {
            'tested_requirements': 0,
            'untested_requirements': 0,
            'tests_per_requirement': {},
            'requirements_per_test': {}
        }

        for req_id, test_files in self.test_mappings.items():
            stats['tested_requirements'] += 1
            stats['tests_per_requirement'][req_id] = len(test_files)

        # Count requirements with no tests
        for req_id in self.requirement_mappings:
            if req_id not in self.test_mappings:
                stats['untested_requirements'] += 1

        return stats

    def validate_requirement_coverage(self, threshold: float = 0.8) -> Dict[str, Any]:
        """
        Validate requirement coverage against threshold

        Args:
            threshold: Coverage threshold (default: 0.8)

        Returns:
            Validation results
        """
        try:
            validation_results = {
                'threshold': threshold,
                'overall_validation': 'pass',
                'requirement_validations': {},
                'summary': {
                    'total_requirements': len(self.requirement_mappings),
                    'passing_requirements': 0,
                    'failing_requirements': 0,
                    'pass_rate': 0.0
                }
            }

            # Validate each requirement
            for req_id, mapping in self.requirement_mappings.items():
                is_valid = mapping.coverage_percentage >= threshold

                validation_results['requirement_validations'][req_id] = {
                    'coverage_percentage': mapping.coverage_percentage,
                    'threshold': threshold,
                    'valid': is_valid,
                    'implementation_locations': mapping.implementation_locations,
                    'test_coverage': mapping.test_coverage
                }

                if is_valid:
                    validation_results['summary']['passing_requirements'] += 1
                else:
                    validation_results['summary']['failing_requirements'] += 1

            # Calculate pass rate
            total_reqs = validation_results['summary']['total_requirements']
            if total_reqs > 0:
                pass_rate = validation_results['summary']['passing_requirements'] / total_reqs
                validation_results['summary']['pass_rate'] = pass_rate

                # Determine overall validation
                if pass_rate < threshold:
                    validation_results['overall_validation'] = 'fail'

            return validation_results

        except Exception as e:
            self.logger.error(f"Failed to validate requirement coverage: {e}")
            return {
                'error': str(e),
                'overall_validation': 'error'
            }

    def generate_coverage_report(self, validation_results: Dict[str, Any]) -> str:
        """
        Generate human-readable coverage report

        Args:
            validation_results: Validation results

        Returns:
            Formatted report string
        """
        report = []
        report.append("=== Requirement Coverage Report ===")
        report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
        report.append("")

        # Overall summary
        summary = validation_results.get('summary', {})
        total_reqs = summary.get('total_requirements', 0)
        passing_reqs = summary.get('passing_requirements', 0)
        failing_reqs = summary.get('failing_requirements', 0)
        pass_rate = summary.get('pass_rate', 0.0)
        threshold = validation_results.get('threshold', 0.8)

        report.append("## Summary")
        report.append(f"Total Requirements: {total_reqs}")
        report.append(f"Passing Requirements: {passing_reqs}")
        report.append(f"Failing Requirements: {failing_reqs}")
        report.append(f"Pass Rate: {pass_rate:.1%}")
        report.append(f"Threshold: {threshold:.1%}")
        report.append(f"Overall Status: {'✓ PASS' if pass_rate >= threshold else '✗ FAIL'}")
        report.append("")

        # Requirement details
        req_validations = validation_results.get('requirement_validations', {})
        if req_validations:
            report.append("## Requirement Details")
            for req_id, validation in req_validations.items():
                coverage = validation.get('coverage_percentage', 0.0)
                is_valid = validation.get('valid', False)
                status = "✓" if is_valid else "✗"

                report.append(f"{status} {req_id}: {coverage:.1%} coverage")

                # Show implementation locations
                impl_locations = validation.get('implementation_locations', [])
                if impl_locations:
                    report.append(f"   Implementation: {len(impl_locations)} files")

                # Show test coverage
                test_coverage = validation.get('test_coverage', [])
                if test_coverage:
                    report.append(f"   Tests: {len(test_coverage)} files")
                else:
                    report.append(f"   Tests: None")

            report.append("")

        # Recommendations
        report.append("## Recommendations")
        if pass_rate < threshold:
            report.append(f"- Overall coverage below threshold ({threshold:.1%}). Focus on failing requirements.")
        else:
            report.append("- Requirement coverage meets threshold. Maintain current standards.")

        # Specific recommendations for failing requirements
        failing_requirements = [req_id for req_id, validation in req_validations.items()
                             if not validation.get('valid', False)]
        if failing_requirements:
            report.append("- Prioritize implementation and testing for:")
            for req_id in failing_requirements[:5]:  # Show top 5
                report.append(f"  * {req_id}")
            if len(failing_requirements) > 5:
                report.append(f"  * ... and {len(failing_requirements) - 5} more")

        return "\n".join(report)

    def _serialize_mappings(self) -> Dict[str, Any]:
        """
        Serialize requirement mappings for output

        Returns:
            Serialized mappings dictionary
        """
        serialized = {}
        for req_id, mapping in self.requirement_mappings.items():
            serialized[req_id] = {
                'requirement_id': mapping.requirement_id,
                'requirement_type': mapping.requirement_type,
                'implementation_locations': mapping.implementation_locations,
                'coverage_percentage': mapping.coverage_percentage,
                'test_coverage': mapping.test_coverage,
                'validation_status': mapping.validation_status
            }

        return serialized