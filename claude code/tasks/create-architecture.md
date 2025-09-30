<input>
  <context>
  1. {root}/docs/requirements/*.md - Authoritative project requirements
  2. {root}/sunnycore/scripts/shard-architecture.py - Architecture sharding script
  </context>
  <templates>
  1. {root}/sunnycore/templates/architecture-tmpl.yaml - Canonical architecture template
  </templates>
</input>

<output>
1. Architecture corpus
  Format: Files (*.md) under {root}/docs/architecture/
  Example: {root}/docs/architecture/
</output>

<constraints importance="Critical">
- MUST: Verify {root}/docs/requirements/*.md exists and is complete before architecture design.
- MUST: Create explicit requirement-to-architecture mapping covering functional and non-functional requirements.
- MUST: Validate that every requirement has a corresponding architectural component or design decision.
- MUST: Author {root}/docs/architecture.md with the canonical template; strictly preserve section ordering and 2-space indentation; do not introduce non-existent paths.
- MUST: After drafting, run 'uv run {root}/sunnycore/scripts/shard-architecture.py' and verify artifacts materialize under {root}/docs/architecture/.
</constraints>

<example>
Example: Minimal expected files generated under {root}/docs/architecture/
- {root}/docs/architecture/overview.md
- {root}/docs/architecture/components.md
- {root}/docs/architecture/traceability_matrix.md
</example>

<workflow importance="Critical">
  <stage id="1: requirement_analysis">
  <tools>
  <tool name="todo_write" description="Track and update execution tasks"/>
  <tool name="sequential_thinking" description="Decompose requirements and identify architectural patterns"/>
  </tools>
  - Verify completeness and consistency of all requirements under {root}/docs/requirements/*.md.
  - Extract functional/non-functional requirements and translate NFRs into architectural constraints.
  - Create mapping matrix (Requirement ID → Component/Decision) and identify gaps or conflicts.

  <questions>
  - Are all functional requirements mapped to specific architectural components?
  - Do non-functional requirements translate to measurable architectural constraints?
  - Are there conflicting requirements that need architectural trade-off decisions?
  </questions>
  </stage>

  <stage id="2: architecture_design">
  <tools>
  <tool name="sequential_thinking" description="Architect system components and validate design decisions"/>
  <tool name="context7" description="Fetch external package and architectural pattern references"/>
  <tool name="todo_write" description="Update task statuses during design"/>
  </tools>
  - Delineate components, boundaries, and canonical data flows based on requirement analysis.
  - Ensure every requirement maps to an architectural element; define interaction contracts and data patterns.
  - Document decisions with requirement traceability and address cross-cutting concerns (security, observability, performance).

  <questions>
  - Does the proposed architecture address all identified requirements?
  - Are architectural decisions traceable back to specific requirements?
  - How will non-functional requirements be validated in this architecture?
  </questions>
  </stage>

  <stage id="3: author">
  <tools>
  <tool name="todo_write" description="Track authoring progress and results"/>
  <tool name="sequential_thinking" description="Structure drafting and verification steps"/>
  </tools>
  - Draft {root}/docs/architecture.md using {root}/sunnycore/templates/architecture-tmpl.yaml.
  - Include the requirement traceability matrix and ensure every mapping is addressed.
  - Execute 'uv run {root}/sunnycore/scripts/shard-architecture.py' and verify artifacts under {root}/docs/architecture/.
  </stage>

  <stage id="4: final_validation">
  <tools>
  <tool name="sequential_thinking" description="Run final validation sequence"/>
  <tool name="todo_write" description="Close tasks with final statuses"/>
  </tools>
  - Cross-validate the architecture against all requirements via the mapping matrix.
  - Remediate typographical issues and normalize terminology.
  - Confirm architectural decisions are justified by requirements.
  
  <checks>
  - [ ] {root}/docs/architecture.md exists and adheres to the template
  - [ ] All requirements from {root}/docs/requirements/*.md are mapped to architectural elements
  - [ ] Requirement traceability matrix exists at {root}/docs/architecture/traceability_matrix.md and is complete and accurate
  - [ ] Non-functional requirements are expressed as measurable architectural constraints
  - [ ] Sharded files are generated under {root}/docs/architecture/ and paths/commands are valid
  </checks>
  </stage>
</workflow>

