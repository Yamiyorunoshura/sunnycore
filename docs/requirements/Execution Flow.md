## Execution Flow


### 1. Pipeline Execution
```bash
# Run spec-coding pipeline
python orchestrator.py \
  --input create-requirements.md \
  --output artifacts/{run_id}/
```

### 2. Contract Testing (Gate 1)
```bash
# Validate all artifacts against schemas
pytest tests/00_contract/ -v
# Must pass 100% to proceed
```

### 3. Behavior Testing (Gate 2)
```bash
# Run A/B testing and LLM-as-judge
promptfoo eval
# Run DeepEval assertions
pytest tests/10_behavior/ -v
```

### 4. Robustness & Security (Gate 3)
```bash
# Metamorphic testing
python tests/20_metamorphic/test_metamorphic.py
# Security testing
python tests/30_security/test_security.py
```

### 5. Retrieval Testing (Gate 4 - if applicable)
```bash
# RAG evaluation
python tests/40_retrieval/test_retrieval.py
```

### 6. CI Integration
```yaml
# .github/workflows/test-pipeline.yml
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run contract tests
        run: pytest tests/00_contract/
      - name: Run behavior tests
        run: pytest tests/10_behavior/
      - name: Run security tests
        run: python tests/30_security/test_security.py
      - name: Check quality gates
        run: python ci/quality-gates.py
```

