[Input]
  1. {root}/docs/requirements/*.md --Project functional and non-functional requirements
  2. {root}/docs/architecture/*.md --Architecture design and technical specifications
  3. {root}/sunnycore/templates/tasks-tmpl.yaml --Task template format

[Output]
  1. {root}/docs/epic.md --Task list (Markdown format)

[Constraints]
  1. Must create atomic, verifiable tasks (≤14 characters, clear outcomes)
  2. Must exclude operational actions unless explicitly requested by the user
    - Operational actions refer to execution-level commands such as git commit, npm install, etc., but design, implementation, testing and other development tasks do not fall into this category
  3. Must ensure all file names/paths do not use spaces; prefer kebab-case

[Tools]
  1. **todo_write**
    - [Step 1: Create task list; Steps 2-4: Track task progress]
  2. **sequentialthinking (MCP)**
    - [Step 1: Analyze requirement complexity and task dependencies; Step 2: Design atomic tasks and logical grouping]

[Steps]
  1. Research Phase
    - Verify all necessary input files (including templates) exist and are readable. If reading fails, stop responding and explicitly notify the user of missing file paths
    - Read requirement and architecture source documents
    - Identify scope, success criteria, and constraints to drive task design
    - Map non-functional requirements to cross-cutting tasks
    - Create todo list to track subsequent task design work

  2. Drafting Phase
    - Use template to generate atomic tasks
    - Include brief acceptance hints to ensure verifiability
    - Logically group tasks, avoid overlap
    - Deliverable: Task draft in Markdown format

  3. Review Phase
    - Deduplicate and remove non-actionable items
    - Ensure each task is traceable to requirements
    - Verify format complies with template requirements

  4. Finalization Phase
    - Write tasks to {root}/docs/epic.md (Markdown format)
    - Include brief introduction explaining grouping and scope
    - Check all DoD items one by one to ensure they are met
    - Confirm all todo items are completed

[DoD]
  - [ ] All requirement and architecture documents have been read
  - [ ] Research notes are complete, including mapping of functional requirements/non-functional requirements to tasks
  - [ ] File {root}/docs/epic.md exists and is valid Markdown
  - [ ] All tasks comply with template fields
  - [ ] Each task is atomic, outcome-oriented, and verifiable
  - [ ] No file names or key names use spaces; kebab-case is enforced
  - [ ] All todo items are completed
