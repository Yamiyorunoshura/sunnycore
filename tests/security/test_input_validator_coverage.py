"""
Test cases for Input Validator functionality - Task 5 brownfield improvement
Tests for input validation and security testing capabilities
"""

import pytest
import json
from typing import Dict, Any, List

from src.security.input_validator import InputValidator, ValidationResult
from src.security.types import SeverityLevel, TestCase, VulnerabilityType


class TestInputValidator:
    """Test suite for InputValidator functionality"""

    @pytest.fixture
    def validator(self):
        """Create InputValidator instance"""
        return InputValidator()

    @pytest.fixture
    def validator_with_config(self):
        """Create InputValidator with custom configuration"""
        config = {
            "max_input_length": 5000,
            "allowed_special_chars": set("_-@"),
            "enable_deep_validation": False
        }
        return InputValidator(config)

    def test_initialization_default_config(self, validator):
        """Test input validator initialization with default config"""
        assert validator.max_input_length == 10000
        assert validator.enable_deep_validation is True
        assert len(validator.allowed_special_chars) > 0

    def test_initialization_custom_config(self, validator_with_config):
        """Test input validator initialization with custom config"""
        assert validator_with_config.max_input_length == 5000
        assert validator_with_config.enable_deep_validation is False
        assert validator_with_config.allowed_special_chars == set("_-@")

    def test_validation_result_creation(self):
        """Test ValidationResult creation and post_init"""
        # Test with all fields
        result = ValidationResult(
            valid=True,
            error="Test error",
            warnings=["warning1", "warning2"],
            sanitized_data={"clean": "data"}
        )
        assert result.valid is True
        assert result.error == "Test error"
        assert result.warnings == ["warning1", "warning2"]
        assert result.sanitized_data == {"clean": "data"}

        # Test with warnings as None
        result = ValidationResult(valid=True)
        assert result.warnings == []

    def test_validate_string_input_valid(self, validator):
        """Test validation of valid string input"""
        result = validator.validate_input("Hello, World!")

        assert isinstance(result, ValidationResult)
        assert result.valid is True
        assert result.error is None
        assert len(result.warnings) == 0

    def test_validate_string_input_too_long(self, validator):
        """Test validation of string input that's too long"""
        # Create a very long string
        long_string = "a" * 15000
        result = validator.validate_input(long_string)

        assert isinstance(result, ValidationResult)
        assert result.valid is False
        assert "too long" in result.error.lower()

    def test_validate_string_input_with_special_chars(self, validator):
        """Test validation of string with special characters"""
        # Test with allowed characters
        valid_string = "test_user@example.com"
        result = validator.validate_input(valid_string)

        assert result.valid is True
        assert result.error is None

        # Test with potentially dangerous characters
        dangerous_string = "<script>alert('xss')</script>"
        result = validator.validate_input(dangerous_string)

        assert result.valid is False
        assert "dangerous" in result.error.lower()

    def test_validate_json_input_valid(self, validator):
        """Test validation of valid JSON input"""
        json_data = {"name": "test", "value": 123}
        result = validator.validate_input(json_data)

        assert isinstance(result, ValidationResult)
        assert result.valid is True
        assert result.error is None

    def test_validate_json_input_with_nested_dangerous_content(self, validator):
        """Test validation of JSON with nested dangerous content"""
        json_data = {
            "user_input": "<script>alert('xss')</script>",
            "nested": {
                "deep_field": "'; DROP TABLE users; --"
            }
        }
        result = validator.validate_input(json_data)

        assert result.valid is False
        assert result.error is not None

    def test_validate_list_input(self, validator):
        """Test validation of list input"""
        valid_list = ["item1", "item2", "item3"]
        result = validator.validate_input(valid_list)

        assert isinstance(result, ValidationResult)
        assert result.valid is True
        assert result.error is None

    def test_validate_list_with_dangerous_items(self, validator):
        """Test validation of list with dangerous items"""
        dangerous_list = ["safe_item", "<script>alert(1)</script>", "safe_item_2"]
        result = validator.validate_input(dangerous_list)

        assert result.valid is False
        assert result.error is not None

    def test_validate_number_input(self, validator):
        """Test validation of number input"""
        result = validator.validate_input(123)

        assert isinstance(result, ValidationResult)
        assert result.valid is True
        assert result.error is None

    def test_validate_none_input(self, validator):
        """Test validation of None input"""
        result = validator.validate_input(None)

        assert isinstance(result, ValidationResult)
        assert result.valid is True
        assert result.error is None

    def test_validate_boolean_input(self, validator):
        """Test validation of boolean input"""
        result_true = validator.validate_input(True)
        result_false = validator.validate_input(False)

        assert result_true.valid is True
        assert result_false.valid is True

    def test_validate_input_with_sanitization(self, validator):
        """Test that dangerous input is properly sanitized"""
        dangerous_input = "Hello<script>alert('xss')</script>World"
        result = validator.validate_input(dangerous_input)

        if not result.valid:
            assert result.sanitized_data is not None
            assert "<script>" not in str(result.sanitized_data)

    def test_batch_validation(self, validator):
        """Test batch validation of multiple inputs"""
        inputs = [
            "safe_string",
            {"key": "value"},
            ["item1", "item2"],
            123
        ]

        results = validator.validate_batch(inputs)

        assert isinstance(results, list)
        assert len(results) == len(inputs)
        assert all(isinstance(r, ValidationResult) for r in results)
        assert all(r.valid for r in results)

    def test_batch_validation_with_mixed_results(self, validator):
        """Test batch validation with mixed valid/invalid results"""
        inputs = [
            "safe_string",
            "<script>alert('xss')</script>",  # Dangerous
            {"key": "value"},
            "a" * 15000  # Too long
        ]

        results = validator.validate_batch(inputs)

        assert len(results) == len(inputs)
        assert results[0].valid is True  # safe_string
        assert results[1].valid is False  # Dangerous script
        assert results[2].valid is True  # Safe JSON
        assert results[3].valid is False  # Too long

    def test_sql_injection_detection(self, validator):
        """Test SQL injection detection"""
        sql_injection_attempts = [
            "'; DROP TABLE users; --",
            "1' OR '1'='1",
            "admin'--",
            "UNION SELECT * FROM passwords",
            "' OR 1=1#"
        ]

        for attempt in sql_injection_attempts:
            result = validator.validate_input(attempt)
            assert result.valid is False, f"SQL injection attempt not detected: {attempt}"

    def test_xss_detection(self, validator):
        """Test XSS detection"""
        xss_attempts = [
            "<script>alert('xss')</script>",
            "javascript:alert('xss')",
            "<img src=x onerror=alert('xss')>",
            "<svg onload=alert('xss')>",
            "'\"><script>alert(String.fromCharCode(88,83,83))</script>"
        ]

        for attempt in xss_attempts:
            result = validator.validate_input(attempt)
            assert result.valid is False, f"XSS attempt not detected: {attempt}"

    def test_command_injection_detection(self, validator):
        """Test command injection detection"""
        cmd_injection_attempts = [
            "; rm -rf /",
            "| ls -la",
            "&& cat /etc/passwd",
            "$(cat /etc/passwd)",
            "`cat /etc/passwd`"
        ]

        for attempt in cmd_injection_attempts:
            result = validator.validate_input(attempt)
            assert result.valid is False, f"Command injection attempt not detected: {attempt}"

    def test_path_traversal_detection(self, validator):
        """Test path traversal detection"""
        path_traversal_attempts = [
            "../../../etc/passwd",
            "..\\..\\windows\\system32\\config\\sam",
            "/etc/passwd%00",
            "....//....//....//etc/passwd"
        ]

        for attempt in path_traversal_attempts:
            result = validator.validate_input(attempt)
            assert result.valid is False, f"Path traversal attempt not detected: {attempt}"

    def test_configuration_updates(self, validator):
        """Test configuration updates"""
        # Test updating max length
        validator.update_config({"max_input_length": 2000})
        assert validator.max_input_length == 2000

        # Test updating allowed characters
        validator.update_config({"allowed_special_chars": set("_-")})
        assert validator.allowed_special_chars == set("_-")

    def test_custom_validation_rules(self, validator):
        """Test custom validation rules"""
        def custom_rule(data):
            if isinstance(data, str) and "blocked" in data.lower():
                return ValidationResult(valid=False, error="Contains blocked word")
            return ValidationResult(valid=True)

        validator.add_custom_rule(custom_rule)

        # Test blocked word
        result = validator.validate_input("This contains blocked word")
        assert result.valid is False
        assert "blocked word" in result.error

        # Test safe word
        result = validator.validate_input("This is safe")
        assert result.valid is True

    def test_validation_performance(self, validator):
        """Test validation performance with large datasets"""
        import time

        # Create a large number of inputs
        large_input_list = [f"safe_string_{i}" for i in range(1000)]

        start_time = time.time()
        results = validator.validate_batch(large_input_list)
        end_time = time.time()

        execution_time = end_time - start_time
        assert execution_time < 5.0, f"Validation took too long: {execution_time}s"
        assert len(results) == 1000
        assert all(r.valid for r in results)

    def test_validation_statistics(self, validator):
        """Test validation statistics tracking"""
        inputs = [
            "safe_string",
            "<script>alert('xss')</script>",
            {"key": "value"},
            "'; DROP TABLE users; --",
            123
        ]

        validator.validate_batch(inputs)
        stats = validator.get_validation_statistics()

        assert "total_validated" in stats
        assert "valid_count" in stats
        assert "invalid_count" in stats
        assert "validation_types" in stats

        assert stats["total_validated"] == 5
        assert stats["valid_count"] == 3
        assert stats["invalid_count"] == 2

    def test_unicode_handling(self, validator):
        """Test handling of unicode characters"""
        unicode_inputs = [
            "你好世界",  # Chinese
            "こんにちは",  # Japanese
            "안녕하세요",  # Korean
            "🚀 rocket emoji",  # Emoji
            "café",  # Accented characters
            "测试",  # More Chinese
        ]

        for input_data in unicode_inputs:
            result = validator.validate_input(input_data)
            assert result.valid is True, f"Unicode input rejected: {input_data}"

    def test_empty_input_handling(self, validator):
        """Test handling of empty inputs"""
        empty_inputs = ["", [], {}, 0, 0.0, False]

        for input_data in empty_inputs:
            result = validator.validate_input(input_data)
            assert result.valid is True, f"Empty input rejected: {input_data}"

    def test_deep_validation_toggle(self, validator):
        """Test deep validation toggle functionality"""
        # Enable deep validation
        validator.enable_deep_validation = True
        result = validator.validate_input("test_string")
        assert result.valid is True

        # Disable deep validation
        validator.enable_deep_validation = False
        result = validator.validate_input("test_string")
        assert result.valid is True

    def test_memory_safety(self, validator):
        """Test memory safety with extremely large inputs"""
        # Test with input that approaches memory limits
        huge_input = "a" * (validator.max_input_length + 1)

        result = validator.validate_input(huge_input)
        assert result.valid is False
        assert "too long" in result.error.lower()

    def test_concurrent_validation(self, validator):
        """Test concurrent validation capability"""
        import threading
        import queue

        def validation_worker(input_queue, result_queue):
            while not input_queue.empty():
                try:
                    input_data = input_queue.get_nowait()
                    result = validator.validate_input(input_data)
                    result_queue.put(result)
                except queue.Empty:
                    break

        # Create test data
        test_inputs = [f"test_string_{i}" for i in range(100)]
        input_queue = queue.Queue()
        result_queue = queue.Queue()

        for item in test_inputs:
            input_queue.put(item)

        # Create worker threads
        threads = []
        for _ in range(4):  # 4 concurrent workers
            thread = threading.Thread(
                target=validation_worker,
                args=(input_queue, result_queue)
            )
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Collect results
        results = []
        while not result_queue.empty():
            results.append(result_queue.get())

        assert len(results) == 100
        assert all(isinstance(r, ValidationResult) for r in results)
        assert all(r.valid for r in results)

    def test_error_message_consistency(self, validator):
        """Test that error messages are consistent and helpful"""
        dangerous_inputs = [
            ("<script>alert('xss')</script>", "xss"),
            ("'; DROP TABLE users; --", "sql"),
            ("../../../etc/passwd", "path traversal"),
            ("a" * 15000, "length")
        ]

        for input_data, expected_keyword in dangerous_inputs:
            result = validator.validate_input(input_data)
            assert result.valid is False
            assert expected_keyword.lower() in result.error.lower(), \
                f"Error message for {input_data} should contain '{expected_keyword}'"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])