**GOAL**: Create detailed TDD implementation plans for all epic tasks with RED/GREEN/REFACTOR phases.

## [Input]
**You must read the following documents:**
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
**You should work along to the following steps:**
1. Understand requirements, architecture, tasks, best practices. This establishes complete context with planning criteria.
2. For each task: Plan RED (complete test coverage). This creates comprehensive test plan.
3. For each task: Plan GREEN (atomic minimal implementation steps). This creates clear minimal implementation roadmap.
4. For each task: Plan REFACTOR (quality improvements). This defines quality improvement plan.
5. Complete all plans, ensure executable and template-compliant. This creates all implementation plans.

## [Instructions]

### 1. Context Gathering
Before creating any plan, gather complete context:
- Read ALL requirements from `{REQ}/*.md`
- Read ALL architecture documents from `{ARCH}/*.md`
- Read ALL tasks from `{EPIC}`
- Read ALL best practices from `{KNOWLEDGE}/*.md` (if exists)

Verify that:
- Every task in the epic maps to at least one requirement
- Every requirement has a corresponding architecture component
- No conflicts exist between requirements and architecture

If any issues are found, record them and request clarification. Do NOT proceed with fabricated or assumed information.

### 2. TDD Phase Planning
For each task, create a complete TDD implementation plan with three phases:

#### RED Phase (Test First)
Plan comprehensive test coverage BEFORE any implementation:
- **Unit Tests**: Test individual functions and classes in isolation
- **Integration Tests**: Test component interactions and database operations
- **Behavior Tests**: Test end-to-end workflows using Given-When-Then format from requirements
- **Performance Tests**: Test non-functional requirements (if specified)

For each test, specify:
- Test name and description
- Expected behavior (from requirements)
- Assertions to verify correctness

#### GREEN Phase (Minimal Implementation)
Plan atomic, minimal implementation steps to pass tests:
- Break down into smallest possible increments
- Each step should be independently verifiable
- Map to specific files and components from architecture
- Focus on making tests pass, not on optimizations

Example atomic steps:
1. "Create Article model with title and content fields"
2. "Implement POST /articles endpoint with basic validation"
3. "Add database save operation for Article"

#### REFACTOR Phase (Quality Improvement)
Plan quality enhancements while maintaining green tests:
- **Code Quality**: Extract reusable patterns, apply SOLID principles
- **Error Handling**: Add comprehensive error handling and validation
- **Performance**: Apply optimizations from knowledge base
- **Security**: Implement security best practices
- **Observability**: Add logging, metrics, and tracing

### 3. Traceability Mapping
For each plan, create explicit traceability:
| Requirement | Architecture Component | Test Cases | Implementation Files |
|------------|----------------------|-----------|---------------------|
| REQ-001 | Article Service | test_article_creation, test_article_validation | src/services/ArticleService.js |
| NFR-001 (<2s) | Reporting Service | test_performance_report_generation | src/services/ReportingService.js |

This ensures complete traceability from requirements through implementation.

### 4. Knowledge Base Integration
Apply best practices from the knowledge base:
- Reference specific patterns: `{KNOWLEDGE}/best-practices-database-queries.md#indexing`
- Apply security guidelines: `{KNOWLEDGE}/security-patterns.md#input-validation`
- Use performance optimizations: `{KNOWLEDGE}/performance-tips.md#caching-strategy`

Document which best practices are applied in each REFACTOR phase.

### 5. Plan Completeness
Ensure ALL tasks have plans:
- If the epic has 5 tasks, create 5 plan files
- Verify each plan file exists at `{PLAN}/{task_id}-plan.md`
- Confirm all plans follow the template structure

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Plan for each task with complete RED/GREEN/REFACTOR structure
- [ ] Proper requirement-architecture-test mapping
- [ ] All plan files at "{PLAN}/{task_id}-plan.md"

## [Example]

### Good #1
**Input**: Task-1: "Implement article publishing". REQ-001 (create/edit, Given-When-Then). Arch: Article Service (Express.js), PostgreSQL  
**Decision**: Read all inputs. Plan TDD phases for Task-1. RED: unit tests (model validation), integration tests (API+DB), behavior tests (Given-When-Then workflow). GREEN: minimal Article model, API endpoints, basic DB ops. REFACTOR: validation, error handling, repository pattern from knowledge base. Map to src/services/ArticleService.js. Create docs/plans/1-plan.md with complete mapping.  
**Why Good**: This derives from authoritative sources (req, arch, knowledge) and structures RED/GREEN/REFACTOR with atomic steps.

### Good #2
**Input**: Task-2: "Build transaction report". REQ-002 (aggregate by date range), NFR-001 (<2s). Arch: Reporting Service, TimescaleDB. Knowledge: best-practices-database-queries.md  
**Decision**: Review all inputs. Design TDD for Task-2. RED: unit tests (aggregation logic), integration tests (TimescaleDB, performance <2s), behavior tests (monthly report Given-When-Then). GREEN: query with indexed date, aggregation logic, minimal API. REFACTOR: caching (Redis per knowledge), optimize with indexing best practices. Map to Reporting Service. Create docs/plans/2-plan.md with complete traceability.  
**Why Good**: This integrates NFRs and knowledge-based optimizations while maintaining template compliance and mapping discipline.

### Bad #1
**Input**: Epic has 3 tasks  
**Bad Decision**: Create plan for Task-1 only, skip Task-2 and Task-3. Fabricate REQ IDs not in docs. Skip RED phase. Use vague steps like "write some code". Omit architecture mapping. Ignore knowledge base. Save incomplete.  
**Why Bad**: This violates fabrication constraint, provides no complete mapping, skips RED phase, and uses vague steps that are not atomic and executable.  
**Correct**: Read all inputs (req, arch, epic, knowledge). Create plans for ALL tasks. Use only actual REQ IDs. Plan all three phases (RED/GREEN/REFACTOR) with atomic steps. Map to specific components and REQ IDs. Apply knowledge base in REFACTOR. Verify complete traceability.
