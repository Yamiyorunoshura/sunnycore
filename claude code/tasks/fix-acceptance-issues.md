**GOAL**: Fix issues identified during acceptance phase.

## [Input]
  1. "{CUTOVER}" --Cutover report (required)
  2. (Conditional) "{PRD}" --Product Requirements Document (if exists, used as primary requirement and architecture source)
  3. (Conditional) "{REQ}/*.md" --Requirement documents (optional, used if "PRD.md" does not exist)
  4. (Conditional) "{ARCH}/*.md" --Architecture documents (optional, used if "PRD.md" does not exist)
  5. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template (required)

## [Output]
  1. "{root}/docs/cutover-fixes-dev-notes.md" --Development notes for fixes
  2. Fixed code implementation
  3. Updated documentation if needed

## [Constraints]
  1. Must address all issues documented in cutover report
  2. Must follow TDD cycle for fixes: write/update tests first (RED), implement fix (GREEN), then refactor (REFACTOR)
  3. Must verify fixes resolve the reported issues
  4. Development notes must preserve the indentation and numbering style used in the template
  5. Must re-run acceptance tests after fixes to ensure issues are resolved
  6. Must not introduce new issues or break existing functionality

## [Tools]
  1. **sequentialthinking (MCP)**: Perform structured reasoning and analysis
    - [Step 2: Analyze root causes; Step 3: Plan fix strategies; Step 6: Evaluate fix results]
  2. **todo_write**: Create and manage task list
    - [Step 1: Create todo list; Steps 2-7: Track task progress]
  3. **claude-context (MCP)**: Search codebase for relevant code
    - [Step 2: Locate code related to issues]

## [Steps]
  1. Preparation Phase
    - Understand all reported issues from cutover report
    - Ensure issues are prioritized by severity and business impact
    - Establish progress tracking mechanism for fixes

  2. Root Cause Analysis Phase
    - Ensure proper handling of both PRD-based and Traditional project structures
    - Achieve complete root cause analysis for all issues
    - Achieve documented fix strategies for each issue

  3. Fix Planning Phase
    - Achieve comprehensive fix plan for all issues
    - Ensure risk assessment and component identification are complete

  4. RED Phase: Test First
    - Achieve failing tests that properly reproduce all issues
    - Ensure RED status is confirmed through test execution

  5. GREEN Phase: Implement Fixes
    - Achieve passing tests through minimal code changes
    - Ensure all fixes follow architecture patterns and standards

  6. REFACTOR Phase: Improve and Verify
    - Achieve improved code quality while maintaining green tests
    - Ensure acceptance tests confirm all issues are resolved

  7. Documentation Phase
    - Achieve complete development notes at "{root}/docs/cutover-fixes-dev-notes.md"
    - Ensure all fixes, decisions, and risks are documented

## [Fix-Development-Guidelines]
  1. **TDD Fix Cycle (Mandatory)**
    - **RED Phase**: Write/update tests to reproduce each reported issue; verify tests fail correctly
    - **GREEN Phase**: Implement minimal fixes to pass tests (exit code 0); follow architecture patterns
    - **REFACTOR Phase**: Improve code quality while maintaining green tests; ensure no regressions
    - Rollback immediately if tests fail during refactoring; re-run acceptance tests after all fixes
  
  2. **Root Cause Analysis First**
    - Identify root cause for each issue before implementing fixes
    - Document fix strategy and risk assessment
    - Prioritize fixes by severity and business impact
  
  3. **Testing & Verification**
    - Minimum 80% coverage; critical logic requires 100%
    - Execute full test suite after every change; rollback on failures
    - Re-run all acceptance tests to confirm issues resolved
    - Ensure no new issues or regressions introduced

## [DoD]
  - [ ] Cutover report has been read and all issues identified
  - [ ] Root cause analysis completed for all issues
  - [ ] Fix strategy planned for each issue
  - [ ] Tests written/updated to catch all issues (RED phase)
  - [ ] All issues fixed and tests pass (GREEN phase)
  - [ ] Code refactored and quality improved (REFACTOR phase)
  - [ ] Full test suite passes with no regressions
  - [ ] Acceptance tests re-run and all issues resolved
  - [ ] Development notes generated with complete documentation

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

