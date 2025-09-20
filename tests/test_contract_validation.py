"""
Test suite for Contract Validation functionality

This module provides comprehensive test coverage for the contract validation system,
including unit tests, integration tests, and performance tests.
"""

import json
import time
import pytest
from pathlib import Path
from unittest.mock import Mock, patch
from src.validation.contract_validator import ContractValidator, ValidationResult


class TestContractValidator:
    """Test cases for ContractValidator class"""

    @pytest.fixture
    def validator(self):
        """Create a validator instance for testing"""
        return ContractValidator()

    @pytest.fixture
    def sample_requirements_data(self):
        """Sample requirements data for testing"""
        return {
            "metadata": {
                "document_id": "test-req-001",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "functional_requirements": [
                {
                    "id": "F-001",
                    "title": "User Authentication",
                    "description": "Implement user authentication system",
                    "priority": "high",
                    "acceptance_criteria": [
                        "Users can log in with valid credentials",
                        "Invalid credentials are rejected"
                    ]
                }
            ],
            "non_functional_requirements": [
                {
                    "id": "N-001",
                    "category": "performance",
                    "title": "Response Time",
                    "description": "System response time requirements",
                    "metrics": [
                        {
                            "name": "login_response_time",
                            "target": "< 2 seconds",
                            "measurement_method": "automated test"
                        }
                    ]
                }
            ]
        }

    @pytest.fixture
    def sample_architecture_data(self):
        """Sample architecture data for testing"""
        return {
            "metadata": {
                "document_id": "test-arch-001",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "components": [
                {
                    "component_id": "AuthService",
                    "name": "Authentication Service",
                    "type": "service",
                    "layer": "business",
                    "responsibilities": ["User authentication", "Token management"]
                }
            ],
            "data_flow": [
                {
                    "flow_id": "FLOW-001",
                    "source": "AuthService",
                    "target": "UserService",
                    "data_type": "User credentials",
                    "description": "Authentication data flow"
                }
            ],
            "interfaces": [
                {
                    "interface_id": "IF-001",
                    "name": "Auth API",
                    "type": "REST",
                    "components": ["AuthService", "UserService"]
                }
            ]
        }

    @pytest.fixture
    def invalid_requirements_data(self):
        """Invalid requirements data for testing error cases"""
        return {
            "metadata": {
                "document_id": "test-req-002",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            # Missing required functional_requirements
            "non_functional_requirements": []
        }

    @pytest.fixture
    def invalid_architecture_data(self):
        """Invalid architecture data for testing error cases"""
        return {
            "metadata": {
                "document_id": "test-arch-002",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            # Missing required components
            "data_flow": [],
            "interfaces": []
        }

    def test_validator_initialization(self, validator):
        """Test that validator initializes correctly"""
        assert validator.schemas_dir is not None
        assert isinstance(validator._schema_cache, dict)
        # Check for either registry (new) or resolver_cache (old)
        assert hasattr(validator, '_registry') or hasattr(validator, '_resolver_cache')

    def test_get_schema_requirements(self, validator):
        """Test getting requirements schema"""
        schema = validator.get_schema("requirements")
        assert schema is not None
        assert "$schema" in schema
        assert "title" in schema
        assert "requirements" in schema["title"].lower()

    def test_get_schema_architecture(self, validator):
        """Test getting architecture schema"""
        schema = validator.get_schema("architecture")
        assert schema is not None
        assert "$schema" in schema
        assert "title" in schema
        assert "architecture" in schema["title"].lower()

    def test_get_schema_nonexistent(self, validator):
        """Test getting non-existent schema"""
        schema = validator.get_schema("nonexistent")
        assert schema is None

    def test_validate_requirements_valid(self, validator, sample_requirements_data):
        """Test validating valid requirements data"""
        result = validator.validate_artifact(sample_requirements_data, "requirements")

        assert result.is_valid is True
        assert len(result.errors) == 0
        assert result.artifact_type == "requirements"
        assert result.validation_time > 0
        assert isinstance(result.validation_time, float)

    def test_validate_architecture_valid(self, validator, sample_architecture_data):
        """Test validating valid architecture data"""
        result = validator.validate_artifact(sample_architecture_data, "architecture")

        assert result.is_valid is True
        assert len(result.errors) == 0
        assert result.artifact_type == "architecture"
        assert result.validation_time > 0

    def test_validate_requirements_invalid(self, validator, invalid_requirements_data):
        """Test validating invalid requirements data"""
        result = validator.validate_artifact(invalid_requirements_data, "requirements")

        assert result.is_valid is False
        assert len(result.errors) > 0
        assert result.artifact_type == "requirements"

    def test_validate_architecture_invalid(self, validator, invalid_architecture_data):
        """Test validating invalid architecture data"""
        result = validator.validate_artifact(invalid_architecture_data, "architecture")

        assert result.is_valid is False
        assert len(result.errors) > 0
        assert result.artifact_type == "architecture"

    def test_validate_from_file(self, validator, tmp_path, sample_requirements_data):
        """Test validating from file"""
        # Create temporary file
        test_file = tmp_path / "test_requirements.json"
        with open(test_file, 'w') as f:
            json.dump(sample_requirements_data, f)

        result = validator.validate_artifact(test_file, "requirements")

        assert result.is_valid is True
        assert len(result.errors) == 0

    def test_validate_nonexistent_schema(self, validator, sample_requirements_data):
        """Test validating with non-existent schema"""
        result = validator.validate_artifact(sample_requirements_data, "nonexistent")

        assert result.is_valid is False
        assert "No schema found for artifact type: nonexistent" in result.errors

    def test_validation_performance_target(self, validator, sample_requirements_data):
        """Test that validation meets performance target (<1s)"""
        result = validator.validate_artifact(sample_requirements_data, "requirements")

        assert result.validation_time < 1.0, f"Validation took {result.validation_time}s, target is <1s"

    def test_validation_warnings_duplicate_ids(self, validator):
        """Test validation warnings for duplicate requirement IDs"""
        data = {
            "metadata": {
                "document_id": "test-req-003",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "functional_requirements": [
                {
                    "id": "F-001",
                    "title": "Test Requirement 1",
                    "description": "First test requirement",
                    "priority": "medium",
                    "acceptance_criteria": ["Test criterion 1"]
                },
                {
                    "id": "F-001",  # Duplicate ID
                    "title": "Test Requirement 2",
                    "description": "Second test requirement",
                    "priority": "medium",
                    "acceptance_criteria": ["Test criterion 2"]
                }
            ],
            "non_functional_requirements": []
        }

        result = validator.validate_artifact(data, "requirements")

        assert result.is_valid is True  # Should still be valid, just with warnings
        assert len(result.warnings) > 0
        assert any("Duplicate functional requirement IDs" in warning for warning in result.warnings)

    def test_validation_warnings_missing_dependencies(self, validator):
        """Test validation warnings for missing dependencies"""
        data = {
            "metadata": {
                "document_id": "test-req-004",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "functional_requirements": [
                {
                    "id": "F-001",
                    "title": "Test Requirement 1",
                    "description": "First test requirement",
                    "priority": "medium",
                    "acceptance_criteria": ["Test criterion 1"],
                    "dependencies": ["F-002"]  # Missing dependency
                }
            ],
            "non_functional_requirements": []
        }

        result = validator.validate_artifact(data, "requirements")

        assert result.is_valid is True
        assert len(result.warnings) > 0
        assert any("Dependency F-002 not found" in warning for warning in result.warnings)

    def test_strict_validation_requirements(self, validator):
        """Test strict validation for requirements"""
        data = {
            "metadata": {
                "document_id": "test-req-005",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "functional_requirements": [
                {
                    "id": "F-001",
                    "title": "Test Requirement",
                    "description": "Test requirement without estimated effort",
                    "priority": "medium",
                    "acceptance_criteria": ["Test criterion"]
                    # Missing estimated_effort
                }
            ],
            "non_functional_requirements": []
        }

        # Non-strict validation
        result_non_strict = validator.validate_artifact(data, "requirements", strict=False)
        assert result_non_strict.is_valid is True
        assert len(result_non_strict.warnings) == 0

        # Strict validation
        result_strict = validator.validate_artifact(data, "requirements", strict=True)
        assert result_strict.is_valid is True
        assert len(result_strict.warnings) > 0
        assert any("Missing estimated effort" in warning for warning in result_strict.warnings)

    def test_validate_multiple_artifacts(self, validator, sample_requirements_data, sample_architecture_data):
        """Test validating multiple artifacts"""
        artifacts = [
            {"id": "req1", "data": sample_requirements_data, "type": "requirements"},
            {"id": "arch1", "data": sample_architecture_data, "type": "architecture"}
        ]

        results = validator.validate_multiple_artifacts(artifacts)

        assert len(results) == 2
        assert "req1" in results
        assert "arch1" in results
        assert results["req1"].is_valid is True
        assert results["arch1"].is_valid is True

    def test_get_validation_summary(self, validator, sample_requirements_data, sample_architecture_data):
        """Test validation summary generation"""
        artifacts = [
            {"id": "req1", "data": sample_requirements_data, "type": "requirements"},
            {"id": "arch1", "data": sample_architecture_data, "type": "architecture"}
        ]

        results = validator.validate_multiple_artifacts(artifacts)
        summary = validator.get_validation_summary(results)

        assert summary['total_artifacts'] == 2
        assert summary['valid_artifacts'] == 2
        assert summary['invalid_artifacts'] == 0
        assert summary['success_rate'] == 1.0
        assert summary['total_errors'] == 0
        assert summary['total_warnings'] >= 0
        assert summary['average_validation_time'] > 0

    def test_clear_cache(self, validator):
        """Test cache clearing functionality"""
        # Ensure schema is cached
        validator.get_schema("requirements")
        assert len(validator._schema_cache) > 0

        # Clear cache
        validator.clear_cache()
        assert len(validator._schema_cache) == 0
        # Check for either registry (new) or resolver_cache (old)
        if hasattr(validator, '_resolver_cache'):
            assert len(validator._resolver_cache) == 0

    def test_schema_loading_error_handling(self, tmp_path):
        """Test handling of schema loading errors"""
        # Create invalid schema file
        schemas_dir = tmp_path / "schemas"
        schemas_dir.mkdir()
        invalid_schema = schemas_dir / "invalid.json"
        invalid_schema.write_text("{ invalid json")

        # Should still initialize without crashing
        validator = ContractValidator(schemas_dir)
        assert validator.schemas_dir == schemas_dir

    def test_validation_result_model(self):
        """Test ValidationResult model"""
        result = ValidationResult(
            is_valid=True,
            errors=[],
            warnings=["Test warning"],
            validation_time=0.5,
            schema_version="1.0",
            artifact_type="requirements"
        )

        assert result.is_valid is True
        assert len(result.errors) == 0
        assert len(result.warnings) == 1
        assert result.validation_time == 0.5
        assert result.schema_version == "1.0"
        assert result.artifact_type == "requirements"

    @pytest.mark.performance
    def test_validation_performance_under_load(self, validator, sample_requirements_data):
        """Test validation performance under load"""
        iterations = 100
        start_time = time.time()

        for _ in range(iterations):
            validator.validate_artifact(sample_requirements_data, "requirements")

        total_time = time.time() - start_time
        avg_time = total_time / iterations

        assert avg_time < 0.1, f"Average validation time {avg_time}s exceeds performance target of 0.1s"

    @pytest.mark.integration
    def test_end_to_end_validation_workflow(self, validator, tmp_path):
        """Test end-to-end validation workflow"""
        # Create test artifacts
        requirements_data = {
            "metadata": {
                "document_id": "test-e2e-req",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "functional_requirements": [
                {
                    "id": "F-001",
                    "title": "E2E Test Requirement",
                    "description": "End-to-end test requirement",
                    "priority": "high",
                    "acceptance_criteria": ["Test passes"],
                    "estimated_effort": {"hours": 8, "story_points": 3}
                }
            ],
            "non_functional_requirements": []
        }

        architecture_data = {
            "metadata": {
                "document_id": "test-e2e-arch",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "components": [
                {
                    "component_id": "TestService",
                    "name": "Test Service",
                    "type": "service",
                    "layer": "business",
                    "responsibilities": ["Testing functionality"]
                }
            ],
            "data_flow": [],
            "interfaces": []
        }

        # Write to files
        req_file = tmp_path / "requirements.json"
        arch_file = tmp_path / "architecture.json"

        with open(req_file, 'w') as f:
            json.dump(requirements_data, f)

        with open(arch_file, 'w') as f:
            json.dump(architecture_data, f)

        # Validate multiple artifacts
        artifacts = [
            {"id": "req", "data": str(req_file), "type": "requirements"},
            {"id": "arch", "data": str(arch_file), "type": "architecture"}
        ]

        results = validator.validate_multiple_artifacts(artifacts)
        summary = validator.get_validation_summary(results)

        # Verify end-to-end workflow
        assert summary['total_artifacts'] == 2
        assert summary['valid_artifacts'] == 2
        assert summary['success_rate'] == 1.0
        assert summary['performance_target_met'] is True
        assert summary['average_validation_time'] < 1.0

    def test_import_error_fallback(self):
        """Test fallback behavior when referencing library is not available"""
        with patch.dict('sys.modules', {'referencing': None}):
            # Force reload of module to trigger ImportError
            import importlib
            import sys

            # Remove module from cache if present
            if 'src.validation.contract_validator' in sys.modules:
                del sys.modules['src.validation.contract_validator']

            # Re-import to test ImportError path
            from src.validation.contract_validator import ContractValidator

            validator = ContractValidator()
            assert hasattr(validator, '_resolver_cache')
            assert not hasattr(validator, '_registry') or validator._registry is None

    
    def test_schema_loading_exception_handling(self, tmp_path):
        """Test exception handling during schema loading"""
        schemas_dir = tmp_path / "schemas"
        schemas_dir.mkdir()

        # Create a directory instead of a file to trigger IOError
        (schemas_dir / "directory_as_file").mkdir()

        validator = ContractValidator(schemas_dir)
        # Should not crash, should handle exception gracefully
        assert validator.schemas_dir == schemas_dir

    
    def test_strict_validation_missing_effort(self, validator):
        """Test strict validation for missing estimated effort"""
        data = {
            "metadata": {
                "document_id": "test-req-006",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "functional_requirements": [
                {
                    "id": "F-001",
                    "title": "Test Requirement",
                    "description": "Test requirement",
                    "priority": "medium",
                    "acceptance_criteria": ["Test criterion"]
                    # Missing estimated_effort - should trigger warning in strict mode
                }
            ],
            "non_functional_requirements": []
        }

        result = validator.validate_artifact(data, "requirements", strict=True)
        assert result.is_valid is True  # Should still be valid
        assert any("Missing estimated effort" in warning for warning in result.warnings)

    def test_architecture_validation_warnings(self, validator):
        """Test architecture validation warnings for duplicate component IDs"""
        data = {
            "metadata": {
                "document_id": "test-arch-003",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "components": [
                {
                    "component_id": "AuthService",
                    "name": "Authentication Service",
                    "type": "service",
                    "layer": "business",
                    "responsibilities": ["User authentication"]
                },
                {
                    "component_id": "AuthService",  # Duplicate ID
                    "name": "Auth Service Duplicate",
                    "type": "service",
                    "layer": "business",
                    "responsibilities": ["Duplicate auth"]
                }
            ],
            "data_flow": [],
            "interfaces": []
        }

        result = validator.validate_artifact(data, "architecture")
        assert result.is_valid is True
        assert any("Duplicate component IDs" in warning for warning in result.warnings)

    def test_data_flow_validation_warnings(self, validator):
        """Test data flow validation warnings for missing components"""
        data = {
            "metadata": {
                "document_id": "test-arch-004",
                "version": "1.0.0",
                "created_date": "2024-01-15T10:30:00Z",
                "author": "Test Author",
                "status": "approved"
            },
            "components": [
                {
                    "component_id": "AuthService",
                    "name": "Authentication Service",
                    "type": "service",
                    "layer": "business",
                    "responsibilities": ["User authentication"]
                }
            ],
            "data_flow": [
                {
                    "flow_id": "FLOW-001",
                    "source": "AuthService",
                    "target": "NonExistentService",  # Missing target
                    "data_type": "Test data",
                    "description": "Test flow"
                }
            ],
            "interfaces": []
        }

        result = validator.validate_artifact(data, "architecture")
        assert result.is_valid is True
        assert any("non-existent target" in warning for warning in result.warnings)

    
    def test_sequential_validation_path(self, validator, sample_requirements_data, sample_architecture_data):
        """Test sequential validation path in validate_multiple_artifacts"""
        artifacts = [
            {"id": "req1", "data": sample_requirements_data, "type": "requirements"},
            {"id": "arch1", "data": sample_architecture_data, "type": "architecture"}
        ]

        # Test with parallel=False to force sequential path
        results = validator.validate_multiple_artifacts(artifacts, parallel=False)

        assert len(results) == 2
        assert "req1" in results
        assert "arch1" in results
        assert results["req1"].is_valid is True
        assert results["arch1"].is_valid is True

    def test_cache_clearing_with_registry(self, validator):
        """Test cache clearing when registry is available"""
        # Ensure registry exists
        if hasattr(validator, '_registry'):
            original_registry = validator._registry
            validator.clear_cache()
            # Should create new registry
            assert validator._registry is not original_registry

    def test_command_line_interface(self, tmp_path, sample_requirements_data):
        """Test command-line interface functionality"""
        import subprocess
        import sys

        # Create test file
        test_file = tmp_path / "test_cli.json"
        with open(test_file, 'w') as f:
            json.dump(sample_requirements_data, f)

        # Test CLI invocation
        cli_script = Path(__file__).parent.parent / "src" / "validation" / "contract_validator.py"
        if cli_script.exists():
            result = subprocess.run([
                sys.executable, str(cli_script),
                str(test_file), "requirements",
                "--schemas-dir", str(tmp_path / "schemas")
            ], capture_output=True, text=True)

            # Should not crash and should produce output
            assert result.returncode in [0, 1]  # May pass or fail depending on schemas
            assert "Validation Result:" in result.stdout

    

if __name__ == '__main__':
    pytest.main([__file__, '-v'])