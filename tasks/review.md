**GOAL**: Review task development outcomes, ensuring compliance with quality standards and requirements.

## [Input]
  1. "{DEVNOTES}/{task_id}-dev-notes.md" --Development notes
  2. "{PLAN}/{task_id}-plan.md" --Implementation plan
  3. "{TMPL}/review-tmpl.yaml" --Review template

## [Output]
  1. "{REVIEW}/{task_id}-review.md" (Markdown format)
  2. "{EPIC}"
  3. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not skip test execution (if tests missing or fail to run, mark as Reject)
  2. Do not omit acceptance decision (Accept/Accept with changes/Reject)
  3. Do not produce review report that deviates from template structure
  4. Do not update epic with incorrect status or score
  5. **Do not accept ANY production code containing mock/stub implementations or hardcoded values, regardless of score** (auto-Reject, but unit tests using mocks/hardcoded test data are allowed)

## [Steps]
  1. Review Planning & Domain Identification
    - Understand implementation plan to identify task domain and establish scope of review
    - Determine domain-specific review criteria and success criteria
    - Create plan.md at "{root}/docs/plan.md" for progress tracking
    - Outcome: Review criteria and approach determined, plan.md initialized

  2. Code & Test Execution Review
    - **CRITICAL**: Scan ALL production/implementation code for mock/stub/placeholder patterns and hardcoded values (auto-reject if found; note: tests using mocks/hardcoded test data are allowed)
    - **CRITICAL**: Execute all relevant existing tests from previous tasks to detect regressions (auto-reject if any previously passing tests now fail)
    - Execute all tests and record results properly
    - Apply domain-specific scoring criteria appropriately
    - Verify test coverage and code alignment with plan
    - Outcome: Mock implementation and hardcoded values check completed, regression check completed, test results recorded and code alignment verified

  3. Development Notes Validation
    - Review development notes for alignment with implementation
    - Verify all technical decisions documented
    - Outcome: Dev notes alignment confirmed

  4. Report Generation & Decision
    - Check if "{REVIEW}/{task_id}-review.md" already exists
    - If exists: Read existing review and update it with new findings while preserving structure
    - If not exists: Create new review report from template
    - Make acceptance decision (Accept/Accept with changes/Reject) with rationale
    - Update "{EPIC}" based on review outcome
    - Outcome: Review report completed (created or updated) and epic updated

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Task identification (task ID and description from development notes)
  - Implementation plan review (requirements, architecture mapping, acceptance criteria)
  - Domain identification (Backend/Frontend/Database/Infrastructure/etc.)
  - Domain-specific review criteria selected (list of dimensions to evaluate)
  - Code quality inspection:
    * Production code files scanned (list)
    * Mock/stub/placeholder detection (found/not found, details if found)
    * Hardcoded values detection (found/not found, details if found)
    * Result: auto-reject triggered (yes/no)
  - Regression testing:
    * Existing tests from previous tasks identified (list)
    * Regression test execution results (all passing: yes/no, failures if any)
    * Result: auto-reject triggered (yes/no)
  - Test execution results:
    * Test command executed
    * Test results summary (passed/failed/total)
    * Test coverage achieved (percentage)
    * Test failures details (if any)
  - Code alignment verification:
    * Implementation matches plan (yes/no, deviations noted)
    * Architecture mapping verified (yes/no)
    * Acceptance criteria satisfied (each criterion with status)
  - Domain-specific scoring:
    * Each dimension score (name and score 0-10)
    * Overall score calculated (mean of dimensions)
    * Score level (Platinum/Gold/Silver/Bronze/Fail)
  - Acceptance decision (Accept/Accept with changes/Reject with rationale)
  - Epic update status (task marked in epic.md with score and status)

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
  - [ ] **CRITICAL**: All production/implementation code scanned and confirmed NO mock/stub/placeholder code or hardcoded values exist (tests using mocks/hardcoded test data are allowed)
  - [ ] **CRITICAL**: All relevant existing tests from previous tasks executed to verify NO regression of previously completed functionality
  - [ ] All tests executed with results recorded and verified against implementation plan
  - [ ] Complete review report exists at "{REVIEW}/{task_id}-review.md" with scoring and acceptance decision
  - [ ] "{EPIC}" updated with task completion status and score

## [Example]

### Example 1: Backend API - User Authentication
[Input]
- Development notes: docs/dev-notes/1-dev-notes.md (Task-1: Implement JWT authentication)
- Implementation plan: docs/plans/1-plan.md (specified JWT, bcrypt, token expiry)
- Template: review-tmpl.yaml

[Decision]
- Domain: Backend (apply backend scoring dimensions)
- Execute tests: npm test (all 15 tests pass, coverage 92%)
- Code alignment: Verify JWT implementation matches plan (src/auth/AuthService.js:L10-L45)
- Score: API Design (10.0), Security (10.0), Error Handling (8.0), Testing (10.0) → Overall 9.5
- Decision: Accept (all dimensions ≥ 6.0, no critical issues)

