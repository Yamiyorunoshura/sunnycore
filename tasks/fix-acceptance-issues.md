**GOAL**: Fix issues identified during acceptance phase.

## [Input]
  1. "{CUTOVER}" --Cutover report (required)
  2. (Conditional) "{PRD}" --Product Requirements Document (if exists, used as primary requirement and architecture source)
  3. (Conditional) "{REQ}/*.md" --Requirement documents (optional, used if "PRD.md" does not exist)
  4. (Conditional) "{ARCH}/*.md" --Architecture documents (optional, used if "PRD.md" does not exist)
  5. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template (required)

## [Output]
  1. "{root}/docs/cutover-fixes-dev-notes.md" --Development notes for fixes (Markdown format)
  2. Fixed code implementation
  3. Updated documentation if needed
  4. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not leave any cutover issues unaddressed
  2. Do not skip TDD cycle for fixes (RED → GREEN → REFACTOR)
  3. Do not skip re-running acceptance tests after fixes
  4. Do not introduce new issues or break existing functionality
  5. Follow the Development-Guidelines defined in sunnycore_dev

## [Steps]
  1. Issue Analysis & Prioritization
    - Understand all reported issues from cutover report
    - Prioritize issues by severity and business impact
    - Create plan.md at "{root}/docs/plan.md" for progress tracking (this is the ONLY temporary tracking document)
    - Outcome: Issues prioritized and plan.md initialized

  2. Root Cause Analysis & Fix Strategy
    - Handle both PRD-based and Traditional project structures
    - Conduct complete root cause analysis for all issues
    - Document fix strategies for each issue in plan.md
    - Note: Record analysis in plan.md only; do NOT create separate analysis documents
    - Outcome: Root causes identified and fix strategies documented in plan.md

  3. Fix Planning & Risk Assessment
    - Create comprehensive fix plan for all issues
    - Complete risk assessment and component identification
    - Update plan.md with fix plan and risk assessment
    - Note: Record planning in plan.md only; do NOT create separate planning documents
    - Outcome: Detailed fix plan with risk assessment in plan.md

  4. RED Phase: Test Reproduction
    - Create failing tests that reproduce all issues
    - Execute tests and confirm RED status (tests fail as expected)
    - Update plan.md with RED phase progress (reproduction tests created, RED status verified)
    - Note: Do NOT create separate test result documents; record status in plan.md only
    - Outcome: All issues reproduced with failing tests, status recorded in plan.md

  5. GREEN Phase: Fix Implementation
    - Implement minimal code changes to pass tests
    - Follow architecture patterns and standards
    - Execute tests and verify all pass (exit code 0)
    - Update plan.md with GREEN phase progress (fixes implemented, test results)
    - Note: Do NOT create separate test result documents; record status in plan.md only
    - Outcome: All tests passing with fixes implemented, status recorded in plan.md

  6. REFACTOR Phase: Quality Improvement & Verification
    - Improve code quality while maintaining green tests
    - Execute tests after each refactoring to ensure they remain green
    - Re-run acceptance tests to confirm issues resolved
    - Update plan.md with REFACTOR phase progress (quality improvements, acceptance test results)
    - Note: Do NOT create separate test result documents; record status in plan.md only
    - Outcome: High-quality fixes with acceptance tests passing, status recorded in plan.md

  7. Documentation
    - Create complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md" following dev-notes-tmpl.yaml
    - Document all fixes, decisions, and risks
    - Note: cutover-fixes-dev-notes.md is the ONLY permanent documentation output; plan.md is temporary
    - Outcome: Comprehensive fix documentation completed

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Cutover report analysis (issues identified from cutover-report.md)
  - Issue prioritization:
    * Critical issues (list with descriptions)
    * High severity issues (list with descriptions)
    * Medium severity issues (list with descriptions)
    * Low severity issues (list with descriptions)
  - Root cause analysis for each issue:
    * Issue ID and description
    * Root cause identified
    * Affected components/files
    * Fix strategy (RED/GREEN/REFACTOR approach)
  - Fix implementation progress for each issue:
    * RED phase (reproduction test created, failing)
    * GREEN phase (fix implemented, tests passing)
    * REFACTOR phase (quality improvements, tests still passing)
    * Completion status (pending/in-progress/completed)
  - Risk assessment (low/medium/high risk for each fix)
  - Acceptance test re-run results:
    * Tests re-executed (list)
    * Issues resolved (verified yes/no)
    * New issues introduced (if any)
  - Overall fix progress (e.g., "Fixed 4/5 issues")
  - Development notes status (completed at {root}/docs/cutover-fixes-dev-notes.md)

## [DoD]
  - [ ] All issues resolved through full TDD cycle (RED → GREEN → REFACTOR) with all tests passing
  - [ ] Acceptance tests re-executed with all issues confirmed resolved
  - [ ] Complete development notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Example]

### Example 1: Push Notification Failure
[Input]
- Cutover report: docs/cutover-report.md (Critical: push notifications fail, missing FCM server key)
- PRD: docs/PRD.md (REQ-002: push notification delivery)
- Template: dev-notes-tmpl.yaml

[Decision]
- Root cause: Firebase config incomplete (no server key in .env)
- Fix strategy: Add FCM_SERVER_KEY to .env, update notification service
- RED: Write test for notification delivery (test_send_notification fails)
- GREEN: Add FCM config, implement send logic (test passes)
- REFACTOR: Add error handling, retry mechanism

[Expected Outcome]
- Fixed code: src/services/NotificationService.js with FCM integration, .env.example with FCM_SERVER_KEY
- docs/cutover-fixes-dev-notes.md documenting root cause, fix, test results
- Re-run acceptance test: Push notifications now work (✓)

### Example 2: Data Export Timeout
[Input]
- Cutover report: docs/cutover-report.md (High: CSV export times out for > 1000 rows)
- Requirements: docs/requirements/functional.md (REQ-003: export up to 10K rows)
- Architecture: docs/architecture/components.md (Export Service with in-memory processing)
- Template: dev-notes-tmpl.yaml

[Decision]
- Root cause: In-memory processing causes timeout for large datasets
- Fix strategy: Implement streaming export instead of loading all data
- RED: Write test for 10K row export with < 30s timeout (test fails)
- GREEN: Implement streaming CSV writer (test passes at 12s)
- REFACTOR: Add progress indicator, optimize database query

[Expected Outcome]
- Fixed code: src/services/ExportService.js with streaming implementation
- docs/cutover-fixes-dev-notes.md with performance comparison (before: timeout, after: 12s)
- Re-run acceptance: Export 10K rows successfully (✓)
