**GOAL**: Create detailed TDD implementation plans for all epic tasks with RED/GREEN/REFACTOR phases.

## [Input]
- `{REQ}/*.md`
- `{ARCH}/*.md`
- `{EPIC}`
- `{TMPL}/implementation-plan-tmpl.yaml`
- `{KNOWLEDGE}/*.md`

## [Output]
- `{PLAN}/{task_id}-plan.md`

## [Constraints]
- **MUST** use source document content only, **MUST NOT** fabricate requirements or tasks
- **MUST** complete requirement-architecture mapping, **MUST NOT** proceed without
- **MUST** record conflicts and request clarification, **MUST NOT** proceed with conflicts/missing files
- **MUST** apply knowledge base best practices, **MUST NOT** ignore

## [Steps]
1. Understand requirements, architecture, tasks, best practices → Complete context with planning criteria established
2. For each task: Plan RED (complete test coverage) → Comprehensive test plan
3. For each task: Plan GREEN (atomic minimal implementation steps) → Clear minimal implementation roadmap
4. For each task: Plan REFACTOR (quality improvements) → Quality improvement plan defined
5. Complete all plans, ensure executable and template-compliant → All implementation plans created

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Plan for each task with complete RED/GREEN/REFACTOR structure
- [ ] Proper requirement-architecture-test mapping
- [ ] All plan files at "{PLAN}/{task_id}-plan.md"

## [Example]

### Good #1
**Input**: Task-1: "Implement article publishing". REQ-001 (create/edit, Given-When-Then). Arch: Article Service (Express.js), PostgreSQL  
**Decision**: Read all inputs→Plan TDD phases for Task-1→RED: unit tests (model validation), integration tests (API+DB), behavior tests (Given-When-Then workflow)→GREEN: minimal Article model, API endpoints, basic DB ops→REFACTOR: validation, error handling, repository pattern from knowledge base→Map to src/services/ArticleService.js→Create docs/plans/1-plan.md with complete mapping  
**Why Good**: Derives from authoritative sources (req, arch, knowledge), structures RED/GREEN/REFACTOR with atomic steps

### Good #2
**Input**: Task-2: "Build transaction report". REQ-002 (aggregate by date range), NFR-001 (<2s). Arch: Reporting Service, TimescaleDB. Knowledge: best-practices-database-queries.md  
**Decision**: Review all inputs→Design TDD for Task-2→RED: unit tests (aggregation logic), integration tests (TimescaleDB, performance <2s), behavior tests (monthly report Given-When-Then)→GREEN: query with indexed date, aggregation logic, minimal API→REFACTOR: caching (Redis per knowledge), optimize with indexing best practices→Map to Reporting Service→docs/plans/2-plan.md with complete traceability  
**Why Good**: Integrates NFRs and knowledge-based optimizations, maintains template compliance and mapping discipline

### Bad #1
**Input**: Epic has 3 tasks  
**Bad Decision**: Create plan for Task-1 only, skip Task-2 and Task-3→Fabricate REQ IDs not in docs→Skip RED phase→Vague steps like "write some code"→No architecture mapping→Ignore knowledge base→Save incomplete  
**Why Bad**: Violates fabrication constraint, no complete mapping, skips RED phase, vague steps not atomic and executable  
**Correct**: Read all inputs (req, arch, epic, knowledge)→Create plans for ALL tasks→Use only actual REQ IDs→Plan all three phases (RED/GREEN/REFACTOR) with atomic steps→Map to specific components and REQ IDs→Apply knowledge base in REFACTOR→Verify complete traceability
