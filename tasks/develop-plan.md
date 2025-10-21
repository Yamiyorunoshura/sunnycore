**Purpose**: Implement the atomic-level tasks stated in the implementation plan to deliver working code with comprehensive test coverage.

## [Context]
- `{PLAN}/{task_id}-plan.md` - Implementation plan with traceability chains, test cases, and implementation steps
- `{TMPL}/dev-notes-tmpl.yaml` - Template for documenting implementation outcomes

## [Products]
- Working code implementation (all tests passing, exit code 0)
- Comprehensive test suite (unit, integration, behavior, and performance tests where applicable)
- `{DEVNOTES}/{task_id}-dev-notes.md` following the template structure

## [Constraints]
- **MUST** adhere strictly to the implementation plan and architecture design.

## [CRITICAL: Blocking Conditions]
If any required document is missing, inconsistent, or lacks critical details (e.g., tech stack, components, tests), stop and request guidance instead of inventing information.

## [Instructions]
1. **Step 1: Prepare for development**
- **GOAL:** Build a comprehensive understanding of the task and create a trustworthy plan.
- **STEPS:**
  - Read `{PLAN}/{task_id}-plan.md` thoroughly to get the task context.
  - Identify all atomic-level tasks in the implementation plan.
  - Trace the tasks with trustworthy mechanisms (e.g., create a to-do list using tools) to avoid missing any of them.
- **QUESTIONS:**
  - Do you understand the key requirements stated in the implementation plan?
  - Have you identified all the atomic-level tasks in the implementation plan?
  - Have you understood all the risks stated in the implementation plan and figured out how to mitigate them?
- **CHECKLIST:**
  - [ ] All atomic-level tasks identified and traced
  - [ ] Key requirements, architecture design, and risks understood
  - [ ] Have an approach to mitigate potential risks

2. **Step 2: Develop atomic-level tasks**
- **GOAL:** Generate production-level code for each atomic-level task
- **STEPS:**
  - Follow the implementation steps to develop each atomic-level task.
  - Validate whether the code meets the implementation plan after developing each atomic-level task.
- **QUESTIONS:**
  - Does the code meet the requirements and architecture design?
  - Has any external integration been successfully implemented (e.g., API integration)?
  - Are all the atomic-level tasks implemented?
- **CHECKLIST:**
  - [ ] All atomic-level tasks implemented
  - [ ] Code meets requirements and architecture design
  - [ ] External integrations successfully implemented

3. **Step 3: Document outcomes**
- **GOAL:** Capture implementation evidence and decisions using the development notes template.
- **STEPS:**
  - Populate `{DEVNOTES}/{task_id}-dev-notes.md` following `{TMPL}/dev-notes-tmpl.yaml`.
  - Record traceability, technical decisions, deviations, challenges, test evidence, and metrics as required.
  - Attach supporting artifacts (test logs, coverage reports, performance data) referenced in the notes.
- **QUESTIONS:**
  - Does the documentation demonstrate that requirements and NFRs were delivered?
  - Are all deviations, mitigations, and risks clearly justified?
  - Would a reviewer understand the implementation without additional context?
- **CHECKLIST:**
  - [ ] Dev notes completed with required sections and evidence
  - [ ] All deviations and outstanding risks documented
  - [ ] Final test results and coverage metrics captured

4. **Step 4: Validation**
- **GOAL:** Ensure the implementation meets all quality gates and is ready for review.
- **STEPS:**
  - Understand the quality gates and ensure all of them are met.
  - If any are not met, restart the relevant tasks to satisfy the quality gates.
- **QUESTIONS:**
  - Have you validated that all quality gates are met?
  - Are there any outstanding issues that need to be addressed before submission?
- **CHECKLIST:**
  - [ ] All quality gates met

## [Quality-Gates]
- [ ] Full automated test suite passes (exit code 0)
- [ ] Coverage ≥ 80% with no skipped tests
- [ ] Implementation aligns with plan traceability and architecture directives
- [ ] Dev notes submitted and linked to the plan

## [Examples]

### Good example 1: Retrieve related documents before development
- **Context:** An implementation plan requires external API integration.
- **Tools:** There is a tool called `context7` that can fetch documents related to the code (e.g., documentation for Redis, PostgreSQL, etc.).
- **Decision:** Use `context7` to get all related documents before starting the fix to understand the latest code formats.
- **Outcome:** The development was done correctly the first time, and all tests passed.
- **Why good:** By getting all related documents first, the LLM was able to understand the latest code formats and avoid mistakes caused by outdated knowledge.

### Bad example 1: Start development without understanding the problem
- **Context:** An implementation plan requires complex interactions between multiple services.
- **Tools:** There is a tool called `sequential thinking` that can help an LLM break down complex problems into smaller steps via reasoning.
- **Decision:** Start development directly without using `sequential thinking` to analyze.
- **Outcome:** The development was incorrect and not aligned with the plan.
- **Why bad:** Without using `sequential thinking`, the LLM failed to gain a comprehensive understanding of the problem, which led to mistakes during development.