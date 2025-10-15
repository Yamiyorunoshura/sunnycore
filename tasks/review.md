**GOAL**: Review task outcomes for quality compliance and requirements.

## [Context]
**You must read the following context:**
- `{DEVNOTES}/{task_id}-dev-notes.md`
- `{PLAN}/{task_id}-plan.md`
- `{ARCH}/*.md`
- `{TMPL}/review-tmpl.yaml`

## [Products]
- `{REVIEW}/{task_id}-review.md`
- Updated `{EPIC}`

## [Constraints]
- **MUST** verify architecture alignment, **MUST NOT** accept any architectural deviations (auto-reject)
- **MUST** scan production code for incomplete implementations, **MUST NOT** accept any mocks/stubs/hardcoded values (auto-reject, tests using mocks acceptable)
- **MUST** execute regression testing on all previous tasks, **MUST NOT** accept any test failures (auto-reject)
- **MUST** execute all current task tests and record results, **MUST NOT** skip test execution
- **MUST** make explicit acceptance decision (Accept/Accept with Changes/Reject), **MUST NOT** omit decision
- **MUST** follow review template structure (`{TMPL}/review-tmpl.yaml`), **MUST NOT** deviate from format
- **MUST** update Epic with accurate task status and score, **MUST NOT** provide incorrect data

## [Steps]
**You should work along to the following steps:**
1. **Understand Context**: Analyze plan, dev notes, and architecture to identify domain and review focus
2. **Verify Architecture Alignment** (CRITICAL): Confirm implementation follows architectural design 
3. **Scan Code Quality** (CRITICAL): Check for incomplete implementations in production code
4. **Execute Regression Testing** (CRITICAL): Ensure no previous functionality is broken
5. **Test and Score Current Task**: Run tests and apply domain-specific scoring criteria
6. **Make Decision and Assess Risk**: Determine acceptance based on scores and critical criteria
7. **Generate Report and Update Epic**: Use template to create review report and update task status

## [Instructions]

### 1. Understanding Task Context
Establish comprehensive context by analyzing the task's background, implementation, and architectural positioning.

**Context Analysis Approach**:
- **Plan Documents**: Extract requirements mapping, architectural components, TDD phases, and acceptance criteria to understand the intended scope and technical approach
- **Development Notes**: Review actual implementation decisions, technical choices, deviations from plan, and completion status to understand what was actually built
- **Architecture Documents**: Identify relevant components, design patterns, interfaces, and technology constraints to understand how this task fits into the overall system
- **Domain Recognition**: Determine the primary domain (Backend, Frontend, Database, Integration, Infrastructure) to select appropriate evaluation criteria

**Focus Areas**: Understand the gap between planned vs. actual implementation, identify architectural touchpoints, and establish domain-specific quality expectations.

### 2. Architecture Alignment Verification (CRITICAL - AUTOMATIC REJECT)
Ensure the implementation strictly adheres to architectural design before proceeding with functional review.

**Alignment Assessment Focus**:
- **Component Integrity**: Verify all specified architectural components are correctly implemented with proper responsibilities and boundaries
- **Pattern Adherence**: Confirm design patterns mandated by architecture are properly applied rather than bypassed with direct implementations
- **Data Flow Consistency**: Validate that data moves through the system following architectural diagrams and sequence flows
- **Interface Compliance**: Ensure component interfaces match architectural specifications for inputs, outputs, and error handling
- **Technology Conformance**: Check that framework and library choices align with architectural technology stack decisions

**Critical Standard**: Any deviation from architectural design results in automatic rejection, regardless of test results or functional quality.

### 3. Production Code Quality Assessment (CRITICAL - AUTOMATIC REJECT)
Verify that production code is deployment-ready without incomplete or placeholder implementations.

**Quality Assessment Focus**:
- **Implementation Completeness**: Ensure no mock classes, stub functions, or placeholder implementations exist in production code paths
- **Configuration Maturity**: Verify no hardcoded credentials, API keys, or environment-specific values that should be externalized
- **Development Artifacts**: Check for TODO/FIXME comments or temporary workarounds that indicate incomplete development
- **Production Readiness**: Confirm all business logic uses real implementations rather than test doubles or development conveniences

**Critical Distinction**: Test code legitimately uses mocks and stubs for isolation - this assessment focuses exclusively on production deployment code.

**Quality Standard**: Any incomplete implementation in production code results in automatic rejection to prevent deploying unfinished functionality.

### 4. Regression Impact Assessment (CRITICAL - AUTOMATIC REJECT)
Ensure current implementation does not break existing functionality from previously completed tasks.

