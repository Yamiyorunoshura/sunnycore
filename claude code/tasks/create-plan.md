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
  2. **sequentialthinking (MCP)**
    - [Step 1: Analyze requirement and task complexity; Step 2: Plan RED phase content (test and acceptance criteria design); Step 3: Plan GREEN phase content (minimal implementation step design); Step 4: Plan REFACTOR phase content (refactoring and optimization work identification)]
  3. **claude-context (MCP)**
    - [Step 1: Search codebase for relevant implementations if needed]

## [Steps]
  1. Setup Phase
    - Read all workflow steps and requirement documents
    - Read knowledge documents to understand project-specific best practices and lessons learned
    - Read "{EPIC}" to extract all tasks and their details
    - Parse task list to identify all task IDs and descriptions
    - Assess overall complexity based on total task count and architecture scope
    - Create todo list to track execution progress for all tasks

  2. For Each Task: Planning RED Phase Content
    - For each task in the epic, write the "RED Phase" section: break down the feature-level task into specific acceptance criteria and test conditions
    - Map requirements to testable outcomes and verification methods
    - Define measurable success metrics, failure conditions, and edge cases
    - Reference knowledge base for testing best practices and common pitfalls to avoid

  3. For Each Task: Planning GREEN Phase Content
    - For each task, write the "GREEN Phase" section: break down the feature into atomic, minimal implementation steps
    - Map each acceptance criterion to specific architecture components, files, and concrete development tasks
    - Each implementation step should be atomic, executable, and traceable to test conditions
    - Steps should be granular enough for straightforward implementation (e.g., "Create User model", "Add login endpoint", "Implement password validation")
    - Apply lessons learned from knowledge base to avoid known issues and follow established patterns

  4. For Each Task: Planning REFACTOR Phase Content
    - For each task, write the "REFACTOR Phase" section: list refactoring and optimization work after GREEN phase completion
    - Identify and integrate duplicate code, cross-cutting concerns (authentication, logging, error handling, etc.)
    - Plan performance optimizations, code quality improvements, and architecture enhancement steps
    - Incorporate best practices from knowledge base for code quality and maintainability improvements

  5. Finalization Phase
    - For each task, integrate content from Steps 2-4 into a complete implementation plan document
    - Format each plan using the template: reference template structure to organize content ensuring all necessary sections are included (requirement mapping, architecture reference, RED/GREEN/REFACTOR three phases, etc.)
    - Verify completeness and executability of each plan
    - Generate Markdown plan files to "{PLAN}/1-plan.md", "{PLAN}/2-plan.md", "{PLAN}/3-plan.md", etc.

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
