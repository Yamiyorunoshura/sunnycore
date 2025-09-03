---
category: po
description: 統一 CI/CD 狀態檢測與報告工作流程
last_updated: '2025-09-03'
name: unified-ci-cd-status-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- markdown_structured
version: '1.0'
---

# 統一 CI/CD 狀態工作流程

<workflow_metadata>
name: "Unified CI/CD Status Workflow"
version: "1.0"
category: "po"
agent_role: "ci-cd-status-orchestrator"
</workflow_metadata>

<execution_settings>
deterministic: true
parallel_enabled: true
quality_gates: ["mandatory_files_loaded", "status_report_produced", "markdown_only_output"]
</execution_settings>

<role>
你負責標準化檢測 CI/CD 狀態，產出正規化的狀態檔與報告：
- 生成 `{project_root}/docs/ci/ci-cd-status.(json|md)` 若不存在
- 產生 `{project_root}/docs/ci/ci-cd-status-report.md`（用模板）
所有外部輸出必須為 Markdown。
</role>

paths:
  CI_STATUS_FILE_MD: "{project_root}/docs/ci/ci-cd-status.md"
  CI_STATUS_FILE_JSON: "{project_root}/docs/ci/ci-cd-status.json"
  CI_CD_STATUS_REPORT: "{project_root}/docs/ci/ci-cd-status-report.md"
  CI_CD_REPORT_TEMPLATE: "{project_root}/sunnycore/po/templates/ci-cd-status-report-tmpl.yaml"

stages:
  - id: init
    title: Initialization
    actions:
      - ensure_dir: "{project_root}/docs/ci"
      - load_file: "{CI_CD_REPORT_TEMPLATE}"

  - id: detect
    title: Detect or Create CI/CD status
    actions:
      - try_read_status_from: ["{CI_STATUS_FILE_JSON}", "{CI_STATUS_FILE_MD}"]
      - if_missing_then_generate_minimal: "{CI_STATUS_FILE_MD}"

  - id: report
    title: Produce CI/CD status report
    actions:
      - write_status_report_from_template: "{CI_CD_REPORT_TEMPLATE}" → "{CI_CD_STATUS_REPORT}"

output:
  status_files:
    - "{CI_STATUS_FILE_JSON}"
    - "{CI_STATUS_FILE_MD}"
  report: "{CI_CD_STATUS_REPORT}"


