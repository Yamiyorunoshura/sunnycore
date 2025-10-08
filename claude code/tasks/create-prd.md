**GOAL**: Create Product Requirements Document (PRD), integrating requirements, architecture, and tasks into a single document.

## [Input]
  1. User-provided requirement description and context
  2. "{TMPL}/prd-tmpl.yaml" --PRD template
  3. (Conditional) "{ARCH}/*.md" --Existing architecture (if Brownfield)
  4. "{KNOWLEDGE}/*.md" --Project knowledge (if exist)

## [Output]
  1. "{PRD}" --Complete Product Requirements Document

## [Constraints]
  1. Must determine project type (Greenfield/Brownfield) by checking "{ARCH}/" directory existence
  2. Each requirement must be verifiable and measurable; vague or subjective wording is not allowed
  3. Tasks must be feature-level, verifiable (clear functional scope and outcomes)
  4. Must exclude operational actions (e.g., git commit, npm install, deployment script execution) unless explicitly requested by the user
  5. Must ensure all file names/paths do not use spaces; prefer kebab-case
  6. If Brownfield, must preserve existing contracts (i.e., public API interfaces, data models, event formats, and other externally visible contracts) and provide impact analysis for changes

## [Tools]
  1. **todo_write**
    - [Step 1: Create todo list; Steps 2-6: Track working progress]
  2. **sequentialthinking (MCP)**
    - [Step 1: Analyze project type and complexity; Step 2: Design requirements; Step 3: Design architecture]
  3. **context7 (MCP)**
    - [Step 3: Obtain external package and architecture pattern references when needed]
  4. **claude-context (MCP)**
    - [Step 1: Search codebase for existing architecture implementations if Brownfield]

## [Steps]
  1. Initialization and Context Understanding Phase
    - Understand the project context and determine project type (Greenfield/Brownfield)
    - Ensure both project types are properly handled with appropriate context gathering
    - Establish progress tracking mechanism for PRD creation

  2. Requirements Definition Phase
    - Achieve complete functional requirements that are verifiable and measurable
    - Achieve quantified non-functional requirements with clear targets
    - Ensure all requirements have well-defined acceptance criteria in Given-When-Then format

  3. Architecture Design Phase
    - Ensure architecture design aligns with all requirements
    - Ensure proper handling of both Greenfield (new design) and Brownfield (extending existing) scenarios
    - Achieve complete architecture documentation with components, data flows, and contracts
    - Ensure impact analysis is documented for all changes in Brownfield projects

  4. PRD Integration Phase
    - Achieve integrated PRD document with complete traceability
    - Ensure proper mapping between requirements, architecture elements, and tasks
    - Ensure dependencies and execution order are clearly identified

  5. Finalization Phase
    - Achieve complete, consistent PRD document saved to "{PRD}"
    - Ensure user confirmation is obtained for the final PRD

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
  - [ ] Project type (Greenfield/Brownfield) has been determined
  - [ ] If Brownfield, existing architecture has been reviewed
  - [ ] Functional requirements have been extracted, deduplicated, and atomized
  - [ ] Non-functional requirements have been identified and quantified
  - [ ] Each requirement has corresponding acceptance criteria (using Given-When-Then structure)
  - [ ] Architecture design is complete with components, data flows, and technical stack
  - [ ] If Brownfield, impact analysis has been documented
  - [ ] Requirement-to-architecture mapping has been established (100% coverage)
  - [ ] Requirement dependencies have been identified
  - [ ] All requirements are verifiable and outcome-oriented
  - [ ] PRD follows template structure and is saved to "{PRD}"
  - [ ] User confirmation of the final PRD has been obtained

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

