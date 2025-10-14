**GOAL**: Execute project acceptance validating deliverables from business and user perspectives.

## [Input]
**You must read the following documents:**
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
**You should work along to the following steps:**
1. Understand business objectives and architecture from PRD. This ensures business objectives and architecture are understood.
2. **CRITICAL**: Scan ALL production code for mock/stub/placeholder/hardcoded values (auto-fail if found; tests using mocks OK). This verifies code quality.
3. Identify configuration needs, document requirements. This documents configuration requirements.
4. Configure environment, document setup steps. This configures environment and makes it ready.
5. Run project, verify functionality with logs. This runs project with verified functionality.
6. Test all critical business requirements from end-user perspective. This documents complete acceptance test results.
7. Generate cutover report, determine status (Success/Partial Success/Failed). This creates complete cutover report with clear status.

## [Instructions]

### 1. Input Validation (CRITICAL FIRST STEP)
Before ANY acceptance testing, validate required inputs:
- Verify `{PRD}` exists and is complete
- Verify `{TMPL}/cutover-report-tmpl.yaml` exists
- If ANY required input is missing, HALT immediately and return an error message

Do NOT proceed without a complete input set.

### 2. Code Quality Scan (AUTOMATIC FAIL CRITERIA)
**BEFORE** any functional testing, scan ALL production code:

**What to scan for**:
- Mock implementations (e.g., `class MockPaymentGateway`)
- Stub functions (e.g., `function stub() { return true; }`)
- TODO/FIXME comments indicating incomplete code
- Hardcoded values:
  - API keys (e.g., `API_KEY = 'sk_test_12345'`)
  - Passwords or secrets
  - URLs not from config
  - Business logic values that should be configurable

**Important Distinction**:
- ✓ Tests using mocks (e.g., `jest.mock()`, `sinon.stub()`) are ACCEPTABLE
- ✗ Production code with mocks/stubs/hardcoded values is AUTOMATIC FAIL

**If found**: Apply AUTOMATIC FAIL regardless of how well functional tests perform. Halt acceptance testing and document critical findings.

### 3. Business Context Understanding
Extract from PRD:
- Business objectives and success criteria
- Critical user journeys and workflows
- All functional requirements (REQ-001, REQ-002, etc.)
- All non-functional requirements (NFR-001, NFR-002, etc.)
- Architecture components and technology stack

### 4. Environment Configuration
Identify and document configuration needs:
- Environment variables required
- External service dependencies
- Database setup and migrations
- API keys and credentials (from secure sources)

Document EVERY configuration step taken:
- What was configured
- Why it was needed
- Where the configuration lives

### 5. Functional Acceptance Testing (End-User Perspective)
Test ALL critical business requirements from an end-user perspective, NOT technical perspective:

**Correct (End-User)**:
- ✓ "User logs in with email and password successfully"
- ✓ "Dashboard displays user's order history within 2 seconds"
- ✓ "Payment processes and confirmation email is sent"

**Incorrect (Technical)**:
- ✗ "JWT token is generated with correct payload"
- ✗ "Database query returns correct records"
- ✗ "Redis cache is populated"

For each requirement:
1. Execute the user action
2. Observe the outcome
3. Verify it matches acceptance criteria from PRD
4. Record: Pass/Fail with evidence (screenshots, logs, error messages)

### 6. Issue Documentation
For ANY failed requirement, document:
- **Severity**: Critical (blocks release) / High (major impact) / Medium (workaround exists) / Low (minor)
- **Description**: What failed and expected vs actual behavior
- **Reproduction Steps**: Exact steps to reproduce
- **Evidence**: Screenshots, log excerpts, error messages
- **Business Impact**: How this affects users/business

### 7. Cutover Report and Decision
Generate complete cutover report following template:

**Status Determination**:
- **Success**: All critical requirements pass, no mocks/hardcoded in production, environment documented
- **Partial Success**: Some non-critical requirements fail, but core functionality works
- **Failed**: 
  - ANY critical requirement fails, OR
  - Production code contains mocks/stubs/hardcoded values, OR
  - Cannot configure environment to run the project

Include in report:
- Summary of results (X/Y requirements passed)
- Configuration steps performed
- All issues with severity levels
- Recommendation (deploy / fix issues first / major rework needed)

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Production code scanned, NO mock/stub/hardcoded values (tests using mocks OK)
- [ ] All critical business requirements tested from end-user perspective with results recorded
- [ ] Complete cutover report at "{CUTOVER}" with status and rationale
- [ ] All issues documented with severity and reproduction steps

## [Example]

### Good #1
**Input**: PRD has 3 requirements (login, push notifications, offline). Code scan passes. App runs but push notifications fail (missing Firebase config)  
**Decision**: Validate PRD exists ✓. Extract objectives from PRD. Scan production code for mocks/hardcoded (none found, passed) ✓. Identify config needs. Setup: install Expo+Firebase. Run: expo start (launches). Test: REQ-001 login (pass), REQ-002 push notifications (fail - FCM server key missing), REQ-003 offline (pass). Document issue severity: Critical. Record reproduction. Status: Partial Success (2/3).  
**Why Good**: This executes entire checklist from code scan to requirement validation before verdict and captures precise diagnostics.

### Good #2
**Input**: PRD has payment processing. Code scan reveals mock with hardcoded API key in PaymentService.js production code. Unit tests properly use jest.mock()  
**Decision**: Scan all production code before functional testing. Detect mock at PaymentService.js:L42 with TODO and hardcoded key. Verify unit tests use mocks (acceptable) ✓. AUTOMATIC FAIL per constraint (production code has mock/hardcoded). HALT functional testing. Document critical findings with excerpts. Generate cutover: Failed. Provide action items: implement real gateway, externalize secrets, remove TODOs.  
**Why Good**: This enforces automatic-fail rules rigorously, halts delivery when production code unsafe, and provides actionable remediation.

### Bad #1
**Input**: PRD exists. Code has mocks but functional tests pass  
**Bad Decision**: Scan finds mocks but tests pass so mark Success. Reasoning: "Tests work, so it's ready".  
**Why Bad**: This violates constraint (ANY mock/stub in production→auto-fail). Code quality gate is CRITICAL and overrides functional results. This would deploy broken system.  
**Correct**: Code scan FIRST. When mocks detected in production, apply AUTOMATIC FAIL immediately. HALT functional testing. Document findings with line numbers. Status: Failed. Require actual implementation before re-running cutover.
