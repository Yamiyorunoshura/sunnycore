"""
Integration test suite for behavior testing layer
End-to-end testing scenarios for Golden Set, Promptfoo, and DeepEval collaboration
"""

import pytest
import json
import tempfile
import os
from unittest.mock import Mock, patch
from datetime import datetime, timezone

from src.behavior.golden_set_manager import GoldenSetManager
from src.behavior.promptfoo_integration import PromptfooIntegration
from src.behavior.deepeval_integration import DeepEvalIntegration
from src.behavior.architecture_validator import ArchitectureValidator
from src.behavior.requirement_mapper import RequirementMapper


class TestBehaviorTestingIntegration:
    """
    Integration tests for behavior testing layer components
    """

    def setup_method(self):
        """Setup test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.golden_set_manager = GoldenSetManager(
            storage_path=os.path.join(self.temp_dir, "golden_set.json")
        )
        self.promptfoo_integration = PromptfooIntegration(
            config_path=os.path.join(self.temp_dir, "promptfoo_config.yaml")
        )
        self.deepeval_integration = DeepEvalIntegration(
            config_path=os.path.join(self.temp_dir, "deepeval_config.yaml"),
            test_dir=os.path.join(self.temp_dir, "deepeval_tests")
        )
        self.architecture_validator = ArchitectureValidator()
        self.requirement_mapper = RequirementMapper()

    def test_golden_set_to_promptfoo_workflow(self):
        """
        Test complete workflow from Golden Set validation to Promptfoo evaluation
        """
        # Create test Golden Set
        test_cases = [
            {
                "id": "test_case_1",
                "description": "Basic functionality test",
                "input": {"prompt": "What is the capital of France?"},
                "expected_output": {"response": "Paris"},
                "metadata": {"category": "geography", "difficulty": "easy"}
            },
            {
                "id": "test_case_2",
                "description": "Complex reasoning test",
                "input": {"prompt": "Explain the process of photosynthesis"},
                "expected_output": {"response": "Detailed explanation of photosynthesis"},
                "metadata": {"category": "science", "difficulty": "medium"}
            }
        ]

        # Add test cases to Golden Set
        for test_case in test_cases:
            self.golden_set_manager.add_test_case(test_case)

        # Validate Golden Set
        validation_result = self.golden_set_manager.validate_golden_set()
        assert validation_result["valid"] is True
        assert validation_result["total_test_cases"] == 2

        # Generate Promptfoo configuration
        promptfoo_config = self.promptfoo_integration.generate_promptfoo_config(
            test_cases=test_cases
        )

        assert "prompts" in promptfoo_config
        assert "providers" in promptfoo_config
        assert "tests" in promptfoo_config
        assert len(promptfoo_config["tests"]) == 2

        # Execute Promptfoo evaluation
        evaluation_result = self.promptfoo_integration.run_evaluation(
            test_cases=test_cases
        )

        assert "success" in evaluation_result
        assert "results" in evaluation_result

    def test_deepeval_architecture_validation_workflow(self):
        """
        Test DeepEval architecture validation with requirement mapping
        """
        # Create test architecture specification
        architecture_spec = {
            "components": [
                {
                    "id": "golden_set_manager",
                    "type": "business",
                    "description": "Manages Golden Set test cases"
                },
                {
                    "id": "promptfoo_integration",
                    "type": "business",
                    "description": "Integrates Promptfoo for A/B testing"
                },
                {
                    "id": "deepeval_integration",
                    "type": "business",
                    "description": "Integrates DeepEval for architecture validation"
                }
            ],
            "data_flows": [
                {
                    "source": "golden_set_manager",
                    "target": "promptfoo_integration",
                    "data_type": "test_cases"
                },
                {
                    "source": "promptfoo_integration",
                    "target": "deepeval_integration",
                    "data_type": "evaluation_results"
                }
            ],
            "interfaces": [
                {
                    "id": "test_case_interface",
                    "methods": [
                        {"name": "add_test_case", "parameters": [{"name": "test_case"}]},
                        {"name": "validate_test_case", "parameters": [{"name": "test_case_id"}]}
                    ]
                }
            ]
        }

        # Create actual implementation representation
        actual_implementation = {
            "components": [
                {
                    "id": "golden_set_manager",
                    "type": "business",
                    "description": "Manages Golden Set test cases"
                },
                {
                    "id": "promptfoo_integration",
                    "type": "business",
                    "description": "Integrates Promptfoo for A/B testing"
                }
                # Note: deepeval_integration missing to test F1 score calculation
            ],
            "data_flows": [
                {
                    "source": "golden_set_manager",
                    "target": "promptfoo_integration",
                    "data_type": "test_cases"
                }
            ]
        }

        # Validate architecture alignment
        validation_results = self.architecture_validator.validate_architecture_alignment(
            actual_implementation=actual_implementation,
            expected_architecture=architecture_spec
        )

        assert "f1_score" in validation_results
        assert "overall_alignment_score" in validation_results
        assert "meets_target" in validation_results

        # F1 score should be less than 1.0 due to missing component
        f1_score = validation_results["f1_score"]["f1_score"]
        assert 0.0 <= f1_score < 1.0

        # Generate DeepEval tests
        test_path = self.deepeval_integration.generate_architecture_tests(architecture_spec)
        assert os.path.exists(test_path)

        # Run DeepEval tests
        test_results = self.deepeval_integration.run_deepeval_tests(test_path)
        assert "success" in test_results

    def test_requirement_mapping_coverage_analysis(self):
        """
        Test requirement mapping and coverage analysis
        """
        # Create test requirements
        requirements = {
            "functional": {
                "F-001": {
                    "description": "Golden Set validation system",
                    "priority": "high"
                },
                "F-002": {
                    "description": "LLM-as-judge evaluation system",
                    "priority": "high"
                },
                "F-003": {
                    "description": "Architecture alignment F1 evaluation",
                    "priority": "medium"
                }
            },
            "non_functional": {
                "NFR-P-001": {
                    "description": "Performance optimization",
                    "priority": "medium"
                },
                "NFR-SC-001": {
                    "description": "Scalable design",
                    "priority": "medium"
                }
            }
        }

        # Create temporary implementation files with requirement references
        impl_file1 = os.path.join(self.temp_dir, "impl1.py")
        with open(impl_file1, 'w') as f:
            f.write("""
