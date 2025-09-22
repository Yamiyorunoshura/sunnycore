import json
import time
from typing import Dict, List, Any, Optional, Union, Tuple
from datetime import datetime, timezone
import logging
import statistics
import hashlib


class LLMJudge:
    """
    LLM-as-Judge Evaluation System

    Implements automated evaluation using LLM-based judges to assess
    test case results with consistency and reliability measures.
    """

    def __init__(self, judge_model: str = "gpt-4", consistency_threshold: float = 0.8):
        """
        Initialize LLM Judge

        Args:
            judge_model: Model to use for judging (default: gpt-4)
            consistency_threshold: Threshold for consistency checking (default: 0.8)
        """
        self.judge_model = judge_model
        self.consistency_threshold = consistency_threshold
        self.logger = logging.getLogger(__name__)

        # Evaluation history for consistency tracking
        self.evaluation_history = []

    def evaluate_response(self, actual_response: str, expected_response: str,
                         test_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Evaluate a response against expected output using LLM judge

        Args:
            actual_response: Actual response from system
            expected_response: Expected response
            test_context: Additional context for evaluation

        Returns:
            Evaluation result dictionary
        """
        try:
            # Prepare evaluation prompt
            eval_prompt = self._create_evaluation_prompt(
                actual_response, expected_response, test_context
            )

            # Perform multiple evaluations for consistency
            evaluations = []
            for i in range(3):  # Triple evaluation for consistency
                eval_result = self._simulate_llm_evaluation(eval_prompt)
                evaluations.append(eval_result)
                time.sleep(0.1)  # Small delay between evaluations

            # Analyze consistency
            consistency_analysis = self._analyze_consistency(evaluations)

            # Determine final evaluation
            final_evaluation = self._determine_final_evaluation(
                evaluations, consistency_analysis
            )

            # Store evaluation history
            self._store_evaluation_history({
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'actual_response': actual_response,
                'expected_response': expected_response,
                'evaluations': evaluations,
                'consistency_analysis': consistency_analysis,
                'final_evaluation': final_evaluation
            })

            return {
                'success': True,
                'evaluation': final_evaluation,
                'consistency_score': consistency_analysis['consistency_score'],
                'confidence': consistency_analysis['confidence'],
                'evaluations': evaluations,
                'metadata': {
                    'judge_model': self.judge_model,
                    'evaluation_count': len(evaluations)
                }
            }

        except Exception as e:
            self.logger.error(f"Failed to evaluate response: {e}")
            return {
                'success': False,
                'error': str(e)
            }

    def _create_evaluation_prompt(self, actual_response: str, expected_response: str,
                                test_context: Optional[Dict[str, Any]] = None) -> str:
        """
        Create evaluation prompt for LLM judge

        Args:
            actual_response: Actual response to evaluate
            expected_response: Expected response
            test_context: Additional context

        Returns:
            Evaluation prompt string
        """
        prompt = f"""You are an expert evaluator for AI system responses. Please evaluate the following response:

EXPECTED RESPONSE:
{expected_response}

ACTUAL RESPONSE:
{actual_response}

"""

        if test_context:
            prompt += f"\nCONTEXT:\n{json.dumps(test_context, indent=2)}\n"

        prompt += """
Please evaluate this response on the following criteria:
1. **Accuracy**: Does the response contain the correct information?
2. **Completeness**: Does the response include all necessary information?
3. **Clarity**: Is the response clear and well-structured?
4. **Relevance**: Is the response relevant to the expected output?

Provide your evaluation in JSON format with the following structure:
{
  "accuracy_score": 0.0 to 1.0,
  "completeness_score": 0.0 to 1.0,
  "clarity_score": 0.0 to 1.0,
  "relevance_score": 0.0 to 1.0,
  "overall_score": 0.0 to 1.0,
  "explanation": "Brief explanation of your evaluation",
  "passed": true/false
}

Be objective and consistent in your evaluations.
"""

        return prompt

    def _simulate_llm_evaluation(self, prompt: str) -> Dict[str, Any]:
        """
        Simulate LLM evaluation (placeholder for actual LLM API call)

        Args:
            prompt: Evaluation prompt

        Returns:
            Simulated evaluation result
        """
        # This is a simulation - in production, this would call an actual LLM API
        # For now, we'll generate consistent but slightly varied results

        # Generate deterministic but varied results based on prompt hash
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
        base_score = int(prompt_hash[:8], 16) / (16**8)  # 0-1 range

        # Simulate variation between evaluations
        variation = 0.1 * (int(prompt_hash[8:10], 16) / 256 - 0.5)  # ±0.05 variation

        accuracy_score = max(0.0, min(1.0, base_score + variation))
        completeness_score = max(0.0, min(1.0, base_score + variation * 0.8))
        clarity_score = max(0.0, min(1.0, base_score + variation * 0.6))
        relevance_score = max(0.0, min(1.0, base_score + variation * 0.7))

        overall_score = (accuracy_score + completeness_score + clarity_score + relevance_score) / 4

        return {
            'accuracy_score': round(accuracy_score, 3),
            'completeness_score': round(completeness_score, 3),
            'clarity_score': round(clarity_score, 3),
            'relevance_score': round(relevance_score, 3),
            'overall_score': round(overall_score, 3),
            'explanation': f"Simulated evaluation with score {overall_score:.3f}",
            'passed': overall_score >= 0.7,  # 70% threshold
            'timestamp': datetime.now(timezone.utc).isoformat()
        }

    def _analyze_consistency(self, evaluations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze consistency across multiple evaluations

        Args:
            evaluations: List of evaluation results

        Returns:
            Consistency analysis dictionary
        """
        if len(evaluations) < 2:
            return {
                'consistency_score': 1.0,
                'confidence': 1.0,
                'consistent': True
            }

        # Calculate score variances
        score_types = ['accuracy_score', 'completeness_score', 'clarity_score', 'relevance_score', 'overall_score']
        variances = {}

        for score_type in score_types:
            scores = [eval[score_type] for eval in evaluations]
            if len(scores) > 1:
                variances[score_type] = statistics.variance(scores)

        # Calculate overall consistency (inverse of average variance)
        avg_variance = sum(variances.values()) / len(variances) if variances else 0
        consistency_score = max(0.0, 1.0 - avg_variance * 10)  # Scale variance to 0-1 range

        # Calculate confidence based on consistency
        confidence = consistency_score if consistency_score >= self.consistency_threshold else 0.0

        # Check pass/fail consistency
        passed_evaluations = [eval['passed'] for eval in evaluations]
        pass_consistency = len(set(passed_evaluations)) == 1  # All same result

        return {
            'consistency_score': round(consistency_score, 3),
            'confidence': round(confidence, 3),
            'consistent': consistency_score >= self.consistency_threshold,
            'pass_consistency': pass_consistency,
            'variances': variances,
            'evaluation_count': len(evaluations)
        }

    def _determine_final_evaluation(self, evaluations: List[Dict[str, Any]],
                                  consistency_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determine final evaluation based on multiple evaluations

        Args:
            evaluations: List of evaluation results
            consistency_analysis: Consistency analysis results

        Returns:
            Final evaluation dictionary
        """
        if not consistency_analysis['consistent']:
            # If inconsistent, use majority vote or middle value
            overall_scores = [eval['overall_score'] for eval in evaluations]
            final_score = statistics.median(overall_scores)

            # Determine pass/fail by majority
            passed_count = sum(1 for eval in evaluations if eval['passed'])
            final_passed = passed_count > len(evaluations) / 2

            confidence = consistency_analysis['confidence'] * 0.5  # Lower confidence for inconsistent results
        else:
            # If consistent, use average
            overall_scores = [eval['overall_score'] for eval in evaluations]
            final_score = statistics.mean(overall_scores)

            # All evaluations should agree on pass/fail
            final_passed = evaluations[0]['passed']

            confidence = consistency_analysis['confidence']

        # Calculate individual scores
        score_types = ['accuracy_score', 'completeness_score', 'clarity_score', 'relevance_score']
        final_scores = {}

        for score_type in score_types:
            scores = [eval[score_type] for eval in evaluations]
            final_scores[score_type] = round(statistics.mean(scores), 3)

        final_scores['overall_score'] = round(final_score, 3)

        return {
            'scores': final_scores,
            'passed': final_passed,
            'confidence': confidence,
            'determination_method': 'majority' if not consistency_analysis['consistent'] else 'consistent'
        }

    def _store_evaluation_history(self, evaluation_record: Dict[str, Any]):
        """
        Store evaluation record in history

        Args:
            evaluation_record: Complete evaluation record
        """
        self.evaluation_history.append(evaluation_record)

        # Keep only last 1000 evaluations to prevent memory issues
        if len(self.evaluation_history) > 1000:
            self.evaluation_history = self.evaluation_history[-1000:]

    def batch_evaluate(self, test_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Evaluate multiple test results

        Args:
            test_results: List of test result dictionaries

        Returns:
            Batch evaluation results
        """
        batch_results = {
            'evaluations': [],
            'summary': {},
            'performance_metrics': {}
        }

        start_time = time.time()

        try:
            for i, test_result in enumerate(test_results):
                self.logger.info(f"Evaluating test {i+1}/{len(test_results)}")

                evaluation = self.evaluate_response(
                    actual_response=str(test_result.get('actual_output', '')),
                    expected_response=str(test_result.get('expected_output', '')),
                    test_context=test_result.get('context')
                )

                batch_results['evaluations'].append({
                    'test_id': test_result.get('test_id', f'test_{i}'),
                    'evaluation': evaluation
                })

            # Calculate summary statistics
            batch_results['summary'] = self._calculate_batch_summary(batch_results['evaluations'])

            # Calculate performance metrics
            end_time = time.time()
            batch_results['performance_metrics'] = {
                'total_evaluations': len(test_results),
                'execution_time': round(end_time - start_time, 2),
                'average_time_per_evaluation': round((end_time - start_time) / len(test_results), 2)
            }

        except Exception as e:
            self.logger.error(f"Failed to complete batch evaluation: {e}")
            batch_results['error'] = str(e)

        return batch_results

    def _calculate_batch_summary(self, evaluations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate summary statistics for batch evaluation

        Args:
            evaluations: List of evaluation results

        Returns:
            Summary statistics dictionary
        """
        total_tests = len(evaluations)
        passed_tests = 0
        failed_tests = 0
        total_scores = []
        consistency_scores = []

        for eval_data in evaluations:
            evaluation = eval_data.get('evaluation', {})
            if evaluation.get('success', False):
                eval_result = evaluation.get('evaluation', {})
                if eval_result.get('passed', False):
                    passed_tests += 1
                else:
                    failed_tests += 1

                total_scores.append(eval_result.get('scores', {}).get('overall_score', 0.0))
                consistency_scores.append(evaluation.get('consistency_score', 0.0))

        return {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'pass_rate': passed_tests / total_tests if total_tests > 0 else 0.0,
            'average_score': statistics.mean(total_scores) if total_scores else 0.0,
            'average_consistency': statistics.mean(consistency_scores) if consistency_scores else 0.0,
            'min_score': min(total_scores) if total_scores else 0.0,
            'max_score': max(total_scores) if total_scores else 0.0
        }

    def get_evaluation_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about evaluation history

        Returns:
            Evaluation statistics dictionary
        """
        if not self.evaluation_history:
            return {'total_evaluations': 0}

        total_evaluations = len(self.evaluation_history)
        consistency_scores = [eval['consistency_analysis']['consistency_score']
                            for eval in self.evaluation_history]

        # Analyze pass rates
        passed_evaluations = 0
        for eval_record in self.evaluation_history:
            final_eval = eval_record.get('final_evaluation', {})
            if final_eval.get('passed', False):
                passed_evaluations += 1

        return {
            'total_evaluations': total_evaluations,
            'passed_evaluations': passed_evaluations,
            'pass_rate': passed_evaluations / total_evaluations,
            'average_consistency': statistics.mean(consistency_scores),
            'consistency_distribution': {
                'high': sum(1 for score in consistency_scores if score >= 0.9),
                'medium': sum(1 for score in consistency_scores if 0.7 <= score < 0.9),
                'low': sum(1 for score in consistency_scores if score < 0.7)
            }
        }

    def calibrate_judge(self, calibration_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calibrate the judge using known good/bad examples

        Args:
            calibration_data: List of calibration examples with known ratings

        Returns:
            Calibration results
        """
        calibration_results = {
            'examples': [],
            'accuracy_metrics': {},
            'adjustments': {}
        }

        try:
            for example in calibration_data:
                # Evaluate calibration example
                evaluation = self.evaluate_response(
                    actual_response=example['actual'],
                    expected_response=example['expected'],
                    test_context=example.get('context')
                )

                # Compare with known rating
                known_rating = example.get('rating', 0.0)
                evaluated_rating = evaluation.get('evaluation', {}).get('evaluation', {}).get('overall_score', 0.0)

                calibration_results['examples'].append({
                    'example_id': example.get('id', 'unknown'),
                    'known_rating': known_rating,
                    'evaluated_rating': evaluated_rating,
                    'difference': abs(known_rating - evaluated_rating),
                    'evaluation': evaluation
                })

            # Calculate accuracy metrics
            differences = [ex['difference'] for ex in calibration_results['examples']]
            calibration_results['accuracy_metrics'] = {
                'mean_absolute_error': statistics.mean(differences),
                'max_error': max(differences),
                'examples_within_0.1': sum(1 for d in differences if d <= 0.1),
                'examples_within_0.2': sum(1 for d in differences if d <= 0.2)
            }

            # Determine if adjustments are needed
            mae = calibration_results['accuracy_metrics']['mean_absolute_error']
            if mae > 0.15:  # If error is too high
                calibration_results['adjustments']['needed'] = True
                calibration_results['adjustments']['suggested_bias'] = statistics.mean(differences)
            else:
                calibration_results['adjustments']['needed'] = False

        except Exception as e:
            self.logger.error(f"Failed to calibrate judge: {e}")
            calibration_results['error'] = str(e)

        return calibration_results