<input>
  <context>
    1. {root}/docs/requirements
    2. {root}/docs/architecture/*.md
    3. {root}/sunnycore/scripts/shard-architecture.sh - Architecture Script
  </context>
  <templates>
    {root}/sunnycore/templates/architecture-tmpl.yaml
  </templates>
</input>

<output>
1. {root}/docs/architecture/*.md
</output>

<constraints importance="Important">
- Read requirements and existing architecture before proposing designs.
- New modules must integrate without breaking existing contracts; include impact analysis for any proposed changes.
- Follow the template structure and section order consistently.
- Draft to {root}/docs/architecture.md, then run {root}/sunnycore/scripts/shard-architecture.sh to shard.
- Use clear, concise English and 2-space indentation.
</constraints>

<workflow importance="Critical">
  <stage id="0: plan-todos">
  - Read all working steps in this task.
  - Create todo items for each step using the todo-list tool.
  </stage>

  <stage id="1: assess-existing">
  - Read the current architecture under {root}/docs/architecture/*.md.
  - Identify extension points, constraints, and shared services.
  - Map affected domains, bounded contexts, and dependencies.
  </stage>

  <stage id="2: design-new-modules">
  - Define responsibilities, boundaries, and interfaces for new modules.
  - Specify data flows and interactions with existing components.
  - Evaluate non-functional needs (security, observability, performance) and compatibility.
  
  <questions>
  - Which extension points or APIs will the new modules rely on?
  - What contracts must be preserved to avoid regressions?
  - What data ownership or consistency implications arise?
  </questions>
  </stage>

  <stage id="3: author-and-shard">
  - Use the architecture template to draft {root}/docs/architecture.md.
  - Ensure sections emphasize new modules and integration impacts.
  - Run the sharding script to split the document:
    - bash '{root}/sunnycore/scripts/shard-architecture.sh'
  - Verify files appear under {root}/docs/architecture/.
  </stage>

  <stage id="4: finalize">
  - Cross-check against constraints and questions; fix gaps and inconsistencies.
  
  <checks>
  - [ ] New modules documented with boundaries, interfaces, and data flows
  - [ ] Compatibility with existing contracts articulated (no breaking changes)
  - [ ] {root}/docs/architecture.md exists and follows the template
  - [ ] Sharded files generated under {root}/docs/architecture/
  - [ ] Paths and commands reference {root}/sunnycore/scripts/shard-architecture.sh
  </checks>
  </stage>
</workflow>