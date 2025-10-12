**GOAL**: Execute TDD development based on implementation plan, completing single task implementation.

## [Input]
  1. "{PLAN}/{task_id}-plan.md" --Implementation plan
  2. "{ARCH}/*.md" --Architecture design
  3. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template

## [Output]
  1. "{DEVNOTES}/{task_id}-dev-notes.md" --Complete development notes document (Markdown format)
  2. High-quality, tested, refactored code implementation highly allign with the implementation plans
  3. Complete test coverage and test cases allign with the implementation plans
  4. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not deviate from implementation plan's acceptance criteria and architecture mapping
  2. Do not skip TDD cycle (RED → GREEN → REFACTOR)
  3. Do not modify files outside plan scope without recording rationale in dev notes
  4. Do not deliver with failing tests (exit code must be 0)
  5. Follow the Development-Guidelines defined in sunnycore_dev

## [Blocking-Conditions]
  - missing critical inputs
  - unexpected RED failures
  - risky irreversible actions needing approval
  - tools lacking non-interactive flags
  
## [Steps]
  1. Preparation & Planning
    - Understand TDD implementation plan and three phases
    - Create plan.md at "{root}/docs/plan.md" for progress tracking
    - Outcome: Implementation plan understood and plan.md initialized

  2. RED Phase: Test Implementation
    - Implement complete test coverage with all planned test cases
    - Ensure tests fail with expected errors (confirm RED status)
    - Outcome: All tests implemented and failing correctly

  3. GREEN Phase: Minimal Implementation
    - Implement minimal code to pass all tests
    - Align implementation with architecture mapping from plan
    - Outcome: All tests passing with minimal implementation

  4. REFACTOR Phase: Code Quality Enhancement
    - Improve code quality while maintaining green tests
    - Apply all planned optimizations and cross-cutting concerns
    - Outcome: High-quality code with all tests still passing

  5. Validation & Documentation
    - Validate all acceptance criteria are met
    - Check if "{DEVNOTES}/{task_id}-dev-notes.md" already exists
    - If exists: Update existing dev notes with new implementation details
    - If not exists: Create new dev notes from template
    - Outcome: Acceptance criteria met and dev notes completed (created or updated)

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Task identification (task ID and description from implementation plan)
  - Implementation plan summary (requirements, architecture mapping, acceptance criteria)
  - RED phase progress:
    * Test cases implemented (list with test names)
    * Test types (unit/integration/behaviour) with count
    * RED status verification (tests failing as expected: yes/no)
    * Test coverage planned vs achieved
  - GREEN phase progress:
    * Implementation files created/modified (list with file paths)
    * Architecture components implemented (list)
    * Test execution results (all passing: yes/no, failure details if any)
    * Minimal implementation verified (yes/no)
  - REFACTOR phase progress:
    * Refactoring activities performed (list)
    * Code quality improvements (patterns applied, DRY, SOLID)
    * Cross-cutting concerns integrated (logging, error handling, etc.)
    * Test status maintained (all still passing: yes/no)
  - Acceptance criteria validation (each criterion with met/not met status)
  - Code quality metrics (test coverage %, function length compliance, etc.)
  - Development notes status (created/updated at {DEVNOTES}/{task_id}-dev-notes.md)

## [DoD]
  - [ ] All acceptance criteria satisfied through full TDD cycle (RED → GREEN → REFACTOR) with all tests passing
  - [ ] Code quality meets standards (SOLID, DRY, functions ≤50 lines, coverage ≥80%)
  - [ ] Complete development notes document exists at "{DEVNOTES}/{task_id}-dev-notes.md"

## [Example]

### Example 1: E-commerce Cart Service - Add Item
[Input]
- Implementation plan: docs/plans/1-plan.md (Task-1: Implement add to cart)
- Architecture: Cart Service (Node.js/Express), Redis
- Template: dev-notes-tmpl.yaml

[Decision]
- RED: Write test_add_item_to_cart() asserting item added to Redis, test fails (no implementation yet)
- GREEN: Implement POST /cart endpoint, Redis HSET operation, test passes (exit code 0)
- REFACTOR: Add input validation, apply error handling pattern, ensure tests stay green

[Expected Outcome]
- Code: src/services/CartService.js with addItem() method, tests/CartService.test.js
- docs/dev-notes/1-dev-notes.md documenting TDD cycle, decisions, test results
- All acceptance criteria from plan met, test coverage ≥ 80%

### Example 2: Healthcare System - Patient Search
[Input]
- Implementation plan: docs/plans/2-plan.md (Task-2: Implement patient search by name/ID)
- Architecture: Patient Service (Python/FastAPI), PostgreSQL with full-text search
- Template: dev-notes-tmpl.yaml

[Decision]
- RED: Write test_search_patients() with assertions for name match, ID match, fuzzy search; tests fail
- GREEN: Implement GET /patients/search with SQL query using ILIKE, tests pass
- REFACTOR: Optimize with PostgreSQL full-text search (tsvector), add pagination, tests remain green

[Expected Outcome]
- Code: src/api/patient_routes.py, src/repositories/PatientRepository.py
- docs/dev-notes/2-dev-notes.md with performance optimization notes
- All tests pass, search response time meets NFR (< 500ms)

### Example 3: Real-time Notification - WebSocket Connection
[Input]
- Implementation plan: docs/plans/3-plan.md (Task-3: Implement WebSocket notification delivery)
- Architecture: Notification Gateway (Socket.io), Redis Pub/Sub
- Template: dev-notes-tmpl.yaml

[Decision]
- RED: Write test for connection establishment, message delivery, disconnection handling; tests fail
- GREEN: Implement Socket.io server, Redis subscriber, message broadcast logic; tests pass
- REFACTOR: Add connection pooling, heartbeat mechanism, apply error recovery pattern

[Expected Outcome]
- Code: src/gateways/NotificationGateway.js, tests/integration/websocket.test.js
- docs/dev-notes/3-dev-notes.md documenting WebSocket architecture decisions
- Integration tests pass, NFR met (message latency < 100ms)
