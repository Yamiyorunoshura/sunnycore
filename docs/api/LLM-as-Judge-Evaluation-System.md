# LLM-as-Judge Evaluation System API Documentation

## Overview

The LLM-as-Judge Evaluation System provides comprehensive automated evaluation capabilities for AI-generated content, integrating multiple evaluation frameworks including Promptfoo and DeepEval to ensure consistent, high-quality outputs.

## Architecture

### Core Components

1. **Golden Set Manager** (`src/behavior/golden_set_manager.py`)
2. **Promptfoo Integration** (`src/behavior/promptfoo_integration.py`)
3. **DeepEval Integration** (`src/behavior/deepeval_integration.py`)
4. **Architecture Validator** (`src/behavior/architecture_validator.py`)
5. **Requirement Mapper** (`src/behavior/requirement_mapper.py`)

### Data Flow

```
Golden Set → Promptfoo Evaluation → DeepEval Validation → Architecture Alignment → Requirement Coverage
```

## Installation

```bash
pip install -r requirements.txt
pip install promptfoo deepeval pytest pytest-benchmark
```

## Quick Start

### Basic Usage

```python
from src.behavior.golden_set_manager import GoldenSetManager
from src.behavior.promptfoo_integration import PromptfooIntegration
from src.behavior.deepeval_integration import DeepEvalIntegration

# Initialize components
golden_set = GoldenSetManager()
promptfoo = PromptfooIntegration()
deepeval = DeepEvalIntegration()

# Add test case to Golden Set
test_case = {
    "id": "test_001",
    "description": "Basic functionality test",
    "input": {"prompt": "What is the capital of France?"},
    "expected_output": {"response": "Paris"},
    "metadata": {"category": "geography", "difficulty": "easy"}
}

golden_set.add_test_case(test_case)

# Run evaluation
evaluation_result = promptfoo.run_evaluation([test_case])
print(f"Evaluation success: {evaluation_result['success']}")
```

### Advanced Usage with Architecture Validation

```python
from src.behavior.architecture_validator import ArchitectureValidator
from src.behavior.requirement_mapper import RequirementMapper

# Define architecture specification
architecture_spec = {
    "components": [
        {"id": "component_1", "type": "business"},
        {"id": "component_2", "type": "business"}
    ],
    "data_flows": [
        {"source": "component_1", "target": "component_2", "data_type": "data"}
    ]
}

# Validate architecture alignment
validator = ArchitectureValidator(target_f1_score=0.9)
validation_results = validator.validate_architecture_alignment(
    actual_implementation=actual_impl,
    expected_architecture=architecture_spec
)

print(f"F1 Score: {validation_results['f1_score']['f1_score']}")
print(f"Meets target: {validation_results['meets_target']}")
```

## API Reference

### GoldenSetManager

#### Constructor

```python
GoldenSetManager(storage_path: Optional[str] = None)
```

**Parameters:**
- `storage_path`: Path to Golden Set storage file (default: "golden_set.json")

#### Methods

##### `add_test_case(test_case: Dict[str, Any]) -> bool`

Add a test case to the Golden Set.

**Parameters:**
- `test_case`: Dictionary containing test case data

**Returns:**
- `bool`: True if successfully added

**Example:**
```python
test_case = {
    "id": "unique_test_id",
    "description": "Test description",
    "input": {"prompt": "Your prompt here"},
    "expected_output": {"response": "Expected response"},
    "metadata": {"category": "test_category", "difficulty": "easy"}
}

success = golden_set.add_test_case(test_case)
```

##### `validate_test_case(test_case_id: str) -> Dict[str, Any]`

Validate a specific test case.

**Parameters:**
- `test_case_id`: Unique identifier for the test case

**Returns:**
- `Dict`: Validation results including validity status and issues

##### `validate_golden_set() -> Dict[str, Any]`

Validate all test cases in the Golden Set.

**Returns:**
- `Dict`: Comprehensive validation results

##### `get_test_case(test_case_id: str) -> Optional[Dict[str, Any]]`

Retrieve a specific test case.

**Parameters:**
- `test_case_id`: Test case identifier

**Returns:**
- `Optional[Dict]`: Test case data or None if not found

##### `get_all_test_cases() -> List[Dict[str, Any]]`

Get all test cases in the Golden Set.

**Returns:**
- `List[Dict]`: List of all test cases

##### `remove_test_case(test_case_id: str) -> bool`

Remove a test case from the Golden Set.

**Parameters:**
- `test_case_id`: Test case identifier

