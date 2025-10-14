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
- **MUST** verify implementation aligns with architecture, **MUST NOT** accept if misalignment found (auto-Fail)
- **MUST** reject ANY production code with mock/stub/hardcoded values regardless of functional tests (auto-Fail; tests using mocks OK), **MUST NOT** accept

## [Steps]
**You should work along to the following steps:**
1. Understand business objectives and architecture. This ensures business objectives are understood and architecture validated.
2. **CRITICAL**: Verify implementation aligns with architecture (components, patterns, data flow, interfaces). This confirms architectural alignment (auto-fail if misaligned).
3. **CRITICAL**: Scan ALL production code for mock/stub/placeholder/hardcoded values (auto-fail if found; tests using mocks OK). This verifies code quality.
4. Identify configuration needs, document requirements. This documents configuration requirements.
5. Configure environment, document setup. This configures environment.
6. Run project, verify functionality. This runs project with verified functionality.
7. Test all critical requirements from end-user perspective. This documents complete acceptance test results.
8. Generate cutover report, determine status (Success/Partial Success/Failed). This creates complete cutover report with clear status.

## [Instructions]

### 1. Input Validation (CRITICAL FIRST STEP)
Before ANY acceptance testing, validate required inputs:
- Verify `{REQ}/*.md` exist and are complete
- Verify `{ARCH}/*.md` exist and are complete
- Verify `{TMPL}/cutover-report-tmpl.yaml` exists
- If ANY required input is missing, HALT immediately and return an error message

Do NOT proceed without a complete input set.

### 2. Architecture Alignment Verification (AUTOMATIC FAIL CRITERIA #1)
**CRITICAL**: Verify implementation aligns with architecture specifications:

**Check alignment for**:
- **Components**: All specified components are implemented (e.g., if arch specifies OrderService, PaymentService, it must exist)
- **Patterns**: Design patterns are followed (e.g., if arch specifies Repository pattern, it must be used)
- **Data Flow**: Data flows match architecture diagrams (e.g., if arch shows API → Service → Repository, implementation must follow this)
- **Interfaces**: Contracts match specifications (e.g., if arch defines IPaymentGateway interface, implementation must use it)
- **Technology Stack**: Tech choices match architecture (e.g., if arch specifies PostgreSQL, not MySQL)

**If misalignment found**: Apply AUTOMATIC FAIL regardless of functional test results. Architecture deviation is a critical issue that must be resolved.

### 3. Code Quality Scan (AUTOMATIC FAIL CRITERIA #2)
**BEFORE** any functional testing, scan ALL production code:

**What to scan for**:
- Mock implementations in production code
- Stub functions with hardcoded responses
- TODO/FIXME indicating incomplete implementation
- Hardcoded values (API keys, secrets, URLs, business logic values)

**Important**: Tests using mocks are OK; production code with mocks is AUTOMATIC FAIL.

**If found**: Apply AUTOMATIC FAIL and halt acceptance testing.

### 4. Requirements and Architecture Understanding
Extract from input documents:
- All functional requirements (REQ-001, REQ-002, etc.) with acceptance criteria
- All non-functional requirements (NFR-001, NFR-002, etc.)
- Architecture components, patterns, and technology stack
- Data flows and integration points

### 5. Environment Configuration
Identify and document configuration needs:
- Environment variables required
- External service dependencies (databases, APIs, message queues)
- Infrastructure setup (Docker, Kubernetes, etc.)
- Migration scripts to run

Document EVERY configuration step:
- What was configured
- Why it was needed  
- How to reproduce the setup

### 6. Functional Acceptance Testing (End-User Perspective)
Test ALL critical requirements from an end-user perspective:

**For each requirement**:
1. Set up test scenario matching Given-When-Then criteria from requirements
2. Execute user action
3. Observe outcome
4. Verify against acceptance criteria
5. Record result with evidence

**Focus on business value, not technical implementation**:
- ✓ "User completes checkout and receives order confirmation"
- ✗ "Database transaction commits successfully"

### 7. Issue Documentation and Resolution
For ANY failed requirement:
- **Severity**: Critical / High / Medium / Low
- **Description**: Expected vs actual behavior
- **Reproduction Steps**: Exact steps to reproduce
- **Evidence**: Screenshots, logs, error messages
- **Root Cause** (if identifiable): What caused the failure
- **Business Impact**: How this affects users/business