[Expected Outcome]
- docs/review/1-review.md with test results, code alignment analysis, score 9.5
- docs/epic.md updated: Task-1 marked completed with score
- Acceptance decision: Accept with rationale (strong implementation, minor error handling improvements suggested)

### Example 2: Frontend - Dashboard Widget
[Input]
- Development notes: docs/dev-notes/2-dev-notes.md (Task-2: Build analytics widget)
- Implementation plan: docs/plans/2-plan.md (React component with chart.js)
- Template: review-tmpl.yaml

[Decision]
- Domain: Frontend (apply frontend scoring dimensions)
- Execute tests: npm test (12/15 tests pass, 3 accessibility tests fail)
- Code alignment: Missing responsive design from plan (src/components/AnalyticsWidget.jsx)
- Score: UI/UX (8.0), State Management (9.0), Performance (8.0), Accessibility (5.5), Testing (6.0) → Overall 7.3
- Decision: Accept with changes (accessibility and responsive design fixes needed)

[Expected Outcome]
- docs/review/2-review.md with failed test details (L42-L58), alignment gaps
- Action items: Fix accessibility (aria-labels, keyboard nav), add responsive breakpoints
- docs/epic.md updated with score 7.3, status: needs revision

### Example 3: Database Migration - Schema Update
[Input]
- Development notes: docs/dev-notes/3-dev-notes.md (Task-3: Add user preferences table)
- Implementation plan: docs/plans/3-plan.md (migration script, indexes, foreign keys)
- Template: review-tmpl.yaml

[Decision]
- Domain: Database (apply database scoring dimensions)
- Execute tests: npm run test:db (migration fails rollback test, missing index on user_id)
- Code alignment: Foreign key constraint missing from plan (migrations/003_user_preferences.sql:L15)
- Score: Schema Design (7.0), Indexing (5.0), Migration (3.5), Performance (5.5) → Overall 5.3
- Decision: Reject (migration script has critical issue, rollback fails)

[Expected Outcome]
- docs/review/3-review.md with critical findings: migration rollback failure
- Risk: High (data integrity risk if deployed)
- Action items: Fix rollback script, add missing index, re-test migration
- docs/epic.md: Task-3 status = failed review, requires rework

### Good Example 1
[INPUT]
Task-1: JWT authentication implementation. Dev notes at docs/dev-notes/1-dev-notes.md. Plan at docs/plans/1-plan.md specifies JWT, bcrypt, token expiry. Template: review-tmpl.yaml.

[DECISION]
Step 1: Read plan to understand domain (Backend API) and acceptance criteria. Apply backend scoring dimensions. Step 2: Scan production code - NO mock/stub/placeholder patterns found. NO hardcoded values detected. Run existing tests from previous tasks - ALL passing (no regression). Execute npm test - all 15 tests pass, coverage 92%. Step 3: Verify code aligns with plan - JWT implementation at src/auth/AuthService.js:L10-L45 matches architecture. Step 4: Score using backend dimensions - API Design (10.0), Security (10.0), Error Handling (8.0), Testing (10.0). Overall: 9.5. Decision: Accept (all dimensions ≥6.0, no critical issues, no mocks, no regression). Update docs/epic.md with Task-1 completed, score 9.5.

[OUTCOME]
Complete docs/review/1-review.md with test results, code analysis, score 9.5 (Platinum). docs/epic.md updated with Task-1 completion status. Acceptance: Accept with rationale (strong implementation, minor error handling improvements suggested). No blocking issues.

### Good Example 2
[INPUT]
Task-2: Analytics dashboard widget. Dev notes and plan reference React, chart.js. Some accessibility tests failing.

[DECISION]
Step 1: Identify domain (Frontend). Apply frontend scoring dimensions. Step 2: Scan production code - NO mock implementations found. Run regression tests - previous Task-1 still passing. Execute npm test - 12/15 pass, 3 accessibility tests fail. Step 3: Review code alignment - missing responsive design from plan (src/components/AnalyticsWidget.jsx). Step 4: Score - UI/UX (8.0), State Management (9.0), Performance (8.0), Accessibility (5.5), Testing (6.0). Overall: 7.3. Decision: Accept with changes (accessibility below 6.0 needs fixes, but not critical failure). Update epic with revision status.

[OUTCOME]
docs/review/2-review.md documents failed accessibility tests (L42-L58), alignment gaps noted. Action items: Fix accessibility (aria-labels, keyboard nav), add responsive breakpoints. docs/epic.md updated: score 7.3, status needs revision. Clear guidance for improvements.

### Bad Example 1
[INPUT]
Task completed. Dev notes and plan exist.

[BAD-DECISION]
Skip test execution entirely. Assume tests pass. Don't check for mock implementations in production code. Don't run regression tests. Give high scores based on "code looks good". Mark as Accept without verification. Skip updating epic file.

