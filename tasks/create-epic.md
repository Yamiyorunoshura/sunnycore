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

## [Steps]
1. Understand requirements and architecture → Complete understanding with design criteria established
2. Create feature-level task breakdown → Well-structured task list with clear boundaries
3. Deduplicate, ensure actionable and traceable → Refined task list meeting quality criteria
4. Complete draft, obtain approval, save to "{EPIC}" → Approved epic created

## [DoD]
- [ ] Epic at "{EPIC}" with feature-level, outcome-oriented tasks mapped to requirements
- [ ] 100% requirement coverage
- [ ] kebab-case file names

## [Example]

### Good #1
**Input**: REQ-001 (ingestion), REQ-002 (ETL), REQ-003 (dashboard). Arch: Kafka Consumer, Spark Jobs, Dashboard Service  
**Decision**: Identify feature tasks (not steps)→Task-1: "Implement data ingestion" (REQ-001→Kafka Consumer, ≤14 chars)→Task-2: "Implement ETL pipeline" (REQ-002→Spark)→Task-3: "Build dashboard" (REQ-003→Dashboard)→100% coverage→Logical flow order→Clear DoD→Exclude operational actions→Approve→Save  
**Why Good**: Translates to feature-level with full traceability, preserves naming and DoD standards

### Good #2
**Input**: REQ-001 (product CRUD), REQ-002 (stock tracking), REQ-003 (alerts), REQ-004 (reports). Arch: Product Service, Inventory Service, Notification Service  
**Decision**: Map systematically→Task-1: "Product CRUD" (REQ-001→Product Service)→Task-2: "Stock tracking" (REQ-002→Inventory)→Task-3: "Alert system" (REQ-003→Notification)→Task-4: "Create reports" (REQ-004→Inventory)→100% coverage: 4 REQs→4 tasks→Dependencies: Task-3→Task-2→Feature-level (not atomic like "write test")→Checkbox format→Approve  
**Why Good**: One-to-one coverage with dependencies, required granularity and format

### Bad #1
**Input**: REQ-001, REQ-002, REQ-003 exist  
**Bad Decision**: Break to atomic level: "Write unit tests", "Create migration", "Run npm install", "Commit to git"→Skip requirement mapping→Long descriptions (>14 chars)→Include operational actions  
**Why Bad**: Violates feature-level constraint, includes operational actions, wrong granularity. Should be "Implement login" not atomic steps  
**Correct**: Create feature-level representing major deliverables→Map REQ→Task→Keep ≤14 chars→Focus on deliverables with verifiable outcomes→Exclude operational actions→Atomic breakdown happens in create-plan phase
