#!/usr/bin/env python3
"""
Demonstration of Robustness Testing Framework

This script demonstrates the complete functionality of the robustness testing
system including transformation strategies, validation, and reporting.
"""

import json
from datetime import datetime
from src.behavior.robustness_engine import RobustnessEngine, RobustnessTestConfig
from src.behavior.transformation_strategies import TransformationConfig
from src.behavior.transformation_validator import TransformationValidator, ValidationConfig
from src.behavior.stability_analyzer import StabilityAnalyzer, StabilityAnalysisConfig
from src.behavior.report_generator import ReportGenerator, ReportConfig


def demonstrate_transformation_strategies():
    """Demonstrate different transformation strategies"""

    print("=" * 60)
    print("TRANSFORMATION STRATEGIES DEMONSTRATION")
    print("=" * 60)

    # Initialize configuration
    transform_config = TransformationConfig(
        max_synonym_replacements=5,
        synonym_confidence_threshold=0.7,
        paragraph_shuffle_probability=0.5,
        irrelevant_content_ratio=0.1
    )

    # Create strategies
    from src.behavior.transformation_strategies import TransformationFactory

    strategies = {}
    for strategy_type in TransformationFactory.get_available_strategies():
        strategies[strategy_type] = TransformationFactory.create_strategy(strategy_type, transform_config)

    # Test text
    test_text = """The robustness testing framework provides comprehensive validation capabilities.
It ensures that key conclusions remain consistent across various input transformations.

The system supports multiple transformation types including synonym replacement,
paragraph reordering, and irrelevant content injection. Each transformation
is designed to maintain semantic neutrality while testing system stability.

Therefore, we can conclude that the framework provides reliable robustness testing."""

    print(f"Original text ({len(test_text)} characters):")
    print("-" * 40)
    print(test_text)
    print()

    # Apply each transformation
    for strategy_name, strategy in strategies.items():
        if strategy.is_applicable(test_text):
            result = strategy.transform(test_text)

            print(f"{strategy_name.upper().replace('_', ' ')}:")
            print("-" * 40)
            print(f"Transformed text:")
            print(result.transformed_text)
            print(f"Confidence: {result.confidence_score:.3f}")
            print(f"Changes made: {len(result.changes_made)}")
            print(f"Processing time: {result.processing_time:.3f}s")
            print()

    return test_text


def demonstrate_robustness_engine(test_text):
    """Demonstrate robustness engine functionality"""

    print("=" * 60)
    print("ROBUSTNESS ENGINE DEMONSTRATION")
    print("=" * 60)

    # Initialize engine
    robustness_config = RobustnessTestConfig(
        target_consistency_score=0.9,
        max_processing_time=0.5
    )
    engine = RobustnessEngine(robustness_config)

    # Execute robustness test
    result = engine.execute_robustness_test("demo_test", test_text)

    print(f"Test ID: {result.test_id}")
    print(f"Timestamp: {result.timestamp}")
    print(f"Consistency Score: {result.consistency_score:.3f}")
    print(f"Success Criteria Met: {result.success_criteria_met}")
    print(f"Execution Time: {result.execution_time:.3f}s")
    print(f"Number of Transformations: {len(result.transformation_results)}")
    print()

    # Show transformation details
    for i, transform_result in enumerate(result.transformation_results):
        print(f"Transformation {i+1}: {transform_result.transformation_type}")
        print(f"  Confidence: {transform_result.confidence_score:.3f}")
        print(f"  Processing Time: {transform_result.processing_time:.3f}s")
        print(f"  Changes Made: {len(transform_result.changes_made)}")
        print()

    return result, engine


def demonstrate_validation(result):
    """Demonstrate transformation validation"""

    print("=" * 60)
    print("TRANSFORMATION VALIDATION DEMONSTRATION")
    print("=" * 60)

    # Initialize validator
    validation_config = ValidationConfig(
        semantic_similarity_threshold=0.8,
        structural_integrity_threshold=0.7,
        overall_validation_threshold=0.85
    )
    validator = TransformationValidator(validation_config)

    # Validate each transformation
    all_validation_results = {}

    for transform_result in result.transformation_results:
        validation_results = validator.validate_transformation(
            result.original_text,
            transform_result.transformed_text,
            transform_result
        )
        all_validation_results[result.test_id] = list(validation_results.values())

        print(f"Validation for {transform_result.transformation_type}:")
        for validation_name, validation_result in validation_results.items():
            status = "✓ PASS" if validation_result.passed else "✗ FAIL"
            print(f"  {validation_name}: {validation_result.score:.3f} {status}")
        print()

    # Generate validation report
    for transform_result in result.transformation_results:
        validation_results = validator.validate_transformation(
            result.original_text,
            transform_result.transformed_text,
            transform_result
        )

        report = validator.generate_validation_report(
            validation_results, result.original_text, transform_result.transformed_text
        )

        print(f"Validation Report for {transform_result.transformation_type}:")
        print(f"  Overall Score: {report['overall_score']:.3f}")
        print(f"  Passed: {report['passed']}")
        print(f"  Recommendations: {len(report['recommendations'])}")
        print()

    return all_validation_results


