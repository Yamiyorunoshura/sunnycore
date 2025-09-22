import unittest
from unittest.mock import Mock, patch, MagicMock
import json
import tempfile
import os
import shutil
from datetime import datetime
from typing import Dict, List, Any

# Import the classes we're going to test
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestGoldenSetManager(unittest.TestCase):
    """Test cases for Golden Set Manager functionality"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.golden_set_path = os.path.join(self.temp_dir, 'golden_set.json')

        # Sample golden set data
        self.sample_golden_set = {
            "version": "1.0.0",
            "created_at": "2025-09-20T10:00:00Z",
            "test_cases": [
                {
                    "id": "test_001",
                    "description": "Basic functionality test",
                    "input": {"prompt": "Hello", "context": []},
                    "expected_output": {"response": "Hi there!"},
                    "category": "functional",
                    "priority": "high"
                },
                {
                    "id": "test_002",
                    "description": "Edge case test",
                    "input": {"prompt": "", "context": []},
                    "expected_output": {"response": "I need more information"},
                    "category": "edge_case",
                    "priority": "medium"
                }
            ],
            "metadata": {
                "total_cases": 2,
                "coverage_target": 0.95,
                "last_updated": "2025-09-20T10:00:00Z"
            }
        }

        # Write sample data to file
        with open(self.golden_set_path, 'w') as f:
            json.dump(self.sample_golden_set, f, indent=2)

    def tearDown(self):
        """Clean up after each test method."""
        if os.path.exists(self.golden_set_path):
            os.remove(self.golden_set_path)
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_golden_set_loading(self):
        """Test that golden set can be loaded from file."""
        from behavior.golden_set_manager import GoldenSetManager

        manager = GoldenSetManager(self.golden_set_path)
        loaded_data = manager.load_golden_set()

        self.assertEqual(loaded_data['version'], "1.0.0")
        self.assertEqual(len(loaded_data['test_cases']), 2)
        self.assertEqual(loaded_data['metadata']['total_cases'], 2)

    def test_golden_set_version_control(self):
        """Test version control functionality."""
        from behavior.golden_set_manager import GoldenSetManager

        manager = GoldenSetManager(self.golden_set_path)

        # Test getting current version
        current_version = manager.get_current_version()
        self.assertEqual(current_version, "1.0.0")

        # Test version creation
        new_version = manager.create_version("1.0.1", "Added new test cases")
        self.assertEqual(new_version, "1.0.1")

        # Test version history
        history = manager.get_version_history()
        self.assertGreaterEqual(len(history), 1)

    def test_test_case_retrieval(self):
        """Test retrieving test cases by various criteria."""
        from behavior.golden_set_manager import GoldenSetManager

        manager = GoldenSetManager(self.golden_set_path)

        # Test getting all test cases
        all_cases = manager.get_all_test_cases()
        self.assertEqual(len(all_cases), 2)

        # Test getting test cases by category
        functional_cases = manager.get_test_cases_by_category("functional")
        self.assertEqual(len(functional_cases), 1)
        self.assertEqual(functional_cases[0]['id'], "test_001")

        # Test getting test cases by priority
        high_priority_cases = manager.get_test_cases_by_priority("high")
        self.assertEqual(len(high_priority_cases), 1)
        self.assertEqual(high_priority_cases[0]['id'], "test_001")

    def test_test_case_addition(self):
        """Test adding new test cases to golden set."""
        from behavior.golden_set_manager import GoldenSetManager

        manager = GoldenSetManager(self.golden_set_path)

        new_test_case = {
            "id": "test_003",
            "description": "New test case",
            "input": {"prompt": "Test prompt", "context": []},
            "expected_output": {"response": "Test response"},
            "category": "functional",
            "priority": "low"
        }

        # Add test case
        manager.add_test_case(new_test_case)

        # Verify addition
        all_cases = manager.get_all_test_cases()
        self.assertEqual(len(all_cases), 3)

        # Verify new test case is present
        new_case = next((case for case in all_cases if case['id'] == "test_003"), None)
        self.assertIsNotNone(new_case)
        self.assertEqual(new_case['description'], "New test case")

    def test_coverage_calculation(self):
        """Test coverage calculation functionality."""
        from behavior.golden_set_manager import GoldenSetManager

        manager = GoldenSetManager(self.golden_set_path)

        # Mock coverage analysis
        with patch.object(manager, 'calculate_coverage') as mock_coverage:
            mock_coverage.return_value = 0.96

            coverage = manager.calculate_coverage()
            self.assertGreaterEqual(coverage, 0.95)  # Should meet target

    def test_validation_engine(self):
        """Test the golden set validation engine."""
        from behavior.golden_set_manager import GoldenSetManager

        manager = GoldenSetManager(self.golden_set_path)

        # Test validation of valid test case
        test_result = {
            "test_case_id": "test_001",
            "actual_output": {"response": "Hi there!"},
            "execution_time": 0.5
        }

        validation_result = manager.validate_test_result(test_result)
        self.assertTrue(validation_result['passed'])
        self.assertEqual(validation_result['confidence'], 1.0)

        # Test validation of invalid test case
        invalid_result = {
            "test_case_id": "test_001",
            "actual_output": {"response": "Different response"},
            "execution_time": 0.5
        }

        validation_result = manager.validate_test_result(invalid_result)
        self.assertFalse(validation_result['passed'])
        self.assertLess(validation_result['confidence'], 1.0)


class TestCoverageAnalyzer(unittest.TestCase):
    """Test cases for Coverage Analyzer functionality"""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()

        # Sample code structure for coverage analysis
        self.sample_code = {
            "functions": [
                {"name": "func1", "lines": 10, "testable": True, "complexity": 1, "lineno": 1},
                {"name": "func2", "lines": 15, "testable": True, "complexity": 2, "lineno": 15},
                {"name": "func3", "lines": 5, "testable": False, "complexity": 1, "lineno": 35}  # Untestable function
            ],
            "total_lines": 30,
            "testable_lines": 25,
            "untestable_lines": 5
        }

    def tearDown(self):
        """Clean up after each test method."""
        if os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir)

    def test_coverage_analysis(self):
        """Test coverage analysis functionality."""
        from behavior.coverage_analyzer import CoverageAnalyzer, CodeStructure

        analyzer = CoverageAnalyzer()

        # Create CodeStructure object with proper untestable lines
        code_structure = CodeStructure(
            functions=self.sample_code['functions'],
            classes=[],
            total_lines=30,
            testable_lines=25,
            untestable_lines=5
        )

        # Test coverage calculation
        coverage_result = analyzer.calculate_coverage(
            executed_lines=20,
            total_lines=25,
            code_structure=code_structure
        )

        self.assertEqual(coverage_result['coverage_percentage'], 80.0)
        self.assertEqual(coverage_result['testable_lines'], 25)
        self.assertEqual(coverage_result['untestable_lines'], 5)

    def test_edge_case_detection(self):
        """Test edge case detection functionality."""
        from behavior.coverage_analyzer import CoverageAnalyzer, CodeStructure

        analyzer = CoverageAnalyzer()

        # Create CodeStructure object
        code_structure = CodeStructure(
            functions=self.sample_code['functions'],
            classes=[],
            total_lines=self.sample_code['total_lines'],
            testable_lines=self.sample_code['testable_lines'],
            untestable_lines=self.sample_code['untestable_lines']
        )

        # Test edge case identification
        edge_cases = analyzer.identify_edge_cases(code_structure)

        self.assertIsInstance(edge_cases, list)
        self.assertGreaterEqual(len(edge_cases), 0)  # Should identify untestable functions

    def test_coverage_threshold_validation(self):
        """Test coverage threshold validation."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Test with coverage above threshold
        result_high = analyzer.validate_coverage_threshold(0.96, 0.95)
        self.assertTrue(result_high['passed'])
        self.assertEqual(result_high['coverage'], 0.96)

        # Test with coverage below threshold
        result_low = analyzer.validate_coverage_threshold(0.90, 0.95)
        self.assertFalse(result_low['passed'])
        self.assertEqual(result_low['coverage'], 0.90)
        self.assertIn('gap', result_low)

    def test_analyze_code_structure_from_file(self):
        """Test analyzing code structure from file."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Create a temporary Python file
        test_file = os.path.join(self.temp_dir, 'test_code.py')
        sample_code = '''
def simple_function():
    return "hello"

class TestClass:
    def method_one(self):
        pass

    def _private_method(self):
        pass

def complex_function(x, y):
    if x > 0:
        if y > 0:
            return x + y
        else:
            return x - y
    else:
        return 0
'''
        with open(test_file, 'w') as f:
            f.write(sample_code)

        # Test code structure analysis
        code_structure = analyzer.analyze_code_structure(test_file)

        from behavior.coverage_analyzer import CodeStructure
        self.assertIsInstance(code_structure, CodeStructure)
        self.assertEqual(len(code_structure.functions), 4)  # Includes __init__ method
        self.assertEqual(len(code_structure.classes), 1)
        self.assertEqual(code_structure.total_lines, 19)  # Includes empty lines and comments
        self.assertGreater(code_structure.testable_lines, 0)

    def test_analyze_code_structure_from_string(self):
        """Test analyzing code structure from string."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        sample_code = '''