### 8. Cutover Report and Decision
Generate complete cutover report:

**Status Determination**:
- **Success**: All requirements pass, architecture aligned, no mocks/hardcoded in production
- **Partial Success**: Some non-critical requirements fail, core functionality works
- **Failed**:
  - ANY critical requirement fails, OR
  - Architecture misalignment found, OR
  - Production code contains mocks/stubs/hardcoded values

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Implementation verified to align with architecture (components, patterns, data flow, interfaces)
- [ ] **CRITICAL**: Production code scanned, NO mock/stub/hardcoded values (tests using mocks OK)
- [ ] All critical requirements tested from end-user perspective with results recorded
- [ ] Complete cutover report at "{CUTOVER}" with status and rationale
- [ ] All issues documented with severity and reproduction steps

## [Example]

### Good #1
**Input**: Requirements and architecture exist. Code scan passes. Docker-compose setup fails (Redis port conflict). After fixing, all requirements (REQ-001: user CRUD, REQ-002: auth) pass  
**Decision**: Validate inputs exist ✓. Read architecture: 3-tier (API layer, Service layer, Data layer). Verify alignment: UserController→UserService→UserRepository ✓, AuthController→AuthService ✓, Redis for sessions as specified ✓. Scan production code for mocks/hardcoded (none, passed) ✓. Analyze config needs. Setup docker-compose (Redis port conflict detected). Fix: change Redis port to 6380 in .env. Restart. Execute successfully. Test end-user perspective: REQ-001 (CRUD operations - pass), REQ-002 (login, token refresh - pass). Document results. Generate cutover: Success.  
**Why Good**: This executes every gate (architecture alignment, code quality, environment setup, requirement validation) before success verdict and documents config fixes.

### Good #2
**Input**: Requirements (REQ-001: payment processing). Code inspection reveals mock and hardcoded API key in PaymentService.js  
**Decision**: Scan all production code before functional testing. Detect CRITICAL: mock at PaymentService.js:L42 with TODO and hardcoded key. Check unit tests (properly use jest.mock, acceptable) ✓. AUTOMATIC FAIL per constraint. HALT functional testing. Document critical findings with excerpts. Generate cutover: Failed. List action items: implement actual gateway, move secrets to env, remove TODOs. Recommend re-run after fixes.  
**Why Good**: This applies automatic-fail decisively, prevents insecure code from advancing, and communicates precise remediation.

### Bad #1
**Input**: Production code has mock with TODO. Functional tests pass because mock returns success  
**Bad Decision**: Code scan finds mock but tests pass. Mark cutover Success. Reasoning: "Tests work, must be good". Skip documenting mock issue. Recommend deployment.  
**Why Bad**: This violates constraint (ANY mock in production→auto-fail). Code quality gate is CRITICAL and must be first. Functional success is irrelevant if production has mocks. This would deploy non-functional code.  
**Correct**: Code quality gate is MANDATORY first step. When mock detected, apply AUTOMATIC FAIL regardless of functional results. HALT testing. Document critical findings with excerpts. Status: Failed. Provide action items to remove mocks. Require re-run after fixes.

### Bad #2: Architecture Misalignment Auto-Fail
**Input**: E-commerce system. All functional tests pass. No mocks. Architecture specifies microservices (OrderService, PaymentService, InventoryService). Implementation is monolithic with direct database calls.  
**Bad Decision**: All requirements work from user perspective. No code quality issues. Mark cutover Success. **SKIP architecture verification**. Recommend deployment.  
**Why Bad**: This violates constraint (must verify architecture alignment). Architecture misalignment is a CRITICAL gate that overrides functional success. Monolithic implementation violates architectural design (scalability, maintainability, deployment). This would deploy technically-debt-laden code requiring future costly refactoring.  
**Correct**: Verify architecture IMMEDIATELY after understanding it. When implementation deviates from specified architecture (components, patterns, boundaries), apply AUTOMATIC FAIL regardless of functional results. HALT acceptance. Document architectural violations with evidence. Status: Failed. Provide action items to refactor to align with architecture. Require re-run after fixes.
