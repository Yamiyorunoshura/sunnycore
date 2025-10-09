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

## [Constraints]
  1. Must strictly extract tasks from provided documents; do not fabricate requirements
  2. Must map each plan item to requirement ID and architecture section
  3. Must use Markdown format (ATX headings and numbered lists)
  4. Must produce exactly one file at the specified output path
  5. The produced implementation plan must ensure logical coherence of TDD three phases (refer to [Development-Guidelines] section for TDD methodology)
  6. If requirement-architecture conflicts, unclear requirements, or missing necessary files are found, must record issues and request user clarification, do not make assumptions or skip
  7. Must break down feature-level tasks (from epic.md) into atomic, executable steps within each TDD phase
  8. Each atomic step in GREEN phase should be minimal and directly traceable to a specific acceptance criterion in RED phase
  9. Must leverage knowledge base to apply best practices and avoid repeated mistakes when planning implementation steps

## [Tools]
  1. **todo_write**
    - [Step 1 (Setup Phase): Create todo list; Steps 2-4: Track task progress]
  2. **sequential-thinking (MCP)**
    - [Step 1: Analyze requirements and task complexity]
    - [Step 2: Plan RED phase - test and acceptance criteria design]
    - [Step 3: Plan GREEN phase - minimal implementation step design]
    - [Step 4: Plan REFACTOR phase - refactoring and optimization work identification]
    - When to use: When need to decompose complex tasks or design TDD workflow
  3. **claude-context (MCP)**
    - [Step 1: Search for relevant implementation references (if needed)]
  4. **context7 (MCP)**
    - [Step 3: Plan GREEN phase - When need to query official API usage and examples for external packages]
    - When to use: When implementation involves external SDK integration or need to verify package compatibility

## [Steps]
  1. Setup Phase
    - Understand all requirements, architecture, and task scope
    - Identify project-specific best practices and lessons learned
    - Establish progress tracking mechanism for plan creation work

  2. For Each Task: Planning RED Phase Content
    - Achieve complete test planning with acceptance criteria and test conditions
    - Ensure measurable success metrics and edge cases are defined
    - Ensure alignment with testing best practices from knowledge base

  3. For Each Task: Planning GREEN Phase Content
    - Achieve atomic, executable implementation steps for minimal code
    - Ensure proper mapping to architecture components and test conditions
    - Ensure application of lessons learned to avoid known issues

  4. For Each Task: Planning REFACTOR Phase Content
    - Achieve comprehensive refactoring and optimization plan
    - Ensure identification of cross-cutting concerns and quality improvements
    - Ensure incorporation of best practices from knowledge base

  5. Finalization Phase
    - Achieve complete implementation plans for all tasks
    - Ensure all plans follow template structure and are executable
    - Ensure all plan files are generated at "{PLAN}/{task_id}-plan.md"

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

## [DoD]
  - [ ] All requirement, architecture, and task documents have been read
  - [ ] Epic has been parsed and all tasks identified
  - [ ] For each task, a plan document has been created with TDD three-phase structure (RED/GREEN/REFACTOR sections)
  - [ ] RED section: Each requirement has corresponding acceptance criteria and test conditions
  - [ ] GREEN section: All implementation steps correspond to specific acceptance criteria and include architecture/file references
  - [ ] REFACTOR section: Refactoring and optimization work has been planned, including cross-cutting concerns integration
  - [ ] All plans follow TDD cycle structure: test-first (RED), minimal implementation (GREEN), refactoring optimization (REFACTOR)
  - [ ] Output path and file naming follow specified pattern
  - [ ] Implementation plan files have been created for all tasks (e.g., "{PLAN}/1-plan.md", "{PLAN}/2-plan.md", "{PLAN}/3-plan.md", etc.)

## [Example]

### Example 1: Content Management System - Article Publishing
[Input]
- Task-1 from epic.md: "Implement article publishing"
- Requirements: REQ-001 (create/edit articles), acceptance criteria in Given-When-Then format
- Architecture: Article Service (Express.js), PostgreSQL
- Template: implementation-plan-tmpl.yaml

[Decision]
- RED phase: Write tests for article CRUD operations (create, read, update)
- GREEN phase: Implement minimal Article model, API endpoints (POST /articles, GET /articles/:id, PUT /articles/:id)
- REFACTOR phase: Add validation, error handling, apply repository pattern

[Expected Outcome]
- docs/plans/1-plan.md with TDD three-phase structure
- RED: Test cases for happy path, edge cases (empty title, invalid ID)
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
- GREEN phase: Implement query with indexed date column, aggregation logic
- REFACTOR phase: Add caching (Redis), query optimization using knowledge base insights

[Expected Outcome]
- docs/plans/2-plan.md following template structure
- RED: Performance test asserting query time < 2s
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
- GREEN phase: gRPC service stub, database insert with unique constraint
- REFACTOR phase: Add device status tracking, integrate with authentication service

[Expected Outcome]
- docs/plans/3-plan.md with complete TDD cycle
- RED: Unit tests and integration tests for gRPC endpoint
- GREEN: Atomic steps mapped to proto files and database schema
- REFACTOR: Cross-cutting concerns (auth, logging) integration