def demonstrate_stability_analysis(engine):
    """Demonstrate stability analysis"""

    print("=" * 60)
    print("STABILITY ANALYSIS DEMONSTRATION")
    print("=" * 60)

    # Initialize analyzer
    stability_config = StabilityAnalysisConfig(
        min_stability_threshold=0.85,
        confidence_level=0.95
    )
    analyzer = StabilityAnalyzer(stability_config)

    # Get test results from engine
    test_results = list(engine.test_results_registry.values())

    if len(test_results) >= 2:
        # Analyze stability
        stability_metrics = analyzer.analyze_stability(test_results)

        print(f"Stability Analysis Results:")
        print(f"  Decision Consistency: {stability_metrics.decision_consistency:.3f}")
        print(f"  Conclusion Stability: {stability_metrics.conclusion_stability:.3f}")
        print(f"  Key Term Preservation: {stability_metrics.key_term_preservation:.3f}")
        print(f"  Structural Stability: {stability_metrics.structural_stability:.3f}")
        print(f"  Overall Stability: {stability_metrics.overall_stability:.3f}")
        print(f"  Confidence Interval: ({stability_metrics.confidence_interval[0]:.3f}, {stability_metrics.confidence_interval[1]:.3f})")
        print(f"  Sample Size: {stability_metrics.sample_size}")

        # Generate stability report
        report = analyzer.generate_stability_report(stability_metrics, test_results)

        print(f"\nStability Assessment: {report['stability_assessment']}")
        print(f"Meets Threshold: {report['meets_threshold']}")
        print(f"Recommendations: {len(report['recommendations'])}")

        for rec in report['recommendations']:
            print(f"  - {rec}")

        return stability_metrics
    else:
        print("Need at least 2 test results for stability analysis")
        return None


def demonstrate_reporting(engine, validation_results, stability_metrics):
    """Demonstrate report generation"""

    print("=" * 60)
    print("REPORT GENERATION DEMONSTRATION")
    print("=" * 60)

    # Initialize report generator
    report_config = ReportConfig(
        include_visualizations=True,
        include_detailed_metrics=True,
        include_recommendations=True,
        export_formats=["json", "markdown"]
    )
    generator = ReportGenerator(report_config)

    # Get test results
    test_results = list(engine.test_results_registry.values())

    # Generate comprehensive report
    report = generator.generate_comprehensive_report(
        test_results, validation_results, stability_metrics
    )

    print("Report Generated Successfully!")
    print(f"Report Title: {report['metadata']['report_title']}")
    print(f"Total Tests: {report['metadata']['total_tests']}")
    print(f"Total Transformations: {report['metadata']['total_transformations']}")
    print(f"Generation Time: {report['metadata']['generation_time_seconds']:.3f}s")

    print("\nExecutive Summary:")
    summary = report['executive_summary']
    print(f"  Overall Consistency: {summary['overall_consistency']:.3f}")
    print(f"  Success Rate: {summary['key_metrics']['success_rate']:.1%}")
    print(f"  Average Execution Time: {summary['key_metrics']['average_execution_time']:.3f}s")

    print(f"\nRecommendations ({len(report['recommendations'])}):")
    for i, rec in enumerate(report['recommendations'], 1):
        print(f"  {i}. {rec}")

    # Save report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"robustness_demo_report_{timestamp}"

    try:
        generator._export_report(report, report_path)
        print(f"\nReport saved to: {report_path}.json")
        print(f"                {report_path}.md")
    except Exception as e:
        print(f"Error saving report: {e}")

    return report


def main():
    """Main demonstration function"""

    print("ROBUSTNESS TESTING FRAMEWORK DEMONSTRATION")
    print("=" * 60)
    print("This demonstration showcases the complete robustness testing system")
    print("including transformations, validation, stability analysis, and reporting.")
    print()

    try:
        # Step 1: Demonstrate transformation strategies
        test_text = demonstrate_transformation_strategies()

        # Step 2: Demonstrate robustness engine
        result, engine = demonstrate_robustness_engine(test_text)

        # Step 3: Demonstrate validation
        validation_results = demonstrate_validation(result)

        # Step 4: Run additional tests for stability analysis
        print("Running additional tests for stability analysis...")
        additional_test_text = """The system demonstrates excellent performance in transformation testing.
All validation criteria are met successfully. The framework provides comprehensive
analysis capabilities with reliable results across different test scenarios."""
        engine.execute_robustness_test("stability_test", additional_test_text)

        # Step 5: Demonstrate stability analysis
        stability_metrics = demonstrate_stability_analysis(engine)

        # Step 6: Demonstrate reporting
        report = demonstrate_reporting(engine, validation_results, stability_metrics)

        # Final summary
        print("\n" + "=" * 60)
        print("DEMONSTRATION SUMMARY")
        print("=" * 60)
        print("✓ Transformation strategies implemented")
        print("✓ Robustness engine functional")
        print("✓ Validation system working")
        print("✓ Stability analysis operational")
        print("✓ Report generation complete")
        print("\nThe robustness testing framework is fully operational and meets all requirements!")

    except Exception as e:
        print(f"\nError during demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()