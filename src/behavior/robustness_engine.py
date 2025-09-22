"""
Robustness Engine - Core Testing Engine

Main engine for orchestrating robustness testing with transformation strategies,
validation, and reporting capabilities.
"""

import time
import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import logging

from .transformation_strategies import (
    TransformationStrategy, TransformationResult, TransformationConfig,
    TransformationFactory, SynonymReplacementStrategy,
    ParagraphReorderingStrategy, IrrelevantContentInjectionStrategy
)


@dataclass
class RobustnessTestConfig:
    """Configuration for robustness testing"""
    target_consistency_score: float = 0.9
    max_processing_time: float = 0.5  # 500ms
    enable_performance_tracking: bool = True
    enable_detailed_logging: bool = True
    transformation_config: TransformationConfig = None

    def __post_init__(self):
        if self.transformation_config is None:
            self.transformation_config = TransformationConfig()


@dataclass
class TestExecutionResult:
    """Result of robustness test execution"""
    test_id: str
    timestamp: datetime
    original_text: str
    transformation_results: List[TransformationResult]
    consistency_score: float
    performance_metrics: Dict[str, float]
    validation_results: Dict[str, Any]
    success_criteria_met: bool
    execution_time: float
    metadata: Dict[str, Any]


class RobustnessEngine:
    """
    Robustness Testing Engine

    Orchestrates transformation testing with validation and reporting capabilities.
    Implements the core testing workflow for ensuring system stability under input variations.
    """

    def __init__(self, config: RobustnessTestConfig):
        """
        Initialize Robustness Engine

        Args:
            config: Configuration for robustness testing
        """
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

        # Initialize transformation strategies
        self.strategies = self._initialize_strategies()

        # Performance tracking
        self.performance_history = []
        self.test_execution_count = 0

        # Registry for test results
        self.test_results_registry = {}

        self.logger.info("Robustness Engine initialized with %d strategies", len(self.strategies))

    def _initialize_strategies(self) -> Dict[str, TransformationStrategy]:
        """Initialize transformation strategies"""
        strategies = {}
        strategy_types = TransformationFactory.get_available_strategies()

        for strategy_type in strategy_types:
            try:
                strategy = TransformationFactory.create_strategy(
                    strategy_type,
                    self.config.transformation_config
                )
                strategies[strategy_type] = strategy
                self.logger.info("Initialized strategy: %s", strategy_type)
            except Exception as e:
                self.logger.error("Failed to initialize strategy %s: %s", strategy_type, e)

        return strategies

    def execute_robustness_test(self, test_id: str, original_text: str,
                              target_conclusions: Optional[List[str]] = None) -> TestExecutionResult:
        """
        Execute comprehensive robustness test

        Args:
            test_id: Unique identifier for the test
            original_text: Original text to test
            target_conclusions: Expected conclusions to verify consistency

        Returns:
            TestExecutionResult with complete test information
        """
        start_time = time.time()

        try:
            self.logger.info("Starting robustness test: %s", test_id)

            # Execute transformations
            transformation_results = self._execute_transformations(original_text)

            # Calculate consistency score
            consistency_score = self._calculate_consistency_score(
                original_text, transformation_results, target_conclusions
            )

            # Collect performance metrics
            performance_metrics = self._collect_performance_metrics(transformation_results)

            # Validate results
            validation_results = self._validate_test_results(
                transformation_results, consistency_score, performance_metrics
            )

            # Determine if success criteria are met
            success_criteria_met = self._check_success_criteria(
                consistency_score, performance_metrics, validation_results
            )

            execution_time = time.time() - start_time

            # Create result object
            test_result = TestExecutionResult(
                test_id=test_id,
                timestamp=datetime.now(timezone.utc),
                original_text=original_text,
                transformation_results=transformation_results,
                consistency_score=consistency_score,
                performance_metrics=performance_metrics,
                validation_results=validation_results,
                success_criteria_met=success_criteria_met,
                execution_time=execution_time,
                metadata={
                    "strategies_used": list(self.strategies.keys()),
                    "text_length": len(original_text),
                    "word_count": len(original_text.split())
                }
            )

            # Store result in registry
            self.test_results_registry[test_id] = test_result

            # Update performance history
            if self.config.enable_performance_tracking:
                self.performance_history.append({
                    "test_id": test_id,
                    "timestamp": test_result.timestamp,
                    "consistency_score": consistency_score,
                    "execution_time": execution_time,
                    "performance_metrics": performance_metrics
                })
                self.test_execution_count += 1

            self.logger.info("Completed robustness test: %s (consistency: %.2f)",
                           test_id, consistency_score)

            return test_result

        except Exception as e:
            self.logger.error("Error executing robustness test %s: %s", test_id, e)
            execution_time = time.time() - start_time

            # Return error result
            return TestExecutionResult(
                test_id=test_id,
                timestamp=datetime.now(timezone.utc),
                original_text=original_text,
                transformation_results=[],
                consistency_score=0.0,
                performance_metrics={},
                validation_results={"error": str(e)},
                success_criteria_met=False,
                execution_time=execution_time,
                metadata={"error": str(e)}
            )

    def _execute_transformations(self, original_text: str) -> List[TransformationResult]:
        """Execute all transformation strategies"""
        transformation_results = []

        for strategy_name, strategy in self.strategies.items():
            try:
                if strategy.is_applicable(original_text):
                    result = strategy.transform(original_text)
                    result.metadata["strategy_name"] = strategy_name
                    transformation_results.append(result)

                    self.logger.debug("Applied %s transformation (confidence: %.2f)",
                                     strategy_name, result.confidence_score)
                else:
                    self.logger.debug("Skipping %s - not applicable to text", strategy_name)

            except Exception as e:
                self.logger.error("Error applying %s transformation: %s", strategy_name, e)

        return transformation_results

    def _calculate_consistency_score(self, original_text: str,
                                   transformation_results: List[TransformationResult],
                                   target_conclusions: Optional[List[str]] = None) -> float:
        """
        Calculate consistency score across transformations

        Args:
            original_text: Original input text
            transformation_results: Results from all transformations
            target_conclusions: Expected conclusions to verify

        Returns:
            Consistency score between 0.0 and 1.0
        """
        if not transformation_results:
            return 0.0

        consistency_scores = []

        # Extract conclusions from original text
        original_conclusions = self._extract_conclusions(original_text)

        # Compare each transformation result with original
        for result in transformation_results:
            transformed_conclusions = self._extract_conclusions(result.transformed_text)

            if target_conclusions:
                # Use provided target conclusions as ground truth
                original_matches = len(set(original_conclusions) & set(target_conclusions))
                transformed_matches = len(set(transformed_conclusions) & set(target_conclusions))

                if len(target_conclusions) > 0:
                    conclusion_consistency = transformed_matches / len(target_conclusions)
                else:
                    conclusion_consistency = 0.0
            else:
                # Compare transformed conclusions with original conclusions
                if len(original_conclusions) > 0:
                    conclusion_consistency = len(set(original_conclusions) & set(transformed_conclusions)) / len(original_conclusions)
                else:
                    conclusion_consistency = 1.0  # No conclusions to compare

            # Combine with transformation confidence
            overall_consistency = (conclusion_consistency * 0.7) + (result.confidence_score * 0.3)
            consistency_scores.append(overall_consistency)

        # Return average consistency
        return sum(consistency_scores) / len(consistency_scores) if consistency_scores else 0.0

    def _extract_conclusions(self, text: str) -> List[str]:
        """Extract conclusions from text using simple heuristics"""
        conclusions = []

        # Simple conclusion extraction based on keywords
        conclusion_keywords = [
            "conclusion", "therefore", "thus", "hence", "consequently",
            "as a result", "in conclusion", "to summarize", "overall",
            "finally", "ultimately", "in summary"
        ]

        sentences = text.split('.')
        for sentence in sentences:
            sentence_lower = sentence.lower().strip()
            if any(keyword in sentence_lower for keyword in conclusion_keywords):
                conclusions.append(sentence.strip())

        # If no explicit conclusions, use the last sentence as conclusion
        if not conclusions and sentences:
            last_sentence = sentences[-1].strip()
            if len(last_sentence.split()) > 5:  # Only if substantial
                conclusions.append(last_sentence)

        return conclusions

    def _collect_performance_metrics(self, transformation_results: List[TransformationResult]) -> Dict[str, float]:
        """Collect performance metrics from transformation results"""
        if not transformation_results:
            return {}

        metrics = {
            "total_processing_time": sum(r.processing_time for r in transformation_results),
            "average_processing_time": sum(r.processing_time for r in transformation_results) / len(transformation_results),
            "max_processing_time": max(r.processing_time for r in transformation_results),
            "min_processing_time": min(r.processing_time for r in transformation_results),
            "total_transformations": len(transformation_results),
            "successful_transformations": len([r for r in transformation_results if r.confidence_score > 0]),
            "average_confidence": sum(r.confidence_score for r in transformation_results) / len(transformation_results)
        }

        return metrics

    def _validate_test_results(self, transformation_results: List[TransformationResult],
                             consistency_score: float,
                             performance_metrics: Dict[str, float]) -> Dict[str, Any]:
        """Validate test results against criteria"""
        validation_results = {
            "consistency_validation": {
                "target_score": self.config.target_consistency_score,
                "actual_score": consistency_score,
                "passed": consistency_score >= self.config.target_consistency_score
            },
            "performance_validation": {
                "target_max_time": self.config.max_processing_time,
                "actual_max_time": performance_metrics.get("max_processing_time", 0),
                "passed": performance_metrics.get("max_processing_time", 0) <= self.config.max_processing_time
            },
            "transformation_validation": {
                "target_min_transformations": 1,
                "actual_transformations": len(transformation_results),
                "passed": len(transformation_results) > 0
            }
        }

        # Overall validation
        all_passed = all(v["passed"] for v in validation_results.values())
        validation_results["overall_validation"] = {
            "passed": all_passed,
            "passed_criteria": sum(1 for v in validation_results.values() if v["passed"]),
            "total_criteria": len(validation_results) - 1  # Exclude overall
        }

        return validation_results

    def _check_success_criteria(self, consistency_score: float,
                               performance_metrics: Dict[str, float],
                               validation_results: Dict[str, Any]) -> bool:
        """Check if all success criteria are met"""
        return validation_results.get("overall_validation", {}).get("passed", False)

    def get_test_result(self, test_id: str) -> Optional[TestExecutionResult]:
        """Get test result by ID"""
        return self.test_results_registry.get(test_id)

    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary for all executed tests"""
        if not self.performance_history:
            return {"message": "No performance history available"}

        summary = {
            "total_tests": len(self.performance_history),
            "average_consistency": sum(h["consistency_score"] for h in self.performance_history) / len(self.performance_history),
            "average_execution_time": sum(h["execution_time"] for h in self.performance_history) / len(self.performance_history),
            "best_consistency": max(h["consistency_score"] for h in self.performance_history),
            "worst_consistency": min(h["consistency_score"] for h in self.performance_history),
            "tests_above_threshold": sum(1 for h in self.performance_history if h["consistency_score"] >= self.config.target_consistency_score)
        }

        return summary

    def export_test_results(self, output_path: str, test_ids: Optional[List[str]] = None) -> bool:
        """Export test results to JSON file"""
        try:
            results_to_export = {}

            if test_ids:
                for test_id in test_ids:
                    if test_id in self.test_results_registry:
                        result = self.test_results_registry[test_id]
                        results_to_export[test_id] = asdict(result)
            else:
                for test_id, result in self.test_results_registry.items():
                    results_to_export[test_id] = asdict(result)

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(results_to_export, f, indent=2, default=str)

            self.logger.info("Exported %d test results to %s", len(results_to_export), output_path)
            return True

        except Exception as e:
            self.logger.error("Error exporting test results: %s", e)
            return False

    def reset_performance_history(self):
        """Reset performance tracking history"""
        self.performance_history.clear()
        self.logger.info("Performance history reset")

    def get_engine_status(self) -> Dict[str, Any]:
        """Get current engine status"""
        return {
            "initialized": True,
            "available_strategies": list(self.strategies.keys()),
            "total_tests_executed": self.test_execution_count,
            "performance_history_size": len(self.performance_history),
            "config": {
                "target_consistency_score": self.config.target_consistency_score,
                "max_processing_time": self.config.max_processing_time,
                "enable_performance_tracking": self.config.enable_performance_tracking
            }
        }