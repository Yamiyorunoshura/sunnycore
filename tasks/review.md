**GOAL**: Review task outcomes for quality compliance and requirements.

## [Input]
- `{DEVNOTES}/{task_id}-dev-notes.md`
- `{PLAN}/{task_id}-plan.md`
- `{TMPL}/review-tmpl.yaml`

## [Output]
- `{REVIEW}/{task_id}-review.md`
- Updated `{EPIC}`

## [Constraints]
- **MUST** execute all tests and record results, **MUST NOT** skip test execution (auto-reject if missing/failing)
- **MUST** make acceptance decision (Accept/Accept with changes/Reject), **MUST NOT** omit decision
- **MUST** follow review template structure, **MUST NOT** deviate from format
- **MUST** scan production code for mocks/stubs/hardcoded values, **MUST NOT** accept ANY found (auto-reject, tests using mocks are OK)
- **MUST** run regression tests on previous tasks, **MUST NOT** accept if any break (auto-reject)
- **MUST** update epic with accurate status/score, **MUST NOT** provide incorrect data

## [Steps]
1. Read plan to identify domain, determine review criteria and scoring dimensions → Domain identified with review approach documented
2. **CRITICAL**: Scan ALL production code for mocks/stubs/hardcoded values → Confirmed NO mocks/hardcoded values in production code (auto-reject if found)
3. **CRITICAL**: Run all existing tests from previous tasks → Confirmed NO regression (auto-reject if any break)
4. Execute current task tests, apply domain-specific scoring, verify coverage + plan alignment → Test results recorded with scores
5. Review implementation against criteria from Step 1, validate all dimensions meet standards → Comprehensive review completed with evidence
6. Create or update `{REVIEW}/{task_id}-review.md`, make decision (Accept/Accept with changes/Reject), update `{EPIC}` → Review report completed with epic updated

## [Domain-Specific-Review-Guidelines]
  
  ### **Domain-Based Review Process**
  Identify task domain first, then apply appropriate domain dimensions below. Use General Review if domain is unclear.

  ### **Scoring System (All Domains)**
  - **Platinum (9.0-10.0)**: ≥ 90% - Fully compliant, no issues
  - **Gold (8.0-8.9)**: ≥ 80% - Excellent implementation, meets high standards
  - **Silver (7.0-7.9)**: ≥ 70% - Meets basic standards, room for improvement
  - **Bronze (6.0-6.9)**: ≥ 60% - Barely acceptable, multiple issues needing improvement
  - **Fail (<6.0)**: < 60% - Below acceptable standards, critical gaps
  - Calculate: overall_score = mean of dimension scores, round to 1 decimal

  ### **Decision Rules**
  - **CRITICAL REJECT CRITERIA** (overrides all scoring):
    - **Mock/Stub Implementation or Hardcoded Values Detection in Production Code**: ANY presence of mock/placeholder/stub code or hardcoded values in production/implementation code → **AUTOMATIC REJECT**
      - Examples: `// TODO: implement`, `throw new Error('Not implemented')`, placeholder return values, mock data in production code, hardcoded API keys, hardcoded credentials, hardcoded test data in production code
      - Rationale: Mock implementations and hardcoded values are incomplete/unsafe work, unacceptable regardless of test scores
      - **Important**: tests using mocks/stubs/hardcoded test data for testing purposes are ALLOWED and expected
    - **Breaking Previously Completed Functionality**: ANY breaking of features/functionality completed in previous tasks → **AUTOMATIC REJECT**
      - Rationale: Regression breaks system stability and undermines prior work, unacceptable regardless of current task scores
      - Verification: Run all relevant existing tests to ensure no regressions
  - **Accept**: All dimensions ≥ 6.0, no critical issues, **AND no mock implementations or hardcoded values in production code**, **AND no regression of previous functionality**
  - **Accept with Changes**: 1-2 dimensions between 5.0-5.9 with clear improvement plan, **AND no mock implementations or hardcoded values in production code**, **AND no regression of previous functionality**
  - **Reject**: 3+ dimensions < 6.0, or any dimension < 5.0, or critical security/functional issues, **OR any mock implementations or hardcoded values found in production code**, **OR any breaking of previously completed functionality**
  - **Risk**: Low (all ≥ 8.0), Medium (1-2 between 6.0-7.9), High (any < 6.0 or security issues or mock implementations/hardcoded values in production code or regression detected)

