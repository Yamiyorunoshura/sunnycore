import ast
import os
import re
from typing import Dict, List, Any, Optional, Tuple
import logging
from dataclasses import dataclass


@dataclass
class CodeStructure:
    """Represents the structure of analyzed code"""
    functions: List[Dict[str, Any]]
    classes: List[Dict[str, Any]]
    total_lines: int
    testable_lines: int
    untestable_lines: int


class CoverageAnalyzer:
    """
    Coverage Analyzer - Strategy Pattern Implementation

    Analyzes code structure and calculates test coverage metrics
    with support for different analysis strategies.
    """

    def __init__(self, coverage_target: float = 0.95):
        """
        Initialize Coverage Analyzer

        Args:
            coverage_target: Target coverage percentage (default: 95%)
        """
        self.coverage_target = coverage_target
        self.logger = logging.getLogger(__name__)

        # Common patterns for untestable code
        self.untestable_patterns = [
            r'if __name__ == [\'"]__main__[\'"]',
            r'import\s+',
            r'from\s+\w+\s+import',
            r'class\s+\w+.*:',
            r'@.*',  # Decorators
            r'pass\s*$',
            r'raise\s+\w+',
            r'return\s+None',
            r'def\s+__.*__:',  # Magic methods
        ]

    def analyze_code_structure(self, file_path: str) -> CodeStructure:
        """
        Analyze code structure from file

        Args:
            file_path: Path to Python file to analyze

        Returns:
            CodeStructure object with analysis results
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source_code = f.read()
        except FileNotFoundError:
            self.logger.error(f"File not found: {file_path}")
            raise

        return self._analyze_source_code(source_code)

    def analyze_code_string(self, source_code: str) -> CodeStructure:
        """
        Analyze code structure from string

        Args:
            source_code: Python source code string

        Returns:
            CodeStructure object with analysis results
        """
        return self._analyze_source_code(source_code)

    def _analyze_source_code(self, source_code: str) -> CodeStructure:
        """
        Analyze Python source code structure

        Args:
            source_code: Python source code

        Returns:
            CodeStructure object
        """
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            self.logger.error(f"Syntax error in source code: {e}")
            raise

        functions = []
        classes = []

        # Analyze functions and classes
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_info = self._analyze_function(node, source_code)
                functions.append(func_info)

            elif isinstance(node, ast.ClassDef):
                class_info = self._analyze_class(node, source_code)
                classes.append(class_info)

        # Calculate line statistics
        total_lines = len(source_code.splitlines())
        testable_lines = self._count_testable_lines(source_code)
        untestable_lines = total_lines - testable_lines

        return CodeStructure(
            functions=functions,
            classes=classes,
            total_lines=total_lines,
            testable_lines=testable_lines,
            untestable_lines=untestable_lines
        )

    def _analyze_function(self, func_node: ast.FunctionDef, source_code: str) -> Dict[str, Any]:
        """
        Analyze individual function

        Args:
            func_node: AST function node
            source_code: Full source code

        Returns:
            Function analysis dictionary
        """
        func_lines = func_node.end_lineno - func_node.lineno + 1
        func_source = ast.get_source_segment(source_code, func_node)

        # Determine if function is testable
        testable = self._is_function_testable(func_node, func_source)

        return {
            'name': func_node.name,
            'lineno': func_node.lineno,
            'end_lineno': func_node.end_lineno,
            'lines': func_lines,
            'testable': testable,
            'source': func_source,
            'parameters': [arg.arg for arg in func_node.args.args],
            'returns': func_node.returns is not None,
            'complexity': self._calculate_function_complexity(func_node)
        }

    def _analyze_class(self, class_node: ast.ClassDef, source_code: str) -> Dict[str, Any]:
        """
        Analyze individual class

        Args:
            class_node: AST class node
            source_code: Full source code

        Returns:
            Class analysis dictionary
        """
        class_lines = class_node.end_lineno - class_node.lineno + 1
        class_source = ast.get_source_segment(source_code, class_node)

        # Analyze methods
        methods = []
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef):
                method_info = self._analyze_function(node, source_code)
                method_info['is_method'] = True
                methods.append(method_info)

        return {
            'name': class_node.name,
            'lineno': class_node.lineno,
            'end_lineno': class_node.end_lineno,
            'lines': class_lines,
            'source': class_source,
            'methods': methods,
            'method_count': len(methods)
        }

    def _is_function_testable(self, func_node: ast.FunctionDef, func_source: str) -> bool:
        """
        Determine if function is testable

        Args:
            func_node: AST function node
            func_source: Function source code

        Returns:
            True if function is testable
        """
        # Check function name patterns
        if func_node.name.startswith('_') and not func_node.name.startswith('__'):
            return False  # Private methods

        # Check for common untestable patterns
        for pattern in self.untestable_patterns:
            if re.search(pattern, func_source, re.MULTILINE):
                return False

        # Check function complexity
        complexity = self._calculate_function_complexity(func_node)
        if complexity > 20:  # Too complex for effective testing
            return False

        return True

    def _calculate_function_complexity(self, func_node: ast.FunctionDef) -> int:
        """
        Calculate cyclomatic complexity of function

        Args:
            func_node: AST function node

        Returns:
            Complexity score
        """
        complexity = 1  # Base complexity

        for node in ast.walk(func_node):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.With):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1

        return complexity

    def _count_testable_lines(self, source_code: str) -> int:
        """
        Count testable lines in source code

        Args:
            source_code: Source code string

        Returns:
            Number of testable lines
        """
        lines = source_code.splitlines()
        testable_count = 0

        for line in lines:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue

            # Check against untestable patterns
            is_testable = True
            for pattern in self.untestable_patterns:
                if re.search(pattern, line):
                    is_testable = False
                    break

            if is_testable:
                testable_count += 1

        return testable_count

    def calculate_coverage(self, executed_lines: int, total_lines: int,
                         code_structure: Optional[CodeStructure] = None) -> Dict[str, Any]:
        """
        Calculate coverage metrics

        Args:
            executed_lines: Number of executed lines
            total_lines: Total lines in code
            code_structure: Optional code structure analysis

        Returns:
            Coverage result dictionary
        """
        if total_lines == 0:
            return {
                'coverage_percentage': 0.0,
                'executed_lines': 0,
                'total_lines': 0,
                'testable_lines': 0,
                'untestable_lines': 0,
                'meets_target': False
            }

        # Use provided structure or calculate default
        if code_structure:
            testable_lines = code_structure.testable_lines
            untestable_lines = code_structure.untestable_lines
        else:
            testable_lines = total_lines  # Assume all lines are testable
            untestable_lines = 0

        # Calculate coverage percentage
        coverage_percentage = (executed_lines / testable_lines) * 100 if testable_lines > 0 else 0.0

        # Determine if target is met
        meets_target = coverage_percentage >= (self.coverage_target * 100)

        return {
            'coverage_percentage': round(coverage_percentage, 2),
            'executed_lines': executed_lines,
            'total_lines': total_lines,
            'testable_lines': testable_lines,
            'untestable_lines': untestable_lines,
            'meets_target': meets_target,
            'target_percentage': self.coverage_target * 100,
            'gap': max(0, (self.coverage_target * 100) - coverage_percentage) if not meets_target else 0
        }

    def validate_coverage_threshold(self, actual_coverage: float,
                                   target_coverage: Optional[float] = None) -> Dict[str, Any]:
        """
        Validate coverage against threshold

        Args:
            actual_coverage: Actual coverage percentage
            target_coverage: Target coverage percentage (uses default if not provided)

        Returns:
            Validation result dictionary
        """
        if target_coverage is None:
            target_coverage = self.coverage_target * 100

        passed = actual_coverage >= target_coverage
        gap = max(0, target_coverage - actual_coverage) if not passed else 0

        return {
            'passed': passed,
            'coverage': actual_coverage,
            'target': target_coverage,
            'gap': gap,
            'status': 'PASS' if passed else 'FAIL'
        }

    def identify_edge_cases(self, code_structure: CodeStructure) -> List[Dict[str, Any]]:
        """
        Identify potential edge cases in code structure

        Args:
            code_structure: Analyzed code structure

        Returns:
            List of edge case dictionaries
        """
        edge_cases = []

        # Analyze functions for edge cases
        for func in code_structure.functions:
            if not func['testable']:
                edge_cases.append({
                    'type': 'untestable_function',
                    'name': func['name'],
                    'location': f"Line {func['lineno']}",
                    'description': f"Function '{func['name']}' is marked as untestable",
                    'severity': 'medium'
                })

            if func['complexity'] > 10:
                edge_cases.append({
                    'type': 'high_complexity',
                    'name': func['name'],
                    'location': f"Line {func['lineno']}",
                    'description': f"Function '{func['name']}' has high complexity ({func['complexity']})",
                    'severity': 'high'
                })

        # Analyze classes for edge cases
        for cls in code_structure.classes:
            if cls['method_count'] == 0:
                edge_cases.append({
                    'type': 'empty_class',
                    'name': cls['name'],
                    'location': f"Line {cls['lineno']}",
                    'description': f"Class '{cls['name']}' has no methods",
                    'severity': 'low'
                })

            # Check for large classes
            if cls['lines'] > 100:
                edge_cases.append({
                    'type': 'large_class',
                    'name': cls['name'],
                    'location': f"Line {cls['lineno']}",
                    'description': f"Class '{cls['name']}' is large ({cls['lines']} lines)",
                    'severity': 'medium'
                })

        # Check overall code metrics
        if code_structure.untestable_lines > code_structure.testable_lines * 0.3:
            edge_cases.append({
                'type': 'high_untestable_ratio',
                'name': 'codebase',
                'location': 'overall',
                'description': f"High ratio of untestable code ({code_structure.untestable_lines} lines)",
                'severity': 'high'
            })

        return edge_cases

    def suggest_test_cases(self, code_structure: CodeStructure) -> List[Dict[str, Any]]:
        """
        Suggest test cases based on code structure

        Args:
            code_structure: Analyzed code structure

        Returns:
            List of suggested test case dictionaries
        """
        suggestions = []

        # Suggest tests for testable functions
        for func in code_structure.functions:
            if func['testable']:
                suggestions.extend(self._suggest_function_tests(func))

        # Suggest tests for classes
        for cls in code_structure.classes:
            suggestions.extend(self._suggest_class_tests(cls))

        return suggestions

    def _suggest_function_tests(self, func: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Suggest test cases for a function

        Args:
            func: Function analysis dictionary

        Returns:
            List of test case suggestions
        """
        suggestions = []

        # Basic functionality test
        suggestions.append({
            'type': 'unit_test',
            'target': func['name'],
            'description': f"Test basic functionality of {func['name']}",
            'priority': 'high'
        })

        # Edge case tests based on parameters
        if func['parameters']:
            suggestions.append({
                'type': 'edge_case',
                'target': func['name'],
                'description': f"Test {func['name']} with edge case parameter values",
                'priority': 'medium'
            })

        # Error handling tests
        if func['complexity'] > 5:
            suggestions.append({
                'type': 'error_handling',
                'target': func['name'],
                'description': f"Test error handling in {func['name']}",
                'priority': 'medium'
            })

        return suggestions

    def _suggest_class_tests(self, cls: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Suggest test cases for a class

        Args:
            cls: Class analysis dictionary

        Returns:
            List of test case suggestions
        """
        suggestions = []

        # Basic instantiation test
        suggestions.append({
            'type': 'unit_test',
            'target': cls['name'],
            'description': f"Test instantiation of {cls['name']}",
            'priority': 'high'
        })

        # Method tests
        for method in cls['methods']:
            if method['testable']:
                suggestions.append({
                    'type': 'unit_test',
                    'target': f"{cls['name']}.{method['name']}",
                    'description': f"Test {cls['name']}.{method['name']} method",
                    'priority': 'high'
                })

        return suggestions

    def generate_coverage_report(self, coverage_result: Dict[str, Any],
                              code_structure: CodeStructure) -> str:
        """
        Generate human-readable coverage report

        Args:
            coverage_result: Coverage calculation result
            code_structure: Code structure analysis

        Returns:
            Formatted coverage report string
        """
        report = []
        report.append("=== Coverage Analysis Report ===")
        report.append(f"Total Lines: {coverage_result['total_lines']}")
        report.append(f"Testable Lines: {coverage_result['testable_lines']}")
        report.append(f"Untestable Lines: {coverage_result['untestable_lines']}")
        report.append(f"Coverage: {coverage_result['coverage_percentage']}%")
        report.append(f"Target: {coverage_result['target_percentage']}%")
        report.append(f"Status: {'PASS' if coverage_result['meets_target'] else 'FAIL'}")

        if not coverage_result['meets_target']:
            report.append(f"Gap: {coverage_result['gap']}%")

        report.append("\n=== Code Structure ===")
        report.append(f"Functions: {len(code_structure.functions)}")
        report.append(f"Classes: {len(code_structure.classes)}")

        # Add edge cases if any
        edge_cases = self.identify_edge_cases(code_structure)
        if edge_cases:
            report.append("\n=== Edge Cases Identified ===")
            for case in edge_cases:
                report.append(f"- {case['description']} ({case['severity']})")

        return "\n".join(report)