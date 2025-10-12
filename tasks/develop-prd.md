**GOAl**: Complete all development tasks based on PRD document in one iteration.

## [Input]
  1. "{PRD}" --Product Requirements Document
  2. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template

## [Output]
  1. "{root}/docs/prd-dev-notes.md" --Complete development notes document (Markdown format)
  2. High-quality, tested, refactored code implementation for all PRD tasks highly allign with the architecture design stated
  3. Complete test coverage and test cases
  4. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not leave any PRD tasks incomplete
  2. Do not skip TDD cycle (RED → GREEN → REFACTOR)
  3. Do not modify files outside PRD scope without recording rationale in dev notes
  4. Do not deliver with failing tests (exit code must be 0)
  5. Follow the Development-Guidelines defined in sunnycore_dev

## [Steps]
  1. Preparation & Strategy
    - Understand all PRD requirements and architecture completely
    - Develop comprehensive TDD implementation strategy
    - Create plan.md at "{root}/docs/plan.md" for progress tracking respecting task dependencies (this is the ONLY temporary tracking document)
    - Outcome: Complete strategy established and plan.md initialized

  2. TDD Development Cycle
    - RED: Write all tests, execute and ensure they fail with expected errors, update plan.md with RED phase status
    - GREEN: Implement minimal code to pass all tests, execute and verify all pass, update plan.md with GREEN phase status
    - REFACTOR: Improve code quality while maintaining green tests, execute tests to verify, update plan.md with REFACTOR phase status
    - Note: Do NOT create separate phase result documents (red-phase-test-result.md, green-phase-test-result.md, etc.); record all status in plan.md only
    - Outcome: All PRD features implemented with high quality, status recorded in plan.md

  3. Integration Testing & Validation
    - Execute complete test suite with all tests passing
    - Validate all PRD acceptance criteria met
    - Handle test failures with iterative fixes
    - Update plan.md with integration test results
    - Note: Record test results in plan.md only; do NOT create separate test result documents
    - Outcome: Full integration verified and acceptance criteria met, results recorded in plan.md

  4. Documentation
    - Create comprehensive development notes document following dev-notes-tmpl.yaml
    - Document all technical decisions and deviations
    - Note: prd-dev-notes.md is the ONLY permanent documentation output; plan.md is temporary
    - Outcome: Complete dev notes at "{root}/docs/prd-dev-notes.md"

  5. Final Verification
    - Verify all requirements satisfied with implementation
    - Confirm code quality and test coverage standards met (≥80%)
    - Outcome: All requirements delivered with quality standards met

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - PRD summary (all requirements and tasks from PRD.md)
  - TDD implementation strategy (task execution order, dependencies identified)
  - Development progress for each task:
    * Task ID and description
    * RED phase status (tests written, failing as expected)
    * GREEN phase status (minimal implementation, tests passing)
    * REFACTOR phase status (quality improvements, tests still passing)
    * Completion status (pending/in-progress/completed)
  - Overall implementation progress:
    * Tasks completed / total tasks
    * Requirements satisfied (list with status)
    * Files created/modified (list with file paths)
  - Integration testing results:
    * Test suite execution status (all passing: yes/no)
    * Test coverage achieved (percentage)
    * Integration issues encountered (if any)
  - Acceptance criteria validation (each criterion from PRD with met/not met status)
  - Code quality verification (SOLID, DRY, function length, coverage ≥80%)
  - Development notes status (completed at {root}/docs/prd-dev-notes.md)

## [Error-Handling]
  1. PRD file not found: Report error and halt execution
  2. Test failures in RED phase that don't fail correctly: Fix test logic and retry
  3. Test failures in GREEN phase: Analyze failure, fix implementation, retry
  4. Test failures in REFACTOR phase: Rollback refactoring, re-evaluate strategy
  5. Integration test failures: Identify root cause, fix specific implementation, re-run integration tests

## [DoD]
  - [ ] All PRD requirements implemented through full TDD cycle (RED → GREEN → REFACTOR) with all tests passing
  - [ ] Code quality meets standards (SOLID, DRY, functions ≤50 lines, coverage ≥80%)
  - [ ] Complete development notes at "{root}/docs/prd-dev-notes.md"

## [Example]

### Good Example 1
[INPUT]
PRD: docs/PRD.md with REQ-001 (update profile), REQ-002 (avatar upload), NFR-001 (<200ms response). Tasks: Task-1 (profile API), Task-2 (avatar storage). Template: dev-notes-tmpl.yaml.

