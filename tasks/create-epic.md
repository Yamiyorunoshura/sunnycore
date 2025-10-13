**GOAL**: Create feature-level task list (epic), breaking down requirements into executable tasks.

## [Input]
  1. "{REQ}/*.md" --Project functional and non-functional requirements
  2. "{ARCH}/*.md" --Architecture design and technical specifications
  3. "{TMPL}/epic-tmpl.yaml" --Epic template format
  4. "{TMPL}/plan-tmpl.yaml" --Unified planning template; focus the plan on requirement coverage, task sequencing, and DoD alignment for this epic

## [Output]
  1. "{EPIC}" --Task list (Markdown format)
  2. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not create tasks below feature-level granularity
  2. Do not include operational actions unless explicitly requested
  3. Do not use spaces in file names/paths (use kebab-case)

## [Steps]
  1. Research & Planning
    - Understand requirements, architecture, and project scope
    - Identify success criteria and constraints
    - Create plan.md at "{root}/docs/plan.md" using the plan template to document coverage analysis, grouping strategy, and validation checkpoints
    - Outcome: Complete understanding, task design criteria established, and plan.md initialized

  2. Task Breakdown & Organization
    - Create feature-level task breakdown with proper grouping
    - Ensure each task represents verifiable feature with clear scope
    - Organize tasks logically without overlap
    - Outcome: Well-structured task list with clear boundaries

  3. Review & Refinement
    - Deduplicate and ensure tasks are actionable
    - Verify feature-level granularity and requirement traceability
    - Validate format compliance with template
    - Outcome: Refined task list meeting all quality criteria

  4. Finalization & Approval
    - Complete task list draft with clear introduction
    - Obtain user approval and integrate feedback
    - Save final epic document to "{EPIC}"
    - Outcome: Approved epic document created

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Requirements summary (total functional/non-functional requirements from REQ/*.md)
  - Architecture components summary (list of components from ARCH/*.md)
  - Task breakdown progress:
    * Total tasks identified
    * Tasks organized by logical grouping
    * Task descriptions refined (each ≤14 characters)
  - Requirement coverage tracking:
    * Requirements mapped to tasks (requirement ID → task ID)
    * Coverage percentage (target: 100%)
    * Unmapped requirements (if any)
  - Task traceability matrix:
    * Each task with requirement IDs and architecture component mappings
    * Dependencies identified between tasks
  - Review and refinement status (deduplication done, granularity verified)
  - User approval status (draft/approved)

## [Task-Design-Guidelines]
  1. **Feature-Level Tasks**
    - Each task represents a major feature (e.g., "Implement login", "Add export function")
    - Tasks should be completable within reasonable scope; description ≤ 14 characters
    - Clear and verifiable outcomes with specific DoD
  
  2. **Complete Traceability**
    - Map each task to specific requirement IDs and architecture components
    - Ensure 100% requirement coverage across all tasks
    - Identify and document dependencies between tasks
  
  3. **Results-Oriented**
    - Focus on deliverables and acceptance criteria, not implementation steps
    - Exclude operational actions (git commit, npm install) unless explicitly requested
    - Atomic breakdown will happen later in create-plan phase using TDD cycles

## [DoD]
  - [ ] Epic file exists at "{EPIC}" with all tasks feature-level, outcome-oriented, and properly mapped to requirements
  - [ ] Task list approved by user with 100% requirement coverage
  - [ ] All file names use kebab-case (no spaces)

## [Example]

### Good Example 1
[INPUT]
Requirements: REQ-001 (data ingestion), REQ-002 (ETL transformation), REQ-003 (dashboard visualization). Architecture: Kafka Consumer, Spark Jobs, Dashboard Service. Template: epic-tmpl.yaml.

[DECISION]
Understand requirements and architecture from docs. Identify feature-level tasks (not implementation steps). Task-1: "Implement data ingestion" (maps REQ-001 to Kafka Consumer, description ≤14 chars). Task-2: "Implement ETL pipeline" (maps REQ-002 to Spark Jobs). Task-3: "Build dashboard" (maps REQ-003 to Dashboard Service). Ensure 100% coverage: all 3 requirements mapped. Organize logically by data flow: ingestion→transformation→visualization. Define clear DoD for each task. Exclude operational actions. Obtain user approval. Save to docs/epic.md.

[OUTCOME]
docs/epic.md with 3 feature-level tasks in proper flow order. Each task has requirement traceability (REQ-ID→Task-ID→Component), clear description, and DoD. 100% requirement coverage verified. Task descriptions concise (≤14 characters). No operational actions included.

[WHY-GOOD]
- Translates requirements into feature-level tasks with full traceability, satisfying scope and coverage rules.
- Preserves naming and DoD standards, yielding an epic developers can act on immediately.

### Good Example 2
[INPUT]
Requirements: REQ-001 (product CRUD), REQ-002 (stock tracking), REQ-003 (low stock alerts), REQ-004 (reporting). Architecture: Product Service, Inventory Service, Notification Service.

[DECISION]
Map each requirement to architecture component systematically. Task-1: "Product CRUD" (REQ-001→Product Service). Task-2: "Stock tracking" (REQ-002→Inventory Service). Task-3: "Alert system" (REQ-003→Notification Service). Task-4: "Create reports" (REQ-004→Inventory Service). Verify 100% coverage: 4 requirements mapped to 4 tasks. Identify dependencies: Task-3 depends on Task-2 (alerts need stock data). Keep feature-level granularity (not atomic steps like "write test" or "git commit"). Generate epic with checkbox format. Obtain approval.

[OUTCOME]
docs/epic.md with 4 tasks covering all requirements. Dependencies documented (Task-3→Task-2). Each task mapped to specific architecture components. Descriptions ≤14 characters and actionable. No operational steps included (git, npm, docker commands excluded).

[WHY-GOOD]
- Maintains one-to-one requirement coverage while highlighting dependencies, which keeps planning coherent.
- Keeps every task at the required granularity and format, so later phases inherit clean inputs.

### Bad Example 1
[INPUT]
Requirements REQ-001, REQ-002, REQ-003 exist. Architecture documented.

[BAD-DECISION]
Break tasks down to atomic implementation level: "Task-1: Write unit tests", "Task-2: Create database migration", "Task-3: Run npm install", "Task-4: Commit code to git". Skip requirement mapping. Use long task descriptions (>14 characters). Include operational actions.

[WHY-BAD]
Violates Constraint 1 (tasks below feature-level granularity). Violates Constraint 2 (includes operational actions git, npm). Violates Task-Design-Guidelines point 1 (should be feature-level like "Implement login", not atomic steps). Breaks DoD requirement for feature-level outcomes. Tasks too granular for epic purpose.

[CORRECT-APPROACH]
Follow Task-Design-Guidelines: create feature-level tasks representing major deliverables. Example: "Implement login" (not "write auth test" + "create user table" + "commit code"). Map each task to requirements (REQ-ID→Task-ID). Keep descriptions ≤14 characters. Focus on deliverables with verifiable outcomes. Exclude operational actions (git, npm, docker) unless explicitly requested. Atomic breakdown happens later in create-plan phase.

### Bad Example 2
[INPUT]
Requirements REQ-001 through REQ-005 documented. Architecture has 3 components.

[BAD-DECISION]
Create 3 tasks mapping to architecture components but skip REQ-004 and REQ-005 mapping. Use spaces in file paths ("docs/epic doc.md"). No traceability matrix showing requirement→task→component mapping. Skip user approval step. Save with incorrect format.

[WHY-BAD]
Violates Constraint 3 (uses spaces in file paths, should use kebab-case). Violates Task-Design-Guidelines point 2 (missing 100% requirement coverage - REQ-004 and REQ-005 unmapped). Violates Step 4 (skip user approval). Missing traceability means can't verify coverage. Incomplete epic will cause gaps in implementation.

[CORRECT-APPROACH]
Create complete requirement→task→component traceability matrix per Task-Design-Guidelines section 2. Ensure 100% coverage: all 5 requirements must map to tasks. Use kebab-case for filenames: "docs/epic.md" not "docs/epic doc.md". Create traceability section showing: REQ-001→Task-1→ComponentA, REQ-002→Task-2→ComponentB, etc. Verify no orphaned requirements. Obtain user approval before finalizing. Follow template format exactly.
