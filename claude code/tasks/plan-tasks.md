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
Format: Markdown file using ATX headings; numbered lists; explicit requirement/architecture mapping sections.
Example: {root}/docs/implementation-plan/ABC-123-plan.md
</output>

<constraints importance="Important">
- MUST: Derive tasks strictly from provided documents; do not invent requirements.
- MUST: Map every plan item to requirement IDs and architecture sections.
- MUST: Use Markdown with ATX headings and numbered lists where applicable.
- MUST: Produce exactly one file at the specified output path.
</constraints>

<workflow importance="Important">
  <stage id="1: setup">
  <tools>
  <tool name="sequential_thinking" description="Plan analysis and step design">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer","minimum":1},"totalThoughts":{"type":"integer","minimum":1}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer"},"totalThoughts":{"type":"integer"}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </returns>
    <selection-rules>
    - Use for analysis/design steps; avoid for file editing or schema emission.
    - Prefer when complex trade-offs or sequencing decisions are required.
    </selection-rules>
  </tool>
  <tool name="todo_write" description="Manage execution tasks and statuses">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"merge":{"type":"boolean"},"todos":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"content":{"type":"string","minLength":3},"status":{"type":"string","enum":["pending","in_progress","completed","cancelled"]},"id":{"type":"string","minLength":3}},"required":["content","status","id"]}}},"required":["merge","todos"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"ok":{"type":"boolean"}},"required":["ok"]}
    </returns>
    <selection-rules>
    - Use to create/update task statuses at each stage boundary.
    - Do not use for storing operational actions; keep tasks high-level.
    </selection-rules>
  </tool>
  <tool name="claude_context" description="Process large documents in segments if needed">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"operation":{"type":"string","enum":["read","split","summarize"]},"target":{"type":"string"}},"required":["operation","target"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"chunks":{"type":"array","items":{"type":"string"}}},"required":["chunks"]}
    </returns>
    <selection-rules>
    - Use when input sources are lengthy or require segmentation.
    - Avoid when content is already in-memory and under token limits.
    </selection-rules>
  </tool>
  </tools>
  - Read all working steps and requirements documents
  - Establish TDD cycle structure for task planning
  </stage>

  <stage id="2: red_define_tests">
  <tools>
  <tool name="sequential_thinking" description="Analyze requirements complexity and design test conditions">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer","minimum":1},"totalThoughts":{"type":"integer","minimum":1}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer"},"totalThoughts":{"type":"integer"}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </returns>
    <selection-rules>
    - Use to enumerate acceptance criteria, tests, and edge cases.
    </selection-rules>
  </tool>
  <tool name="todo_write" description="Track RED-phase tasks">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"merge":{"type":"boolean"},"todos":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"content":{"type":"string","minLength":3},"status":{"type":"string","enum":["pending","in_progress","completed","cancelled"]},"id":{"type":"string","minLength":3}},"required":["content","status","id"]}}},"required":["merge","todos"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"ok":{"type":"boolean"}},"required":["ok"]}
    </returns>
    <selection-rules>
    - Update tasks as acceptance criteria are drafted and finalized.
    </selection-rules>
  </tool>
  </tools>
  - Define acceptance criteria and test conditions for each requirement (RED phase)
  - Map requirements to testable outcomes and verification methods
  - Create measurable success metrics; define failure conditions and edge cases

  <questions>
  - Are acceptance criteria specific, measurable, and verifiable?
  - Do test conditions cover both functional behavior and non-functional constraints?
  - Are edge cases and failure scenarios explicitly defined?
  </questions>
  </stage>

  <stage id="3: green_minimal_design">
  <tools>
  <tool name="sequential_thinking" description="Design minimal implementation approaches">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer","minimum":1},"totalThoughts":{"type":"integer","minimum":1}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer"},"totalThoughts":{"type":"integer"}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </returns>
    <selection-rules>
    - Use to select simplest implementation path that satisfies tests.
    </selection-rules>
  </tool>
  <tool name="todo_write" description="Track GREEN-phase tasks">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"merge":{"type":"boolean"},"todos":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"content":{"type":"string","minLength":3},"status":{"type":"string","enum":["pending","in_progress","completed","cancelled"]},"id":{"type":"string","minLength":3}},"required":["content","status","id"]}}},"required":["merge","todos"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"ok":{"type":"boolean"}},"required":["ok"]}
    </returns>
    <selection-rules>
    - Update tasks as design decisions are made and dependencies resolved.
    </selection-rules>
  </tool>
  </tools>
  - Design minimal implementation plans that satisfy the defined acceptance criteria (GREEN phase)
  - Map each acceptance criterion to specific architecture components and tasks
  - Ensure each task addresses at least one test condition; prioritize simplest solutions

  <questions>
  - Does each implementation task map to specific acceptance criteria?
  - Are solutions minimal and focused on meeting defined test conditions?
  - Are architecture references complete and unambiguous?
  </questions>
  </stage>

  <stage id="4: refactor_optimize">
  <tools>
  <tool name="sequential_thinking" description="Identify consolidation opportunities and optimize sequencing">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer","minimum":1},"totalThoughts":{"type":"integer","minimum":1}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer"},"totalThoughts":{"type":"integer"}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </returns>
    <selection-rules>
    - Use to consolidate cross-cutting concerns and optimize sequencing.
    </selection-rules>
  </tool>
  <tool name="todo_write" description="Track REFACTOR-phase tasks">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"merge":{"type":"boolean"},"todos":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"content":{"type":"string","minLength":3},"status":{"type":"string","enum":["pending","in_progress","completed","cancelled"]},"id":{"type":"string","minLength":3}},"required":["content","status","id"]}}},"required":["merge","todos"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"ok":{"type":"boolean"}},"required":["ok"]}
    </returns>
    <selection-rules>
    - Use when refactors are planned/applied to keep task list consistent.
    </selection-rules>
  </tool>
  </tools>
  - Refactor and optimize the implementation plan while maintaining test coverage (REFACTOR phase)
  - Consolidate duplicate efforts and cross-cutting concerns
  - Optimize task sequencing and dependencies for efficiency without breaking acceptance criteria

  <questions>
  - Are cross-cutting concerns (auth, logging, i18n) properly consolidated?
  - Do optimizations maintain coverage of all acceptance criteria?
  - Are task dependencies and sequencing optimized to avoid blocking?
  </questions>
  </stage>

  <stage id="5: finalize">
  <tools>
  <tool name="sequential_thinking" description="Final validation of deliverables">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer","minimum":1},"totalThoughts":{"type":"integer","minimum":1}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"thought":{"type":"string"},"nextThoughtNeeded":{"type":"boolean"},"thoughtNumber":{"type":"integer"},"totalThoughts":{"type":"integer"}},"required":["thought","nextThoughtNeeded","thoughtNumber","totalThoughts"]}
    </returns>
    <selection-rules>
    - Use to verify checks and acceptance criteria before completion.
    </selection-rules>
  </tool>
  <tool name="todo_write" description="Close tasks and record completion">
    <parameters>
    {"type":"object","additionalProperties":false,"properties":{"merge":{"type":"boolean"},"todos":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"content":{"type":"string","minLength":3},"status":{"type":"string","enum":["pending","in_progress","completed","cancelled"]},"id":{"type":"string","minLength":3}},"required":["content","status","id"]}}},"required":["merge","todos"]}
    </parameters>
    <returns>
    {"type":"object","additionalProperties":false,"properties":{"ok":{"type":"boolean"}},"required":["ok"]}
    </returns>
    <selection-rules>
    - Use to mark all tasks done and close the workflow.
    </selection-rules>
  </tool>
  </tools>
  - Validate final plan against all defined acceptance criteria
  - Use the template to output the structured implementation plan
  - Generate Markdown plan to {root}/docs/implementation-plan/{task_id}-plan.md

  <checks>
  - [ ] Every requirement has corresponding acceptance criteria and test conditions
  - [ ] All implementation tasks map to specific acceptance criteria
  - [ ] Plan follows TDD cycle: test-first, minimal implementation, then refactor
  - [ ] Cross-cutting concerns are consolidated and optimized
  - [ ] Output path and file naming follow the specified pattern
  </checks>
  </stage>
</workflow>