[WHY-BAD]
Violates Constraint 1 (skip test execution - auto-reject). Violates DoD (tests not executed, no results recorded). Violates Step 2 (no mock/regression check). Scores without evidence are meaningless. Epic not updated violates DoD. Review is worthless without verification.

[CORRECT-APPROACH]
Execute Step 2 completely: First, scan ALL production code for mock/stub/placeholder patterns and hardcoded values (auto-reject if found). Second, run ALL relevant existing tests from previous tasks to detect regression (auto-reject if any fail). Third, execute current task tests and record results. Apply domain-specific scoring based on actual test results and code analysis. Make acceptance decision based on criteria. Update epic with accurate status and score.

### Bad Example 2
[INPUT]
Task involves payment processing. All tests passing with high coverage.

[BAD-DECISION]
Give high scores across all dimensions. Mark as Accept. Don't scan production code for mocks. Skip checking if production code has placeholder implementations or hardcoded API keys. Focus only on test results, ignore code quality inspection.

[WHY-BAD]
Violates Constraint 5 (CRITICAL - must reject ANY mock/hardcoded values in production code regardless of test results). Missing the critical code quality gate check. Tests might pass but production code could have "TODO: implement" or hardcoded credentials. Would deploy unsafe/incomplete code.

[CORRECT-APPROACH]
Follow Decision Rules: Code Quality Gate is FIRST and CRITICAL checkpoint. Before any test execution or scoring, scan ALL production/implementation code files for: mock implementations (TODO comments, placeholder functions, mock return values), hardcoded values (API keys, credentials, test data in production code). If ANY found: AUTOMATIC REJECT regardless of test scores. Note: tests using mocks/test data are ALLOWED. Only after passing code quality gate, proceed with test execution and scoring.

### Bad Example 3: Mock Implementation or Hardcoded Values in Production Code Auto-Reject (CRITICAL)
[Input]
- Development notes: docs/dev-notes/4-dev-notes.md (Task-4: Payment gateway integration)
- Implementation plan: docs/plans/4-plan.md (Stripe API integration)
- Template: review-tmpl.yaml

[Decision]
- Domain: Backend (apply backend scoring dimensions)
- **CRITICAL FINDING**: Mock implementation and hardcoded values detected in PRODUCTION CODE src/payment/PaymentService.js:L25
  ```javascript
  async processPayment(amount) {
    // TODO: implement actual Stripe integration
    const API_KEY = 'sk_test_hardcoded_key_123'; // Hardcoded API key!
    return { success: true, transactionId: 'mock-123' };
  }
  ```
- Execute tests: All 20 tests pass (tests properly use mocks for Stripe API - this is acceptable)
- Score: Would be API Design (9.0), Security (8.5), Error Handling (9.0), Testing (8.5) → Overall 8.8
- **Decision: AUTOMATIC REJECT** (mock implementation and hardcoded values found in production code - overrides all scoring)
- **Note**: Unit tests using mocks/hardcoded test data (e.g., `jest.mock('stripe')` in test files) are ALLOWED - rejection is only for production code mocks/hardcoded values

[Expected Outcome]
- docs/review/4-review.md with CRITICAL REJECTION: Mock implementation and hardcoded values detected in production code
- Rationale: Even with high test scores (8.8), mock code and hardcoded values in production are incomplete/unsafe work and unacceptable
- Risk: Critical (would deploy non-functional payment system with exposed credentials)
- Action items: Implement actual Stripe API integration in production code, remove all mock/TODO code and hardcoded values from src/ (keep test mocks/test data)
- docs/epic.md: Task-4 status = REJECTED, requires complete production implementation with proper configuration management

### Bad Example 4: Regression Breaking Previous Functionality Auto-Reject (CRITICAL)
[Input]
- Development notes: docs/dev-notes/5-dev-notes.md (Task-5: Add email notification feature)
- Implementation plan: docs/plans/5-plan.md (Email service integration)
- Template: review-tmpl.yaml

[Decision]
- Domain: Backend (apply backend scoring dimensions)
- Execute current task tests: All 18 new tests pass for email notification feature
- **CRITICAL FINDING**: Regression detected - existing user authentication tests now failing
  - Previous Task-1 authentication tests (15 tests) all passed before
  - Now 5/15 authentication tests fail due to modified session handling in src/auth/SessionManager.js:L32
  - Root cause: Task-5 refactored session storage breaking existing auth flow
- Score: Would be API Design (9.0), Integration (8.5), Error Handling (9.0), Testing (9.0) → Overall 8.9
- **Decision: AUTOMATIC REJECT** (breaking previously completed functionality - overrides all scoring)

[Expected Outcome]
- docs/review/5-review.md with CRITICAL REJECTION: Regression detected in previously completed Task-1 functionality
- Rationale: Even with high current task scores (8.9), breaking existing features undermines system stability
- Risk: Critical (would break production authentication system)
- Action items: Refactor email notification to preserve existing session handling, ensure all Task-1 tests pass, re-run full regression suite
- docs/epic.md: Task-5 status = REJECTED, requires fix to avoid breaking Task-1 functionality