# Implementation for F-001: Golden Set validation system
class GoldenSetManager:
    def validate_test_case(self, test_case_id):
        # F-001 implementation
        pass
""")

        impl_file2 = os.path.join(self.temp_dir, "impl2.py")
        with open(impl_file2, 'w') as f:
            f.write("""
# Implementation for F-002: LLM-as-judge evaluation system
class LLMJudge:
    def evaluate_response(self, response):
        # F-002 implementation
        # Also addresses NFR-P-001 performance requirements
        pass
""")

        # Load requirements
        self.requirement_mapper.load_requirements_from_dict(requirements)

        # Analyze implementation coverage
        coverage_results = self.requirement_mapper.analyze_implementation_coverage(
            implementation_files=[impl_file1, impl_file2]
        )

        assert coverage_results["total_requirements"] == 5
        assert coverage_results["covered_requirements"] >= 2  # F-001, F-002

        # Validate requirement coverage
        validation_results = self.requirement_mapper.validate_requirement_coverage(threshold=0.8)
        assert validation_results["overall_validation"] in ["pass", "fail"]

    def test_end_to_end_behavior_testing_workflow(self):
        """
        Complete end-to-end workflow test
        """
        # 1. Create Golden Set with test cases
        test_cases = [
            {
                "id": "e2e_test_1",
                "description": "End-to-end test case",
                "input": {"prompt": "Test prompt"},
                "expected_output": {"response": "Expected response"},
                "metadata": {"category": "e2e", "difficulty": "medium"}
            }
        ]

        self.golden_set_manager.add_test_case(test_cases[0])

        # 2. Generate Promptfoo configuration and run evaluation
        promptfoo_config = self.promptfoo_integration.generate_promptfoo_config(test_cases)
        evaluation_result = self.promptfoo_integration.run_evaluation(test_cases)

        # 3. Calculate F1 score for architecture alignment
        architecture_spec = {
            "components": [
                {"id": "golden_set_manager", "type": "business"},
                {"id": "promptfoo_integration", "type": "business"}
            ],
            "data_flows": [
                {"source": "golden_set_manager", "target": "promptfoo_integration"}
            ]
        }

        actual_impl = {
            "components": [
                {"id": "golden_set_manager", "type": "business"},
                {"id": "promptfoo_integration", "type": "business"}
            ],
            "data_flows": [
                {"source": "golden_set_manager", "target": "promptfoo_integration"}
            ]
        }

        validation_results = self.architecture_validator.validate_architecture_alignment(
            actual_implementation=actual_impl,
            expected_architecture=architecture_spec
        )

        # 4. Generate comprehensive validation report
        f1_results = validation_results["f1_score"]
        requirement_results = {
            "total_requirements": 3,
            "covered_requirements": 2,
            "coverage_percentage": 66.7,
            "requirement_details": [
                {"requirement_id": "F-001", "covered": True},
                {"requirement_id": "F-002", "covered": True},
                {"requirement_id": "F-003", "covered": False}
            ]
        }

        validation_report = self.deepeval_integration.generate_validation_report(
            f1_results=f1_results,
            requirement_results=requirement_results
        )

        assert "F1 Score Analysis" in validation_report
        assert "Requirement Coverage" in validation_report
        assert "Recommendations" in validation_report

    def test_multi_tool_collaboration_scenario(self):
        """
        Test collaboration between multiple tools in complex scenario
        """
        # Create complex test scenario
        complex_test_cases = [
            {
                "id": "complex_scenario_1",
                "description": "Multi-step reasoning test",
                "input": {"prompt": "Analyze the following business case and provide recommendations"},
                "expected_output": {"response": "Structured analysis with recommendations"},
                "metadata": {
                    "category": "business_analysis",
                    "difficulty": "hard",
                    "steps": ["analysis", "reasoning", "recommendation"]
                }
            },
            {
                "id": "complex_scenario_2",
                "description": "Code generation and validation",
                "input": {"prompt": "Generate Python code for data processing"},
                "expected_output": {"response": "Valid Python code with documentation"},
                "metadata": {
                    "category": "code_generation",
                    "difficulty": "medium",
                    "validation_rules": ["syntax", "documentation", "best_practices"]
                }
            }
        ]

        # Add to Golden Set
        for test_case in complex_test_cases:
            self.golden_set_manager.add_test_case(test_case)

        # Validate Golden Set
        golden_validation = self.golden_set_manager.validate_golden_set()
        assert golden_validation["valid"] is True

        # Run Promptfoo evaluation with custom metrics
        evaluation_config = {
            "prompts": [tc["input"]["prompt"] for tc in complex_test_cases],
            "providers": ["openai:gpt-4"],
            "tests": complex_test_cases,
            "metrics": ["answer_relevancy", "faithfulness", "custom_architecture_alignment"]
        }

        evaluation_result = self.promptfoo_integration.run_evaluation(
            test_cases=complex_test_cases,
            config=evaluation_config
        )

        # Generate DeepEval architecture validation tests
        architecture_spec = {
            "components": [
                {"id": "golden_set_manager", "type": "business"},
                {"id": "promptfoo_integration", "type": "business"},
                {"id": "deepeval_integration", "type": "business"}
            ],
            "data_flows": [
                {"source": "golden_set_manager", "target": "promptfoo_integration"},
                {"source": "promptfoo_integration", "target": "deepeval_integration"}
            ]
        }

        deepeval_test_path = self.deepeval_integration.generate_architecture_tests(architecture_spec)
        deepeval_results = self.deepeval_integration.run_deepeval_tests(deepeval_test_path)

        # Verify all components worked together
        assert golden_validation["valid"] is True
        assert "success" in evaluation_result
        assert "success" in deepeval_results

    def test_error_handling_and_recovery(self):
        """
        Test error handling and recovery mechanisms
        """
        # Test with invalid Golden Set data
        invalid_test_case = {
            "id": "",  # Invalid empty ID
            "description": "Invalid test case",
            "input": {},
            "expected_output": {}
        }

        # Should handle invalid data gracefully
        try:
            self.golden_set_manager.add_test_case(invalid_test_case)
        except Exception as e:
            # Expected to fail validation
            assert "validation" in str(e).lower() or "invalid" in str(e).lower()

        # Test with missing configuration files
        missing_config_path = "/nonexistent/config.yaml"
        promptfoo_with_missing_config = PromptfooIntegration(config_path=missing_config_path)

        # Should create default configuration
        assert promptfoo_with_missing_config.config is not None

        # Test architecture validation with missing components
        incomplete_architecture = {
            "components": [],
            "data_flows": []
        }

        validation_results = self.architecture_validator.validate_architecture_alignment(
            actual_implementation={},
            expected_architecture=incomplete_architecture
        )

        # Should handle empty architecture gracefully
        assert "f1_score" in validation_results
        assert validation_results["f1_score"]["f1_score"] == 0.0

    def test_performance_and_scalability(self):
        """
        Test performance and scalability of integrated system
        """
        # Create large number of test cases for performance testing
        large_test_set = []
        for i in range(100):  # 100 test cases
            large_test_set.append({
                "id": f"perf_test_{i}",
                "description": f"Performance test case {i}",
                "input": {"prompt": f"Test prompt {i}"},
                "expected_output": {"response": f"Test response {i}"},
                "metadata": {"category": "performance", "batch": i // 10}
            })

        # Time Golden Set operations
        import time
        start_time = time.time()

        for test_case in large_test_set:
            self.golden_set_manager.add_test_case(test_case)

        golden_set_time = time.time() - start_time

        # Validate performance (should be reasonable for 100 test cases)
        assert golden_set_time < 10.0  # Less than 10 seconds

        # Test Golden Set validation performance
        start_time = time.time()
        validation_result = self.golden_set_manager.validate_golden_set()
        validation_time = time.time() - start_time

        assert validation_result["valid"] is True
        assert validation_result["total_test_cases"] == 100
        assert validation_time < 5.0  # Less than 5 seconds

        # Test architecture validation performance
        large_architecture = {
            "components": [{"id": f"component_{i}", "type": "business"} for i in range(50)],
            "data_flows": [
                {"source": f"component_{i}", "target": f"component_{i+1}"}
                for i in range(49)
            ]
        }

        start_time = time.time()
        arch_validation = self.architecture_validator.validate_architecture_alignment(
            actual_implementation=large_architecture,
            expected_architecture=large_architecture
        )
        arch_validation_time = time.time() - start_time

        assert arch_validation["meets_target"] is True
        assert arch_validation_time < 5.0  # Less than 5 seconds

    def teardown_method(self):
        """Cleanup test fixtures"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)