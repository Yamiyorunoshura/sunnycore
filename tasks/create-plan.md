**GOAL**: Create detailed TDD implementation plans for all epic tasks with RED/GREEN/REFACTOR phases.

## [Context]
**You must read the following context:**
- `{REQ}/*.md`
- `{ARCH}/*.md`
- `{EPIC}`
- `{TMPL}/implementation-plan-tmpl.yaml`
- `{KNOWLEDGE}/*.md`

## [Products]
- `{PLAN}/{task_id}-plan.md`

## [Constraints]
- **MUST** extract planning intelligence from source documents only, **MUST NOT** fabricate requirements, architecture elements, or task mappings
- **MUST** construct complete traceability chains (REQ → Architecture → Tests → Implementation), **MUST NOT** proceed with broken chains
- **MUST** record conflicts/gaps and request clarification, **MUST NOT** resolve conflicts with assumptions
- **MUST** respect architecture decisions (ADRs, tech stack), **MUST NOT** override with knowledge base when conflicts arise
- **MUST** identify applicable knowledge base patterns, **MUST NOT** force-apply patterns that conflict with architecture

## [Steps]
**You should work along to the following steps:**
1. Extract planning intelligence from requirements, architecture, tasks, knowledge base. This builds the mental model of what needs to be tested, implemented, and optimized.
2. Construct traceability chains linking REQ → Architecture → Tests → Implementation. This ensures every requirement is testable and implementable.
3. Apply TDD decision logic for RED/GREEN/REFACTOR phases. This translates traceability chains into executable test-driven plans.
4. Resolve conflicts, gaps, and ambiguities through structured analysis. This ensures plans are complete and conflict-free before execution.

## [Instructions]

### 1. Extract Planning Intelligence

**Objective**: Build a mental model of the system by extracting key planning information from source documents.

#### From Requirements (`{REQ}/*.md`)

**Functional Requirements (REQ-XXX):**
- **Given-When-Then → Test Scenarios**: Each acceptance criterion maps to at least one behavior test
  - *Given* (initial state) → Test setup / Arrange phase
  - *When* (action) → Test execution / Act phase
  - *Then* (outcome) → Test assertions / Assert phase
- **Dependencies**: Identify requirement chains that dictate implementation order
- **Priority**: Critical/High requirements should be validated with more comprehensive test coverage

**Non-Functional Requirements (NFR-XXX):**
- **Target Metrics → Performance Assertions**: Extract quantifiable thresholds (e.g., "< 2s" → `assert response_time < 2000ms`)
- **Measurement Methods**: Determine test strategy (load testing, profiling, benchmarking)
- **Category**: Map to REFACTOR concerns (Performance → caching/indexing, Security → input validation/encryption)

**Decision Logic:**
- If REQ has multiple Given-When-Then scenarios → Plan separate test case for each scenario
- If NFR specifies measurement method → Use that method in performance test design
- If REQ Priority = Critical → Plan unit + integration + behavior tests (full coverage)
- If REQ Priority = Low → Plan behavior tests only (functional coverage)

#### From Architecture (`{ARCH}/*.md`)

**Technical Stack Table:**
- **Technology + Version → Implementation Constraints**: Use exact versions in plan (e.g., "Express.js 4.18" → specify middleware patterns for that version)
- **Purpose + Rationale → Technology Application**: Understand why chosen to apply correctly (e.g., "PostgreSQL for ACID compliance" → plan transactional tests)

**Components Section:**
- **Responsibility → Test Scope**: Component purpose defines what to test (e.g., "Auth Service: JWT generation" → test token creation, validation, expiry)
- **Key Interfaces/APIs → Integration Test Points**: Each exposed interface needs integration test coverage
- **Dependencies → Test Mocking Strategy**: External dependencies should be mocked in unit tests, real in integration tests
- **Data Storage → Database Test Setup**: Identify which database/schema to use in test environment

**Data Flows + Sequence Diagrams:**
- **Flow Steps → Integration Test Sequences**: Each step in sequence diagram maps to integration test stages
- **Synchronous vs Asynchronous → Test Timing Strategy**: Async flows need await/callback/promise handling in tests

