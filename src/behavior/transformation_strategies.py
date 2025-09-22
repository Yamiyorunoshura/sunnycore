"""
Transformation Strategies - Strategy Pattern Implementation

Implements various text transformation strategies for robustness testing,
including synonym replacement, paragraph reordering, and irrelevant content injection.
"""

import random
import re
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Any, Optional, Union, Tuple
import logging
from pathlib import Path

try:
    import nltk
    from nltk.corpus import wordnet
    import spacy
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False

try:
    import transformers
    from transformers import AutoTokenizer, AutoModel
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False


@dataclass
class TransformationResult:
    """Result of text transformation"""
    original_text: str
    transformed_text: str
    transformation_type: str
    changes_made: List[str]
    confidence_score: float
    processing_time: float
    metadata: Dict[str, Any]


@dataclass
class TransformationConfig:
    """Configuration for transformation strategies"""
    random_seed: int = 42
    max_synonym_replacements: int = 5
    synonym_confidence_threshold: float = 0.7
    paragraph_shuffle_probability: float = 0.3
    irrelevant_content_ratio: float = 0.1
    preserve_key_terms: bool = True
    enable_performance_tracking: bool = True


class TransformationStrategy(ABC):
    """Abstract base class for transformation strategies"""

    def __init__(self, config: TransformationConfig):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        random.seed(config.random_seed)

    @abstractmethod
    def transform(self, text: str) -> TransformationResult:
        """Transform the input text"""
        pass

    @abstractmethod
    def is_applicable(self, text: str) -> bool:
        """Check if transformation is applicable to the text"""
        pass

    def _track_performance(self, start_time: float) -> float:
        """Track transformation performance"""
        return time.time() - start_time


class SynonymReplacementStrategy(TransformationStrategy):
    """
    Synonym Replacement Transformation Strategy

    Replaces words with their synonyms while preserving semantic meaning.
    """

    def __init__(self, config: TransformationConfig):
        super().__init__(config)
        self._initialize_nlp_resources()

    def _initialize_nlp_resources(self):
        """Initialize NLP resources for synonym replacement"""
        if not NLTK_AVAILABLE:
            self.logger.warning("NLTK not available, using fallback synonym replacement")
            return

        try:
            # Download required NLTK data
            nltk.download('wordnet', quiet=True)
            nltk.download('omw-1.4', quiet=True)
            self.nlp_available = True
        except Exception as e:
            self.logger.error(f"Failed to initialize NLTK: {e}")
            self.nlp_available = False

    def transform(self, text: str) -> TransformationResult:
        """Transform text using synonym replacement"""
        start_time = time.time()
        changes_made = []

        try:
            # Simple word tokenization and replacement
            words = text.split()
            transformed_words = []
            replacement_count = 0

            for word in words:
                if replacement_count >= self.config.max_synonym_replacements:
                    transformed_words.append(word)
                    continue

                # Skip key terms if preservation is enabled
                if self.config.preserve_key_terms and self._is_key_term(word):
                    transformed_words.append(word)
                    continue

                synonym = self._get_synonym(word)
                if synonym and random.random() < self.config.synonym_confidence_threshold:
                    transformed_words.append(synonym)
                    changes_made.append(f"Replaced '{word}' with '{synonym}'")
                    replacement_count += 1
                else:
                    transformed_words.append(word)

            transformed_text = " ".join(transformed_words)
            processing_time = self._track_performance(start_time)

            return TransformationResult(
                original_text=text,
                transformed_text=transformed_text,
                transformation_type="synonym_replacement",
                changes_made=changes_made,
                confidence_score=min(replacement_count / self.config.max_synonym_replacements, 1.0),
                processing_time=processing_time,
                metadata={"replacements_count": replacement_count}
            )

        except Exception as e:
            self.logger.error(f"Error in synonym replacement: {e}")
            processing_time = self._track_performance(start_time)
            return TransformationResult(
                original_text=text,
                transformed_text=text,
                transformation_type="synonym_replacement",
                changes_made=[],
                confidence_score=0.0,
                processing_time=processing_time,
                metadata={"error": str(e)}
            )

    def _get_synonym(self, word: str) -> Optional[str]:
        """Get synonym for a word"""
        if not self.nlp_available:
            # Fallback: simple word variations
            return self._get_fallback_synonym(word)

        try:
            synonyms = []
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    synonym = lemma.name().replace('_', ' ')
                    if synonym.lower() != word.lower():
                        synonyms.append(synonym)

            return random.choice(synonyms) if synonyms else None
        except Exception as e:
            self.logger.warning(f"Error getting synonym for '{word}': {e}")
            return self._get_fallback_synonym(word)

    def _get_fallback_synonym(self, word: str) -> Optional[str]:
        """Fallback synonym replacement using simple rules"""
        fallback_map = {
            "good": "excellent",
            "bad": "poor",
            "big": "large",
            "small": "tiny",
            "fast": "quick",
            "slow": "gradual",
            "important": "crucial",
            "necessary": "essential",
            "help": "assist",
            "use": "utilize",
            "make": "create",
            "get": "obtain",
            "show": "demonstrate",
            "tell": "inform",
            "ask": "inquire"
        }

        return fallback_map.get(word.lower())

    def _is_key_term(self, word: str) -> bool:
        """Check if word is a key term that should be preserved"""
        key_terms = {
            "robustness", "transformation", "validation", "testing",
            "semantic", "neutral", "consistency", "stability"
        }
        return word.lower().strip(".,!?;:\"()[]{}") in key_terms

    def is_applicable(self, text: str) -> bool:
        """Check if synonym replacement is applicable"""
        return len(text.split()) > 5  # Need enough words to replace


