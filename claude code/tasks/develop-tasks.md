<input>
  <context>
  1. {root}/docs/implementation-plan/{task_id}-plan.md - Implementation Plan (實作計劃)
  2. {root}/docs/architecture/*.md
  </context>
  <templates>
  1. {root}/sunnycore/templates/dev-notes-tmpl.yaml - Development Notes Template
  </templates>
</input>

<output>
1. {root}/docs/dev-notes/{task_id}-dev-notes.md - 完整的Development Notes文檔
2. high quality, tested code implementation
3. complete Test Coverage and Test Cases
4. refactored code that meets best practices
</output>

<constraints, importance = "Important">
- MUST adhere to acceptance criteria and architectural mappings defined in the implementation plan
- MUST follow TDD cycle: implement tests first (RED), minimal code (GREEN), then refactor (REFACTOR)
- Keep file paths exactly as specified in <input> and <output>
- Preserve indentation and numbering styles used in this document
- Do not change the semantics of <input> and <output>
- Avoid introducing new directories or files beyond those specified
</constraints>

<workflow, importance = "Important">
  <stage id="1: setup">
  - Read all working steps and the TDD-based implementation plan from plan-tasks phase
  - Extract acceptance criteria and test conditions defined in the implementation plan
  </stage>
  
  <stage id="2: red-implement-tests">
  - Implement test cases based on acceptance criteria from the implementation plan (RED phase)
  - Convert each acceptance criterion into executable test code
  - Ensure tests fail initially as expected (RED state)
  - Validate test coverage matches the planned verification methods

  <questions>
  - Do implemented tests directly correspond to acceptance criteria from the plan?
  - Are all edge cases and failure scenarios from the plan covered in tests?
  - Do tests fail appropriately before implementation begins?
  </questions>
  </stage>
  
  <stage id="3: green-minimal-implementation">
  - Implement minimal code to make tests pass (GREEN phase)
  - Follow the architectural mappings specified in the implementation plan
  - Focus on making tests green with simplest possible solutions
  - Implement both functional and non-functional requirements as planned

  <questions>
  - Does implementation follow the architecture components mapped in the plan?
  - Are solutions minimal and focused on making specific tests pass?
  - Do all tests transition from RED to GREEN state?
  </questions>
  </stage>
  
  <stage id="4: refactor-optimize">
  - Refactor code while maintaining all tests green (REFACTOR phase)
  - Apply optimizations and consolidations identified in the implementation plan
  - Implement cross-cutting concerns as specified in the plan
  - Enhance code quality without breaking test coverage

  <questions>
  - Does refactoring maintain all acceptance criteria from the plan?
  - Are cross-cutting concerns implemented as specified in the plan?
  - Do optimizations align with the plan's quality targets?
  </questions>
  </stage>
  
  <stage id="5: validate-and-document">
  - Validate final implementation against all acceptance criteria from the plan
  - Ensure all planned test conditions are satisfied
  - Generate development notes using the template
  - Output documentation to {root}/docs/dev-notes/{task_id}-dev-notes.md

  <checks>
  - [ ] All acceptance criteria from implementation plan are satisfied
  - [ ] Tests cover all verification methods specified in the plan
  - [ ] Implementation follows TDD cycle: RED → GREEN → REFACTOR
  - [ ] Code maps to architecture components as planned
  - [ ] All outputs in <output> are produced and consistent
  - [ ] Development notes document the TDD process and plan adherence
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
