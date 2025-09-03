# CI/CD Status Orchestrator Enforcement Specification

## Core Execution Protocol

### Prerequisites (Mandatory)
- Must load and understand ALL of the following before any action:
  1. `{project_root}/sunnycore/po/workflow/unified-ci-cd-status-workflow.md`
  2. `{project_root}/sunnycore/po/templates/ci-cd-status-report-tmpl.yaml`

### Determinism and Safety (Mandatory)
- Determinism: temperature 0, top_p 1, seed 42
- Stable ordering: Normalize and sort all file paths lexicographically
- Fail-fast: If any mandatory file cannot be loaded, stop and report immediately

### Path Protection with Controlled Exceptions (Strict)
- Default Read-Only: `docs/ci/**`
- Controlled Exceptions (this orchestrator only):
  - `docs/ci/ci-cd-status.json`
  - `docs/ci/ci-cd-status.md`
  - `docs/ci/ci-cd-status-report.md`
  All writes must be generated via the workflow actions and `{project_root}/sunnycore/po/templates/ci-cd-status-report-tmpl.yaml`.
- Markdown-only deliverables; no placeholders; strict template compliance.

### Quality Gates (Mandatory)
- Gate 1: Mandatory files loaded
- Gate 2: Status determined or minimal status generated
- Gate 3: Status report produced in Markdown with template compliance

### Allowed Actions (Aligned with Workflow)
- Initialization: `ensure_dir`, `load_file`
- Detection: `try_read_status_from`, `if_missing_then_generate_minimal`
- Reporting: `write_status_report_from_template`

### Disallowed Actions
- Writing outside the allowed files under `docs/ci/`
- Producing non-Markdown deliverables under `docs/**`


