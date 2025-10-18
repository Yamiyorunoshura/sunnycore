**GOAL**: Execute TDD development following implementation plan to deliver working code with comprehensive test coverage.

## [Context]
**You must read the following context:**
- `{PLAN}/{task_id}-plan.md` - Implementation plan with traceability chains, test cases, and implementation steps
- `{ARCH}/*.md`(Only the related documents) - Architecture documents containing technical stack, components, data flows, and ADRs
- `{TMPL}/dev-notes-tmpl.yaml` - Template for documenting implementation outcomes

## [Products]
- Working code implementation (all tests passing, exit code 0)
- Comprehensive test suite (unit + integration + behavior + performance tests where applicable)
- `{DEVNOTES}/{task_id}-dev-notes.md` following template structure

## [Constraints]
- **MUST** follow strict TDD cycle (RED→GREEN→REFACTOR), **MUST NOT** skip phases or write production code before tests
- **MUST** implement according to plan's traceability chains and architecture specifications, **MUST NOT** deviate without documented rationale
- **MUST** deliver with all tests passing (exit code 0), **MUST NOT** deliver with failing or skipped tests
- **MUST** respect architecture decisions (tech stack, ADRs, component boundaries), **MUST NOT** introduce technologies not in architecture
- **MUST** achieve test coverage ≥80%, **MUST NOT** deliver untested critical paths

## [Steps]
**You should work along to the following steps:**
1. Extract implementation intelligence from plan and architecture. This builds complete understanding of what to build and how to build it.
2. **RED Phase**: Write all test cases from plan, verify they fail correctly. This ensures test suite is complete and fails for right reasons.
3. **GREEN Phase**: Write minimal implementation to pass tests, verify all pass. This ensures working functionality with exit code 0.
4. **REFACTOR Phase**: Improve code quality while maintaining green tests. This ensures production-ready code quality.
5. Document implementation in dev notes following template. This completes implementation record.

## [Instructions]

### 1. Extract Implementation Intelligence

**Objective**: Build complete mental model of what to implement and how to implement it by extracting structured information from plan and architecture.

#### From Implementation Plan (`{PLAN}/{task_id}-plan.md`)

**Traceability Chains**: 
- Map Requirements → Test Cases → Architecture Components → Implementation Files
- Verify every test case maps to a requirement and implementation target
- Identify dependencies between test cases

**Test Case Specifications**:
- Extract test names, test layers (unit/integration/behavior/performance)
- Understand test setup requirements (fixtures, mocks, test data)
- Note expected assertions and success criteria

**Implementation Steps**:
- Review GREEN phase steps (minimal implementation sequence)
- Review REFACTOR phase priorities (quality improvements order)
- Identify atomic implementation units (one step = one test passing)

**Acceptance Criteria**:
- Extract Definition of Done checklist from plan
- Identify performance targets from NFRs (if applicable)
- Note quality gates (coverage thresholds, code standards)

#### From Architecture Documents (`{ARCH}/*.md`(Only the related documents))

**Technical Stack** (from Technical Stack table):
- Exact technology versions to use (language, framework, database)
- Framework-specific patterns and conventions
- Testing tools and frameworks specified

**Component Specifications** (from Components section):
- Component responsibilities and boundaries
- Key interfaces and APIs to implement
- Dependencies to inject or mock
- Data storage patterns to follow

**Architecture Decisions** (from ADRs):
- Architectural patterns to apply (event-driven, hexagonal, etc.)
- Technology choices rationale (why this over alternatives)
- Trade-offs and constraints to respect

**File Structure** (from Work Directory Structure):
- Where to create implementation files
- Where to create test files
- Naming conventions to follow

#### Verification Before Proceeding

**Gap Detection**:
- [ ] Every test case in plan has clear requirements traceability
- [ ] Every implementation step references concrete architecture components
- [ ] All technologies referenced in plan exist in architecture tech stack
- [ ] File paths align with architecture work directory structure

**If gaps found**: Record gap details, request clarification, do NOT proceed with fabricated information.

**Blocking Conditions** (HALT and request guidance):
- Plan file missing or incomplete (no test cases or implementation steps)
- Architecture documents missing critical information (no tech stack, no components)
- Test framework not specified in architecture
- Conflicting information between plan and architecture

### 2. RED Phase: Write All Tests First

**Objective**: Implement complete test suite from plan BEFORE any production code, verify tests fail for correct reasons.

