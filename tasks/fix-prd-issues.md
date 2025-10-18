**GOAL**: Fix issues identified during PRD acceptance phase.

## [Context]
**You must read the following context:**
- `{CUTOVER}` (required) - Contains issues to fix
- `{PRD}` (required) - Provides requirements and architecture context  
- `{TMPL}/dev-notes-tmpl.yaml` (required) - Output documentation structure

## [Products]
- `{root}/docs/cutover-fixes-dev-notes.md`
- Fixed code
- Updated documentation if needed

## [Constraints]
- **MUST** address all cutover issues, **MUST NOT** leave any unaddressed
- **MUST** follow TDD cycle for fixes (RED→GREEN→REFACTOR), **MUST NOT** skip
- **MUST** re-run acceptance tests after fixes, **MUST NOT** skip
- **MUST** not introduce new issues or break existing functionality, **MUST NOT** cause regressions

## [Instructions]
1. **Step 1: Analyze Issues**
- **GOAL:** Build a prioritized inventory of cutover issues mapped to PRD expectations.
- **STEPS:**
  - Pull every issue, severity, and scenario from `{CUTOVER}`.
  - Cross-reference each issue with affected PRD requirements or acceptance criteria.
  - Order the backlog Critical → High → Medium → Low and note dependencies.
- **QUESTIONS:**
  - Which issues block PRD acceptance immediately?
  - Which PRD requirement or REQ ID does each issue violate?
  - Are there setup or configuration notes that impact reproduction?
- **CHECKLIST:**
  - [ ] Complete issue list with severities captured
  - [ ] PRD references linked for every issue
  - [ ] Prioritized backlog agreed before diagnosis begins

2. **Step 2: Root Cause Analysis**
- **GOAL:** Identify the underlying cause and impact pathway for every issue.
- **STEPS:**
  - Review PRD architecture and requirement details describing expected behavior.
  - Inspect current implementation/configuration to locate deviations from expectations.
  - Capture business impact, technical root cause, and architecture alignment notes per issue.
- **QUESTIONS:**
  - What mismatch between implementation and PRD acceptance criteria triggered the defect?
  - Are missing configurations, patterns, or error handling contributing to the failure?
  - Do multiple issues stem from a shared root cause?
- **CHECKLIST:**
  - [ ] Root cause trio (business, technical, architecture) documented per issue
  - [ ] Impacted components/files identified for each root cause
  - [ ] Shared causes or dependencies highlighted for planning

3. **Step 3: Plan Fixes**
- **GOAL:** Define TDD-aligned fix strategies that respect PRD architecture.
- **STEPS:**
  - Specify the failing test scenario that will expose each issue in the RED phase.
  - Outline minimal code and configuration changes while adhering to architecture patterns.
  - Assess sequencing, risks, and documentation updates needed (dev notes, cutover evidence).
- **QUESTIONS:**
  - Which tests will clearly reproduce the defect during RED?
  - What architectural constraints or integrations must the fix honor?
  - Are there high-risk dependencies that require isolation or mocks?
- **CHECKLIST:**
  - [ ] Fix plan covers every issue with a mapped TDD approach
  - [ ] Risks and sequencing agreed before coding starts
  - [ ] Required documentation touchpoints captured

4. **Step 4: RED Phase**
- **GOAL:** Reproduce each issue with failing automated tests.
- **STEPS:**
  - Implement tests based on PRD Given-When-Then scenarios or cutover evidence.
  - Execute tests to confirm failure for the expected reason and capture outputs/logs.
  - Preserve failure evidence for traceability (commit metadata or notes).
- **QUESTIONS:**
  - Does each new test map directly to a PRD acceptance criterion?
  - Are failures triggered for the precise symptom observed in cutover?
  - Do environment/setup prerequisites need adjustment to reproduce?
- **CHECKLIST:**
  - [ ] New tests fail prior to any fix changes
  - [ ] Failure evidence recorded with context
  - [ ] Coverage includes every prioritized issue path

5. **Step 5: GREEN Phase**
- **GOAL:** Deliver minimal fixes that make RED tests pass without regressions.
- **STEPS:**
  - Apply targeted code/config changes that align with PRD architecture decisions.
  - Re-run focused and related tests until all new failures turn green.
  - Run quick regression checks on affected modules or smoke suites.
- **QUESTIONS:**
  - What is the smallest change that satisfies the failing test?
  - Does the implementation stay consistent with patterns and constraints documented in PRD?
  - Did the change impact adjacent functionality or integrations?
- **CHECKLIST:**
  - [ ] All newly added tests pass
  - [ ] No lint/type/static analysis regressions introduced
  - [ ] Targeted regression checks remain green

6. **Step 6: REFACTOR Phase**
- **GOAL:** Harden the solution and validate quality while keeping tests green.
- **STEPS:**
  - Refine code readability, structure, and adherence to architecture guidelines.
  - Enhance observability, error handling, and non-functional requirements per PRD.
  - Run full acceptance and automated test suites to confirm stability.
- **QUESTIONS:**
  - Which refactors improve maintainability without altering behavior?
  - Are logging/metrics/traces sufficient for ongoing monitoring?
  - Do acceptance tests confirm PRD compliance end-to-end?
- **CHECKLIST:**
  - [ ] Refactoring completed with all tests passing
  - [ ] Observability and NFR expectations satisfied
  - [ ] Full test suite (including acceptance) passes without regressions

7. **Step 7: Document Results**
- **GOAL:** Capture outcomes, evidence, and follow-ups for stakeholders.
- **STEPS:**
  - Update `{root}/docs/cutover-fixes-dev-notes.md` using `{TMPL}/dev-notes-tmpl.yaml`, focusing on Brownfield fix details.
  - Summarize implemented fixes, verification evidence, and any deviations or debt.
  - Confirm quality gates and track remaining actions or follow-ups.
- **QUESTIONS:**
  - Does documentation link each fix to its issue and PRD requirement?
  - Are TDD cycle results, test outputs, and acceptance reruns recorded?
  - What technical debt or outstanding risks require future attention?
- **CHECKLIST:**
  - [ ] Dev notes updated with Brownfield fix details completed
  - [ ] Quality gates marked complete with supporting evidence
  - [ ] Outstanding issues or debt logged with next steps

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All issues resolved through full TDD cycle with all tests passing
- [ ] Acceptance tests re-executed with all issues resolved  
- [ ] Complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Examples]

### Good Approach
**Scenario**: Cutover shows critical push notification failure. PRD REQ-002 specifies notification delivery requirements.

**Approach**: Extract issue details and severity. Map to PRD REQ-002 requirements. Root cause: missing FCM configuration. Plan fix strategy following PRD architecture. RED: write failing test based on PRD acceptance criteria. GREEN: implement minimal FCM service. REFACTOR: add error handling per PRD standards. Re-run acceptance tests. Document comprehensive fix in dev notes.

**Why Good**: Follows TDD methodology, anchors fixes in PRD context, validates through acceptance testing.

### Poor Approach  
**Scenario**: Same notification failure.

**Poor Approach**: Implement notification service directly without tests. Add configuration and test manually. Mark as fixed without systematic validation or comprehensive documentation.

**Why Poor**: Skips TDD cycle, lacks systematic testing, provides no regression protection, insufficient documentation.
