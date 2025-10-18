**GOAL**: Fix review-rejected work so it meets quality, observability, and operational-readiness standards.

## [Context Sources]
Read in this order:
- `{TMPL}/dev-notes-tmpl.yaml` - Documentation structure to follow.
- `{DEVNOTES}/{task_id}-dev-notes.md` - Original implementation details and decisions.
- `{REVIEW}/{task_id}-review.md` - Rejection reasons, failing tests, evidence.
- `{ARCH}/*.md` - Relevant architecture specifications, ADRs, and cross-cutting concerns.
- `{KNOWLEDGE}/*.md` - Approved reference implementations and patterns (if present).

## [Input Validation]
- You **MUST** confirm required inputs exist before progressing.
- **IF** `{REVIEW}/{task_id}-review.md` is missing: RETURN `Cannot proceed without review report at {REVIEW}/{task_id}-review.md`
- **IF** `{DEVNOTES}/{task_id}-dev-notes.md` is missing: RETURN `Cannot proceed without development notes at {DEVNOTES}/{task_id}-dev-notes.md`
- **IF** `{ARCH}/*.md` is missing: RETURN `Cannot proceed without architecture specifications at {ARCH}/`
- **MUST NOT** guess or invent specifications when any source is unavailable.

## [Deliverables]
- Fixed code with all quality gates satisfied.
- Root-cause Traceability Table (per `{TMPL}/dev-notes-tmpl.yaml`).
- Change Diff Summary for every fix.
- Updated `{DEVNOTES}/{task_id}-dev-notes.md` (Brownfield Fix Details + observability, testing, ops notes).
- Migration and rollback scripts, when changes touch schema or contracts.

## [Constraints]
- **MUST** ship fixes that keep the full test suite green; **MUST NOT** deliver partial or broken code.
- **MUST** follow architecture specifications and ADRs; **MUST NOT** diverge from approved designs.
- **MUST** preserve existing functionality and backward compatibility for public APIs/events.
- **MUST** rely only on repository code or `{KNOWLEDGE}` assets; external unvetted code is disallowed.
- **MUST** stay within performance budget (p95 latency ≤ +10%, p99 latency ≤ +20%).
- **MUST NOT** create new dev notes files—update the existing `{DEVNOTES}/{task_id}-dev-notes.md` only.

[Instructions]
1. **Step 1: Validate Inputs**
- **GOAL:** Ensure every mandatory source file exists before any remediation work starts.
- **STEPS:**
  - Confirm `{REVIEW}/{task_id}-review.md`, `{DEVNOTES}/{task_id}-dev-notes.md`, and required `{ARCH}/*.md` assets are present.
  - If any required file is missing, stop immediately and return the mandated message word-for-word.
  - Record the validation outcome for later inclusion in dev notes.
  - Check that architecture coverage exists for every component cited in the review findings.
- **QUESTIONS:**
  - Have I positively verified each required path on disk?
  - If something is missing, did I respond with the exact required message?
  - Do I have architecture coverage for every component touched by the review findings?
- **CHECKLIST:**
- [ ] `{REVIEW}/{task_id}-review.md` confirmed or task aborted with required message.
- [ ] `{DEVNOTES}/{task_id}-dev-notes.md` located for later updates.
- [ ] Relevant `{ARCH}/*.md` files gathered for each issue.
- [ ] No assumptions made about absent specifications.

2. **Step 2: Understand Context**
- **GOAL:** Reconstruct original intent, rejection reasons, and architecture expectations.
- **STEPS:**
  - Read the dev notes (Implementation Summary, Implementation Details, Technical Decisions, Testing) to capture delivered behavior.
  - Review the rejection report (Acceptance Decision, Detailed Findings, Test Execution Summary, Alignment Verification) to enumerate failures.
  - Map each finding to architecture sources (Technical Stack, Components, ADRs, Cross-Cutting Concerns, Requirements Traceability Matrix).
  - Capture supporting evidence, file paths, impacted stakeholders, and dependencies for traceability.
- **QUESTIONS:**
  - What behavior was originally delivered and why?
  - Which findings caused rejection and where do they manifest?
  - Which architecture rules or patterns apply to each failure?
  - Which consumers or systems rely on the affected components?
- **CHECKLIST:**
- [ ] Original implementation intent documented from dev notes.
- [ ] Complete list of review findings with severity and evidence.
- [ ] Architecture references identified for every issue.
- [ ] Impacted stakeholders or dependencies noted.

