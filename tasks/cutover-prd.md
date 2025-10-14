**GOAL**: Execute project acceptance validating deliverables from business and user perspectives.

## [Input]
- `{PRD}` (required)
- `{TMPL}/cutover-report-tmpl.yaml` (required)

## [Output]
- `{CUTOVER}`

## [Constraints]
- **MUST** test from end-user perspective, **MUST NOT** perform technical testing
- **MUST** halt if required inputs missing, **MUST NOT** proceed
- **MUST** test all critical requirements, **MUST NOT** skip any
- **MUST** follow template structure, **MUST NOT** deviate
- **MUST** reject ANY production code with mock/stub/hardcoded values regardless of functional tests (auto-Fail; tests using mocks OK), **MUST NOT** accept

## [Steps]
1. Understand business objectives and architecture from PRD → Business objectives and architecture understood
2. **CRITICAL**: Scan ALL production code for mock/stub/placeholder/hardcoded values (auto-fail if found; tests using mocks OK) → Code quality verified
3. Identify configuration needs, document requirements → Configuration requirements documented
4. Configure environment, document setup steps → Environment configured and ready
5. Run project, verify functionality with logs → Project running with verified functionality
6. Test all critical business requirements from end-user perspective → Complete acceptance test results documented
7. Generate cutover report, determine status (Success/Partial Success/Failed) → Complete cutover report with clear status

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Production code scanned, NO mock/stub/hardcoded values (tests using mocks OK)
- [ ] All critical business requirements tested from end-user perspective with results recorded
- [ ] Complete cutover report at "{CUTOVER}" with status and rationale
- [ ] All issues documented with severity and reproduction steps

## [Example]

### Good #1
**Input**: PRD has 3 requirements (login, push notifications, offline). Code scan passes. App runs but push notifications fail (missing Firebase config)  
**Decision**: Validate PRD exists→Extract objectives from PRD→Scan production code for mocks/hardcoded (none found, passed)→Identify config needs→Setup: install Expo+Firebase→Run: expo start (launches)→Test: REQ-001 login (pass), REQ-002 push notifications (fail - FCM server key missing), REQ-003 offline (pass)→Document issue severity: Critical→Record reproduction→Status: Partial Success (2/3)  
**Why Good**: Executes entire checklist from code scan to requirement validation before verdict, captures precise diagnostics

### Good #2
**Input**: PRD has payment processing. Code scan reveals mock with hardcoded API key in PaymentService.js production code. Unit tests properly use jest.mock()  
**Decision**: Scan all production code before functional testing→Detect mock at PaymentService.js:L42 with TODO and hardcoded key→Verify unit tests use mocks (acceptable)→AUTOMATIC FAIL per constraint (production code has mock/hardcoded)→HALT functional testing→Document critical findings with excerpts→Generate cutover: Failed→Provide action items: implement real gateway, externalize secrets, remove TODOs  
**Why Good**: Enforces automatic-fail rules rigorously, halts delivery when production code unsafe, provides actionable remediation

### Bad #1
**Input**: PRD exists. Code has mocks but functional tests pass  
**Bad Decision**: Scan finds mocks but tests pass so mark Success→Reasoning: "Tests work, so it's ready"  
**Why Bad**: Violates constraint (ANY mock/stub in production→auto-fail). Code quality gate CRITICAL, overrides functional results. Would deploy broken system  
**Correct**: Code scan FIRST→When mocks detected in production→AUTOMATIC FAIL immediately→HALT functional testing→Document findings with line numbers→Status: Failed→Require actual implementation before re-running cutover
