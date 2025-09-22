"""
Stability Analyzer - Key Decision Stability Analysis

Analyzes the stability of key decisions across transformations and provides
comprehensive stability metrics for robustness testing.
"""

import re
import time
import logging
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from collections import defaultdict

from .transformation_strategies import TransformationResult
from .robustness_engine import TestExecutionResult


@dataclass
class StabilityMetrics:
    """Stability metrics for analysis"""
    decision_consistency: float
    conclusion_stability: float
    key_term_preservation: float
    structural_stability: float
    overall_stability: float
    confidence_interval: Tuple[float, float]
    sample_size: int


@dataclass
class DecisionPoint:
    """Represents a key decision point in the analysis"""
    decision_id: str
    decision_type: str
    original_value: Any
    transformed_values: List[Any]
    stability_score: float
    confidence: float
    metadata: Dict[str, Any]


@dataclass
class StabilityAnalysisConfig:
    """Configuration for stability analysis"""
    min_stability_threshold: float = 0.85
    confidence_level: float = 0.95
    min_sample_size: int = 5
    enable_statistical_analysis: bool = True
    enable_trend_analysis: bool = True
    decision_keywords: List[str] = None

    def __post_init__(self):
        if self.decision_keywords is None:
            self.decision_keywords = [
                "conclusion", "decision", "result", "outcome", "finding",
                "recommendation", "assessment", "evaluation", "analysis",
                "determination", "judgment", "verdict", "conclusion"
            ]