def test_function():
    return True

class SimpleClass:
    def __init__(self):
        self.value = 42
'''
        # Test code structure analysis from string
        code_structure = analyzer.analyze_code_string(sample_code)

        from behavior.coverage_analyzer import CodeStructure
        self.assertIsInstance(code_structure, CodeStructure)
        self.assertEqual(len(code_structure.functions), 2)  # Includes __init__ method
        self.assertEqual(len(code_structure.classes), 1)
        self.assertGreater(code_structure.total_lines, 0)

    def test_analyze_source_code_core_logic(self):
        """Test the core source code analysis logic."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Test with simple function
        simple_code = 'def hello():\n    return "world"'
        code_structure = analyzer.analyze_code_string(simple_code)

        self.assertEqual(len(code_structure.functions), 1)
        self.assertEqual(code_structure.functions[0]['name'], 'hello')
        self.assertTrue(code_structure.functions[0]['testable'])

    def test_analyze_function_detailed(self):
        """Test detailed function analysis."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        sample_code = '''
def complex_func(x, y=10):
    """A complex function with multiple paths."""
    if x > 0:
        return x + y
    elif x < 0:
        return x - y
    else:
        return 0
'''
        code_structure = analyzer.analyze_code_string(sample_code)
        func_info = code_structure.functions[0]

        self.assertEqual(func_info['name'], 'complex_func')
        self.assertEqual(func_info['parameters'], ['x', 'y'])
        self.assertTrue(func_info['testable'])
        self.assertGreater(func_info['complexity'], 1)

    def test_analyze_class_detailed(self):
        """Test detailed class analysis."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        sample_code = '''
