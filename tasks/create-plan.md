**GOAL**: Create detailed TDD implementation plans for all tasks in epic, including RED/GREEN/REFACTOR three phases for each task.

## [Input]
  1. "{REQ}/*.md" --Project requirements
  2. "{ARCH}/*.md" --Architecture design
  3. "{EPIC}" --Feature-level task list
  4. "{TMPL}/implementation-plan-tmpl.yaml" --Implementation plan template (including: project information, requirement mapping, architecture reference, RED/GREEN/REFACTOR three phases, etc.)
  5. "{KNOWLEDGE}/*.md" --Project knowledge base (best practices, lessons learned, bug fixes)

## [Output]
  1. "{PLAN}/{task_id}-plan.md" --Implementation plans for all tasks (Markdown format)
    - Format: Use ATX headings; numbered lists; explicit requirement/architecture mapping sections
    - Content: Breaks down feature-level tasks into atomic implementation steps across TDD RED/GREEN/REFACTOR phases
    - Example: "{PLAN}/1-plan.md", "{PLAN}/2-plan.md", "{PLAN}/3-plan.md", etc.
  2. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not fabricate requirements or tasks not in source documents
  2. Do not create plans without complete requirement-architecture mapping
  3. Do not proceed if conflicts or missing files are found (must record and request clarification)
  4. Do not ignore knowledge base best practices when planning

## [Steps]
  1. Setup & Context Understanding
    - Understand all requirements, architecture, and task scope
    - Identify project-specific best practices and lessons learned
    - Create plan.md at "{root}/docs/plan.md" for progress tracking
    - Outcome: Complete context, planning criteria established, and plan.md initialized

  2. RED Phase Planning (For Each Task)
    - Plan complete test coverage with acceptance criteria
    - Define measurable success metrics and edge cases
    - Align with testing best practices from knowledge base
    - Outcome: Comprehensive test plan for each task

  3. GREEN Phase Planning (For Each Task)
    - Design atomic, executable implementation steps for minimal code
    - Map steps to architecture components and test conditions
    - Apply lessons learned to avoid known issues
    - Outcome: Clear minimal implementation roadmap

  4. REFACTOR Phase Planning (For Each Task)
    - Plan refactoring and optimization activities
    - Identify cross-cutting concerns and quality improvements
    - Incorporate best practices from knowledge base
    - Outcome: Quality improvement plan defined

  5. Finalization & Generation
    - Complete implementation plans for all tasks
    - Ensure plans follow template structure and are executable
    - Generate all plan files at "{PLAN}/{task_id}-plan.md"
    - Outcome: All implementation plans created and validated

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Epic summary (total tasks from epic.md)
  - Requirements and architecture context summary
  - Knowledge base review (best practices and lessons learned identified)
  - Planning progress for each task:
    * Task ID and description
    * RED phase planning status (test cases defined, coverage planned)
    * GREEN phase planning status (implementation steps outlined, architecture mapping done)
    * REFACTOR phase planning status (improvements and optimizations planned)
    * Completion status (pending/in-progress/completed)
  - Overall planning progress (e.g., "Completed 5/8 implementation plans")
  - Template compliance verification (all plans follow structure)
  - Traceability verification (requirement-architecture-test mapping complete)

## [TDD-Planning-Guidelines]
  1. **TDD Three-Phase Structure**
    - **RED Phase**: Define test cases from acceptance criteria; plan tests that will fail initially (normal, edge cases, error handling)
    - **GREEN Phase**: Plan minimal implementation to make tests pass; follow architecture mapping
    - **REFACTOR Phase**: Plan quality improvements (patterns, DRY, performance); plan integration with real APIs/services if needed
  
  2. **Atomic Step Breakdown**
    - Break feature-level tasks from epic into atomic, executable steps within each TDD phase
    - Each step must be minimal and directly traceable to acceptance criteria
    - Map steps to specific architecture components and requirement IDs
  
  3. **Leverage Knowledge Base**
    - Apply documented best practices from knowledge base
    - Avoid repeated mistakes by referencing error patterns
    - Incorporate lessons learned into planning
  
  4. **Traceability & Dependencies**
    - Ensure three-way mapping: Task ↔ Requirement ↔ Architecture
    - Identify execution dependencies and parallel opportunities
    - Exclude operational actions (git, npm) unless explicitly requested