**Returns:**
- `bool`: True if successfully removed

##### `calculate_coverage() -> Dict[str, Any]`

Calculate test coverage metrics.

**Returns:**
- `Dict`: Coverage analysis results

### PromptfooIntegration

#### Constructor

```python
PromptfooIntegration(config_path: Optional[str] = None)
```

**Parameters:**
- `config_path`: Path to Promptfoo configuration file

#### Methods

##### `generate_promptfoo_config(test_cases: List[Dict[str, Any]]) -> Dict[str, Any]`

Generate Promptfoo configuration from test cases.

**Parameters:**
- `test_cases`: List of test cases

**Returns:**
- `Dict`: Promptfoo configuration

##### `run_evaluation(test_cases: List[Dict[str, Any]], config: Optional[Dict] = None) -> Dict[str, Any]`

Run Promptfoo evaluation.

**Parameters:**
- `test_cases`: List of test cases to evaluate
- `config`: Optional custom configuration

**Returns:**
- `Dict`: Evaluation results

##### `calculate_quality_metrics(evaluation_results: Dict[str, Any]) -> Dict[str, Any]`

Calculate quality metrics from evaluation results.

**Parameters:**
- `evaluation_results`: Results from Promptfoo evaluation

**Returns:**
- `Dict`: Quality metrics including scores and analysis

### DeepEvalIntegration

#### Constructor

```python
DeepEvalIntegration(config_path: Optional[str] = None, test_dir: Optional[str] = None)
```

**Parameters:**
- `config_path`: Path to DeepEval configuration file
- `test_dir`: Directory for DeepEval test files

#### Methods

##### `generate_architecture_tests(architecture_spec: Dict[str, Any]) -> str`

Generate architecture validation tests.

**Parameters:**
- `architecture_spec`: Architecture specification

**Returns:**
- `str`: Path to generated test file

##### `run_deepeval_tests(test_file_path: Optional[str] = None) -> Dict[str, Any]`

Run DeepEval tests using pytest.

**Parameters:**
- `test_file_path`: Specific test file to run (optional)

**Returns:**
- `Dict`: Test execution results

##### `calculate_f1_score(test_results: Dict[str, Any], architecture_mapping: Dict[str, Any]) -> Dict[str, Any]`

Calculate F1 score for architecture alignment.

**Parameters:**
- `test_results`: Test execution results
- `architecture_mapping`: Architecture component mapping

**Returns:**
- `Dict`: F1 score calculation results

##### `validate_requirement_mapping(test_results: Dict[str, Any], requirements: Dict[str, Any]) -> Dict[str, Any]`

Validate requirement mapping coverage.

**Parameters:**
- `test_results`: Test execution results
- `requirements`: Requirements specification

**Returns:**
- `Dict`: Requirement validation results

### ArchitectureValidator

#### Constructor

```python
ArchitectureValidator(target_f1_score: float = 0.9)
```

**Parameters:**
- `target_f1_score`: Target F1 score for validation (default: 0.9)

#### Methods

##### `validate_architecture_alignment(actual_implementation: Dict[str, Any], expected_architecture: Dict[str, Any]) -> Dict[str, Any]`

Validate architecture alignment between implementation and specification.

**Parameters:**
- `actual_implementation`: Actual implementation structure
- `expected_architecture`: Expected architecture specification

**Returns:**
- `Dict`: Validation results with F1 score

##### `load_architecture_spec(spec_path: str) -> Dict[str, Any]`

Load architecture specification from file.

**Parameters:**
- `spec_path`: Path to architecture specification file

**Returns:**
- `Dict`: Architecture specification dictionary

##### `generate_architecture_report(validation_results: Dict[str, Any]) -> str`

Generate human-readable architecture validation report.

**Parameters:**
- `validation_results`: Validation results

**Returns:**
- `str`: Formatted report string

### RequirementMapper

#### Constructor

```python
RequirementMapper(requirements_path: Optional[str] = None)
```

**Parameters:**
- `requirements_path`: Path to requirements specification file

#### Methods

##### `analyze_implementation_coverage(implementation_files: List[str]) -> Dict[str, Any]`

Analyze implementation files for requirement coverage.

**Parameters:**
- `implementation_files`: List of implementation file paths

**Returns:**
- `Dict`: Coverage analysis results

##### `map_tests_to_requirements(test_files: List[str]) -> Dict[str, Any]`

Map test files to requirements.

**Parameters:**
- `test_files`: List of test file paths

**Returns:**
- `Dict`: Test mapping results