**Architecture Decision Records (ADRs):**
- **Decision + Rationale → Implementation Patterns**: ADRs define architectural patterns to follow (e.g., "ADR-003: Event-driven for decoupling" → plan event publisher/subscriber in implementation)
- **Alternatives Considered → Knowledge Base Override Rules**: If ADR explicitly rejected an approach, do NOT apply that approach from knowledge base

**Decision Logic:**
- If Component has Dependencies → Plan integration tests covering component interactions
- If Data Flow is Asynchronous → Plan async test handling (event listeners, message queues)
- If ADR documents a decision → Respect that decision over conflicting knowledge base patterns

#### From Epic (`{EPIC}`)

**Task Metadata:**
- **Description → Feature Scope**: Defines boundaries of what this plan should cover
- **Requirements List → Traceability Anchors**: These REQ-XXX IDs are the traceability starting points
- **Architecture List → Implementation Targets**: These component names define where code will live
- **Dependencies → Planning Order**: Dependent tasks may reuse tests/components from prerequisite tasks
- **Quality-Gate → Additional Test Requirements**: Supplement standard TDD tests with task-specific validation

**Decision Logic:**
- If Task depends on another task → Review that task's plan first, reuse test fixtures/setup where applicable
- If Quality-Gate specifies coverage threshold → Ensure test plan meets or exceeds that threshold

#### From Knowledge Base (`{KNOWLEDGE}/*.md`, if exists)

**Best Practice Patterns:**
- **Applicable Context → Selective Application**: Identify when pattern applies (e.g., "caching for read-heavy workloads" → only apply if NFR indicates high read volume)
- **Implementation Guidance → REFACTOR Phase Input**: Knowledge base informs quality improvements, not initial implementation

**Decision Logic:**
- If Knowledge pattern conflicts with Architecture ADR → Ignore knowledge pattern, follow ADR
- If Knowledge pattern addresses an NFR → Apply pattern in REFACTOR phase
- If Knowledge pattern is generic best practice (e.g., input validation) → Apply in REFACTOR phase
- If Knowledge pattern suggests different tech stack → Do NOT apply, respect Architecture tech stack table

**Conflict Detection:**
- Record as conflict: REQ references component not in Architecture, Task maps to non-existent REQ, Architecture tech stack conflicts with REQ constraints
- Request clarification: Do NOT proceed, do NOT invent missing information

---

### 2. Construct Traceability Chains

**Objective**: Build explicit mappings from requirements through tests to implementation, ensuring every requirement is testable and traceable.

#### Build REQ → Test Cases Mapping

For each REQ-XXX referenced in Task:
1. **Extract Test Scenarios**: Each Given-When-Then → One test case name
   - Example: REQ-001 "Given user is logged in, When user creates article, Then article is saved" → `test_authenticated_user_can_create_article()`
2. **Determine Test Layers**:
   - **Behavior Test**: Always create for each Given-When-Then (end-to-end validation)
   - **Integration Test**: Create if REQ involves database, external API, or multiple components
   - **Unit Test**: Create for complex business logic extracted from REQ description
3. **Map NFR → Performance Test**:
   - Example: NFR-001 "Report generation < 2s" → `test_report_generation_performance()` with `assert duration < 2.0`

#### Build Architecture → Implementation Files Mapping

For each Component referenced in Task:
1. **Locate Component Definition**: Find component in `{ARCH}/*.md` Components section
2. **Extract Technology Stack**: Component's "Technology" field defines implementation language/framework
3. **Derive File Paths**: Use Architecture's "Work Directory Structure" + Component name + Tech stack conventions
   - Example: "Article Service" + "Express.js" + Work Structure → `src/services/ArticleService.js`, `src/routes/articles.js`
4. **Identify Test File Paths**: Apply framework's test conventions
   - Example: Express.js project → `tests/unit/services/ArticleService.test.js`, `tests/integration/articles.test.js`

#### Build Complete Traceability Table

| Requirement | Acceptance Criterion | Test Case Name | Test Layer | Architecture Component | Implementation File |
|-------------|---------------------|----------------|------------|----------------------|---------------------|
| REQ-001 | Given logged in, When create article, Then saved | test_authenticated_user_can_create_article | Behavior | Article Service | src/services/ArticleService.js |
| REQ-001 | (same) | test_article_save_to_database | Integration | Article Service, PostgreSQL | src/services/ArticleService.js |
| REQ-001 | (same) | test_article_validation | Unit | Article Service | src/services/ArticleService.js |
| NFR-001 | Report generation < 2s | test_report_generation_performance | Performance | Reporting Service | src/services/ReportingService.js |

