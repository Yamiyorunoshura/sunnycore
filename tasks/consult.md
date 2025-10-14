**GOAL**: Recommend optimal development workflow (full or PRD) based on requirement analysis.

## [Input]
- User requirement description
- `{ARCH}/*.md` (if exist)

## [Output]
- Workflow recommendation with command

## [Constraints]
- **MUST** correctly identify project type (Greenfield/Brownfield), **MUST NOT** misidentify
- **MUST** analyze existing architecture for Brownfield, **MUST NOT** skip
- **MUST** follow decision criteria, **MUST NOT** recommend incorrect workflow

## [Steps]
1. Determine project type, gather context → Project type identified with context collected
2. Analyze scope and architectural impact → Complexity and impact assessed
3. Recommend workflow with rationale → Clear recommendation provided
4. Provide next-step command → User receives actionable guidance

## [Decision-Criteria]
**Full Workflow (*create-requirements)**: New components, architecture changes, new tech stack, external integrations, modified boundaries, cross-cutting concerns, large scope (5+ tasks)

**PRD Workflow (*create-prd)**: Within existing boundaries, feature enhancements, bug fixes, UI/UX changes, small-medium scope (1-5 tasks), no new patterns

## [DoD]
- [ ] Project type determined with scope analyzed
- [ ] Workflow recommendation with command provided
- [ ] User understands rationale

## [Example]

### Good #1
**Input**: "Add product search with filters to e-commerce dashboard". Existing architecture: Product Service + API Gateway.  
**Decision**: Brownfield→Analyze scope: within Product Service boundaries, no new modules, 2-3 tasks→Recommend PRD workflow→Provide command: /sunnycore_pm *create-prd  
**Why Good**: Evaluates against architecture and decision criteria, communicates rationale clearly

### Good #2
**Input**: "Migrate monolith to microservices". Existing monolithic architecture.  
**Decision**: Brownfield→Analyze: fundamental arch change, multiple services needed, new patterns (service mesh), 10+ tasks→Recommend full workflow→Command: /sunnycore_pm *create-requirements  
**Why Good**: Recognizes transformational scope, maps to full workflow with concrete indicators

### Bad #1
**Input**: "Add caching layer for API performance"  
**Bad Decision**: Immediately recommend full workflow without scope analysis or architecture review  
**Why Bad**: Violates project type determination, skips architecture analysis. Caching typically 2-3 tasks within existing boundaries→PRD workflow  
**Correct**: Check architecture exists→Analyze scope: Redis cache middleware, 2-3 tasks, no new modules→Recommend PRD with rationale