class StabilityAnalyzer:
    """
    Stability Analyzer for Key Decisions

    Analyzes the stability of key decisions across multiple transformations
    and provides comprehensive stability metrics.
    """

    def __init__(self, config: StabilityAnalysisConfig):
        """
        Initialize Stability Analyzer

        Args:
            config: Configuration for stability analysis
        """
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

        # Storage for analysis history
        self.analysis_history = []
        self.decision_registry = {}

        # Pattern matching for decision points
        self.decision_patterns = self._initialize_decision_patterns()

        self.logger.info("Stability Analyzer initialized")

    def _initialize_decision_patterns(self) -> Dict[str, re.Pattern]:
        """Initialize regex patterns for decision point detection"""
        patterns = {
            "conclusion": re.compile(
                r'\b(in\s+conclusion|therefore|thus|hence|consequently|ultimately|finally|overall)\b.*?[.!?]',
                re.IGNORECASE
            ),
            "recommendation": re.compile(
                r'\b(recommend|suggest|propose|advise|should|would|could)\b.*?[.!?]',
                re.IGNORECASE
            ),
            "assessment": re.compile(
                r'\b(assessment|evaluation|analysis|review|examination)\b.*?[.!?]',
                re.IGNORECASE
            ),
            "determination": re.compile(
                r'\b(determine|establish|identify|recognize|confirm|verify)\b.*?[.!?]',
                re.IGNORECASE
            ),
            "quantitative": re.compile(
                r'\b(\d+%|\d+\.\d+|\d+)\s*(percent|percentage|score|rate|ratio)\b',
                re.IGNORECASE
            )
        }

        return patterns

    def analyze_stability(self, test_results: List[TestExecutionResult],
                        decision_context: Optional[Dict[str, Any]] = None) -> StabilityMetrics:
        """
        Analyze stability across multiple test results

        Args:
            test_results: List of test execution results
            decision_context: Optional context for decision analysis

        Returns:
            StabilityMetrics with comprehensive analysis
        """
        start_time = time.time()

        try:
            self.logger.info("Starting stability analysis for %d test results", len(test_results))

            if len(test_results) < self.config.min_sample_size:
                self.logger.warning("Insufficient sample size for stability analysis")
                return StabilityMetrics(
                    decision_consistency=0.0,
                    conclusion_stability=0.0,
                    key_term_preservation=0.0,
                    structural_stability=0.0,
                    overall_stability=0.0,
                    confidence_interval=(0.0, 0.0),
                    sample_size=len(test_results)
                )

            # Extract decision points from all test results
            decision_points = self._extract_decision_points(test_results)

            # Analyze decision consistency
            decision_consistency = self._analyze_decision_consistency(decision_points)

            # Analyze conclusion stability
            conclusion_stability = self._analyze_conclusion_stability(test_results)

            # Analyze key term preservation
            key_term_preservation = self._analyze_key_term_preservation(test_results)

            # Analyze structural stability
            structural_stability = self._analyze_structural_stability(test_results)

            # Calculate overall stability
            overall_stability = self._calculate_overall_stability(
                decision_consistency, conclusion_stability, key_term_preservation, structural_stability
            )

            # Calculate confidence interval
            confidence_interval = self._calculate_confidence_interval(
                [decision_consistency, conclusion_stability, key_term_preservation, structural_stability]
            )

            processing_time = time.time() - start_time

            stability_metrics = StabilityMetrics(
                decision_consistency=decision_consistency,
                conclusion_stability=conclusion_stability,
                key_term_preservation=key_term_preservation,
                structural_stability=structural_stability,
                overall_stability=overall_stability,
                confidence_interval=confidence_interval,
                sample_size=len(test_results)
            )

            # Store analysis in history
            self.analysis_history.append({
                "timestamp": datetime.now(timezone.utc),
                "sample_size": len(test_results),
                "stability_metrics": stability_metrics,
                "processing_time": processing_time,
                "decision_context": decision_context
            })

            self.logger.info("Stability analysis completed (overall: %.2f)", overall_stability)

            return stability_metrics

        except Exception as e:
            self.logger.error("Error in stability analysis: %e")
            processing_time = time.time() - start_time

            return StabilityMetrics(
                decision_consistency=0.0,
                conclusion_stability=0.0,
                key_term_preservation=0.0,
                structural_stability=0.0,
                overall_stability=0.0,
                confidence_interval=(0.0, 0.0),
                sample_size=len(test_results)
            )

    def _extract_decision_points(self, test_results: List[TestExecutionResult]) -> List[DecisionPoint]:
        """
        Extract decision points from all test results for stability analysis.

        This method processes each test result and its transformations to identify
        key decision points that need to be tracked for stability analysis.
        Decision points include conclusions, findings, and important statements
        that should remain stable across transformations.

        Args:
            test_results: List of test execution results to analyze

        Returns:
            List[DecisionPoint]: List of extracted decision points with their
                                stability information across transformations

        Process:
            1. For each test result, extract decisions from original text
            2. For each transformation, extract decisions from transformed text
            3. Match corresponding decisions across transformations
            4. Calculate stability scores for each decision point
        """
        decision_points = []

        for i, test_result in enumerate(test_results):
            # Extract decision points from the original text
            original_decisions = self._extract_decisions_from_text(
                test_result.original_text, f"test_{i}_original"
            )

            # Extract decision points from each transformed version
            for j, transform_result in enumerate(test_result.transformation_results):
                transformed_decisions = self._extract_decisions_from_text(
                    transform_result.transformed_text, f"test_{i}_transform_{j}"
                )

                # Match and track decisions across transformations
                self._match_decisions(original_decisions, transformed_decisions)

            decision_points.extend(original_decisions)

        return decision_points

    def _extract_decisions_from_text(self, text: str, source_id: str) -> List[DecisionPoint]:
        """Extract decision points from text"""
        decisions = []

        # Extract conclusions
        conclusions = self._extract_conclusions(text)
        for conclusion in conclusions:
            decision = DecisionPoint(
                decision_id=f"{source_id}_conclusion_{len(decisions)}",
                decision_type="conclusion",
                original_value=conclusion,
                transformed_values=[],
                stability_score=1.0,
                confidence=0.8,
                metadata={"source": source_id, "text_length": len(conclusion)}
            )
            decisions.append(decision)

        # Extract recommendations
        recommendations = self._extract_recommendations(text)
        for recommendation in recommendations:
            decision = DecisionPoint(
                decision_id=f"{source_id}_recommendation_{len(decisions)}",
                decision_type="recommendation",
                original_value=recommendation,
                transformed_values=[],
                stability_score=1.0,
                confidence=0.7,
                metadata={"source": source_id, "text_length": len(recommendation)}
            )
            decisions.append(decision)

        # Extract quantitative statements
        quantitative = self._extract_quantitative_statements(text)
        for quant in quantitative:
            decision = DecisionPoint(
                decision_id=f"{source_id}_quantitative_{len(decisions)}",
                decision_type="quantitative",
                original_value=quant,
                transformed_values=[],
                stability_score=1.0,
                confidence=0.9,
                metadata={"source": source_id, "text_length": len(quant)}
            )
            decisions.append(decision)

        return decisions

    def _extract_conclusions(self, text: str) -> List[str]:
        """Extract conclusions from text"""
        conclusions = []

        # Use regex patterns to find conclusions
        for pattern_name, pattern in self.decision_patterns.items():
            if pattern_name == "conclusion":
                matches = pattern.findall(text)
                conclusions.extend(matches)

        # If no structured conclusions found, look for sentences with conclusion keywords
        if not conclusions:
            sentences = text.split('.')
            for sentence in sentences:
                if any(keyword in sentence.lower() for keyword in self.config.decision_keywords[:4]):
                    conclusions.append(sentence.strip())

        return conclusions

    def _extract_recommendations(self, text: str) -> List[str]:
        """Extract recommendations from text"""
        recommendations = []

        # Use regex pattern for recommendations
        pattern = self.decision_patterns["recommendation"]
        matches = pattern.findall(text)
        recommendations.extend(matches)

        return recommendations

    def _extract_quantitative_statements(self, text: str) -> List[str]:
        """Extract quantitative statements from text"""
        quantitative = []

        # Use regex pattern for quantitative statements
        pattern = self.decision_patterns["quantitative"]
        matches = pattern.findall(text)
        quantitative.extend(matches)

        return quantitative

    def _match_decisions(self, original_decisions: List[DecisionPoint],
                        transformed_decisions: List[DecisionPoint]):
        """Match decisions between original and transformed text"""
        # Simple matching based on decision type and content similarity
        for orig_decision in original_decisions:
            for trans_decision in transformed_decisions:
                if (orig_decision.decision_type == trans_decision.decision_type and
                    self._calculate_similarity(orig_decision.original_value, trans_decision.original_value) > 0.6):
                    orig_decision.transformed_values.append(trans_decision.original_value)

    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two texts"""
        # Simple word overlap similarity
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())

        if not words1 or not words2:
            return 0.0

        intersection = words1 & words2
        union = words1 | words2

        return len(intersection) / len(union)

    def _analyze_decision_consistency(self, decision_points: List[DecisionPoint]) -> float:
        """Analyze decision consistency across transformations"""
        if not decision_points:
            return 0.0

        consistency_scores = []

        for decision in decision_points:
            if decision.transformed_values:
                # Calculate consistency based on similarity to original
                similarities = [
                    self._calculate_similarity(decision.original_value, transformed)
                    for transformed in decision.transformed_values
                ]
                avg_similarity = sum(similarities) / len(similarities)
                consistency_scores.append(avg_similarity)
            else:
                consistency_scores.append(1.0)  # No transformation means perfect consistency

        return sum(consistency_scores) / len(consistency_scores) if consistency_scores else 0.0

    def _analyze_conclusion_stability(self, test_results: List[TestExecutionResult]) -> float:
        """Analyze conclusion stability across test results"""
        if not test_results:
            return 0.0

        conclusion_stabilities = []

        for test_result in test_results:
            original_conclusions = self._extract_conclusions(test_result.original_text)

            if not original_conclusions:
                continue

            transformation_scores = []
            for transform_result in test_result.transformation_results:
                transformed_conclusions = self._extract_conclusions(transform_result.transformed_text)

                if original_conclusions and transformed_conclusions:
                    # Calculate conclusion preservation
                    original_set = set(original_conclusions)
                    transformed_set = set(transformed_conclusions)

                    intersection = original_set & transformed_set
                    preservation_score = len(intersection) / len(original_set)
                    transformation_scores.append(preservation_score)

            if transformation_scores:
                avg_score = sum(transformation_scores) / len(transformation_scores)
                conclusion_stabilities.append(avg_score)

        return sum(conclusion_stabilities) / len(conclusion_stabilities) if conclusion_stabilities else 0.0

    def _analyze_key_term_preservation(self, test_results: List[TestExecutionResult]) -> float:
        """Analyze key term preservation across transformations"""
        if not test_results:
            return 0.0

        key_terms = [
            "robustness", "transformation", "validation", "testing",
            "semantic", "neutral", "consistency", "stability",
            "conclusion", "result", "analysis", "evaluation"
        ]

        preservation_scores = []

        for test_result in test_results:
            original_text = test_result.original_text.lower()
            original_term_count = sum(1 for term in key_terms if term in original_text)

            if original_term_count == 0:
                continue

            transformation_preservations = []
            for transform_result in test_result.transformation_results:
                transformed_text = transform_result.transformed_text.lower()
                transformed_term_count = sum(1 for term in key_terms if term in transformed_text)

                preservation_ratio = transformed_term_count / original_term_count
                transformation_preservations.append(min(preservation_ratio, 1.0))

            if transformation_preservations:
                avg_preservation = sum(transformation_preservations) / len(transformation_preservations)
                preservation_scores.append(avg_preservation)

        return sum(preservation_scores) / len(preservation_scores) if preservation_scores else 0.0

    def _analyze_structural_stability(self, test_results: List[TestExecutionResult]) -> float:
        """Analyze structural stability across transformations"""
        if not test_results:
            return 0.0

        structural_scores = []

        for test_result in test_results:
            original_structure = self._analyze_text_structure(test_result.original_text)

            transformation_scores = []
            for transform_result in test_result.transformation_results:
                transformed_structure = self._analyze_text_structure(transform_result.transformed_text)

                # Calculate structural similarity
                para_ratio = min(original_structure["paragraphs"], transformed_structure["paragraphs"]) / max(original_structure["paragraphs"], transformed_structure["paragraphs"]) if max(original_structure["paragraphs"], transformed_structure["paragraphs"]) > 0 else 1.0
                sent_ratio = min(original_structure["sentences"], transformed_structure["sentences"]) / max(original_structure["sentences"], transformed_structure["sentences"]) if max(original_structure["sentences"], transformed_structure["sentences"]) > 0 else 1.0

                structural_similarity = (para_ratio + sent_ratio) / 2
                transformation_scores.append(structural_similarity)

            if transformation_scores:
                avg_score = sum(transformation_scores) / len(transformation_scores)
                structural_scores.append(avg_score)

        return sum(structural_scores) / len(structural_scores) if structural_scores else 0.0

    def _analyze_text_structure(self, text: str) -> Dict[str, int]:
        """Analyze basic text structure"""
        paragraphs = len([p for p in text.split('\n\n') if p.strip()])
        sentences = len([s for s in text.split('.') if s.strip()])
        words = len(text.split())

        return {
            "paragraphs": paragraphs,
            "sentences": sentences,
            "words": words
        }

    def _calculate_overall_stability(self, decision_consistency: float, conclusion_stability: float,
                                   key_term_preservation: float, structural_stability: float) -> float:
        """Calculate overall stability score"""
        # Weighted average of different stability aspects
        weights = {
            "decision_consistency": 0.4,
            "conclusion_stability": 0.3,
            "key_term_preservation": 0.2,
            "structural_stability": 0.1
        }

        overall_score = (
            decision_consistency * weights["decision_consistency"] +
            conclusion_stability * weights["conclusion_stability"] +
            key_term_preservation * weights["key_term_preservation"] +
            structural_stability * weights["structural_stability"]
        )

        return overall_score

    def _calculate_confidence_interval(self, scores: List[float]) -> Tuple[float, float]:
        """Calculate confidence interval for stability scores"""
        if not scores or len(scores) < 2:
            return (0.0, 1.0)

        import statistics
        mean_score = statistics.mean(scores)
        stdev = statistics.stdev(scores) if len(scores) > 1 else 0.0

        # 95% confidence interval (simplified)
        margin_of_error = 1.96 * stdev / (len(scores) ** 0.5) if len(scores) > 1 else 0.1

        lower_bound = max(0.0, mean_score - margin_of_error)
        upper_bound = min(1.0, mean_score + margin_of_error)

        return (lower_bound, upper_bound)

    def generate_stability_report(self, stability_metrics: StabilityMetrics,
                                 test_results: List[TestExecutionResult]) -> Dict[str, Any]:
        """Generate comprehensive stability report"""
        report = {
            "analysis_timestamp": datetime.now(timezone.utc).isoformat(),
            "sample_size": stability_metrics.sample_size,
            "overall_stability": stability_metrics.overall_stability,
            "stability_threshold": self.config.min_stability_threshold,
            "meets_threshold": stability_metrics.overall_stability >= self.config.min_stability_threshold,
            "confidence_interval": stability_metrics.confidence_interval,
            "detailed_metrics": {
                "decision_consistency": stability_metrics.decision_consistency,
                "conclusion_stability": stability_metrics.conclusion_stability,
                "key_term_preservation": stability_metrics.key_term_preservation,
                "structural_stability": stability_metrics.structural_stability
            },
            "recommendations": self._generate_stability_recommendations(stability_metrics),
            "test_ids": [result.test_id for result in test_results]
        }

        return report

    def _generate_stability_recommendations(self, stability_metrics: StabilityMetrics) -> List[str]:
        """Generate recommendations based on stability analysis"""
        recommendations = []

        if stability_metrics.overall_stability < self.config.min_stability_threshold:
            recommendations.append("Overall stability below threshold - review transformation strategies")

        if stability_metrics.decision_consistency < 0.8:
            recommendations.append("Decision consistency is low - consider adjusting decision extraction algorithms")

        if stability_metrics.conclusion_stability < 0.8:
            recommendations.append("Conclusion stability needs improvement - review conclusion preservation methods")

        if stability_metrics.key_term_preservation < 0.9:
            recommendations.append("Key term preservation could be improved - enhance term protection mechanisms")

        if stability_metrics.structural_stability < 0.7:
            recommendations.append("Structural stability is low - consider more conservative transformation approaches")

        if not recommendations:
            recommendations.append("Stability metrics are within acceptable ranges")

        return recommendations

    def get_stability_history(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get stability analysis history"""
        if limit:
            return self.analysis_history[-limit:]
        return self.analysis_history

    def get_analyzer_status(self) -> Dict[str, Any]:
        """Get current analyzer status"""
        return {
            "initialized": True,
            "total_analyses": len(self.analysis_history),
            "config": {
                "min_stability_threshold": self.config.min_stability_threshold,
                "confidence_level": self.config.confidence_level,
                "min_sample_size": self.config.min_sample_size
            },
            "available_decision_types": ["conclusion", "recommendation", "quantitative"]
        }