## [DoD]
- [ ] **CRITICAL**: Production code scanned, NO mocks/stubs/hardcoded values found (tests using mocks OK)
- [ ] **CRITICAL**: Regression tests executed, NO previous functionality broken
- [ ] All tests executed with results recorded and scored
- [ ] Review report exists at `{REVIEW}/{task_id}-review.md` with decision
- [ ] `{EPIC}` updated with status and score

## [Example]

### Good #1
**Input**: JWT auth implementation (Backend), plan specifies JWT + bcrypt + expiry  
**Decision**: Domain=Backend → Scan production: NO mocks/hardcoded values → Run previous tests: NO regression → Execute tests: 15/15 pass, 92% coverage → Score: API(10.0) Security(10.0) Error(8.0) Testing(10.0) = 9.5 → Accept → Update epic  
**Why Good**: Full verification gates (mock scan, regression, tests, alignment) completed before accepting, evidence-based scoring

### Good #2
**Input**: Analytics widget (Frontend), React + chart.js, accessibility tests failing  
**Decision**: Domain=Frontend → Scan: NO mocks → Regression: Task-1 still passing → Tests: 12/15 pass (3 accessibility fail) → Missing responsive design → Score: UI(8.0) State(9.0) Perf(8.0) A11y(5.5) Testing(6.0) = 7.3 → Accept with changes → Update epic  
**Why Good**: Surfaces deficiencies (accessibility) with actionable fixes, accurate epic status (needs revision)

### Good #3
**Input**: Database migration (Database), add user preferences table with indexes  
**Decision**: Domain=Database → Determine criteria: Schema Design, Indexing, Migration Safety, Performance → Scan: NO hardcoded credentials → Regression: Previous migrations rollback OK → Tests: 22/22 pass, migration + rollback verified → Review against criteria: Schema(9.0) Indexing(8.5) Migration(9.0) Performance(8.0) = 8.6 → Accept → Update epic  
**Why Good**: Applies domain-specific criteria (Step 1), validates migration safety and rollback, reviews against established dimensions (Step 5)

### Bad #1
**Input**: Task completed, dev notes and plan exist  
**Decision**: Skip tests → Assume pass → No mock scan → No regression check → "Code looks good" → High scores → Accept → Skip epic  
**Why Bad**: Violates Constraint 1 (no tests), DoD (no verification), Step 2-3 (no critical checks), meaningless review  
**Correct Approach**: Scan production code → Run regression tests → Execute current tests → Score based on evidence → Update epic

### Bad #2: Mock/Hardcoded Auto-Reject
**Input**: Payment gateway (Backend), all tests pass  
**Decision**: Tests pass → Give high scores → Mark Accept → **SKIP mock scan** → **SKIP hardcoded check**  
**Why Bad**: Violates Constraint 4 (CRITICAL - must scan). Production code has `// TODO: implement` + `API_KEY='sk_test_123'` → Would deploy unsafe/incomplete code  
**Correct Approach**: Scan FIRST → If mock/hardcoded found in production code → AUTOMATIC REJECT regardless of test scores (tests using mocks OK)

### Bad #3: Regression Auto-Reject
**Input**: Email notification (Backend), 18 new tests pass  
**Decision**: Current tests pass → Score high → Accept → **SKIP regression check**  
**Why Bad**: Violates Constraint 5 (CRITICAL - must check regression). Previous Task-1 auth tests now 5/15 fail → Would break production auth  
**Correct Approach**: Run ALL previous tests → If ANY fail → AUTOMATIC REJECT regardless of current scores
