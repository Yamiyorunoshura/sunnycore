**GOAL**: Review task development outcomes, ensuring compliance with quality standards and requirements.

## [Input]
  1. "{DEVNOTES}/{task_id}-dev-notes.md" --Development notes
  2. "{PLAN}/{task_id}-plan.md" --Implementation plan
  3. "{TMPL}/review-tmpl.yaml" --Review template

## [Output]
  1. "{REVIEW}/{task_id}-review.md" (Markdown format)
  2. "{EPIC}"

## [Constraints]
  1. Do not skip test execution (if tests missing or fail to run, mark as Reject)
  2. Do not omit acceptance decision (Accept/Accept with changes/Reject)
  3. Do not produce review report that deviates from template structure
  4. Do not update epic with incorrect status or score

## [Tools]
  1. **sequential-thinking (MCP)** - Structured reasoning tool for complex logic analysis
    - [Step 1: Identify task domain and select review criteria]
    - [Step 2-4: Reason about domain-specific scoring logic, issue prioritization, and decision rationale]
    - When to use: When need complex code quality assessment or architecture alignment analysis
  2. **claude-context (MCP)** - Codebase semantic search and indexing tool
    - [Step 1-2: Search codebase for implementation plan-related code (if needed)]
    - [Step 2: Search for relevant test cases and implementation patterns]
  3. **context7 (MCP)**
    - [Step 2: Code and Test Review Phase - Verify external API usage correctness]
    - When to use: When reviewing code that integrates with external services or SDKs

## [Steps]
  1. Review Planning & Domain Identification
    - Understand implementation plan and identify task domain
    - Determine domain-specific review criteria and success criteria
    - Establish progress tracking mechanism
    - Outcome: Review criteria and approach determined

  2. Code & Test Execution Review
    - Execute all tests and record results properly
    - Apply domain-specific scoring criteria appropriately
    - Verify test coverage and code alignment with plan
    - Outcome: Test results recorded and code alignment verified

  3. Development Notes Validation
    - Review development notes for alignment with implementation
    - Verify all technical decisions documented
    - Outcome: Dev notes alignment confirmed

  4. Report Generation & Decision
    - Create complete review report at "{REVIEW}/{task_id}-review.md"
    - Make acceptance decision (Accept/Accept with changes/Reject) with rationale
    - Update "{EPIC}" based on review outcome
    - Outcome: Review report completed and epic updated

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
  - **Accept**: All dimensions ≥ 6.0, no critical issues
  - **Accept with Changes**: 1-2 dimensions between 5.0-5.9 with clear improvement plan
  - **Reject**: 3+ dimensions < 6.0, or any dimension < 5.0, or critical security/functional issues
  - **Risk**: Low (all ≥ 8.0), Medium (1-2 between 6.0-7.9), High (any < 6.0 or security issues)

## [DoD]
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
