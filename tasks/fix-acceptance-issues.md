**GOAL**: Fix issues identified during acceptance phase by systematically addressing root causes through TDD and comprehensive testing.

## [Context]
**Read these context documents to understand issues and system design:**
- `{CUTOVER}` - Contains all issues found during acceptance testing with severity levels
- `{REQ}/*.md`(Only the related documents) - Shows what functionality was intended and acceptance criteria
- `{ARCH}/*.md`(Only the related documents) - Reveals system design, components, and technical decisions
- `{TMPL}/dev-notes-tmpl.yaml` - Provides structure for documentation output

## [Products]
- `{root}/docs/cutover-fixes-dev-notes.md` (comprehensive fix documentation)
- Fixed code addressing all issues
- Updated documentation if architectural changes made

## [Constraints]
- **MUST** address all cutover issues systematically, **MUST NOT** leave any unresolved
- **MUST** follow complete TDD cycle (RED→GREEN→REFACTOR) for each fix
- **MUST** re-run full acceptance tests to verify resolution
- **MUST** maintain existing functionality without introducing regressions

## [Instructions]
1. **Step 1: Triage Acceptance Issues**
- **GOAL:** Establish a severity-ranked backlog of all acceptance findings with traceable references.
- **STEPS:**
  - Extract every issue from `{CUTOVER}` and capture severity, symptoms, and impacted capabilities.
  - Link each issue to the relevant `{REQ}` and `{ARCH}` documents to understand intended behavior and design.
  - Highlight Critical and High issues that block release and clarify desired resolution order.
- **QUESTIONS:**
  - Which issues block go-live if left unresolved?
  - What requirement IDs and architectural components are tied to each issue?
  - Are there dependencies between issues that change prioritization?
- **CHECKLIST:**
  - [ ] Severity-sorted issue list recorded with unique identifiers
  - [ ] Source documents mapped for every issue
  - [ ] Blocker status confirmed with stakeholders

2. **Step 2: Diagnose Root Causes**
- **GOAL:** Understand failure mechanisms so fixes target the underlying defect, not just symptoms.
- **STEPS:**
  - Inspect logs, test evidence, and code paths associated with each issue to trace causation.
  - Compare observed behavior against requirements and architecture intent to pinpoint gaps or regressions.
  - Document hypothesized root causes and validation approach for each issue before coding.
- **QUESTIONS:**
  - Why did the system diverge from the requirement or design?
  - What signals or data confirm the suspected root cause?
  - Do multiple issues share a common underlying defect?
- **CHECKLIST:**
  - [ ] Root cause written for every issue with supporting evidence
  - [ ] Impacted code paths and components identified
  - [ ] Validation approach defined to confirm diagnosis

3. **Step 3: Design Fix Strategy**
- **GOAL:** Plan targeted, low-risk fixes with clear test coverage and sequencing.
- **STEPS:**
  - Determine the minimal code or configuration changes required per issue.
  - Define the tests needed (unit, integration, acceptance) to expose and verify each fix.
  - Sequence fixes to address blockers first while minimizing merge or dependency conflicts.
- **QUESTIONS:**
  - What is the leanest change that resolves the root cause?
  - Which tests must exist before implementation begins?
  - How do fixes interact across shared modules or deployments?
- **CHECKLIST:**
  - [ ] Fix plan captured with owners, scope, and risk notes
  - [ ] Test coverage strategy agreed for each issue
  - [ ] Execution order aligned with severity and dependencies

4. **Step 4: Run TDD Fix Cycle**
- **GOAL:** Implement each fix through disciplined RED→GREEN→REFACTOR loops.
- **STEPS:**
  - Write a failing test that reproduces the acceptance issue or missing capability.
  - Implement the minimal code change to make the new and existing tests pass.
  - Refactor for readability, resilience, and reuse while keeping the test suite green.
- **QUESTIONS:**
  - Does the new test fail for the expected reason before the fix?
  - Have all related tests (new and existing) passed after the change?
  - Can the implementation be simplified without reintroducing the defect?
- **CHECKLIST:**
  - [ ] Failing test created and observed for each issue
  - [ ] Fix committed with full test suite passing locally
  - [ ] Refactoring completed without breaking coverage

5. **Step 5: Validate System Quality**
- **GOAL:** Confirm fixes hold under full regression and acceptance conditions.
- **STEPS:**
  - Re-run the targeted regression suites plus any impacted smoke or integration tests.
  - Execute the original acceptance tests from `{CUTOVER}` to verify issues are fully resolved.
  - Monitor for collateral regressions and capture evidence of successful runs.
- **QUESTIONS:**
  - Do acceptance scenarios now pass end-to-end?
  - Did any new failures surface during regression?
  - Is there objective evidence (logs, reports) proving resolution?
- **CHECKLIST:**
  - [ ] Regression and acceptance test results archived with timestamps
  - [ ] All original issues confirmed resolved with proof
  - [ ] New or reopened issues documented if discovered

6. **Step 6: Capture Resolution Notes**
- **GOAL:** Record decisions, fixes, and verification outcomes for future reference.
- **STEPS:**
  - Update `{root}/docs/cutover-fixes-dev-notes.md` following `{TMPL}/dev-notes-tmpl.yaml` structure.
  - Summarize root causes, applied fixes, test evidence, and follow-up work per issue.
  - Share outcomes with stakeholders and align on readiness for re-run or release.
- **QUESTIONS:**
  - What lessons or patterns should inform future acceptance cycles?
  - Are any follow-up tasks required beyond the immediate fixes?
  - Who needs to sign off on the documented resolution?
- **CHECKLIST:**
  - [ ] Dev notes completed and stored in the designated location
  - [ ] Stakeholders notified with resolution summary
  - [ ] Outstanding follow-ups tracked in backlog or runbook

## [Quality-Gates]
**All gates must pass before completion:**
- [ ] All cutover issues systematically resolved through complete TDD cycle
- [ ] Full test suite passing (no regressions introduced)
- [ ] Acceptance tests re-executed with all original issues confirmed resolved
- [ ] Comprehensive development notes created following template structure