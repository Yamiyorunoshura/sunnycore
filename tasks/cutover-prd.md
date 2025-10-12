**GOAL**: Execute project acceptance, validating deliverables from business and user perspectives.

## [Input]
  1. "{PRD}" --Product Requirements Document (required, used as primary requirement and architecture source)
  2. "{TMPL}/cutover-report-tmpl.yaml" --Cutover report template (required)

## [Output]
  1. "{CUTOVER}" --Cutover report (Markdown format)
  2. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not perform technical testing (must test from end-user perspective)
  2. Do not proceed if required input files are missing (must list and halt)
  3. Do not skip testing any critical business requirements
  4. Do not deviate from template structure
  5. **Do not accept ANY production code containing mock/stub implementations or hardcoded values, regardless of functional test results** (auto-Fail cutover, but unit tests using mocks/hardcoded test data are allowed)

## [Steps]
  1. Preparation & Validation
    - Understand business objectives and technical architecture from PRD
    - Create plan.md at "{root}/docs/plan.md" for progress tracking
    - Outcome: Business objectives and architecture understood from PRD, and plan.md initialized

  2. Code Quality Inspection (CRITICAL)
    - **CRITICAL**: Scan ALL production/implementation code for mock/stub/placeholder patterns and hardcoded values (auto-fail if found; note: tests using mocks/hardcoded test data are allowed)
    - Verify no TODO/placeholder comments in production code
    - Check for hardcoded credentials, API keys, or configuration values
    - Outcome: Code quality verified, no mock implementations or hardcoded values in production code

  3. Configuration Analysis & Documentation
    - Identify configuration needs based on PRD technical specifications
    - Document all configuration requirements clearly
    - Outcome: Configuration requirements documented

  4. Environment Setup & Verification
    - Configure project environment following documentation
    - Document all setup steps and any failures
    - Outcome: Fully configured environment ready for testing

  5. Project Execution & Functional Verification
    - Run project and verify functionality
    - Document execution results with detailed logs
    - Outcome: Project running with verified functionality

  6. Acceptance Testing
    - Test all critical business requirements from PRD from end-user perspective
    - Document comprehensive test results with evidence
    - Record all issues with severity and impact
    - Outcome: Complete acceptance test results documented

  7. Report Generation & Status Determination
    - Generate complete cutover report at "{CUTOVER}"
    - Determine cutover status (Success/Partial Success/Failed)
    - Document all findings and recommendations
    - Outcome: Complete cutover report with clear status

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Business objectives summary from PRD (key requirements and success criteria)
  - Architecture validation from PRD (components identified, dependencies verified)
  - Code quality inspection results:
    * Production code files scanned (list of files)
    * Mock/stub/placeholder detection results (found/not found)
    * Hardcoded values detection results (found/not found)
    * TODO/placeholder comments check (found/not found)
  - Configuration analysis:
    * Configuration requirements identified (list)
    * Environment variables needed (list)
    * External service dependencies (list)
  - Environment setup status:
    * Dependencies installed (list with status)
    * Configuration applied (list with status)
    * Setup issues encountered (if any)
  - Project execution results:
    * Application start command
    * Execution status (success/failed)
    * Execution logs summary
  - Acceptance testing progress:
    * Critical requirements tested from PRD (list with test ID and result)
    * Issues identified (count and severity: critical/high/medium/low)
    * Test evidence collected (yes/no)
  - Cutover status determination (Success/Partial Success/Failed with rationale)