**Verification**:
- Every REQ-XXX in Task → At least one Test Case
- Every Test Case → Mapped to Architecture Component
- Every Architecture Component → Mapped to Implementation File Path
- If any mapping is missing → Record as gap and request clarification

---

### 3. Apply TDD Decision Logic

**Objective**: Use traceability chains to decide what tests to write (RED), what minimal code to write (GREEN), and what improvements to make (REFACTOR).

#### RED Phase: Decide Test Coverage

**Decision Tree for Test Layer Selection:**

```
For each REQ-XXX:
├─ Has Given-When-Then?
│  └─ YES → Create Behavior Test (end-to-end workflow)
│
├─ Involves multiple components / database / external API?
│  └─ YES → Create Integration Test
│
├─ Contains complex business logic / calculations / validations?
│  └─ YES → Create Unit Test for that logic
│
└─ Has related NFR-XXX?
   └─ YES → Create Performance/Security/Reliability Test per NFR category
```

**Test Content Decisions:**
- **Behavior Test**: Follow Given-When-Then structure directly from REQ
  - Setup: Create initial state from "Given"
  - Execute: Perform action from "When"
  - Assert: Verify outcome from "Then"
- **Integration Test**: Follow Data Flow from Architecture
  - Test component → component communication
  - Test component → database operations (using real test DB)
  - Test component → external API (using mocks/stubs)
- **Unit Test**: Isolate business logic
  - Mock all dependencies (database, external services, other components)
  - Focus on edge cases and validation rules from REQ description
- **Performance Test**: Use NFR target metric as assertion
  - Example: NFR-001 "< 2s" → `start = time(); execute(); end = time(); assert (end - start) < 2.0`

**Test Naming Convention** (derive from framework in Tech Stack):
- Extract testing framework from Architecture Technical Stack table
- Apply that framework's naming conventions
- Example: Jest → `describe()` blocks + `test()` / `it()` functions

#### GREEN Phase: Decide Minimal Implementation Steps

**Atomicity Principle**: Each step should make exactly one failing test pass.

**Step Granularity Decision:**
```
For each failing test:
├─ Test requires data model?
│  └─ Step: "Create {Model} class/schema with fields {list from REQ}"
│
├─ Test requires API endpoint?
│  └─ Step: "Implement {METHOD} {path} endpoint with {framework from tech stack}"
│
├─ Test requires database operation?
│  └─ Step: "Add {operation} method using {database from tech stack}"
│
├─ Test requires external API call?
│  └─ Step: "Implement {API name} client with {endpoint from Architecture}"
│
└─ Test requires business logic?
   └─ Step: "Implement {function name} with {algorithm/validation from REQ}"
```

**File Path Decision**: Use Implementation File from traceability table

**Technology Application**: Use exact technology + version from Architecture Technical Stack table
- Example: "PostgreSQL 14.2" → Use PostgreSQL-specific syntax (e.g., `RETURNING` clause)
- Example: "Express.js 4.18" → Use Express 4.x middleware patterns (not Express 5.x)

**Dependency Handling**:
- If Task has Dependencies in Epic → Reference implementation files from dependent task plans
- If Component has Dependencies in Architecture → Plan to import/instantiate those dependencies

#### REFACTOR Phase: Decide Quality Improvements

**Priority Order (descending):**
1. **NFR-Driven Improvements**: Address non-functional requirements first
2. **Architecture-Driven Improvements**: Apply patterns from ADRs and Cross-Cutting Concerns
3. **Knowledge Base Improvements**: Apply applicable best practices (only if no conflict with Architecture)
4. **General Code Quality**: Extract reusable patterns, apply SOLID principles

**Decision Logic per NFR Category:**
- **Performance NFR** → Check Architecture for caching strategy, indexing, query optimization; apply Knowledge Base performance patterns if compatible
- **Security NFR** → Check Architecture Cross-Cutting Concerns for auth/encryption approach; apply Knowledge Base security patterns if compatible
- **Reliability NFR** → Check Architecture for retry/circuit breaker patterns; apply Knowledge Base reliability patterns if compatible
- **Scalability NFR** → Check Architecture Deployment section for scaling strategy; apply Knowledge Base scalability patterns if compatible

