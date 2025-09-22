"""
Transformation Validator - Semantic Neutral Validation System

Validates that transformations maintain semantic neutrality and provides
comprehensive validation metrics for robustness testing.
"""

import re
import time
import logging
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass
from abc import ABC, abstractmethod
import json

from .transformation_strategies import TransformationResult


@dataclass
class ValidationResult:
    """Result of transformation validation"""
    validation_type: str
    score: float
    threshold: float
    passed: bool
    details: Dict[str, Any]
    confidence: float
    processing_time: float


@dataclass
class ValidationConfig:
    """Configuration for validation system"""
    semantic_similarity_threshold: float = 0.8
    key_conclusion_preservation_threshold: float = 0.9
    structural_integrity_threshold: float = 0.7
    overall_validation_threshold: float = 0.85
    enable_detailed_analysis: bool = True
    max_validation_time: float = 1.0  # 1 second max validation time


class BaseValidator(ABC):
    """Abstract base class for transformation validators"""

    def __init__(self, config: ValidationConfig):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def validate(self, original_text: str, transformed_text: str,
                transformation_result: TransformationResult) -> ValidationResult:
        """Validate transformation result"""
        pass

    def _track_performance(self, start_time: float) -> float:
        """Track validation performance"""
        return time.time() - start_time


