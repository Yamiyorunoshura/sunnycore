**GOAL**: Create Product Requirements Document integrating requirements, architecture, and tasks.

## [Input]
- User requirement description
- `{TMPL}/prd-tmpl.yaml`
- `{ARCH}/*.md` (if Brownfield)
- `{KNOWLEDGE}/*.md` (if exist)

## [Output]
- `{PRD}`

## [Constraints]
- **MUST** correctly identify project type (Greenfield/Brownfield), **MUST NOT** misidentify
- **MUST** create measurable requirements, **MUST NOT** create vague ones
- **MUST** exclude operational actions unless requested, **MUST NOT** include unnecessarily
- **MUST** provide impact analysis for Brownfield contract changes, **MUST NOT** break existing contracts

## [Instructions]

### 1. Project Type Identification
Determine whether this is a Greenfield or Brownfield project:
- **Greenfield**: No existing architecture (`{ARCH}/` is empty or doesn't exist)
- **Brownfield**: Existing architecture documents in `{ARCH}/`

This determination affects how you approach requirements and architecture design.

### 2. Requirements Definition
Create SMART (Specific, Measurable, Achievable, Relevant, Time-bound) requirements:

#### Functional Requirements
For each functional requirement, specify:
- **REQ-ID**: Unique identifier (e.g., REQ-001)
- **Description**: Clear, actionable statement
- **Acceptance Criteria**: Given-When-Then format

Example:
```
REQ-001: CSV Export
Given: User has dashboard data
When: User clicks "Export to CSV" button
Then: System generates CSV file with all visible data within 5 seconds
```

#### Non-Functional Requirements
Quantify ALL non-functional requirements with measurable metrics:
- ❌ Vague: "System should be fast"
- ✓ Quantified: "API response time P95 < 200ms"

- ❌ Vague: "User-friendly interface"
- ✓ Quantified: "Users complete checkout in ≤ 3 clicks"

Common NFR categories:
- **Performance**: Response time, throughput, latency (with percentiles)
- **Scalability**: Concurrent users, data volume limits
- **Reliability**: Uptime SLA, error rate thresholds
- **Security**: Authentication methods, compliance standards (e.g., RFC 6238)

### 3. Architecture Design

#### For Greenfield Projects
Design complete architecture from scratch:
- Define all components with clear responsibilities
- Specify technology stack with version numbers
- Create data flow diagrams
- Document Architecture Decision Records (ADRs)
- Map 100% of requirements to architecture components

#### For Brownfield Projects
Extend existing architecture carefully:
1. **Review**: Read ALL existing architecture documents
2. **Impact Analysis**: For ANY contract change, create an Impact Analysis Table:
   | Changed Element | Affected Components | Breaking Change? | Migration Path |
   |----------------|---------------------|------------------|---------------|
   | User API | API Gateway, 3 clients | Yes | Add v2 endpoint, deprecate v1 in 6 months |

3. **Backward Compatibility**: Ensure existing functionality is preserved
   - Add new endpoints/events rather than modifying existing ones
   - Use versioning for contract evolution
   - Provide migration timeline for breaking changes

4. **Integration Strategy**: Identify extension points (event bus, hooks, plugins)

### 4. Task Breakdown
Create feature-level tasks (not atomic steps):
- Map each task to specific requirements and architecture components
- Use kebab-case naming (e.g., "implement-export-service")
- Ensure 100% requirement coverage (every requirement → at least one task)
- Define clear Definition of Done for each task

### 5. PRD Integration
Integrate all sections into a unified, traceable PRD:
- **Traceability Matrix**: Show requirement → architecture → task mapping
- **Impact Summary**: List all changes and affected systems (for Brownfield)
- **Risk Assessment**: Identify technical and business risks
- **Success Metrics**: Define how success will be measured

## [Steps]
1. Determine project type, gather context. This identifies the project type with context gathered.
2. Define verifiable functional and quantified non-functional requirements. This creates complete requirements with acceptance criteria.
3. Design architecture (Greenfield: new; Brownfield: extending with impact analysis). This produces complete architecture documentation.
4. Integrate requirements, architecture, tasks into unified PRD. This creates integrated PRD with full traceability.
5. Complete PRD, save to "{PRD}", obtain confirmation. This creates approved PRD.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Functional and non-functional requirements with quantified metrics and Given-When-Then criteria
- [ ] Architecture complete with 100% requirement mapping and impact analysis (if Brownfield)
- [ ] PRD at "{PRD}" approved by user

## [Example]

### Good #1
**Input**: "Export dashboard data to CSV/PDF". Existing arch: Dashboard Service (React), Analytics API (Node.js), PostgreSQL  
**Decision**: Brownfield confirmed (arch exists). Read existing arch. Define: REQ-001 (CSV export), REQ-002 (PDF with charts), NFR-001 (export <5s for 10K rows), Given-When-Then criteria. Design: add Export Service using Analytics API, no breaking changes. Impact Analysis: new endpoints only. Map: REQ-001→Export Service→Task-1, REQ-002→Task-2, 100% coverage. Generate PRD. Obtain approval.  
**Why Good**: This handles Brownfield carefully, reviews existing assets, documents impacts, and preserves compatibility.

### Good #2
**Input**: "Add 2FA for login". No existing architecture  
**Decision**: Greenfield. Define: REQ-001 (TOTP generation), REQ-002 (code verification), NFR-001 (RFC 6238 compliance). Quantify all NFRs. Design: Auth Service (FastAPI), Redis (TOTP storage), PostgreSQL. Include components, data flows, ADRs. Create Task-1 (TOTP setup), Task-2 (verification), Task-3 (backup codes). Complete req→arch→task mapping. Generate PRD. Obtain approval.  
**Why Good**: This identifies Greenfield, designs end-to-end, and embeds quantifiable requirements and task mapping.

### Bad #1
**Input**: User describes requirement  
**Bad Decision**: Skip project type determination. Create vague requirements: "fast system". Mix functional and non-functional. Omit Given-When-Then. Fabricate component names. Provide no traceability. Skip approval. Save incomplete PRD.  
**Why Bad**: This violates project type identification, creates vague unmeasurable requirements, provides no traceability, and produces unusable PRD.  
**Correct**: Determine project type (check docs/architecture/). Create SMART requirements (specific, measurable). Use Given-When-Then for acceptance. Quantify NFRs (P95 <200ms, not "fast"). Design with 100% mapping. Obtain approval.
