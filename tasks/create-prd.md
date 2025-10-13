**GOAL**: Create Product Requirements Document (PRD), integrating requirements, architecture, and tasks into a single document.

## [Input]
  1. User-provided requirement description and context
  2. "{TMPL}/prd-tmpl.yaml" --PRD template
  3. (Conditional) "{ARCH}/*.md" --Existing architecture (if Brownfield)
  4. "{KNOWLEDGE}/*.md" --Project knowledge (if exist)
  5. "{TMPL}/plan-tmpl.yaml" --Unified planning template; tailor sections to project type analysis, integrated PRD content, and validation checkpoints

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
    - Create plan.md at "{root}/docs/plan.md" via the plan template, capturing project type evidence, required artifacts, and approval steps
    - Outcome: Project type determined, context gathered, and plan.md initialized

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

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Project type determination (Greenfield/Brownfield)
  - User requirement description summary
  - Existing architecture review (if Brownfield - components, patterns, contracts)
  - Requirements definition progress:
    * Functional requirements defined (count, IDs, descriptions)
    * Non-functional requirements defined (count, IDs, targets)
    * Acceptance criteria created (Given-When-Then format)
  - Architecture design progress:
    * Components designed (list with status)
    * Data flows documented (count)
    * ADRs documented (count and key decisions)
    * Impact analysis completed (if Brownfield - affected components, breaking changes)
  - Task breakdown progress:
    * Total tasks identified
    * Each task with requirement mapping
    * Dependencies identified
  - Traceability matrix:
    * Requirements → Architecture (coverage %)
    * Architecture → Tasks (coverage %)
  - User approval status (draft/approved/revisions needed)

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

### Good Example 1
[INPUT]
User requirement: "Users need to export dashboard data to CSV and PDF formats". Existing architecture: Dashboard Service (React), Analytics API (Node.js), PostgreSQL. Project type needs determination.

[DECISION]
Step 1: Check docs/architecture/ exists - Brownfield project confirmed. Read existing architecture to understand components. Step 2: Define requirements - REQ-001 (CSV export format), REQ-002 (PDF export with charts), NFR-001 (export <5s for 10K rows). Create Given-When-Then acceptance criteria. Step 3: Design architecture - add Export Service using existing Analytics API. No breaking changes (new endpoints only). Create Impact Analysis section. Step 4: Define tasks - Task-1 (CSV export), Task-2 (PDF generation). Map requirements→architecture→tasks achieving 100% coverage. Step 5: Generate docs/PRD.md following template. Obtain user approval.

[OUTCOME]
Complete docs/PRD.md with requirements, architecture, and tasks in single document. Impact Analysis confirms no breaking changes to Dashboard Service. 100% traceability: REQ-001→Export Service→Task-1, REQ-002→Export Service→Task-2, NFR-001→performance constraint. All acceptance criteria in Given-When-Then format.

[WHY-GOOD]
- Handles Brownfield context carefully by reviewing existing assets, documenting impacts, and preserving compatibility.
- Produces a unified PRD with traceability and measurable criteria, setting up downstream work for success.

### Good Example 2
[INPUT]
User requirement: "Add 2FA support for user login". No existing architecture (new project). Template: prd-tmpl.yaml.

[DECISION]
Step 1: Check docs/architecture/ - not found, Greenfield project. Step 2: Define requirements - REQ-001 (TOTP generation), REQ-002 (code verification), NFR-001 (RFC 6238 TOTP compliance). Quantified metrics for all NFRs. Step 3: Design new architecture - Auth Service (Python FastAPI), Redis (TOTP storage), User DB (PostgreSQL). Document components, data flows, ADRs. Step 4: Break into tasks - Task-1 (TOTP setup flow), Task-2 (login verification), Task-3 (backup codes). Complete requirement→architecture→task mapping. Step 5: Generate PRD with all sections. User approval obtained.

[OUTCOME]
docs/PRD.md with complete 2FA module design. Architecture section includes component diagrams and data flows. All requirements verifiable with specific metrics. Tasks have clear DoD and acceptance criteria. No existing system references (Greenfield handled correctly).

[WHY-GOOD]
- Correctly identifies the project as Greenfield and designs end-to-end artifacts instead of assuming legacy constraints.
- Embeds quantifiable requirements and task mapping, giving implementers unambiguous targets.

### Bad Example 1
[INPUT]
User describes requirement. docs/architecture/ may or may not exist.

[BAD-DECISION]
Skip project type determination step. Create vague requirements like "system should be fast" without quantification. Mix functional and non-functional requirements. No Given-When-Then format. Design architecture with fabricated component names not validated. No traceability matrix. Skip user approval. Save PRD with incomplete sections.

[WHY-BAD]
Violates Constraint 1 (misidentify project type). Violates Constraint 2 (vague, unmeasurable requirements). Violates PRD-Design-Guidelines point 1 (requirements not verifiable, NFRs not quantified). Missing traceability violates DoD. No user approval violates Step 5. Unusable PRD blocks development.

[CORRECT-APPROACH]
Execute Step 1: determine project type by checking docs/architecture/. For Greenfield: gather user context only. For Brownfield: read existing architecture, understand components and contracts. Step 2: create SMART requirements - specific, measurable, achievable. Use Given-When-Then for acceptance criteria. Quantify all NFRs (P95 <200ms, not "fast"). Step 3: design architecture with 100% requirement mapping. Step 4: create tasks with full traceability. Step 5: obtain user approval. Follow template structure exactly.

### Bad Example 2
[INPUT]
Adding caching layer to existing API. Existing architecture shows REST API and MongoDB.

[BAD-DECISION]
Misidentify as Greenfield despite docs/architecture/ existing. Skip reading existing architecture. Design caching without analyzing current API contracts. Create breaking changes without Impact Analysis. Fabricate requirement IDs. No task breakdown. Claim Brownfield but ignore existing system completely.

[WHY-BAD]
Violates Constraint 1 (misidentify Brownfield as Greenfield). Violates Constraint 4 (break existing contracts without Impact Analysis). Violates PRD-Design-Guidelines point 3 (no Impact Analysis for integration). Ignores Error-Handling rule 2 (must read existing architecture). Will cause integration failures.

[CORRECT-APPROACH]
Step 1: Identify Brownfield (docs/architecture/ exists). Read existing API architecture: endpoints, contracts, response formats. Step 2: Define requirements preserving contracts (REQ-001: transparent caching layer, no API signature changes). Step 3: Design Redis middleware integration. Create Impact Analysis: middleware addition only, all contracts preserved, backward compatible. Map to existing components. Step 4: Tasks with integration points. Step 5: Generate PRD showing Brownfield integration properly. Approval with architecture compatibility confirmed.