class SemanticSimilarityValidator(BaseValidator):
    """
    Semantic Similarity Validator

    Validates that transformations preserve semantic meaning through
    various similarity metrics and heuristics.
    """

    def __init__(self, config: ValidationConfig):
        super().__init__(config)
        self._initialize_nlp_resources()

    def _initialize_nlp_resources(self):
        """Initialize NLP resources for semantic validation"""
        try:
            # Try to import sentence transformers for semantic similarity
            from sentence_transformers import SentenceTransformer
            self.semantic_model = SentenceTransformer('all-MiniLM-L6-v2')
            self.model_available = True
            self.logger.info("Sentence transformers model loaded successfully")
        except ImportError:
            self.model_available = False
            self.logger.warning("Sentence transformers not available, using fallback validation")
            # Initialize fallback resources
            self._initialize_fallback_resources()

    def _initialize_fallback_resources(self):
        """Initialize fallback validation resources"""
        # Keyword importance weights
        self.keyword_weights = {
            "important": 1.0, "crucial": 1.0, "essential": 1.0, "critical": 1.0,
            "significant": 0.9, "major": 0.9, "key": 0.8, "primary": 0.8,
            "main": 0.7, "core": 0.7, "fundamental": 0.8
        }

        # Negation words that change meaning
        self.negation_words = {
            "not", "no", "never", "none", "neither", "nor", "nothing",
            "nowhere", "nobody", "no one", "cannot", "can't", "don't", "doesn't"
        }

    def validate(self, original_text: str, transformed_text: str,
                transformation_result: TransformationResult) -> ValidationResult:
        """Validate semantic similarity"""
        start_time = time.time()

        try:
            if self.model_available:
                similarity_score = self._calculate_model_similarity(original_text, transformed_text)
            else:
                similarity_score = self._calculate_fallback_similarity(original_text, transformed_text)

            # Additional validation checks
            key_term_preservation = self._validate_key_term_preservation(original_text, transformed_text)
            negation_consistency = self._validate_negation_consistency(original_text, transformed_text)

            # Calculate overall semantic score
            semantic_score = (
                similarity_score * 0.6 +
                key_term_preservation * 0.25 +
                negation_consistency * 0.15
            )

            processing_time = self._track_performance(start_time)

            return ValidationResult(
                validation_type="semantic_similarity",
                score=semantic_score,
                threshold=self.config.semantic_similarity_threshold,
                passed=semantic_score >= self.config.semantic_similarity_threshold,
                details={
                    "similarity_score": similarity_score,
                    "key_term_preservation": key_term_preservation,
                    "negation_consistency": negation_consistency,
                    "model_used": self.model_available
                },
                confidence=min(semantic_score, 1.0),
                processing_time=processing_time
            )

        except Exception as e:
            self.logger.error(f"Error in semantic validation: {e}")
            processing_time = self._track_performance(start_time)
            return ValidationResult(
                validation_type="semantic_similarity",
                score=0.0,
                threshold=self.config.semantic_similarity_threshold,
                passed=False,
                details={"error": str(e)},
                confidence=0.0,
                processing_time=processing_time
            )

    def _calculate_model_similarity(self, original_text: str, transformed_text: str) -> float:
        """
        Calculate semantic similarity using sentence transformers.

        This method uses a pre-trained sentence transformer model to encode
        both texts into vector representations and calculates their cosine
        similarity as a measure of semantic equivalence.

        Args:
            original_text: The original text to compare
            transformed_text: The transformed text to compare

        Returns:
            float: Semantic similarity score between 0.0 and 1.0

        Note:
            If the model calculation fails, falls back to heuristic-based
            similarity calculation for robustness.
        """
        try:
            # Encode texts into vector representations
            original_embedding = self.semantic_model.encode(original_text, convert_to_tensor=True)
            transformed_embedding = self.semantic_model.encode(transformed_text, convert_to_tensor=True)

            # Calculate cosine similarity between embeddings
            import torch
            similarity = torch.nn.functional.cosine_similarity(
                original_embedding, transformed_embedding, dim=0
            )

            return float(similarity)
        except Exception as e:
            self.logger.warning(f"Error in model similarity calculation: {e}")
            return self._calculate_fallback_similarity(original_text, transformed_text)

    def _calculate_fallback_similarity(self, original_text: str, transformed_text: str) -> float:
        """
        Calculate semantic similarity using fallback heuristics when model is unavailable.

        This method uses multiple heuristic approaches to estimate semantic similarity:
        1. Jaccard similarity for word overlap
        2. Weighted word overlap for keyword importance
        3. Length ratio penalty to discourage extreme length changes

        Args:
            original_text: The original text to compare
            transformed_text: The transformed text to compare

        Returns:
            float: Estimated semantic similarity score between 0.0 and 1.0
        """
        # Text overlap analysis using word sets
        original_words = set(original_text.lower().split())
        transformed_words = set(transformed_text.lower().split())

        # Handle edge cases: empty texts
        if not original_words:
            return 1.0 if not transformed_words else 0.0

        # Calculate Jaccard similarity (intersection over union)
        intersection = original_words & transformed_words
        union = original_words | transformed_words
        jaccard_score = len(intersection) / len(union) if union else 0.0

        # Calculate weighted word overlap considering keyword importance
        weighted_overlap = self._calculate_weighted_overlap(original_text, transformed_text)

        # Apply length ratio penalty to discourage extreme length changes
        length_ratio = min(len(transformed_text) / len(original_text), len(original_text) / len(transformed_text))
        length_penalty = min(length_ratio, 1.0)

        # Combine scores with weights: Jaccard (40%) + Weighted (60%)
        similarity_score = (jaccard_score * 0.4 + weighted_overlap * 0.6) * length_penalty

        return similarity_score

    def _calculate_weighted_overlap(self, original_text: str, transformed_text: str) -> float:
        """Calculate weighted word overlap based on keyword importance"""
        original_lower = original_text.lower()
        transformed_lower = transformed_text.lower()

        total_weight = 0.0
        matched_weight = 0.0

        for keyword, weight in self.keyword_weights.items():
            original_count = original_lower.count(keyword)
            transformed_count = transformed_lower.count(keyword)

            if original_count > 0:
                total_weight += weight * original_count
                matched_weight += weight * min(original_count, transformed_count)

        return matched_weight / total_weight if total_weight > 0 else 1.0

    def _validate_key_term_preservation(self, original_text: str, transformed_text: str) -> float:
        """Validate that key terms are preserved"""
        key_terms = [
            "robustness", "transformation", "validation", "testing",
            "semantic", "neutral", "consistency", "stability",
            "conclusion", "result", "analysis", "evaluation"
        ]

        original_terms = [term for term in key_terms if term.lower() in original_text.lower()]
        if not original_terms:
            return 1.0

        preserved_terms = [term for term in original_terms if term.lower() in transformed_text.lower()]

        return len(preserved_terms) / len(original_terms)

    def _validate_negation_consistency(self, original_text: str, transformed_text: str) -> float:
        """Validate that negation patterns are consistent"""
        original_negations = [word for word in original_text.lower().split() if word in self.negation_words]
        transformed_negations = [word for word in transformed_text.lower().split() if word in self.negation_words]

        if not original_negations:
            return 1.0 if not transformed_negations else 0.5

        # Check if negation count is similar
        negation_ratio = len(transformed_negations) / len(original_negations)
        if 0.5 <= negation_ratio <= 2.0:  # Allow some variation
            return 1.0
        elif 0.25 <= negation_ratio <= 4.0:  # Allow more variation
            return 0.7
        else:
            return 0.3


