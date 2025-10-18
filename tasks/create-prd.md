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

## [Steps]
**You should work along to the following steps:**
1. **Project Analysis**: Determine project type and gather all relevant context to understand scope and constraints.
2. **Requirements Engineering**: Create verifiable functional requirements and quantified non-functional requirements with clear acceptance criteria.
3. **Architecture Integration**: Design or extend architecture ensuring complete requirement mapping and impact analysis for Brownfield.
4. **Task Planning**: Break down into feature-level implementation tasks with clear Definition of Done and requirement traceability.
5. **PRD Finalization**: Integrate all sections with traceability matrix, obtain stakeholder approval, and deliver complete PRD.

## [Instructions]

### 1. Project Analysis
**Objective**: Establish project foundation and approach strategy.

**For All Projects:**
- Examine user requirements to identify core functionality and constraints
- Determine project boundaries and success criteria
- Assess technical and business constraints

**Project Type Decision:**
- **Greenfield**: `{ARCH}/` is empty or non-existent → design from scratch
- **Brownfield**: Existing architecture in `{ARCH}/` → extend with impact analysis

**Context Gathering Focus:**
- Understand user goals and pain points
- Identify integration requirements and external dependencies  
- Assess technical constraints and compliance needs

### 2. Requirements Engineering
**Objective**: Transform user needs into verifiable, measurable requirements.

**Functional Requirements Focus:**
- Create atomic, testable requirements using Given-When-Then format
- Ensure each requirement addresses a specific user capability
- Prioritize based on user value and technical dependencies
- Link requirements to clear business objectives

**Non-Functional Requirements Focus:**
- Quantify ALL performance requirements with specific metrics (P95, P99 latency thresholds)
- Define scalability targets with concrete user/data volume limits
- Specify reliability targets with measurable uptime and error rate SLAs
- Document security requirements with specific compliance standards

### 3. Architecture Integration
**Objective**: Create or extend architecture that fully satisfies requirements.

**For Greenfield Projects:**
- Design components that directly map to functional requirements
- Select technology stack based on NFR constraints and team capabilities
- Document architectural decisions with clear rationale and trade-offs
- Create comprehensive component interaction patterns

**For Brownfield Projects:**
- Analyze existing architecture thoroughly before making changes
- Document impact of every proposed change on existing components
- Preserve existing contracts unless breaking changes are essential
- Design extension points that minimize disruption to current functionality
- Create detailed migration strategies for any breaking changes

**Architecture Quality Focus:**
- Ensure every requirement maps to specific architectural elements
- Validate that architecture can satisfy all NFR targets
- Document integration patterns and data flow clearly
- Address cross-cutting concerns (security, monitoring, error handling)

### 4. Task Planning
**Objective**: Create implementable tasks with clear deliverables.

**Task Breakdown Strategy:**
- Focus on feature-level granularity that delivers user value
- Map each task to specific requirements and architecture components
- Define clear Definition of Done with testable completion criteria
- Establish task dependencies and implementation sequence

**Quality Assurance Focus:**
- Ensure tasks include comprehensive testing requirements
- Define code quality standards and review processes
- Include integration testing and performance validation
- Plan for security testing and compliance verification

### 5. PRD Integration
**Objective**: Create unified document with complete traceability.

**Integration Focus:**
- Build comprehensive traceability matrix linking requirements → architecture → tasks
- Validate 100% requirement coverage across all sections
- Document assumptions, risks, and mitigation strategies
- Define measurable success criteria for project completion

**Quality Validation:**
- Verify all requirements are testable and measurable
- Ensure architecture fully supports all functional and non-functional requirements
- Confirm task breakdown provides complete implementation coverage
- Validate impact analysis completeness for Brownfield projects

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
