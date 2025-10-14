**GOAL**: Fix issues identified during PRD acceptance phase.

## [Input]
- `{CUTOVER}` (required)
- `{PRD}` (required)
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
2. Reference PRD for context, conduct root cause analysis, document strategies in dev notes/progress → Root causes identified with fix strategies documented
3. Create comprehensive fix plan with risk assessment based on PRD → Detailed fix plan with risk assessment documented
4. RED: Create failing tests reproducing issues, verify RED, record progress → All issues reproduced with failing tests, status recorded
5. GREEN: Implement minimal fixes to pass tests, verify all pass (exit code 0), record progress → All tests passing with fixes, status recorded
6. REFACTOR: Improve quality while maintaining green, re-run acceptance tests, record progress → High-quality fixes with acceptance tests passing, status recorded
7. Create complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md" → Comprehensive fix documentation completed

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All issues resolved through full TDD cycle with all tests passing
- [ ] Acceptance tests re-executed with all issues resolved
- [ ] Complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Example]

### Good #1
**Input**: Cutover shows critical: push notifications fail with "Invalid FCM token". PRD specifies REQ-002 for push notification delivery. Missing Firebase config  
**Decision**: Analyze issue (push notification failure)→Prioritize: critical→Reference PRD for REQ-002 context→Root cause: FCM_SERVER_KEY missing from env config→Fix strategy: add FCM config and implement notification logic→Document in plan.md→RED: write test_send_notification expecting successful delivery (fails with config error)→GREEN: add FCM_SERVER_KEY to .env, implement NotificationService.send() (test passes)→REFACTOR: add error handling, retry logic, logging (tests stay green)→Re-run acceptance for REQ-002 (push notifications deliver successfully)→Document comprehensive fix  
**Why Good**: Connects fix to PRD requirement, documents missing config, validates through TDD and acceptance testing

### Good #2
**Input**: Cutover lists 3 issues: critical auth failure, high-severity data validation missing, medium-severity UI inconsistency. PRD has relevant requirements  
**Decision**: Extract all 3 issues→Prioritize: critical (auth) first, then high (validation), then medium (UI)→Reference PRD for each requirement context→Root cause analysis for each in plan.md→Fix strategy: Issue 1 - fix token validation; Issue 2 - add input validation middleware; Issue 3 - update UI components→Execute sequentially following TDD for each→RED: failing tests for all 3→GREEN: implement fixes until pass→REFACTOR: improve quality→Re-run acceptance for all 3 requirements→Document all fixes comprehensively in single dev notes  
**Why Good**: Handles multiple issues with prioritized TDD cycles anchored in PRD requirements

### Bad #1
**Input**: Cutover shows critical notification failure. PRD has relevant requirement  
**Bad Decision**: Quickly implement notification service without tests first→Add FCM config→Test manually (works on first try)→Mark fixed without documentation→Skip re-running formal acceptance→Create minimal dev notes: "Fixed notifications. Added FCM."  
**Why Bad**: Violates TDD constraint (no RED phase proves issue existed), no test coverage for future regression, manual testing not systematic acceptance, minimal dev notes violate documentation requirements  
**Correct**: Full TDD: RED (write failing test proving notification failure)→GREEN (implement FCM integration until test passes)→REFACTOR (add error handling while keeping tests green)→Re-run formal acceptance matching PRD requirements→Document complete root cause analysis, fix implementation, risk assessment per dev-notes-tmpl.yaml
