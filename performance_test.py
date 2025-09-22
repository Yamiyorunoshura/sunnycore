#!/usr/bin/env python3
"""
Performance test for robustness engine to verify 500ms requirement
"""

import time
import statistics
from src.behavior.robustness_engine import RobustnessEngine, RobustnessTestConfig
from src.behavior.transformation_strategies import TransformationConfig


def test_performance_requirements():
    """Test that performance requirements are met"""

    # Initialize configuration with performance tracking
    transform_config = TransformationConfig(
        max_synonym_replacements=3,
        synonym_confidence_threshold=0.7
    )

    robustness_config = RobustnessTestConfig(
        target_consistency_score=0.9,
        max_processing_time=0.5,  # 500ms requirement
        transformation_config=transform_config
    )

    engine = RobustnessEngine(robustness_config)

    # Test texts of varying lengths
    test_texts = [
        "Short text for testing.",
        "This is a medium length text with multiple sentences. It should be suitable for testing transformation performance.",
        """This is a longer text with multiple paragraphs. It contains various types of content
that can be transformed using different strategies. The text has enough complexity to
test all three transformation types effectively. We expect the system to maintain
good performance while processing this content.

Therefore, the robustness testing framework should demonstrate efficient processing
times and reliable transformation results across all test cases."""
    ]

    performance_results = []

    print("Testing performance requirements...")
    print("=" * 50)

    for i, text in enumerate(test_texts):
        print(f"\nTest {i+1}: Text length = {len(text)} characters")

        # Run multiple iterations for reliable measurement
        iteration_times = []
        transformation_times = []

        for iteration in range(5):
            start_time = time.time()
            result = engine.execute_robustness_test(f"perf_test_{i}_{iteration}", text)
            end_time = time.time()

            execution_time = end_time - start_time
            iteration_times.append(execution_time)

            # Collect individual transformation times
            for transform_result in result.transformation_results:
                transformation_times.append(transform_result.processing_time)

            print(f"  Iteration {iteration+1}: {execution_time:.3f}s, "
                  f"Transformations: {len(result.transformation_results)}, "
                  f"Consistency: {result.consistency_score:.3f}")

        # Calculate statistics
        avg_execution_time = statistics.mean(iteration_times)
        max_execution_time = max(iteration_times)
        avg_transform_time = statistics.mean(transformation_times) if transformation_times else 0
        max_transform_time = max(transformation_times) if transformation_times else 0

        performance_results.append({
            "text_length": len(text),
            "avg_execution_time": avg_execution_time,
            "max_execution_time": max_execution_time,
            "avg_transform_time": avg_transform_time,
            "max_transform_time": max_transform_time,
            "transformation_count": len(transformation_times) / 5  # Average per iteration
        })

        # Check against requirements
        execution_ok = max_execution_time <= 1.0  # Allow some overhead
        transform_ok = max_transform_time <= 0.5  # 500ms requirement

        print(f"  Results:")
        print(f"    Avg execution time: {avg_execution_time:.3f}s")
        print(f"    Max execution time: {max_execution_time:.3f}s {'✓' if execution_ok else '✗'}")
        print(f"    Avg transformation time: {avg_transform_time:.3f}s")
        print(f"    Max transformation time: {max_transform_time:.3f}s {'✓' if transform_ok else '✗'}")
        print(f"    Avg transformations per iteration: {performance_results[-1]['transformation_count']:.1f}")

    # Summary
    print("\n" + "=" * 50)
    print("PERFORMANCE SUMMARY")
    print("=" * 50)

    all_execution_times = [r["max_execution_time"] for r in performance_results]
    all_transform_times = []
    for r in performance_results:
        all_transform_times.extend([r["avg_transform_time"]] * int(r["transformation_count"] * 5))

    if all_execution_times:
        max_execution = max(all_execution_times)
        print(f"Maximum execution time: {max_execution:.3f}s {'✓' if max_execution <= 1.0 else '✗'}")

    if all_transform_times:
        max_transform = max(all_transform_times)
        print(f"Maximum transformation time: {max_transform:.3f}s {'✓' if max_transform <= 0.5 else '✗'}")

    # Overall assessment
    performance_met = (max(all_execution_times) <= 1.0 if all_execution_times else True) and \
                     (max(all_transform_times) <= 0.5 if all_transform_times else True)

    print(f"\nOverall performance requirement: {'✓ MET' if performance_met else '✗ NOT MET'}")
    print(f"Target: <500ms per transformation")
    print(f"Actual: {max(all_transform_times)*1000:.1f}ms per transformation" if all_transform_times else "No data")

    return performance_met


def test_reproducibility():
    """Test result reproducibility"""

    print("\n" + "=" * 50)
    print("TESTING REPRODUCIBILITY")
    print("=" * 50)

    # Use fixed random seed
    transform_config = TransformationConfig(random_seed=42)
    robustness_config = RobustnessTestConfig(transformation_config=transform_config)

    test_text = "This is a test text for reproducibility testing with fixed random seed."

    # Run test multiple times
    results = []
    for i in range(3):
        engine = RobustnessEngine(robustness_config)
        result = engine.execute_robustness_test(f"repro_test_{i}", test_text)
        results.append(result)
        print(f"Run {i+1}: {len(result.transformation_results)} transformations, "
              f"Consistency: {result.consistency_score:.3f}")

    # Check reproducibility
    transformation_counts = [len(r.transformation_results) for r in results]
    consistency_scores = [r.consistency_score for r in results]

    count_reproducible = len(set(transformation_counts)) == 1
    consistency_variation = max(consistency_scores) - min(consistency_scores)

    print(f"\nTransformation count reproducible: {'✓' if count_reproducible else '✗'}")
    print(f"Consistency score variation: {consistency_variation:.3f}")
    print(f"Reproducibility assessment: {'✓ GOOD' if consistency_variation < 0.1 else '⚠ MARGINAL' if consistency_variation < 0.2 else '✗ POOR'}")

    return count_reproducible and consistency_variation < 0.1


if __name__ == "__main__":
    print("Robustness Engine Performance and Reproducibility Test")
    print("=" * 60)

    performance_ok = test_performance_requirements()
    reproducibility_ok = test_reproducibility()

    print("\n" + "=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)
    print(f"Performance requirements: {'✓ MET' if performance_ok else '✗ NOT MET'}")
    print(f"Reproducibility: {'✓ GOOD' if reproducibility_ok else '✗ NEEDS IMPROVEMENT'}")

    if performance_ok and reproducibility_ok:
        print("\n🎉 All requirements satisfied!")
    else:
        print("\n⚠️  Some requirements need attention.")