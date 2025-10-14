**GOAL**: Review task outcomes for quality compliance and requirements.

## [Input]
**You must read the following documents:**
- `{DEVNOTES}/{task_id}-dev-notes.md`
- `{PLAN}/{task_id}-plan.md`
- `{ARCH}/*.md`
- `{TMPL}/review-tmpl.yaml`

## [Output]
- `{REVIEW}/{task_id}-review.md`
- Updated `{EPIC}`

## [Constraints]
- **MUST** execute all tests and record results, **MUST NOT** skip test execution (auto-reject if missing/failing)
- **MUST** make acceptance decision (Accept/Accept with changes/Reject), **MUST NOT** omit decision
- **MUST** follow review template structure, **MUST NOT** deviate from format
- **MUST** scan production code for mocks/stubs/hardcoded values, **MUST NOT** accept ANY found (auto-reject, tests using mocks OK)
- **MUST** run regression tests on previous tasks, **MUST NOT** accept if any break (auto-reject)
- **MUST** verify implementation aligns with architecture, **MUST NOT** accept if misalignment found (auto-reject)
- **MUST** update epic with accurate status/score, **MUST NOT** provide incorrect data

## [Steps]
**You should work along to the following steps:**
1. Read plan and architecture to identify domain, determine review criteria and scoring dimensions. This identifies domain with review approach documented.
2. **CRITICAL**: Verify implementation aligns with architecture (components, patterns, data flow, interfaces). This confirms architectural alignment (auto-reject if misaligned).
3. **CRITICAL**: Scan ALL production code for mocks/stubs/hardcoded values. This confirms NO mocks/hardcoded values in production code (auto-reject if found).
4. **CRITICAL**: Run all existing tests from previous tasks. This confirms NO regression (auto-reject if any break).
5. Execute current task tests, apply domain-specific scoring, verify coverage + plan alignment. This records test results with scores.
6. Review implementation against criteria from Step 1, validate all dimensions meet standards. This completes comprehensive review with evidence.
7. Create or update `{REVIEW}/{task_id}-review.md`, make decision (Accept/Accept with changes/Reject), update `{EPIC}`. This completes review report with epic updated.

## [Instructions]

### 1. Domain Identification and Review Criteria
Identify the task domain from plan and architecture to determine appropriate review dimensions:

**Domain Identification**:
- Read `{PLAN}/{task_id}-plan.md` to understand what was built
- Read `{ARCH}/*.md` to identify which component/layer is involved
- Determine domain: Backend, Frontend, Database, DevOps, Mobile, etc.

**Domain-Specific Dimensions**: Each domain has specialized review criteria (see Domain-Specific-Review-Guidelines below).

### 2. Architecture Alignment Verification (CRITICAL - AUTOMATIC FAIL)
**BEFORE** any other review, verify implementation aligns with architecture:

**Verification Checklist**:
- [ ] **Components**: All specified components are implemented correctly
- [ ] **Patterns**: Design patterns from architecture are followed
- [ ] **Data Flow**: Data flows match architecture diagrams
- [ ] **Interfaces**: Contracts match architecture specifications
- [ ] **Technology Stack**: Tech choices align with architecture

**If misalignment found**: Apply AUTOMATIC REJECT regardless of test scores. Document the deviation and require refactoring to align with architecture.

### 3. Code Quality Scan (CRITICAL - AUTOMATIC FAIL)
**BEFORE** functional review, scan ALL production code:

**Scan For**:
- Mock implementations in production code (e.g., `class MockPaymentGateway`)
- Stub functions with hardcoded responses
- TODO/FIXME comments indicating incomplete implementation
- Hardcoded values (API keys, secrets, URLs, business logic constants)

**Important**: Tests using mocks (e.g., `jest.mock()`, `sinon.stub()`) are ACCEPTABLE. Production code with mocks is AUTOMATIC REJECT.

**If found**: Apply AUTOMATIC REJECT regardless of test scores. Document findings with file paths and line numbers.

### 4. Regression Testing (CRITICAL - AUTOMATIC FAIL)
**BEFORE** reviewing current task, run ALL tests from previous tasks:

**Regression Checklist**:
- [ ] All tests from Task-1 still pass
- [ ] All tests from Task-2 still pass
- [ ] ... (all previous tasks)
- [ ] No previously passing functionality breaks

**If ANY previous test fails**: Apply AUTOMATIC REJECT. The current task has introduced a regression and must be fixed.

### 5. Test Execution and Scoring
Execute current task tests and score based on domain-specific criteria:

**Test Execution**:
- Run complete test suite (unit + integration + behavior)
- Record results (pass/fail counts)
- Measure coverage percentage
- Note any performance metrics (if NFRs exist)

**Domain-Specific Scoring**: Apply appropriate scoring dimensions based on identified domain (see Domain-Specific-Review-Guidelines below).

### 6. Implementation Quality Review
Review implementation against domain-specific quality criteria:

**Review Each Dimension**:
- Score each dimension (0-10 scale)
- Provide specific evidence (code excerpts, test results, metrics)
- Note strengths and areas for improvement
- Calculate overall score (mean of all dimensions, rounded to 1 decimal)

### 7. Decision and Risk Assessment
Make acceptance decision based on scoring and critical criteria:

**Decision Rules**:
- **Accept**: All dimensions ≥ 6.0, no critical issues, architecture aligned, no mocks in production, no regression
- **Accept with Changes**: 1-2 dimensions 5.0-5.9 with clear improvement plan, all critical criteria pass
- **Reject**: 
  - 3+ dimensions < 6.0, OR
  - Any dimension < 5.0, OR
  - Architecture misalignment (CRITICAL), OR
  - Mocks/hardcoded in production (CRITICAL), OR
  - Regression detected (CRITICAL)

**Risk Level**:
- **Low**: All dimensions ≥ 8.0
- **Medium**: 1-2 dimensions 6.0-7.9
- **High**: Any dimension < 6.0 OR any critical issue

### 8. Review Report and Epic Update
Create or update `{REVIEW}/{task_id}-review.md` with complete findings:

**Report Must Include**:
- Architecture alignment verification results
- Code quality scan results (mocks/hardcoded check)
- Regression test results
- Test execution results with coverage
- Domain-specific dimension scores with evidence
- Overall score calculation
- Decision (Accept/Accept with Changes/Reject) with rationale
- Risk level assessment
- Actionable recommendations (if issues found)

**Update Epic**: Update `{EPIC}` with task status and score.

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
