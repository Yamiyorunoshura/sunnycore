**GOAL**: Review task development outcomes, ensuring compliance with quality standards and requirements.

## [Input]
  1. "{DEVNOTES}/{task_id}-dev-notes.md" --Development notes
  2. "{PLAN}/{task_id}-plan.md" --Implementation plan
  3. "{TMPL}/review-tmpl.yaml" --Review template

## [Output]
  1. "{REVIEW}/{task_id}-review.md"
  2. "{EPIC}"

## [Constraints]
  1. Must execute all tests created during the develop-plan phase and verify test results align with the implementation plan. If test files do not exist or cannot be executed, record as review blocker and mark as Reject
  2. Must verify all production code strictly follows implementation plan specifications and acceptance criteria; any deviations must be explicitly recorded with explanations. "Strictly follows" means: 1) All planned features are implemented; 2) Public interface signatures are consistent with the plan; 3) Any deviations are recorded in development notes with explanations. Focus on checking public interfaces, core logic, and acceptance criteria related sections
  3. Must produce machine-checkable Markdown (including structured heading hierarchy H1-H3, list items, code blocks, and using consistent markup format), containing sections: Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items
  4. Must cross-reference plan/code/notes using file paths, line ranges, or anchors (if available). Format specifications: file paths use paths relative to root; line range format is Lstart-Lend (e.g., L10-L20); anchor format is #anchor-id
  5. Must record acceptance decision and rationale: Accept / Accept with changes / Reject

## [Tools]
  1. **sequential-thinking (MCP)** - Structured reasoning tool for complex logic analysis
    - [Step 1: Identify task domain and select review criteria]
    - [Step 2-4: Reason about domain-specific scoring logic, issue prioritization, and decision rationale]
    - When to use: When need complex code quality assessment or architecture alignment analysis
  2. **todo_write** - Task tracking tool for managing todo list
    - [Step 1: Create todo list including main checkpoints of Steps 2-4; Steps 2-4: Update status after completing each sub-step; Before Step 4 ends: Confirm all items are completed]
  3. **claude-context (MCP)** - Codebase semantic search and indexing tool
    - [Step 1-2: Search codebase for implementation plan-related code (if needed)]
    - [Step 2: Search for relevant test cases and implementation patterns]

## [Steps]
  1. Review Planning Phase
    - Understand the implementation plan and identify task domain
    - Determine appropriate domain-specific review criteria and success criteria
    - Establish progress tracking mechanism for review checkpoints

  2. Code and Test Review Phase
    - Ensure all tests are executed with results properly recorded
    - Ensure domain-specific scoring criteria are applied appropriately
    - Ensure proper handling of both passing and failing test scenarios
    - Achieve verification of test coverage and code alignment with plan

  3. Development Notes Review Phase
    - Ensure alignment between development notes and actual implementation

  4. Results Generation and Decision Phase
    - Achieve complete review report saved to "{REVIEW}/{task_id}-review.md"
    - Ensure appropriate acceptance decision (Accept/Accept with changes/Reject) with clear rationale
    - Ensure "{EPIC}" is updated correctly based on review outcome

## [Domain-Specific-Review-Guidelines]
  
  ### **Domain-Based Review Process**
  Identify task domain first, then apply appropriate domain dimensions below. Use General Review if domain is unclear.

  ### **Scoring System (All Domains)**
  - **Platinum (4.0)**: Fully compliant, no issues
  - **Gold (3.0)**: Meets standards, 1-2 minor issues
  - **Silver (2.0)**: Minimum standards, 3-4 issues needing improvement
  - **Bronze (1.0)**: Below standards, serious issues or critical gaps
  - Calculate: overall_score = mean of dimension scores, round to 2 decimals

  ### **Decision Rules**
  - **Accept**: All dimensions ≥ 2.0, no critical issues
  - **Accept with Changes**: 1-2 dimensions ≥ 1.5 with clear improvement plan
  - **Reject**: 3+ dimensions < 2.0, or critical security/functional issues
  - **Risk**: Low (all ≥2.5), Medium (1-2 between 2.0-2.4), High (any <2.0 or security issues)

## [DoD]
  - [ ] Task domain has been identified and corresponding domain-specific review criteria have been applied
  - [ ] Scoring has been performed according to domain-specific scoring dimensions
  - [ ] All tests have been executed and results recorded
  - [ ] Integration tests have been executed to confirm implementation does not affect existing code and results recorded
  - [ ] Test results have been verified to align with the plan
  - [ ] Code alignment analysis is complete, including specific references to deviations from the plan
  - [ ] All necessary sections are present: Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items
  - [ ] "{EPIC}" has been updated with completion status and score
  - [ ] Test failures and plan misalignments have been clearly identified and prioritized
  - [ ] Acceptance decision has been recorded with rationale based on test results and plan adherence

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
- Score: API Design (4.0), Security (4.0), Error Handling (3.0), Testing (4.0) → Overall 3.75
- Decision: Accept (all dimensions ≥ 2.0, no critical issues)

[Expected Outcome]
- docs/review/1-review.md with test results, code alignment analysis, score 3.75
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
- Score: UI/UX (3.0), State Management (4.0), Performance (3.0), Accessibility (2.0), Testing (2.0) → Overall 2.8
- Decision: Accept with changes (accessibility and responsive design fixes needed)

[Expected Outcome]
- docs/review/2-review.md with failed test details (L42-L58), alignment gaps
- Action items: Fix accessibility (aria-labels, keyboard nav), add responsive breakpoints
- docs/epic.md updated with score 2.8, status: needs revision

### Example 3: Database Migration - Schema Update
[Input]
- Development notes: docs/dev-notes/3-dev-notes.md (Task-3: Add user preferences table)
- Implementation plan: docs/plans/3-plan.md (migration script, indexes, foreign keys)
- Template: review-tmpl.yaml

[Decision]
- Domain: Database (apply database scoring dimensions)
- Execute tests: npm run test:db (migration fails rollback test, missing index on user_id)
- Code alignment: Foreign key constraint missing from plan (migrations/003_user_preferences.sql:L15)
- Score: Schema Design (3.0), Indexing (2.0), Migration (1.0), Performance (2.0) → Overall 2.0
- Decision: Reject (migration script has critical issue, rollback fails)

[Expected Outcome]
- docs/review/3-review.md with critical findings: migration rollback failure
- Risk: High (data integrity risk if deployed)
- Action items: Fix rollback script, add missing index, re-test migration
- docs/epic.md: Task-3 status = failed review, requires rework
