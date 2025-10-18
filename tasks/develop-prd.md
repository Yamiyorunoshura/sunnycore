**GOAL**: Complete all PRD development tasks in one iteration.

## [Context]
**You must read the following context:**
- `{PRD}`
- `{TMPL}/dev-notes-tmpl.yaml`

## [Products]
- `{root}/docs/prd-dev-notes.md`
- High-quality tested code aligned with architecture
- Complete test coverage

## [Constraints]
- **MUST** complete all PRD tasks, **MUST NOT** leave any incomplete
- **MUST** follow TDD cycle (RED→GREEN→REFACTOR), **MUST NOT** skip
- **MUST** document out-of-scope changes in dev notes, **MUST NOT** modify files silently
- **MUST** deliver with all tests passing (exit code 0), **MUST NOT** deliver failing tests

## [Instructions]
1. **Step 1: PRD Analysis**
- **GOAL:** Understand the full requirement set and derive an executable work plan.
- **STEPS:**
  - Read `{PRD}` end-to-end and inventory every REQ-XXX and NFR-XXX identifier.
  - Map dependencies between requirements, architecture components, and tasks.
  - Outline task sequencing that respects dependencies and aligns with the approved tech stack.
- **QUESTIONS:**
  - Which requirements unblock others or demand parallel work streams?
  - Do any PRD directives conflict with existing architecture or constraints?
  - What risks (integrations, novel tech, performance) require early mitigation?
- **CHECKLIST:**
  - [ ] Requirement inventory captured with ownership notes
  - [ ] Dependency graph and sequencing drafted
  - [ ] Risks and mitigation approach logged

2. **Step 2: TDD Implementation**
- **GOAL:** Deliver each feature through disciplined RED→GREEN→REFACTOR loops.
- **STEPS:**
  - Author failing unit and integration tests covering happy paths, edge cases, and error handling.
  - Implement the minimal code needed to turn the new tests green while honoring architecture patterns.
  - Refactor to remove duplication, improve structure, and keep observability in place with tests still passing.
- **QUESTIONS:**
  - Do the new tests cover the acceptance criteria and critical failure modes?
  - Are failure messages and assertions clear enough to guide debugging?
  - What refactors improve maintainability without breaking existing contracts?
- **CHECKLIST:**
  - [ ] Each feature started with failing automated tests
  - [ ] All new and existing tests pass after implementation
  - [ ] Refactoring completed with suite remaining green

3. **Step 3: Integration Validation**
- **GOAL:** Confirm cross-component workflows satisfy functional and non-functional expectations.
- **STEPS:**
  - Execute end-to-end or integration scenarios that traverse complete data flows.
  - Inject boundary failures to verify graceful degradation and error propagation.
  - Measure latency and throughput against documented NFR targets.
- **QUESTIONS:**
  - Do services exchange data using the expected contracts and schemas?
  - How does the system behave when upstream or downstream components fail?
  - Are performance metrics within the specified thresholds?
- **CHECKLIST:**
  - [ ] Critical workflows validated across component boundaries
  - [ ] Error handling confirmed at service and interface edges
  - [ ] Performance evidence collected for key NFRs

4. **Step 4: Quality Assurance**
- **GOAL:** Satisfy all quality gates before delivery.
- **STEPS:**
  - Run the full automated test suite and ensure exit code 0.
  - Generate coverage reports and confirm ≥80% for overall code and critical paths.
  - Execute linting and static analysis, resolving every violation.
- **QUESTIONS:**
  - Are any tests flaky or missing for high-risk areas?
  - Does coverage reveal untested acceptance criteria?
  - Do quality tools highlight architectural or style deviations to address?
- **CHECKLIST:**
  - [ ] Complete automated suite passes without retries
  - [ ] Coverage threshold documented and met
  - [ ] Lint/static analysis reports clean
  - [ ] Acceptance criteria mapped to verified evidence

5. **Step 5: Documentation**
- **GOAL:** Capture delivery outcomes and follow-ups in the canonical record.
- **STEPS:**
  - Update `{root}/docs/prd-dev-notes.md` to reflect work performed using `{TMPL}/dev-notes-tmpl.yaml`.
  - Document key decisions, deviations, risks, and supporting validation evidence.
  - Record follow-up actions or open questions requiring handoff.
- **QUESTIONS:**
  - Which decisions or risks need visibility for stakeholders?
  - Are acceptance criteria traceable to specific tests or metrics?
  - What outstanding items require future iterations or approvals?
- **CHECKLIST:**
  - [ ] Dev notes refreshed per template structure
  - [ ] Evidence links or attachments referenced
  - [ ] Follow-up items logged for next cycle

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] ALL PRD tasks implemented
- [ ] ALL tests passing (exit code 0)
- [ ] Code quality met (SOLID, DRY, functions ≤50 lines)
- [ ] Coverage ≥ 80%
- [ ] ALL acceptance criteria met
- [ ] Comprehensive prd-dev-notes.md created
- [ ] No linter errors

## [Example]

### Good #1
**Input**: PRD with REQ-001 (update profile), REQ-002 (avatar upload), NFR-001 (<200ms). Tasks: Task-1 (profile API), Task-2 (avatar storage)  
**Decision**: Understand all PRD. Develop strategy respecting dependencies (Task-1→Task-2). RED: write tests for PUT /profile, POST /profile/avatar (all fail correctly). GREEN: implement profile update, S3 avatar upload (all pass). REFACTOR: add validation, optimize image processing (tests stay green). Create prd-dev-notes.md. Validate all acceptance criteria.  
**Why Good**: This implements every requirement via full TDD loop, validates each phase, produces mandated documentation, and achieves 87% coverage.

### Good #2
**Input**: PRD with REQ-001 (rate limit per user), NFR-001 (100 req/min), NFR-002 (Redis storage). Tasks: middleware, config, monitoring  
**Decision**: Read PRD completely. Plan TDD. RED: tests for rate limit enforcement, exceed limit, reset after window (all fail). GREEN: Redis-based token bucket, Express middleware (all pass). REFACTOR: configurable limits, monitoring metrics (tests stay green). Document in prd-dev-notes.md. Verify NFRs (100 req/min enforced, monitoring functional).  
**Why Good**: This proves NFRs with tests and monitoring evidence, leaves thorough notes and configs, and achieves 82% coverage.

### Bad #1
**Input**: PRD with multiple tasks  
**Bad Decision**: Implement Task-1 only, skip others. Skip TDD entirely (write code without tests). Deliver with failing tests. No prd-dev-notes.md. Claim all complete.  
**Why Bad**: This violates complete all tasks, skips TDD cycle, delivers with failing tests, provides no dev notes. This produces incomplete unusable delivery.  
**Correct**: Execute ALL steps for ALL tasks. Develop strategy covering ALL PRD tasks. For each: RED (tests, verify fail)→GREEN (minimal, verify pass)→REFACTOR (quality). Create comprehensive prd-dev-notes.md. Verify ALL acceptance criteria. Ensure exit code 0.