#### Test Implementation Decision Logic

**For each test case listed in plan's RED phase**:

1. **Determine Test Layer** (from plan's test case table):
   - Unit Test → Test single function/class in isolation with mocked dependencies
   - Integration Test → Test component interactions with real dependencies (database, APIs)
   - Behavior Test → Test end-to-end user workflow (Given-When-Then from requirements)
   - Performance Test → Test NFR targets with time/resource assertions

2. **Locate Test File Path** (from plan's traceability or architecture work structure):
   - Apply testing framework conventions from architecture tech stack
   - Example: Jest → `tests/unit/{component}.test.js`, `tests/integration/{feature}.test.js`

3. **Apply Test Framework Patterns** (from architecture tech stack):
   - Extract test framework and version from architecture
   - Use framework-specific syntax (Jest: `describe()`/`test()`, pytest: `def test_*`, etc.)
   - Follow framework's mocking patterns (Jest: `jest.mock()`, pytest: `@patch`)

4. **Structure Test Content** (from plan's test case specifications):
   - **Behavior Tests**: Follow Given-When-Then from requirements
     - Setup: Arrange initial state from "Given"
     - Execute: Perform action from "When"
     - Assert: Verify outcome from "Then"
   - **Integration Tests**: Follow data flows from architecture
     - Test component → component communication
     - Test component → database with real test database
     - Test component → external API with mocks/stubs
   - **Unit Tests**: Isolate business logic
     - Mock ALL dependencies (use architecture's dependency injection patterns)
     - Focus on edge cases and validation rules from requirements
   - **Performance Tests**: Use NFR metrics as assertions
     - Example: NFR-001 "< 2s" → `start = time(); execute(); assert (time() - start) < 2.0`

5. **Setup Test Environment**:
   - Create test fixtures from plan's test setup requirements
   - Initialize test database schema (if integration tests)
   - Configure mocks for external services (from architecture external APIs section)

#### Execution and Verification

**Run Test Suite**:
```bash
{test_command from architecture tech stack}
```

**Expected Outcome**: ALL tests FAIL

**Verify Failure Reasons** (critical validation):
- ✓ Tests fail because implementation doesn't exist (`ModuleNotFoundError`, `undefined`, etc.)
- ✗ Tests fail because of test bugs (syntax errors, wrong assertions, incorrect mocks)

**If tests fail for wrong reasons**: Fix test code, NOT implementation code

**Exit Criteria**:
- [ ] All test cases from plan implemented
- [ ] Test suite executes without syntax/import errors
- [ ] All tests fail with expected error messages (not found, undefined, etc.)
- [ ] Test failure count matches plan's test case count

### 3. GREEN Phase: Minimal Implementation to Pass Tests

**Objective**: Write simplest possible code to make ALL tests pass, following architecture specifications.

#### Implementation Decision Logic

**For each failing test** (process in order from plan's GREEN phase steps):

1. **Identify Implementation Target** (from plan's traceability):
   - Locate implementation file path (from traceability table)
   - Identify component/class/function to implement
   - Verify file location aligns with architecture work directory structure

2. **Apply Technology Stack** (from architecture tech stack table):
   - Use exact technology and version specified
   - Apply framework-specific patterns and conventions
   - Example: "Express.js 4.18" → Use Express 4.x middleware patterns (not Express 5.x)
   - Example: "PostgreSQL 14.2" → Use PostgreSQL 14 syntax features (e.g., `RETURNING` clause)

3. **Implement Atomic Unit** (from plan's GREEN step description):
   - Each step should make exactly ONE test (or test group) pass
   - Follow step's implementation guidance from plan
   - Examples of atomic units:
     - Create data model/schema with fields from requirements
     - Implement API endpoint with framework from tech stack
     - Add database operation using database from tech stack
     - Implement business logic function from requirements

4. **Follow Architecture Patterns** (from architecture components and ADRs):
   - **Component Boundaries**: Implement within specified component's responsibility
   - **Dependency Injection**: Use architecture's dependency patterns for component dependencies
   - **Data Storage**: Use database and schema design from architecture
   - **API Contracts**: Follow interface specifications from architecture components section
   - **ADR Patterns**: Apply architectural decisions (e.g., event-driven, hexagonal, etc.)

5. **Minimal Implementation Principles**:
   - Write ONLY code needed to pass currently failing tests
   - DO NOT add features not tested by current test suite
   - DO NOT optimize for performance (defer to REFACTOR)
   - DO NOT add comprehensive error handling (defer to REFACTOR)
   - Use simplest algorithm that satisfies test assertions

#### Execution and Verification

**After each atomic implementation**:
1. Run test suite: `{test_command from architecture}`
2. Verify more tests pass (at least one)
3. Verify no previously passing tests now fail (regression check)

**Repeat** until all tests pass.

**Final Verification**:
```bash
{test_command from architecture}
```

**Expected Outcome**: ALL tests PASS, exit code 0

**Exit Criteria**:
- [ ] All tests from RED phase now passing
- [ ] Test suite exit code = 0
- [ ] No skipped or ignored tests
- [ ] Implementation files created match plan's traceability table
- [ ] All code uses technologies from architecture tech stack

### 4. REFACTOR Phase: Improve Code Quality While Maintaining Green Tests

**Objective**: Transform minimal implementation into production-ready code following plan's REFACTOR priorities, architecture patterns, and quality standards.

#### Refactoring Priority Order (from plan's REFACTOR phase)

**Apply improvements in this sequence**:

1. **NFR-Driven Improvements** (if NFRs exist in plan):
   - **Performance NFRs** → Apply caching, indexing, query optimization from architecture
   - **Security NFRs** → Apply authentication, encryption, validation from architecture cross-cutting concerns
   - **Reliability NFRs** → Apply retry logic, circuit breakers from architecture
   - **Scalability NFRs** → Apply horizontal scaling patterns from architecture deployment section
   
   **Verification**: Run performance/security tests after each NFR improvement

2. **Architecture Pattern Application** (from ADRs and cross-cutting concerns):
   - Extract patterns documented in architecture ADRs
   - Apply cross-cutting concerns (logging, monitoring, error handling)
   - Follow architectural style (event-driven, hexagonal, etc.)
   
   **Example**: ADR-003 "Event-driven for decoupling" → Extract event publisher/subscriber pattern

3. **Code Quality Improvements** (SOLID, DRY, Clean Code):
   - **Single Responsibility**: Extract classes/functions with one clear purpose
   - **Open/Closed**: Use interfaces for extensibility
   - **Dependency Inversion**: Depend on abstractions, inject dependencies
   - **DRY**: Extract duplicated logic into reusable functions
   - **Naming**: Use clear, descriptive names from domain language
   - **Function Size**: Keep functions ≤ 50 lines
   - **Complexity**: Keep cyclomatic complexity ≤ 10

4. **Error Handling and Validation**:
   - Add input validation with clear error messages
   - Implement graceful error handling (try-catch, error middleware)
   - Add defensive programming for edge cases
   - Follow error handling patterns from architecture

5. **Observability** (from architecture cross-cutting concerns):
   - Add structured logging at key decision points
   - Add metrics collection for monitoring
   - Add distributed tracing (if applicable)
   - Implement health check endpoints

#### Refactoring Execution Pattern

**For each improvement from plan's REFACTOR list**:

1. **Apply one refactoring** (extract function, add validation, etc.)
2. **Run test suite** immediately: `{test_command}`
3. **Verify tests STAY GREEN** (exit code 0)
4. **If tests fail**: Revert refactoring, fix issue, try again
5. **If tests pass**: Commit improvement, proceed to next

**Critical Rule**: NEVER make multiple refactorings without running tests in between

#### Code Quality Standards (must achieve)

**Quantitative Metrics**:
- [ ] Test coverage ≥ 80% (run coverage tool from architecture)
- [ ] Functions ≤ 50 lines (check with linter)
- [ ] Cyclomatic complexity ≤ 10 (check with complexity tool)
- [ ] No linter errors (run linter from architecture tech stack)

**Qualitative Standards**:
- [ ] All architecture ADR patterns applied
- [ ] All NFR improvements from plan implemented
- [ ] Error handling covers edge cases from requirements
- [ ] Code follows framework conventions from tech stack

#### Final Verification

**Run complete quality check**:
```bash
{linter_command from architecture}  # Should report 0 errors
{test_command from architecture}    # Should exit 0
{coverage_command from architecture} # Should report ≥80%
```

**Exit Criteria**:
- [ ] All improvements from plan's REFACTOR phase applied
- [ ] All tests still passing (exit code 0)
- [ ] Code quality standards met (coverage ≥80%, functions ≤50 lines, complexity ≤10)
- [ ] No linter errors
- [ ] All NFRs validated (performance tests, security tests passing)

### 5. Document Implementation Outcomes

**Objective**: Create comprehensive development notes recording what was implemented, decisions made, and outcomes achieved.

#### Create or Update Dev Notes

**File**: `{DEVNOTES}/{task_id}-dev-notes.md`

**Follow Template**: `{TMPL}/dev-notes-tmpl.yaml`

**Key Documentation Requirements**:
- Record TDD cycle execution (RED → GREEN → REFACTOR phases)
- Document technical decisions and rationale
- List all files created/modified with purposes
- Report test coverage and results (all tests must pass)
- Note any deviations from plan with justification
- Document challenges encountered and solutions applied
- Record any technical debt or known issues

**Critical Items to Document**:
1. **Out-of-Scope Changes**: If ANY files were modified outside plan's traceability scope, document with clear rationale
2. **Architecture Deviations**: If implementation differs from architecture specifications, document why and impact
3. **Performance Metrics**: If NFRs exist, include actual measurements vs targets
4. **Acceptance Criteria Status**: Confirm each criterion from plan is met or document exceptions

#### Validate Acceptance Criteria

**Before finalizing dev notes**, verify against plan's Definition of Done:
- [ ] All functional requirements from plan implemented
- [ ] All NFR targets achieved (with evidence from tests)
- [ ] All acceptance criteria from plan satisfied
- [ ] Any deviations documented with rationale

**Provide Evidence**:
- Test results showing all tests passing (exit code 0)
- Coverage report showing ≥80%
- Performance test results (if applicable)
- Linter output showing 0 errors

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Complete intelligence extraction: Plan and architecture fully understood, no gaps detected
- [ ] RED phase complete: All test cases implemented, all failing for correct reasons (not test bugs)
- [ ] GREEN phase complete: All tests passing (exit code 0), implementation aligned with architecture
- [ ] REFACTOR phase complete: Code quality standards met (coverage ≥80%, functions ≤50 lines, complexity ≤10, no linter errors)
- [ ] Dev notes complete: `{DEVNOTES}/{task_id}-dev-notes.md` created following template with all sections filled
- [ ] Acceptance criteria validated: All criteria from plan met with evidence provided

## [Example]

### Good #1: Full TDD Cycle with Architecture Alignment
**Input**: Plan for Task-1 (article publishing). Plan has 4 test cases (2 behavior, 1 unit, 1 integration). Architecture: Express.js 4.18, PostgreSQL 14, Jest testing. Plan specifies traceability: REQ-001 → ArticleService → `src/services/ArticleService.js`.

**Decision Process**:
1. **Extract Intelligence**: Read plan's traceability table, extract test cases (test_create_article, test_edit_article, test_validation, test_db_operations). Read architecture tech stack (Express 4.18, PostgreSQL 14, Jest). Read architecture ADR-002 (RESTful API design). Verify all paths align with architecture work structure.
2. **RED**: Write 4 test files following Jest patterns from architecture. Setup test DB from PostgreSQL schema. Run `npm test` → 4 failures with "ArticleService not defined". Verify failures correct (implementation missing, NOT test bugs).
3. **GREEN**: Create ArticleService class with minimal methods. Implement POST /articles and PUT /articles/:id endpoints. Add basic save/update DB methods with PostgreSQL 14 RETURNING syntax. Run `npm test` → exit code 0, all pass.
4. **REFACTOR**: Apply plan's REFACTOR priorities: (1) Extract validation logic per ADR-002, (2) Add error handling middleware, (3) Extract query builder. Run `npm test` after each → stays green. Run coverage → 85%.
5. **Document**: Create dev notes following template. Record TDD phases, list files (ArticleService.js, articles.test.js), report coverage 85%, confirm acceptance criteria met.

**Why Good**: This demonstrates complete intelligence extraction (plan + architecture), strict TDD cycle with verification at each phase, architecture alignment (uses Express 4.18 patterns, PostgreSQL 14 syntax, follows ADR-002), and achieves quality gates (exit code 0, coverage 85%, dev notes complete).

---

### Good #2: NFR-Driven Development with Performance Validation
**Input**: Plan for Task-2 (transaction reports). Plan has NFR-001 (<2s response). Architecture: Node.js 18, TimescaleDB 2.9, continuous aggregates pattern from ADR-007. Plan's REFACTOR phase prioritizes NFR-001 first.

**Decision Process**:
1. **Extract Intelligence**: Read plan's traceability (REQ-002, NFR-001 → ReportingService). Read architecture ADR-007 (chose TimescaleDB for time-series, use continuous aggregates). Extract performance target (<2s from NFR-001). Note plan's REFACTOR priority: apply continuous aggregates for NFR-001.
2. **RED**: Write behavior test (test_report_by_date_range) and performance test (test_report_under_2_seconds with `assert duration < 2000ms`). Run tests → fail (service missing).
3. **GREEN**: Create ReportingService with basic TimescaleDB query using hypertables. Run tests → all pass, performance test shows 1.8s (meets NFR).
4. **REFACTOR**: Priority 1 (NFR): Apply continuous aggregates pattern from ADR-007 → performance improves to 120ms. Priority 2: Add error handling. Priority 3: Extract query builder. Run tests after each → stay green. Coverage 82%.
5. **Document**: Create dev notes. Record performance improvement (1.8s → 120ms after continuous aggregates). Reference ADR-007 in technical decisions section. Confirm NFR-001 met with evidence.

**Why Good**: This demonstrates NFR extraction and validation, architecture ADR adherence (TimescaleDB features, continuous aggregates), REFACTOR prioritization (NFR first), and evidence-based acceptance (performance metrics documented).

---

### Bad #1: Skipping TDD Cycle
**Input**: Plan for Task-3 exists with 8 test cases and GREEN/REFACTOR steps.

**Bad Decision**: Skip RED phase entirely. Write implementation with all optimizations immediately (caching + validation + logging). Run tests as afterthought → 5/8 pass, 3 fail. Try to fix failing tests by modifying assertions. Give up, mark complete with "mostly working".

**Why Bad**: Violates Constraint 1 (no TDD cycle, skipped RED phase). Violates Constraint 3 (exit code ≠ 0, failing tests). Violates Quality-Gates (RED not complete, GREEN not verified, exit code not 0). Makes debugging impossible (can't identify which implementation caused failures).

**Correct Approach**: 
1. **RED**: Write all 8 tests first, verify fail with correct reasons (implementation missing)
2. **GREEN**: Write minimal code to pass tests ONE AT A TIME, verify exit code 0
3. **REFACTOR**: Add optimizations incrementally while maintaining green tests
4. **Document**: Create dev notes with complete TDD cycle record

---

### Bad #2: Ignoring Architecture Specifications
**Input**: Plan references Express.js 4.18 and PostgreSQL from architecture. Plan's traceability specifies `src/services/` directory structure.

**Bad Decision**: Read plan but skip architecture docs. Implement using Express 5.x (not in architecture). Use MongoDB instead of PostgreSQL (not in tech stack). Create files in `app/controllers/` (not in work structure). Tests pass but code incompatible with project.

**Why Bad**: Violates Constraint 4 (ignored architecture tech stack, introduced unapproved technologies). Violates Quality-Gates (implementation NOT aligned with architecture). Creates integration failures with rest of system.

**Correct Approach**:
1. **Extract Intelligence**: Read architecture tech stack table → use EXACT versions (Express 4.18, PostgreSQL 14)
2. **Verify File Paths**: Check architecture work directory structure → create files in specified locations
3. **Apply Framework Patterns**: Use Express 4.x middleware patterns (not Express 5.x)
4. **Respect ADRs**: Follow all architecture decisions without deviation

---

### Bad #3: Inadequate Documentation
**Input**: Successfully complete TDD cycle, all tests passing, coverage 88%.

**Bad Decision**: Skip dev notes creation. Claim "code is self-documenting". Modified 3 files outside plan scope (utils, config, middleware) without documentation. Made architecture deviation (used Redis instead of Memcached from architecture) without rationale.

**Why Bad**: Violates Constraint 2 (deviated from architecture without documented rationale). Violates Constraint 4 (modified out-of-scope files without documentation). Violates Quality-Gates (dev notes not complete). Makes code review and future maintenance impossible.

**Correct Approach**:
1. **Document Deviations**: If Redis used instead of Memcached → document in dev notes "Deviations from Plan" section with clear rationale and impact analysis
2. **Document Out-of-Scope Changes**: List all 3 modified files in dev notes with purposes and justifications
3. **Complete All Sections**: Follow dev-notes-tmpl.yaml completely (implementation summary, technical decisions, challenges, test coverage, etc.)
4. **Provide Evidence**: Include test results, coverage reports, performance metrics