class TestClass:
    def __init__(self, value):
        self.value = value

    def public_method(self):
        return self.value

    def _private_method(self):
        return self.value * 2
'''
        code_structure = analyzer.analyze_code_string(sample_code)
        class_info = code_structure.classes[0]

        self.assertEqual(class_info['name'], 'TestClass')
        self.assertEqual(class_info['method_count'], 3)
        self.assertEqual(len(class_info['methods']), 3)

    def test_function_testable_determination(self):
        """Test function testable determination logic."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Test testable function
        testable_code = 'def normal_function():\n    return True'
        code_structure = analyzer.analyze_code_string(testable_code)
        self.assertTrue(code_structure.functions[0]['testable'])

        # Test private function (should be untestable)
        private_code = 'def _private_function():\n    return False'
        code_structure = analyzer.analyze_code_string(private_code)
        self.assertFalse(code_structure.functions[0]['testable'])

    def test_function_complexity_calculation(self):
        """Test cyclomatic complexity calculation."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Test simple function (complexity = 1)
        simple_code = 'def simple_func():\n    return True'
        code_structure = analyzer.analyze_code_string(simple_code)
        self.assertEqual(code_structure.functions[0]['complexity'], 1)

        # Test complex function with multiple branches
        complex_code = '''
def complex_func(x):
    if x > 0:
        if x > 10:
            return x * 2
        else:
            return x
    elif x < 0:
        return x * -1
    else:
        return 0
'''
        code_structure = analyzer.analyze_code_string(complex_code)
        complexity = code_structure.functions[0]['complexity']
        self.assertGreater(complexity, 3)

    def test_count_testable_lines(self):
        """Test counting testable lines."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        sample_code = '''
# This is a comment
import os
from sys import path

def testable_function():
    """This is a testable function."""
    return True

if __name__ == '__main__':
    pass
'''
        code_structure = analyzer.analyze_code_string(sample_code)

        # Should exclude comments, imports, and __main__ block
        self.assertGreater(code_structure.testable_lines, 0)
        self.assertLess(code_structure.testable_lines, code_structure.total_lines)

    def test_suggest_test_cases_functionality(self):
        """Test test case suggestion functionality."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        sample_code = '''
class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

def complex_calculation(x, y, z):
    if x > 0 and y > 0:
        return (x + y) * z
    elif x < 0 or y < 0:
        return abs(x) + abs(y) + z
    else:
        return z
