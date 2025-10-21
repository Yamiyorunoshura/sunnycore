**GOAL**: Create detailed TDD implementation plan for a specific task with RED/GREEN/REFACTOR phases.

## [Context]
**You must read the following context:**
- `{REQ}/*.md`(Only the related documents)
- `{ARCH}/*.md`(Only the related documents)
- `{EPIC}`
- `{TMPL}/implementation-plan-tmpl.yaml`
- `{KNOWLEDGE}/*.md` (optional)

## [Products]
- `{PLAN}/{task_id}-plan.md`

## [Constraints]
- **MUST** extract planning intelligence from source documents only, **MUST NOT** fabricate requirements, architecture elements, or task mappings
- **MUST** construct complete traceability chains (REQ → Architecture → Tests → Implementation), **MUST NOT** proceed with broken chains
- **MUST** record conflicts/gaps and request clarification, **MUST NOT** resolve conflicts with assumptions
- **MUST** respect architecture decisions (ADRs, tech stack), **MUST NOT** override with knowledge base when conflicts arise
- **MUST** identify applicable knowledge base patterns, **MUST NOT** force-apply patterns that conflict with architecture

## [Instructions]
1. **Step 1: Gather Planning Intelligence**
- **GOAL:** Capture the information required by `implementation-plan-tmpl.yaml` to build a complete mental model for the task.
- **STEPS:**
  - Identify the relevant functional and non-functional requirements, including acceptance criteria, dependencies, and priorities.
  - Review architecture materials (tech stack tables, component responsibilities, data flows, ADRs) to note constraints and integration points.
  - Read the epic/task metadata to confirm scope, mapped requirements/components, dependencies, and quality gates.
  - Scan the knowledge base for patterns that reinforce requirements and architecture without creating conflicts.
- **QUESTIONS:**
  - Which requirements and acceptance criteria govern this task?
  - What architecture components and interfaces support those requirements?
  - Which dependencies or quality gates from the epic affect planning?
  - Do any knowledge base patterns apply without contradicting ADRs?
- **CHECKLIST:**
- [ ] Relevant REQ/NFR sources and acceptance criteria captured.
- [ ] Architecture constraints, integrations, and ADR decisions recorded.
- [ ] Epic dependencies, quality gates, and scope confirmed.
- [ ] Applicable knowledge patterns logged or conflicts flagged for clarification.

2. **Step 2: Build Traceability Chains**
- **GOAL:** Ensure every requirement links to planned tests, architecture components, and implementation files.
- **STEPS:**
  - Derive required behavior, integration, unit, and performance tests for each requirement and NFR.
  - Map each test to the architecture components, technologies, and interfaces it exercises.
  - Determine implementation and test file paths that align with the architecture structure and template expectations.
  - Draft the traceability table (REQ → Tests → Components → Files) and highlight missing links.
- **QUESTIONS:**
  - Do all functional and non-functional requirements have mapped tests?
  - Which components and files implement each planned test?
  - Are performance or integration layers required to satisfy constraints?
  - Where do traceability gaps or uncertainties remain?
- **CHECKLIST:**
- [ ] REQ-to-test mappings complete for functional and non-functional items.
- [ ] Tests mapped to architecture components and interfaces.
- [ ] Implementation and test file paths drafted per tech stack conventions.
- [ ] Traceability gaps or open questions documented for follow-up.

3. **Step 3: Plan TDD Phases**
- **GOAL:** Translate traceability into RED/GREEN/REFACTOR actions aligned with the template.
- **STEPS:**
  - Enumerate RED phase tests with expected failure reasons and file locations.
  - Outline minimal GREEN implementation steps that respect architecture constraints and traceability mappings.
  - Identify REFACTOR targets (quality, integration, performance, knowledge patterns) consistent with ADRs.
  - Define verification tasks for each phase, including test suite runs and coverage thresholds.
- **QUESTIONS:**
  - Which tests must fail first and what behaviors do they validate?
  - What minimal code changes will satisfy each test while honoring architecture decisions?
  - Which refactors improve quality without breaking GREEN?
  - How will verification ensure failure reasons, pass conditions, and coverage targets are met?
- **CHECKLIST:**
- [ ] RED phase tests listed with expected failures and file paths.
- [ ] GREEN steps linked to components, files, and corresponding tests.
- [ ] REFACTOR targets align with ADRs and applicable knowledge patterns.
- [ ] Phase-specific verification criteria (failures, exits, coverage) documented.

4. **Step 4: Resolve Conflicts and Finalize Plan**
- **GOAL:** Deliver a conflict-free, template-ready implementation plan.
- **STEPS:**
  - Review the plan for conflicts across requirements, architecture, and knowledge guidance.
  - Flag missing information or broken traceability chains that require clarification.
  - Summarize risks, dependencies, and rollback/mitigation expectations for the template’s risk and additional detail sections.
  - Confirm readiness of the `{PLAN}/{task_id}-plan.md` deliverable against template sections.
- **QUESTIONS:**
  - Are any conflicts or assumptions unresolved and needing clarification?
  - What gaps still block complete traceability or planning?
  - Have risks, dependencies, and mitigations been captured for the plan?
  - Does the plan satisfy all constraints and template deliverables?
- **CHECKLIST:**
- [ ] Conflicts and unanswered questions recorded with required follow-ups.
- [ ] Traceability chains validated end-to-end or gaps escalated.
- [ ] Risk, dependency, and mitigation notes prepared for the plan.
- [ ] Deliverable structure aligned with `implementation-plan-tmpl.yaml` sections and constraints.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Complete traceability chains constructed: Every REQ → Test Cases → Architecture Components → Implementation Files
- [ ] TDD decision logic applied: RED (test coverage decisions documented), GREEN (atomic step granularity justified), REFACTOR (improvement priorities explained)
- [ ] Conflict resolution completed: All gaps/conflicts recorded or resolved, no fabricated information
- [ ] Knowledge base patterns evaluated: Applied only where compatible with Architecture decisions (ADRs, tech stack)
- [ ] Plan files created: One plan file per Task at `{PLAN}/{task_id}-plan.md` following `{TMPL}/implementation-plan-tmpl.yaml`

## [Examples]

### Good example 1: Create a plan with different test types
- **Context**: A task to implement a user authentication feature with specific security and performance requirements.
- **Decision**: Design unit tests for individual functions (e.g., password hashing), integration tests for component interactions (e.g., login flow), behavioral tests for end-to-end scenarios (e.g., successful login), and performance tests to ensure response times meet NFRs.
- **Outcome**: The developers successfully built a working authentication module with comprehensive test coverage.
- **Why good**: Use of different test type strategies ensured all aspects of the feature were validated, leading to a robust implementation.