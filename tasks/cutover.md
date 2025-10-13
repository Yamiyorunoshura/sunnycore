**GOAL**: Execute project acceptance, validating deliverables from business and user perspectives.

## [Input]
  1. "{REQ}/*.md" --Requirement documents (required)
  2. "{ARCH}/*.md" --Architecture documents (required)
  3. "{TMPL}/cutover-report-tmpl.yaml" --Cutover report template (required)
  4. "{TMPL}/plan-tmpl.yaml" --Unified planning template; capture user-centric test scope, configuration checkpoints, and evidence collection steps

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
    - Understand business objectives from requirement documents
    - Understand system architecture from architecture documents
    - Create comprehensive plan.md at "{root}/docs/plan.md" using the plan template to track the working progress
    - Outcome: Business objectives understood, architecture validated, and plan.md initialized

  2. Code Quality Inspection (CRITICAL)
    - **CRITICAL**: Scan ALL production/implementation code for mock/stub/placeholder patterns and hardcoded values (auto-fail if found; note: tests using mocks/hardcoded test data are allowed)
    - Verify no TODO/placeholder comments in production code
    - Check for hardcoded credentials, API keys, or configuration values
    - Outcome: Code quality verified, no mock implementations or hardcoded values in production code

  3. Configuration Analysis & Documentation
    - Identify configuration needs based on architecture documents
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
    - Test all critical business requirements from end-user perspective
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
    - Test all critical business requirements from user perspective (not technical testing)
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
    - Confirm deliverables align with business objectives from requirement documents
    - Determine cutover status: Success / Partial Success / Failed
    - Assess production deployment readiness and risk

## [DoD]
  - [ ] **CRITICAL**: All production/implementation code scanned and confirmed NO mock/stub/placeholder code or hardcoded values exist (tests using mocks/hardcoded test data are allowed)
  - [ ] All critical business requirements tested from end-user perspective with results recorded
  - [ ] Complete cutover report at "{CUTOVER}" with status (Success/Partial Success/Failed) and clear rationale
  - [ ] All issues documented with severity classification and reproduction steps

## [Example]

### Good Example 1
[INPUT]
Requirements and architecture documents exist. Production code scanned shows no mocks or hardcoded values. Docker-compose setup fails due to Redis port conflict. After fixing configuration, all critical requirements (REQ-001: user CRUD, REQ-002: authentication) pass from end-user perspective.

[DECISION]
Validate input files exist. Scan production code for mocks/hardcoded values (none found, code quality gate passed). Analyze configuration needs from architecture docs. Setup environment with docker-compose (Redis port conflict detected). Fix configuration: change Redis port to 6380 in .env. Restart services. Execute project successfully. Test all critical requirements from user perspective: REQ-001 (create, read, update, delete user - all pass), REQ-002 (login, token refresh - pass). Document all results. Generate cutover report with status: Success.

[OUTCOME]
Cutover report at docs/cutover-report.md with status: Success. Configuration issue documented: Redis port changed to 6380 (add to .env.example). All acceptance tests passed with evidence (API response logs). Recommendations: Update README.md with port configuration. Environment ready for production deployment. Plan.md shows code quality passed, config fixed, all requirements tested and verified.

[WHY-GOOD]
- Executes every gate—code quality, environment setup, requirement validation—before issuing a success verdict.
- Documents configuration fixes and evidence, enabling repeatable deployments and knowledge transfer.

### Good Example 2
[INPUT]
PRD contains requirements (REQ-001: payment processing). Code quality inspection reveals mock implementation and hardcoded API key in production code (src/services/PaymentService.js).

[DECISION]
Scan all production code files before functional testing. Detect CRITICAL issue: Mock implementation at PaymentService.js:L42 with TODO comment and hardcoded API key. Check unit tests (properly use jest.mock, acceptable). Apply AUTOMATIC FAIL criteria per Constraint 5. HALT functional testing immediately. Document critical findings with code excerpts. Generate cutover report with status: Failed. List specific action items: implement actual payment gateway, move secrets to environment variables, remove TODO comments. Recommend re-run cutover after fixes.

[OUTCOME]
Cutover report at docs/cutover-report.md with status: Failed. CRITICAL findings documented: mock implementation and hardcoded credentials in production code. Rationale: code not production-ready, security vulnerabilities present. Risk level: Critical (would deploy non-functional system). Functional testing not performed (halted at code quality gate). Action items provided for developers to fix issues. Plan.md documents code quality scan results and automatic fail decision.

[WHY-GOOD]
- Applies the automatic-fail rule decisively, preventing insecure code from advancing.
- Communicates precise remediation steps, so the development team knows exactly how to recover.

### Bad Example 1
[INPUT]
Production code contains mock implementation with TODO comment. Functional tests all pass because mock returns success.

[BAD-DECISION]
Code quality scan finds mock implementation but functional tests pass, so mark cutover as Success. Reasoning: "The tests work, so it must be good enough." Skip documenting the mock implementation issue. Generate success report recommending deployment.

[WHY-BAD]
Violates Constraint 5 (do not accept ANY mock/stub implementations in production code). Code quality gate is CRITICAL and must be checked first. Functional test success is irrelevant if production code contains mocks. Would deploy non-functional code to production. Ignores security risks of hardcoded values. Violates automatic fail criteria in Acceptance-Testing-Guidelines.

[CORRECT-APPROACH]
Code quality gate is MANDATORY first step. When mock implementation detected, AUTOMATIC FAIL regardless of functional test results. HALT testing immediately. Document critical findings with code excerpts. Report status: Failed. Provide specific action items to remove mocks and implement actual functionality. Require re-run of cutover after fixes. Never proceed to functional testing when code quality gate fails.

### Bad Example 2
[INPUT]
Environment setup fails with dependency installation error. Configuration is incomplete. Cannot run project to test requirements.

[BAD-DECISION]
Skip environment setup and functional testing. Review code and documentation only. Generate cutover report with status: Partial Success based on code review. Reasoning: "The code looks good, so environment issues are minor."

[WHY-BAD]
Violates the goal of validating deliverables from end-user perspective. Cannot determine Success/Partial Success/Failed without actually running and testing the project. Skipping functional testing contradicts Step 5-6 (Project Execution and Acceptance Testing). Code review alone is insufficient for cutover acceptance. Would approve untested deployment.

[CORRECT-APPROACH]
Document environment setup failure in plan.md. Identify configuration gaps from architecture documents. Work through setup issues systematically (install dependencies, configure environment variables, resolve conflicts). Do not proceed to status determination until project actually runs. If environment issues cannot be resolved, report status: Failed with detailed documentation of blocking issues. Request configuration documentation improvements. Never approve cutover without actual functional verification.
