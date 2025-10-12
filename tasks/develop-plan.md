**GOAL**: Execute TDD development based on implementation plan, completing single task implementation.

## [Input]
  1. "{PLAN}/{task_id}-plan.md" --Implementation plan
  2. "{ARCH}/*.md" --Architecture design
  3. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template

## [Output]
  1. "{DEVNOTES}/{task_id}-dev-notes.md" --Complete development notes document (Markdown format)
  2. High-quality, tested, refactored code implementation highly allign with the implementation plans
  3. Complete test coverage and test cases allign with the implementation plans
  4. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not deviate from implementation plan's acceptance criteria and architecture mapping
  2. Do not skip TDD cycle (RED → GREEN → REFACTOR)
  3. Do not modify files outside plan scope without recording rationale in dev notes
  4. Do not deliver with failing tests (exit code must be 0)
  5. Follow the Development-Guidelines defined in sunnycore_dev

## [Blocking-Conditions]
  - missing critical inputs
  - unexpected RED failures
  - risky irreversible actions needing approval
  - tools lacking non-interactive flags
  
## [Steps]
  1. Preparation & Planning
    - Understand TDD implementation plan and three phases
    - Create plan.md at "{root}/docs/plan.md" for progress tracking (this is the ONLY temporary tracking document)
    - Outcome: Implementation plan understood and plan.md initialized

  2. RED Phase: Test Implementation
    - Implement complete test coverage with all planned test cases
    - Execute tests and verify they fail with expected errors (confirm RED status)
    - Update plan.md with RED phase progress (test cases implemented, RED status verified)
    - Note: Do NOT create separate test result documents; record status in plan.md only
    - Outcome: All tests implemented and failing correctly, status recorded in plan.md

  3. GREEN Phase: Minimal Implementation
    - Implement minimal code to pass all tests
    - Align implementation with architecture mapping from plan
    - Execute tests and verify all pass (exit code 0)
    - Update plan.md with GREEN phase progress (implementation files, test results)
    - Note: Do NOT create separate test result documents; record status in plan.md only
    - Outcome: All tests passing with minimal implementation, status recorded in plan.md

  4. REFACTOR Phase: Code Quality Enhancement
    - Improve code quality while maintaining green tests
    - Apply all planned optimizations and cross-cutting concerns
    - Execute tests after each refactoring to ensure they remain green
    - Update plan.md with REFACTOR phase progress (refactoring activities, test status)
    - Note: Do NOT create separate test result documents; record status in plan.md only
    - Outcome: High-quality code with all tests still passing, status recorded in plan.md

  5. Validation & Documentation
    - Validate all acceptance criteria are met
    - Check if "{DEVNOTES}/{task_id}-dev-notes.md" already exists
    - If exists: Update existing dev notes with new implementation details
    - If not exists: Create new dev notes from template following dev-notes-tmpl.yaml
    - Note: dev-notes.md is the ONLY permanent documentation output; plan.md is temporary
    - Outcome: Acceptance criteria met and dev notes completed (created or updated)

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Task identification (task ID and description from implementation plan)
  - Implementation plan summary (requirements, architecture mapping, acceptance criteria)
  - RED phase progress:
    * Test cases implemented (list with test names)
    * Test types (unit/integration/behaviour) with count
    * RED status verification (tests failing as expected: yes/no)
    * Test coverage planned vs achieved
  - GREEN phase progress:
    * Implementation files created/modified (list with file paths)
    * Architecture components implemented (list)
    * Test execution results (all passing: yes/no, failure details if any)
    * Minimal implementation verified (yes/no)
  - REFACTOR phase progress:
    * Refactoring activities performed (list)
    * Code quality improvements (patterns applied, DRY, SOLID)
    * Cross-cutting concerns integrated (logging, error handling, etc.)
    * Test status maintained (all still passing: yes/no)
  - Acceptance criteria validation (each criterion with met/not met status)
  - Code quality metrics (test coverage %, function length compliance, etc.)
  - Development notes status (created/updated at {DEVNOTES}/{task_id}-dev-notes.md)

## [DoD]
  - [ ] All acceptance criteria satisfied through full TDD cycle (RED → GREEN → REFACTOR) with all tests passing
  - [ ] Code quality meets standards (SOLID, DRY, functions ≤50 lines, coverage ≥80%)
  - [ ] Complete development notes document exists at "{DEVNOTES}/{task_id}-dev-notes.md"