class StructuralIntegrityValidator(BaseValidator):
    """
    Structural Integrity Validator

    Validates that transformations maintain proper text structure and coherence.
    """

    def validate(self, original_text: str, transformed_text: str,
                transformation_result: TransformationResult) -> ValidationResult:
        """Validate structural integrity"""
        start_time = time.time()

        try:
            # Analyze text structure
            original_structure = self._analyze_text_structure(original_text)
            transformed_structure = self._analyze_text_structure(transformed_text)

            # Calculate structural similarity
            paragraph_score = self._compare_paragraph_structure(original_structure, transformed_structure)
            sentence_score = self._compare_sentence_structure(original_structure, transformed_structure)
            coherence_score = self._assess_coherence(transformed_text)

            # Calculate overall structural score
            structural_score = (
                paragraph_score * 0.4 +
                sentence_score * 0.4 +
                coherence_score * 0.2
            )

            processing_time = self._track_performance(start_time)

            return ValidationResult(
                validation_type="structural_integrity",
                score=structural_score,
                threshold=self.config.structural_integrity_threshold,
                passed=structural_score >= self.config.structural_integrity_threshold,
                details={
                    "paragraph_score": paragraph_score,
                    "sentence_score": sentence_score,
                    "coherence_score": coherence_score,
                    "original_structure": original_structure,
                    "transformed_structure": transformed_structure
                },
                confidence=min(structural_score, 1.0),
                processing_time=processing_time
            )

        except Exception as e:
            self.logger.error(f"Error in structural validation: {e}")
            processing_time = self._track_performance(start_time)
            return ValidationResult(
                validation_type="structural_integrity",
                score=0.0,
                threshold=self.config.structural_integrity_threshold,
                passed=False,
                details={"error": str(e)},
                confidence=0.0,
                processing_time=processing_time
            )

    def _analyze_text_structure(self, text: str) -> Dict[str, Any]:
        """Analyze text structure"""
        # Split into paragraphs
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        words = text.split()

        return {
            "paragraph_count": len(paragraphs),
            "sentence_count": len(sentences),
            "word_count": len(words),
            "average_paragraph_length": len(words) / len(paragraphs) if paragraphs else 0,
            "average_sentence_length": len(words) / len(sentences) if sentences else 0,
            "paragraph_lengths": [len(p.split()) for p in paragraphs],
            "sentence_lengths": [len(s.split()) for s in sentences]
        }

    def _compare_paragraph_structure(self, original: Dict[str, Any], transformed: Dict[str, Any]) -> float:
        """Compare paragraph structure similarity"""
        # Compare paragraph count similarity
        para_count_ratio = min(original["paragraph_count"], transformed["paragraph_count"]) / max(original["paragraph_count"], transformed["paragraph_count"])

        # Compare average paragraph length similarity
        if original["average_paragraph_length"] > 0 and transformed["average_paragraph_length"] > 0:
            length_ratio = min(original["average_paragraph_length"], transformed["average_paragraph_length"]) / max(original["average_paragraph_length"], transformed["average_paragraph_length"])
        else:
            length_ratio = 1.0

        return (para_count_ratio + length_ratio) / 2

    def _compare_sentence_structure(self, original: Dict[str, Any], transformed: Dict[str, Any]) -> float:
        """Compare sentence structure similarity"""
        # Compare sentence count similarity
        sent_count_ratio = min(original["sentence_count"], transformed["sentence_count"]) / max(original["sentence_count"], transformed["sentence_count"])

        # Compare average sentence length similarity
        if original["average_sentence_length"] > 0 and transformed["average_sentence_length"] > 0:
            length_ratio = min(original["average_sentence_length"], transformed["average_sentence_length"]) / max(original["average_sentence_length"], transformed["average_sentence_length"])
        else:
            length_ratio = 1.0

        return (sent_count_ratio + length_ratio) / 2

    def _assess_coherence(self, text: str) -> float:
        """Assess text coherence using simple heuristics"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]

        if len(sentences) < 2:
            return 1.0

        # Check for transitional phrases
        transitional_phrases = [
            "however", "therefore", "furthermore", "moreover", "additionally",
            "consequently", "thus", "hence", "accordingly", "subsequently"
        ]

        coherence_score = 0.0
        for i, sentence in enumerate(sentences[1:], 1):
            # Check if sentence connects to previous one
            has_transition = any(phrase in sentence.lower() for phrase in transitional_phrases)
            if has_transition:
                coherence_score += 0.1

        return min(coherence_score + 0.7, 1.0)  # Base score of 0.7


class TransformationValidator:
    """
    Main Transformation Validator

    Orchestrates multiple validation strategies to provide comprehensive
    validation of transformation results.
    """

    def __init__(self, config: ValidationConfig):
        """
        Initialize Transformation Validator

        Args:
            config: Validation configuration
        """
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

        # Initialize validators
        self.validators = {
            "semantic_similarity": SemanticSimilarityValidator(config),
            "structural_integrity": StructuralIntegrityValidator(config)
        }

        self.logger.info("Transformation Validator initialized with %d validators", len(self.validators))

    def validate_transformation(self, original_text: str, transformed_text: str,
                              transformation_result: TransformationResult) -> Dict[str, ValidationResult]:
        """
        Validate transformation using all available validators

        Args:
            original_text: Original input text
            transformed_text: Transformed text
            transformation_result: Result from transformation

        Returns:
            Dictionary mapping validator names to validation results
        """
        validation_results = {}

        for validator_name, validator in self.validators.items():
            try:
                self.logger.debug("Running %s validator", validator_name)
                result = validator.validate(original_text, transformed_text, transformation_result)
                validation_results[validator_name] = result

                if self.config.enable_detailed_analysis:
                    self.logger.debug("%s validation result: score=%.2f, passed=%s",
                                     validator_name, result.score, result.passed)

            except Exception as e:
                self.logger.error("Error in %s validation: %s", validator_name, e)
                # Create error result
                validation_results[validator_name] = ValidationResult(
                    validation_type=validator_name,
                    score=0.0,
                    threshold=0.0,
                    passed=False,
                    details={"error": str(e)},
                    confidence=0.0,
                    processing_time=0.0
                )

        return validation_results

    def calculate_overall_validation_score(self, validation_results: Dict[str, ValidationResult]) -> float:
        """Calculate overall validation score"""
        if not validation_results:
            return 0.0

        total_score = 0.0
        total_weight = 0.0

        # Weights for different validation types
        validator_weights = {
            "semantic_similarity": 0.7,
            "structural_integrity": 0.3
        }

        for validator_name, result in validation_results.items():
            weight = validator_weights.get(validator_name, 0.5)
            total_score += result.score * weight
            total_weight += weight

        return total_score / total_weight if total_weight > 0 else 0.0

    def generate_validation_report(self, validation_results: Dict[str, ValidationResult],
                                 original_text: str, transformed_text: str) -> Dict[str, Any]:
        """Generate comprehensive validation report"""
        overall_score = self.calculate_overall_validation_score(validation_results)

        # Count passed/failed validations
        passed_validations = sum(1 for result in validation_results.values() if result.passed)
        total_validations = len(validation_results)

        # Generate recommendations
        recommendations = self._generate_recommendations(validation_results)

        report = {
            "overall_score": overall_score,
            "threshold": self.config.overall_validation_threshold,
            "passed": overall_score >= self.config.overall_validation_threshold,
            "passed_validations": passed_validations,
            "total_validations": total_validations,
            "validation_details": {name: {
                "score": result.score,
                "threshold": result.threshold,
                "passed": result.passed,
                "confidence": result.confidence,
                "processing_time": result.processing_time
            } for name, result in validation_results.items()},
            "recommendations": recommendations,
            "summary": {
                "overall_consistency": overall_score,
                "validation_coverage": passed_validations / total_validations if total_validations > 0 else 0.0,
                "processing_time": sum(result.processing_time for result in validation_results.values())
            }
        }

        return report

    def _generate_recommendations(self, validation_results: Dict[str, ValidationResult]) -> List[str]:
        """Generate recommendations based on validation results"""
        recommendations = []

        for validator_name, result in validation_results.items():
            if not result.passed:
                if validator_name == "semantic_similarity":
                    recommendations.append(
                        "Consider adjusting transformation parameters to better preserve semantic meaning"
                    )
                elif validator_name == "structural_integrity":
                    recommendations.append(
                        "Review text structure preservation in transformation strategy"
                    )

        if recommendations:
            recommendations.append("Consider running additional validation tests with different input samples")

        return recommendations

    def get_validator_status(self) -> Dict[str, Any]:
        """Get current validator status"""
        return {
            "initialized": True,
            "available_validators": list(self.validators.keys()),
            "config": {
                "semantic_similarity_threshold": self.config.semantic_similarity_threshold,
                "structural_integrity_threshold": self.config.structural_integrity_threshold,
                "overall_validation_threshold": self.config.overall_validation_threshold
            }
        }