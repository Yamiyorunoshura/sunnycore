**GOAL**: Execute TDD development based on implementation plan.

## [Input]
- `{PLAN}/{task_id}-plan.md`
- `{ARCH}/*.md`
- `{TMPL}/dev-notes-tmpl.yaml`

## [Output]
- `{DEVNOTES}/{task_id}-dev-notes.md`
- High-quality code (tests passing, aligned with plan)
- Complete test coverage (unit + integration + behavior)

## [Constraints]
- **MUST** follow TDD cycle (RED→GREEN→REFACTOR), **MUST NOT** skip any phase
- **MUST** align with plan acceptance criteria and architecture, **MUST NOT** deviate without rationale
- **MUST** deliver with all tests passing (exit code 0), **MUST NOT** deliver failing tests
- **MUST** document out-of-scope changes in dev notes, **MUST NOT** modify files silently outside plan scope
- **MUST** follow [develop-guidelines], **MUST NOT** violate code quality standards

## [Instructions]

### 1. Planning and Context Gathering
Before writing any code, gather complete context:
- Read `{PLAN}/{task_id}-plan.md` thoroughly
- Read all relevant architecture documents from `{ARCH}/*.md`
- Understand acceptance criteria and Definition of Done
- Identify all files that will be created or modified

If you encounter **Blocking Conditions** (missing inputs, unexpected failures, risky actions, tools without non-interactive flags), HALT and request guidance.

### 2. RED Phase (Test First)
Implement ALL test cases BEFORE any production code:

**Test Coverage Must Include**:
- **Unit Tests**: Test individual functions/classes in isolation
  - Example: `test_article_title_validation()`, `test_article_save()`
- **Integration Tests**: Test component interactions
  - Example: `test_article_api_with_database()`, `test_article_service_integration()`
- **Behavior Tests**: Test end-to-end workflows (Given-When-Then)
  - Example: `test_create_article_workflow()`
- **Performance Tests** (if NFRs specified): Test performance requirements
  - Example: `test_report_generation_under_2_seconds()`

**Verification**: Execute tests and verify they ALL FAIL for the right reasons:
- Tests should fail because functionality doesn't exist yet
- NOT because tests are written incorrectly

**Exit Criteria**: All tests implemented and failing correctly (RED phase complete)

### 3. GREEN Phase (Minimal Implementation)
Implement the MINIMAL code to make tests pass:

