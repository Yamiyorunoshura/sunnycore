import json
import ast
from typing import Dict, List, Any, Optional, Union, Tuple, Set
from datetime import datetime, timezone
import logging
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of architecture validation"""
    component_id: str
    validation_type: str
    passed: bool
    score: float
    issues: List[str]
    recommendations: List[str]


class ArchitectureValidator:
    """
    Architecture Alignment Validator - Strategy Pattern Implementation

    Validates system architecture alignment using F1 score metrics and
    comprehensive architecture analysis.
    """

    def __init__(self, target_f1_score: float = 0.9):
        """
        Initialize Architecture Validator

        Args:
            target_f1_score: Target F1 score (default: 0.9)
        """
        self.target_f1_score = target_f1_score
        self.logger = logging.getLogger(__name__)

        # Architecture components registry
        self.component_registry = {}
        self.dependency_graph = {}

    def load_architecture_spec(self, spec_path: str) -> Dict[str, Any]:
        """
        Load architecture specification from file

        Args:
            spec_path: Path to architecture specification file

        Returns:
            Architecture specification dictionary
        """
        try:
            with open(spec_path, 'r') as f:
                if spec_path.endswith('.json'):
                    spec = json.load(f)
                else:
                    # Assume YAML format
                    import yaml
                    spec = yaml.safe_load(f)

            self._process_architecture_spec(spec)
            return spec

        except Exception as e:
            self.logger.error(f"Failed to load architecture spec: {e}")
            raise

    def _process_architecture_spec(self, spec: Dict[str, Any]):
        """
        Process architecture specification and build internal structures

        Args:
            spec: Architecture specification
        """
        # Build component registry
        components = spec.get('components', [])
        for component in components:
            component_id = component.get('id')
            if component_id:
                self.component_registry[component_id] = component

        # Build dependency graph
        data_flows = spec.get('data_flows', [])
        for flow in data_flows:
            source = flow.get('source')
            target = flow.get('target')

            if source and target:
                if source not in self.dependency_graph:
                    self.dependency_graph[source] = []
                self.dependency_graph[source].append(target)

    def validate_architecture_alignment(self, actual_implementation: Dict[str, Any],
                                      expected_architecture: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate architecture alignment between implementation and specification

        Args:
            actual_implementation: Actual implementation structure
            expected_architecture: Expected architecture specification

        Returns:
            Validation results with F1 score
        """
        try:
            # Extract components from both sides
            expected_components = self._extract_components(expected_architecture)
            actual_components = self._extract_components(actual_implementation)

            # Calculate F1 score
            f1_results = self._calculate_component_f1_score(
                expected_components, actual_components
            )

            # Validate component dependencies
            dependency_results = self._validate_dependencies(
                expected_architecture, actual_implementation
            )

            # Validate interfaces
            interface_results = self._validate_interfaces(
                expected_architecture, actual_implementation
            )

            # Calculate overall alignment score
            overall_score = self._calculate_overall_alignment_score(
                f1_results, dependency_results, interface_results
            )

            return {
                'f1_score': f1_results,
                'dependency_validation': dependency_results,
                'interface_validation': interface_results,
                'overall_alignment_score': overall_score,
                'meets_target': overall_score >= self.target_f1_score,
                'validation_timestamp': datetime.now(timezone.utc).isoformat()
            }

        except Exception as e:
            self.logger.error(f"Failed to validate architecture alignment: {e}")
            return {
                'error': str(e),
                'f1_score': {'f1_score': 0.0, 'meets_target': False},
                'overall_alignment_score': 0.0,
                'meets_target': False
            }

    def _extract_components(self, architecture: Dict[str, Any]) -> Set[str]:
        """
        Extract component IDs from architecture

        Args:
            architecture: Architecture specification

        Returns:
            Set of component IDs
        """
        components = set()

        # Extract from components section
        for component in architecture.get('components', []):
            component_id = component.get('id')
            if component_id:
                components.add(component_id)

        # Extract from data flows
        for flow in architecture.get('data_flows', []):
            source = flow.get('source')
            target = flow.get('target')
            if source:
                components.add(source)
            if target:
                components.add(target)

        # Extract from interfaces
        for interface in architecture.get('interfaces', []):
            interface_id = interface.get('id')
            if interface_id:
                components.add(interface_id)

        return components

    def _calculate_component_f1_score(self, expected_components: Set[str],
                                    actual_components: Set[str]) -> Dict[str, Any]:
        """
        Calculate F1 score for component alignment

        Args:
            expected_components: Set of expected component IDs
            actual_components: Set of actual component IDs

        Returns:
            F1 score calculation results
        """
        # Calculate true positives, false positives, false negatives
        true_positives = expected_components.intersection(actual_components)
        false_positives = actual_components - expected_components
        false_negatives = expected_components - actual_components

        tp_count = len(true_positives)
        fp_count = len(false_positives)
        fn_count = len(false_negatives)

        # Calculate precision, recall, F1
        precision = tp_count / (tp_count + fp_count) if (tp_count + fp_count) > 0 else 0.0
        recall = tp_count / (tp_count + fn_count) if (tp_count + fn_count) > 0 else 0.0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

        return {
            'f1_score': round(f1_score, 3),
            'precision': round(precision, 3),
            'recall': round(recall, 3),
            'true_positives': tp_count,
            'false_positives': fp_count,
            'false_negatives': fn_count,
            'true_positive_components': list(true_positives),
            'false_positive_components': list(false_positives),
            'false_negative_components': list(false_negatives),
            'meets_target': f1_score >= self.target_f1_score
        }

    def _validate_dependencies(self, expected_architecture: Dict[str, Any],
                            actual_implementation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate component dependencies

        Args:
            expected_architecture: Expected architecture
            actual_implementation: Actual implementation

        Returns:
            Dependency validation results
        """
        results = {
            'total_dependencies': 0,
            'valid_dependencies': 0,
            'invalid_dependencies': 0,
            'missing_dependencies': 0,
            'dependency_details': []
        }

        expected_flows = expected_architecture.get('data_flows', [])
        results['total_dependencies'] = len(expected_flows)

        for flow in expected_flows:
            source = flow.get('source')
            target = flow.get('target')
            flow_id = f"{source}->{target}"

            dependency_result = {
                'flow_id': flow_id,
                'source': source,
                'target': target,
                'valid': False,
                'issues': []
            }

            # Check if dependency exists in implementation
            if self._dependency_exists_in_implementation(source, target, actual_implementation):
                dependency_result['valid'] = True
                results['valid_dependencies'] += 1
            else:
                dependency_result['valid'] = False
                dependency_result['issues'].append('Dependency not found in implementation')
                results['invalid_dependencies'] += 1

            results['dependency_details'].append(dependency_result)

        return results

    def _dependency_exists_in_implementation(self, source: str, target: str,
                                          implementation: Dict[str, Any]) -> bool:
        """
        Check if dependency exists in implementation

        Args:
            source: Source component
            target: Target component
            implementation: Implementation structure

        Returns:
            True if dependency exists
        """
        # This is a simplified check
        # In practice, this would involve code analysis or runtime inspection
        actual_flows = implementation.get('data_flows', [])

        for flow in actual_flows:
            if (flow.get('source') == source and flow.get('target') == target):
                return True

        return False

    def _validate_interfaces(self, expected_architecture: Dict[str, Any],
                           actual_implementation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate interface compliance

        Args:
            expected_architecture: Expected architecture
            actual_implementation: Actual implementation

        Returns:
            Interface validation results
        """
        results = {
            'total_interfaces': 0,
            'compliant_interfaces': 0,
            'non_compliant_interfaces': 0,
            'missing_interfaces': 0,
            'interface_details': []
        }

        expected_interfaces = expected_architecture.get('interfaces', [])
        results['total_interfaces'] = len(expected_interfaces)

        for expected_interface in expected_interfaces:
            interface_id = expected_interface.get('id')
            interface_result = {
                'interface_id': interface_id,
                'compliant': False,
                'issues': []
            }

            # Find corresponding interface in implementation
            actual_interface = self._find_interface_in_implementation(interface_id, actual_implementation)

            if actual_interface:
                # Validate interface methods
                method_issues = self._validate_interface_methods(expected_interface, actual_interface)
                if method_issues:
                    interface_result['issues'].extend(method_issues)
                    results['non_compliant_interfaces'] += 1
                else:
                    interface_result['compliant'] = True
                    results['compliant_interfaces'] += 1
            else:
                interface_result['issues'].append('Interface not found in implementation')
                results['missing_interfaces'] += 1

            results['interface_details'].append(interface_result)

        return results

    def _find_interface_in_implementation(self, interface_id: str,
                                       implementation: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Find interface in implementation

        Args:
            interface_id: Interface ID to find
            implementation: Implementation structure

        Returns:
            Interface dictionary or None
        """
        actual_interfaces = implementation.get('interfaces', [])

        for interface in actual_interfaces:
            if interface.get('id') == interface_id:
                return interface

        return None

    def _validate_interface_methods(self, expected_interface: Dict[str, Any],
                                 actual_interface: Dict[str, Any]) -> List[str]:
        """
        Validate interface methods

        Args:
            expected_interface: Expected interface specification
            actual_interface: Actual interface implementation

        Returns:
            List of validation issues
        """
        issues = []

        expected_methods = expected_interface.get('methods', [])
        actual_methods = actual_interface.get('methods', [])

        expected_method_names = {method.get('name') for method in expected_methods}
        actual_method_names = {method.get('name') for method in actual_methods}

        # Check for missing methods
        missing_methods = expected_method_names - actual_method_names
        if missing_methods:
            issues.append(f"Missing methods: {', '.join(missing_methods)}")

        # Check method signatures
        for expected_method in expected_methods:
            method_name = expected_method.get('name')
            if method_name in actual_method_names:
                # Find corresponding actual method
                actual_method = next(
                    (m for m in actual_methods if m.get('name') == method_name),
                    None
                )

                if actual_method:
                    signature_issues = self._validate_method_signature(expected_method, actual_method)
                    issues.extend(signature_issues)

        return issues

    def _validate_method_signature(self, expected_method: Dict[str, Any],
                                 actual_method: Dict[str, Any]) -> List[str]:
        """
        Validate method signature

        Args:
            expected_method: Expected method specification
            actual_method: Actual method implementation

        Returns:
            List of signature issues
        """
        issues = []

        # Check parameters
        expected_params = expected_method.get('parameters', [])
        actual_params = actual_method.get('parameters', [])

        expected_param_names = {param.get('name') for param in expected_params}
        actual_param_names = {param.get('name') for param in actual_params}

        missing_params = expected_param_names - actual_param_names
        if missing_params:
            issues.append(f"Missing parameters: {', '.join(missing_params)}")

        # Check return type
        expected_return = expected_method.get('return_type')
        actual_return = actual_method.get('return_type')

        if expected_return and actual_return and expected_return != actual_return:
            issues.append(f"Return type mismatch: expected {expected_return}, got {actual_return}")

        return issues

    def _calculate_overall_alignment_score(self, f1_results: Dict[str, Any],
                                          dependency_results: Dict[str, Any],
                                          interface_results: Dict[str, Any]) -> float:
        """
        Calculate overall architecture alignment score

        Args:
            f1_results: F1 score results
            dependency_results: Dependency validation results
            interface_results: Interface validation results

        Returns:
            Overall alignment score (0-1)
        """
        # Weight factors
        f1_weight = 0.5
        dependency_weight = 0.3
        interface_weight = 0.2

        # Calculate individual scores
        f1_score = f1_results.get('f1_score', 0.0)

        total_deps = dependency_results.get('total_dependencies', 1)
        valid_deps = dependency_results.get('valid_dependencies', 0)
        dependency_score = valid_deps / total_deps if total_deps > 0 else 0.0

        total_interfaces = interface_results.get('total_interfaces', 1)
        compliant_interfaces = interface_results.get('compliant_interfaces', 0)
        interface_score = compliant_interfaces / total_interfaces if total_interfaces > 0 else 0.0

        # Calculate weighted average
        overall_score = (
            f1_score * f1_weight +
            dependency_score * dependency_weight +
            interface_score * interface_weight
        )

        return round(overall_score, 3)

    def generate_architecture_report(self, validation_results: Dict[str, Any]) -> str:
        """
        Generate human-readable architecture validation report

        Args:
            validation_results: Validation results

        Returns:
            Formatted report string
        """
        report = []
        report.append("=== Architecture Validation Report ===")
        report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
        report.append("")

        # Overall results
        overall_score = validation_results.get('overall_alignment_score', 0.0)
        meets_target = validation_results.get('meets_target', False)
        target_score = self.target_f1_score

        report.append(f"Overall Alignment Score: {overall_score:.3f}")
        report.append(f"Target Score: {target_score:.3f}")
        report.append(f"Status: {'✓ PASS' if meets_target else '✗ FAIL'}")
        report.append("")

        # F1 Score details
        f1_results = validation_results.get('f1_score', {})
        if f1_results:
            report.append("## F1 Score Analysis")
            f1_score = f1_results.get('f1_score', 0.0)
            precision = f1_results.get('precision', 0.0)
            recall = f1_results.get('recall', 0.0)

            report.append(f"F1 Score: {f1_score:.3f}")
            report.append(f"Precision: {precision:.3f}")
            report.append(f"Recall: {recall:.3f}")
            report.append("")

            # Component details
            tp_components = f1_results.get('true_positive_components', [])
            fp_components = f1_results.get('false_positive_components', [])
            fn_components = f1_results.get('false_negative_components', [])

            if tp_components:
                report.append("✓ Correctly Identified Components:")
                for comp in tp_components:
                    report.append(f"  - {comp}")
                report.append("")

            if fp_components:
                report.append("✗ False Positive Components:")
                for comp in fp_components:
                    report.append(f"  - {comp}")
                report.append("")

            if fn_components:
                report.append("✗ Missing Components:")
                for comp in fn_components:
                    report.append(f"  - {comp}")
                report.append("")

        # Dependency validation
        dependency_results = validation_results.get('dependency_validation', {})
        if dependency_results:
            report.append("## Dependency Validation")
            total_deps = dependency_results.get('total_dependencies', 0)
            valid_deps = dependency_results.get('valid_dependencies', 0)
            invalid_deps = dependency_results.get('invalid_dependencies', 0)

            report.append(f"Total Dependencies: {total_deps}")
            report.append(f"Valid Dependencies: {valid_deps}")
            report.append(f"Invalid Dependencies: {invalid_deps}")
            report.append("")

        # Interface validation
        interface_results = validation_results.get('interface_validation', {})
        if interface_results:
            report.append("## Interface Validation")
            total_interfaces = interface_results.get('total_interfaces', 0)
            compliant_interfaces = interface_results.get('compliant_interfaces', 0)
            non_compliant_interfaces = interface_results.get('non_compliant_interfaces', 0)

            report.append(f"Total Interfaces: {total_interfaces}")
            report.append(f"Compliant Interfaces: {compliant_interfaces}")
            report.append(f"Non-compliant Interfaces: {non_compliant_interfaces}")
            report.append("")

        # Recommendations
        report.append("## Recommendations")
        if not meets_target:
            report.append("- Architecture alignment below target. Review component mapping.")
        if f1_results.get('precision', 1.0) < 0.8:
            report.append("- Low precision indicates false positives. Review component identification.")
        if f1_results.get('recall', 1.0) < 0.8:
            report.append("- Low recall indicates missing components. Expand test coverage.")
        if meets_target:
            report.append("- Architecture alignment meets targets. Maintain current standards.")

        return "\n".join(report)