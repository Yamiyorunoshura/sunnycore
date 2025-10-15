**GOAL**: Execute project acceptance validation from business and user perspectives.

## [Context]
**You must read the following context:**
- `{REQ}/*.md` (required)
- `{ARCH}/*.md` (required)
- `{TMPL}/cutover-report-tmpl.yaml` (required)

## [Products]
- `{CUTOVER}`

## [Constraints]
- **MUST** verify architecture alignment, **MUST NOT** accept architectural deviations (auto-reject)
- **MUST** scan production code for mocks/stubs/hardcoded values, **MUST NOT** accept any found (auto-reject; tests using mocks OK)
- **MUST** test from end-user perspective, **MUST NOT** perform technical testing
- **MUST** halt if required inputs missing, **MUST NOT** proceed without complete input set

## [Steps]
**You should work along to the following steps:**
1. Validate required inputs exist and are complete. This ensures all necessary documentation is available.
2. **CRITICAL**: Verify implementation aligns with architecture (components, patterns, data flow, interfaces). This confirms architectural compliance.
3. **CRITICAL**: Scan production code for incomplete implementations (mocks, stubs, hardcoded values). This ensures production readiness.
4. Configure environment and document setup requirements. This establishes proper runtime environment.
5. Execute project and verify basic functionality. This confirms the system runs correctly.
6. Test all critical requirements from end-user business perspective. This validates business value delivery.
7. Generate cutover report with clear acceptance decision. This documents validation outcomes.

## [Instructions]

### Architecture Alignment Verification (AUTOMATIC REJECT CRITERIA)
Verify implementation strictly follows architectural design before functional testing:

**Focus Areas**:
- **Components**: All architectural components properly implemented with correct responsibilities
- **Patterns**: Design patterns from architecture applied correctly (not bypassed with direct implementations)
- **Data Flow**: Information flows match architectural diagrams and sequences
- **Interfaces**: Component contracts match architectural specifications
- **Technology Stack**: Implementation uses technologies specified in architecture

**Approach**: Systematically compare implementation against architecture documents. Any deviation results in automatic rejection regardless of test outcomes.

### Production Code Quality Assessment (AUTOMATIC REJECT CRITERIA)
Ensure production code is deployment-ready without incomplete implementations:

**Focus Areas**:
- Mock implementations in production code paths
- Stub functions with placeholder responses
- Hardcoded credentials, API keys, or configuration values
- TODO/FIXME comments indicating incomplete work

**Approach**: Scan all production code (tests using mocks are acceptable). Any incomplete implementation results in automatic rejection.

### End-User Perspective Testing
Test critical requirements from business user viewpoint:

**Focus**: Business workflows and user value, not technical implementation details
- ✓ "User completes checkout and receives confirmation"
- ✗ "Database transaction commits successfully"

**Approach**: Use Given-When-Then scenarios from requirements. Execute user actions, observe outcomes, verify against acceptance criteria. Document results with evidence.

### Environment Configuration
Identify and document all configuration requirements:

**Focus**: Complete setup reproducibility
- Environment variables and their purposes
- External service dependencies
- Infrastructure requirements
- Migration scripts and setup steps

**Approach**: Document every configuration step with rationale for future deployment reproducibility.

### Decision Framework
Determine cutover status based on validation results:

**Success**: All requirements pass, architecture aligned, no incomplete production code
**Partial Success**: Core functionality works, some non-critical issues identified
**Failed**: Critical requirements fail, OR architecture violations, OR incomplete production code

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Implementation verified to align with architecture specifications
- [ ] **CRITICAL**: Production code verified free of mocks/stubs/hardcoded values  
- [ ] All critical requirements tested from end-user perspective with documented results
- [ ] Environment setup documented and verified functional
- [ ] Complete cutover report generated with clear acceptance decision

## [Example]

### Good #1: Complete Validation Process
**Context**: E-commerce checkout system. Architecture specifies OrderService→PaymentService→EmailService flow.
**Approach**: Verify OrderService delegates to PaymentService (✓), PaymentService calls real payment gateway (✓), EmailService sends actual emails (✓). Scan code - no mocks in production (✓). Test user workflow: add to cart → checkout → payment → confirmation email received (✓). Status: Success.
**Why Good**: Validates architecture alignment, confirms real implementations, tests complete user journey.

### Good #2: Architecture Violation Detection  
**Context**: Authentication system. Architecture specifies JWT with refresh tokens. Implementation uses session cookies only.
**Approach**: Compare implementation against architecture - JWT requirement violated. Functional tests pass but architectural deviation found. Status: Failed (automatic rejection).
**Why Good**: Correctly identifies architectural violations as blocking issues regardless of functional success.

### Bad #1: Missing Critical Verification
**Context**: Payment processing system with mock payment gateway in production code.
**Bad Approach**: Skip code quality scan. Focus only on functional testing. Tests pass because mock returns success. Mark as Success.
**Why Bad**: Violates automatic rejection criteria. Would deploy non-functional payment processing to production.
**Correct**: Scan production code first. Detect mock implementation. Apply automatic rejection. Require real payment gateway implementation.