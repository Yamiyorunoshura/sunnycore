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
</output>

<constraints importance="Important">
- Each requirement must be verifiable and measurable; avoid ambiguous or subjective phrasing.
- Use numbered lists and concise sentences (average < 20 words) for scannability.
- Align sections and field names exactly with the requirement template.
- Do not include sensitive or personal data in examples.
- Clarify the requirements and the acceptance criteria with the user.
- MUST maintain English-only content throughout the prompt and generated documentation.
</constraints>

<workflow importance="Important">
  <stage id="1: init">
  <tools>
  - sequential_thinking
  - todo_write
  </tools>
  - Read all working steps to understand the expected deliverables.
  </stage>

  <stage id="2: functional">
  <tools>
  - todo_write
  - Analysis: Consolidate and organize requirements by user stories or capabilities
  - Sequential Thinking Tool: Decompose complex functional requirements systematically
  - Playwright Browser Automation: Perform web research for requirement examples if needed
  </tools>
  - Derive functional requirements from the user's input and context.
  - Consolidate duplicates using comparison criteria: same trigger condition, same outcome, same user role.
  - Remove ambiguity by ensuring each statement is atomic (single testable condition).
  - Organize by user stories or system capabilities as appropriate.

  <questions>
  - What are the core user goals and success criteria for each scenario?
  - Which preconditions, data contracts, and error states must be explicit?
  - Are there external integrations or upstream/downstream dependencies?
  </questions>
  </stage>

  <stage id="3: nonfunctional">
  <tools>
  - todo_write
  - Sequential Thinking Tool: Systematically analyze NFRs across performance, security, and compliance domains
  - Claude-Context: Process large requirement documents in segments
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
  - todo_write
  - sequential_thinking
  </tools>
  - Define acceptance criteria per requirement; ensure they are deterministic and testable.
  - Reference inputs, preconditions, and explicit pass/fail outcomes using Given-When-Then format when helpful.
  - Use clear structure; Gherkin-style is acceptable if helpful.
  - Validate each criterion can be automated or manually verified with binary outcomes.
  </stage>

  <stage id="5: finalize">
  - Cross-check consistency across FRs, NFRs, and acceptance criteria and ask for user's confirmation.
  - Populate the requirement template and place markdown formatted outputs under {root}/docs/requirements/.
  - Run the {root}/sunnycore/scripts/shard-requirements.py script by using uv run to shard the requirements.
  - Handle script execution failures: if sharding fails, document requirements in single file and notify user of manual sharding requirement.

  <checks>
  - [ ] Outputs include FRs, NFRs, and acceptance criteria per template
  - [ ] All content is written in English and uses numbered lists where applicable
  - [ ] Each requirement is measurable and verifiable (no ambiguity)
  - [ ] File paths and names match {root}/docs/requirements/*.md
  - [ ] Sensitive data has not been introduced in examples
  - [ ] The requirements are sharded into {root}/docs/requirements/*.md
  - [ ] User confirmation obtained for final requirement set
  - [ ] Script execution completed successfully or fallback documented
  </checks>
  </stage>
</workflow>

