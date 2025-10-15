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

## [Steps]
**Execute these steps in sequence:**
1. **Analyze PRD**: Extract requirements, identify dependencies, plan task sequence
2. **TDD Implementation**: RED→GREEN→REFACTOR cycle for all tasks with quality focus
3. **Integration Validation**: Verify cross-component functionality and acceptance criteria
4. **Quality Assurance**: Confirm all tests pass, coverage ≥80%, code quality standards met
5. **Documentation**: Generate comprehensive dev notes using template

## [Instructions]

### 1. PRD Analysis and Strategy Development
**How to analyze the PRD systematically:**
- **Requirements Extraction**: Scan PRD for REQ-XXX and NFR-XXX identifiers, categorize by functional domain (auth, data, UI, etc.)
- **Dependency Mapping**: Create task dependency graph - identify which components must exist before others can be built
- **Technology Stack Verification**: Confirm PRD-specified technologies align with architecture, note any conflicts
- **Risk Identification**: Flag tasks involving external integrations, complex algorithms, or new technologies for extra attention

**How to develop execution strategy:**
- **Sequence Tasks**: Start with foundational components (data models, core services), then build dependent features
- **Batch Similar Work**: Group related tasks (e.g., all API endpoints, all UI components) for efficiency
- **Plan Integration Points**: Identify where components connect and plan integration testing approach

### 2. TDD Implementation with Quality Focus
**How to execute RED→GREEN→REFACTOR effectively:**

#### RED Phase: Write Failing Tests First
- **Test Types**: Unit tests (component behavior), integration tests (component interactions), e2e tests (user workflows)
- **Test Strategy**: Write tests for happy path, error cases, edge cases, and performance requirements
- **Verification Method**: Run test suite, confirm each new test fails with expected error message

#### GREEN Phase: Minimal Implementation
- **Implementation Focus**: Write simplest code that makes tests pass, prioritize correctness over elegance  
- **Quality Standards**: Follow architecture patterns, maintain consistent naming, add basic error handling
- **Verification Method**: All tests pass (exit code 0), no skipped or ignored tests

#### REFACTOR Phase: Enhance Quality
- **Code Quality**: Apply SOLID principles, eliminate duplication, ensure functions ≤50 lines
- **Error Handling**: Add comprehensive validation, meaningful error messages, proper exception propagation
- **Performance**: Optimize hot paths, add caching where beneficial, implement async patterns for I/O
- **Observability**: Add structured logging with correlation IDs, key metrics, distributed tracing spans
- **Verification Method**: Tests remain green, code quality tools report no violations

### 3. Integration Validation
**How to verify cross-component functionality:**
- **Data Flow Testing**: Trace data through complete workflows (input→processing→output), verify transforms and persistence
- **Error Boundary Testing**: Inject failures at component boundaries, confirm proper error propagation and recovery
- **Transaction Testing**: Verify ACID properties across multi-component operations, test rollback scenarios
- **Performance Validation**: Run load tests on integrated system, measure end-to-end latency against NFR targets

### 4. Quality Assurance
**How to ensure delivery quality:**
- **Test Execution**: Run full test suite (unit + integration + e2e), verify 100% pass rate with exit code 0
- **Coverage Analysis**: Generate coverage report, ensure ≥80% line coverage, 100% coverage of critical paths
- **Code Quality**: Run linters and static analysis, fix all violations, confirm functions ≤50 lines
- **Acceptance Criteria**: Map each PRD acceptance criterion to test evidence, document any deviations with technical rationale

### 5. Documentation Generation
**How to create comprehensive dev notes:**
- **Use Template**: Follow `{TMPL}/dev-notes-tmpl.yaml` structure for complete documentation
- **Focus on Decisions**: Document significant technical choices, challenges overcome, and deviations from plan
- **Evidence-Based**: Include test results, coverage reports, performance metrics as verification evidence
- **Actionable Insights**: Record lessons learned and recommendations for future development

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
