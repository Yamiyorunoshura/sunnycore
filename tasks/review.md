**GOAL**: Review task outcomes for quality compliance and requirements.

## [Context]
**You must read the following context:**
- `{DEVNOTES}/{task_id}-dev-notes.md`
- `{PLAN}/{task_id}-plan.md`
- `{ARCH}/*.md`(Only the related documents)
- `{TMPL}/review-tmpl.yaml`

## [Products]
- `{REVIEW}/{task_id}-review.md`
- Updated `{EPIC}`

## [Constraints]
- **MUST** verify architecture alignment, **MUST NOT** accept any architectural deviations (auto-reject)
- **MUST** scan production code for incomplete implementations, **MUST NOT** accept any mocks/stubs/hardcoded values (auto-reject, tests using mocks acceptable)
- **MUST** execute regression testing on all previous tasks, **MUST NOT** accept any test failures (auto-reject)
- **MUST** execute all current task tests and record results, **MUST NOT** skip test execution
- **MUST** make explicit acceptance decision (Accept/Accept with Changes/Reject), **MUST NOT** omit decision
- **MUST** follow review template structure (`{TMPL}/review-tmpl.yaml`), **MUST NOT** deviate from format
- **MUST** update Epic with accurate task status and score, **MUST NOT** provide incorrect data

## [Instructions]
**Core Review Principles**
- Enforce CRITICAL gates first: architecture alignment, production code completeness, and regression stability must pass before considering acceptance.
- Stop and document an auto-reject immediately when misalignment, mocks/stubs, hardcoded secrets, or regression failures are confirmed.
- Record evidence with precise file paths, line numbers, commands, timestamps, and outputs to support every conclusion.

**Context Consumption Strategy**
- Summarize each required document (plan, dev notes, architecture, template) and capture domain, requirements, and risk flags before deep inspection.
- Highlight discrepancies between plan and implementation early so later findings can reference them efficiently.
- Maintain a running list of questions or open items to resolve in subsequent steps.

**Testing Discipline**
- Execute regression suites before final scoring; note environment configuration, seed data, and reruns when applicable.
- Run current task tests and capture coverage metrics; investigate and document any failures or flaky behavior.
- Preserve raw command outputs for inclusion in the test summary section of the review report.

**Scoring and Decision Hygiene**
- Tie each score dimension directly to observed evidence, citing files, commits, or test results.
- Apply the decision matrix literally; document the specific clause that justifies Accept, Accept with Changes, or Reject.
- Assess risk using a combination of scores, findings severity, and coverage gaps, and prepare mitigation notes for high-risk areas.

**Reporting and Epic Updates**
- Populate `{REVIEW}/{task_id}-review.md` strictly following `{TMPL}/review-tmpl.yaml`; avoid adding or removing sections.
- Link findings, evidence, and test outputs to their respective sections so the report is self-contained.
- Update `{EPIC}` immediately after the decision, ensuring status, score, risk level, and required actions are synchronized with the review report.

1. **Step 1: Understand Context**
- **GOAL:** Establish domain, scope, and risk focus before validating deliverables.
- **STEPS:**
  - Collect `{PLAN}/{task_id}-plan.md`, `{DEVNOTES}/{task_id}-dev-notes.md`, relevant `{ARCH}/*.md`, and `{TMPL}/review-tmpl.yaml`.
  - Extract primary requirements, architectural touchpoints, and previously flagged risks.
  - Identify the task domain and note areas requiring deeper inspection later.
- **QUESTIONS:**
  - Which domain (Backend/Frontend/Database/Integration/Infrastructure) governs scoring?
  - What requirements or architectural commitments are mandatory for this task?
  - Where do plan or dev notes signal deviations or unfinished work?
- **CHECKLIST:**
  - [ ] All context documents reviewed and summarized.
  - [ ] Domain selection confirmed with rationale.
  - [ ] High-risk focus areas logged for follow-up.

2. **Step 2: Verify Architecture Alignment (CRITICAL)**
- **GOAL:** Ensure implementation fidelity to approved architecture before further evaluation.
- **STEPS:**
  - Map each implemented component to its defined architectural counterpart and responsibilities.
  - Inspect interfaces, data flows, and design patterns for required compliance.
  - Document any deviation with evidence and determine if automatic rejection applies.
- **QUESTIONS:**
  - Do implemented modules match the architecture-specified components and patterns?
  - Are interfaces, data contracts, and error paths consistent with architecture requirements?
  - Does any deviation mandate an immediate auto-reject decision?
- **CHECKLIST:**
  - [ ] Architecture requirements cross-referenced with implementation evidence.
  - [ ] No undocumented deviations remain unresolved.
  - [ ] Auto-reject determination recorded if misalignment exists.

3. **Step 3: Scan Production Code Quality (CRITICAL)**
- **GOAL:** Confirm production code is deployment-ready without mocks, stubs, or unsafe shortcuts.
- **STEPS:**
  - Identify production entry points and critical modules for inspection.
  - Search for mocks, stubs, placeholders, TODO/FIXME markers, and hardcoded secrets or configuration.
  - Verify environment-specific values are externalized and production logic is complete.
