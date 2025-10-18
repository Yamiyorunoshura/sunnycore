**GOAL**: Create Product Requirements Document integrating requirements, architecture, and tasks with complete traceability and measurable acceptance criteria.

## [Context]
**You must read the following context:**
- User requirement description
- `{TMPL}/prd-tmpl.yaml`
- `{ARCH}/*.md`(Only the related documents) (if Brownfield)
- `{KNOWLEDGE}/*.md` (if exist)

## [Products]
- `{PRD}`

## [Constraints]
- **MUST** correctly identify project type (Greenfield/Brownfield) by checking for existing architecture
- **MUST** create quantified, measurable requirements with Given-When-Then acceptance criteria
- **MUST** ensure 100% requirement-to-architecture-to-task traceability
- **MUST** provide comprehensive impact analysis for any Brownfield contract changes
- **MUST** focus on integration and avoid duplication with existing templates

## [Instructions]
1. **Step 1: Project Analysis**
- **GOAL:** Determine the project type, scope, and constraints before drafting the PRD.
- **STEPS:**
  - Gather all mandatory context: user requirement description, `templates/prd-tmpl.yaml`, relevant `{ARCH}/*.md`, and `{KNOWLEDGE}/*.md` artifacts.
  - Synthesize business goals, scope boundaries, and success criteria from the collected sources.
  - Inspect `{ARCH}/` to confirm whether the engagement is Greenfield or Brownfield and note implications.
  - Capture initial risks, dependencies, and compliance considerations that could influence downstream decisions.
- **QUESTIONS:**
  - What direct evidence confirms the initiative is Greenfield or Brownfield?
  - Which explicit constraints or success metrics appear in the supplied context?
  - Which assumptions or knowledge gaps require clarification before design begins?
- **CHECKLIST:**
  - [ ] Project type classified with supporting rationale.
  - [ ] Core goals, scope, and constraints summarized.
  - [ ] Required context sources reviewed and tagged for citation.
  - [ ] Initial risks and dependencies noted for follow-up.

2. **Step 2: Requirements Engineering**
- **GOAL:** Produce measurable functional and non-functional requirements with clear acceptance criteria.
- **STEPS:**
  - Translate user goals into atomic functional requirements using Given-When-Then scenarios from the template.
  - Prioritize requirements by business value and technical dependency, capturing IDs and traceability notes.
  - Define quantified non-functional requirements (latency targets, reliability SLAs, security standards, scalability thresholds).
  - Validate coverage against user needs and template guidance, adding TODOs where inputs are missing.
- **QUESTIONS:**
  - Do all user objectives map to at least one functional requirement?
  - Are acceptance criteria measurable and testable for every scenario?
  - Which NFR metrics are mandatory versus negotiable, and how will they be validated?
- **CHECKLIST:**
  - [ ] Functional requirements numbered and paired with Given-When-Then criteria.
  - [ ] Non-functional requirements quantified with measurement methods.
  - [ ] Priorities, dependencies, and traceability notes recorded.
  - [ ] Gaps or assumptions explicitly marked for stakeholder input.

3. **Step 3: Architecture Integration**
- **GOAL:** Define architecture elements that satisfy every requirement while respecting project context.
- **STEPS:**
  - Audit existing `{ARCH}/*.md` for Brownfield impacts or outline baseline components for Greenfield builds.
  - Select and document the technical stack with versions, aligning choices to NFR targets and team capabilities.
  - Map functional and non-functional requirements to components, data flows, and ADR decisions per template sections.
  - For Brownfield, document impact analysis covering contract changes, integration paths, and mitigation strategies.
- **QUESTIONS:**
  - Which architectural components or patterns fulfill each requirement and NFR?
  - Where do integration risks or breaking changes emerge in Brownfield scenarios?
  - Are data flows and cross-cutting concerns (security, observability) explicitly addressed?
