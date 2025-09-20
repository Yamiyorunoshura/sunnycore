"""
Contract Validator Module

This module provides JSON Schema validation for pipeline artifacts
with performance optimization and comprehensive error reporting.
"""

import json
import time
from typing import Dict, Any, List, Optional, Union
from pathlib import Path
from functools import lru_cache
from jsonschema import validate, ValidationError, SchemaError
try:
    from referencing import Registry, Resource
    from jsonschema.validators import Draft7Validator
    HAS_REFERENCING = True
except ImportError:
    HAS_REFERENCING = False
    from jsonschema import RefResolver
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)


class ValidationResult(BaseModel):
    """Result of contract validation"""
    is_valid: bool
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    validation_time: float
    schema_version: str
    artifact_type: str


class ContractValidator:
    """Contract validator for pipeline artifacts"""

    def __init__(self, schemas_dir: Optional[Path] = None):
        """
        Initialize contract validator

        Args:
            schemas_dir: Directory containing JSON schema files
        """
        self.schemas_dir = schemas_dir or Path(__file__).parent / "schemas"
        self._schema_cache: Dict[str, Dict] = {}
        if HAS_REFERENCING:
            self._registry = Registry()
        else:
            self._resolver_cache: Dict[str, RefResolver] = {}

        # Pre-load schemas for better performance
        self._load_schemas()

    def _load_schemas(self) -> None:
        """Load all available schemas from the schemas directory"""
        try:
            schema_files = list(self.schemas_dir.glob("*.json"))
            for schema_file in schema_files:
                try:
                    with open(schema_file, 'r', encoding='utf-8') as f:
                        schema_data = json.load(f)

                    schema_id = schema_data.get('$id', schema_file.stem)
                    self._schema_cache[schema_id] = schema_data

                    # Create resolver for schema references
                    if '$id' in schema_data:
                        if HAS_REFERENCING:
                            try:
                                resource = Resource.from_contents(schema_data)
                                self._registry = self._registry.with_resource(resource)
                            except Exception as e:
                                logger.warning(f"Failed to create resource for {schema_id}: {e}")
                        else:
                            self._resolver_cache[schema_id] = RefResolver(
                                base_uri=schema_data['$id'],
                                referrer=schema_data
                            )

                    logger.info(f"Loaded schema: {schema_id}")

                except (json.JSONDecodeError, IOError) as e:
                    logger.error(f"Failed to load schema {schema_file}: {e}")

        except Exception as e:
            logger.error(f"Failed to load schemas from {self.schemas_dir}: {e}")

    @lru_cache(maxsize=128)
    def get_schema(self, artifact_type: str) -> Optional[Dict]:
        """
        Get schema for a specific artifact type

        Args:
            artifact_type: Type of artifact (e.g., 'requirements', 'architecture')

        Returns:
            Schema dictionary or None if not found
        """
        schema_id = f"https://github.com/company/multi-stage-testing-framework/schemas/{artifact_type}_schema.json"
        return self._schema_cache.get(schema_id)

    def validate_artifact(
        self,
        artifact_data: Union[Dict, str, Path],
        artifact_type: str,
        strict: bool = True
    ) -> ValidationResult:
        """
        Validate an artifact against its schema

        Args:
            artifact_data: Artifact data (dict, JSON string, or file path)
            artifact_type: Type of artifact to validate
            strict: Whether to use strict validation mode

        Returns:
            ValidationResult object
        """
        start_time = time.time()

        try:
            # Parse input data
            if isinstance(artifact_data, (str, Path)):
                with open(artifact_data, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = artifact_data

            # Get schema
            schema = self.get_schema(artifact_type)
            if not schema:
                return ValidationResult(
                    is_valid=False,
                    errors=[f"No schema found for artifact type: {artifact_type}"],
                    validation_time=time.time() - start_time,
                    schema_version="unknown",
                    artifact_type=artifact_type
                )

            # Validate against schema
            if HAS_REFERENCING:
                validator = Draft7Validator(schema, registry=self._registry)
                validator.validate(data)
            else:
                resolver = self._resolver_cache.get(
                    f"https://github.com/company/multi-stage-testing-framework/schemas/{artifact_type}_schema.json"
                )
                validate(instance=data, schema=schema, resolver=resolver)

            # Additional validation rules
            warnings = self._additional_validation(data, artifact_type, strict)

            return ValidationResult(
                is_valid=True,
                warnings=warnings,
                validation_time=time.time() - start_time,
                schema_version=schema.get('$schema', 'unknown'),
                artifact_type=artifact_type
            )

        except ValidationError as e:
            return ValidationResult(
                is_valid=False,
                errors=self._format_validation_error(e),
                validation_time=time.time() - start_time,
                schema_version=schema.get('$schema', 'unknown') if 'schema' in locals() else 'unknown',
                artifact_type=artifact_type
            )
        except SchemaError as e:
            return ValidationResult(
                is_valid=False,
                errors=[f"Schema error: {str(e)}"],
                validation_time=time.time() - start_time,
                schema_version="unknown",
                artifact_type=artifact_type
            )
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                errors=[f"Unexpected error: {str(e)}"],
                validation_time=time.time() - start_time,
                schema_version="unknown",
                artifact_type=artifact_type
            )

    def _additional_validation(
        self,
        data: Dict,
        artifact_type: str,
        strict: bool
    ) -> List[str]:
        """
        Perform additional validation beyond JSON schema

        Args:
            data: Artifact data
            artifact_type: Type of artifact
            strict: Whether to use strict validation

        Returns:
            List of warnings
        """
        warnings = []

        if artifact_type == "requirements":
            warnings.extend(self._validate_requirements(data, strict))
        elif artifact_type == "architecture":
            warnings.extend(self._validate_architecture(data, strict))

        return warnings

    def _validate_requirements(self, data: Dict, strict: bool) -> List[str]:
        """Validate specific requirements for requirements documents"""
        warnings = []

        # Check for duplicate requirement IDs
        req_ids = [req.get('id') for req in data.get('functional_requirements', [])]
        duplicate_ids = [req_id for req_id in set(req_ids) if req_ids.count(req_id) > 1]
        if duplicate_ids:
            warnings.append(f"Duplicate functional requirement IDs found: {duplicate_ids}")

        # Check for missing dependencies
        for req in data.get('functional_requirements', []):
            dependencies = req.get('dependencies', [])
            for dep_id in dependencies:
                if dep_id not in req_ids:
                    warnings.append(f"Dependency {dep_id} not found in requirements")

        # Strict mode checks
        if strict:
            # Check for estimated effort
            for req in data.get('functional_requirements', []):
                if 'estimated_effort' not in req:
                    warnings.append(f"Missing estimated effort for requirement {req.get('id')}")

            # Check for acceptance criteria
            for req in data.get('functional_requirements', []):
                if not req.get('acceptance_criteria'):
                    warnings.append(f"Missing acceptance criteria for requirement {req.get('id')}")

        return warnings

    def _validate_architecture(self, data: Dict, strict: bool) -> List[str]:
        """Validate specific requirements for architecture documents"""
        warnings = []

        # Check for duplicate component IDs
        component_ids = [comp.get('component_id') for comp in data.get('components', [])]
        duplicate_ids = [comp_id for comp_id in set(component_ids) if component_ids.count(comp_id) > 1]
        if duplicate_ids:
            warnings.append(f"Duplicate component IDs found: {duplicate_ids}")

        # Check for missing dependencies
        all_components = set(component_ids)
        for comp in data.get('components', []):
            dependencies = comp.get('dependencies', [])
            for dep_id in dependencies:
                if dep_id not in all_components:
                    warnings.append(f"Component {comp.get('component_id')} depends on non-existent component {dep_id}")

        # Check data flow consistency
        data_flows = data.get('data_flow', [])
        for flow in data_flows:
            source = flow.get('source')
            target = flow.get('target')
            if source not in all_components:
                warnings.append(f"Data flow {flow.get('flow_id')} has non-existent source: {source}")
            if target not in all_components:
                warnings.append(f"Data flow {flow.get('flow_id')} has non-existent target: {target}")

        # Strict mode checks
        if strict:
            # Check for interface specifications
            for interface in data.get('interfaces', []):
                if 'specification' not in interface:
                    warnings.append(f"Missing specification for interface {interface.get('interface_id')}")

            # Check for SLA definitions
            for interface in data.get('interfaces', []):
                if 'sla' not in interface:
                    warnings.append(f"Missing SLA definition for interface {interface.get('interface_id')}")

        return warnings

    def _format_validation_error(self, error: ValidationError) -> List[str]:
        """Format JSON Schema validation errors"""
        errors = []

        def extract_errors(err, path=""):
            if err.path:
                error_path = path + "/" + "/".join(str(p) for p in err.path)
            else:
                error_path = path

            errors.append(f"Validation error at {error_path}: {err.message}")

            for sub_error in err.context:
                extract_errors(sub_error, error_path)

        extract_errors(error)
        return errors

    def validate_multiple_artifacts(
        self,
        artifacts: List[Dict[str, Any]],
        parallel: bool = True
    ) -> Dict[str, ValidationResult]:
        """
        Validate multiple artifacts

        Args:
            artifacts: List of artifact dictionaries with 'data' and 'type' keys
            parallel: Whether to validate in parallel

        Returns:
            Dictionary mapping artifact identifiers to validation results
        """
        results = {}

        if parallel:
            # For now, implement sequential validation
            # In production, use asyncio or multiprocessing for true parallel validation
            for i, artifact in enumerate(artifacts):
                artifact_id = artifact.get('id', f'artifact_{i}')
                result = self.validate_artifact(
                    artifact['data'],
                    artifact['type']
                )
                results[artifact_id] = result
        else:
            for i, artifact in enumerate(artifacts):
                artifact_id = artifact.get('id', f'artifact_{i}')
                result = self.validate_artifact(
                    artifact['data'],
                    artifact['type']
                )
                results[artifact_id] = result

        return results

    def get_validation_summary(self, results: Dict[str, ValidationResult]) -> Dict[str, Any]:
        """
        Generate summary of validation results

        Args:
            results: Dictionary of validation results

        Returns:
            Summary dictionary
        """
        total_artifacts = len(results)
        valid_artifacts = sum(1 for r in results.values() if r.is_valid)
        invalid_artifacts = total_artifacts - valid_artifacts

        total_errors = sum(len(r.errors) for r in results.values())
        total_warnings = sum(len(r.warnings) for r in results.values())
        avg_validation_time = sum(r.validation_time for r in results.values()) / total_artifacts if total_artifacts > 0 else 0

        return {
            'total_artifacts': total_artifacts,
            'valid_artifacts': valid_artifacts,
            'invalid_artifacts': invalid_artifacts,
            'success_rate': valid_artifacts / total_artifacts if total_artifacts > 0 else 0,
            'total_errors': total_errors,
            'total_warnings': total_warnings,
            'average_validation_time': avg_validation_time,
            'performance_target_met': avg_validation_time < 1.0  # 1 second target
        }

    def clear_cache(self) -> None:
        """Clear the schema cache"""
        self._schema_cache.clear()
        if HAS_REFERENCING:
            # Registry doesn't have a clear method, but we can create a new one
            self._registry = Registry()
        else:
            self._resolver_cache.clear()
        self.get_schema.cache_clear()


def main():
    """Main function for command-line usage"""
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Validate pipeline artifacts against JSON schemas')
    parser.add_argument('artifact_file', help='Path to artifact file to validate')
    parser.add_argument('artifact_type', choices=['requirements', 'architecture'],
                       help='Type of artifact to validate')
    parser.add_argument('--schemas-dir', help='Directory containing schema files')
    parser.add_argument('--strict', action='store_true', help='Enable strict validation')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Initialize validator
    validator = ContractValidator(Path(args.schemas_dir) if args.schemas_dir else None)

    # Validate artifact
    result = validator.validate_artifact(args.artifact_file, args.artifact_type, args.strict)

    # Print results
    print(f"Validation Result: {'PASS' if result.is_valid else 'FAIL'}")
    print(f"Validation Time: {result.validation_time:.3f}s")
    print(f"Schema Version: {result.schema_version}")

    if result.errors:
        print("\nErrors:")
        for error in result.errors:
            print(f"  - {error}")

    if result.warnings:
        print("\nWarnings:")
        for warning in result.warnings:
            print(f"  - {warning}")

    # Exit with appropriate code
    sys.exit(0 if result.is_valid else 1)


if __name__ == '__main__':
    main()