<input>
  <context>
    1. {root}/docs/requirements - Canonical requirements source
    2. {root}/docs/architecture/*.md - Existing architecture corpus
    3. {root}/sunnycore/scripts/shard-architecture.py - Architecture sharding script
  </context>
  <templates>
    {root}/sunnycore/templates/architecture-tmpl.yaml
  </templates>
</input>

<output>
1. {root}/docs/architecture/*.md - Updated architecture documentation set
  Format: Files under {root}/docs/architecture/ matching *.md
</output>

<constraints importance="Important">
- MUST: Thoroughly review {root}/docs/requirements and {root}/docs/architecture/*.md before proposing designs (evidence: cite reviewed sections in draft).
- MUST: Preserve existing contracts; include an explicit "Impact Analysis" subsection for any proposed changes.
- MUST: Follow {root}/sunnycore/templates/architecture-tmpl.yaml structure and section order exactly.
- MUST: Draft into {root}/docs/architecture.md, then execute: uv run '{root}/sunnycore/scripts/shard-architecture.py' to shard.
- SHOULD: Use clear, concise English and 2-space indentation throughout.
</constraints>

<workflow importance="Critical">
  <stage id="1: assess_existing">
  <tools>
  <tool name="sequential_thinking"/>
  <tool name="todo_write">
  <tool name="Claude-Context" description="Process large architecture corpus in segments"/>
  </tools>
  - Examine the current architecture under {root}/docs/architecture/*.md.
  - Identify extension points, constraints, and shared services.
  - Map affected domains, bounded contexts, and dependencies.
  </stage>

  <stage id="2: design_new_modules">
  <tools>
  <tool name="sequential_thinking" description="Design module boundaries and integration patterns"/>
  <tool name="context7_integration" description="Research architectural patterns and best practices"/>
  <tool name="todo_write"/>
  </tools>
  - Define responsibilities, boundaries, and interfaces for new modules.
  - Specify data flows and interactions with existing components.
  - Evaluate non-functional requirements (security, observability, performance) and compatibility.
  
  <questions>
  - Which extension points or APIs will the new modules depend on?
  - Which contracts must be preserved to preclude regressions?
  - What data ownership or consistency implications emerge?
  </questions>
  </stage>

  <stage id="3: author_and_shard">
  <tools>
  <tool name="sequential_thinking"/>
  <tool name="todo_write">
  </tool>
  - Use the architecture template to draft markdown formatted {root}/docs/architecture.md.
  - Ensure sections emphasize new modules and integration impacts.
  - Run the sharding script to split the document: uv run '{root}/sunnycore/scripts/shard-architecture.py'
  - Verify files appear under {root}/docs/architecture/.
  </stage>

  <stage id="4: finalize">
  - Cross-check against constraints and guiding questions; remedy gaps and inconsistencies.
  
  <checks>
  - [ ] New modules documented with boundaries, interfaces, and data flows
  - [ ] Compatibility with existing contracts articulated (no breaking changes)
  - [ ] {root}/docs/architecture.md exists and adheres to the template
  - [ ] Sharded files generated under {root}/docs/architecture/
  - [ ] Paths and commands reference {root}/sunnycore/scripts/shard-architecture.py
  </checks>
  </stage>
</workflow>