## [Acceptance-Testing-Guidelines]
  1. **Code Quality Gate (CRITICAL - Must Pass First)**
    - **AUTOMATIC FAIL CRITERIA** (overrides all functional test results):
      - **Mock/Stub Implementation or Hardcoded Values Detection in Production Code**: ANY presence of mock/placeholder/stub code or hardcoded values in production/implementation code → **AUTOMATIC FAIL**
        - Examples: `// TODO: implement`, `throw new Error('Not implemented')`, placeholder return values, mock data in production code, hardcoded API keys, hardcoded credentials, hardcoded configuration values in production code
        - Rationale: Mock implementations and hardcoded values are incomplete/unsafe work, unacceptable for production deployment regardless of functional test results
        - **Important**: tests using mocks/stubs/hardcoded test data for testing purposes are ALLOWED and expected
    - Scan all production code files before proceeding with functional testing
    - If mock implementations or hardcoded values found: STOP testing, report as Failed, document findings
  
  2. **End-User Perspective Testing**
    - Test all critical business requirements from PRD from user perspective (not technical testing)
    - Verify user workflows are smooth and intuitive
    - Assess error messages clarity and user guidance
  
  3. **Configuration & Setup Validation**
    - Identify and document all configuration requirements
    - Verify setup documentation completeness
    - Test deployment and installation procedures
  
  4. **Issue Documentation**
    - Record all issues with severity classification (critical/high/medium/low)
    - Provide clear reproduction steps for each issue
    - Assess business impact of each issue
  
  5. **Business Value & Readiness**
    - Confirm deliverables align with business objectives from PRD
    - Determine cutover status: Success / Partial Success / Failed
    - Assess production deployment readiness and risk

## [DoD]
  - [ ] **CRITICAL**: All production/implementation code scanned and confirmed NO mock/stub/placeholder code or hardcoded values exist (tests using mocks/hardcoded test data are allowed)
  - [ ] All critical business requirements from PRD tested from end-user perspective with results recorded
  - [ ] Complete cutover report at "{CUTOVER}" with status (Success/Partial Success/Failed) and clear rationale
  - [ ] All issues documented with severity classification and reproduction steps

## [Example]

### Example 1: Mobile App Release
[Input]
- PRD: docs/PRD.md (REQ-001: user login, REQ-002: push notifications, REQ-003: offline mode)
- Template: cutover-report-tmpl.yaml

[Decision]
- Setup: Install Expo, configure Firebase (successful)
- Run: expo start (app launches successfully on iOS/Android simulators)
- Test REQ-001: Login with test credentials (✓ success)
- Test REQ-002: Send test notification (✗ failed - Firebase config missing)
- Test REQ-003: Offline data sync (✓ success)
- Issues: 1 critical (push notifications not working)

[Expected Outcome]
- docs/cutover-report.md with status: Partial Success
- Test results: REQ-001 (pass), REQ-002 (fail - missing FCM server key), REQ-003 (pass)
- Issues documented: Critical severity, reproduction steps (send notification → error "Invalid FCM token")
- Configuration needs: Firebase Cloud Messaging server key required

### Example 2: Mock Implementation or Hardcoded Values Auto-Fail (CRITICAL)
[Input]
- PRD: docs/PRD.md (REQ-001: Payment processing, REQ-002: Order management)
- Template: cutover-report-tmpl.yaml

[Decision]
- **CRITICAL FINDING**: Code quality inspection reveals mock implementations and hardcoded values in PRODUCTION CODE
  - src/services/PaymentService.js:L42: Mock implementation detected
    ```javascript
    async processPayment(order) {
      // TODO: implement actual payment gateway
      const API_KEY = 'pk_test_hardcoded_12345'; // Hardcoded API key!
      return { success: true, transactionId: 'mock-txn-001' };
    }
    ```
  - src/config/database.js:L15: Hardcoded database credentials
    ```javascript
    const DB_CONFIG = {
      host: 'localhost',
      password: 'admin123', // Hardcoded password!
      database: 'production_db'
    };
    ```
- **Decision: AUTOMATIC FAIL** (mock implementations and hardcoded values found in production code - testing halted)
- **Note**: Unit tests properly use mocks (jest.mock()) - this is acceptable, but production code must not contain mocks or hardcoded values

[Expected Outcome]
- docs/cutover-report.md with status: Failed
- CRITICAL findings documented: Mock implementations and hardcoded sensitive values in production code
- Rationale: Code is not production-ready; contains incomplete implementations and security vulnerabilities
- Risk: Critical (would deploy non-functional payment system with exposed credentials)
- Action items: 
  1. Implement actual payment gateway integration (remove mock code from src/services/PaymentService.js)
  2. Move all hardcoded values to environment variables/configuration files
  3. Remove all TODO/placeholder comments from production code
  4. Re-run cutover after fixes are complete
- Functional testing not performed (halted at code quality gate)

