**GOAL**: Execute TDD development based on implementation plan, completing single task implementation.

## [Input]
  1. "{PLAN}/{task_id}-plan.md" --Implementation plan
  2. "{ARCH}/*.md" --Architecture design
  3. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template

## [Output]
  1. "{DEVNOTES}/{task_id}-dev-notes.md" --Complete development notes document
  2. High-quality, tested, refactored code implementation highly allign with the implementation plans
  3. Complete test coverage and test cases allign with the implementation plans

## [Constraints]
  1. Must comply with acceptance criteria and architecture mapping defined in the implementation plan
  2. **Must use TDD methodology for development**: Follow the TDD practice guidelines detailed in [Development-Guidelines] section
  3. Development notes must preserve the indentation and numbering style used in the template
  4. Allowed to modify modules specified in the implementation plan and their test files, as well as necessary configuration files; if modification of files outside the plan is needed (referring to files not explicitly listed for modification in the implementation plan, including but not limited to: shared utility classes, configuration files, dependency injection settings, etc.), must record in development notes and explain the reason
  5. Development notes must include: implementation summary, technical decisions, risk considerations, test results, and other complete sections (refer to template)

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

## [Steps]
  1. Preparation Phase
    - Understand the TDD implementation plan and its three phases
    - Establish progress tracking mechanism for TDD cycle execution

  2. RED Phase: Test Implementation
    - Achieve complete test coverage with all planned test cases implemented
    - Ensure all tests fail with expected error messages instead of unexpected erorrs(e.g could not compile, syntax error, etc.)(RED status confirmed)

  3. GREEN Phase: Minimal Implementation
    - Achieve passing tests with minimal code implementation
    - Ensure implementation aligns with architecture mapping from the plan

  4. REFACTOR Phase: Code Quality Enhancement
    - Achieve improved code quality while maintaining green tests
    - Ensure all planned optimizations and cross-cutting concerns are applied

  5. Validation and Documentation Phase
    - Ensure all acceptance criteria are validated and met
    - Achieve complete development notes document at "{DEVNOTES}/{task_id}-dev-notes.md"

## [Development-Guidelines]
  1. **TDD Practice (Mandatory)**
    - **RED Phase**: Write failing tests from acceptance criteria before any code; verify tests fail for the right reason
    - **GREEN Phase**: Implement minimal code to pass tests (exit code 0); follow architecture mapping strictly
    - **REFACTOR Phase**: Improve code quality while maintaining green tests; integrate real APIs/services; apply patterns and eliminate duplication
    - Iterate RED→GREEN→REFACTOR until all acceptance criteria met; rollback immediately if tests fail during refactoring
  
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
  - [ ] All acceptance criteria from implementation plan are satisfied and verified
  - [ ] Test coverage is complete, covering all verification methods specified in the plan
  - [ ] Implementation is complete through full TDD cycle (RED → GREEN → REFACTOR) with all tests passing
  - [ ] Code implementation aligns with planned architecture components
  - [ ] Code quality meets standards (SOLID, DRY, functions ≤50 lines)
  - [ ] Complete development notes document exists at "{DEVNOTES}/{task_id}-dev-notes.md"
  - [ ] All outputs specified in [Output] are generated and consistent

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
