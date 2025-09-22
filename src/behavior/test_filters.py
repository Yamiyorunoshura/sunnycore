import ast
import re
from typing import Dict, List, Any, Optional, Tuple, Union
import logging
from dataclasses import dataclass


@dataclass
class FilterResult:
    """Result of filtering operation"""
    filtered_items: List[Dict[str, Any]]
    removed_items: List[Dict[str, Any]]
    filter_reason: str
    total_count: int
    filtered_count: int


class TestFilters:
    """
    Test Filters - Strategy Pattern Implementation

    Provides filtering and analysis capabilities for test cases,
    including untestable statement detection and edge case generation.
    """

    def __init__(self):
        """Initialize Test Filters"""
        self.logger = logging.getLogger(__name__)

        # Patterns for untestable statements
        self.untestable_patterns = {
            'imports': [
                r'^\s*import\s+\w+(?:\s+as\s+\w+)?$',
                r'^\s*from\s+\w+\s+import\s+(?:\w+|\*)$',
                r'^\s*from\s+\w+\s+import\s+\w+\s+as\s+\w+$'
            ],
            'main_guards': [
                r'^\s*if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:',
            ],
            'declarations': [
                r'^\s*class\s+\w+',
                r'^\s*@\w+.*',  # Decorators
            ],
            'simple_statements': [
                r'^\s*pass\s*$',
                r'^\s*raise\s+\w+',
                r'^\s*return\s+None',
                r'^\s*return\s*$',
            ],
            'magic_methods': [
                r'^\s*def\s+__\w+__\s*\(',
            ],
            'type_hints': [
                r'^\s*from\s+typing\s+import',
                r'^\s*:\s*\w+.*?=',  # Type hints in assignments
            ]
        }

        # Edge case generation patterns
        self.edge_case_strategies = {
            'boundary_values': self._generate_boundary_values,
            'null_handling': self._generate_null_cases,
            'empty_collections': self._generate_empty_collections,
            'extreme_values': self._generate_extreme_values,
            'invalid_inputs': self._generate_invalid_inputs,
            'special_characters': self._generate_special_characters
        }

    def filter_untestable_statements(self, statements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filter out untestable statements from a list

        Args:
            statements: List of statement dictionaries

        Returns:
            List of testable statements only
        """
        testable_statements = []
        removed_statements = []

        for statement in statements:
            if self._is_statement_testable(statement):
                testable_statements.append(statement)
            else:
                removed_statements.append(statement)

        self.logger.info(f"Filtered {len(removed_statements)} untestable statements")
        return testable_statements

    def _is_statement_testable(self, statement: Dict[str, Any]) -> bool:
        """
        Determine if a statement is testable

        Args:
            statement: Statement dictionary

        Returns:
            True if statement is testable
        """
        content = statement.get('content', '')
        statement_type = statement.get('type', 'unknown')

        # Check against untestable patterns
        for category, patterns in self.untestable_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                    self.logger.debug(f"Statement matches untestable pattern '{category}': {content[:50]}...")
                    return False

        # Additional logic-based checks
        if statement_type == 'function':
            return self._is_function_testable(content)
        elif statement_type == 'class':
            return self._is_class_testable(content)

        return True

    def _is_function_testable(self, func_content: str) -> bool:
        """
        Determine if a function is testable

        Args:
            func_content: Function source code

        Returns:
            True if function is testable
        """
        try:
            tree = ast.parse(func_content)
        except SyntaxError:
            return False

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Check for private functions
                if node.name.startswith('_') and not node.name.startswith('__'):
                    return False

                # Check for magic methods
                if node.name.startswith('__') and node.name.endswith('__'):
                    return False

                # Check for functions that only contain pass or raise
                if self._is_empty_function(node):
                    return False

                return True

        return False

    def _is_class_testable(self, class_content: str) -> bool:
        """
        Determine if a class is testable

        Args:
            class_content: Class source code

        Returns:
            True if class is testable
        """
        try:
            tree = ast.parse(class_content)
        except SyntaxError:
            return False

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Check if class has any testable methods
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        if self._is_function_testable(ast.get_source_segment(class_content, item)):
                            return True

                return False

        return False

    def _is_empty_function(self, func_node: ast.FunctionDef) -> bool:
        """
        Check if function is empty (only contains pass or raise)

        Args:
            func_node: AST function node

        Returns:
            True if function is empty
        """
        if not func_node.body:
            return True

        for stmt in func_node.body:
            if isinstance(stmt, ast.Pass):
                return True
            elif isinstance(stmt, ast.Raise) and not stmt.exc:
                return True

        return False

    def generate_edge_cases(self, function_def: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate edge cases for a function

        Args:
            function_def: Function definition dictionary

        Returns:
            List of edge case test scenarios
        """
        edge_cases = []

        parameters = function_def.get('parameters', [])
        return_type = function_def.get('returns', None)

        for param in parameters:
            param_name = param.get('name', 'unknown')
            param_type = param.get('type', 'any')

            # Apply all edge case generation strategies
            for strategy_name, strategy_func in self.edge_case_strategies.items():
                cases = strategy_func(param_name, param_type)
                edge_cases.extend(cases)

        return edge_cases

    def _generate_boundary_values(self, param_name: str, param_type: str) -> List[Dict[str, Any]]:
        """Generate boundary value test cases"""
        cases = []

        if param_type in ['int', 'integer']:
            cases.extend([
                {
                    'name': f'{param_name}_min_int',
                    'description': f'Test {param_name} with minimum integer value',
                    'input': {param_name: -2147483648},
                    'category': 'boundary',
                    'expected_behavior': 'should handle minimum value'
                },
                {
                    'name': f'{param_name}_max_int',
                    'description': f'Test {param_name} with maximum integer value',
                    'input': {param_name: 2147483647},
                    'category': 'boundary',
                    'expected_behavior': 'should handle maximum value'
                },
                {
                    'name': f'{param_name}_zero',
                    'description': f'Test {param_name} with zero',
                    'input': {param_name: 0},
                    'category': 'boundary',
                    'expected_behavior': 'should handle zero'
                }
            ])
        elif param_type in ['float', 'number']:
            cases.extend([
                {
                    'name': f'{param_name}_min_float',
                    'description': f'Test {param_name} with minimum float value',
                    'input': {param_name: -1.7976931348623157e+308},
                    'category': 'boundary',
                    'expected_behavior': 'should handle minimum float'
                },
                {
                    'name': f'{param_name}_max_float',
                    'description': f'Test {param_name} with maximum float value',
                    'input': {param_name: 1.7976931348623157e+308},
                    'category': 'boundary',
                    'expected_behavior': 'should handle maximum float'
                }
            ])
        elif param_type in ['str', 'string']:
            cases.extend([
                {
                    'name': f'{param_name}_empty_string',
                    'description': f'Test {param_name} with empty string',
                    'input': {param_name: ''},
                    'category': 'boundary',
                    'expected_behavior': 'should handle empty string'
                },
                {
                    'name': f'{param_name}_very_long_string',
                    'description': f'Test {param_name} with very long string',
                    'input': {param_name: 'a' * 10000},
                    'category': 'boundary',
                    'expected_behavior': 'should handle long string'
                }
            ])

        return cases

    def _generate_null_cases(self, param_name: str, param_type: str) -> List[Dict[str, Any]]:
        """Generate null/None test cases"""
        return [
            {
                'name': f'{param_name}_null',
                'description': f'Test {param_name} with None value',
                'input': {param_name: None},
                'category': 'null_handling',
                'expected_behavior': 'should handle None gracefully'
            }
        ]

    def _generate_empty_collections(self, param_name: str, param_type: str) -> List[Dict[str, Any]]:
        """Generate empty collection test cases"""
        cases = []

        if param_type in ['list', 'array']:
            cases.append({
                'name': f'{param_name}_empty_list',
                'description': f'Test {param_name} with empty list',
                'input': {param_name: []},
                'category': 'empty_collection',
                'expected_behavior': 'should handle empty list'
            })
        elif param_type in ['dict', 'map']:
            cases.append({
                'name': f'{param_name}_empty_dict',
                'description': f'Test {param_name} with empty dictionary',
                'input': {param_name: {}},
                'category': 'empty_collection',
                'expected_behavior': 'should handle empty dict'
            })
        elif param_type in ['set']:
            cases.append({
                'name': f'{param_name}_empty_set',
                'description': f'Test {param_name} with empty set',
                'input': {param_name: set()},
                'category': 'empty_collection',
                'expected_behavior': 'should handle empty set'
            })

        return cases

    def _generate_extreme_values(self, param_name: str, param_type: str) -> List[Dict[str, Any]]:
        """Generate extreme value test cases"""
        cases = []

        if param_type in ['int', 'float', 'number']:
            cases.extend([
                {
                    'name': f'{param_name}_negative_extreme',
                    'description': f'Test {param_name} with large negative value',
                    'input': {param_name: -999999},
                    'category': 'extreme_value',
                    'expected_behavior': 'should handle extreme negative value'
                },
                {
                    'name': f'{param_name}_positive_extreme',
                    'description': f'Test {param_name} with large positive value',
                    'input': {param_name: 999999},
                    'category': 'extreme_value',
                    'expected_behavior': 'should handle extreme positive value'
                }
            ])

        return cases

    def _generate_invalid_inputs(self, param_name: str, param_type: str) -> List[Dict[str, Any]]:
        """Generate invalid input test cases"""
        cases = []

        if param_type in ['int', 'float', 'number']:
            cases.extend([
                {
                    'name': f'{param_name}_string_input',
                    'description': f'Test {param_name} with string input',
                    'input': {param_name: 'invalid_number'},
                    'category': 'invalid_input',
                    'expected_behavior': 'should handle type error'
                },
                {
                    'name': f'{param_name}_nan',
                    'description': f'Test {param_name} with NaN value',
                    'input': {param_name: float('nan')},
                    'category': 'invalid_input',
                    'expected_behavior': 'should handle NaN'
                }
            ])

        return cases

    def _generate_special_characters(self, param_name: str, param_type: str) -> List[Dict[str, Any]]:
        """Generate special character test cases"""
        cases = []

        if param_type in ['str', 'string']:
            cases.extend([
                {
                    'name': f'{param_name}_unicode_chars',
                    'description': f'Test {param_name} with Unicode characters',
                    'input': {param_name: 'Hello 世界 🌍'},
                    'category': 'special_characters',
                    'expected_behavior': 'should handle Unicode'
                },
                {
                    'name': f'{param_name}_escape_chars',
                    'description': f'Test {param_name} with escape characters',
                    'input': {param_name: 'Hello\\nWorld\\tTest'},
                    'category': 'special_characters',
                    'expected_behavior': 'should handle escape chars'
                },
                {
                    'name': f'{param_name}_html_tags',
                    'description': f'Test {param_name} with HTML tags',
                    'input': {param_name: '<script>alert("test")</script>'},
                    'category': 'special_characters',
                    'expected_behavior': 'should handle HTML tags'
                }
            ])

        return cases

    def analyze_test_complexity(self, test_cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze complexity of test cases

        Args:
            test_cases: List of test case dictionaries

        Returns:
            Complexity analysis result
        """
        complexity_scores = []
        categories = {}

        for test_case in test_cases:
            # Calculate individual test case complexity
            score = self._calculate_test_complexity(test_case)
            complexity_scores.append(score)

            # Categorize tests
            category = test_case.get('category', 'unknown')
            if category not in categories:
                categories[category] = []
            categories[category].append(score)

        # Calculate overall metrics
        avg_complexity = sum(complexity_scores) / len(complexity_scores) if complexity_scores else 0
        max_complexity = max(complexity_scores) if complexity_scores else 0

        return {
            'total_tests': len(test_cases),
            'average_complexity': round(avg_complexity, 2),
            'max_complexity': max_complexity,
            'complexity_scores': complexity_scores,
            'categories': categories,
            'complexity_level': self._determine_complexity_level(avg_complexity)
        }

    def _calculate_test_complexity(self, test_case: Dict[str, Any]) -> float:
        """
        Calculate complexity score for a single test case

        Args:
            test_case: Test case dictionary

        Returns:
            Complexity score (0-10)
        """
        score = 0.0

        # Base complexity from test steps
        steps = test_case.get('steps', [])
        score += len(steps) * 0.5

        # Complexity from input parameters
        inputs = test_case.get('input', {})
        score += len(inputs) * 0.3

        # Complexity from assertions
        assertions = test_case.get('assertions', [])
        score += len(assertions) * 0.7

        # Category-based complexity multipliers
        category = test_case.get('category', 'unit')
        category_multipliers = {
            'unit': 1.0,
            'integration': 1.5,
            'edge_case': 1.3,
            'error_handling': 1.4,
            'performance': 1.2
        }
        score *= category_multipliers.get(category, 1.0)

        # Cap the score at 10
        return min(score, 10.0)

    def _determine_complexity_level(self, avg_complexity: float) -> str:
        """
        Determine complexity level based on average complexity

        Args:
            avg_complexity: Average complexity score

        Returns:
            Complexity level string
        """
        if avg_complexity < 2.0:
            return 'low'
        elif avg_complexity < 5.0:
            return 'medium'
        elif avg_complexity < 8.0:
            return 'high'
        else:
            return 'very_high'

    def filter_by_priority(self, test_cases: List[Dict[str, Any]],
                          min_priority: str = 'low') -> List[Dict[str, Any]]:
        """
        Filter test cases by priority level

        Args:
            test_cases: List of test case dictionaries
            min_priority: Minimum priority level ('low', 'medium', 'high', 'critical')

        Returns:
            Filtered list of test cases
        """
        priority_levels = {'low': 0, 'medium': 1, 'high': 2, 'critical': 3}
        min_level = priority_levels.get(min_priority, 0)

        filtered_cases = []
        for test_case in test_cases:
            priority = test_case.get('priority', 'low')
            if priority_levels.get(priority, 0) >= min_level:
                filtered_cases.append(test_case)

        return filtered_cases

    def suggest_test_improvements(self, test_cases: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Suggest improvements for existing test cases

        Args:
            test_cases: List of test case dictionaries

        Returns:
            List of improvement suggestions
        """
        suggestions = []

        for test_case in test_cases:
            case_suggestions = []

            # Check for missing assertions
            assertions = test_case.get('assertions', [])
            if len(assertions) < 2:
                case_suggestions.append({
                    'type': 'add_assertions',
                    'description': 'Add more assertions to increase test coverage',
                    'priority': 'medium'
                })

            # Check for edge case coverage
            category = test_case.get('category', 'unit')
            if category == 'unit':
                case_suggestions.append({
                    'type': 'add_edge_cases',
                    'description': 'Consider adding edge case tests',
                    'priority': 'low'
                })

            # Check for error handling
            has_error_handling = any('error' in assert_type.lower() for assert_type in assertions)
            if not has_error_handling:
                case_suggestions.append({
                    'type': 'add_error_handling',
                    'description': 'Add error handling tests',
                    'priority': 'medium'
                })

            if case_suggestions:
                suggestions.append({
                    'test_case': test_case.get('name', 'unknown'),
                    'suggestions': case_suggestions
                })

        return suggestions