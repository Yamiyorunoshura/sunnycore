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
- MUST update the todo list document after completing each individual todo item by marking it as completed.
- MUST delete the todo file completely after all todo items are marked as completed.
- MUST maintain English-only content throughout the prompt and generated documentation.
</constraints>

<workflow importance="Important">
  <stage id="1: init">
  <tools>
  - read_file: Review workflow stages and deliverable requirements
  - edit_file: Create todo list tracking document
  </tools>
  - Read all working steps to understand the expected deliverables.
  - Create a todo list markdown file at {root}/docs/create-requirements-todo.md following the todo list format.
  </stage>

  <stage id="2: functional">
  <tools>
  - User interaction: Gather functional requirements through structured questioning
  - Analysis: Consolidate and organize requirements by user stories or capabilities
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
  - Analysis: Identify Non-Functional Requirements (NFRs) across domains
  - Measurement: Define quantifiable targets and constraints
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
  - Specification: Define testable acceptance criteria
  - Validation: Ensure deterministic pass/fail outcomes
  </tools>
  - Define acceptance criteria per requirement; ensure they are deterministic and testable.
  - Reference inputs, preconditions, and explicit pass/fail outcomes using Given-When-Then format when helpful.
  - Use clear structure; Gherkin-style is acceptable if helpful.
  - Validate each criterion can be automated or manually verified with binary outcomes.
  </stage>

  <stage id="5: finalize">
  <tools>
  - Review: Cross-check consistency across requirement types
  - File operations: Generate structured documentation
  - Script execution: Run sharding automation
  </tools>
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

<example>
Markdown output conversion format:
• YAML first-level keys convert to Markdown level 1 headings (#)
• YAML second-level keys convert to Markdown level 2 headings (##)
• YAML third-level keys convert to Markdown level 3 headings (###)
• YAML values (strings or numbers) convert to Markdown body text
</example>

<example>
Todo list format for {root}/docs/create-requirements-todo.md:

create-requirements

# Stage 1
- [ ] Read all working steps to understand the expected deliverables
- [ ] Create a todo list markdown file

# Stage 2
- [ ] Derive functional requirements from the user's input and context
- [ ] Consolidate duplicates and remove ambiguity
- [ ] Organize by user stories or system capabilities

# Stage 3
- [ ] Identify non-functional requirements across performance, reliability, security
- [ ] Quantify targets and constraints
- [ ] Map NFRs to monitoring/observability signals

# Stage 4
- [ ] Define acceptance criteria per requirement
- [ ] Reference inputs, preconditions, and explicit pass/fail outcomes
- [ ] Use clear structure

# Stage 5
- [ ] Cross-check consistency across FRs, NFRs, and acceptance criteria
- [ ] Populate the requirement template
- [ ] Run the sharding script to shard the requirements
</example>