**GOAL**: Execute TDD development based on implementation plan, completing single task implementation.

## [Input]
  1. "{PLAN}/{task_id}-plan.md" --Implementation plan
  2. "{ARCH}/*.md" --Architecture design
  3. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template

## [Output]
  1. "{DEVNOTES}/{task_id}-dev-notes.md" --Complete development notes document (Markdown format)
  2. High-quality, tested, refactored code implementation highly allign with the implementation plans
  3. Complete test coverage and test cases allign with the implementation plans

## [Constraints]
  1. Do not deviate from implementation plan's acceptance criteria and architecture mapping
  2. Do not skip TDD cycle (RED → GREEN → REFACTOR)
  3. Do not modify files outside plan scope without recording rationale in dev notes
  4. Do not deliver with failing tests (exit code must be 0)

## [Tools]
  1. **sequential-thinking (MCP)**
    - [Step 1: Analyze implementation plan complexity]
    - [Steps 2-4: Reason about implementation strategies and technical decisions for each TDD phase]
    - When to use: When need to evaluate implementation approaches or handle technical challenges
  2. **todo_write**
    - [Step 1: Create TDD phase todo list; Steps 2-5: Track implementation progress for each phase]
  3. **claude-context (MCP)**
    - [Step 1: Search codebase for implementation plan-related code, modules, and test cases]
    - Query examples: "Where is the related implementation?" "How to test this?" "What modules does this depend on?"
  4. **context7 (MCP)**
    - [Steps 2-4: When need external API calls, query official documentation and examples]

## [Blocking-Conditions]
  - missing critical inputs
  - unexpected RED failures
  - risky irreversible actions needing approval
  - tools lacking non-interactive flags
  
## [Steps]
  1. Preparation & Planning
    - Understand TDD implementation plan and three phases
    - Establish progress tracking mechanism
    - Outcome: Implementation plan understood and tracking established

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
    - Create complete development notes at "{DEVNOTES}/{task_id}-dev-notes.md"
    - Outcome: Acceptance criteria met and dev notes completed

## [Development-Guidelines]
  1. **TDD Practice (Mandatory)**
    - **RED Phase**: Write failing tests from acceptance criteria before any code; verify tests fail for the right reason
    - **GREEN Phase**: Implement minimal code to pass tests (exit code 0); follow architecture mapping strictly
    - **REFACTOR Phase**: Improve code quality while maintaining green tests; integrate real APIs/services; apply patterns and eliminate duplication
  
  2. **Code Quality Standards**
    - Apply SOLID principles (Single Responsibility, Open-Closed, Dependency Inversion)
    - Use meaningful names; keep functions ≤50 lines; avoid duplication (DRY)
    - Statically typed languages must compile successfully
  
  3. **Testing Requirements**
    - Minimum 80% coverage; critical logic requires 100%
    - Cover unit, integration, and E2E levels appropriately
    - Execute full test suite after every change; rollback on failures (exit code ≠ 0)
  
  4. **Documentation & Risk Management**
    - Record technical decisions, deviations, and rationale in dev notes
    - Link requirement IDs and architecture references
    - Identify risks (technical, dependency, timeline); document mitigation and rollback strategies

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
