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

## [Steps]
**You should work along to the following steps:**
1. Analyze requirements, create mapping matrix (100% coverage). This ensures requirements are understood with complete mapping.
2. Design architecture with all components, map all requirements. This creates complete architecture with full coverage.
3. Create architecture.md, obtain approval, run shard-architecture.py. This results in approved and sharded architecture.
4. Verify architecture satisfies all requirements. This validates the architecture.

## [Instructions]

### 1. Requirement Analysis and Coverage Matrix
You must create a comprehensive **Requirement-Architecture Mapping Matrix** to ensure 100% coverage:

| Requirement ID | Description | Priority | Dependencies | Architecture Component | Acceptance Coverage | Design Decision |
|---------------|-------------|----------|--------------|----------------------|---------------------|-----------------|
| REQ-001 | User can send real-time messages | Critical | None | WebSocket Gateway + Message Broker | Test: Given user connected, When message sent, Then delivered <100ms | ADR-001 |
| REQ-002 | Message history retrieval | High | REQ-001 | Message Store + Query API | Test: Given 1000 messages, When query last 50, Then return <200ms | ADR-002 |
| NFR-001 | <100ms message latency (P95) | Critical | N/A | All components (constraint) | Measurement: APM traces, Load tests with 10K users | Performance budget |
| NFR-002 | 99.9% uptime | High | N/A | Multi-AZ deployment + Health checks | Measurement: Uptime monitoring, Incident logs | ADR-003 |

**Matrix Guidelines:**
- **Priority**: Identify the Priority field in each requirement (Critical/High/Medium/Low); validate Critical/High requirements first
- **Dependencies**: Identify the Dependencies field in each requirement; ensure architecture reflects dependency order
- **Acceptance Coverage**: Transform the Given-When-Then acceptance criteria found in requirements into testable architecture validation points
- **NFR Measurement**: For each NFR, extract its Target Metric and specify where in the architecture this metric will be measured (e.g., API gateway logs for latency, database query analyzer for query time)

Every requirement (functional and non-functional) must map to at least one architecture component. If any requirement cannot be mapped, record it as an issue and request clarification.

### 2. Architecture Design Methodology
Your architecture design must be driven by requirements and follow the architecture template structure.

**Follow Architecture Template Structure**:
- Use `{TMPL}/architecture-tmpl.yaml` as the definitive guide for document structure
- Ensure coverage of all required sections: Introduction, Work Directory Structure, Technical Stack, System Architecture, Components, Data Flows, External APIs, Requirements Traceability Matrix, ADRs, Cross-Cutting Concerns, Deployment, Source References
- Follow the format and content requirements specified in each template section
- The template defines WHAT to document; this task defines HOW to design

**Design from Requirements Mapping**:
- Start from the mapping matrix created in Step 1
- Design components in priority order: Critical → High → Medium → Low
- Respect requirement Dependencies: design prerequisite components first
- For each requirement, translate Acceptance Criteria into component capabilities
- Ensure every requirement maps to specific architecture elements (components, ADRs, deployment decisions)

**NFR-Category Driven Design**:
Requirements documents categorize each NFR by type (Performance/Security/Reliability/Usability/Maintainability/Scalability). For each NFR Category:
- **Performance** → Design caching strategy, database indexing, load balancing; create ADR
- **Security** → Design authentication/authorization flow, encryption, secrets management; create ADR
- **Reliability** → Design multi-AZ deployment, circuit breakers, retry logic, backup strategy; create ADR
- **Scalability** → Design horizontal scaling, database sharding, CDN usage; create ADR
- **Maintainability** → Design CI/CD pipeline, testing strategy, monitoring; create ADR
- **Usability** → Design UI/UX patterns, response time optimization; create ADR

For each NFR, locate its **Target Metric** (from requirements) and specify the **Measurement Point** in the architecture (e.g., API gateway logs for latency, database transaction logs for ACID compliance, uptime monitoring for reliability).

**Constraints-Aware Design**:
All constraints documented in requirements must shape your design:
- **Technical Constraints** (e.g., "Must use AWS services") → Inform technology stack selection and integration patterns
- **Business Constraints** (e.g., "Budget <$5K/month") → Validate cost in ADRs; choose cost-effective options
- **Regulatory Constraints** (e.g., "GDPR: data residency in EU") → Enforce in data flows and deployment architecture

When creating ADRs, the **Alternatives Considered** section must explain why rejected options violated constraints from requirements.

**Completeness Validation**:
Before finalizing the architecture document, verify:
- [ ] All REQ-xxx mapped to specific components with clear implementation approach
- [ ] All NFR-xxx addressed with architectural decisions and measurement points
- [ ] All Constraints reflected in technology choices and documented in ADRs
- [ ] All Acceptance Criteria (Given-When-Then) have corresponding validation strategy
- [ ] All requirement Dependencies correctly reflected in component dependencies and design order
- [ ] Requirements Traceability Matrix (from template) shows 100% coverage

### 3. Approval and Sharding Workflow
After creating the unified `architecture.md`:
1. Present the architecture to the user for approval
2. Once approved, execute `shard-architecture.py` to split into semantic files
3. Verify the sharded files in `{ARCH}/` directory
4. Confirm all cross-references are preserved

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
