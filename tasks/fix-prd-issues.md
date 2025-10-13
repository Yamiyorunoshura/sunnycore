**GOAL**: Fix issues identified during acceptance phase.

## [Input]
  1. "{CUTOVER}" --Cutover report (required)
  2. "{PRD}" --Product Requirements Document (required, used as primary requirement and architecture source)
  3. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template (required)
  

## [Output]
  1. "{root}/docs/cutover-fixes-dev-notes.md" --Development notes for fixes (Markdown format)
  2. Fixed code implementation
  3. Updated documentation if needed
  

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
    - Record a short planning outline in the conversation (no standalone plan.md)
    - Outcome: Issues prioritized and plan outline documented

  2. Root Cause Analysis & Fix Strategy
    - Reference PRD for requirements and technical architecture context
    - Conduct complete root cause analysis for all issues
    - Document fix strategies for each issue in progress notes (conversation/dev notes)
    - Note: Keep analysis in dev notes/progress; do NOT create a separate plan.md
    - Outcome: Root causes identified and fix strategies documented

  3. Fix Planning & Risk Assessment
    - Create comprehensive fix plan for all issues
    - Complete risk assessment and component identification based on PRD
    - Record fix plan and risk assessment in dev notes/progress
    - Outcome: Detailed fix plan with risk assessment documented

  4. RED Phase: Test Reproduction
    - Create failing tests that reproduce all issues
    - Execute tests and confirm RED status (tests fail as expected)
    - Record RED phase progress (reproduction tests created, RED status verified) in dev notes/progress
    - Outcome: All issues reproduced with failing tests, status recorded

  5. GREEN Phase: Fix Implementation
    - Implement minimal code changes to pass tests
    - Follow architecture patterns and standards from PRD
    - Execute tests and verify all pass (exit code 0)
    - Record GREEN phase progress (fixes implemented, test results) in dev notes/progress
    - Outcome: All tests passing with fixes implemented, status recorded

  6. REFACTOR Phase: Quality Improvement & Verification
    - Improve code quality while maintaining green tests
    - Execute tests after each refactoring to ensure they remain green
    - Re-run acceptance tests to confirm issues resolved
    - Record REFACTOR phase progress (quality improvements, acceptance test results) in dev notes/progress
    - Outcome: High-quality fixes with acceptance tests passing, status recorded

  7. Documentation
    - Create complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md" following dev-notes-tmpl.yaml
    - Document all fixes, decisions, and risks
    - Note: cutover-fixes-dev-notes.md is the ONLY permanent documentation output
    - Outcome: Comprehensive fix documentation completed

## [DoD]
  - [ ] All issues resolved through full TDD cycle (RED → GREEN → REFACTOR) with all tests passing
  - [ ] Acceptance tests re-executed with all issues confirmed resolved
  - [ ] Complete development notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Example]

### Good Example 1
[INPUT]
Cutover report shows critical issue: push notifications fail with "Invalid FCM token" error. PRD specifies REQ-002 for push notification delivery. Missing Firebase configuration identified.

[DECISION]
Analyze issue from cutover report (push notification failure). Prioritize as critical. Reference PRD for requirements context (REQ-002). Root cause analysis: FCM_SERVER_KEY missing from environment configuration. Fix strategy: add FCM configuration and implement notification logic. Document in plan.md. RED phase: write test_send_notification that expects successful delivery (fails with config error). GREEN phase: add FCM_SERVER_KEY to .env, implement NotificationService.send() (test passes). REFACTOR phase: add error handling, retry logic, logging (tests remain green). Re-run acceptance test for REQ-002 (push notifications deliver successfully). Document comprehensive fix in dev notes.

[OUTCOME]
Fixed code at src/services/NotificationService.js with complete FCM integration. Environment updated: .env.example includes FCM_SERVER_KEY configuration. Complete dev notes at docs/cutover-fixes-dev-notes.md documenting root cause (missing config), solution (FCM integration), and verification. All tests passing. Acceptance test re-run: REQ-002 push notifications working. Plan.md shows TDD cycle completed (RED→GREEN→REFACTOR), acceptance verified.

