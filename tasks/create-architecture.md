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
- **MUST** execute shard-architecture.py, **MUST NOT** skip

## [Instructions]
1. **Step 1: Requirement Intake & Coverage Matrix**
- **GOAL:**
  Build a complete requirements-to-architecture mapping with documented issues and measurement points.
- **STEPS:**
  - Review relevant `{REQ}/*.md` files to extract Priority, Dependencies, Acceptance Criteria, NFR Category, Target Metric, Measurement Method, and all constraints.
  - Populate the Requirement-Architecture Mapping Matrix with Requirement ID, mapped components, acceptance validation approach, and related design decisions or ADR links; raise an issue for any unmapped or conflicting item.
  - Translate Given-When-Then criteria into validation notes and define concrete measurement points for each NFR Target Metric.
- **QUESTIONS:**
  What requirement fields are missing or contradictory?  
  Which components or decisions cover each Critical/High requirement first?  
  Where will each NFR metric be measured and observed?
- **CHECKLIST:**
  - [ ] Every REQ/NFR links to at least one architecture component with acceptance coverage documented.
  - [ ] Issues logged for incomplete, ambiguous, or conflicting requirements (no assumptions introduced).
  - [ ] Measurement points recorded for all NFR Target Metrics and constraints acknowledged.

2. **Step 2: Architecture Design & Traceability**
- **GOAL:**
  Design architecture components that satisfy requirements, constraints, and template expectations with full traceability.
- **STEPS:**
  - Use the mapping matrix to design components, data flows, and integrations in priority order (Critical → High → Medium → Low) while honoring Dependencies.
  - Follow `{TMPL}/architecture-tmpl.yaml` to plan content for each required section (Introduction through Source References), ensuring every decision ties back to requirements or constraints.
  - Document technology selections, cross-cutting concerns, and ADRs with rationale linked to requirement IDs, constraints, and NFR measurements.
- **QUESTIONS:**
  Does each architectural element reference the requirements it fulfills?  
  How do constraints (technical, business, regulatory) shape technology and design choices?  
  Are monitoring, security, and resilience considerations integrated for every critical flow?
- **CHECKLIST:**
  - [ ] Components, data flows, and integrations mapped directly to requirement IDs and constraints.
  - [ ] ADRs drafted or updated with alternatives, rationale, and requirement references.
  - [ ] Cross-cutting concerns (security, observability, resilience, compliance) addressed with explicit strategies.

3. **Step 3: Draft Architecture Document & Sharding Prep**
- **GOAL:**
  Produce an approved `{root}/docs/architecture.md` aligned with the template and prepare it for sharding.
- **STEPS:**
  - Author `{root}/docs/architecture.md` strictly following `{TMPL}/architecture-tmpl.yaml`, embedding the mapping matrix, diagrams, and ADR references.
  - Review the document for template adherence, requirement coverage, and stakeholder approval readiness; capture approvals or outstanding clarifications.
  - After approval, execute `{SCRIPTS}/shard-architecture.py` to generate `{ARCH}/*.md`, verifying outputs for completeness.
- **QUESTIONS:**
  Does the document mirror the template structure with accurate links to requirements and ADRs?  
  Have stakeholders approved or provided feedback on the architecture decisions?  
  Did sharding maintain section integrity without data loss?
- **CHECKLIST:**
  - [ ] `{root}/docs/architecture.md` completed with traceability matrix, diagrams, and referenced ADRs.
  - [ ] Approval status documented, issues or follow-ups noted.
  - [ ] `{SCRIPTS}/shard-architecture.py` executed successfully and `{ARCH}/*.md` outputs verified.

4. **Step 4: Validation & Coverage Assurance**
- **GOAL:**
  Confirm the architecture fully satisfies requirements, NFR targets, and constraints with no unresolved gaps.
- **STEPS:**
  - Reconcile requirements, NFR metrics, and constraints against the final architecture to ensure zero unmapped items and recorded resolutions for issues.
  - Validate data flows, sequence diagrams, external API definitions, and monitoring plans against acceptance criteria and measurement methods.
  - Update the issue log with remaining clarifications, highlighting blockers and escalation needs for unresolved requirements.
- **QUESTIONS:**
  Are all user journeys and system flows demonstrably covered with measurable outcomes?  
  Can every NFR target be validated via defined monitoring or testing methods?  
  Which open issues must be resolved before implementation can start?
- **CHECKLIST:**
  - [ ] Requirement coverage reconfirmed with no outstanding unmapped REQ/NFR items.
  - [ ] Measurement and monitoring strategy validated for all NFR targets and constraints.
  - [ ] Outstanding issues documented with clear escalation or follow-up actions.
  
## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] 100% requirement-architecture mapping matrix with all fields (Priority, Dependencies, Acceptance Coverage, Measurement Points)
- [ ] All **Critical** and **High** priority requirements mapped and validated in initial design review
- [ ] All NFR **Target Metrics** have designated **Measurement Points** in architecture (e.g., APM for latency, logs for errors)
- [ ] All **Constraints** (Technical/Business/Regulatory) reflected in ADR "Alternatives Considered"
- [ ] All requirement **Dependencies** correctly reflected in architecture component dependencies
- [ ] architecture.md approved and sharded to "{ARCH}/"
- [ ] All functional and non-functional requirements covered