[DECISION]
Step 1: Understand all PRD requirements and architecture. Develop strategy respecting task dependencies (Task-1→Task-2, avatar depends on profile). Create plan.md for progress tracking. Step 2 TDD RED: Write tests for PUT /profile, POST /profile/avatar; execute - all fail correctly. Update plan.md with RED status. Step 3 TDD GREEN: Implement profile update endpoint, S3 avatar upload; execute - all pass. Update plan.md with GREEN status. Step 4 TDD REFACTOR: Add input validation, optimize image processing. Execute tests - remain green. Update plan.md with REFACTOR status. Step 5: Create docs/prd-dev-notes.md documenting all tasks. Step 6: Validate all PRD acceptance criteria met.

[OUTCOME]
Code: src/api/profile.js, src/services/AvatarService.js, tests/ with all passing. docs/prd-dev-notes.md documenting complete implementation. All PRD acceptance criteria met. Integration tests pass. Coverage 87%. plan.md tracked complete progress.

### Good Example 2
[INPUT]
PRD: docs/PRD.md with REQ-001 (rate limit per user), NFR-001 (100 req/min), NFR-002 (Redis storage). Tasks: Task-1 (middleware), Task-2 (config), Task-3 (monitoring).

[DECISION]
Step 1: Read PRD completely, understand rate limiting requirements. Plan TDD strategy. Create plan.md. Step 2 RED: Write tests for rate limit enforcement, exceed limit scenario, reset after window. Execute - all fail. Record in plan.md. Step 3 GREEN: Implement Redis-based token bucket algorithm, Express middleware. Execute - all pass. Record in plan.md. Step 4 REFACTOR: Add configurable limits per endpoint, monitoring metrics. Tests stay green. Record in plan.md. Step 5: Document in prd-dev-notes.md with algorithm explanation. Step 6: Verify all NFRs (100 req/min enforced, monitoring functional).

[OUTCOME]
Code: src/middleware/rateLimiter.js, config/limits.json, tests/ all passing. docs/prd-dev-notes.md with rate limiting algorithm details. All NFRs verified (100 req/min enforced). Monitoring dashboard functional. Coverage 82%.

### Bad Example 1
[INPUT]
PRD with multiple tasks exists. Need to implement all.

[BAD-DECISION]
Implement only Task-1, skip Task-2 and Task-3. Skip TDD cycle entirely - write code without tests. Don't track progress in plan.md. Deliver with failing tests. No prd-dev-notes.md documentation. Claim all PRD tasks complete.

[WHY-BAD]
Violates Constraint 1 (leave PRD tasks incomplete). Violates Constraint 2 (skip TDD cycle). Violates Constraint 4 (deliver with failing tests). No progress tracking violates Steps. No documentation violates DoD. Incomplete implementation unusable.

[CORRECT-APPROACH]
Execute ALL Steps for ALL tasks in PRD. Step 1: Develop strategy covering ALL PRD tasks. Create plan.md. For each task: Step 2 RED (write tests, verify fail), Step 3 GREEN (minimal implementation, verify pass), Step 4 REFACTOR (quality improvements). Track ALL progress in plan.md. Step 5: Create comprehensive prd-dev-notes.md covering ALL tasks. Step 6: Verify ALL acceptance criteria met. Ensure exit code 0 before declaring complete.

### Bad Example 2
[INPUT]
PRD requirements documented. Tasks defined.

[BAD-DECISION]
Create separate phase result documents (red-results.md, green-results.md, refactor-results.md). Skip plan.md entirely. Modify files not in PRD scope without documentation. Test coverage only 45%. Claim complete without verifying all PRD criteria.

[WHY-BAD]
Creating separate phase result files violates Step instructions (use plan.md ONLY for tracking). No plan.md violates Steps 1-4. Modifying out-of-scope files without rationale violates Constraint 3. Coverage 45% fails DoD (≥80%). Not verifying acceptance criteria violates Step 6. Creates document clutter and incomplete work.

[CORRECT-APPROACH]
Use plan.md as THE ONLY temporary tracking document per Steps. Record ALL phase status (RED/GREEN/REFACTOR), test results, and progress in plan.md. Do NOT create separate result files. If modifying files outside PRD scope, document rationale in prd-dev-notes.md per Constraint 3. Achieve coverage ≥80% per DoD. Verify EVERY acceptance criterion from PRD before declaring complete. prd-dev-notes.md is permanent documentation, plan.md is temporary and deleted after.