class ParagraphReorderingStrategy(TransformationStrategy):
    """
    Paragraph Reordering Transformation Strategy

    Reorders paragraphs while preserving logical flow within paragraphs.
    """

    def transform(self, text: str) -> TransformationResult:
        """Transform text by reordering paragraphs"""
        start_time = time.time()
        changes_made = []

        try:
            # Split text into paragraphs
            paragraphs = self._split_into_paragraphs(text)

            if len(paragraphs) < 2:
                processing_time = self._track_performance(start_time)
                return TransformationResult(
                    original_text=text,
                    transformed_text=text,
                    transformation_type="paragraph_reordering",
                    changes_made=["Not enough paragraphs to reorder"],
                    confidence_score=0.0,
                    processing_time=processing_time,
                    metadata={"paragraphs_count": len(paragraphs)}
                )

            # Determine reordering strategy
            if random.random() < self.config.paragraph_shuffle_probability:
                # Complete shuffle
                original_order = list(range(len(paragraphs)))
                shuffled_order = original_order.copy()
                random.shuffle(shuffled_order)

                reordered_paragraphs = [paragraphs[i] for i in shuffled_order]
                changes_made.append(f"Completely reordered {len(paragraphs)} paragraphs")
            else:
                # Partial reordering - swap adjacent paragraphs
                paragraphs_copy = paragraphs.copy()
                for i in range(0, len(paragraphs_copy) - 1, 2):
                    if random.random() < 0.5:
                        paragraphs_copy[i], paragraphs_copy[i + 1] = paragraphs_copy[i + 1], paragraphs_copy[i]
                        changes_made.append(f"Swapped paragraphs {i+1} and {i+2}")

                reordered_paragraphs = paragraphs_copy

            transformed_text = "\n\n".join(reordered_paragraphs)
            processing_time = self._track_performance(start_time)

            return TransformationResult(
                original_text=text,
                transformed_text=transformed_text,
                transformation_type="paragraph_reordering",
                changes_made=changes_made,
                confidence_score=len(changes_made) / max(len(paragraphs) - 1, 1),
                processing_time=processing_time,
                metadata={"paragraphs_count": len(paragraphs), "reordering_type": "shuffle"}
            )

        except Exception as e:
            self.logger.error(f"Error in paragraph reordering: {e}")
            processing_time = self._track_performance(start_time)
            return TransformationResult(
                original_text=text,
                transformed_text=text,
                transformation_type="paragraph_reordering",
                changes_made=[],
                confidence_score=0.0,
                processing_time=processing_time,
                metadata={"error": str(e)}
            )

    def _split_into_paragraphs(self, text: str) -> List[str]:
        """Split text into paragraphs"""
        # Split by double newlines, then clean up
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        return paragraphs

    def is_applicable(self, text: str) -> bool:
        """Check if paragraph reordering is applicable"""
        return len(self._split_into_paragraphs(text)) > 1


