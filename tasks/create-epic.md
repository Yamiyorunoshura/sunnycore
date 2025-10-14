**GOAL**: Create feature-level task list breaking down requirements into executable tasks.

## [Input]
- `{REQ}/*.md`
- `{ARCH}/*.md`
- `{TMPL}/epic-tmpl.yaml`

## [Output]
- `{EPIC}`

## [Constraints]
- **MUST** create feature-level tasks, **MUST NOT** go below feature granularity
- **MUST** focus on deliverables, **MUST NOT** include operational actions unless requested
- **MUST** use kebab-case, **MUST NOT** use spaces in file names

## [Instructions]

### 1. Task Granularity
Create **feature-level** tasks that represent major deliverables, not atomic implementation steps:

**Correct Granularity** (Feature-level):
- ✓ "Implement user authentication"
- ✓ "Build product catalog"
- ✓ "Create payment integration"

**Incorrect Granularity** (Too atomic):
- ✗ "Write unit tests for login"
- ✗ "Create database migration"
- ✗ "Run npm install"
- ✗ "Commit code to git"

Atomic breakdown happens later in the `*create-plan` phase. Epic tasks should be completable in 1-3 days of focused work.

### 2. Requirement-Task Mapping
Ensure 100% requirement coverage by creating a mapping table:
| Requirement ID | Task ID | Task Name | Architecture Component |
|---------------|---------|-----------|------------------------|
| REQ-001 | 1 | implement-data-ingestion | Kafka Consumer |
| REQ-002 | 2 | implement-etl-pipeline | Spark Jobs |
| REQ-003 | 3 | build-dashboard | Dashboard Service |

Every requirement must map to at least one task. Complex requirements may span multiple tasks.

### 3. Task Naming Conventions
Follow these naming rules:
- **Format**: `{verb}-{noun}` in kebab-case
- **Length**: ≤14 characters (excluding task ID)
- **Examples**: "implement-auth", "build-api", "create-reports"

### 4. Operational Actions Exclusion
Do NOT include operational or process tasks unless explicitly requested:
- ✗ Testing (covered in TDD workflow)
- ✗ Linting (part of development standards)
- ✗ Deployment (separate operational concern)
- ✗ Documentation (embedded in dev-notes)
- ✗ Code review (part of review workflow)

Focus only on **deliverable features** that provide user or business value.

### 5. Task Dependencies
Identify and document dependencies between tasks:
- Use checkbox format: `- [ ] Task-1: implement-auth`
- Mark dependencies: `Task-3 depends on Task-1 completion`
- Order tasks logically based on dependencies

### 6. Definition of Done (DoD)
For each task, define clear, verifiable completion criteria:
- All acceptance criteria met
- Tests passing (unit + integration + behavior)
- Code quality standards met
- Documentation complete

## [Steps]
1. Understand requirements and architecture. This establishes complete understanding with design criteria.
2. Create feature-level task breakdown. This produces well-structured task list with clear boundaries.
3. Deduplicate, ensure actionable and traceable. This refines the task list meeting quality criteria.
4. Complete draft, obtain approval, save to "{EPIC}". This creates the approved epic.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Epic at "{EPIC}" with feature-level, outcome-oriented tasks mapped to requirements
- [ ] 100% requirement coverage
- [ ] kebab-case file names

## [Example]

### Good #1
**Input**: REQ-001 (ingestion), REQ-002 (ETL), REQ-003 (dashboard). Arch: Kafka Consumer, Spark Jobs, Dashboard Service  
**Decision**: Identify feature tasks (not steps). Task-1: "Implement data ingestion" (REQ-001→Kafka Consumer, ≤14 chars). Task-2: "Implement ETL pipeline" (REQ-002→Spark). Task-3: "Build dashboard" (REQ-003→Dashboard). Achieve 100% coverage. Order by logical flow. Define clear DoD. Exclude operational actions. Obtain approval. Save successfully.  
**Why Good**: This translates to feature-level with full traceability and preserves naming and DoD standards.

### Good #2
**Input**: REQ-001 (product CRUD), REQ-002 (stock tracking), REQ-003 (alerts), REQ-004 (reports). Arch: Product Service, Inventory Service, Notification Service  
**Decision**: Map systematically. Task-1: "Product CRUD" (REQ-001→Product Service). Task-2: "Stock tracking" (REQ-002→Inventory). Task-3: "Alert system" (REQ-003→Notification). Task-4: "Create reports" (REQ-004→Inventory). Achieve 100% coverage: 4 REQs→4 tasks. Define dependencies: Task-3→Task-2. Use feature-level (not atomic like "write test"). Apply checkbox format. Obtain approval.  
**Why Good**: This provides one-to-one coverage with dependencies at required granularity and format.

### Bad #1
**Input**: REQ-001, REQ-002, REQ-003 exist  
**Bad Decision**: Break to atomic level: "Write unit tests", "Create migration", "Run npm install", "Commit to git". Skip requirement mapping. Use long descriptions (>14 chars). Include operational actions.  
**Why Bad**: This violates feature-level constraint and includes operational actions at wrong granularity. Should be "Implement login" not atomic steps.  
**Correct**: Create feature-level representing major deliverables. Map REQ→Task. Keep ≤14 chars. Focus on deliverables with verifiable outcomes. Exclude operational actions. Atomic breakdown happens in create-plan phase.
