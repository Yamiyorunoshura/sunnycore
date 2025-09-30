<input>
  <context>
  1. Transform initial ideas into complete, testable requirements through a structured, interactive workflow.
  2. Use the canonical requirement template to ensure consistency and verifiability.
  3. Maintain English-only prompt content; user communications may be multilingual.
  </context>
  <templates>
  1. {root}/sunnycore/templates/requirement-tmpl.yaml - Standard requirement template
  </templates>
</input>

<output>
1. {root}/docs/requirements/*.md - Complete requirement specifications including functional, non-functional, and acceptance criteria.
Format: JSON Schema
Example: {"requirements_manifest":{"file_count":1,"paths":["{root}/docs/requirements/requirements.md"],"includes":["functional-requirements","non-functional-requirements","acceptance-criteria"]},"notes":"Files must follow template structure; additionalProperties=false in validation"}
</output>

<constraints importance="Important">
- MUST: Each requirement is verifiable and measurable; no ambiguous or subjective phrasing.
- MUST: Use numbered lists; average sentence length < 20 words.
- MUST: Align section and field names exactly with the requirement template.
- MUST: Do not include sensitive or personal data in examples.
- MUST: Maintain English-only content throughout the prompt and generated documentation.
</constraints>

<workflow importance="Important">
  <stage id="1: init">
  <tools>
    <tool name="sequential_thinking" description="Structured decomposition and reflective reasoning">
    <tool name="todo_write" description="Manage execution tasks with statuses">
  </tools>
  - Read all working steps to understand the expected deliverables.
  </stage>

  <stage id="2: functional">
  <tools>
    <tool name="todo_write" description="Track functional analysis tasks and decisions"/>
    <tool name="sequential_thinking" description="Systematically decompose complex functional requirements"/>
    <tool name="playwright_browser" description="Perform web research for requirement examples when needed"/>
  </tools>
  - Derive functional requirements from the user's input and context.
  - Deduplicate and atomize statements (single testable condition).
  - Organize by user stories or system capabilities.

  <questions>
  - What are the core user goals and success criteria for each scenario?
  - Which preconditions, data contracts, and error states must be explicit?
  - Are there external integrations or upstream/downstream dependencies?
  </questions>
  </stage>

  <stage id="3: nonfunctional">
  <tools>
    <tool name="todo_write" description="Track non-functional analysis tasks"/>
    <tool name="sequential_thinking" description="Systematic NFR analysis across domains"/>
    <tool name="claude_context" description="Process large requirement documents in segments"/>
  </tools>
  - Identify non-functional requirements across performance, reliability, security, compliance, and operability.
  - Quantify targets (e.g., P95 latency, uptime SLO, RTO/RPO) and constraints.
  - Map NFRs to monitoring/observability signals when relevant.
  
  <questions>
  - What performance baselines and environment assumptions are in scope?
  - What threat model, data classification, or compliance scope applies?
  - How will we validate and observe these NFRs post-deployment?
  </questions>
  </stage>

  <stage id="4: acceptance">
  <tools>
    <tool name="todo_write" description="Track acceptance criteria authoring and validation"/>
    <tool name="sequential_thinking" description="Structure Given-When-Then and validation logic"/>
  </tools>
  - Define acceptance criteria per requirement; ensure they are deterministic and testable.
  - Structure Given-When-Then with inputs, preconditions, and pass/fail outcomes.
  - Validate each criterion can be automated or manually verified with binary outcomes.
  </stage>

  <stage id="5: finalize">
  - Cross-check FRs, NFRs, and acceptance criteria; request user's confirmation.
  - Populate the requirement template and write outputs under {root}/docs/requirements/.
  - Run "uv run {root}/sunnycore/scripts/shard-requirements.py"; document fallback on failure.

  <checks>
  - [ ] Outputs include FRs, NFRs, and acceptance criteria per template
  - [ ] English-only content and numbered lists used where applicable
  - [ ] Each requirement is measurable and verifiable (no ambiguity)
  - [ ] Sharding executed successfully or fallback documented
  - [ ] User confirmation obtained for final requirement set
  </checks>
  </stage>
</workflow>

