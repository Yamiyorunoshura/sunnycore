<input>
  <context>
  1. {root}/docs/implementation-plan/{task_id}-plan.md - Implementation Plan
  2. {root}/docs/architecture/*.md
  </context>
  <templates>
  1. {root}/sunnycore/templates/dev-notes-tmpl.yaml - Development Notes Template
  </templates>
</input>

<output>
1. {root}/docs/dev-notes/{task_id}-dev-notes.md - Complete Development Notes document
2. High-quality, tested code implementation
3. Complete test coverage and test cases
4. Refactored code that meets best practices
</output>

<constraints importance="Important">
- MUST: Adhere to acceptance criteria and architectural mappings defined in the implementation plan
- MUST: Follow the TDD cycle: implement tests first (RED), minimal code (GREEN), then refactor (REFACTOR)
- MUST: Preserve the semantics of <input> and <output> (semantic invariance)
- MUST: Preserve indentation and numbering styles used in this document
- MUST: Keep file paths exactly as specified; do not introduce new directories or files beyond those specified
</constraints>

<workflow importance="Important">
  <stage id="1: setup">
  <tools>
    <tool name="sequential_thinking" description="Plan steps and assumptions"/>
    <tool name="todo_write" description="Track tasks and status"/>
    <tool name="context_processor" description="Process large implementation plans in segments"/>
  </tools>
  - Read all working steps and the TDD-based implementation plan from the plan-tasks phase
  - Extract acceptance criteria and planned verification/test conditions
  </stage>
  
  <stage id="2: red_implement_tests">
  <tools>
    <tool name="todo_write" description="Record test authoring tasks"/>
    <tool name="sequential_thinking" description="Design test scenarios and edge cases"/>
  </tools>
  - Implement test cases based on acceptance criteria from the implementation plan (RED phase)
  - Convert each acceptance criterion into executable test code
  - Ensure tests fail initially as expected and validate planned coverage
  <questions>
  - Do implemented tests directly correspond to the plan's acceptance criteria?
  - Do tests fail appropriately before implementation begins?
  </questions>
  </stage>
  
  <stage id="3: green_minimal_implementation">
  <tools>
    <tool name="todo_write" description="Track implementation subtasks"/>
    <tool name="sequential_thinking" description="Design minimal solutions that make tests pass"/>
  </tools>
  - Implement minimal code to make tests pass (GREEN phase)
  - Follow the architectural mappings specified in the implementation plan
  - Ensure all tests transition from RED to GREEN
  <questions>
  - Does implementation follow the architecture components mapped in the plan?
  - Are solutions minimal and tied to specific tests?
  </questions>
  </stage>
  
  <stage id="4: refactor_optimize">
  <tools>
    <tool name="todo_write" description="Capture refactor tasks"/>
    <tool name="sequential_thinking" description="Identify optimization and consolidation opportunities"/>
  </tools>
  - Refactor while maintaining all tests green (REFACTOR phase)
  - Apply planned optimizations and cross-cutting concerns without reducing coverage
  - Enhance code quality and maintainability aligned with quality targets
  </stage>
  
  <stage id="5: validate_and_document">
  <tools>
    <tool name="sequential_thinking" description="Perform final validation"/>
    <tool name="todo_write" description="Complete documentation tasks"/>
  </tools>
  - Validate implementation against all acceptance criteria and planned test conditions
  - Generate development notes using the template
  - Output documentation to {root}/docs/dev-notes/{task_id}-dev-notes.md
  <checks>
  - [ ] All acceptance criteria from the implementation plan are satisfied
  - [ ] Tests cover all verification methods specified in the plan
  - [ ] Implementation follows the TDD cycle: RED → GREEN → REFACTOR
  - [ ] Code maps to architecture components as planned
  - [ ] All outputs in <output> are produced and consistent
  </checks>
  </stage>
</workflow>