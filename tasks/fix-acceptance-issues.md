**GOAL**: Fix issues identified during acceptance phase.

## [Input]
- `{CUTOVER}` (required)
- `{REQ}/*.md` (required)
- `{ARCH}/*.md` (required)
- `{TMPL}/dev-notes-tmpl.yaml` (required)

## [Output]
- `{root}/docs/cutover-fixes-dev-notes.md`
- Fixed code
- Updated documentation if needed

## [Constraints]
- **MUST** address all cutover issues, **MUST NOT** leave any unaddressed
- **MUST** follow TDD cycle for fixes (RED→GREEN→REFACTOR), **MUST NOT** skip
- **MUST** re-run acceptance tests after fixes, **MUST NOT** skip
- **MUST** not introduce new issues or break existing functionality, **MUST NOT** cause regressions

## [Steps]
1. Understand all issues, prioritize by severity → Issues prioritized
2. Reference req and arch, conduct root cause analysis, document in plan.md → Root causes identified with fix strategies in plan.md
3. Create comprehensive fix plan with risk assessment in plan.md → Detailed fix plan with risk assessment in plan.md
4. RED: Create failing tests reproducing issues, verify RED, update plan.md → All issues reproduced with failing tests, status in plan.md
5. GREEN: Implement minimal fixes to pass tests, verify all pass (exit code 0), update plan.md → All tests passing with fixes, status in plan.md
6. REFACTOR: Improve quality while maintaining green, re-run acceptance tests, update plan.md → High-quality fixes with acceptance tests passing, status in plan.md
7. Create complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md" → Comprehensive fix documentation completed

## [DoD]
- [ ] All issues resolved through full TDD cycle with all tests passing
- [ ] Acceptance tests re-executed with all issues resolved
- [ ] Complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Example]

### Good #1
**Input**: Cutover shows high-severity: CSV export times out for >1000 rows. Requirements specify 10K rows. Architecture shows in-memory processing  
**Decision**: Analyze issue (export timeout)→Prioritize: high severity→Reference REQ-003 (10K rows) and arch (in-memory)→Root cause: loading entire dataset into memory causes timeout→Fix strategy: streaming export→RED: write test for 10K row export with 30s timeout (fails)→GREEN: implement streaming CSV writer (passes at 12s)→REFACTOR: add progress indicator, optimize query (tests stay green)→Re-run acceptance (10K rows successfully)→Document fix  
**Why Good**: Anchors in requirement and architecture analysis, executes full TDD and acceptance retest, produces evidence

### Good #2
**Input**: Cutover identifies critical: push notifications fail with missing FCM key. Two separate issues  
**Decision**: Extract all issues (2 issues: FCM config missing, payload validation missing)→Prioritize both critical→Root cause: Issue 1 - FCM_SERVER_KEY not in env; Issue 2 - payload validation missing→Strategies in plan.md→RED: tests reproducing both (both fail)→GREEN: add FCM_SERVER_KEY to env, implement validation (tests pass)→REFACTOR: error handling and logging (tests stay green)→Re-run acceptance for both (notifications deliver, invalid payloads rejected)→Document all  
**Why Good**: Handles multiple critical issues systematically, updates config and documentation alongside code

### Bad #1
**Input**: Cutover shows critical: export timeout for large datasets. Requirements specify 10K support  
**Bad Decision**: Skip TDD→Directly implement streaming without tests first→Test manually with 5K rows (works)→Mark fixed→Skip re-running acceptance tests→Generate quick dev notes without root cause  
**Why Bad**: Violates TDD constraint, no RED phase proves issue exists, no test coverage for future regressions, manual testing only 5K not verifying 10K requirement, skips acceptance re-run  
**Correct**: Full TDD: RED (write test for 10K rows, fails proving issue exists)→GREEN (implement streaming until passes)→REFACTOR (improve while keeping green)→Re-run acceptance with actual 10K dataset→Document complete root cause analysis and metrics