3. **Step 3: Analyze Root Causes**
- **GOAL:** Build a complete Root-cause Traceability Table that ties symptoms to architecture requirements.
- **STEPS:**
  - Populate the table defined in `{TMPL}/dev-notes-tmpl.yaml` for every issue.
  - Link symptom → original implementation decision → relevant architecture requirement → root cause.
  - Define verification evidence (tests, metrics, logs) that will confirm the fix.
  - Capture file paths and line ranges needed by documentation.
- **QUESTIONS:**
  - What observable failure (test, log, metric) triggered this issue?
  - Which implementation decision caused the gap?
  - Which ADR or architecture section mandates the correct behavior?
  - How will I demonstrate the fix is successful?
- **CHECKLIST:**
- [ ] Traceability table includes Symptom, Root Cause, Architecture Ref, Changed Files, Affected Tests, Verification Evidence.
- [ ] Each root cause maps to a single, testable fix.
- [ ] Architecture citations (ADR/component/cross-cutting) captured per row.
- [ ] Verification method defined before coding starts.

4. **Step 4: Plan Changes**
- **GOAL:** Design minimal, architecture-aligned fixes for every root cause.
- **STEPS:**
  - Write a Diff Summary for each root cause covering file, lines, issue, root cause, fix strategy, architecture alignment, and impact.
  - Ensure each planned change resolves exactly one traceability row with surgical scope.
  - Identify required tests, coverage touchpoints, and any new cases needed.
  - Flag migrations, configuration updates, or cross-team notifications early.
- **QUESTIONS:**
  - Does the planned change solve exactly one root cause?
  - Which architecture pattern or ADR am I reaffirming with this change?
  - What existing tests will cover the fix, and do I need new ones?
  - Are there downstream consumers or contracts that must be warned?
- **CHECKLIST:**
- [ ] Diff Summary written for each planned change.
- [ ] Fix scope constrained to necessary files and lines.
- [ ] Required tests and coverage noted per fix.
- [ ] Potential migrations/config changes identified.

5. **Step 5: Implement Fixes**
- **GOAL:** Execute disciplined TDD cycles and produce minimal compliant code.
- **STEPS:**
  - Run the failing test (RED) and capture evidence showing the expected failure.
  - Apply the smallest implementation that passes the targeted test (GREEN).
  - Refactor safely while keeping tests green and aligned with repository patterns.
  - Prepare migrations or configuration updates when schemas or contracts change.
  - Document coverage deltas and test outputs for later reporting.
- **QUESTIONS:**
  - Did the targeted test fail for the expected reason before the fix?
  - Is my implementation the smallest change that makes the test pass?
  - Have I refactored safely with tests remaining green?
  - Are migrations or config scripts versioned and reversible?
- **CHECKLIST:**
- [ ] RED phase executed with failing test evidence captured.
- [ ] GREEN phase achieved via minimal compliant implementation.
- [ ] REFACTOR phase completed without breaking tests.
- [ ] VERIFY phase run with full suite confirmation and artifacts stored.

6. **Step 6: Verify Quality Gates**
- **GOAL:** Prove all quality controls, coverage, and performance budgets are satisfied.
- **STEPS:**
  - Run unit, integration, and e2e suites until every test passes simultaneously.
  - Measure coverage versus baseline and record the delta.
  - Execute static analysis, lint, type, and security checks with zero errors.
  - Validate contract tests, backward compatibility, and load tests at 2× expected traffic.
  - Capture p95/p99 latency metrics and confirm they stay within budget.
- **QUESTIONS:**
  - Are all automated quality gates green simultaneously?
  - What is the exact coverage change relative to baseline?
  - Did any contract or compatibility check reveal a breaking change?
  - Do performance metrics stay within budget under peak load?
- **CHECKLIST:**
- [ ] Unit, integration, and e2e suites green with evidence saved.
- [ ] Coverage ≥ baseline with delta documented.
- [ ] Static analysis, type checks, and security scans report zero errors.
- [ ] Contract and backward compatibility validations passed.
- [ ] Performance and load results within budget (p95/p99 thresholds met).

