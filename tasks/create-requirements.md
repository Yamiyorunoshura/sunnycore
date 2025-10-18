**GOAL**: Create detailed functional and non-functional requirements documentation.

## [Context]
**You must read the following context:**
- `{TMPL}/requirement-tmpl.yaml` (defines document structure and formatting)
- User-provided ideas and descriptions

## [Products]
- `{root}/docs/requirements.md` (temporary, will be sharded)
- `{REQ}/*.md`(Only the related documents)

## [Constraints]
- **MUST** create measurable requirements, **MUST NOT** create vague ones
- **MUST** follow `requirement-tmpl.yaml` structure, **MUST NOT** deviate
- **MUST** exclude sensitive data in examples, **MUST NOT** include
- **MUST** execute shard-requirements.py after approval, **MUST NOT** skip

## [Instructions]
1. **Step 1: Define Requirements Gathering Scope**
- **GOAL:** Establish project context and boundaries before extracting requirements.
- **STEPS:**
  - Review `templates/requirement-tmpl.yaml` and all user inputs to confirm required sections.
  - Summarize problem domain, target users, and primary use cases for the Project Overview.
  - Capture in-scope versus out-of-scope boundaries and key integration touchpoints.
- **QUESTIONS:**
  - What problem is the project solving and for whom?
  - Which user journeys or personas drive the scope?
  - Which systems or interfaces sit inside or outside the solution boundary?
- **CHECKLIST:**
  - [ ] Project Overview describes domain, users, and critical flows.
  - [ ] Scope boundaries and integration context are documented.
  - [ ] Constraints and assumptions tied to scope are noted for later sections.

2. **Step 2: Extract Atomic Functional Requirements**
- **GOAL:** Convert user input into deduplicated functional requirements with testable acceptance criteria.
- **STEPS:**
  - Parse stakeholder input to highlight distinct capabilities and data interactions.
  - Decompose vague statements into atomic REQ entries with sequential IDs and dependencies.
  - Draft Given-When-Then acceptance criteria that verify measurable outcomes for each REQ.
  - Capture open clarifications and resolve overlaps before finalizing the list.
- **QUESTIONS:**
  - Are the requirements atomic, non-overlapping, and aligned to goals?
  - What clarifications or missing details block testable acceptance criteria?
  - Do the Given-When-Then scenarios prove success and include realistic data placeholders?
- **CHECKLIST:**
  - [ ] Every functional requirement is SMART and numbered (REQ-00X).
  - [ ] Acceptance criteria follow Given-When-Then format per template.
  - [ ] Dependencies and placeholders exclude sensitive information.

3. **Step 3: Quantify Non-Functional Requirements**
- **GOAL:** Derive measurable quality attributes that support the functional scope.
- **STEPS:**
  - Identify explicit and implicit quality expectations from context and stakeholder cues.
  - Translate qualitative adjectives into quantified targets with measurement methods.
  - Assign categories (Performance, Security, etc.) and sequential IDs for each NFR.
- **QUESTIONS:**
  - Which quality attributes are implied by the problem space or constraints?
  - What concrete metrics best express the desired experience or compliance level?
  - How will each metric be measured or observed in practice?
  - Are the targets realistic given stated limitations?
- **CHECKLIST:**
  - [ ] Each NFR lists category, quantified target, and measurement method.
  - [ ] Targets align with functional scope and project constraints.
  - [ ] Sensitive data and vendor-specific secrets remain excluded.

4. **Step 4: Run Quality Validation**
- **GOAL:** Ensure requirements are complete, consistent, feasible, and compliant.
- **STEPS:**
  - Execute completeness, consistency, feasibility, and sensitivity checks against the full set.
  - Resolve conflicting requirements, unrealistic metrics, and missing acceptance criteria.
  - Populate Constraints, Assumptions, and Risks sections with consolidated findings.
- **QUESTIONS:**
  - Have all stakeholder features and quality expectations been addressed?
  - Do any requirements contradict each other or violate constraints?
  - Are placeholders and examples compliant with sensitivity guidance?
- **CHECKLIST:**
  - [ ] Quality gate items (SMART, quantification, acceptance criteria) all pass.
  - [ ] Constraints, assumptions, and risks are documented per template.
  - [ ] Outstanding clarifications or dependencies are logged for follow-up.