[WHY-GOOD]
- Connects the fix back to the PRD requirement and documents the missing configuration, preventing repeat regressions.
- Validates through TDD and acceptance testing, leaving behind comprehensive evidence in dev notes.

### Good Example 2
[INPUT]
Cutover report lists 3 issues: critical authentication failure, high-severity data validation missing, medium-severity UI inconsistency. PRD contains relevant requirements for all issues.

[DECISION]
Extract all 3 issues from cutover report. Prioritize by severity: critical (auth failure) first, then high (validation), then medium (UI). Reference PRD for each issue's requirements context. Root cause analysis for each issue documented in plan.md. Fix strategy: Issue 1 - fix token validation logic; Issue 2 - add input validation middleware; Issue 3 - update UI components. Execute fixes sequentially following TDD for each. RED: create failing tests for all 3 issues. GREEN: implement fixes until tests pass. REFACTOR: improve code quality. Re-run acceptance tests for all 3 requirements. Document all fixes comprehensively in single dev notes file.

[OUTCOME]
Fixed code for all 3 issues: AuthService.js (token validation), ValidationMiddleware.js (input validation), UI components updated. Complete dev notes at docs/cutover-fixes-dev-notes.md documenting all 3 fixes with root causes, solutions, risk assessments. All tests passing. Acceptance tests re-run for all 3 requirements: all passing. Plan.md shows prioritized fixes, TDD cycles for each, acceptance tests verified. Single comprehensive documentation.

[WHY-GOOD]
- Handles multiple issues with prioritized TDD cycles anchored in PRD requirements, ensuring nothing is skipped.
- Consolidates documentation and acceptance evidence, giving stakeholders confidence that the cutover retry will pass.

### Bad Example 1
[INPUT]
Cutover report shows critical notification failure. PRD has relevant requirement. Fix seems straightforward.

[BAD-DECISION]
Quickly implement notification service without writing tests first. Add FCM configuration. Test manually by triggering notification (works on first try). Mark issue as fixed without documentation. Skip re-running formal acceptance tests because manual test worked. Create minimal dev notes: "Fixed notifications. Added FCM."

[WHY-BAD]
Violates Constraint 2 (do not skip TDD cycle). No RED phase means cannot prove issue existed. No test coverage for future regression prevention. Manual testing is not systematic acceptance testing. Violates Constraint 3 (do not skip re-running acceptance tests). Minimal dev notes violate Step 7 documentation requirements. Rushed fix lacks proper validation and documentation.

[CORRECT-APPROACH]
Follow full TDD cycle: RED - write failing test proving notification failure exists. GREEN - implement FCM integration until test passes. REFACTOR - add error handling while keeping tests green. Re-run formal acceptance tests matching PRD requirements. Document complete root cause analysis, fix implementation, risk assessment in dev notes per dev-notes-tmpl.yaml. Track all progress in plan.md. Never skip TDD steps or acceptance verification.

### Bad Example 2
[INPUT]
Cutover report shows 4 issues with different severity levels. PRD contains requirements for all.

[BAD-DECISION]
Start with the most interesting issue regardless of severity. Work on low-severity UI polish before fixing critical security vulnerability. Create separate dev notes files: fix1-dev-notes.md, fix2-dev-notes.md, etc. Update plan.md sporadically. Skip root cause analysis for "obvious" issues.

[WHY-BAD]
Violates Step 1 (prioritize by severity). Critical issues must be fixed first. Working on low-value issues while critical bugs remain is poor prioritization. Multiple dev notes files violate Output specification (single cutover-fixes-dev-notes.md). Sporadic plan.md updates violate progress tracking requirements. Skipping root cause analysis risks surface-level fixes that don't address underlying problems.

[CORRECT-APPROACH]
Prioritize ALL issues by severity in plan.md: critical first, then high, medium, low. Fix issues sequentially in priority order. Conduct thorough root cause analysis for EVERY issue regardless of apparent simplicity. Track each issue's TDD cycle progress in plan.md. Create single comprehensive dev notes at docs/cutover-fixes-dev-notes.md covering all fixes with complete analysis. Maintain detailed plan.md throughout per Progress-Tracking-Guidelines.