## [Example]

### Good Example 1
[INPUT]
Plan: docs/plans/1-plan.md for article publishing. Architecture: Article Service (Express), PostgreSQL. Template: dev-notes-tmpl.yaml.

[DECISION]
Step 1: Read plan - RED: unit tests (model validation), integration tests (API+DB), behavior tests (workflow). GREEN: minimal implementation. REFACTOR: patterns. Step 2 RED: Write all test files, execute - all fail correctly (RED status verified). Update plan.md with RED progress. Step 3 GREEN: Implement minimal code (Article model, POST/GET/PUT endpoints), execute tests - all pass (exit code 0). Update plan.md with GREEN progress. Step 4 REFACTOR: Add validation, error handling, repository pattern. Execute tests - remain green. Update plan.md with REFACTOR progress. Step 5: Check docs/dev-notes/1-dev-notes.md exists - YES. Update existing dev notes with implementation details. All acceptance criteria met.

[OUTCOME]
Complete TDD cycle executed. Code at src/services/ArticleService.js, tests/ with all passing. Updated docs/dev-notes/1-dev-notes.md documents implementation. Coverage 85%. All acceptance criteria satisfied. plan.md tracked progress throughout.

### Good Example 2
[INPUT]
Plan: docs/plans/2-plan.md for transaction reports. NFR: query <2s. Architecture: Reporting Service, TimescaleDB.

[DECISION]
Step 1: Read plan completely. Step 2 RED: Write unit tests (aggregation), integration tests (TimescaleDB with real DB, performance <2s), behavior tests (report generation). Execute - all fail (RED verified). Record in plan.md. Step 3 GREEN: Implement minimal query with indexed date column, aggregation. Execute tests - all pass including performance <2s. Record in plan.md. Step 4 REFACTOR: Add Redis caching, optimize queries. Tests remain green. Record in plan.md. Step 5: docs/dev-notes/2-dev-notes.md doesn't exist - create new from template. Document all phases, test results, performance metrics.

[OUTCOME]
All tests passing, performance validated 120ms (<2s requirement). New docs/dev-notes/2-plan.md created with complete documentation. Code quality high. plan.md shows full progression through TDD phases.

### Bad Example 1
[INPUT]
Plan exists for task. Need to implement.

[BAD-DECISION]
Skip RED phase entirely - start coding without tests. Write implementation with optimizations immediately (not minimal). Skip test execution. Don't track progress in plan.md. Skip REFACTOR phase. No dev notes documentation. Claim task complete.

[WHY-BAD]
Violates Constraint 2 (skip TDD cycle). No RED phase means no test-first approach. Skipping tests violates DoD (all tests must pass). No progress tracking violates plan.md requirement. No dev notes violates DoD. Implementation unverified.

[CORRECT-APPROACH]
Follow TDD cycle strictly per Steps. Step 2: Write ALL tests from plan (unit, integration, behavior), execute to verify RED status. Step 3: Implement MINIMAL code only, execute tests to achieve GREEN. Step 4: Apply quality improvements in REFACTOR while maintaining green. Track ALL progress in plan.md (RED status, GREEN status, REFACTOR status). Step 5: Create or update dev notes with complete documentation.

### Bad Example 2
[INPUT]
Task implementation required. Plan specifies acceptance criteria.

[BAD-DECISION]
Deliver code with failing tests (exit code non-zero). Modify files outside plan scope without recording rationale. Skip dev notes update claiming "code is self-documenting". Create separate files like red-phase-test-result.md, green-phase-result.md instead of using plan.md.

[WHY-BAD]
Violates Constraint 4 (deliver with failing tests - DoD violation). Constraint 3 requires recording rationale for out-of-scope changes. "Self-documenting code" violates DoD (dev notes required). Creating separate phase result files violates Step instructions (use plan.md ONLY for tracking). Creates document clutter.

[CORRECT-APPROACH]
Ensure ALL tests pass (exit code 0) before declaring complete per Constraint 4 and DoD. If modifying files outside plan scope, document rationale in dev notes per Constraint 3. Always create/update dev notes - never skip documentation. Use plan.md as THE ONLY temporary tracking document - record all RED/GREEN/REFACTOR status, test results, progress in plan.md. Do NOT create separate result files. Dev notes are permanent, plan.md is temporary.