**Knowledge Base Integration Logic:**
```
For each Knowledge Base pattern:
├─ Does Architecture ADR explicitly reject this pattern?
│  └─ YES → Skip pattern, document reason
│
├─ Does pattern conflict with Tech Stack table?
│  └─ YES → Skip pattern (e.g., Knowledge suggests Redis, Architecture chose Memcached → use Memcached)
│
├─ Does pattern address an NFR from requirements?
│  └─ YES → Apply pattern, reference NFR-XXX and Knowledge file
│
├─ Is pattern a general best practice (logging, error handling, validation)?
│  └─ YES → Apply pattern, reference Knowledge file
│
└─ Otherwise
   └─ Evaluate applicability based on REQ and Architecture context
```

**Refactoring Steps Format**:
- "Extract {pattern name} from {Knowledge file} to address {NFR-XXX}"
- "Apply {Architecture Cross-Cutting Concern} for {category}"
- "Refactor {code element} to follow {SOLID principle}"

---

### 4. Resolve Conflicts, Gaps, and Ambiguities

**Objective**: Identify and handle issues before creating plan files.

#### Conflict Types and Resolution

**Type 1: Requirement Conflicts**
- **Detection**: Two REQs specify contradictory behaviors
- **Resolution**: Record both REQ IDs and contradictory statements → Request clarification → HALT planning

**Type 2: Architecture Gaps**
- **Detection**: Task references Architecture component not defined in `{ARCH}/*.md`
- **Resolution**: Record missing component name → Request clarification → HALT planning
- **Fallback** (if minor): Infer component from REQ + Tech Stack, mark as `[INFERRED]`, proceed with warning

**Type 3: Traceability Breaks**
- **Detection**: Task maps to REQ-XXX not found in `{REQ}/*.md`
- **Resolution**: Record missing REQ ID → Request clarification → HALT planning

**Type 4: Knowledge vs Architecture Conflicts**
- **Detection**: Knowledge Base recommends approach explicitly rejected in Architecture ADR
- **Resolution**: Follow Architecture ADR → Ignore Knowledge pattern → Document decision in plan
- **Example**: ADR-005 rejects microservices → Knowledge suggests service mesh → Ignore service mesh pattern

**Type 5: Tech Stack Ambiguities**
- **Detection**: Architecture Technical Stack table missing version numbers or rationale
- **Resolution**: Use specified technology without version assumptions → Proceed, note ambiguity in plan

#### Gap Analysis Checklist

Before finalizing plans, verify:
- [ ] Every Task in Epic has been planned
- [ ] Every REQ-XXX referenced in Task exists in `{REQ}/*.md`
- [ ] Every Architecture Component referenced in Task exists in `{ARCH}/*.md`
- [ ] Every Test Case in plan maps to at least one REQ
- [ ] Every Implementation File in plan maps to Architecture Component
- [ ] All NFRs have corresponding performance/security/reliability tests
- [ ] All Knowledge Base patterns applied are compatible with Architecture decisions

**If any check fails**: Record gap details, request clarification, do NOT fabricate information.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Complete traceability chains constructed: Every REQ → Test Cases → Architecture Components → Implementation Files
- [ ] TDD decision logic applied: RED (test coverage decisions documented), GREEN (atomic step granularity justified), REFACTOR (improvement priorities explained)
- [ ] Conflict resolution completed: All gaps/conflicts recorded or resolved, no fabricated information
- [ ] Knowledge base patterns evaluated: Applied only where compatible with Architecture decisions (ADRs, tech stack)
- [ ] Plan files created: One plan file per Task at `{PLAN}/{task_id}-plan.md` following `{TMPL}/implementation-plan-tmpl.yaml`

## [Example]

### Good #1: Traceability-Driven Planning
**Input**: Task-1: "Implement article publishing". REQ-001 has 2 Given-When-Then scenarios (create, edit). Arch: Article Service (Express.js 4.18, PostgreSQL 14). Work Structure: `src/services/`, `src/routes/`. No knowledge base.

