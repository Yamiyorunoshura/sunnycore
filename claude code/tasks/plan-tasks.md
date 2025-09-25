<input>
  <context>
  1. {root}/docs/requirements/*.md
  2. {root}/docs/architecture/*.md
  3. {root}/docs/tasks.md
  </context>
  <templates>
  4. {root}/sunnycore/templates/implementation-plan-tmpl.yaml
  </templates>
</input>

<output>
1. {root}/docs/implementation-plan/{task_id}-plan.md
</output>

<constraints, importance = "Important">
- Derive tasks strictly from provided documents; do not invent requirements.
- Map every plan item to requirement IDs and architecture sections.
- Use Markdown with ATX headings; prefer numbered lists and concise bullets.
- Produce exactly one file at the specified output path.
</constraints>

<workflow, importance = "Important">
  <stage id="0: setup">
  - Read all working steps and requirements documents
  - Create a todo list markdown file at {root}/docs/plan-tasks-todo.md following the todo list format
  - Establish TDD cycle structure for task planning
  </stage>

  <stage id="1: red-define-tests">
  - Define acceptance criteria and test conditions for each requirement (RED phase)
  - Create measurable success metrics before designing implementation
  - Map requirements to testable outcomes and verification methods
  - Establish failure conditions and edge cases for each requirement

  <questions>
  - Are acceptance criteria specific, measurable, and verifiable?
  - Do test conditions cover both functional behavior and non-functional constraints?
  - Are edge cases and failure scenarios explicitly defined?
  </questions>
  </stage>

  <stage id="2: green-minimal-design">
  - Design minimal implementation plans that satisfy the defined acceptance criteria (GREEN phase)
  - Map each acceptance criterion to specific architecture components and tasks
  - Ensure each task directly addresses at least one test condition
  - Prioritize simplest solutions that make the "tests" pass

  <questions>
  - Does each implementation task map to specific acceptance criteria?
  - Are solutions minimal and focused on meeting defined test conditions?
  - Are architecture references complete and unambiguous?
  </questions>
  </stage>

  <stage id="3: refactor-optimize">
  - Refactor and optimize the implementation plan while maintaining test coverage (REFACTOR phase)
  - Consolidate duplicate efforts and identify cross-cutting concerns
  - Optimize task sequencing and dependencies for efficiency
  - Enhance solution quality without breaking acceptance criteria

  <questions>
  - Are cross-cutting concerns (auth, logging, i18n) properly consolidated?
  - Do optimizations maintain coverage of all acceptance criteria?
  - Are task dependencies and sequencing optimized to avoid blocking?
  </questions>
  </stage>

  <stage id="4: finalize">
  - Validate final plan against all defined acceptance criteria
  - Use the template to output the structured implementation plan
  - Generate Markdown plan to {root}/docs/implementation-plan/{task_id}-plan.md

  <checks>
  - [ ] Every requirement has corresponding acceptance criteria and test conditions
  - [ ] All implementation tasks map to specific acceptance criteria
  - [ ] Plan follows TDD cycle: test-first, minimal implementation, then refactor
  - [ ] Cross-cutting concerns are consolidated and optimized
  - [ ] Markdown uses ATX headings and numbered lists
  - [ ] Output path and file naming follow the specified pattern
  </checks>
  </stage>
</workflow>

<example>
markdown文件輸出方式：
	•	YAML 第一層 key 轉換為 Markdown 一級標題 (#)
	•	YAML 第二層 key 轉換為 Markdown 二級標題 (##)
	•	YAML 第三層 key 轉換為 Markdown 三級標題 (###)
	•	YAML value（字串或數字） 轉換為 Markdown 正文文字
</example>

<example>
todo list format for {root}/docs/plan-tasks-todo.md:

plan-tasks

# Stage 0: Setup
- [ ] Read all working steps and requirements documents
- [ ] Create a todo list markdown file
- [ ] Establish TDD cycle structure for task planning

# Stage 1: RED - Define Tests
- [ ] Define acceptance criteria and test conditions for each requirement
- [ ] Create measurable success metrics before designing implementation
- [ ] Map requirements to testable outcomes and verification methods
- [ ] Establish failure conditions and edge cases for each requirement

# Stage 2: GREEN - Minimal Design
- [ ] Design minimal implementation plans that satisfy acceptance criteria
- [ ] Map each acceptance criterion to specific architecture components and tasks
- [ ] Ensure each task directly addresses at least one test condition
- [ ] Prioritize simplest solutions that make the "tests" pass

# Stage 3: REFACTOR - Optimize
- [ ] Refactor and optimize the implementation plan while maintaining test coverage
- [ ] Consolidate duplicate efforts and identify cross-cutting concerns
- [ ] Optimize task sequencing and dependencies for efficiency
- [ ] Enhance solution quality without breaking acceptance criteria

# Stage 4: Finalize
- [ ] Validate final plan against all defined acceptance criteria
- [ ] Use the template to output the structured implementation plan
- [ ] Generate Markdown plan to docs/implementation-plan
</example>