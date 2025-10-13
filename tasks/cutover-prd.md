**GOAL**: Execute project acceptance, validating deliverables from business and user perspectives.

## [Input]
  1. "{PRD}" --Product Requirements Document (required, used as primary requirement and architecture source)
  2. "{TMPL}/cutover-report-tmpl.yaml" --Cutover report template (required)
  3. "{TMPL}/plan-tmpl.yaml" --Unified planning template; customize sections for PRD-sourced acceptance testing and configuration validation

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
    - Create comprehensive plan.md at "{root}/docs/plan.md" using the plan template to track the working progress
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
  - [ ] All the checkbox in plan.md are marked as done
  - [ ] plan.md is deleted

## [Example]

### Good Example 1
[INPUT]
PRD contains 3 requirements (login, push notifications, offline mode). Code quality scan passes (no mocks or hardcoded values in production code). App runs successfully but push notifications fail due to missing Firebase configuration.

[DECISION]
Validate PRD exists. Extract business objectives and requirements from PRD. Scan production code for mocks/hardcoded values (none found, code quality passed). Identify configuration needs from PRD technical specs. Setup environment: install Expo and Firebase SDK. Run project: expo start (launches successfully). Test REQ-001 login (pass), REQ-002 push notifications (fail - FCM server key missing), REQ-003 offline mode (pass). Document issue with severity: Critical. Record reproduction steps and configuration gap. Determine status: Partial Success (2/3 requirements working).

[OUTCOME]
Cutover report at docs/cutover-report.md with status: Partial Success. Test results documented: REQ-001 pass, REQ-002 fail (missing FCM server key in Firebase config), REQ-003 pass. Issue documented with severity: Critical, impact: Push notifications non-functional. Configuration requirement documented: Add FCM_SERVER_KEY to .env file. Recommendation: Complete Firebase setup before production release. Plan.md shows 2/3 requirements passed, 1 configuration issue identified.

[WHY-GOOD]
- Executes the entire cutover checklist—from code quality scan to requirement validation—before issuing a verdict.
- Captures precise diagnostics and remediation guidance, giving stakeholders a clear path to production readiness.

### Good Example 2
[INPUT]
PRD contains payment processing requirement. Code quality scan reveals mock implementation with hardcoded API key in PaymentService.js production code. Unit tests properly use jest.mock().

[DECISION]
Scan all production code before functional testing. Detect mock implementation at src/services/PaymentService.js:L42 with TODO and hardcoded API key. Verify unit tests use mocks appropriately (acceptable for testing). Apply AUTOMATIC FAIL per Constraint 5 (production code contains mock/hardcoded values). HALT functional testing. Document critical findings with code excerpts showing mock return value and hardcoded credentials. Generate cutover report: Failed. Provide action items: implement real payment gateway, externalize secrets, remove TODOs.

[OUTCOME]
Cutover report at docs/cutover-report.md with status: Failed. Critical findings: mock implementation and hardcoded values in production code documented with line numbers and code examples. Rationale: production code incomplete and insecure. Risk: Critical (would deploy broken payment system). Action items provided: remove mocks, implement actual integration, move secrets to environment. Functional testing not performed (halted at code quality gate). Plan.md documents code scan results and automatic fail decision.

[WHY-GOOD]
- Enforces automatic-fail rules rigorously, halting delivery when production code is unsafe.
- Provides actionable remediation steps and evidence, enabling rapid correction without ambiguity.

### Bad Example 1
[INPUT]
PRD exists but contains only high-level descriptions without specific requirement IDs. Code contains mock implementations that return successful test results.

[BAD-DECISION]
Extract vague requirements from PRD. Scan code and find mocks but functional tests pass so continue testing. Generate cutover report: Success because all tests passed. Reasoning: "The mocks make the tests work, so it's ready."

[WHY-BAD]
Violates Constraint 5 (do not accept ANY mock implementations). Code quality gate is CRITICAL and overrides functional test results. Mock implementations are not production-ready code. Would deploy non-functional system. Violates automatic fail criteria when mocks detected in production code. Ignores security risks.

[CORRECT-APPROACH]
Code quality scan must happen FIRST before functional testing. When mocks detected in production code, apply AUTOMATIC FAIL immediately. HALT functional testing. Document findings: mock implementations found at specific line numbers. Report status: Failed. Never proceed to functional testing when code quality gate fails. Require actual implementation before re-running cutover.

### Bad Example 2
[INPUT]
PRD contains 5 critical requirements. Only tested 3 of them because the other 2 seemed less important. All 3 tested requirements passed.

[BAD-DECISION]
Generate cutover report with status: Success. Document only the 3 requirements tested. Reasoning: "The main features work, so the app is ready for release." Skip testing requirements that seem less critical.

[WHY-BAD]
Violates Constraint 3 (do not skip testing any critical business requirements). PRD defines all requirements as critical for the business. Selective testing leaves untested functionality that may be broken. Incomplete acceptance validation. Would deploy with unknown defects. Violates Step 6 (test ALL critical requirements).

[CORRECT-APPROACH]
Test ALL critical business requirements from PRD without exception. Even if requirement seems minor, test it if PRD marks it as critical. Document test results for every requirement. If time/resource constraints prevent complete testing, report as blocker and request prioritization from user. Status should be Partial Success if any requirements remain untested, with clear documentation of what was not verified.
