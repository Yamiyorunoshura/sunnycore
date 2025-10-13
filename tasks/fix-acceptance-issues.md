**GOAL**: Fix issues identified during acceptance phase.

## [Input]
  1. "{CUTOVER}" --Cutover report (required)
  2. "{REQ}/*.md" --Requirement documents (required)
  3. "{ARCH}/*.md" --Architecture documents (required)
  4. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template (required)
  5. "{TMPL}/plan-tmpl.yaml" --Unified planning template; detail acceptance issues, fix strategies, and validation checkpoints for this task

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
    - Create comprehensive plan.md at "{root}/docs/plan.md" using the plan template to track the working progress
    - Outcome: Issues prioritized and plan.md initialized

  2. Root Cause Analysis & Fix Strategy
    - Reference requirement and architecture documents for context
    - Conduct complete root cause analysis for all issues
    - Document fix strategies for each issue in plan.md
    - Note: Record analysis in plan.md only; do NOT create separate analysis documents
    - Outcome: Root causes identified and fix strategies documented in plan.md

  3. Fix Planning & Risk Assessment
    - Create comprehensive fix plan for all issues
    - Complete risk assessment and component identification based on architecture documents
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
    - Follow architecture patterns and standards from architecture documents
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


## [DoD]
  - [ ] All issues resolved through full TDD cycle (RED → GREEN → REFACTOR) with all tests passing
  - [ ] Acceptance tests re-executed with all issues confirmed resolved
  - [ ] Complete development notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Example]

### Good Example 1
[INPUT]
Cutover report shows high-severity issue: CSV export times out for datasets over 1000 rows. Requirements specify support for up to 10K rows. Architecture shows Export Service uses in-memory processing.

[DECISION]
Analyze issue from cutover report (export timeout). Prioritize as high severity. Reference requirements (REQ-003: support 10K rows) and architecture (in-memory processing). Conduct root cause analysis: loading entire dataset into memory causes timeout. Fix strategy: implement streaming export. RED phase: write test for 10K row export with 30s timeout (test fails as expected). GREEN phase: implement streaming CSV writer (test passes at 12s). REFACTOR phase: add progress indicator, optimize database query (tests remain green). Re-run acceptance tests (export 10K rows successfully). Document complete fix in dev notes.

[OUTCOME]
Fixed code at src/services/ExportService.js with streaming implementation. Complete dev notes at docs/cutover-fixes-dev-notes.md documenting root cause (in-memory processing), solution (streaming), and performance improvement (12s vs timeout). All tests passing (TDD cycle completed). Acceptance tests re-run successfully: 10K row export works. Plan.md shows issue analyzed, TDD cycle completed (RED→GREEN→REFACTOR), acceptance verified.

[WHY-GOOD]
- Anchors the remediation in requirement expectations and architecture analysis, avoiding guesswork fixes.
- Executes the full TDD loop and acceptance retest, producing evidence that the regression is resolved.

### Good Example 2
[INPUT]
Cutover report identifies critical issue: push notifications fail with missing FCM server key error. Requirements specify push notification delivery. Two separate issues need fixing.

[DECISION]
Extract all issues from cutover report (2 issues: FCM config missing, notification payload validation missing). Prioritize by severity (both critical). Root cause analysis: Issue 1 - FCM_SERVER_KEY not in environment; Issue 2 - payload validation logic missing. Fix strategies documented in plan.md. RED phase: create tests reproducing both issues (both fail). GREEN phase: add FCM_SERVER_KEY to env, implement payload validation (tests pass). REFACTOR phase: add error handling and logging (tests remain green). Re-run acceptance tests for both issues (notifications deliver successfully, invalid payloads rejected). Document all fixes comprehensively.

[OUTCOME]
Fixed code: NotificationService.js with FCM integration and payload validation. Environment configuration: .env.example updated with FCM_SERVER_KEY. Complete dev notes at docs/cutover-fixes-dev-notes.md documenting both fixes with root causes, solutions, and risks. All tests passing. Acceptance tests verified: notifications work, validation prevents bad payloads. Plan.md shows both issues fixed through TDD, acceptance tests passed.

[WHY-GOOD]
- Handles multiple critical issues systematically, documenting severity, root causes, and fixes.
- Updates configuration and documentation alongside code, ensuring the deployment can succeed.

### Bad Example 1
[INPUT]
Cutover report shows critical issue: export timeout for large datasets. Requirements specify 10K row support.

[BAD-DECISION]
Skip TDD cycle. Directly implement streaming export without writing tests first. Test manually with 5K rows (works). Mark issue as fixed. Skip re-running acceptance tests. Generate dev notes quickly without documenting root cause analysis.

[WHY-BAD]
Violates Constraint 2 (do not skip TDD cycle). No RED phase means cannot verify issue reproduction. No test coverage means future regressions possible. Manual testing only 5K rows does not verify 10K requirement. Violates Constraint 3 (do not skip re-running acceptance tests). Incomplete dev notes violate Step 7 documentation requirements. Rushed fix lacks quality assurance.

[CORRECT-APPROACH]
Follow full TDD cycle: RED phase - write test for 10K rows that fails initially proving issue exists. GREEN phase - implement streaming export until test passes. REFACTOR phase - improve code quality while keeping tests green. Re-run acceptance tests with actual 10K row dataset per requirements. Document complete root cause analysis, fix strategy, and performance metrics in dev notes. Never skip TDD steps or acceptance verification.

### Bad Example 2
[INPUT]
Cutover report lists 5 issues ranging from critical to low severity. All need fixing.

[BAD-DECISION]
Start fixing low-severity issues first because they seem easier. Fix issues randomly without prioritization. Work on multiple issues simultaneously. Create separate dev notes for each issue (5 files). Leave plan.md empty because "the fixes speak for themselves."

[WHY-BAD]
Violates Step 1 (prioritize by severity). Should fix critical issues first to maximize business impact. Random order wastes time on low-value fixes while critical issues remain. Multiple simultaneous fixes increases complexity and error risk. Creating 5 separate dev notes violates Output specification (single cutover-fixes-dev-notes.md). Empty plan.md violates progress tracking requirements. Unstructured approach lacks discipline.

[CORRECT-APPROACH]
Prioritize ALL issues by severity in plan.md: critical first, then high, medium, low. Fix issues sequentially in priority order. Track each issue's progress through TDD cycle in plan.md. Create single comprehensive dev notes at docs/cutover-fixes-dev-notes.md covering all fixes. Document root cause, fix strategy, and risk assessment for each issue. Maintain plan.md throughout with detailed progress tracking per Progress-Tracking-Guidelines.