7. **Step 7: Add Observability**
- **GOAL:** Instrument changed paths with actionable logs, metrics, traces, and alerts.
- **STEPS:**
  - Add structured logs with correlation IDs, entity identifiers, and purpose.
  - Introduce or update metrics (counters, histograms) with labels and alert thresholds.
  - Enhance traces/spans with meaningful tags and error annotations.
  - Define alert routing, severity, and runbook references for new or updated signals.
- **QUESTIONS:**
  - Do logs capture enough context to diagnose new failures quickly?
  - Which metrics reveal success/failure rates and latency trends?
  - Are traces linked across services with consistent identifiers?
  - Who is paged and what action do they take when alerts trigger?
- **CHECKLIST:**
- [ ] New/updated logs documented with message, level, and fields.
- [ ] Metrics defined with purpose, labels, and alert conditions.
- [ ] Tracing enhancements captured with span names and tags.
- [ ] Alert policies recorded with severity and escalation details.

8. **Step 8: Update Documentation**
- **GOAL:** Capture the complete remediation story inside `{DEVNOTES}/{task_id}-dev-notes.md`.
- **STEPS:**
  - Update Brownfield Fix Details with review reference, original notes link, and decision.
  - Insert the finalized Root-cause Traceability Table, Diff Summaries, and analysis method.
  - Record quality gate outcomes, test evidence, performance metrics, and observability additions.
  - Document migrations/rollback scripts, known issues, and technical debt with mitigation plans.
- **QUESTIONS:**
  - Does the dev notes file now tell the complete recovery story?
  - Are quality gate results, metrics, and evidence reproducible by others?
  - Have I documented all operational impacts and rollback paths?
  - Are known issues and technical debt clearly owned and prioritized?
- **CHECKLIST:**
- [ ] Brownfield Fix Details section updated with review references.
- [ ] Root-cause Traceability Table and Diff Summaries inserted.
- [ ] Quality gate, testing, and performance evidence recorded.
- [ ] Observability enhancements and alerting noted.
- [ ] Migrations, rollback steps, known issues, and technical debt documented.

## [Operational Standards]

### Performance & Compatibility Standards
- Maintain performance budgets: p95 latency ≤ +10% increase, p99 latency ≤ +20%.
- Execute load test at 2× expected traffic before completion.
- Preserve backward compatibility across APIs, events, and contracts.
- Document migration path and deprecation timeline for any breaking change.

### Data & Schema Change Requirements
- Supply database migration and rollback scripts, each tested (up and down).
- Update API contract tests and versioning when interfaces change.
- Ensure event schema updates remain backward compatible for all consumers.

## [Examples]

### Good #1: Token Validation Fix
**Input**: `Auth token validation fails - test_expired_token_rejection failing`
1. Inputs validated before work.
2. Traceability table tied failure to missing expiry check in `TokenValidator.js:L25-30`.
3. Diff Summary added JWT expiry validation aligned with `security-arch.md §4.2`.
4. TDD cycle completed; coverage increased from 95% to 97%.
5. Observability added (`token_expired` log + `auth_rejection_reason` metric) and dev notes updated.

### Good #2: API Contract Compatibility
**Input**: `API returns {user_id: 123} but frontend expects {userId: 123}`
1. Architecture standard for camelCase confirmed.
2. Root cause linked to `UserController.js:L78`.
3. Response formatter introduced with Diff Summary referencing ADR.
4. RED → GREEN → REFACTOR cycle executed; all 12 contract tests passed.
5. Backward-compatible query parameter added with six-month deprecation plan and documented.

### Good #3: Concurrency Fix with Performance Budget
**Input**: `Race condition: duplicate inventory records on concurrent checkout`
1. ADR-045 (Redis distributed lock) validated.
2. Traceability table pinpointed missing lock in `InventoryService.js:L45-89`.
3. Redis lock implemented with reusable manager per Diff Summary.
4. Parallel test (50 concurrent requests) passed; performance stayed within budget.
5. Logs, metrics, traces, and alerts added; dev notes fully updated.

### Bad #1: Missing Input Validation
Skipping validation, guessing issues, or suppressing errors violates Step 1 and quality gates. Always stop with the mandated message when required inputs are absent.

### Bad #2: External Unreviewed Code
Copy-pasting unapproved solutions violates Constraints and Step 5. Use only repository or `{KNOWLEDGE}` assets and document architecture alignment.

### Bad #3: No Traceability or Performance Validation
Broad, undocumented changes without traceability break Steps 3–6 and usually explode performance budgets. Stay surgical, keep tests green, and prove performance before completion.