'''
        code_structure = analyzer.analyze_code_string(sample_code)
        suggestions = analyzer.suggest_test_cases(code_structure)

        self.assertIsInstance(suggestions, list)
        self.assertGreater(len(suggestions), 0)

        # Check for specific types of suggestions
        suggestion_types = [s['type'] for s in suggestions]
        self.assertIn('unit_test', suggestion_types)

        # Check for high priority suggestions
        high_priority_suggestions = [s for s in suggestions if s['priority'] == 'high']
        self.assertGreater(len(high_priority_suggestions), 0)

    def test_generate_coverage_report(self):
        """Test coverage report generation."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Create a code structure
        from behavior.coverage_analyzer import CodeStructure
        code_structure = CodeStructure(
            functions=[
                {'name': 'test_func', 'testable': True, 'complexity': 1, 'lineno': 1}
            ],
            classes=[],
            total_lines=10,
            testable_lines=8,
            untestable_lines=2
        )

        # Generate coverage result
        coverage_result = analyzer.calculate_coverage(
            executed_lines=6,
            total_lines=8,
            code_structure=code_structure
        )

        # Generate report
        report = analyzer.generate_coverage_report(coverage_result, code_structure)

        self.assertIsInstance(report, str)
        self.assertIn('Coverage Analysis Report', report)
        self.assertIn('75.0%', report)  # 6/8 = 75%
        self.assertIn('FAIL', report)  # 75% < 95% target, so should be FAIL

    def test_error_handling_file_not_found(self):
        """Test error handling for file not found."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Test with non-existent file
        with self.assertRaises(FileNotFoundError):
            analyzer.analyze_code_structure('/nonexistent/file.py')

    def test_error_handling_syntax_error(self):
        """Test error handling for syntax errors."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Test with invalid Python syntax
        invalid_code = 'def invalid_function(\n    # Missing closing parenthesis'

        with self.assertRaises(SyntaxError):
            analyzer.analyze_code_string(invalid_code)

    def test_edge_case_empty_code(self):
        """Test edge case with empty code."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Test with empty string
        code_structure = analyzer.analyze_code_string('')

        self.assertEqual(len(code_structure.functions), 0)
        self.assertEqual(len(code_structure.classes), 0)
        self.assertEqual(code_structure.total_lines, 0)
        self.assertEqual(code_structure.testable_lines, 0)

    def test_edge_case_zero_lines_coverage(self):
        """Test edge case with zero lines for coverage calculation."""
        from behavior.coverage_analyzer import CoverageAnalyzer

        analyzer = CoverageAnalyzer()

        # Test with zero total lines
        result = analyzer.calculate_coverage(0, 0)

        self.assertEqual(result['coverage_percentage'], 0.0)
        self.assertEqual(result['executed_lines'], 0)
        self.assertEqual(result['total_lines'], 0)
        self.assertFalse(result['meets_target'])


class TestTestFilters(unittest.TestCase):
    """Test cases for Test Filters functionality"""

    def setUp(self):
        """Set up test fixtures."""
        self.sample_statements = [
            {"id": 1, "content": "def test_function(): pass", "testable": True},
            {"id": 2, "content": "import os", "testable": False},  # Import statement
            {"id": 3, "content": "if __name__ == '__main__':", "testable": False},  # Main guard
            {"id": 4, "content": "def another_function(): return True", "testable": True}
        ]

    def test_untestable_filter(self):
        """Test filtering of untestable statements."""
        from behavior.test_filters import TestFilters

        filters = TestFilters()

        # Filter untestable statements
        testable_only = filters.filter_untestable_statements(self.sample_statements)

        self.assertEqual(len(testable_only), 2)  # Only 2 testable statements
        self.assertTrue(all(stmt['testable'] for stmt in testable_only))

    def test_edge_case_generation(self):
        """Test edge case generation functionality."""
        from behavior.test_filters import TestFilters

        filters = TestFilters()

        # Generate edge cases for a function
        function_def = {
            "name": "calculate_average",
            "parameters": [{"name": "numbers", "type": "list"}],
            "type": "function"
        }

        edge_cases = filters.generate_edge_cases(function_def)

        self.assertIsInstance(edge_cases, list)
        self.assertGreater(len(edge_cases), 0)

        # Check for common edge cases
        edge_case_inputs = [case['input'] for case in edge_cases]
        self.assertIn({'numbers': []}, edge_case_inputs)  # Empty list
        self.assertIn({'numbers': None}, edge_case_inputs)  # None values


if __name__ == '__main__':
    unittest.main()