## [Example]

**Note**: Examples below show how requirements appear in {REQ}/*.md documents and how to process them.

### Good #1: Complete Requirement-Architecture Mapping
**Input** (from requirements documents in {REQ}/*.md): 
- **REQ-001** (Priority: Critical, Dependencies: None): User can send real-time messages
  - **Acceptance Criteria**: 
    - Given user is logged in and connected
    - When user sends a message
    - Then message is delivered to recipient within 100ms
- **REQ-002** (Priority: High, Dependencies: REQ-001): User can view message history
  - **Acceptance Criteria**:
    - Given 1000 historical messages exist
    - When user requests last 50 messages
    - Then system returns messages within 200ms
- **NFR-001** (Category: Performance, Target Metric: P95 latency <100ms, Measurement Method: APM traces)
- **Constraint** (from Constraints section): Must use AWS services (Technical Constraint)

**Decision**: 
1. Read requirements documents and create mapping matrix:
   - Extract REQ-001 (Critical priority identified in document) → WebSocket Gateway (AWS API Gateway WebSocket) + Message Broker (Amazon MQ)
   - Extract REQ-002 (High priority, Dependencies field shows REQ-001) → Message Store (DynamoDB) + Query API (Lambda)
   - Extract NFR-001 (Category: Performance, Target Metric: <100ms) → All components constraint; Measurement Point: CloudWatch traces on API Gateway + Lambda
2. Process Dependencies: REQ-002 depends on REQ-001 (found in Dependencies field), so architecture must ensure REQ-001 components operational first
3. Process Acceptance Criteria: Transform Given-When-Then from requirements into test scenarios
4. Process Constraints: AWS constraint from Constraints section → all technology choices use AWS services
5. Create ADR-001 with AWS constraint reflected in Alternatives Considered
6. Generate architecture.md, obtain approval, run shard script

**Why Good**: 
- Systematically read and extracted all structured fields from requirements documents (Priority, Dependencies, Acceptance Criteria, Category, Target Metric, Constraints)
- Transformed requirement structure into architecture elements
- No assumptions; all decisions traceable to requirement document content

### Good #2: External API Integration with NFR Coverage
**Input** (from requirements documents):
- **REQ-001** (Priority: Critical): Process payments via Stripe
- **REQ-002** (Priority: High, Dependencies: REQ-001): Detect fraudulent transactions
- **NFR-001** (Category: Reliability, Target Metric: ACID compliance for transactions, Measurement Method: Database transaction logs)
- **Constraint**: Budget <$10K/month (Business Constraint)

**Decision**: 
1. Read requirements and map:
   - REQ-001 → Payment Gateway (Stripe integration)
   - REQ-002 → Fraud Analyzer (depends on REQ-001 payment events)
   - NFR-001 → PostgreSQL with ACID guarantees; Measurement Point: transaction logs
2. Document Stripe API completely: endpoints (POST /charges, GET /customers), auth (API key), schemas (charge object, customer object), rate limits (100 req/sec), error handling (retry logic for 5xx)
3. Create ADR-001: Synchronous processing for ACID compliance
   - Alternatives Considered: Async processing rejected due to NFR-001 (ACID requirement)
   - Cost analysis: Stripe fees + PostgreSQL RDS = $8K/month (within budget constraint)
4. Map 100% coverage, shard successfully

**Why Good**: 
- External API documented to template depth (endpoints, auth, schemas, rate limits, errors)
- NFR Category (Reliability) drove technology choice (PostgreSQL for ACID)
- Business Constraint (budget) validated in ADR cost analysis
- All dependencies and priorities addressed

### Bad #1: Ignoring Requirement Structure
**Input** (from requirements documents):
- REQ-001, REQ-002 with Given-When-Then acceptance criteria, Priority (Critical/High), Dependencies
- NFR-001 with Category (Security), Target Metric (OAuth 2.0 compliance), Measurement Method
- Constraints: Must comply with GDPR (Regulatory Constraint)

**Bad Decision**: 
- Create simple mapping: REQ-001→WebSocket, REQ-002→Database
- Skip Priority analysis (miss that REQ-001 is Critical and must be prioritized)
- Ignore Dependencies field (design REQ-002 without ensuring REQ-001 completion)
- No acceptance criteria validation plan (Given-When-Then not transformed into tests)
- Skip GDPR constraint (no data residency consideration in architecture)
- No measurement points for NFR Target Metrics (OAuth compliance not verified)

**Why Bad**: 
- Violates constraint (no assumptions allowed) by ignoring structured requirement fields
- Missing Critical priority handling risks project failure
- Ignoring dependencies creates impossible implementation order
- No acceptance coverage = no validation strategy
- Regulatory violation risk (GDPR)
- NFR Category (Security) not addressed in ADR

**Correct**: 
1. Extract all fields: Priority (Critical→prioritize first), Dependencies (REQ-002 depends on REQ-001), Acceptance Criteria (Given-When-Then→test scenarios)
2. Create complete mapping matrix with all columns
3. Design architecture reflecting priorities and dependencies
4. Define measurement points for NFR Target Metrics (OAuth: auth logs)
5. Document GDPR compliance in ADR (data residency in EU, data flow diagrams show EU-only storage)
6. Map NFR Category (Security) to ADR on OAuth 2.0 implementation
