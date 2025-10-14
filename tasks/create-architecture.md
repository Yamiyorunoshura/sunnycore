**GOAL**: Create comprehensive technical architecture for Greenfield projects.

## [Input]
**You must read the following documents:**
- `{REQ}/*.md`
- `{SCRIPTS}/shard-architecture.py`
- `{TMPL}/architecture-tmpl.yaml`

## [Output]
- `{root}/docs/architecture.md` (temporary, will be sharded)
- `{ARCH}/*.md`

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
| Requirement ID | Requirement Description | Architecture Component | Design Decision |
|---------------|------------------------|----------------------|-----------------|
| REQ-001 | WebSocket messaging | WebSocket Gateway + Message Broker | ADR-001 |
| NFR-001 | <100ms latency | All components (constraint) | Performance budget |

Every requirement (functional and non-functional) must map to at least one architecture component. If any requirement cannot be mapped, record it as an issue and request clarification.

### 2. Architecture Design
Your architecture design must include:

**Components**: All system components with clear responsibilities, interfaces, and technology choices. For each component, specify:
- Name and purpose
- Technology stack (with version if critical)
- Interfaces (APIs, events, messages)
- Dependencies on other components

**Data Flows**: Complete data flow diagrams showing how information moves through the system. Include:
- Request/response flows
- Event flows
- Data persistence flows

**Architecture Decision Records (ADRs)**: Document all significant decisions with:
- Context: Why this decision was needed
- Decision: What was chosen
- Consequences: Trade-offs and implications
- Alternatives considered

**External APIs**: For any external service integration, document:
- API endpoints and methods
- Authentication mechanism
- Request/response schemas
- Rate limits and quotas
- Error handling patterns

### 3. Approval and Sharding Workflow
After creating the unified `architecture.md`:
1. Present the architecture to the user for approval
2. Once approved, execute `shard-architecture.py` to split into semantic files
3. Verify the sharded files in `{ARCH}/` directory
4. Confirm all cross-references are preserved

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] 100% requirement-architecture mapping matrix
- [ ] architecture.md approved and sharded to "{ARCH}/"
- [ ] All functional and non-functional requirements covered

## [Example]

### Good #1
**Input**: REQ-001 (WebSocket messaging), REQ-002 (persistence), NFR-001 (<100ms latency)  
**Decision**: Create mapping: REQ-001→WebSocket Gateway+Broker, REQ-002→Message Store, NFR-001→constraint for all. Design components. Create ADR for WebSocket over HTTP polling. Generate architecture.md. Obtain approval. Run shard script.  
**Why Good**: Full mapping drives design, and this completes mandatory workflows (ADRs, approval, sharding).

### Good #2
**Input**: REQ-001 (Stripe payment), REQ-002 (fraud detection), NFR-001 (ACID)  
**Decision**: Design: Payment Gateway, Fraud Analyzer, PostgreSQL. ADR-001: synchronous for ACID. Document Stripe API completely (endpoints, auth, schemas, rate limits, errors). Map 100%. Shard successfully.  
**Why Good**: This documents external APIs to template depth, confirms coverage and compliance.

### Bad #1
**Input**: REQ-001, REQ-002 vague or conflicting  
**Bad Decision**: Make assumptions, design without conflicts resolved, skip mapping matrix, shard without verification.  
**Why Bad**: This violates constraints (no assumptions, 100% coverage). Architecture built on assumptions fails review.  
**Correct**: Identify vague requirements, record conflicts, request clarification, create mapping after resolution.
