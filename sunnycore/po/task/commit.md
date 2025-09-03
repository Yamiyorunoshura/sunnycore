# PO Commit Task Execution Instructions

<task_metadata>
name: "PO Commit Task Execution"
version: "2.0"
category: "po"
prompt_techniques: ["chain_of_thought", "self_discover", "markdown_structured", "multi_agent_coordination"]
quality_standards: ["evidence_based", "systematic", "template_compliant", "markdown_only_output"]
<!-- task_metadata>

## Task Overview
When the user calls the `*commit` command, read this task file and execute the unified commit workflow to either:

- Generate a standardized commit message based on the project conclusion report and propose commit commands (when CI/CD PASSED), or
- Update `docs/specs/` using standardized templates and generate a CI/CD status report (when CI/CD FAILED).

Follow the workflow: `{project_root}/sunnycore/po/workflow/unified-commit-workflow.md`.
Enforce: `{project_root}/sunnycore/po/enforcement/commit-orchestrator-enforcement.md`.
CI/CD Status Orchestrator Enforce: `{project_root}/sunnycore/po/enforcement/ci-cd-status-orchestrator-enforcement.md`.

## Execution Steps (SELF-DISCOVER Framework)

### Step 1: Intent and Inputs (SELECT)
1. Confirm `*commit` intent and gather necessary paths and templates
2. Load enforcement, task, and templates listed in the workflow

### Step 2: Status Determination (ADAPT)
1. Determine CI/CD status from `{project_root}/docs/ci/ci-cd-status.(json|md)`
2. If unknown, produce a normalized status report and HALT commit proposal

### Step 3: Branch Execution (IMPLEMENT)
- If PASSED:
  1. Ensure completion report exists (trigger conclusion workflow if missing)
  2. Populate commit message using `commit-message-tmpl.yaml`
  3. Write message to `{project_root}/docs/commit/last-commit-message.md`
  4. Propose commands: `git add -A`, `git commit -F {message_file}`
- If FAILED:
  1. Generate `{project_root}/docs/ci/ci-cd-status-report.md` using template
  2. Update `docs/specs/requirements.md`, `design.md`, `task.md` using `specs-update-tmpl.yaml`
  3. Validate all updated docs strictly match `cursor prompt/specs.md` formatting

### Step 4: Validation and Handover (APPLY)
1. Validate outputs against enforcement gates (no placeholders, markdown only)
2. Record outputs and provide next-step guidance

## Deliverables and Paths
- Commit message (on pass): `{{project_root}}/docs/commit/last-commit-message.md`
- Proposed commands (on pass):
  - `git add -A`
  - `git commit -F {{project_root}}/docs/commit/last-commit-message.md`
- CI/CD status report (on fail): `{{project_root}}/docs/ci/ci-cd-status-report.md`
- Updated specs (on fail):
  - `{{project_root}}/docs/specs/requirements.md`
  - `{{project_root}}/docs/specs/design.md`
  - `{{project_root}}/docs/specs/task.md`

## Definition of Done (DoD)
- All mandatory files loaded and understood
- CI/CD status determined and documented
- On pass: Commit message generated via template and written to file; commands proposed
- On fail: Specs updated via template; CI/CD status report generated; formatting validated
- All deliverables are Markdown and template-compliant

## Best Practices
- Use Chain of Thought for branching decisions; keep deliverables Markdown
- Be strictly evidence-driven: reference completion report sections and CI artifacts
- Prefer parallelizable steps (status parse, template load) before branching


