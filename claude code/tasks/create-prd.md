**GOAL**: Create Product Requirements Document (PRD), integrating requirements, architecture, and tasks into a single document.

## [Input]
  1. User-provided requirement description and context
  2. "{TMPL}/prd-tmpl.yaml" --PRD template
  3. (Conditional) "{ARCH}/*.md" --Existing architecture (if Brownfield)
  4. "{KNOWLEDGE}/*.md" --Project knowledge (if exist)

## [Output]
  1. "{PRD}" --Complete Product Requirements Document (Markdown format)
  2. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not misidentify project type (Greenfield/Brownfield)
  2. Do not create vague or unmeasurable requirements
  3. Do not include operational actions unless explicitly requested
  4. Do not break existing contracts for Brownfield projects (must provide impact analysis for changes)

## [Steps]
  1. Initialization & Context Understanding
    - Determine project type (Greenfield/Brownfield)
    - Gather appropriate context for project type
    - Establish progress tracking mechanism
    - Outcome: Project type determined and context gathered

  2. Requirements Definition
    - Define complete, verifiable, measurable functional requirements
    - Define quantified non-functional requirements with clear targets
    - Create acceptance criteria in Given-When-Then format
    - Outcome: Complete requirements with clear acceptance criteria

  3. Architecture Design
    - Design architecture aligned with all requirements
    - Handle Greenfield (new) or Brownfield (extending) scenarios appropriately
    - Document components, data flows, contracts, and impact analysis (if Brownfield)
    - Outcome: Complete architecture documentation

  4. PRD Integration & Mapping
    - Integrate requirements, architecture, and tasks into unified PRD
    - Ensure complete traceability and proper mapping
    - Identify dependencies and execution order
    - Outcome: Integrated PRD with full traceability

  5. Finalization & Approval
    - Complete consistent PRD document
    - Save to "{PRD}"
    - Obtain user confirmation
    - Outcome: Approved PRD document created

## [Error-Handling]
  1. Directory check failure: Log error and proceed as Greenfield
  2. Existing architecture read failure: Record issue and request user clarification
  3. Requirement conflicts: Record conflicts and request user clarification
  4. Requirement conflicts cannot be automatically resolved: Document conflicting requirements and request user prioritization
  5. Architecture design infeasibility: Record technical limitations and propose alternatives
  6. Architecture design incompatible with non-functional requirements: Document incompatibility and request user guidance on trade-offs
  7. User rejects final PRD: Record rejection reasons and iterate on requirements/architecture based on feedback

## [PRD-Design-Guidelines]
  1. **Requirements: Verifiable & Quantified**
    - All requirements must be testable with clear success/failure criteria
    - Use Given-When-Then format; quantify non-functional requirements (e.g., "P95 < 200ms")
    - Map dependencies and priorities between requirements
  
  2. **Architecture: Mapped & Justified**
    - Establish 100% bidirectional mapping: requirements ↔ architecture components
    - Record key decisions using ADR format (context, rationale, trade-offs)
    - Address cross-cutting concerns (security, logging, error handling) systematically
  
  3. **Integration: Impact Analysis Required**
    - For Brownfield: analyze impact on existing system, preserve contracts
    - Identify extension points and shared services
    - Clearly document any breaking changes with migration path
  
  4. **Tasks: Feature-Level & Traceable**
    - Break requirements into feature-level tasks (clear scope, verifiable outcomes)
    - Ensure complete traceability: requirements → architecture → tasks

## [DoD]
  - [ ] Complete functional and non-functional requirements with quantified metrics and Given-When-Then acceptance criteria
  - [ ] Architecture design complete with 100% requirement mapping and impact analysis (if Brownfield)
  - [ ] PRD document exists at "{PRD}" following template structure and approved by user

## [Example]

### Example 1: Add Export Feature to Dashboard (Brownfield)
[Input]
- User requirement: "Users need to export dashboard data to CSV and PDF"
- Existing architecture: Dashboard Service (React), Analytics API (Node.js), PostgreSQL
- Template: prd-tmpl.yaml

[Decision]
- Project type: Brownfield (docs/architecture/ exists)
- Requirements: REQ-001 (CSV export), REQ-002 (PDF export), NFR-001 (export < 5s for 10K rows)
- Architecture: Add Export Service using existing Analytics API data
- Tasks: Task-1 (CSV export), Task-2 (PDF export)
- Impact: No breaking changes, new API endpoints only

[Expected Outcome]
- docs/PRD.md with requirements, architecture, and tasks in one document
- Impact analysis showing compatibility with existing Dashboard Service
- 100% requirement-to-architecture-to-task mapping

### Example 2: Two-Factor Authentication (Greenfield Module)
[Input]
- User requirement: "Add 2FA support for user login"
- No existing architecture (new project)
- Template: prd-tmpl.yaml

[Decision]
- Project type: Greenfield (no docs/architecture/)
- Requirements: REQ-001 (TOTP generation), REQ-002 (verify code), NFR-001 (TOTP standard compliance)
- Architecture: Auth Service (Python FastAPI), Redis (TOTP storage), User DB (PostgreSQL)
- Tasks: Task-1 (TOTP setup), Task-2 (login verification), Task-3 (backup codes)

[Expected Outcome]
- docs/PRD.md with complete design for new 2FA module
- Architecture section with component diagrams and data flows
- Tasks with clear DoD and acceptance criteria

### Example 3: Add Caching Layer to API (Brownfield)
[Input]
- User requirement: "Improve API response time by adding caching"
- Existing: REST API (Express.js), MongoDB
- Template: prd-tmpl.yaml

[Decision]
- Project type: Brownfield
- Requirements: REQ-001 (cache GET endpoints), NFR-001 (P95 latency < 100ms), NFR-002 (cache hit rate > 80%)
- Architecture: Add Redis cache layer, preserve existing API contracts
- Tasks: Task-1 (cache middleware), Task-2 (cache invalidation), Task-3 (monitoring)
- Impact: Middleware addition, no API signature changes

[Expected Outcome]
- docs/PRD.md with caching design integrated into existing architecture
- Impact analysis documenting backward compatibility
- Performance metrics and acceptance criteria clearly defined