5. **Step 5: Finalize and Shard Deliverables**
- **GOAL:** Secure approval and produce the sharded requirements package.
- **STEPS:**
  - Present `requirements.md` to stakeholders, gather feedback, and capture explicit approval.
  - Apply revisions, rerun quality validation, and confirm readiness for distribution.
  - After approval, run `python scripts/shard-requirements.py` and verify outputs in `{REQ}/`.
- **QUESTIONS:**
  - Has the stakeholder confirmed scope alignment and accepted the requirements?
  - Were revisions revalidated against the quality checks?
  - Did sharding preserve IDs and cross-references across files?
- **CHECKLIST:**
  - [ ] Approval recorded and updates incorporated into `requirements.md`.
  - [ ] Sharded files generated with correct structure and numbering.
  - [ ] Stakeholders notified of final artifacts and next actions.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Requirements extracted following SMART principles (Specific, Measurable, Achievable, Relevant, Testable)
- [ ] All NFRs quantified with measurable metrics (no vague adjectives like "fast" or "secure")
- [ ] Every requirement has Given-When-Then acceptance criteria per `requirement-tmpl.yaml`
- [ ] Quality checks passed (completeness, consistency, feasibility, sensitivity)
- [ ] Final requirement set approved by user
- [ ] Requirements sharded to "{REQ}/*.md" using shard-requirements.py

## [Example]

### Good #1: Decomposition and Quantification
**Input**: "Customers search products by category, price, ratings with fast response"

**Decision Process**:
1. **Scope**: Product search capability for e-commerce platform
2. **Extract functional** (decompose vague "search" into atomic capabilities):
   - REQ-001: Category filter with dropdown UI and backend query
   - REQ-002: Price range slider ($0-$10K) with real-time filtering
   - REQ-003: Star rating filter (1-5 stars) with result count
3. **Quantify NFRs** (transform "fast" into metrics):
   - NFR-001: API response time P95 < 500ms under 100 concurrent users
   - NFR-002: Search results render in < 300ms after filter change
4. **Quality check**: SMART criteria met, no contradictions, technically feasible
5. **Generate** `requirements.md` per `requirement-tmpl.yaml`, obtain approval, run shard script

**Why Good**: Transforms vague user input into atomic, measurable, testable requirements with clear acceptance criteria.

### Good #2: Inferring Implicit Requirements
**Input**: "Send real-time notifications to iOS/Android when events occur with high reliability"

**Decision Process**:
1. **Scope**: Cross-platform push notification system
2. **Extract functional**:
   - REQ-001: Event subscription management (users opt-in/out by event type)
   - REQ-002: iOS push via APNs with certificate handling
   - REQ-003: Android push via FCM with token management
   - REQ-004: Notification template engine (title, body, actions)
3. **Quantify NFRs** (infer from "real-time" and "high reliability"):
   - NFR-001: Latency < 2s from event trigger to device delivery (P95)
   - NFR-002: 99.9% delivery success rate
   - NFR-003: Support 10K notifications/min peak load
   - NFR-004: Retry mechanism with exponential backoff (3 attempts)
4. **Ask clarifications**: Notification priority levels? Silent notifications? Rich media support?
5. **Generate** and shard after approval

**Why Good**: Infers implicit NFRs from context, asks clarifying questions to uncover hidden requirements.

### Bad #1: Vague and Unmeasurable
**Input**: "Need a user-friendly system that's fast and secure"

**Bad Decision**: 
- REQ-001: "System must be user-friendly"
- NFR-001: "System must be fast"
- NFR-002: "System must be secure"
- Skip Given-When-Then, skip quantification, obtain approval, skip sharding

**Why Bad**: 
- "User-friendly", "fast", "secure" are not measurable or testable
- No decomposition into atomic capabilities
- No acceptance criteria
- Cannot verify these requirements in testing

**Correct Approach**:
1. **Ask clarifications**: What does "user-friendly" mean? (task completion time? error rate?) What does "fast" mean? (API latency? page load?) What security concerns? (authentication? data encryption?)
2. **Transform to measurable**:
   - REQ-001: "Users complete checkout in ≤3 clicks with 95% task completion rate"
   - NFR-001: "API P95 < 200ms, P99 < 500ms under 500 concurrent users"
   - NFR-002: "OAuth 2.0 authentication, AES-256 data encryption, OWASP Top 10 compliance"
3. **Create Given-When-Then** for each requirement
4. **Follow workflow**: Generate per template → quality check → approval → shard