**Regression Assessment Focus**:
- **Historical Functionality**: Verify all tests from previously completed tasks continue to pass without modification
- **Integration Stability**: Confirm that changes do not disrupt existing component interactions or data flows
- **Behavioral Consistency**: Ensure previously established business logic and user behaviors remain intact
- **System Resilience**: Validate that the system maintains its existing reliability and performance characteristics

**Protection Standard**: Any failure of previously passing tests indicates a regression that compromises system stability and requires immediate correction before acceptance.

### 5. Current Task Validation and Scoring
Evaluate the current task's implementation quality through comprehensive testing and domain-specific assessment.

**Validation Approach**:
- **Test Completeness**: Execute the full test suite including unit, integration, and behavioral tests to verify functional correctness
- **Coverage Assessment**: Measure test coverage to ensure critical paths and edge cases are adequately validated
- **TDD Verification**: Confirm that the RED-GREEN-REFACTOR cycle was properly followed as documented in development notes
- **Performance Validation**: Assess performance characteristics against non-functional requirements when applicable

**Scoring Methodology**: Apply domain-specific evaluation criteria (Backend, Frontend, Database, etc.) using established quality dimensions, collecting concrete evidence for each score, and calculating weighted averages for overall assessment.

### 6. Acceptance Decision and Risk Assessment
Determine task acceptance based on comprehensive evaluation results and assess associated risks.

**Decision Framework**:
- **Critical Gates First**: Any failure in architecture alignment, production code quality, or regression testing results in automatic rejection regardless of other scores
- **Quality Threshold Analysis**: Evaluate dimension scores against acceptance standards, considering both individual dimension performance and overall system impact  
- **Risk-Based Assessment**: Determine risk level based on quality scores, security implications, and potential system impact
- **Improvement Planning**: For conditional acceptance scenarios, establish clear improvement requirements and timelines

**Decision Considerations**: Balance functional completeness against quality standards, prioritize system stability over feature delivery, and ensure acceptance decisions align with long-term maintainability goals.

### 7. Documentation and Status Update
Generate comprehensive review documentation and update project tracking.

**Documentation Approach**:
- **Template Utilization**: Use the review template structure to ensure consistent reporting across all task reviews
- **Evidence-Based Reporting**: Document all findings with specific evidence, code references, and measurable results
- **Actionable Recommendations**: Provide clear, prioritized recommendations for any identified issues or improvements
- **Traceability**: Maintain clear links between requirements, implementation, and review outcomes

**Status Management**: Update Epic task status and scores to reflect review outcomes, ensuring accurate project tracking and enabling informed decision-making for subsequent tasks.

## [Domain-Specific-Review-Guidelines]
**Domain-Based Review Process**: Identify task domain first, then apply appropriate domain dimensions below. Use General Review if domain unclear.

**Scoring System (All Domains)**:
- **Platinum (9.0-10.0)**: ≥ 90% - Fully compliant, no issues
- **Gold (8.0-8.9)**: ≥ 80% - Excellent implementation, meets high standards
- **Silver (7.0-7.9)**: ≥ 70% - Meets basic standards, room for improvement
- **Bronze (6.0-6.9)**: ≥ 60% - Barely acceptable, multiple issues needing improvement
- **Fail (<6.0)**: < 60% - Below acceptable standards, critical gaps
- Calculate: overall_score = mean of dimension scores, round to 1 decimal

**Decision Rules**:
- **CRITICAL REJECT CRITERIA** (overrides all scoring):
  - **Architecture Misalignment**: ANY deviation from architecture (components, patterns, data flow, interfaces) → **AUTOMATIC REJECT**
  - **Mock/Stub Implementation or Hardcoded Values in Production Code**: ANY presence → **AUTOMATIC REJECT** (tests using mocks OK)
  - **Breaking Previously Completed Functionality**: ANY breaking of previous features → **AUTOMATIC REJECT**
- **Accept**: All dimensions ≥ 6.0, no critical issues, architecture aligned, no mocks/hardcoded in production, no regression
- **Accept with Changes**: 1-2 dimensions 5.0-5.9 with clear improvement plan, architecture aligned, no mocks/hardcoded in production, no regression
- **Reject**: 3+ dimensions < 6.0, or any dimension < 5.0, or critical issues, or architecture misalignment, or mocks/hardcoded in production, or regression
- **Risk**: Low (all ≥ 8.0), Medium (1-2 between 6.0-7.9), High (any < 6.0 or security issues or architecture misalignment or mocks/hardcoded or regression)

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Implementation verified to align with architecture (components, patterns, data flow, interfaces)
- [ ] **CRITICAL**: Production code scanned, NO mocks/stubs/hardcoded values found (tests using mocks OK)
- [ ] **CRITICAL**: Regression tests executed, NO previous functionality broken
- [ ] All tests executed with results recorded and scored
- [ ] Review report exists at `{REVIEW}/{task_id}-review.md` with decision
- [ ] `{EPIC}` updated with status and score