- **CHECKLIST:**
  - [ ] Technical stack table completed with versions and rationale.
  - [ ] Component responsibilities, interfaces, and statuses documented.
  - [ ] Requirements-to-architecture mapping table shows 100% coverage.
  - [ ] Brownfield impact analysis prepared when applicable.

4. **Step 4: Task Planning**
- **GOAL:** Break the solution into feature-level implementation tasks with verifiable outcomes.
- **STEPS:**
  - Derive tasks from requirements and architecture components, ensuring each delivers user-visible value.
  - Specify dependencies, sequencing, and ownership notes to support execution planning.
  - Define clear Quality-Gate criteria (tests, reviews, documentation) for each task per template checklist.
  - Cross-reference tasks with requirement and architecture IDs to preserve traceability.
- **QUESTIONS:**
  - Does every requirement map to at least one task with a clear Definition of Done?
  - Are testing, security, and compliance activities embedded within tasks?
  - Do dependencies or sequencing constraints require stakeholder alignment?
- **CHECKLIST:**
  - [ ] Tasks listed with IDs, descriptions, and associated requirements.
  - [ ] Architecture touchpoints and dependencies noted for each task.
  - [ ] Quality-Gate items defined and feasible to validate.
  - [ ] Traceability matrix updated to include task coverage.

5. **Step 5: PRD Finalization**
- **GOAL:** Assemble the complete PRD with traceability and stakeholder-ready validation.
- **STEPS:**
  - Populate every section in `templates/prd-tmpl.yaml`, ensuring consistent formatting and citations.
  - Build the traceability matrix linking requirements, architecture decisions, and tasks.
  - Review quality gates, Brownfield analyses, and outstanding TODOs; resolve or escalate blockers.
  - Prepare the PRD for stakeholder review, highlighting decisions, risks, and approval needs.
- **QUESTIONS:**
  - Are all template sections complete with measurable content and supporting evidence?
  - Does the traceability matrix prove end-to-end coverage without gaps or duplicates?
  - Which stakeholders must approve the final PRD, and what questions might they raise?
- **CHECKLIST:**
  - [ ] PRD drafted with every template section filled and cross-referenced.
  - [ ] Traceability matrix demonstrates requirement → architecture → task alignment.
  - [ ] Quality gates reviewed with outstanding issues flagged.
  - [ ] Stakeholder review package prepared with next steps.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Functional and non-functional requirements with quantified metrics and Given-When-Then criteria
- [ ] Architecture complete with 100% requirement mapping and impact analysis (if Brownfield)
- [ ] PRD at "{PRD}" approved by user

## [Examples]

### Good #1: Brownfield Integration
**Input**: "Export dashboard data to CSV/PDF" with existing Dashboard Service (React), Analytics API (Node.js)  
**Approach**: Identified Brownfield project → analyzed existing architecture → created measurable requirements (REQ-001: CSV export <5s for 10K rows, REQ-002: PDF generation with charts) → designed Export Service integration with no breaking changes → built complete traceability matrix → delivered integrated PRD with impact analysis.  
**Key Success Factors**: Preserved existing contracts, quantified performance requirements, ensured complete requirement mapping.

### Good #2: Greenfield Design
**Input**: "Add 2FA authentication system" with no existing authentication  
**Approach**: Identified Greenfield project → defined verifiable requirements (REQ-001: TOTP generation per RFC 6238, REQ-002: backup codes) → designed Auth Service with FastAPI/Redis/PostgreSQL → created comprehensive task breakdown → integrated everything into unified PRD with full traceability.  
**Key Success Factors**: Complete architecture design, quantified NFRs, end-to-end task mapping.

### Bad Example: Incomplete Analysis
**Problem**: Skipped project type analysis → created vague requirements ("system should be fast") → designed without impact analysis → missing requirement traceability → delivered incomplete PRD.  
**Missing Elements**: Project type identification, measurable acceptance criteria, architecture mapping, stakeholder approval.  
**Correction Approach**: Always determine project type first, quantify all requirements with specific metrics, ensure 100% traceability, validate completeness before delivery.