**Focus**:
- Make tests pass with simplest possible implementation
- DO NOT add extra features or optimizations
- DO NOT worry about code quality yet (that's REFACTOR phase)
- Follow architecture specifications for component structure

**Verification**: Execute tests and verify ALL PASS (exit code 0)

**Exit Criteria**: All tests passing with minimal implementation (GREEN phase complete)

### 4. REFACTOR Phase (Quality Improvement)
Enhance code quality while maintaining green tests:

**Quality Improvements**:
- **SOLID Principles**: Extract classes, apply Single Responsibility
- **DRY**: Remove duplication, extract reusable functions
- **Error Handling**: Add comprehensive validation and error handling
- **Performance**: Apply optimizations (caching, indexing)
- **Security**: Implement input validation, sanitization
- **Observability**: Add logging, metrics, tracing

**Code Quality Standards**:
- Functions ≤ 50 lines
- Cyclomatic complexity ≤ 10
- Code coverage ≥ 80%
- No linter errors

**Verification**: After each refactoring step, re-run tests to ensure they STAY GREEN

**Exit Criteria**: High-quality code with tests still passing (REFACTOR phase complete)

### 5. Dev Notes Documentation
Create or update `{DEVNOTES}/{task_id}-dev-notes.md` following the template:

**Must Include**:
- **Implementation Summary**: What was built
- **TDD Progress**: RED → GREEN → REFACTOR phases with verification
- **Architecture Alignment**: How implementation follows architecture
- **Out-of-Scope Changes**: ANY files modified outside plan scope (with rationale)
- **Test Coverage**: Coverage percentage and key test scenarios
- **Known Issues**: Any limitations or technical debt
- **Performance Metrics**: If NFRs exist (e.g., "Report generation: 1.2s, target <2s ✓")

### 6. Acceptance Criteria Validation
Verify ALL acceptance criteria from the plan are met:
- Check each criterion individually
- Provide evidence (test results, performance metrics)
- Document any deviations with rationale

### 7. Quality Verification
Before marking complete, verify:
- [ ] All tests passing (exit code 0)
- [ ] Code quality standards met (SOLID, DRY, functions ≤50 lines)
- [ ] Test coverage ≥ 80%
- [ ] No linter errors
- [ ] Dev notes created/updated
- [ ] All acceptance criteria met

## [Blocking-Conditions]
HALT and request guidance if you encounter:
- **Missing Critical Inputs**: Plan file missing, architecture docs incomplete
- **Unexpected RED Failures**: Tests fail for wrong reasons (test bugs vs missing functionality)
- **Risky Irreversible Actions**: Database migrations, API breaking changes
- **Tools Lacking Non-Interactive Flags**: Commands that require user interaction

## [Steps]
1. Read plan + architecture, conceive solution. This ensures TDD phases are understood and outline documented.
2. **RED**: Implement all test cases, execute and verify they fail correctly. This ensures all tests are failing as expected.
3. **GREEN**: Minimal implementation aligned with architecture, execute tests. This ensures all tests passing (exit code 0).
4. **REFACTOR**: Enhance code quality, maintain green tests. This produces high-quality code with tests still passing.
5. Create or update `{DEVNOTES}/{task_id}-dev-notes.md`, validate acceptance criteria. This completes dev notes.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Full TDD cycle (RED→GREEN→REFACTOR) completed with all tests passing
- [ ] Code quality standards met (SOLID, DRY, functions ≤50 lines, coverage ≥80%)
- [ ] Dev notes exist at `{DEVNOTES}/{task_id}-dev-notes.md`

## [Example]

### Good #1
**Input**: Plan for article publishing (Express, PostgreSQL), template available  
**Decision**: Read plan. RED: write all tests (unit/integration/behavior), verify fail. GREEN: minimal code (Article model, API endpoints), all tests pass. REFACTOR: add validation + error handling + patterns, tests stay green. Update existing dev notes.  
**Why Good**: This executes full TDD cycle with verification at each phase, updates dev notes (not new file), and achieves 85% coverage meeting DoD.

### Good #2
**Input**: Transaction reports plan with NFR <2s query time (TimescaleDB)  
**Decision**: RED: write tests including performance <2s, verify fail. GREEN: minimal query + indexed columns, all pass (120ms). REFACTOR: add Redis caching + optimizations, tests green. Create new dev notes from template (doesn't exist).  
**Why Good**: This validates performance NFR explicitly, creates dev notes when needed, and tracking shows full TDD progression.

### Good #3
**Input**: User notification service plan (WebSocket, Redis pub/sub), architecture specifies event-driven pattern  
**Decision**: Read plan + arch. RED: write unit tests (event handlers), integration tests (Redis pub/sub), behavior tests (notification delivery), verify all fail correctly. GREEN: minimal WebSocket server + event handlers + Redis subscriber, all tests pass (exit code 0). REFACTOR: extract event bus pattern, add error recovery, tests stay green. Update existing dev notes with implementation.  
**Why Good**: This aligns with architecture (event-driven), completes full TDD cycle with verification, achieves 88% coverage (exceeds DoD 80%), and updates not creates dev notes.

### Bad #1
**Input**: Plan exists, need to implement  
**Bad Decision**: Skip RED. Code with optimizations immediately. Skip tests. No dev notes. Mark complete.  
**Why Bad**: This violates Constraint 1 (no TDD cycle), violates DoD (no passing tests, no dev notes), and delivers unverified implementation.  
**Correct**: Execute RED (all tests, verify fail). Then GREEN (minimal code, tests pass). Then REFACTOR (quality improvements). Finally create dev notes.

### Bad #2
**Input**: Task implementation with acceptance criteria  
**Bad Decision**: Deliver with failing tests. Modify out-of-scope files silently. Claim "self-documenting code". Create red-phase-result.md, green-phase-result.md separately.  
**Why Bad**: This violates Constraint 3 (exit code ≠ 0), Constraint 4 (no rationale for scope changes), DoD (no dev notes), and creates unnecessary files.  
**Correct**: Ensure exit code 0. Document all out-of-scope changes in dev notes. Always create/update dev notes. Use plan.md only for tracking (temporary).

### Bad #3
**Input**: API endpoint plan with security requirements (rate limiting, input validation)  
**Bad Decision**: Skip RED. Write implementation with all features (validation + rate limiting + caching + logging) at once. Run tests: 8/12 pass, 4 fail. Debug for hours. Give up, commit partial work. No dev notes "will document later".  
**Why Bad**: This violates Constraint 1 (no TDD cycle), implements everything at once instead of minimal GREEN, violates Constraint 3 (exit code ≠ 0), DoD violated (failing tests, no dev notes), and makes it unverifiable which piece failed.  
**Correct**: Execute RED: write all 12 tests, verify fail. Then GREEN: minimal implementation for JUST passing tests (no extra features). Then REFACTOR: add rate limiting, then caching, then logging one by one with tests green. Finally create dev notes with complete documentation.