## [Example]

### Good #1
**Input**: JWT auth implementation (Backend), plan specifies JWT + bcrypt + expiry  
**Decision**: Domain=Backend. Read architecture: AuthService with JWT validation, bcrypt hashing. Verify alignment: AuthController uses AuthService ✓, JWT payload matches spec ✓, bcrypt rounds=10 as specified ✓. Scan production: NO mocks/hardcoded values ✓. Run previous tests: NO regression ✓. Execute tests: 15/15 pass, 92% coverage. Score: API(10.0) Security(10.0) Error(8.0) Testing(10.0) = 9.5. Accept. Update epic.  
**Why Good**: This completes full verification gates (architecture alignment, mock scan, regression, tests, alignment) before accepting with evidence-based scoring.

### Good #2
**Input**: Analytics widget (Frontend), React + chart.js, accessibility tests failing  
**Decision**: Domain=Frontend. Scan: NO mocks ✓. Regression: Task-1 still passing ✓. Tests: 12/15 pass (3 accessibility fail). Missing responsive design. Score: UI(8.0) State(9.0) Perf(8.0) A11y(5.5) Testing(6.0) = 7.3. Accept with changes. Update epic.  
**Why Good**: This surfaces deficiencies (accessibility) with actionable fixes and accurate epic status (needs revision).

### Good #3
**Input**: Database migration (Database), add user preferences table with indexes  
**Decision**: Domain=Database. Determine criteria: Schema Design, Indexing, Migration Safety, Performance. Scan: NO hardcoded credentials ✓. Regression: Previous migrations rollback OK ✓. Tests: 22/22 pass, migration + rollback verified. Review against criteria: Schema(9.0) Indexing(8.5) Migration(9.0) Performance(8.0) = 8.6. Accept. Update epic.  
**Why Good**: This applies domain-specific criteria (Step 1), validates migration safety and rollback, and reviews against established dimensions (Step 5).

### Bad #1
**Input**: Task completed, dev notes and plan exist  
**Bad Decision**: Skip tests. Assume pass. No mock scan. No regression check. "Code looks good". High scores. Accept. Skip epic.  
**Why Bad**: This violates Constraint 1 (no tests), DoD (no verification), Step 2-3 (no critical checks), and produces meaningless review.  
**Correct**: Scan production code. Run regression tests. Execute current tests. Score based on evidence. Update epic.

### Bad #2: Mock/Hardcoded Auto-Reject
**Input**: Payment gateway (Backend), all tests pass  
**Bad Decision**: Tests pass. Give high scores. Mark Accept. **SKIP mock scan**. **SKIP hardcoded check**.  
**Why Bad**: This violates Constraint 4 (CRITICAL - must scan). Production code has `// TODO: implement` + `API_KEY='sk_test_123'`. This would deploy unsafe/incomplete code.  
**Correct**: Scan FIRST. If mock/hardcoded found in production code, apply AUTOMATIC REJECT regardless of test scores (tests using mocks OK).

### Bad #3: Regression Auto-Reject
**Input**: Email notification (Backend), 18 new tests pass  
**Bad Decision**: Current tests pass. Score high. Accept. **SKIP regression check**.  
**Why Bad**: This violates Constraint 5 (CRITICAL - must check regression). Previous Task-1 auth tests now 5/15 fail. This would break production auth.  
**Correct**: Run ALL previous tests. If ANY fail, apply AUTOMATIC REJECT regardless of current scores.

### Bad #4: Architecture Misalignment Auto-Reject
**Input**: Payment processing (Backend), all tests pass, no mocks, no regression  
**Bad Decision**: Tests pass. No mocks. No regression. Give high scores. Accept. **SKIP architecture verification**.  
**Why Bad**: This violates Constraint 6 (CRITICAL - must verify architecture alignment). Architecture specifies PaymentGateway interface + strategy pattern, but implementation uses direct API calls bypassing interface. This violates architectural design and reduces maintainability/testability.  
**Correct**: Verify architecture FIRST. If implementation deviates from specified components/patterns/interfaces, apply AUTOMATIC REJECT regardless of test scores. Require refactoring to align with architecture.
