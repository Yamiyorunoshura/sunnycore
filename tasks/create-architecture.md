**GOAL**: Create comprehensive technical architecture for Greenfield projects.

## [Context]
**You must read the following context:**
- `{REQ}/*.md`(Only the related documents) - Requirements documents following standardized structure. Each document contains:
  - **Functional Requirements** (REQ-xxx): Each requirement includes Description, Acceptance Criteria (Given-When-Then format), Priority (Critical/High/Medium/Low), Dependencies (other requirement IDs)
  - **Non-Functional Requirements** (NFR-xxx): Each requirement includes Category (Performance/Security/Reliability/Usability/Maintainability/Scalability), Requirement statement, Target Metric (quantified), Measurement Method, Priority
  - **Constraints**: Technical Constraints (technology limitations, integration requirements, compliance), Business Constraints (budget, timeline, resources), Regulatory Constraints (legal requirements, industry standards, data protection)
  - **Assumptions and Risks**: Assumptions (what we assume to be true, dependencies on external factors), Risks (technical/integration/dependency risks, mitigation strategies)
- `{SCRIPTS}/shard-architecture.py`
- `{TMPL}/architecture-tmpl.yaml`

**Note**: Requirements documents are structured with verifiable, complete, and atomic requirements. Your architecture must leverage this structure to ensure comprehensive coverage.

## [Products]
- `{root}/docs/architecture.md` (temporary, will be sharded)
- `{ARCH}/*.md`(Only the related documents)

## [Constraints]
- **MUST** record issues when requirements incomplete/conflicting, **MUST NOT** make assumptions
- **MUST** achieve 100% requirement coverage, **MUST NOT** deliver incomplete architecture
- **MUST** follow template structure, **MUST NOT** deviate
- **MUST** guide the user through question-driven checkpoints, **MUST NOT** advance without capturing user confirmation at each stage
- **MUST** execute shard-architecture.py, **MUST NOT** skip

## [Instructions]
1. **Step 1: Requirement Alignment Dialogue**
- **GOAL:**
  Build a shared understanding of scope by confirming requirements, constraints, and priorities with the user before mapping.
- **STEPS:**
  - Summarize the known requirement set to the user and ask targeted questions to clarify priorities, dependencies, constraints, and missing Acceptance Criteria details.
  - Capture the user's answers verbatim in working notes, flag open issues, and request additional artifacts when needed.
  - Confirm with the user that the clarified requirement list is ready for mapping, or agree on follow-up actions if gaps remain.
- **QUESTIONS (for the user and self-check):**
  - Which requirement details remain unclear or contradictory?  
  - What additional context does the user need to provide before design can start?  
  - Which Critical/High items must be addressed first according to the user?
- **CHECKLIST:**
  - [ ] User-provided clarifications recorded, including priorities and dependencies.
  - [ ] Outstanding issues or missing information logged and acknowledged by the user.
  - [ ] User confirmation captured that requirements are ready for architecture mapping.

2. **Step 2: Collaborative Mapping & Architecture Outline**
- **GOAL:**
  Co-create the requirement-to-architecture mapping and high-level component plan with continuous user validation.
- **STEPS:**
  - Draft the mapping matrix row by row, proposing component responsibilities and validation approaches; after each critical cluster, pause to review with the user.
  - Ask follow-up questions whenever assumptions arise about data flows, integrations, or cross-cutting concerns; do not proceed until the user resolves them.
  - Iterate on the outline (components, integrations, data flows) based on user feedback, updating the matrix and noting agreed decisions or ADR placeholders.
- **QUESTIONS (for the user and self-check):**
  - Does the user agree with the component responsibilities and coverage for each requirement?  
  - What monitoring or measurement points does the user expect for each NFR target metric?  
  - Are any constraints or dependencies still undecided by the user?
- **CHECKLIST:**
  - [ ] Mapping matrix updated with user-validated component coverage and measurement points.
  - [ ] ADR candidates and decision owners aligned with user expectations.
  - [ ] User approval recorded for the high-level architecture outline.

3. **Step 3: Document Drafting & User Approval**
- **GOAL:**
  Produce architecture documentation aligned with the template, validated section-by-section with the user.
- **STEPS:**
  - Populate `{root}/docs/architecture.md` following `{TMPL}/architecture-tmpl.yaml`, referencing the agreed mapping matrix, decisions, and measurement strategies.
  - After drafting each major section (Overview, Components, Data Flows, Cross-Cutting Concerns, ADRs), summarize the content for the user and request confirmation or corrections before proceeding.
  - Record user approvals, outstanding clarifications, and decision ownership directly in the document notes or issue log.
- **QUESTIONS (for the user and self-check):**
  - Does the user accept the documented decisions and traceability for every requirement?  
  - Which sections need more detail or supporting evidence according to the user?  
  - Are there unresolved questions that block final approval?
- **CHECKLIST:**
  - [ ] All template sections drafted and reviewed with the user.
  - [ ] User-approved traceability matrix embedded with requirement coverage and measurement points.
  - [ ] Open clarifications documented with responsible parties and follow-up plan.

4. **Step 4: Validation, Sharding & Final Handoff**
- **GOAL:**
  Confirm end-to-end coverage with the user, then distribute the architecture artifacts.
- **STEPS:**
  - Walk the user through the final validation pass, reconciling requirements, NFR metrics, and constraints against the documented architecture; adjust based on feedback.
  - Once the user confirms readiness, execute `{SCRIPTS}/shard-architecture.py` to generate `{ARCH}/*.md`, and review outputs together for completeness.
  - Update the issue log and Quality-Gate checklist with any remaining follow-up tasks, owners, and timelines agreed with the user.
- **QUESTIONS (for the user and self-check):**
  - Are all user journeys, data flows, and measurement points acceptable to the user?  
  - Did the user confirm the sharded outputs match expectations?  
  - What remaining risks or decisions need escalation?
- **CHECKLIST:**
  - [ ] User walkthrough completed with zero unmapped REQ/NFR items.
  - [ ] `{SCRIPTS}/shard-architecture.py` executed post-approval and outputs validated with the user.
  - [ ] Outstanding actions logged with owners, due dates, and escalation path.
  
## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] 100% requirement-architecture mapping matrix with all fields (Priority, Dependencies, Acceptance Coverage, Measurement Points)
- [ ] All **Critical** and **High** priority requirements mapped and validated in initial design review
- [ ] All NFR **Target Metrics** have designated **Measurement Points** in architecture (e.g., APM for latency, logs for errors)
- [ ] All **Constraints** (Technical/Business/Regulatory) reflected in ADR "Alternatives Considered"
- [ ] All requirement **Dependencies** correctly reflected in architecture component dependencies
- [ ] architecture.md approved and sharded to "{ARCH}/"
- [ ] All functional and non-functional requirements covered
