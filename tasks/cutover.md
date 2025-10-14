**GOAL**: Execute project acceptance validating deliverables from business and user perspectives.

## [Input]
- `{REQ}/*.md` (required)
- `{ARCH}/*.md` (required)
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
1. Understand business objectives and architecture → Business objectives understood, architecture validated
2. **CRITICAL**: Scan ALL production code for mock/stub/placeholder/hardcoded values (auto-fail if found; tests using mocks OK) → Code quality verified
3. Identify configuration needs, document requirements → Configuration requirements documented
4. Configure environment, document setup → Environment configured
5. Run project, verify functionality → Project running with verified functionality
6. Test all critical requirements from end-user perspective → Complete acceptance test results documented
7. Generate cutover report, determine status (Success/Partial Success/Failed) → Complete cutover report with clear status

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Production code scanned, NO mock/stub/hardcoded values (tests using mocks OK)
- [ ] All critical requirements tested from end-user perspective with results recorded
- [ ] Complete cutover report at "{CUTOVER}" with status and rationale
- [ ] All issues documented with severity and reproduction steps

## [Example]

### Good #1
**Input**: Requirements and architecture exist. Code scan passes. Docker-compose setup fails (Redis port conflict). After fixing, all requirements (REQ-001: user CRUD, REQ-002: auth) pass  
**Decision**: Validate inputs exist→Scan production code for mocks/hardcoded (none, passed)→Analyze config needs→Setup docker-compose (Redis port conflict detected)→Fix: change Redis port to 6380 in .env→Restart→Execute successfully→Test end-user perspective: REQ-001 (CRUD operations - pass), REQ-002 (login, token refresh - pass)→Document results→Generate cutover: Success  
**Why Good**: Executes every gate (code quality, environment setup, requirement validation) before success verdict, documents config fixes

### Good #2
**Input**: Requirements (REQ-001: payment processing). Code inspection reveals mock and hardcoded API key in PaymentService.js  
**Decision**: Scan all production code before functional testing→Detect CRITICAL: mock at PaymentService.js:L42 with TODO and hardcoded key→Check unit tests (properly use jest.mock, acceptable)→AUTOMATIC FAIL per constraint→HALT functional testing→Document critical findings with excerpts→Generate cutover: Failed→List action items: implement actual gateway, move secrets to env, remove TODOs→Recommend re-run after fixes  
**Why Good**: Applies automatic-fail decisively, prevents insecure code from advancing, communicates precise remediation

### Bad #1
**Input**: Production code has mock with TODO. Functional tests pass because mock returns success  
**Bad Decision**: Code scan finds mock but tests pass→Mark cutover Success→Reasoning: "Tests work, must be good"→Skip documenting mock issue→Recommend deployment  
**Why Bad**: Violates constraint (ANY mock in production→auto-fail). Code quality gate CRITICAL, must be first. Functional success irrelevant if production has mocks. Would deploy non-functional code  
**Correct**: Code quality gate MANDATORY first step→When mock detected→AUTOMATIC FAIL regardless of functional results→HALT testing→Document critical findings with excerpts→Status: Failed→Provide action items to remove mocks→Require re-run after fixes