**Decision Process**:
1. **Extract Intelligence**:
   - REQ-001 Scenario 1: "Given logged-in user, When POST article, Then saved to DB" → Behavior test: `test_authenticated_user_creates_article`
   - REQ-001 Scenario 2: "Given existing article, When PUT article, Then updated in DB" → Behavior test: `test_authenticated_user_edits_article`
   - REQ-001 Description mentions "title and content required" → Unit test: `test_article_validation_rejects_missing_fields`
   - Architecture: Article Service uses Express.js 4.18 → Test framework likely Jest or Mocha (check Tech Stack table)
   - Architecture: PostgreSQL 14 → Integration tests need real test DB with migrations

2. **Construct Traceability**:
   | REQ | Scenario | Test Case | Layer | Component | File |
   |-----|----------|-----------|-------|-----------|------|
   | REQ-001 | Create (G-W-T #1) | test_authenticated_user_creates_article | Behavior | Article Service | src/services/ArticleService.js |
   | REQ-001 | Edit (G-W-T #2) | test_authenticated_user_edits_article | Behavior | Article Service | src/services/ArticleService.js |
   | REQ-001 | Validation | test_article_validation | Unit | Article Service | src/services/ArticleService.js |
   | REQ-001 | DB operations | test_article_save_and_update | Integration | Article Service + PostgreSQL | src/services/ArticleService.js |

3. **Apply TDD Logic**:
   - **RED**: 4 tests (2 behavior, 1 unit, 1 integration) based on Given-When-Then extraction
   - **GREEN**: Atomic steps = (1) Create Article model with title/content fields, (2) POST /articles endpoint, (3) PUT /articles/:id endpoint, (4) Save/update DB methods with PostgreSQL 14 `RETURNING` syntax
   - **REFACTOR**: No NFRs → Focus on code quality (extract validation logic, apply Express error handling middleware)

4. **Conflict Resolution**: No conflicts detected. All REQs exist, Architecture component defined, Tech stack complete.

**Why Good**: This demonstrates extraction of test scenarios from Given-When-Then, traceability table construction, TDD decision logic (test layer selection, atomic step granularity based on "one test passing" principle), and technology-specific implementation details (PostgreSQL 14 syntax).

---

### Good #2: NFR-Driven Planning with Knowledge Base
**Input**: Task-2: "Build transaction report". REQ-002 (aggregate by date range, Given-When-Then). NFR-001 (<2s response, Performance category). Arch: Reporting Service (Node.js 18, TimescaleDB 2.9), ADR-007 (chose TimescaleDB for time-series). Knowledge: `best-practices-timeseries.md` suggests "continuous aggregates".

**Decision Process**:
1. **Extract Intelligence**:
   - REQ-002: "Given date range, When request report, Then aggregate transactions" → Behavior test: `test_report_aggregates_by_date_range`
   - NFR-001: "< 2s" → Performance test: `test_report_generation_under_2_seconds` with `assert duration < 2000ms`
   - Architecture ADR-007: Chose TimescaleDB for time-series optimization → Integration test should use TimescaleDB-specific features (hypertables)
   - Knowledge Base: Suggests "continuous aggregates" for performance → Evaluate applicability

2. **Construct Traceability**:
   | REQ/NFR | Criterion | Test Case | Layer | Component | File |
   |---------|-----------|-----------|-------|-----------|------|
   | REQ-002 | Aggregate (G-W-T) | test_report_aggregates_by_date_range | Behavior | Reporting Service | src/services/ReportingService.js |
   | REQ-002 | DB query | test_timescaledb_query_with_hypertable | Integration | Reporting Service + TimescaleDB | src/services/ReportingService.js |
   | NFR-001 | < 2s | test_report_generation_under_2_seconds | Performance | Reporting Service | src/services/ReportingService.js |

3. **Apply TDD Logic**:
   - **RED**: 3 tests (1 behavior from Given-When-Then, 1 integration for TimescaleDB, 1 performance for NFR-001 threshold)
   - **GREEN**: Atomic steps = (1) Create Report model, (2) GET /reports endpoint with date params, (3) TimescaleDB query using hypertable (from ADR-007), (4) Aggregation logic
   - **REFACTOR Priority**:
     1. NFR-001 (Performance): Apply Knowledge Base "continuous aggregates" pattern (compatible with ADR-007 TimescaleDB choice)
     2. Architecture: Check Cross-Cutting Concerns for caching strategy
     3. General: Extract query builder, add input validation

4. **Knowledge Base Evaluation**:
   - Pattern: "continuous aggregates" from `best-practices-timeseries.md`
   - Check: Does ADR-007 reject this? No, ADR-007 chose TimescaleDB specifically for time-series features
   - Check: Does it address NFR-001? Yes, pre-computed aggregates improve query performance
   - Decision: Apply in REFACTOR phase, reference both NFR-001 and Knowledge file

**Why Good**: This demonstrates NFR extraction (quantified metric → test assertion), Architecture ADR respect (use TimescaleDB features), Knowledge Base evaluation logic (check compatibility with ADR, apply to address NFR), and REFACTOR prioritization (NFR-driven first).

---

### Bad #1: Fabrication and Missing Traceability
**Input**: Task-3 references REQ-003, REQ-004. Epic maps Task-3 to "Payment Service" component.

**Bad Decision Process**:
1. Read Epic, see Task-3 needs Payment Service
2. Cannot find REQ-003 in `{REQ}/*.md` → **Assume** it's about payment processing, fabricate test cases
3. Cannot find "Payment Service" in `{ARCH}/*.md` → **Guess** it uses Stripe API and Node.js, plan accordingly
4. Create plan with fabricated REQ-003 tests and guessed Stripe integration
5. Skip Knowledge Base (no time)
6. Save plan file

**Why Bad**: 
- Violates "MUST NOT fabricate" constraint (invented REQ-003 content, guessed architecture)
- Violates "MUST NOT proceed with broken chains" constraint (proceeded despite missing REQ and Architecture component)
- Violates "MUST record conflicts and request clarification" constraint (did not halt and request clarification)

**Correct Approach**:
1. Read Epic, see Task-3 references REQ-003, REQ-004
2. Search `{REQ}/*.md` for REQ-003 → **Not found** → Record: "Missing REQ-003 referenced in Task-3"
3. Search `{ARCH}/*.md` for Payment Service → **Not found** → Record: "Missing Payment Service component referenced in Task-3"
4. **Request Clarification**: "Task-3 references REQ-003 and REQ-004 not found in requirements. Task-3 references Payment Service not defined in architecture. Please provide missing documents or update Task-3 mappings."
5. **HALT planning** for Task-3 until clarification received
6. Proceed with other tasks if possible

**Key Lesson**: When traceability chain breaks (missing REQ or Architecture component), ALWAYS halt and request clarification. NEVER fabricate or assume missing information. The goal is complete, accurate traceability, not speedy but incorrect planning.

---

### Bad #2: Knowledge Base Override of Architecture
**Input**: Task-4: "Implement caching". REQ-005 (cache user sessions). Architecture ADR-009: "Chose Memcached over Redis due to simpler deployment in our infrastructure". Knowledge: `caching-patterns.md` recommends Redis for session storage with persistence.

**Bad Decision Process**:
1. Extract REQ-005: cache user sessions
2. Read Knowledge Base: recommends Redis with persistence for sessions
3. **Decision**: Use Redis (from Knowledge) because it's better for sessions
4. Plan implementation with Redis
5. Ignore Architecture ADR-009

**Why Bad**:
- Violates "MUST respect architecture decisions" constraint
- Violates "MUST NOT override with knowledge base when conflicts arise" constraint
- Architecture ADR-009 explicitly chose Memcached with rationale (simpler deployment)
- Knowledge Base should inform, not override, Architecture decisions

**Correct Approach**:
1. Extract REQ-005: cache user sessions
2. Read Knowledge Base: recommends Redis
3. Read Architecture ADR-009: chose Memcached, rejected Redis (deployment complexity)
4. **Detect Conflict**: Knowledge recommends Redis, ADR-009 explicitly chose Memcached
5. **Resolution**: Follow Architecture ADR-009 → Use Memcached
6. **Document in Plan**: "Knowledge Base suggests Redis for session persistence, but ADR-009 chose Memcached for simpler deployment. Respecting Architecture decision. Trade-off: No session persistence (Memcached is memory-only), mitigated by REQ-005 accepting session loss on cache restart."
7. Plan implementation with Memcached (from Architecture)

**Key Lesson**: Architecture ADRs are authoritative. When Knowledge Base conflicts with ADRs, always follow ADRs and document the decision rationale. Knowledge Base informs REFACTOR improvements but does not override fundamental architecture choices.
