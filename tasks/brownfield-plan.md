**GOAL**: Re-develop plan that failed review based on review feedback.

## [Input]
  1. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template
  2. "{REVIEW}/{task_id}-review.md" --Review report
  3. "{ARCH}/*.md" --Architecture design
  4. "{KNOWLEDGE}/*.md" --Project knowledge (if exist)
  5. "{TMPL}/plan-tmpl.yaml" --Unified planning template; populate sections with review issues, architecture impacts, and required validations for this task

## [Output]
  1. Fixed code that runs properly
  2. Updated development notes "{DEVNOTES}/{task_id}-dev-notes.md" (Markdown format)
  3. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not deliver fixes that fail to run properly
  2. Do not deviate from architecture design specifications
  3. Do not break existing functionality during fixes
  4. Follow the Development-Guidelines defined in sunnycore_dev

## [Steps]
  1. Issue Analysis & Planning
    - Understand issues from review report and architecture context
    - Formulate atomic fix tasks based on analysis
    - Create comprehensive plan.md at "{root}/docs/plan.md" using the plan template to track the working progress
    - Outcome: Clear understanding of issues, fix plan created, and plan.md initialized

  2. Test-Driven Fix Implementation
    - Establish progress tracking for fixes in plan.md
    - Implement fixes ensuring all tests pass (RED → GREEN → REFACTOR)
    - Execute tests and verify all pass after each phase
    - Update plan.md with implementation progress and test results
    - Note: Do NOT create separate phase result documents (red-phase-test-result.md, green-phase-test-result.md, etc.); record all status in plan.md only
    - Outcome: All unit tests and integration tests passing, status recorded in plan.md

  3. Documentation & Summary
    - Create comprehensive fix summary with evidence
    - Read existing development notes at "{DEVNOTES}/{task_id}-dev-notes.md"
    - Update existing dev notes with fix summary (do not create new file)
    - Note: Only update the existing dev-notes.md; plan.md is temporary and will be deleted
    - Outcome: Fix summary completed and development notes updated

## [DoD]
  - [ ] All unit and integration tests passed
  - [ ] Development notes updated
  - [ ] All the checkbox in plan.md are marked as done
  - [ ] plan.md is deleted

## [Example]

### Good Example 1
[INPUT]
Review report identifies: "Authentication token validation fails for expired tokens - test_expired_token_rejection failing"

[DECISION]
Read review report and identify specific test failure. Analyze architecture to understand JWT token expiry design. Create fix plan in plan.md: add expiry validation logic in TokenValidator before Redis lookup. Follow TDD: ensure test_expired_token_rejection fails (RED), implement expiry check (GREEN), optimize token parsing logic (REFACTOR).

[OUTCOME]
Fixed code with token expiry validation at src/auth/TokenValidator.js:L25-L30. All authentication tests passing. Updated docs/dev-notes/1-dev-notes.md with fix summary documenting the change, test evidence, and rollback plan. Issue fully resolved.

[WHY-GOOD]
- Treats the review feedback as the planning source, aligning fixes with architecture and TDD expectations before changing code.
- Provides verified tests and documentation updates, proving the regression is resolved and traceable.

### Good Example 2
[INPUT]
Review report shows: "Performance requirement NFR-001 violated - database query takes 3 seconds, requirement is under 500ms"

[DECISION]
Analyze architecture documents to understand database schema and query patterns. Review knowledge base for indexing best practices. Identify missing index on products.name column as root cause. Create migration script to add index. Test query performance to verify sub-500ms response. Document performance improvement in dev notes.

[OUTCOME]
Migration script at migrations/add_product_name_index.sql executed successfully. Query optimized in src/repositories/ProductRepository.js. Performance test now passes at 120ms. Updated docs/dev-notes/3-dev-notes.md with before/after performance metrics and migration details.

[WHY-GOOD]
- Diagnoses the performance issue through architecture and knowledge references, then applies a targeted fix compliant with constraints.
- Supplies measurable evidence and documentation, showing the improvement is validated and recorded for future teams.

### Bad Example 1
[INPUT]
Review report states: "User registration endpoint returns 500 error, test_create_user failing"

[BAD-DECISION]
Quickly patch the code with try-catch to suppress the error and return 200 status. Skip running tests to verify the fix. Mark the task as complete without investigating root cause or updating documentation.

[WHY-BAD]
Suppressing errors without fixing root cause violates Constraint 1 (deliver fixes that run properly). Not running tests violates DoD requirement. Skipping documentation prevents future debugging. This creates technical debt and may break other functionality.

[CORRECT-APPROACH]
Analyze the review report to identify the actual error (e.g., database constraint violation). Trace through architecture to understand expected behavior. Write failing test to reproduce issue (RED), implement proper fix addressing root cause (GREEN), add validation and error handling (REFACTOR). Execute all tests to verify, then update dev notes with fix details.

### Bad Example 2
[INPUT]
Review identifies three issues: missing validation, incorrect error codes, and failing integration test

[BAD-DECISION]
Only fix the failing integration test without addressing validation and error codes. Assume the other issues are "minor" and can be ignored. Update dev notes claiming all issues are fixed.

[WHY-BAD]
Violates Constraint 1 by not fixing all issues properly. Incomplete fixes leave the system in unstable state. Misleading documentation creates confusion for future work. Review-driven fixes must address all identified issues comprehensively.

[CORRECT-APPROACH]
Create plan.md listing all three issues with priorities. Address each systematically using TDD cycle. Track progress in plan.md: Issue 1 - validation (pending→in-progress→completed), Issue 2 - error codes (pending→in-progress→completed), Issue 3 - integration test (pending→in-progress→completed). Verify all tests pass. Update dev notes accurately reflecting all fixes applied.
