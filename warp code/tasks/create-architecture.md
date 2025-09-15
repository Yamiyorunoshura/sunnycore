<input>
  <context>
  1. {root}/docs/requirements/*.md - Project requirements
  2. {root}/warp code/scripts/shard-architecture.sh - Sharding script
  </context>
  <templates>
  1. {root}/warp code/templates/architecture-tmpl.yaml - Architecture template
  </templates>
</input>

<output>
1. {root}/docs/architecture/*.md - Complete architecture documentation
</output>

<constraints importance="Important">
- Before authoring, create todo items for each workflow stage.
- Read all requirements under {root}/docs/requirements/*.md and decide macro architecture and key interactions before drafting.
- Draft using the architecture template to {root}/docs/architecture.md; include components, boundaries, data flows, risks, and decisions; preserve section order.
- After the draft, shard with: bash '{root}/sunnycore/scripts/shard-architecture.sh'; verify files under {root}/docs/architecture/.
- Use clear English and 2-space indentation; do not invent paths or files.
</constraints>

<workflow importance="Critical">
  <stage id="0: plan-todos">
  - Read all steps in this task.
  - Create todo items for each working stage with the todo-list tool.
  </stage>

  <stage id="1: research">
  - Read all requirements under {root}/docs/requirements/*.md.
  - Identify components, boundaries, and data flows.
  - Decide macro architecture and key interactions.
  
  <questions>
  - Are the requirements complete and up to date?
  - Which cross-cutting concerns (security, observability, performance) must be included?
  - Are there external systems or constraints that affect boundaries?
  </questions>
  </stage>

  <stage id="2: author">
  - Use the architecture template to draft {root}/docs/architecture.md.
  - Ensure sections cover components, interactions, data flow, risks, and decisions.
  - Run the sharding script to split the document:
    - bash '{root}/sunnycore/scripts/shard-architecture.sh'
  - Verify files appear under {root}/docs/architecture/.
  </stage>

  <stage id="3: finalize">
  - Cross-check against constraints and questions.
  - Fix typos and inconsistent terminology.
  
  <checks>
  - [ ] {root}/docs/architecture.md exists and follows the template
  - [ ] Sharded files generated under {root}/docs/architecture/
  - [ ] Section order and headings match the template
  - [ ] Paths and commands are valid in this repository
  - [ ] Language is clear, concise, and free of typos
  </checks>
  </stage>
</workflow>