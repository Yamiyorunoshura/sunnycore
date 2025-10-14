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
**You should work along to the following steps:**
1. Understand all PRD requirements and architecture. This establishes complete strategy.
2. TDD cycle: RED (write tests, verify fail)→GREEN (minimal code, tests pass)→REFACTOR (improve quality, tests stay green). This implements all features with high quality.
3. Execute complete test suite, validate acceptance criteria. This verifies full integration and acceptance.
4. Create comprehensive dev notes at "{root}/docs/prd-dev-notes.md". This creates complete dev notes.
5. Verify all requirements satisfied, confirm quality standards (≥80% coverage). This ensures all requirements delivered with quality met.

## [Instructions]

### 1. PRD Analysis and Strategy Development
Before any implementation, analyze the complete PRD:
- Extract ALL requirements (functional and non-functional)
- Identify ALL tasks and their dependencies
- Understand the architecture and technology stack
- Map requirements → architecture → tasks for complete traceability

Develop an execution strategy:
- **Task Ordering**: Respect dependencies (e.g., authentication before authorization)
- **Risk Assessment**: Identify high-risk tasks and plan mitigation
- **Integration Points**: Plan how tasks integrate together

### 2. Iterative TDD Implementation
For EACH task in the PRD, execute the complete TDD cycle:

#### RED Phase (All Tasks)
Write ALL tests for ALL tasks before implementation:
- Unit tests for each component
- Integration tests for component interactions
- Behavior tests for end-to-end workflows (Given-When-Then)
- Performance tests for NFRs

**Verification**: Execute ALL tests and verify they fail correctly

#### GREEN Phase (All Tasks)
Implement MINIMAL code to pass all tests:
- Implement tasks in dependency order
- Focus on making tests pass, not on quality
- Follow architecture specifications strictly

**Verification**: Execute ALL tests and verify exit code 0 (all pass)

#### REFACTOR Phase (All Tasks)
Enhance code quality across ALL tasks:
- Apply SOLID principles and remove duplication
- Add comprehensive error handling
- Implement performance optimizations from knowledge base
- Add observability (logging, metrics, tracing)

**Verification**: Re-run ALL tests and verify they stay green

### 3. Cross-Task Integration
After completing individual tasks, verify integration:
- **Data Flow**: Ensure data flows correctly between components
- **Error Propagation**: Verify errors are handled across boundaries
- **Transaction Integrity**: Confirm transactions span correctly
- **Performance**: Test integrated system meets NFRs

### 4. Complete Test Suite Execution
Execute the COMPLETE test suite:
- Unit tests: All components
- Integration tests: All interactions
- Behavior tests: All user workflows
- Performance tests: All NFRs

**Requirement**: Exit code MUST be 0 (all tests passing)

### 5. Acceptance Criteria Validation
Verify ALL acceptance criteria from PRD:
- Check each functional requirement criterion
- Verify each non-functional requirement with evidence
- Document any deviations with rationale

### 6. Comprehensive Dev Notes
Create `{root}/docs/prd-dev-notes.md` with complete documentation:

**Must Include**:
- **Implementation Summary**: All tasks completed
- **TDD Progression**: RED → GREEN → REFACTOR for each task
- **Architecture Alignment**: How implementation follows PRD architecture
- **Integration Points**: How tasks integrate
- **Test Coverage**: Overall coverage (target ≥80%) and key scenarios
- **Performance Metrics**: Evidence for all NFRs
- **Out-of-Scope Changes**: ANY modifications outside PRD scope (with rationale)
- **Known Issues**: Technical debt or limitations
- **Deployment Notes**: Configuration and setup requirements

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
