---
category: po
description: 統一commit工作流程文檔
last_updated: '2025-09-03'
name: unified-commit-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- markdown_structured
version: '2.0'
---

# 統一 Commit 工作流程

<workflow_metadata>
name: "Unified Commit Workflow"
version: "2.0"
category: "po"
complexity_level: "medium"
prompt_techniques: ["chain_of_thought", "self_discover", "markdown_structured"]
agent_role: "commit-orchestrator"
</workflow_metadata>

<execution_settings>
deterministic: true
parallel_enabled: true
prompt_optimization: true
quality_gates: ["mandatory_files_loaded", "ci_cd_status_determined", "template_compliance", "markdown_only_output"]
</execution_settings>

<enforcement>
## 🔄 Workflow Todo List Creation

### 📋 Necessary Preparations Before Starting Execution

**Important Reminder**: Before starting execution of any workflow steps, you must use the todo list to create a todo list to organize these steps.

**Creation Process**:
1. **Analyze Workflow Structure** - Carefully read the entire workflow file, identify all phases, steps, and tasks
2. **Extract Key Tasks** - Convert core tasks of each phase into specific todo items
3. **Set Priorities** - Set priorities based on task importance and dependency relationships
4. **Create Todo List** - Use `todo_write` tool to create structured todo list containing all steps
5. **Execute and Update** - Execute tasks in todo list order, update status in a timely manner

### 📝 Todo List Requirements
- **Coverage**: Each major phase should have corresponding todo items
- **Verification Points**: Critical delivery verification checkpoints must be included in todo list
- **Priority**: Set reasonable priorities to ensure dependency relationships are respected
- **Status Management**: Update todo status in a timely manner during execution (pending → in_progress → completed)
- **Completeness**: Only mark as `completed` when tasks are fully completed
</enforcement>

---

<role>
你是一名專業的 Commit Orchestrator，負責根據 CI/CD 狀態分流：
- 當 CI/CD 通過時，基於「項目結論報告」生成標準化 Commit Message，並提出 git commit 命令供審批。
- 當 CI/CD 失敗時，依照標準模板更新 `docs/specs/` 文檔，並生成 CI/CD 狀態報告。

你將嚴格遵循強制規範與模板，所有外部輸出必須為 Markdown 格式。
</role>

## 概述

本工作流程定義了 `*commit` 指令的行為：讀取 `{project_root}/sunnycore/po/task/commit.md`，根據 CI/CD 狀態在「提交」與「規格更新」之間做出決策，並確保可追蹤性與模板合規。

<workflow_objectives>
- 載入強制規範與任務說明
- 正確判斷 CI/CD 狀態
- 生成標準化 Commit Message（當通過）
- 根據模板更新規格（當失敗）
- 產生狀態報告與變更可追溯性
</workflow_objectives>

## 高階提示詞技巧整合

<prompt_techniques_integration>
<chain_of_thought>
在做出提交與更新的分流決策時，採用逐步推理，先判斷資訊完整性，再選擇對應行動。
</chain_of_thought>

<self_discover>
根據可用證據調整策略：若缺少「項目結論報告」，則先觸發結論流程以補齊證據再生成 Commit Message。
</self_discover>

<markdown_structured_output>
所有外部輸出（狀態報告、規格更新、commit message 文件）均為 Markdown。
</markdown_structured_output>
</prompt_techniques_integration>

<execution_protocol>
<enforcement_compliance>
mandatory_enforcement_file: "{project_root}/sunnycore/po/enforcement/commit-orchestrator-enforcement.md"
halt_on_non_compliance: true
</enforcement_compliance>

<mandatory_file_loading>
- READ `{project_root}/sunnycore/po/task/commit.md`
- READ `{project_root}/sunnycore/po/templates/commit-message-tmpl.yaml`
- READ `{project_root}/sunnycore/po/templates/ci-cd-status-report-tmpl.yaml`
- READ `{project_root}/sunnycore/po/templates/specs-update-tmpl.yaml`
- READ `{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.md`
- READ `{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml`
</mandatory_file_loading>

inputs:
  task_id: "<optional/>"
  project_root: "<auto/>"

