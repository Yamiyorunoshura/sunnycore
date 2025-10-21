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

## [Instructions]
1. **Step 1: Assimilate Plan And Architecture**
  - **GOAL:** Build an executable understanding of requirements, tests, architecture, and quality gates.
  - **STEPS:**
    - Read the implementation plan to capture traceability chains, test cases, and phase sequencing.
    - Review relevant architecture documents for tech stack, component contracts, directory structure, and ADR constraints.
    - Map plan elements to architecture components, highlighting dependencies and target files.
  - **QUESTIONS:**
    - Do I understand how every requirement maps to tests and components?
    - Are any technologies, directories, or interfaces unspecified or conflicting?
    - What assumptions require confirmation before coding?
  - **CHECKLIST:**
    - [ ] All tests and requirements traced to concrete components and files
    - [ ] Architecture decisions and versions noted for implementation
    - [ ] Gaps or conflicts recorded and escalated before continuing

2. **Step 2: RED Phase — Author Failing Tests**
  - **GOAL:** Implement the complete test suite that expresses the plan’s acceptance criteria and currently fails for the right reasons.
  - **STEPS:**
    - Enumerate and scaffold test files per plan (unit, integration, behavior, performance).
    - Implement test cases with approved frameworks, covering happy path, edge, and error scenarios.
    - Run targeted and full suites to verify failures align with missing implementation, capturing failure output.
  - **QUESTIONS:**
    - Do the tests fully express each acceptance criterion and NFR?
    - Are fixtures, mocks, and data consistent with architecture expectations?
    - Do failure messages confirm missing implementation rather than setup errors?
  - **CHECKLIST:**
    - [ ] Every planned test case implemented in the correct location
    - [ ] Test run produces expected failures with informative errors
    - [ ] No production code added beyond scaffolding required for tests

3. **Step 3: GREEN Phase — Minimal Passing Implementation**
   - **GOAL:** Write the smallest amount of production code needed to turn the RED suite green while honoring architecture boundaries.
   - **STEPS:**
     - Implement features in the order prescribed by the plan, adhering to component responsibilities and interfaces.
     - Integrate required dependencies, configurations, and data layers as defined in architecture documents and ADRs.
     - Re-run the full suite until all tests pass with exit code 0 and coverage goals met.
   - **QUESTIONS:**
     - Does each code change directly correspond to a failing test?
     - Am I respecting directory structure, interfaces, and technology versions?
     - Are side effects (data, I/O, external calls) handled per plan and architecture?
   - **CHECKLIST:**
     - [ ] All RED tests now pass without relaxing assertions
     - [ ] Implementation stays within authorized files and components
     - [ ] Coverage report meets or exceeds required threshold

4. **Step 4: REFACTOR Phase — Quality And Compliance**
   - **GOAL:** Improve design, clarity, and non-functional qualities while keeping the suite green.
   - **STEPS:**
     - Inspect code for duplication, architecture rule violations, and technical debt identified in the plan.
     - Apply refactorings (SOLID, DRY, performance, observability) prioritized by the plan and ADR guidance.
     - After each change, run the full suite to ensure behavior remains correct and coverage holds.
   - **QUESTIONS:**
     - Which refactorings deliver the highest quality or risk reduction first?
     - Does each change maintain architectural boundaries and contracts?
     - Are logs, metrics, or error handling required by ADRs now present?
   - **CHECKLIST:**
     - [ ] Refactoring priorities from plan addressed in documented order
     - [ ] Tests remain green after every change, with coverage stable
     - [ ] Architecture and quality standards (performance, observability, security) satisfied

5. **Step 5: Document Outcomes**
  - **GOAL:** Capture implementation evidence and decisions using the development notes template.
  - **STEPS:**
    - Populate `{DEVNOTES}/{task_id}-dev-notes.md` following `{TMPL}/dev-notes-tmpl.yaml`.
    - Record traceability, technical decisions, deviations, challenges, test evidence, and metrics as required.
    - Attach supporting artifacts (test logs, coverage reports, performance data) referenced in the notes.
  - **QUESTIONS:**
    - Does the documentation prove requirements and NFRs were delivered?
    - Are all deviations, mitigations, and risks clearly justified?
    - Would a reviewer understand the implementation without more context?
  - **CHECKLIST:**
    - [ ] Dev notes complete with required sections and evidence
    - [ ] All deviations and outstanding risks documented
    - [ ] Final test results and coverage metrics captured

## [Blocking Conditions]
If any required document is missing, inconsistent, or lacks critical details (tech stack, components, tests), stop and request guidance instead of inventing information.

## [Quality Gates]
- [ ] Full automated test suite passes (exit code 0)
- [ ] Coverage ≥80% with no skipped tests
- [ ] Implementation aligns with plan traceability and architecture directives
- [ ] Dev notes submitted and linked to the plan

## [Examples]

### Good example 1: Get related documents before development
- **Context:** An implementation plan requires external API integration.
- **Tools:** There is a tool called `context7` that can fetch documents related to the code (e.g., documentation for Redis, PostgreSQL, etc.).
- **Decision:** Use `context7` to get all related documents before starting the fix to understand the latest code formats.
- **Outcome:** The development was done correctly the first time, and all tests passed.
- **Why good:** By getting all related documents first, the LLM was able to understand the latest code formats and avoid mistakes caused by outdated knowledge.

### Bad example 1: Start development without understanding the problem
- **Context:** An implementation plan requires complex interactions between multiple services.
- **Tools:** There is a tool called `sequential thinking` that can help an LLM break down complex problems into smaller steps via reasoning.
- **Decision:** Start development directly without using `sequential thinking` to analyze.
- **Outcome:** The development was incorrect and is not aligned to the plan.
- **Why bad:** Without using `sequential thinking`, the LLM failed to gain a comprehensive understanding of the problem, which led to mistakes during the development.