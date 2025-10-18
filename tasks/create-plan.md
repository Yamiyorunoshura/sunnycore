**GOAL**: Create detailed TDD implementation plan for a specific task with RED/GREEN/REFACTOR phases.

## [Context]
**You must read the following context:**
- `{REQ}/*.md`(Only the related documents)
- `{ARCH}/*.md`(Only the related documents)
- `{EPIC}`
- `{TMPL}/implementation-plan-tmpl.yaml`
- `{KNOWLEDGE}/*.md` (optional)

## [Products]
- `{PLAN}/{task_id}-plan.md`

## [Constraints]
- **MUST** extract planning intelligence from source documents only, **MUST NOT** fabricate requirements, architecture elements, or task mappings
- **MUST** construct complete traceability chains (REQ → Architecture → Tests → Implementation), **MUST NOT** proceed with broken chains
- **MUST** record conflicts/gaps and request clarification, **MUST NOT** resolve conflicts with assumptions
- **MUST** respect architecture decisions (ADRs, tech stack), **MUST NOT** override with knowledge base when conflicts arise
- **MUST** identify applicable knowledge base patterns, **MUST NOT** force-apply patterns that conflict with architecture

## [Instructions]
1. **Step 1: Gather Planning Intelligence**
- **GOAL:** Capture the information required by `implementation-plan-tmpl.yaml` to build a complete mental model for the task.
- **STEPS:**
  - Identify the relevant functional and non-functional requirements, including acceptance criteria, dependencies, and priorities.
  - Review architecture materials (tech stack tables, component responsibilities, data flows, ADRs) to note constraints and integration points.
  - Read the epic/task metadata to confirm scope, mapped requirements/components, dependencies, and quality gates.
  - Scan the knowledge base for patterns that reinforce requirements and architecture without creating conflicts.
- **QUESTIONS:**
  - Which requirements and acceptance criteria govern this task?
  - What architecture components and interfaces support those requirements?
  - Which dependencies or quality gates from the epic affect planning?
  - Do any knowledge base patterns apply without contradicting ADRs?
- **CHECKLIST:**
- [ ] Relevant REQ/NFR sources and acceptance criteria captured.
- [ ] Architecture constraints, integrations, and ADR decisions recorded.
- [ ] Epic dependencies, quality gates, and scope confirmed.
- [ ] Applicable knowledge patterns logged or conflicts flagged for clarification.

2. **Step 2: Build Traceability Chains**
- **GOAL:** Ensure every requirement links to planned tests, architecture components, and implementation files.
- **STEPS:**
  - Derive required behavior, integration, unit, and performance tests for each requirement and NFR.
  - Map each test to the architecture components, technologies, and interfaces it exercises.
  - Determine implementation and test file paths that align with the architecture structure and template expectations.
  - Draft the traceability table (REQ → Tests → Components → Files) and highlight missing links.
- **QUESTIONS:**
  - Do all functional and non-functional requirements have mapped tests?
  - Which components and files implement each planned test?
  - Are performance or integration layers required to satisfy constraints?
  - Where do traceability gaps or uncertainties remain?
- **CHECKLIST:**
- [ ] REQ-to-test mappings complete for functional and non-functional items.
- [ ] Tests mapped to architecture components and interfaces.
- [ ] Implementation and test file paths drafted per tech stack conventions.
- [ ] Traceability gaps or open questions documented for follow-up.

3. **Step 3: Plan TDD Phases**
- **GOAL:** Translate traceability into RED/GREEN/REFACTOR actions aligned with the template.
- **STEPS:**
  - Enumerate RED phase tests with expected failure reasons and file locations.
  - Outline minimal GREEN implementation steps that respect architecture constraints and traceability mappings.
  - Identify REFACTOR targets (quality, integration, performance, knowledge patterns) consistent with ADRs.
  - Define verification tasks for each phase, including test suite runs and coverage thresholds.
- **QUESTIONS:**
  - Which tests must fail first and what behaviors do they validate?
  - What minimal code changes will satisfy each test while honoring architecture decisions?
  - Which refactors improve quality without breaking GREEN?
  - How will verification ensure failure reasons, pass conditions, and coverage targets are met?
- **CHECKLIST:**
- [ ] RED phase tests listed with expected failures and file paths.
- [ ] GREEN steps linked to components, files, and corresponding tests.
- [ ] REFACTOR targets align with ADRs and applicable knowledge patterns.
- [ ] Phase-specific verification criteria (failures, exits, coverage) documented.

4. **Step 4: Resolve Conflicts and Finalize Plan**
- **GOAL:** Deliver a conflict-free, template-ready implementation plan.
- **STEPS:**
  - Review the plan for conflicts across requirements, architecture, and knowledge guidance.
  - Flag missing information or broken traceability chains that require clarification.
  - Summarize risks, dependencies, and rollback/mitigation expectations for the template’s risk and additional detail sections.
  - Confirm readiness of the `{PLAN}/{task_id}-plan.md` deliverable against template sections.
- **QUESTIONS:**
  - Are any conflicts or assumptions unresolved and needing clarification?
  - What gaps still block complete traceability or planning?
  - Have risks, dependencies, and mitigations been captured for the plan?
  - Does the plan satisfy all constraints and template deliverables?
- **CHECKLIST:**
- [ ] Conflicts and unanswered questions recorded with required follow-ups.
- [ ] Traceability chains validated end-to-end or gaps escalated.
- [ ] Risk, dependency, and mitigation notes prepared for the plan.
- [ ] Deliverable structure aligned with `implementation-plan-tmpl.yaml` sections and constraints.

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
2. Cannot find REQ-003 in `{REQ}/*.md`(Only the related documents) → **Assume** it's about payment processing, fabricate test cases
3. Cannot find "Payment Service" in `{ARCH}/*.md`(Only the related documents) → **Guess** it uses Stripe API and Node.js, plan accordingly
4. Create plan with fabricated REQ-003 tests and guessed Stripe integration
5. Skip Knowledge Base (no time)
6. Save plan file

**Why Bad**: 
- Violates "MUST NOT fabricate" constraint (invented REQ-003 content, guessed architecture)
- Violates "MUST NOT proceed with broken chains" constraint (proceeded despite missing REQ and Architecture component)
- Violates "MUST record conflicts and request clarification" constraint (did not halt and request clarification)

**Correct Approach**:
1. Read Epic, see Task-3 references REQ-003, REQ-004
2. Search `{REQ}/*.md`(Only the related documents) for REQ-003 → **Not found** → Record: "Missing REQ-003 referenced in Task-3"
3. Search `{ARCH}/*.md`(Only the related documents) for Payment Service → **Not found** → Record: "Missing Payment Service component referenced in Task-3"
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
