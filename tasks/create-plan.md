**GOAL**: Create detailed TDD implementation plans for all tasks in epic, including RED/GREEN/REFACTOR three phases for each task.

## [Input]
  1. "{REQ}/*.md" --Project requirements
  2. "{ARCH}/*.md" --Architecture design
  3. "{EPIC}" --Feature-level task list
  4. "{TMPL}/implementation-plan-tmpl.yaml" --Implementation plan template (including: project information, requirement mapping, architecture reference, RED/GREEN/REFACTOR three phases, etc.)
  5. "{KNOWLEDGE}/*.md" --Project knowledge base (best practices, lessons learned, bug fixes)
  6. "{TMPL}/plan-tmpl.yaml" --Unified planning template; document coverage audits, plan production checklist, and validation checkpoints for this task

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
    - Create comprehensive plan.md at "{root}/docs/plan.md" using the plan template to track the working progress
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

### Good Example 1
[INPUT]
Task-1 from epic.md: "Implement article publishing". Requirements: REQ-001 (create/edit articles) with Given-When-Then acceptance criteria. Architecture: Article Service (Express.js), PostgreSQL. Template: implementation-plan-tmpl.yaml. Knowledge base available.

[DECISION]
Read epic, requirements, architecture, and knowledge base. Plan TDD three phases for Task-1. RED phase: define unit tests (Article model validation: title/content required, character limits), integration tests (API endpoints POST /articles, GET /articles/:id, PUT /articles/:id with database), behavior tests (complete publishing workflow Given-When-Then). GREEN phase: implement minimal Article model, create API endpoints, basic database operations. REFACTOR phase: add validation, error handling, apply repository pattern from knowledge base. Map to architecture: src/services/ArticleService.js. Create docs/plans/1-plan.md following template with complete requirement-architecture-test mapping.

[OUTCOME]
Complete docs/plans/1-plan.md with TDD structure. RED: Unit tests (model), Integration tests (API+DB), Behavior tests (workflow). GREEN: Minimal implementation steps mapped to architecture components. REFACTOR: Quality improvements with knowledge base patterns. All phases have clear atomic steps and component mappings.

[WHY-GOOD]
- Derives every planning detail from authoritative sources—requirements, architecture, knowledge—so the plan is grounded and traceable.
- Structures RED/GREEN/REFACTOR with atomic steps, providing developers a ready-to-execute roadmap.

### Good Example 2
[INPUT]
Task-2 from epic: "Build transaction report". Requirements: REQ-002 (aggregate by date range), NFR-001 (query <2s). Architecture: Reporting Service, TimescaleDB. Knowledge base: best-practices-database-queries.md.

[DECISION]
Review all inputs. Design TDD plan for Task-2. RED: Unit tests (aggregation logic: sum, group by date), Integration tests (TimescaleDB queries with real database, date range filtering, performance <2s requirement), Behavior tests (user generates monthly report Given-When-Then). GREEN: implement query with indexed date column, aggregation logic, minimal API. REFACTOR: add caching (Redis per knowledge base), optimize query using indexing best practices. Map steps to Reporting Service components. Create docs/plans/2-plan.md with complete traceability.

[OUTCOME]
docs/plans/2-plan.md following template structure. RED: Comprehensive test coverage including performance tests (<2s NFR). GREEN: Minimal SQL implementation. REFACTOR: Caching and optimization from knowledge base. Complete mapping to architecture components and requirements.

[WHY-GOOD]
- Integrates non-functional requirements and knowledge-based optimizations directly into the plan.
- Maintains template compliance and mapping discipline, ensuring downstream execution remains aligned with architecture.

### Bad Example 1
[INPUT]
Epic has 3 tasks. Requirements and architecture documented.

[BAD-DECISION]
Create plan for only Task-1, skip Task-2 and Task-3. Fabricate requirement IDs not in actual requirement documents. Skip RED phase planning entirely. In GREEN phase, list vague steps like "write some code". No architecture mapping. Ignore knowledge base completely. Save incomplete plans.

[WHY-BAD]
Violates Constraint 1 (fabricate requirements). Violates Constraint 2 (no complete requirement-architecture mapping). Violates Constraint 4 (ignore knowledge base). Violates TDD-Planning-Guidelines by skipping RED phase. Vague steps are not atomic and executable. Incomplete plans block development.

[CORRECT-APPROACH]
Follow Step 1: read all requirements, architecture, epic, and knowledge base first. Create plans for ALL tasks in epic per DoD. Use only actual requirement IDs from documents. Follow TDD-Planning-Guidelines: plan all three phases (RED/GREEN/REFACTOR) with atomic steps. Map every step to specific architecture components and requirement IDs. Apply knowledge base best practices in REFACTOR phase. Verify complete traceability before generating files.

### Bad Example 2
[INPUT]
Task requires database operations. Architecture specifies PostgreSQL. Knowledge base has caching best practices.

[BAD-DECISION]
Plan only unit tests in RED phase, skip integration and behavior tests. GREEN phase includes complex features and optimizations together (not minimal). REFACTOR phase is empty. No mention of PostgreSQL from architecture. Knowledge base practices ignored. Create plan without following template structure.

[WHY-BAD]
Violates TDD-Planning-Guidelines section 1 (RED should include normal, edge, error cases with unit AND integration AND behavior tests). GREEN phase should be minimal but includes optimization (belongs in REFACTOR). Violates Test-Case-Design-Guidelines by missing integration and behavior tests. Ignores architecture component details. No knowledge base leverage.

[CORRECT-APPROACH]
Follow Test-Case-Design-Guidelines completely. RED phase: Unit tests (business logic), Integration tests (PostgreSQL database operations), Behavior tests (Given-When-Then user scenarios). GREEN phase: Minimal code only - basic CRUD operations, simple queries. REFACTOR phase: Optimizations (indexes, caching from knowledge base), patterns (repository pattern), cross-cutting concerns. Map all to PostgreSQL component in architecture. Follow template structure exactly.
