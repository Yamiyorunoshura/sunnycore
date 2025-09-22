import json
import os
import subprocess
import tempfile
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timezone
import logging
import yaml


class PromptfooIntegration:
    """
    Promptfoo Integration - Adapter Pattern Implementation

    Integrates Promptfoo A/B testing framework with the behavior testing layer,
    providing automated LLM evaluation and comparison capabilities.
    """

    def __init__(self, config_path: Optional[str] = None, workspace_dir: Optional[str] = None):
        """
        Initialize Promptfoo Integration

        Args:
            config_path: Path to promptfoo configuration file
            workspace_dir: Directory for promptfoo workspace
        """
        self.config_path = config_path or "promptfooconfig.yaml"
        self.workspace_dir = workspace_dir or tempfile.mkdtemp(prefix="promptfoo_")
        self.logger = logging.getLogger(__name__)

        # Ensure workspace directory exists
        os.makedirs(self.workspace_dir, exist_ok=True)

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
                with open(self.config_path, 'r') as f:
                    return yaml.safe_load(f)
            except Exception as e:
                self.logger.warning(f"Failed to load config: {e}")

        # Create default configuration
        return self._create_default_config()

    def _create_default_config(self) -> Dict[str, Any]:
        """
        Create default promptfoo configuration

        Returns:
            Default configuration dictionary
        """
        return {
            "description": "Behavior Test Layer A/B Testing",
            "providers": [
                {
                    "id": "openai:gpt-4",
                    "config": {
                        "apiKey": "${OPENAI_API_KEY}",
                        "model": "gpt-4"
                    }
                }
            ],
            "tests": [],
            "defaultTest": {
                "options": {
                    "provider": "openai:gpt-4",
                    "vars": {}
                }
            },
            "evaluateOptions": {
                "maxConcurrency": 5,
                "repeat": 1,
                "delay": 0
            },
            "sharing": {
                "appName": "behavior-test-layer",
                "author": "System Generated"
            }
        }

    def save_config(self):
        """Save current configuration to file"""
        try:
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
            self.logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            self.logger.error(f"Failed to save config: {e}")

    def add_test_case(self, test_case: Dict[str, Any]) -> bool:
        """
        Add a test case to the promptfoo configuration

        Args:
            test_case: Test case dictionary

        Returns:
            True if successful, False otherwise
        """
        try:
            # Convert test case to promptfoo format
            promptfoo_test = self._convert_to_promptfoo_format(test_case)

            # Add to configuration
            if 'tests' not in self.config:
                self.config['tests'] = []

            self.config['tests'].append(promptfoo_test)

            # Save configuration
            self.save_config()

            self.logger.info(f"Added test case: {test_case.get('id', 'unknown')}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to add test case: {e}")
            return False

    def _convert_to_promptfoo_format(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert internal test case format to promptfoo format

        Args:
            test_case: Internal test case format

        Returns:
            Promptfoo-compatible test case
        """
        promptfoo_test = {
            "description": test_case.get('description', 'Test case'),
            "vars": {},
            "assert": []
        }

        # Add input variables
        input_data = test_case.get('input', {})
        for key, value in input_data.items():
            promptfoo_test['vars'][key] = value

        # Add assertions for expected output
        expected_output = test_case.get('expected_output', {})
        if isinstance(expected_output, dict):
            for key, value in expected_output.items():
                promptfoo_test['assert'].append({
                    "type": "contains",
                    "value": str(value)
                })

        # Add metadata
        if 'id' in test_case:
            promptfoo_test['metadata'] = {
                "id": test_case['id'],
                "category": test_case.get('category', 'general'),
                "priority": test_case.get('priority', 'medium')
            }

        return promptfoo_test

    def add_multiple_test_cases(self, test_cases: List[Dict[str, Any]]) -> int:
        """
        Add multiple test cases to the configuration

        Args:
            test_cases: List of test case dictionaries

        Returns:
            Number of successfully added test cases
        """
        success_count = 0

        for test_case in test_cases:
            if self.add_test_case(test_case):
                success_count += 1

        self.logger.info(f"Added {success_count}/{len(test_cases)} test cases")
        return success_count

    def run_ab_test(self, test_ids: Optional[List[str]] = None,
                   providers: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Run A/B test with specified test cases and providers

        Args:
            test_ids: List of test case IDs to run (empty for all)
            providers: List of provider IDs to use (empty for default)

        Returns:
            Test results dictionary
        """
        try:
            # Prepare test configuration
            test_config = self._prepare_test_config(test_ids, providers)

            # Write temporary configuration
            temp_config_path = os.path.join(self.workspace_dir, 'temp_config.yaml')
            with open(temp_config_path, 'w') as f:
                yaml.dump(test_config, f, default_flow_style=False)

            # Run promptfoo evaluation
            result = self._run_promptfoo_eval(temp_config_path)

            # Clean up temporary file
            if os.path.exists(temp_config_path):
                os.remove(temp_config_path)

            return result

        except Exception as e:
            self.logger.error(f"Failed to run A/B test: {e}")
            return {
                'success': False,
                'error': str(e)
            }

    def _prepare_test_config(self, test_ids: Optional[List[str]] = None,
                           providers: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Prepare test configuration for A/B testing

        Args:
            test_ids: List of test case IDs to include
            providers: List of provider IDs to use

        Returns:
            Test configuration dictionary
        """
        test_config = {
            "description": "A/B Test Configuration",
            "providers": providers or self.config.get('providers', []),
            "tests": [],
            "evaluateOptions": self.config.get('evaluateOptions', {})
        }

        # Filter tests if test_ids specified
        if test_ids:
            for test in self.config.get('tests', []):
                test_metadata = test.get('metadata', {})
                if test_metadata.get('id') in test_ids:
                    test_config['tests'].append(test)
        else:
            test_config['tests'] = self.config.get('tests', [])

        return test_config

    def _run_promptfoo_eval(self, config_path: str) -> Dict[str, Any]:
        """
        Run promptfoo evaluation with specified configuration

        Args:
            config_path: Path to configuration file

        Returns:
            Evaluation results
        """
        try:
            # Build command
            cmd = [
                'promptfoo', 'eval',
                '--config', config_path,
                '--output', os.path.join(self.workspace_dir, 'results.json'),
                '--share'
            ]

            # Run command
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            if result.returncode == 0:
                # Load results
                results_path = os.path.join(self.workspace_dir, 'results.json')
                if os.path.exists(results_path):
                    with open(results_path, 'r') as f:
                        results_data = json.load(f)

                    return {
                        'success': True,
                        'results': results_data,
                        'stdout': result.stdout,
                        'stderr': result.stderr
                    }
                else:
                    return {
                        'success': False,
                        'error': 'Results file not found'
                    }
            else:
                return {
                    'success': False,
                    'error': result.stderr,
                    'returncode': result.returncode
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

    def compare_results(self, results1: Dict[str, Any], results2: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compare two test result sets

        Args:
            results1: First result set
            results2: Second result set

        Returns:
            Comparison results
        """
        comparison = {
            'summary': {},
            'test_comparisons': [],
            'provider_comparisons': []
        }

        try:
            # Extract test results
            tests1 = self._extract_test_results(results1)
            tests2 = self._extract_test_results(results2)

            # Compare individual tests
            for test_id in set(tests1.keys()).union(set(tests2.keys())):
                test1_result = tests1.get(test_id, {})
                test2_result = tests2.get(test_id, {})

                comparison['test_comparisons'].append({
                    'test_id': test_id,
                    'result1': test1_result,
                    'result2': test2_result,
                    'improved': self._is_improvement(test1_result, test2_result)
                })

            # Calculate summary statistics
            comparison['summary'] = self._calculate_comparison_summary(
                comparison['test_comparisons']
            )

        except Exception as e:
            self.logger.error(f"Failed to compare results: {e}")
            comparison['error'] = str(e)

        return comparison

    def _extract_test_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract test results from promptfoo output

        Args:
            results: Promptfoo results dictionary

        Returns:
            Dictionary of test results by test ID
        """
        test_results = {}

        try:
            if 'results' in results:
                results_data = results['results']
                if 'table' in results_data:
                    for row in results_data['table']:
                        test_id = row.get('test_id', 'unknown')
                        test_results[test_id] = {
                            'success': row.get('success', False),
                            'score': row.get('score', 0.0),
                            'latency': row.get('latency', 0),
                            'provider': row.get('provider', 'unknown')
                        }

        except Exception as e:
            self.logger.error(f"Failed to extract test results: {e}")

        return test_results

    def _is_improvement(self, result1: Dict[str, Any], result2: Dict[str, Any]) -> bool:
        """
        Determine if result2 is an improvement over result1

        Args:
            result1: First result
            result2: Second result

        Returns:
            True if result2 is better
        """
        # Simple improvement logic: higher score and lower latency
        score1 = result1.get('score', 0.0)
        score2 = result2.get('score', 0.0)
        latency1 = result1.get('latency', float('inf'))
        latency2 = result2.get('latency', float('inf'))

        return (score2 > score1) or (score2 == score1 and latency2 < latency1)

    def _calculate_comparison_summary(self, comparisons: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate summary statistics for comparison

        Args:
            comparisons: List of test comparisons

        Returns:
            Summary statistics
        """
        total_tests = len(comparisons)
        improvements = sum(1 for comp in comparisons if comp.get('improved', False))
        regressions = sum(1 for comp in comparisons if not comp.get('improved', False))

        return {
            'total_tests': total_tests,
            'improvements': improvements,
            'regressions': regressions,
            'improvement_rate': improvements / total_tests if total_tests > 0 else 0.0
        }

    def generate_report(self, results: Dict[str, Any]) -> str:
        """
        Generate human-readable test report

        Args:
            results: Test results dictionary

        Returns:
            Formatted report string
        """
        report = []
        report.append("=== Promptfoo A/B Test Report ===")
        report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")

        if 'results' in results:
            results_data = results['results']

            # Summary statistics
            if 'stats' in results_data:
                stats = results_data['stats']
                report.append(f"\nTotal Tests: {stats.get('total', 0)}")
                report.append(f"Passed: {stats.get('success', 0)}")
                report.append(f"Failed: {stats.get('failure', 0)}")
                report.append(f"Success Rate: {stats.get('success_rate', 0):.2%}")

            # Test details
            if 'table' in results_data:
                report.append("\n=== Test Details ===")
                for row in results_data['table']:
                    test_id = row.get('test_id', 'unknown')
                    success = row.get('success', False)
                    score = row.get('score', 0.0)
                    latency = row.get('latency', 0)

                    status = "PASS" if success else "FAIL"
                    report.append(f"  {test_id}: {status} (Score: {score:.2f}, Latency: {latency}ms)")

        else:
            report.append("No results available")

        return "\n".join(report)

    def get_test_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about configured tests

        Returns:
            Test statistics dictionary
        """
        stats = {
            'total_tests': len(self.config.get('tests', [])),
            'categories': {},
            'priorities': {},
            'providers': len(self.config.get('providers', []))
        }

        # Analyze test categories and priorities
        for test in self.config.get('tests', []):
            metadata = test.get('metadata', {})

            # Categories
            category = metadata.get('category', 'unknown')
            if category not in stats['categories']:
                stats['categories'][category] = 0
            stats['categories'][category] += 1

            # Priorities
            priority = metadata.get('priority', 'medium')
            if priority not in stats['priorities']:
                stats['priorities'][priority] = 0
            stats['priorities'][priority] += 1

        return stats

    def cleanup(self):
        """Clean up temporary files and directories"""
        try:
            if os.path.exists(self.workspace_dir):
                import shutil
                shutil.rmtree(self.workspace_dir)
            self.logger.info("Cleaned up temporary files")
        except Exception as e:
            self.logger.error(f"Failed to cleanup: {e}")