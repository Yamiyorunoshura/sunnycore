**GOAL**: Create feature-level task list (epic), breaking down requirements into executable tasks.

## [Input]
  1. "{REQ}/*.md" --Project functional and non-functional requirements
  2. "{ARCH}/*.md" --Architecture design and technical specifications
  3. "{TMPL}/epic-tmpl.yaml" --Epic template format

## [Output]
  1. "{EPIC}" --Task list (Markdown format)

## [Constraints]
  1. Must create feature-level tasks representing major features within modules (e.g., "Implement login functionality", "Implement registration functionality")
  2. Tasks should be verifiable at the feature level with clear functional scope and outcomes
  3. Must exclude operational actions unless explicitly requested by the user
    - Operational actions refer to execution-level commands such as git commit, npm install, etc., but design, implementation, testing and other development tasks do not fall into this category
  4. Must ensure all file names/paths do not use spaces; prefer kebab-case
  5. Note: Atomic breakdown of tasks will be handled later in the create-plan phase using TDD RED/GREEN/REFACTOR cycles

## [Tools]
  1. **todo_write**
    - [Step 1: Create task list; Steps 2-4: Track task progress]
  2. **sequential-thinking (MCP)**
    - [Step 1: Analyze requirement complexity and task dependencies]
    - [Step 2: Design feature-level tasks with logical grouping]
    - When to use: When need to decompose complex requirements or identify task dependencies

## [Steps]
  1. Research Phase
    - Understand requirements, architecture, and project scope
    - Identify success criteria and constraints for task design
    - Establish progress tracking mechanism for task design work

  2. Drafting Phase
    - Achieve feature-level task breakdown with proper grouping
    - Ensure each task represents a verifiable feature with clear scope
    - Ensure tasks are logically organized without overlap

  3. Review Phase
    - Ensure tasks are deduplicated and actionable
    - Ensure proper feature-level granularity and requirement traceability
    - Ensure format compliance with template requirements

  4. Finalization Phase
    - Achieve complete task list draft with clear introduction
    - Ensure user approval is obtained with proper feedback integration
    - Achieve final epic document saved to "{EPIC}"

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
  - [ ] All requirement and architecture documents have been read
  - [ ] Research notes are complete, including mapping of functional requirements/non-functional requirements to tasks
  - [ ] User approval has been obtained for task list draft
  - [ ] File "{EPIC}" exists and is valid Markdown
  - [ ] All tasks comply with template fields
  - [ ] Each task is feature-level, outcome-oriented, and verifiable
  - [ ] No file names or key names use spaces; kebab-case is enforced

## [Example]

### Example 1: Data Analytics Pipeline
[Input]
- Requirements: REQ-001 (data ingestion), REQ-002 (transformation), REQ-003 (visualization)
- Architecture: Kafka, Spark, Dashboard Service
- Template: epic-tmpl.yaml

[Decision]
- Task-1: Implement data ingestion (maps to REQ-001, Kafka Consumer)
- Task-2: Implement ETL pipeline (maps to REQ-002, Spark Jobs)
- Task-3: Build analytics dashboard (maps to REQ-003, Dashboard Service)

[Expected Outcome]
- docs/epic.md with 3 feature-level tasks
- Each task has clear DoD and requirement traceability
- Tasks are logically ordered: ingestion → transformation → visualization

### Example 2: Booking System
[Input]
- Requirements: REQ-001 (search availability), REQ-002 (create reservation), REQ-003 (payment processing)
- Architecture: Search API, Booking Service, Payment Gateway
- Template: epic-tmpl.yaml

[Decision]
- Task-1: Implement availability search (REQ-001 → Search API)
- Task-2: Implement booking creation (REQ-002 → Booking Service)
- Task-3: Integrate payment (REQ-003 → Payment Gateway)
- Dependencies: Task-3 depends on Task-2

[Expected Outcome]
- docs/epic.md with tasks ordered by dependencies
- Each task has requirement mapping and architecture component references
- No operational actions (git commit, npm install) included

### Example 3: Inventory Management
[Input]
- Requirements: REQ-001 (product CRUD), REQ-002 (stock tracking), REQ-003 (low stock alerts), REQ-004 (reporting)
- Architecture: Product Service, Inventory Service, Notification Service
- Template: epic-tmpl.yaml

[Decision]
- Task-1: Implement product management (REQ-001 → Product Service)
- Task-2: Implement stock tracking (REQ-002 → Inventory Service)
- Task-3: Build alert system (REQ-003 → Notification Service)
- Task-4: Create reports (REQ-004 → Inventory Service)

[Expected Outcome]
- docs/epic.md with 4 feature-level tasks
- 100% requirement coverage across tasks
- Each task description ≤14 characters, clear and actionable

Epic format with checkboxes:

- [ ] Task-{task_id}
  - {description of the task}
- [ ] Task-{task_id}
  - {description of the task}
- [ ] Task-{task_id}
  - {description of the task}
