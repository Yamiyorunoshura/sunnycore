[Input]
  1. {root}/docs/requirements --Standardized requirement source
  2. {root}/docs/architecture/*.md --Existing architecture document collection
  3. {root}/sunnycore/scripts/shard-architecture.py --Architecture sharding script
  4. {root}/sunnycore/templates/architecture-tmpl.yaml --Architecture template

[Output]
  1. {root}/docs/architecture/*.md --Updated architecture document collection (*.md format)

[Constraints]
  1. Must thoroughly review {root}/docs/requirements and {root}/docs/architecture/*.md before proposing design (evidence: reference reviewed content in architecture draft using `Reference: {file path}#{section heading}` format)
  2. Must preserve existing contracts; any proposed changes must include explicit "Impact Analysis" subsection
  3. Must fully comply with {root}/sunnycore/templates/architecture-tmpl.yaml structure and section order
  4. Must draft to {root}/docs/architecture.md, then execute: uv run {root}/sunnycore/scripts/shard-architecture.py to perform sharding
  5. Should use clear, concise English with 2-space indentation throughout

[Tools]
  1. **todo_write**
    - [Step 1: Track tasks; Steps 2-4: Track task status]
  2. **sequentialthinking (MCP)**
    - [Step 1: Evaluate existing architecture]
    - [Step 2: Design module boundaries and integration patterns]
    - [Step 3: Structured drafting]
  3. **claude-context (MCP)**
    - [Step 1: Evaluate existing architecture - handling large document collections]

[Tool-Guidelines]
  1. **todo_write**
    - Create a todo list during evaluation phase, including all major tasks
    - Update the status of each completed step to completed
    - State gate: Only allow a single task to be in_progress; mark completed immediately after completion
  2. **sequentialthinking (MCP)**
    - Simple task reasoning: 1-3 totalThoughts
    - Medium task reasoning: 3-5 totalThoughts
    - Complex task reasoning: 5-8 totalThoughts
    - If still uncertain after completing the original reasoning steps: nextThoughtNeeded = true
    - Must complete all configured reasoning steps
  3. **claude-context (MCP)**
    - Usage scenario: When handling large existing architecture document collections
    - Can be used to read and understand complex architectures in segments
  4. **context7 (MCP)**
    - Usage scenario: Finding domain-specific best practices or researching specific technology stacks or design patterns
    - Used to find high-quality open source project practices that meet user needs, avoiding reinventing the wheel

[Steps]
  1. Evaluate Existing Architecture Phase
    - Review current architecture under {root}/docs/architecture/*.md
    - Identify extension points, constraints, and shared services
    - Map affected domains, bounded contexts, and dependencies
    - Create todo list to track subsequent design and writing tasks

  2. Design New Module Phase
    - Define responsibilities, boundaries, and interfaces of new module
    - Specify data flows and interaction methods with existing components
    - Assess non-functional requirements (security, observability, performance) and compatibility
    - Write "Impact Analysis" for all proposed changes to explain potential impact on existing system

  3. Writing and Sharding Phase
    - Use architecture template to draft {root}/docs/architecture.md in Markdown format
    - Ensure sections emphasize new module and integration impact
    - Execute sharding script to split documents: uv run {root}/sunnycore/scripts/shard-architecture.py
    - Verify documents appear under {root}/docs/architecture/

  4. Finalization Phase
    - Cross-check against constraints and guidance questions; fix gaps and inconsistencies
    - Confirm all impact analyses are included and complete
    - Verify compatibility between new and old modules
    - Check all DoD items one by one to ensure they are met
    - Confirm all todo items are completed

[DoD]
  - [ ] {root}/docs/requirements and {root}/docs/architecture/*.md have been thoroughly reviewed
  - [ ] Extension points, constraints, and affected domains have been identified
  - [ ] New module has documented boundaries, interfaces, and data flows
  - [ ] All proposed changes include explicit "Impact Analysis" subsections
  - [ ] Compatibility with existing contracts has been clarified (no breaking changes)
  - [ ] {root}/docs/architecture.md exists and follows the template
  - [ ] shard-architecture.py has been executed and shard file generation has been verified
  - [ ] All todo items are completed