- **QUESTIONS:**
  - Does any production path contain mock, stub, or placeholder logic?
  - Are there hardcoded credentials, API keys, or environment-specific constants?
  - Are all TODO/FIXME markers resolved or justified with evidence?
- **CHECKLIST:**
  - [ ] Production code confirmed free of mocks, stubs, placeholders, and hardcoded values.
  - [ ] Blocking findings captured with file paths and severity.
  - [ ] Escalation path prepared if critical issue detected.

4. **Step 4: Execute Regression Testing (CRITICAL)**
- **GOAL:** Ensure legacy functionality remains intact after recent changes.
- **STEPS:**
  - Compile the regression suite covering previous tasks and relevant automation pipelines.
  - Execute regression tests with consistent environment configuration and data seeding.
  - Capture commands, outputs, and timing for evidence and follow-up analysis.
- **QUESTIONS:**
  - Which regression suites must run to cover prior functionality and integrations?
  - Did any regression test fail, and which functional area is impacted?
  - Are environment prerequisites satisfied to make results trustworthy?
- **CHECKLIST:**
  - [ ] Regression suite executed with reproducible command and timestamp noted.
  - [ ] Failures investigated and categorized with impact assessment.
  - [ ] Evidence stored for later inclusion in the report.

5. **Step 5: Test and Score Current Task**
- **GOAL:** Validate new functionality and translate findings into domain-aligned scores.
- **STEPS:**
  - Execute the current task's test suite and record status, coverage, and performance metrics.
  - Evaluate implementation against domain-specific scoring dimensions from the template.
  - Compute the average score and maturity level, ensuring rationale is traceable to evidence.
- **QUESTIONS:**
  - Which tests validate the new functionality, and do they all pass reliably?
  - How does the implementation perform against each selected scoring dimension?
  - Is coverage ≥ 80%, or are critical gaps documented for remediation?
- **CHECKLIST:**
  - [ ] Current task test results captured with command output and coverage figures.
  - [ ] Dimension scores assigned with short evidence-backed comments.
  - [ ] Overall score and maturity level calculated per template rules.

6. **Step 6: Make Decision and Assess Risk**
- **GOAL:** Apply decision matrix objectively and communicate residual risk.
- **STEPS:**
  - Apply decision rules (Accept / Accept with Changes / Reject) using scores and critical findings.
  - Evaluate risk level based on quality scores, testing outcomes, security posture, and alignment.
  - Draft acceptance rationale summarizing decisive evidence and gating results.
- **QUESTIONS:**
  - Does any auto-reject condition exist (architecture misalignment, mocks, regression failures)?
  - Which findings materially influence acceptance or risk level?
  - Is the assigned risk level justified by documented evidence and mitigation plans?
- **CHECKLIST:**
  - [ ] Acceptance decision recorded with explicit rationale references.
  - [ ] Risk level assigned with supporting factors and mitigation notes.
  - [ ] Follow-up actions captured for inclusion in recommendations.

7. **Step 7: Generate Report and Update Epic**
- **GOAL:** Deliver final documentation and synchronize project tracking artifacts.
- **STEPS:**
  - Populate `{REVIEW}/{task_id}-review.md` using `{TMPL}/review-tmpl.yaml` without altering structure.
  - Embed evidence snippets, test outputs, scores, and findings into their designated sections.
  - Update `{EPIC}` with decision, score, risk status, and required actions.
- **QUESTIONS:**
  - Does the review report follow the template exactly, including all required sections?
  - Are findings, tests, and decisions linked to evidence and file paths?
  - Has `{EPIC}` been updated to reflect the final decision and next steps?
- **CHECKLIST:**
- [ ] Review report completed and saved in the correct location with all sections filled.
- [ ] Epic updated with status, score, and action items.
- [ ] Supporting artifacts referenced and accessible for audit.

8. **Step 8: Validation**
- **GOAL:** Ensure all quality gates are satisfied before marking the task complete.
- **STEPS:**
  - Review each quality gate checklist item to confirm compliance.
  - Address any outstanding issues or gaps before finalizing the review.
  - Start the task again to fulfil the quality gates if any item is unmet.
- **QUESTIONS:**
  - Have all critical quality gates been satisfied without exceptions?
  - Are there any unresolved issues that could impact the final decision?
  - Is the review report and Epic update fully aligned with the quality gate outcomes?
- **CHECKLIST:**
  - [ ] All quality gates reviewed and confirmed as passed.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Implementation verified to align with architecture (components, patterns, data flow, interfaces)
- [ ] **CRITICAL**: Production code scanned, NO mocks/stubs/hardcoded values found (tests using mocks OK)
- [ ] **CRITICAL**: Regression tests executed, NO previous functionality broken
- [ ] All tests executed with results recorded and scored
- [ ] Review report exists at `{REVIEW}/{task_id}-review.md` with decision
- [ ] `{EPIC}` updated with status and score