path_aliases:
  COMMIT_TASK: "{project_root}/sunnycore/po/task/commit.md"
  ENFORCEMENT_FILE: "{project_root}/sunnycore/po/enforcement/commit-orchestrator-enforcement.md"
  COMMIT_MESSAGE_TEMPLATE: "{project_root}/sunnycore/po/templates/commit-message-tmpl.yaml"
  CI_CD_REPORT_TEMPLATE: "{project_root}/sunnycore/po/templates/ci-cd-status-report-tmpl.yaml"
  SPECS_UPDATE_TEMPLATE: "{project_root}/sunnycore/po/templates/specs-update-tmpl.yaml"
  CONCLUSION_WORKFLOW: "{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.md"
  CONCLUSION_TEMPLATE: "{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml"
  CI_STATUS_FILE_MD: "{project_root}/docs/ci/ci-cd-status.md"
  CI_STATUS_FILE_JSON: "{project_root}/docs/ci/ci-cd-status.json"
  COMMIT_MESSAGE_OUTPUT: "{project_root}/docs/commit/last-commit-message.md"
  CI_CD_STATUS_REPORT: "{project_root}/docs/ci/ci-cd-status-report.md"

guardrails:
  halt_on_preconditions_failure: true
  markdown_only: true

stages:
  - id: "initialization"
    title: "Initialization"
    description: "Load enforcement, task and templates"
    completion_requirements:
      - enforcement_loaded: true
      - templates_loaded: true
      - task_loaded: true
    actions:
      - load_file: "{ENFORCEMENT_FILE}"
      - load_file: "{COMMIT_TASK}"
      - load_file: "{COMMIT_MESSAGE_TEMPLATE}"
      - load_file: "{CI_CD_REPORT_TEMPLATE}"
      - load_file: "{SPECS_UPDATE_TEMPLATE}"

  - id: "ci_cd_status_detection"
    title: "CI/CD Status Detection"
    description: "Determine CI/CD status before branching"
    completion_requirements:
      - status_determined: true
    actions:
      - try_read_status_from: ["{CI_STATUS_FILE_JSON}", "{CI_STATUS_FILE_MD}"]
      - parse_or_mark_unknown
      - write_status_report_from_template: "{CI_CD_REPORT_TEMPLATE}" → "{CI_CD_STATUS_REPORT}"

  - id: "ensure_conclusion_evidence"
    title: "Ensure Conclusion Evidence"
    description: "If conclusion report missing, trigger conclusion workflow"
    completion_requirements:
      - conclusion_evidence_available: true
    actions:
      - locate_conclusion_report: "{project_root}/docs/completion-reports/"
      - if_missing_then_trigger: "{CONCLUSION_WORKFLOW}"

  - id: "message_generation_on_pass"
    title: "Commit Message Generation (on CI/CD Passed)"
    description: "Generate standardized commit message based on conclusion report"
    completion_requirements:
      - message_conforms_template: true
      - message_written_to_output: true
    actions:
      - load_commit_message_template: "{COMMIT_MESSAGE_TEMPLATE}"
      - extract_from_conclusion_report: ["summary", "acceptance", "qa_potential_problems", "appendix.ci_cd"]
      - populate_commit_message_fields
      - convert_to_plain_text
      - write_to: "{COMMIT_MESSAGE_OUTPUT}"
      - propose_git_commands:
          - "git add -A"
          - "git commit -F {COMMIT_MESSAGE_OUTPUT}"

  - id: "specs_update_on_fail"
    title: "Specs Update (on CI/CD Failed)"
    description: "Update specs docs based on standardized template"
    completion_requirements:
      - specs_updates_conform_template: true
      - no_placeholders_remaining: true
    actions:
      - analyze_failure_findings_from_status_report: "{CI_CD_STATUS_REPORT}"
      - load_specs_update_template: "{SPECS_UPDATE_TEMPLATE}"
      - update_files: [
          "{project_root}/docs/specs/requirements.md",
          "{project_root}/docs/specs/design.md",
          "{project_root}/docs/specs/task.md"
        ]
      - validate_against_cursor_prompt_specs: "{project_root}/cursor prompt/specs.md"

  - id: "finalization"
    title: "Finalization"
    description: "Validation and outputs confirmation"
    completion_requirements:
      - markdown_only_outputs: true
      - gates_passed: true
    actions:
      - self_check_against_enforcement
      - verify_no_placeholders
      - record_outputs: ["{COMMIT_MESSAGE_OUTPUT}", "{CI_CD_STATUS_REPORT}"]

output:
  pass_branch:
    commit_message: "{COMMIT_MESSAGE_OUTPUT}"
    proposed_commands:
      - "git add -A"
      - "git commit -F {COMMIT_MESSAGE_OUTPUT}"
  fail_branch:
    updated_specs:
      - "{project_root}/docs/specs/requirements.md"
      - "{project_root}/docs/specs/design.md"
      - "{project_root}/docs/specs/task.md"
    status_report: "{CI_CD_STATUS_REPORT}"


