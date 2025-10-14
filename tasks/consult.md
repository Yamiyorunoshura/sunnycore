**GOAL**: Recommend optimal development workflow (full or PRD) based on requirement analysis.

## [Context]
**You must read the following context:**
- User requirement description
- `{ARCH}/*.md` (if exist)

## [Products]
- Workflow recommendation with command

## [Constraints]
- **MUST** correctly identify project type (Greenfield/Brownfield), **MUST NOT** misidentify
- **MUST** analyze existing architecture for Brownfield, **MUST NOT** skip
- **MUST** follow decision criteria, **MUST NOT** recommend incorrect workflow

## [Steps]
**You should work along to the following steps:**
1. Determine project type, gather context. This identifies the project type with context collected.
2. Analyze scope and architectural impact. This assesses complexity and impact.
3. Recommend workflow with rationale. This provides a clear recommendation.
4. Provide next-step command. This gives the user actionable guidance.

## [Instructions]

### 1. Project Type Determination
You must first determine whether the project is **Greenfield** (new project) or **Brownfield** (existing project):
- **Greenfield**: No existing architecture documents in `{ARCH}/`
- **Brownfield**: Architecture documents exist in `{ARCH}/`

For Brownfield projects, you must analyze the existing architecture to understand:
- Current components and their boundaries
- Existing technology stack
- Integration points and contracts
- Design patterns in use

### 2. Workflow Decision Criteria
Apply the following criteria to recommend the appropriate workflow:

**Full Workflow (*create-requirements)** is required when ANY of the following apply:
- New components or services need to be created
- Architecture changes are required (new patterns, modified boundaries)
- New technology stack or external integrations
- Cross-cutting concerns (security, observability, performance)
- Large scope: 5+ tasks expected
- Fundamental transformation (e.g., monolith to microservices)

**PRD Workflow (*create-prd)** is appropriate when ALL of the following apply:
- Within existing component boundaries
- Feature enhancements or bug fixes
- UI/UX changes without backend impact
- Small to medium scope: 1-5 tasks expected
- No new architectural patterns required
- Existing technology stack is sufficient

### 3. Recommendation Presentation
Your recommendation must include:
1. **Project Type**: Greenfield or Brownfield with evidence
2. **Scope Analysis**: Complexity assessment and impact analysis
3. **Workflow Recommendation**: Full or PRD with clear rationale
4. **Next-Step Command**: Exact command for the user to execute

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Project type determined with scope analyzed
- [ ] Workflow recommendation with command provided
- [ ] User understands rationale

## [Example]

### Good #1
**Input**: "Add product search with filters to e-commerce dashboard". Existing architecture: Product Service + API Gateway.  
**Decision**: Brownfield. Analyze scope: within Product Service boundaries, no new modules, 2-3 tasks. Recommend PRD workflow. Provide command: /sunnycore_pm *create-prd  
**Why Good**: This evaluates against architecture and decision criteria, and communicates rationale clearly.

### Good #2
**Input**: "Migrate monolith to microservices". Existing monolithic architecture.  
**Decision**: Brownfield. Analyze: fundamental arch change, multiple services needed, new patterns (service mesh), 10+ tasks. Recommend full workflow. Command: /sunnycore_pm *create-requirements  
**Why Good**: This recognizes transformational scope and maps to full workflow with concrete indicators.

### Bad #1
**Input**: "Add caching layer for API performance"  
**Bad Decision**: Immediately recommend full workflow without scope analysis or architecture review.  
**Why Bad**: This violates project type determination and skips architecture analysis. Caching typically requires 2-3 tasks within existing boundaries, which suggests PRD workflow.  
**Correct**: Check architecture exists. Analyze scope: Redis cache middleware, 2-3 tasks, no new modules. Recommend PRD with rationale.