class IrrelevantContentInjectionStrategy(TransformationStrategy):
    """
    Irrelevant Content Injection Transformation Strategy

    Injects semantically neutral content that doesn't affect key conclusions.
    """

    def __init__(self, config: TransformationConfig):
        super().__init__(config)
        self.irrelevant_phrases = self._generate_irrelevant_phrases()

    def _generate_irrelevant_phrases(self) -> List[str]:
        """Generate a pool of semantically neutral phrases"""
        return [
            "It is worth noting that",
            "Interestingly enough",
            "As a matter of fact",
            "It should be mentioned that",
            "One might observe that",
            "It can be seen that",
            "It is important to recognize that",
            "As expected",
            "Not surprisingly",
            "In general terms",
            "Looking at the broader context",
            "From a different perspective",
            "Taking everything into account",
            "All things considered",
            "In the final analysis"
        ]

    def transform(self, text: str) -> TransformationResult:
        """Transform text by injecting irrelevant content"""
        start_time = time.time()
        changes_made = []

        try:
            # Calculate how much content to inject
            word_count = len(text.split())
            target_injection_words = int(word_count * self.config.irrelevant_content_ratio)

            if target_injection_words < 5:
                processing_time = self._track_performance(start_time)
                return TransformationResult(
                    original_text=text,
                    transformed_text=text,
                    transformation_type="irrelevant_content_injection",
                    changes_made=["Text too short for content injection"],
                    confidence_score=0.0,
                    processing_time=processing_time,
                    metadata={"target_injection_words": target_injection_words}
                )

            # Split text into sentences for injection points
            sentences = self._split_into_sentences(text)

            if len(sentences) < 3:
                processing_time = self._track_performance(start_time)
                return TransformationResult(
                    original_text=text,
                    transformed_text=text,
                    transformation_type="irrelevant_content_injection",
                    changes_made=["Not enough sentences for content injection"],
                    confidence_score=0.0,
                    processing_time=processing_time,
                    metadata={"sentences_count": len(sentences)}
                )

            # Inject content at random positions
            transformed_sentences = sentences.copy()
            injection_count = 0

            for i in range(1, len(transformed_sentences) - 1):
                if injection_count >= target_injection_words / 10:  # Average 10 words per injection
                    break

                if random.random() < 0.3:  # 30% chance to inject at each position
                    phrase = random.choice(self.irrelevant_phrases)
                    transformed_sentences.insert(i, phrase + ".")
                    changes_made.append(f"Injected phrase at position {i}")
                    injection_count += 1

            transformed_text = " ".join(transformed_sentences)
            processing_time = self._track_performance(start_time)

            return TransformationResult(
                original_text=text,
                transformed_text=transformed_text,
                transformation_type="irrelevant_content_injection",
                changes_made=changes_made,
                confidence_score=min(injection_count / (target_injection_words / 10), 1.0),
                processing_time=processing_time,
                metadata={"injection_count": injection_count, "target_injection_words": target_injection_words}
            )

        except Exception as e:
            self.logger.error(f"Error in irrelevant content injection: {e}")
            processing_time = self._track_performance(start_time)
            return TransformationResult(
                original_text=text,
                transformed_text=text,
                transformation_type="irrelevant_content_injection",
                changes_made=[],
                confidence_score=0.0,
                processing_time=processing_time,
                metadata={"error": str(e)}
            )

    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        # Simple sentence splitting - can be enhanced with NLP libraries
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        return sentences

    def is_applicable(self, text: str) -> bool:
        """Check if irrelevant content injection is applicable"""
        return len(text.split()) > 20  # Need enough text for meaningful injection


class TransformationFactory:
    """
    Factory Pattern for creating transformation strategies
    """

    @staticmethod
    def create_strategy(strategy_type: str, config: TransformationConfig) -> TransformationStrategy:
        """Create a transformation strategy based on type"""
        strategies = {
            "synonym_replacement": SynonymReplacementStrategy,
            "paragraph_reordering": ParagraphReorderingStrategy,
            "irrelevant_content_injection": IrrelevantContentInjectionStrategy
        }

        if strategy_type not in strategies:
            raise ValueError(f"Unknown transformation strategy: {strategy_type}")

        return strategies[strategy_type](config)

    @staticmethod
    def get_available_strategies() -> List[str]:
        """Get list of available transformation strategies"""
        return ["synonym_replacement", "paragraph_reordering", "irrelevant_content_injection"]