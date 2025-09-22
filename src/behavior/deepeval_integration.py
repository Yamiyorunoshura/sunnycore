import json
import os
import tempfile
import ast
from typing import Dict, List, Any, Optional, Union, Tuple, Callable
from datetime import datetime, timezone
import logging
import subprocess


class DeepEvalIntegration:
    """
    DeepEval Integration - Template Method Pattern Implementation

    Integrates DeepEval pytest-style assertion framework for architecture
    alignment validation and requirement mapping verification.
    """

    def __init__(self, config_path: Optional[str] = None, test_dir: Optional[str] = None):
        """
        Initialize DeepEval Integration

        Args:
            config_path: Path to DeepEval configuration file
            test_dir: Directory for DeepEval test files
        """
        self.config_path = config_path or "deepeval_config.yaml"
        self.test_dir = test_dir or "tests/deepeval"
        self.logger = logging.getLogger(__name__)

        # Ensure test directory exists
        os.makedirs(self.test_dir, exist_ok=True)

        # Initialize configuration
        self.config = self._load_or_create_config()

    def _load_or_create_config(self) -> Dict[str, Any]:
        """
        Load existing configuration or create default

        Returns:
            Configuration dictionary
        """
        if os.path.exists(self.config_path):
            try:
                import yaml
                with open(self.config_path, 'r') as f:
                    return yaml.safe_load(f)
            except Exception as e:
                self.logger.warning(f"Failed to load config: {e}")

        # Create default configuration
        return self._create_default_config()

    def _create_default_config(self) -> Dict[str, Any]:
        """
        Create default DeepEval configuration

        Returns:
            Default configuration dictionary
        """
        return {
            "default_model": "gpt-4",
            "evaluation_params": {
                "max_concurrent": 5,
                "timeout": 30,
                "temperature": 0.1
            },
            "metrics": [
                "answer_relevancy",
                "faithfulness",
                "contextual_recall",
                "contextual_precision",
                "harmfulness"
            ],
            "custom_metrics": {
                "architecture_alignment": {
                    "type": "custom",
                    "description": "Evaluates alignment with system architecture"
                },
                "requirement_coverage": {
                    "type": "custom",
                    "description": "Evaluates coverage of specified requirements"
                }
            }
        }

    def save_config(self):
        """Save current configuration to file"""
        try:
            import yaml
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
            self.logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            self.logger.error(f"Failed to save config: {e}")

    def create_pytest_test(self, test_case: Dict[str, Any]) -> str:
        """
        Create pytest-style test case using DeepEval assertions

        Args:
            test_case: Test case dictionary

        Returns:
            Generated test file content
        """
        test_template = f'''import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from src.behavior.deepeval_integration import DeepEvalIntegration

class TestArchitectureAlignment:
    """Architecture alignment test cases"""

    def test_{test_case['id'].replace('-', '_')}(self):
        """Test: {test_case.get('description', 'Architecture alignment test')}"""
        # Test input
        input_data = {test_case.get('input', {})}

        # Expected output
        expected_output = {test_case.get('expected_output', {})}

        # Test the architecture component
        actual_output = self._test_architecture_component(input_data)

        # DeepEval assertions
        metrics = [
            AnswerRelevancyMetric(
                threshold=0.8,
                model="gpt-4",
                include_reason=True
            ),
            FaithfulnessMetric(
                threshold=0.8,
                model="gpt-4",
                include_reason=True
            )
        ]

        # Run assertions
        assert_test(
            input_data,
            actual_output,
            expected_output,
            metrics=metrics
        )

        # Additional architecture-specific assertions
        self._assert_architecture_alignment(actual_output, expected_output)

    def _test_architecture_component(self, input_data):
        """Test the architecture component with given input"""
        # This would be replaced with actual component testing
        return {{"response": "Test response", "components": ["component1", "component2"]}}

    def _assert_architecture_alignment(self, actual_output, expected_output):
        """Assert architecture alignment requirements"""
        # Check for required components
        actual_components = set(actual_output.get('components', []))
        expected_components = set(expected_output.get('components', []))

        assert actual_components.issuperset(expected_components), \\
            f"Missing components: {{expected_components - actual_components}}"

        # Check component dependencies
        self._validate_component_dependencies(actual_output)

    def _validate_component_dependencies(self, output):
        """Validate component dependencies"""
        # Implementation would check for proper component dependencies
        pass
'''

        return test_template

    def generate_architecture_tests(self, architecture_spec: Dict[str, Any]) -> str:
        """
        Generate comprehensive architecture validation tests

        Args:
            architecture_spec: Architecture specification dictionary

        Returns:
            Path to generated test file
        """
        test_cases = self._generate_architecture_test_cases(architecture_spec)

        test_content = f'''import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from src.behavior.deepeval_integration import DeepEvalIntegration

class TestArchitectureValidation:
    """Comprehensive architecture validation tests"""

    def setup_method(self):
        """Setup test fixtures"""
        self.de = DeepEvalIntegration()
        self.architecture_spec = {architecture_spec}

    def test_component_integrity(self):
        """Test architecture component integrity"""
        components = self.architecture_spec.get('components', [])

        for component in components:
            self._test_single_component_integrity(component)

    def test_data_flow_validation(self):
        """Test data flow between components"""
        data_flows = self.architecture_spec.get('data_flows', [])

        for flow in data_flows:
            self._test_data_flow(flow)

    def test_interface_compliance(self):
        """Test interface compliance"""
        interfaces = self.architecture_spec.get('interfaces', [])

        for interface in interfaces:
            self._test_interface_compliance(interface)

    def test_performance_requirements(self):
        """Test performance requirements"""
        performance_reqs = self.architecture_spec.get('performance', {})

        for req_name, req_value in performance_reqs.items():
            self._test_performance_requirement(req_name, req_value)

    def _test_single_component_integrity(self, component):
        """Test individual component integrity"""
        component_id = component.get('id')
        component_type = component.get('type')

        # Test component exists and is properly structured
        assert component_id is not None, f"Component missing ID"
        assert component_type is not None, f"Component missing type"

    def _test_data_flow(self, flow):
        """Test individual data flow"""
        source = flow.get('source')
        target = flow.get('target')
        data_type = flow.get('data_type')

        assert source is not None, "Data flow missing source"
        assert target is not None, "Data flow missing target"
        assert data_type is not None, "Data flow missing data type"

    def _test_interface_compliance(self, interface):
        """Test interface compliance"""
        interface_id = interface.get('id')
        methods = interface.get('methods', [])

        assert interface_id is not None, "Interface missing ID"
        assert len(methods) > 0, f"Interface {{interface_id}} has no methods"

    def _test_performance_requirement(self, req_name, req_value):
        """Test individual performance requirement"""
        # This would involve actual performance testing
        assert req_value is not None, f"Performance requirement {{req_name}} has no value"
'''

        # Save test file
        test_filename = f"test_architecture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        test_path = os.path.join(self.test_dir, test_filename)

        with open(test_path, 'w') as f:
            f.write(test_content)

        self.logger.info(f"Generated architecture test file: {test_path}")
        return test_path

    def _generate_architecture_test_cases(self, architecture_spec: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate test cases from architecture specification

        Args:
            architecture_spec: Architecture specification

        Returns:
            List of test case dictionaries
        """
        test_cases = []

        # Component integrity tests
        components = architecture_spec.get('components', [])
        for component in components:
            test_cases.append({
                'id': f"component_integrity_{component.get('id', 'unknown')}",
                'description': f"Test integrity of component {component.get('id')}",
                'type': 'component_integrity',
                'input': {'component_id': component.get('id')},
                'expected_output': {'status': 'valid', 'integrity': 'intact'}
            })

        # Data flow tests
        data_flows = architecture_spec.get('data_flows', [])
        for flow in data_flows:
            test_cases.append({
                'id': f"data_flow_{flow.get('source', 'unknown')}_{flow.get('target', 'unknown')}",
                'description': f"Test data flow from {flow.get('source')} to {flow.get('target')}",
                'type': 'data_flow',
                'input': {'flow': flow},
                'expected_output': {'status': 'valid', 'flow_established': True}
            })

        return test_cases

    def run_deepeval_tests(self, test_file_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Run DeepEval tests using pytest

        Args:
            test_file_path: Specific test file to run (optional)

        Returns:
            Test execution results
        """
        try:
            # Build pytest command
            cmd = ['python', '-m', 'pytest']

            if test_file_path:
                cmd.append(test_file_path)
            else:
                cmd.append(self.test_dir)

            cmd.extend([
                '--tb=short',
                '--verbose',
                '--deepeval',
                '--json-report',
                '--json-report-file=deepeval_results.json'
            ])

            # Run tests
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            # Parse results
            test_results = self._parse_test_results(result)

            return {
                'success': result.returncode == 0,
                'returncode': result.returncode,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'results': test_results
            }

        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Test execution timed out'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _parse_test_results(self, subprocess_result) -> Dict[str, Any]:
        """
        Parse pytest results

        Args:
            subprocess_result: Subprocess result object

        Returns:
            Parsed test results
        """
        results = {
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'error_tests': 0,
            'skipped_tests': 0,
            'test_details': []
        }

        try:
            # Parse stdout for test results
            stdout = subprocess_result.stdout
            lines = stdout.split('\n')

            for line in lines:
                if 'passed' in line and 's' in line:
                    # Parse test result line
                    parts = line.split()
                    if len(parts) >= 3:
                        results['passed_tests'] += 1
                        results['total_tests'] += 1
                elif 'failed' in line:
                    results['failed_tests'] += 1
                    results['total_tests'] += 1
                elif 'error' in line:
                    results['error_tests'] += 1
                    results['total_tests'] += 1
                elif 'skipped' in line:
                    results['skipped_tests'] += 1
                    results['total_tests'] += 1

        except Exception as e:
            self.logger.error(f"Failed to parse test results: {e}")

        return results

    def calculate_f1_score(self, test_results: Dict[str, Any],
                          architecture_mapping: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate F1 score for architecture alignment

        Args:
            test_results: Test execution results
            architecture_mapping: Architecture component mapping

        Returns:
            F1 score calculation results
        """
        try:
            # Extract true positives, false positives, false negatives
            tp = test_results.get('passed_tests', 0)
            fp = test_results.get('failed_tests', 0)
            fn = len(architecture_mapping.get('components', [])) - tp

            # Calculate precision, recall, F1
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

            return {
                'precision': round(precision, 3),
                'recall': round(recall, 3),
                'f1_score': round(f1_score, 3),
                'true_positives': tp,
                'false_positives': fp,
                'false_negatives': fn,
                'meets_target': f1_score >= 0.9  # Target F1 score ≥ 0.9
            }

        except Exception as e:
            self.logger.error(f"Failed to calculate F1 score: {e}")
            return {
                'precision': 0.0,
                'recall': 0.0,
                'f1_score': 0.0,
                'error': str(e)
            }

    def validate_requirement_mapping(self, test_results: Dict[str, Any],
                                   requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate requirement mapping coverage

        Args:
            test_results: Test execution results
            requirements: Requirements specification

        Returns:
            Requirement validation results
        """
        validation_results = {
            'total_requirements': 0,
            'covered_requirements': 0,
            'uncovered_requirements': 0,
            'coverage_percentage': 0.0,
            'requirement_details': []
        }

        try:
            functional_reqs = requirements.get('functional', {})
            non_functional_reqs = requirements.get('non_functional', {})

            all_requirements = {**functional_reqs, **non_functional_reqs}
            validation_results['total_requirements'] = len(all_requirements)

            # Check coverage for each requirement
            for req_id, req_details in all_requirements.items():
                is_covered = self._check_requirement_coverage(req_id, test_results)

                validation_results['requirement_details'].append({
                    'requirement_id': req_id,
                    'covered': is_covered,
                    'details': req_details
                })

                if is_covered:
                    validation_results['covered_requirements'] += 1
                else:
                    validation_results['uncovered_requirements'] += 1

            # Calculate coverage percentage
            if validation_results['total_requirements'] > 0:
                validation_results['coverage_percentage'] = (
                    validation_results['covered_requirements'] / validation_results['total_requirements']
                ) * 100

        except Exception as e:
            self.logger.error(f"Failed to validate requirement mapping: {e}")
            validation_results['error'] = str(e)

        return validation_results

    def _check_requirement_coverage(self, requirement_id: str, test_results: Dict[str, Any]) -> bool:
        """
        Check if a specific requirement is covered by tests

        Args:
            requirement_id: Requirement identifier
            test_results: Test execution results

        Returns:
            True if requirement is covered
        """
        # This is a simplified implementation
        # In practice, this would involve more sophisticated mapping
        test_details = test_results.get('test_details', [])

        for test in test_details:
            test_name = test.get('name', '').lower()
            if requirement_id.lower() in test_name:
                return True

        return False

    def generate_validation_report(self, f1_results: Dict[str, Any],
                                 requirement_results: Dict[str, Any]) -> str:
        """
        Generate comprehensive validation report

        Args:
            f1_results: F1 score calculation results
            requirement_results: Requirement validation results

        Returns:
            Formatted report string
        """
        report = []
        report.append("=== DeepEval Architecture Validation Report ===")
        report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
        report.append("")

        # F1 Score Results
        report.append("## F1 Score Analysis")
        f1_score = f1_results.get('f1_score', 0.0)
        precision = f1_results.get('precision', 0.0)
        recall = f1_results.get('recall', 0.0)
        meets_target = f1_results.get('meets_target', False)

        report.append(f"F1 Score: {f1_score:.3f}")
        report.append(f"Precision: {precision:.3f}")
        report.append(f"Recall: {recall:.3f}")
        report.append(f"Target (≥0.9): {'✓' if meets_target else '✗'}")
        report.append("")

        # Requirement Coverage
        report.append("## Requirement Coverage")
        coverage_pct = requirement_results.get('coverage_percentage', 0.0)
        covered = requirement_results.get('covered_requirements', 0)
        total = requirement_results.get('total_requirements', 0)

        report.append(f"Coverage: {coverage_pct:.1f}% ({covered}/{total} requirements)")
        report.append("")

        # Detailed Requirements
        report.append("### Requirement Details")
        for req_detail in requirement_results.get('requirement_details', []):
            req_id = req_detail['requirement_id']
            covered = req_detail['covered']
            status = "✓" if covered else "✗"
            report.append(f"- {req_id}: {status}")

        # Recommendations
        report.append("")
        report.append("## Recommendations")
        if not meets_target:
            report.append("- F1 score below target. Consider improving test coverage.")
        if coverage_pct < 90:
            report.append("- Requirement coverage below 90%. Add more test cases.")
        if meets_target and coverage_pct >= 90:
            report.append("- Architecture validation meets targets. Maintain current standards.")

        return "\n".join(report)

    def cleanup(self):
        """Clean up temporary files and directories"""
        try:
            # Clean up old test files (keep last 10)
            if os.path.exists(self.test_dir):
                test_files = [f for f in os.listdir(self.test_dir) if f.startswith('test_architecture_')]
                test_files.sort()

                # Remove old files
                for old_file in test_files[:-10]:
                    old_path = os.path.join(self.test_dir, old_file)
                    os.remove(old_path)

            self.logger.info("Cleaned up temporary files")
        except Exception as e:
            self.logger.error(f"Failed to cleanup: {e}")