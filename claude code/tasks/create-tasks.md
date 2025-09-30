<input>
  <context>
    1. {root}/docs/requirements/*.md - Project functional and non-functional requirements
    2. {root}/docs/architecture/*.md - Architecture design and technical specifications
    3. {root}/sunnycore/templates/tasks-tmpl.yaml - Task template format
  </context>
  <templates>
    1. sunnycore/templates/tasks-tmpl.yaml - Standard task structure template
  </templates>
</input>

<output>
  1. Deliverables specification
     Format: Strict JSON Schema (additionalProperties=false)
</output>

<constraints importance="Important">
- MUST: Use 2-space indentation and kebab-case keys in YAML.
- MUST: Create atomic, verifiable tasks (≤14 words, clear outcome).
- MUST: Exclude operational actions unless explicitly requested by the user.
- MUST: Ensure no filenames/paths use spaces; prefer kebab-case.
- MUST: Produce valid JSON per schema (additionalProperties=false; no text outside JSON).
</constraints>

<workflow importance="Important">
  <stage id="1: research">
    - Read requirements and architecture sources.
    - Identify scope, success criteria, and constraints to drive task design.
    - Map non-functional requirements to cross-cutting tasks.
    - Deliverable: structured research notes mapping FR/NFR to task candidates.
    <tools>
      <tool name="todo_write"/>
      <tool name="sequential_thinking" description="Analyze requirements complexity and task dependencies"/>
    </tools>
    <questions>
    - Are all FRs and NFRs discoverable and current?
    - What dependencies or sequencing constraints exist between tasks?
    - What are acceptance signals for each task?
    </questions>
  </stage>

  <stage id="2: draft">
    - Use the template to generate atomic tasks.
    - Include brief acceptance hints for verifiability.
    - Group tasks logically while avoiding overlaps.
    - Deliverable: draft tasks JSON conforming to the schema.
    <tools>
      <tool name="todo_write"/>
      <tool name="sequential_thinking" description="Design atomic tasks and logical groupings"/>
    </tools>
  </stage>

  <stage id="3: review">
    - De-duplicate and prune non-actionable items.
    - Ensure traceability from each task to requirement(s).
    - Validate formatting against the template.
    - Deliverable: reviewed tasks JSON (schema-valid).
  </stage>

  <stage id="4: finalize">
    - Write markdown format tasks to {root}/docs/tasks.md from the JSON.
    - Include a short introduction explaining grouping and scope.
    - On JSON validation failure: auto-correct and retry up to 2 times.
    - Deliverable: {root}/docs/tasks.md created.

    <checks>
    - [ ] JSON passes schema validation (additionalProperties=false)
    - [ ] File {root}/docs/tasks.md exists and is valid Markdown.
    - [ ] Tasks conform to template fields and 2-space indentation.
    - [ ] Each task is atomic, outcome-oriented, and verifiable.
    - [ ] No filenames or keys use spaces; kebab-case enforced.
    </checks>
  </stage>
</workflow>

