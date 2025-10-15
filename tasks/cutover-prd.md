**GOAL**: Execute project acceptance validating deliverables from business and user perspectives.

## [Context]
**You must read the following context:**
- `{PRD}` (required)
- `{TMPL}/cutover-report-tmpl.yaml` (required)

## [Products]
- `{CUTOVER}`

## [Constraints]
- **MUST** test from end-user perspective, **MUST NOT** perform technical testing
- **MUST** halt if required inputs missing, **MUST NOT** proceed
- **MUST** test all critical requirements, **MUST NOT** skip any
- **MUST** follow template structure, **MUST NOT** deviate
- **CRITICAL**: **MUST** reject ANY production code with mock/stub/hardcoded values regardless of functional tests (auto-Fail; tests using mocks OK), **MUST NOT** accept

## [Steps]
**You should work through the following steps:**
1. **Validate Inputs**: Ensure PRD and template are available and complete before proceeding.
2. **Code Quality Scan**: Systematically examine ALL production code for mocks, stubs, TODOs, and hardcoded values. Focus on business logic, API integrations, and configuration. Auto-fail if any found.
3. **Extract Business Context**: From PRD, identify critical user journeys, functional requirements (REQ-xxx), non-functional requirements (NFR-xxx), and success criteria that define business value.
4. **Environment Setup**: Identify configuration dependencies, set up environment following documentation, and document any gaps or issues encountered.
5. **Project Execution**: Start the project using documented methods, verify it runs successfully, and capture any startup errors or performance issues.
6. **End-User Acceptance Testing**: Test each critical requirement from user perspective, focusing on workflows and business outcomes rather than technical implementation.
7. **Assessment and Reporting**: Determine overall status based on test results and code quality, following Success/Partial Success/Failed criteria.

## [Instructions]

### Approach Guidelines

**Code Quality Focus**: 
- Prioritize production code integrity over functional test results
- Distinguish between test mocks (acceptable) and production mocks/stubs (automatic fail)
- Look for incomplete implementations, hardcoded values, and placeholder code

**Business Validation Approach**:
- Test user workflows and business outcomes, not technical implementation details
- Validate against acceptance criteria defined in PRD requirements
- Focus on critical user journeys that deliver business value

**Evidence Collection**:
- Document configuration steps and environment setup challenges
- Capture test evidence (screenshots, logs, error messages) for both passing and failing scenarios
- Record business impact of any issues found

**Decision Framework**:
- Success: All critical requirements pass + clean production code + documented setup
- Partial Success: Core functionality works + minor issues with workarounds
- Failed: Critical failures OR production code quality issues OR environment setup impossible

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Production code scanned, NO mock/stub/hardcoded values (tests using mocks OK)
- [ ] All critical business requirements tested from end-user perspective with results recorded
- [ ] Complete cutover report generated following template structure
- [ ] All issues documented with severity and business impact

## [Example]

### Good Execution
**Scenario**: E-commerce app with login, payment, and inventory features. Code scan finds clean production code. Payment gateway configured correctly but inventory API returns stale data.  
**Approach**: Validate inputs → Scan code (passes) → Extract 5 critical requirements from PRD → Setup environment (minor config issues documented) → Run app successfully → Test user workflows: login (pass), checkout (pass), inventory view (fail - shows old stock levels) → Document as High severity with business impact → Status: Partial Success (4/5 critical requirements).  
**Why Good**: Systematic approach, code quality verified first, business-focused testing, clear impact assessment.

### Poor Execution  
**Scenario**: Same app but code scan reveals MockPaymentGateway class in production.  
**Wrong Approach**: Skip code quality issues because "functional tests might pass anyway."  
**Why Wrong**: Violates automatic fail constraint. Production mocks create deployment risk regardless of test outcomes.  
**Correct Approach**: Detect production mock → Apply automatic fail → Document code quality issues → Status: Failed → Require real implementation before re-testing.