## [Test-Case-Design-Guidelines]
  1. **Unit Test**
    - When to use: Test single function, class, or module logic in isolation with external dependencies mocked/stubbed
    - Key considerations: Cover normal paths, boundary conditions, error handling; ensure fast execution and repeatability
  
  2. **Integration Test**
    - When to use: Verify collaboration between multiple components (e.g., API + Database, Service + External API)
    - Key considerations: Test real dependency interactions and data flow correctness; use test containers or test environments
  
  3. **Behaviour Test**
    - When to use: Validate complete business workflows from user perspective (Given-When-Then format)
    - Key considerations: Align with acceptance criteria, simulate real user scenarios; use BDD frameworks (e.g., Cucumber, Behave)

## [DoD]
  - [ ] Implementation plan exists for each task with complete TDD three-phase structure (RED/GREEN/REFACTOR sections)
  - [ ] All plans have proper requirement-architecture-test mapping with specific file references
  - [ ] All plan files created at "{PLAN}/{task_id}-plan.md" following template structure

## [Example]

### Example 1: Content Management System - Article Publishing
[Input]
- Task-1 from epic.md: "Implement article publishing"
- Requirements: REQ-001 (create/edit articles), acceptance criteria in Given-When-Then format
- Architecture: Article Service (Express.js), PostgreSQL
- Template: implementation-plan-tmpl.yaml

[Decision]
- RED phase: Write tests for article CRUD operations (create, read, update)
  - Unit Test: Article model validation (title/content required, character limits)
  - Integration Test: API endpoints with database (POST /articles, GET /articles/:id, PUT /articles/:id)
  - Behaviour Test: Complete publishing workflow (Given user creates article → When submits → Then article appears)
- GREEN phase: Implement minimal Article model, API endpoints (POST /articles, GET /articles/:id, PUT /articles/:id)
- REFACTOR phase: Add validation, error handling, apply repository pattern

[Expected Outcome]
- docs/plans/1-plan.md with TDD three-phase structure
- RED: Unit tests (model logic), Integration tests (API + DB), Behaviour tests (user workflow)
- GREEN: Step-by-step implementation mapped to src/services/ArticleService.js
- REFACTOR: Planned improvements (DRY, SOLID principles)

### Example 2: Financial Dashboard - Transaction Report
[Input]
- Task-2 from epic.md: "Build transaction report"
- Requirements: REQ-002 (aggregate transactions by date range), NFR-001 (query < 2s)
- Architecture: Reporting Service, TimescaleDB
- Knowledge base: best-practices-database-queries.md

[Decision]
- RED phase: Write tests for date range filtering, aggregation accuracy, performance (< 2s)
  - Unit Test: Aggregation logic functions (sum, group by date)
  - Integration Test: TimescaleDB queries with real database (date range filtering, performance < 2s)
  - Behaviour Test: User generates monthly report (Given date range → When requests report → Then receives aggregated data)
- GREEN phase: Implement query with indexed date column, aggregation logic
- REFACTOR phase: Add caching (Redis), query optimization using knowledge base insights

[Expected Outcome]
- docs/plans/2-plan.md following template structure
- RED: Unit tests (aggregation functions), Integration tests (DB queries + performance), Behaviour tests (report generation)
- GREEN: Minimal SQL queries and API implementation
- REFACTOR: Caching strategy, index optimization from knowledge base

### Example 3: IoT Platform - Device Registration
[Input]
- Task-3 from epic.md: "Implement device registration"
- Requirements: REQ-003 (register device with unique ID), REQ-004 (device metadata storage)
- Architecture: Device Registry (gRPC), PostgreSQL
- Template: implementation-plan-tmpl.yaml

[Decision]
- RED phase: Tests for device registration, duplicate ID rejection, metadata validation
  - Unit Test: Metadata validation logic (required fields, format checks)
  - Integration Test: gRPC service with PostgreSQL (device insert, unique constraint enforcement)
  - Behaviour Test: Device onboarding flow (Given new device → When registers with metadata → Then stored and retrievable)
- GREEN phase: gRPC service stub, database insert with unique constraint
- REFACTOR phase: Add device status tracking, integrate with authentication service

[Expected Outcome]
- docs/plans/3-plan.md with complete TDD cycle
- RED: Unit tests (validation logic), Integration tests (gRPC + DB), Behaviour tests (onboarding flow)
- GREEN: Atomic steps mapped to proto files and database schema
- REFACTOR: Cross-cutting concerns (auth, logging) integration
