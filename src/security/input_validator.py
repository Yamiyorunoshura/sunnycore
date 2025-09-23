"""
Input Validator for Security Testing

This module provides comprehensive input validation capabilities for security test cases,
ensuring all inputs are properly sanitized and validated before processing.
"""

import json
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

from .types import SeverityLevel, TestCase, VulnerabilityType


@dataclass
class ValidationResult:
    """Result of input validation"""

    valid: bool
    error: Optional[str] = None
    warnings: List[str] = None
    sanitized_data: Optional[Any] = None

    def __post_init__(self):
        if self.warnings is None:
            self.warnings = []


class InputValidator:
    """
    Comprehensive input validation system for security testing.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the input validator.

        Args:
            config: Configuration dictionary for validation parameters
        """
        self.config = config or {}
        self.max_input_length = self.config.get("max_input_length", 10000)
        self.allowed_special_chars = self.config.get(
            "allowed_special_chars", set("_-@#$%^&*()")
        )
        self.enable_deep_validation = self.config.get("enable_deep_validation", True)

        # Initialize validation rules
        self._init_validation_rules()

    def _init_validation_rules(self):
        """Initialize validation rules for different input types."""
        self.validation_rules = {
            "test_id": {
                "pattern": r"^[a-zA-Z0-9_\-]{3,50}$",
                "min_length": 3,
                "max_length": 50,
                "description": "Test ID must be 3-50 characters, alphanumeric, underscores, and hyphens only",
            },
            "test_name": {
                "pattern": r"^[a-zA-Z0-9\s_\-.,!?:]{5,100}$",
                "min_length": 5,
                "max_length": 100,
                "description": "Test name must be 5-100 characters, basic punctuation allowed",
            },
            "description": {
                "min_length": 10,
                "max_length": 500,
                "description": "Description must be 10-500 characters",
            },
        }

        # Forbidden patterns for security
        self.forbidden_patterns = [
            r"<script[^>]*>.*?</script>",  # Script tags
            r"javascript:",  # JavaScript protocol
            r"vbscript:",  # VBScript protocol
            r"on\w+\s*=",  # Event handlers
            r"eval\s*\(",  # eval() function
            r"document\.",  # Document object access
            r"window\.",  # Window object access
            r"<iframe[^>]*>",  # iframe tags
            r"<object[^>]*>",  # object tags
            r"<embed[^>]*>",  # embed tags
        ]

    def validate_test_input(self, test_case: TestCase) -> ValidationResult:
        """
        Validate a security test case input.

        Args:
            test_case: The test case to validate

        Returns:
            ValidationResult: Validation result with details
        """
        errors = []
        warnings = []

        # Validate test_id
        test_id_result = self._validate_test_id(test_case.test_id)
        if not test_id_result.valid:
            errors.append(test_id_result.error)
        warnings.extend(test_id_result.warnings)

        # Validate test_name
        name_result = self._validate_test_name(test_case.name)
        if not name_result.valid:
            errors.append(name_result.error)
        warnings.extend(name_result.warnings)

        # Validate description
        desc_result = self._validate_description(test_case.description)
        if not desc_result.valid:
            errors.append(desc_result.error)
        warnings.extend(desc_result.warnings)

        # Validate input_data
        input_result = self._validate_input_data(test_case.input_data)
        if not input_result.valid:
            errors.append(input_result.error)
        warnings.extend(input_result.warnings)

        # Validate severity
        severity_result = self._validate_severity(test_case.severity)
        if not severity_result.valid:
            errors.append(severity_result.error)
        warnings.extend(severity_result.warnings)

        # Validate test_steps
        steps_result = self._validate_test_steps(test_case.test_steps)
        if not steps_result.valid:
            errors.append(steps_result.error)
        warnings.extend(steps_result.warnings)

        # Perform deep validation if enabled
        if self.enable_deep_validation:
            deep_result = self._deep_validation(test_case)
            if not deep_result.valid:
                errors.append(deep_result.error)
            warnings.extend(deep_result.warnings)

        # Return overall validation result
        valid = len(errors) == 0
        error_msg = "; ".join(errors) if errors else None

        return ValidationResult(
            valid=valid,
            error=error_msg,
            warnings=warnings,
            sanitized_data=self._sanitize_input(test_case) if valid else None,
        )

    def _validate_test_id(self, test_id: str) -> ValidationResult:
        """Validate test ID format."""
        if not test_id or not isinstance(test_id, str):
            return ValidationResult(
                valid=False, error="Test ID is required and must be a string"
            )

        rules = self.validation_rules["test_id"]

        if len(test_id) < rules["min_length"] or len(test_id) > rules["max_length"]:
            return ValidationResult(
                valid=False,
                error=f"Test ID must be between {rules['min_length']} and {rules['max_length']} characters",
            )

        if not re.match(rules["pattern"], test_id):
            return ValidationResult(
                valid=False,
                error=f"Test ID contains invalid characters. {rules['description']}",
            )

        return ValidationResult(valid=True)

    def _validate_test_name(self, name: str) -> ValidationResult:
        """Validate test name format."""
        if not name or not isinstance(name, str):
            return ValidationResult(
                valid=False, error="Test name is required and must be a string"
            )

        rules = self.validation_rules["test_name"]

        if len(name) < rules["min_length"] or len(name) > rules["max_length"]:
            return ValidationResult(
                valid=False,
                error=f"Test name must be between {rules['min_length']} and {rules['max_length']} characters",
            )

        if not re.match(rules["pattern"], name):
            return ValidationResult(
                valid=False,
                error=f"Test name contains invalid characters. {rules['description']}",
            )

        return ValidationResult(valid=True)

    def _validate_description(self, description: str) -> ValidationResult:
        """Validate description format."""
        if not description or not isinstance(description, str):
            return ValidationResult(
                valid=False, error="Description is required and must be a string"
            )

        rules = self.validation_rules["description"]

        if (
            len(description) < rules["min_length"]
            or len(description) > rules["max_length"]
        ):
            return ValidationResult(
                valid=False,
                error=f"Description must be between {rules['min_length']} and {rules['max_length']} characters",
            )

        return ValidationResult(valid=True)

    def _validate_input_data(self, input_data: Any) -> ValidationResult:
        """Validate input data format and content."""
        if input_data is None:
            return ValidationResult(valid=False, error="Input data is required")

        # Convert to string for length validation
        str_input = str(input_data)

        if len(str_input) > self.max_input_length:
            return ValidationResult(
                valid=False,
                error=f"Input data exceeds maximum length of {self.max_input_length} characters",
            )

        # Check for forbidden patterns
        for pattern in self.forbidden_patterns:
            if re.search(pattern, str_input, re.IGNORECASE | re.DOTALL):
                return ValidationResult(
                    valid=False,
                    error=f"Input data contains forbidden pattern: {pattern}",
                )

        return ValidationResult(valid=True)

    def _validate_severity(self, severity: SeverityLevel) -> ValidationResult:
        """Validate severity level."""
        if not isinstance(severity, SeverityLevel):
            return ValidationResult(
                valid=False,
                error=f"Severity must be a SeverityLevel enum value, got {type(severity)}",
            )

        return ValidationResult(valid=True)

    def _validate_test_steps(self, test_steps: List[str]) -> ValidationResult:
        """Validate test steps format."""
        if not isinstance(test_steps, list):
            return ValidationResult(valid=False, error="Test steps must be a list")

        if not test_steps:
            return ValidationResult(
                valid=False, error="At least one test step is required"
            )

        for i, step in enumerate(test_steps):
            if not isinstance(step, str):
                return ValidationResult(
                    valid=False, error=f"Test step {i} must be a string"
                )

            if len(step.strip()) == 0:
                return ValidationResult(
                    valid=False, error=f"Test step {i} cannot be empty"
                )

        return ValidationResult(valid=True)

    def _deep_validation(self, test_case: TestCase) -> ValidationResult:
        """Perform deep validation checks on test case."""
        warnings = []

        # Check for potentially dangerous inputs
        str_input = str(test_case.input_data).lower()
        dangerous_keywords = [
            "delete",
            "drop",
            "truncate",
            "exec",
            "eval",
            "system",
            "shell_exec",
            "passthru",
            "proc_open",
            "popen",
        ]

        found_keywords = [kw for kw in dangerous_keywords if kw in str_input]
        if found_keywords:
            warnings.append(
                f"Input contains potentially dangerous keywords: {', '.join(found_keywords)}"
            )

        # Check for SQL injection patterns
        sql_patterns = [
            r"\b(select|insert|update|delete|drop|create|alter)\s+\w+",
            r"\b(union\s+select)\b",
            r"\b(or\s+\d+\s*=\s*\d+)\b",
            r"\b(and\s+\d+\s*=\s*\d+)\b",
        ]

        for pattern in sql_patterns:
            if re.search(pattern, str_input):
                warnings.append(
                    f"Input contains potential SQL injection pattern: {pattern}"
                )
                break

        # Check for XSS patterns
        xss_patterns = [
            r"<[^>]*script[^>]*>",
            r"javascript:",
            r"on\w+\s*=",
            r"<\s*iframe[^>]*>",
            r"<\s*object[^>]*>",
        ]

        for pattern in xss_patterns:
            if re.search(pattern, str_input, re.IGNORECASE):
                warnings.append(f"Input contains potential XSS pattern: {pattern}")
                break

        return ValidationResult(valid=True, warnings=warnings)

    def _sanitize_input(self, test_case: TestCase) -> TestCase:
        """Sanitize input data to prevent injection attacks."""
        # Create a copy of the test case
        sanitized_case = TestCase(
            test_id=test_case.test_id,
            name=test_case.name,
            description=test_case.description,
            vulnerability_type=test_case.vulnerability_type,
            severity=test_case.severity,
            input_data=test_case.input_data,
            expected_behavior=test_case.expected_behavior,
            test_steps=test_case.test_steps.copy(),
            prerequisites=test_case.prerequisites.copy(),
            tags=test_case.tags.copy(),
        )

        # Sanitize string inputs
        if isinstance(sanitized_case.input_data, str):
            sanitized_case.input_data = self._sanitize_string(sanitized_case.input_data)

        sanitized_case.name = self._sanitize_string(sanitized_case.name)
        sanitized_case.description = self._sanitize_string(sanitized_case.description)
        sanitized_case.expected_behavior = self._sanitize_string(
            sanitized_case.expected_behavior
        )

        # Sanitize test steps
        sanitized_case.test_steps = [
            self._sanitize_string(step) for step in sanitized_case.test_steps
        ]

        return sanitized_case

    def _sanitize_string(self, input_str: str) -> str:
        """Sanitize a string input."""
        if not isinstance(input_str, str):
            return input_str

        # Remove HTML tags
        sanitized = re.sub(r"<[^>]*>", "", input_str)

        # Escape special characters
        sanitized = sanitized.replace("&", "&amp;")
        sanitized = sanitized.replace("<", "&lt;")
        sanitized = sanitized.replace(">", "&gt;")
        sanitized = sanitized.replace('"', "&quot;")
        sanitized = sanitized.replace("'", "&#x27;")

        # Remove null bytes
        sanitized = sanitized.replace("\x00", "")

        # Normalize whitespace
        sanitized = " ".join(sanitized.split())

        return sanitized

    def validate_json_input(self, json_data: str) -> ValidationResult:
        """
        Validate JSON input data.

        Args:
            json_data: JSON string to validate

        Returns:
            ValidationResult: Validation result
        """
        try:
            data = json.loads(json_data)

            # Basic JSON validation
            if not isinstance(data, dict):
                return ValidationResult(
                    valid=False, error="JSON data must be an object"
                )

            # Validate size
            json_size = len(json_data)
            if json_size > self.max_input_length:
                return ValidationResult(
                    valid=False,
                    error=f"JSON data exceeds maximum size of {self.max_input_length} characters",
                )

            # Check for dangerous keys
            dangerous_keys = ["__proto__", "constructor", "prototype"]
            for key in data.keys():
                if key in dangerous_keys:
                    return ValidationResult(
                        valid=False, error=f"JSON contains dangerous key: {key}"
                    )

            return ValidationResult(valid=True, sanitized_data=data)

        except json.JSONDecodeError as e:
            return ValidationResult(valid=False, error=f"Invalid JSON format: {str(e)}")

    def validate_batch_input(
        self, test_cases: List[TestCase]
    ) -> List[ValidationResult]:
        """
        Validate a batch of test cases.

        Args:
            test_cases: List of test cases to validate

        Returns:
            List[ValidationResult]: Validation results for each test case
        """
        return [self.validate_test_input(test_case) for test_case in test_cases]

    def get_validation_rules(self) -> Dict[str, Any]:
        """Get the current validation rules."""
        return {
            "max_input_length": self.max_input_length,
            "allowed_special_chars": list(self.allowed_special_chars),
            "enable_deep_validation": self.enable_deep_validation,
            "validation_rules": self.validation_rules,
            "forbidden_patterns": self.forbidden_patterns,
        }

    def update_validation_rules(self, new_rules: Dict[str, Any]):
        """Update validation rules."""
        if "max_input_length" in new_rules:
            self.max_input_length = new_rules["max_input_length"]

        if "allowed_special_chars" in new_rules:
            self.allowed_special_chars = set(new_rules["allowed_special_chars"])

        if "enable_deep_validation" in new_rules:
            self.enable_deep_validation = new_rules["enable_deep_validation"]

        if "validation_rules" in new_rules:
            self.validation_rules.update(new_rules["validation_rules"])

        if "forbidden_patterns" in new_rules:
            self.forbidden_patterns.extend(new_rules["forbidden_patterns"])