##### `validate_requirement_coverage(threshold: float = 0.8) -> Dict[str, Any]`

Validate requirement coverage against threshold.

**Parameters:**
- `threshold`: Coverage threshold (default: 0.8)

**Returns:**
- `Dict`: Validation results

## Configuration

### Golden Set Configuration

```json
{
  "version": "1.0",
  "metadata": {
    "created": "2025-01-01T00:00:00Z",
    "description": "Golden Set for behavior testing"
  },
  "test_cases": [
    {
      "id": "test_001",
      "description": "Basic functionality test",
      "input": {"prompt": "What is the capital of France?"},
      "expected_output": {"response": "Paris"},
      "metadata": {
        "category": "geography",
        "difficulty": "easy",
        "tags": ["basic", "geography"]
      }
    }
  ]
}
```

### Promptfoo Configuration

```yaml
default_model: "gpt-4"
evaluation_params:
  max_concurrent: 5
  timeout: 30
  temperature: 0.1
metrics:
  - answer_relevancy
  - faithfulness
  - contextual_recall
  - contextual_precision
```

### DeepEval Configuration

```yaml
default_model: "gpt-4"
evaluation_params:
  max_concurrent: 5
  timeout: 30
  temperature: 0.1
custom_metrics:
  architecture_alignment:
    type: custom
    description: "Evaluates alignment with system architecture"
  requirement_coverage:
    type: custom
    description: "Evaluates coverage of specified requirements"
```

## Error Handling

The system provides comprehensive error handling with detailed error messages:

```python
try:
    result = golden_set.add_test_case(invalid_test_case)
except ValueError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Common Error Codes

- `INVALID_TEST_CASE`: Test case fails validation
- `FILE_NOT_FOUND`: Required file not found
- `CONFIG_ERROR`: Configuration parsing error
- `EVALUATION_FAILED`: Evaluation process failed
- `VALIDATION_ERROR`: Architecture validation failed

## Performance Considerations

### Optimization Tips

1. **Batch Processing**: Process multiple test cases together when possible
2. **Caching**: Enable caching for repeated evaluations
3. **Parallel Execution**: Use concurrent evaluation for large test sets
4. **Memory Management**: Clean up temporary files and data structures

### Performance Metrics

- Golden Set validation: < 3 seconds for 100 test cases
- Promptfoo evaluation: < 5 seconds per test case
- DeepEval validation: < 2 seconds for architecture alignment
- F1 score calculation: < 1 second for complex architectures

## Testing

### Unit Tests

```bash
python -m pytest tests/test_golden_set.py -v
python -m pytest tests/test_promptfoo_integration.py -v
python -m pytest tests/test_deepeval_integration.py -v
```

### Integration Tests

```bash
python -m pytest tests/test_behavior_integration.py -v
```

### Performance Tests

```bash
python -m pytest tests/ --benchmark-only
```

## Best Practices

### 1. Test Case Design

- Use clear, descriptive test case IDs
- Include comprehensive metadata for categorization
- Provide both simple and complex test scenarios
- Ensure expected outputs are specific and verifiable

### 2. Architecture Validation

- Define clear architecture specifications
- Use consistent component naming conventions
- Include comprehensive interface definitions
- Validate both structure and behavior

### 3. Requirement Mapping

- Use standardized requirement identifiers (e.g., F-001, NFR-001)
- Include requirement references in code comments
- Maintain traceability between requirements and implementation
- Regularly update requirement mappings

### 4. Performance Monitoring

- Monitor key performance metrics regularly
- Set up alerts for performance degradation
- Optimize based on usage patterns
- Use benchmarking to track improvements

## Troubleshooting

### Common Issues

**Golden Set validation fails**
- Check test case format and required fields
- Verify test case ID uniqueness
- Ensure expected outputs are properly structured

**Promptfoo evaluation fails**
- Verify Promptfoo installation and configuration
- Check model API credentials and access
- Ensure test cases are properly formatted

**DeepEval integration fails**
- Verify DeepEval installation and dependencies
- Check test directory permissions
- Ensure architecture specifications are valid

**Architecture validation fails**
- Verify architecture specification format
- Check component and interface definitions
- Ensure data flows are properly defined

### Debug Mode

Enable debug logging for detailed troubleshooting:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Your code here
```

## Contributing

1. Follow the established coding standards
2. Add comprehensive tests for new features
3. Update documentation for API changes
4. Ensure all quality gates pass before submitting

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the GitHub repository
- Refer to the troubleshooting section
- Check the existing documentation and examples