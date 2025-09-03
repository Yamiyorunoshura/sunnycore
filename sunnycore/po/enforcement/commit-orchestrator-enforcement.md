# Commit Orchestrator Enforcement Specification

## Core Execution Protocol

### Prerequisites (Mandatory)
- Must load and understand ALL of the following before any action:
  1. `{project_root}/sunnycore/po/task/commit.md`
  2. `{project_root}/sunnycore/po/workflow/unified-commit-workflow.md`
  3. `{project_root}/sunnycore/po/templates/commit-message-tmpl.yaml`
  4. `{project_root}/sunnycore/po/templates/ci-cd-status-report-tmpl.yaml`
  5. `{project_root}/sunnycore/po/templates/specs-update-tmpl.yaml`
  6. `{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.md`
  7. `{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml`

### Determinism and Safety (Mandatory)
- Determinism: Use temperature 0, top_p 1, seed 42 for all automated steps
- Stable ordering: Normalize and sort all file paths lexicographically
- Fail-fast: If any mandatory file cannot be loaded, stop and report immediately
- Non-destructive: Do not execute `git commit` automatically; propose the command for approval first

### CI/CD Status Decision (Mandatory)
- CI/CD status MUST be determined prior to any commit action
- Primary source: `{project_root}/docs/ci/ci-cd-status.md` or `{project_root}/docs/ci/ci-cd-status.json`
- Secondary sources (fallbacks):
  - CI vendor badges or artifacts recorded in `README.md` or `.github/` / `.gitlab/`
  - Latest pipeline summary exported to `{project_root}/docs/ci/` by other automation
- Status branches:
  - Passed → Generate commit message from project conclusion and propose commit
  - Failed → Update specs docs using standardized template; DO NOT propose a code-change commit

### Evidence-based Commit Message (Absolute Mandatory)
- Source-of-truth: `{project_root}/docs/completion-reports/{task_id}-completion.md`
- Each commit header/body must trace to completion evidence: PR links, commit hashes, changed files, tests, measurements
- If completion report is missing, orchestrator must first trigger the conclusion workflow before generating a commit message

### Standardized Commit Message (Mandatory Compliance)
- Must conform to `{project_root}/sunnycore/po/templates/commit-message-tmpl.yaml`
- Header format: `type(scope): summary`
- Body sections must include: change summary, evidence, acceptance/test references, impacts/risks, breaking changes (if any)
- Footer may include: issue references, co-authored-by
- Output traceability: Write the final plain-text message to `{project_root}/docs/commit/last-commit-message.md`

### Specs Update on CI/CD Failure (Mandatory Compliance)
- Must follow `{project_root}/sunnycore/po/templates/specs-update-tmpl.yaml`
- Updates target files (as needed):
  - `docs/specs/requirements.md`
  - `docs/specs/design.md`
  - `docs/specs/task.md`
- All updates must preserve each file's required structure from `cursor prompt/specs.md`
- Generate a CI/CD status report using `{project_root}/sunnycore/po/templates/ci-cd-status-report-tmpl.yaml` at `{project_root}/docs/ci/ci-cd-status-report.md`

### Markdown and XML Usage (Strict)
- External deliverables: Markdown only (reports, specs, commit message file)
- XML: Allowed only for internal orchestration logs if needed; never write XML to project deliverables

### Multi-Agent Collaboration (Coordinated)
- Project-Concluder: Provide completion evidence foundation
- CI/CD Aggregator (conceptual sub-agent within this workflow): Normalize pipeline results into status report
- QA Reviewer (advisory): Optionally review spec updates for clarity

### Output Locations (Fixed)
- Commit message file: `{{project_root}}/docs/commit/last-commit-message.md`
- CI/CD status report: `{{project_root}}/docs/ci/ci-cd-status-report.md`
- Updated specs: `{{project_root}}/docs/specs/*.md`

### Quality Gates (Mandatory)
- Gate 1: Mandatory files loaded and understood
- Gate 2: CI/CD status determined and recorded
- Gate 3: If passed → Commit message fully conforms to template and is evidence-traceable
- Gate 4: If failed → Specs updates fully conform to templates; no placeholders remain
- Gate 5: All outputs validated for Markdown format; no XML tags in deliverables

### Failure Handling (Recorded and Actionable)
- Missing conclusion report → Trigger conclusion workflow; retry commit message generation
- Unknown CI/CD status → Generate status report with "unknown" state and halt commit proposal
- Template non-compliance → Record diffs and correction plan; do not proceed until resolved
- File write errors → Report with absolute paths and remediation suggestions


