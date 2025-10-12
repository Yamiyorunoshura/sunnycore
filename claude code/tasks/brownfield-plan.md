**GOAL**: Re-develop plan that failed review based on review feedback.

## [Input]
  1. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template
  2. "{REVIEW}/{task_id}-review.md" --Review report
  3. "{ARCH}/*.md" --Architecture design
  4. "{KNOWLEDGE}/*.md" --Project knowledge (if exist)

## [Output]
  1. Fixed code that runs properly
  2. Updated development notes "{DEVNOTES}/{task_id}-dev-notes.md" (Markdown format)

## [Constraints]
  1. Do not deliver fixes that fail to run properly
  2. Do not deviate from architecture design specifications
  3. Do not break existing functionality during fixes
  4. Follow the Development-Guidelines defined in sunnycore_dev

## [Steps]
  1. Issue Analysis & Planning
    - Understand issues from review report and architecture context
    - Formulate atomic fix tasks based on analysis
    - Outcome: Clear understanding of issues and fix plan created

  2. Test-Driven Fix Implementation
    - Establish progress tracking for fixes
    - Implement fixes ensuring all tests pass (RED → GREEN → REFACTOR)
    - Outcome: All unit tests and integration tests passing

  3. Documentation & Summary
    - Create comprehensive fix summary with evidence
    - Read existing development notes at "{DEVNOTES}/{task_id}-dev-notes.md"
    - Update existing dev notes with fix summary (do not create new file)
    - Outcome: Fix summary completed and development notes updated

## [DoD]
  - [ ] All unit and integration tests passed
  - [ ] Development notes updated

## [Example]

### Example 1: Failed Authentication Logic
[Input]
- Review report: docs/review/1-review.md (Reject: token validation fails for expired tokens)
- Dev notes: docs/dev-notes/1-dev-notes.md (original implementation)
- Architecture: JWT authentication with Redis token store

[Decision]
- Issue: Token expiry check missing (test_expired_token_rejection failed)
- Fix: Add token expiry validation before Redis lookup
- TDD: RED (write test for expiry check) → GREEN (add expiry logic) → REFACTOR (optimize Redis queries)

[Expected Outcome]
- Fixed code: src/auth/TokenValidator.js with expiry check (L25-L30)
- Fix summary: Changes (added expiry validation), Tests (test_expired_token_rejection now passes), Evidence (all auth tests pass), Risk (low), Rollback (revert commit abc123)
- Updated docs/dev-notes/1-dev-notes.md with fix details

### Example 2: Performance Issue in Query
[Input]
- Review report: docs/review/3-review.md (Accept with changes: NFR-001 violated, query takes 3s instead of < 500ms)
- Dev notes: docs/dev-notes/3-dev-notes.md (missing database index)
- Architecture: PostgreSQL with search functionality

[Decision]
- Issue: Missing index on search column (performance test failed)
- Fix: Add index on products.name column, optimize query
- TDD: RED (performance test < 500ms fails) → GREEN (add index, query passes) → REFACTOR (add query explain logging)

[Expected Outcome]
- Fixed code: migrations/add_product_name_index.sql, src/repositories/ProductRepository.js (optimized query)
- Fix summary: Changes (added index, rewrote query), Tests (performance test now passes at 120ms), Evidence (test output shows timing), Risk (medium - index creation on large table), Rollback (drop index migration)
- Updated docs/dev-notes/3-dev-notes.md
