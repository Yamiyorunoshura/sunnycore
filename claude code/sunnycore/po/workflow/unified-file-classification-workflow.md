---
category: po
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: unified-file-classification-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '2.0'
---

# 統一文件分類工作流程

<workflow_metadata>
name: "智能文件分類工作流程"
version: "2.0"
category: "po"
complexity_level: "complex"
prompt_techniques: ["chain_of_thought", "self_discover", "xml_structured"]
agent_role: "po_file-classifier"
</workflow_metadata>

<execution_settings>
deterministic: true
parallel_enabled: true
prompt_optimization: true
quality_gates: ["information_validation", "classification_accuracy", "safety_verification"]
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
- **Verification Points**: Critical safety checkpoints must be included in todo list
- **Priority**: Set reasonable priorities to ensure dependency relationships are respected
- **Status Management**: Update todo status in a timely manner during execution (pending → in_progress → completed)
- **Safety Focus**: Prioritize safety validation and file protection measures
- **Completeness**: Only mark as `completed` when tasks are fully completed
</enforcement>

---

## 上下文摘要機制

<context-summarization>
**目的**：在每個階段完成後輸出結構化摘要以節省上下文，強調安全與分類決策。

**方法**：
- 使用 `{project_root}/sunnycore/po/templates/stage-summary-tmpl.yaml`
- 目標 200 字（上限 260 字），包含 objective、key_decisions、inputs/outputs、notables、risks、recommendations、references

**保留策略**：
- 追加並裁剪；僅保留最近 2 個完整摘要
- 舊摘要壓縮為 1–2 行要點；丟棄 2 個階段前原始細節；保留 open_risks、pending_decisions、followups
<!-- context-summarization>

<role>
你是一名專業文件分類專家，負責識別和分類項目文件，確保核心文件安全並優化項目結構。

**Chain of Thought Integration**: 在進行任何文件分析前，我會首先理解文件分類需求，然後系統性推理出最安全可靠的分類策略。

**SELF-DISCOVER Framework Application**: 我會使用結構化方法來選擇適當的分類標準，調整方法以適應項目特性，並實施comprehensive的文件安全分類。

**Safety-First Approach**: 我優先考慮文件安全，在不確定的情況下總是選擇保守的分類決策。
</role>

## 概述

本工作流程專為文件分類代理設計，能夠智能識別和分類項目文件，區分臨時測試文件和應保留的核心文件：

<workflow_objectives>
- 系統化分析項目文件結構和類型
- 應用 Chain of Thought 進行風險評估
- 使用 SELF-DISCOVER 框架優化分類策略
- 生成 Markdown 結構化的清理建議和風險評估
- 確保核心文件安全，優化項目結構
</workflow_objectives>

## 高階提示詞技巧整合

<prompt_techniques_integration>
<chain_of_thought>
<description>在文件分析和風險評估中應用逐步推理</description>
<reasoning_flow>
文件掃描 → 類型識別 → 依賴分析 → 風險評估 → 分類決策
</reasoning_flow>
</chain_of_thought>

<self_discover>
<description>動態調整文件分類策略</description>
<adaptive_classification>
根據項目特性選擇最適合的分類方法和安全標準
</adaptive_classification>
</self_discover>

<markdown_structured_output>
<standard_structure>
## 文件分析結果
詳細的文件掃描和分類結果

## 分類建議
### 保留文件
- 核心源代碼文件
- 重要配置文件

### 可清理文件  
- 臨時文件
- 構建產物

## 風險評估
### 高風險操作
描述需要謹慎處理的文件

### 低風險操作
描述可安全清理的文件

## 清理計劃
具體的清理步驟和建議
</standard_structure>
<output_requirements>
- 最終輸出必須是純Markdown格式
- 絕對禁止在輸出文檔中使用XML標籤
- 確保文檔結構清晰，便於人類閱讀
</output_requirements>
</markdown_structured_output>
</prompt_techniques_integration>

<execution_protocol>
<todo_list_creation importance="critical">
<description>AI 必須在執行任何工作流程步驟之前創建包含所有工作流程步驟的 todo 列表</description>
  process_steps:
    1_analyze_workflow:
      description: Analyze workflow structure - carefully read entire workflow file,
        identify all stages, steps and tasks
      priority: high
    2_extract_tasks:
      description: Extract key tasks - convert core tasks of each stage to specific
        todo items
      priority: high
    3_set_priorities:
      description: Set priorities - set priorities based on task importance and dependencies
      priority: medium
    4_create_todo_list:
      description: Create Todo List - use todo_write tool to create structured todo
        list
      priority: high
    5_execute_workflow:
      description: Execute and update - execute tasks in todo list order, update status
        timely
      priority: high
  requirements:
    completeness: Only mark as completed when task is fully completed
    coverage: Each main stage should have corresponding todo item
    priority_setting: Set reasonable priorities, ensure dependency relationships respected
    status_tracking: Update todo status timely during execution (pending → in_progress
      → completed)
    uniqueness: Only one task can be in in_progress status simultaneously
    validation: Key validation checkpoints must be included in todo list
  tool_syntax:
    format: JSON
    structure: "{\n  \"todos\": [\n    {\n      \"content\": \"Specific task description\"\
      ,\n      \"status\": \"pending|in_progress|completed\",\n      \"id\": \"unique\
      \ identifier\",\n      \"priority\": \"high|medium|low\"\n    }\n  ]\n}\n"
version: 1
---





workflow:
  name: "Unified File Classification Workflow"
  description: "Identify and classify project files, distinguish temporary test files from core files that should be retained, generate cleanup suggestions and risk assessments."
  enforcement_level: "strict"
  halt_on_validation_failure: true

inputs:
  project_root: "<auto/>"
  task_id: "<optional/>"
  classification_scope: "full_project"  # full_project, specific_directories, file_types

execution_hints:
  determinism:
    temperature: 0
    top_p: 0
    top_k: 1
    seed: 42
    response_variability: "none"
  parallelization:
    enabled: true
    max_concurrency: 10
    in_stages:
      file_scanning:
        - "scan_project_structure"
        - "identify_file_types"
        - "analyze_file_sizes"
        - "detect_hidden_files"
      classification_analysis:
        - "analyze_source_code_files"
        - "analyze_test_files"
        - "analyze_config_files"
        - "analyze_documentation_files"
        - "analyze_script_files"
        - "analyze_dependency_relationships"
      risk_assessment:
        - "assess_cleanup_risks"
        - "evaluate_dependency_impacts"
        - "analyze_functional_impacts"
        - "identify_safety_concerns"
  caching:
    enabled: true
    strategy: "content_hash"
    key_paths:
      - "{{project_root}}/src/**/*"
      - "{{project_root}}/test/**/*"
      - "{{project_root}}/docs/**/*"
      - "{{project_root}}/config/**/*"
    expire_on_changes: true
  ordering:
    list_sorting: "stable_lexicographic"
    normalize_paths: true

path_aliases:
  WORKFLOW_FILE: "{project_root}/sunnycore/po/workflow/unified-file-classification-workflow.yaml"
  ENFORCEMENT_FILE: "{project_root}/sunnycore/po/enforcement/po_file-classifier-enforcement.md"

classification_criteria:
  must_keep:
    - "source_code_files"
    - "test_files"
    - "config_files"
    - "documentation_files"
    - "script_files"
    - "license_files"
  can_clean:
    - "temporary_files"
    - "build_artifacts"
    - "ide_configs"
    - "backup_files"
    - "cache_files"
  needs_review:
    - "boundary_files"
    - "large_files"
    - "binary_files"
    - "hidden_files"
    - "external_dependencies"

file_type_patterns:
  source_code:
    - "*.js", "*.ts", "*.jsx", "*.tsx"
    - "*.py", "*.java", "*.cpp", "*.c", "*.cs"
    - "*.go", "*.rs", "*.php", "*.rb"
    - "*.swift", "*.kt", "*.scala"
  test_files:
    - "*test*.js", "*test*.ts", "*test*.py"
    - "*spec*.js", "*spec*.ts", "*spec*.py"
    - "test_*.py", "test_*.js", "test_*.ts"
  config_files:
    - "*.json", "*.yaml", "*.yml", "*.toml"
    - "*.env", "*.config", "*.conf"
    - "package.json", "requirements.txt", "pom.xml"
  documentation:
    - "*.md", "*.rst", "*.txt"
    - "*.pdf", "*.doc", "*.docx"
    - "README*", "CHANGELOG*", "LICENSE*"
  scripts:
    - "*.sh", "*.bat", "*.ps1"
    - "Makefile", "Dockerfile", "docker-compose*"
  temporary:
    - "*.tmp", "*.temp", "*.bak", "*.backup"
    - "*.log", "*.out", "*.err"
    - "node_modules/", "dist/", "build/", "target/"

# File Scanning Stage
file_scanning:
  description: "Scan and analyze project file structure"
  steps:
    scan_project_structure:
      description: "Scan project directory structure"
      method: "recursive_directory_scan"
      output: "project_structure_map"
      validation:
        min_files: 1
        max_depth: 10
        exclude_patterns:
          - ".git/**"
          - "node_modules/**"
          - "dist/**"
          - "build/**"
          - "target/**"

    identify_file_types:
      description: "Identify file types"
      method: "file_extension_analysis"
      input: "project_structure_map"
      output: "file_type_classification"
      validation:
        required_categories: ["source_code", "test_files", "config_files", "documentation"]

    analyze_file_sizes:
      description: "Analyze file sizes"
      method: "file_size_analysis"
      input: "project_structure_map"
      output: "file_size_statistics"
      validation:
        max_file_size: "100MB"
        large_file_threshold: "10MB"

    detect_hidden_files:
      description: "Detect hidden files"
      method: "hidden_file_detection"
      input: "project_structure_map"
      output: "hidden_files_list"
      validation:
        include_patterns: [".*"]

# Classification Analysis Stage
classification_analysis:
  description: "Deep analysis of file content and dependency relationships"
  steps:
    analyze_source_code_files:
      description: "Analyze source code files"
      method: "source_code_analysis"
      input: "file_type_classification"
      output: "source_code_analysis"
      validation:
        min_analysis_depth: "function_level"
        required_metrics: ["complexity", "dependencies", "test_coverage"]

    analyze_test_files:
      description: "Analyze test files"
      method: "test_file_analysis"
      input: "file_type_classification"
      output: "test_file_analysis"
      validation:
        required_metrics: ["test_coverage", "test_types", "test_quality"]

    analyze_config_files:
      description: "Analyze configuration files"
      method: "config_file_analysis"
      input: "file_type_classification"
      output: "config_file_analysis"
      validation:
        required_metrics: ["environment_specific", "security_implications", "dependencies"]

    analyze_documentation_files:
      description: "Analyze documentation files"
      method: "documentation_analysis"
      input: "file_type_classification"
      output: "documentation_analysis"
      validation:
        required_metrics: ["completeness", "accuracy", "usefulness"]

    analyze_script_files:
      description: "Analyze script files"
      method: "script_file_analysis"
      input: "file_type_classification"
      output: "script_file_analysis"
      validation:
        required_metrics: ["functionality", "safety", "maintainability"]

    analyze_dependency_relationships:
      description: "Analyze file dependency relationships"
      method: "dependency_analysis"
      input: ["source_code_analysis", "config_file_analysis"]
      output: "dependency_graph"
      validation:
        required_metrics: ["imports", "exports", "circular_dependencies"]

# Risk Assessment Stage
risk_assessment:
  description: "Assess risks and impacts of file cleanup"
  steps:
    assess_cleanup_risks:
      description: "Assess cleanup risks"
      method: "risk_assessment_analysis"
      input: ["file_type_classification", "dependency_graph"]
      output: "cleanup_risk_assessment"
      validation:
        required_risk_levels: ["low", "medium", "high", "critical"]
        required_metrics: ["probability", "impact", "mitigation"]

    evaluate_dependency_impacts:
      description: "Evaluate dependency impacts"
      method: "dependency_impact_analysis"
      input: "dependency_graph"
      output: "dependency_impact_assessment"
      validation:
        required_metrics: ["direct_impact", "indirect_impact", "cascade_effects"]

    analyze_functional_impacts:
      description: "Analyze functional impacts"
      method: "functional_impact_analysis"
      input: ["source_code_analysis", "test_file_analysis"]
      output: "functional_impact_assessment"
      validation:
        required_metrics: ["core_functionality", "optional_features", "integration_points"]

    identify_safety_concerns:
      description: "Identify security concerns"
      method: "safety_analysis"
      input: ["config_file_analysis", "script_file_analysis"]
      output: "safety_concerns"
      validation:
        required_metrics: ["security_risks", "data_protection", "access_control"]

# Cleanup Execution Stage
cleanup_execution:
  description: "Directly execute file cleanup operations"
  steps:
    execute_cleanup_operations:
      description: "Execute cleanup operations"
      method: "cleanup_execution"
      input: ["cleanup_risk_assessment", "dependency_impact_assessment"]
      output: "cleanup_execution_log"
      validation:
        required_sections: ["safe_to_clean", "needs_review", "must_keep", "risk_warnings"]

    create_backup_protection:
      description: "Create backup protection"
      method: "backup_creation"
      input: "cleanup_risk_assessment"
      output: "backup_files"
      validation:
        required_features: ["safety_checks", "backup_mechanism", "error_handling", "logging"]

    generate_execution_report:
      description: "Generate execution report"
      method: "execution_report_generation"
      input: ["cleanup_execution_log", "backup_files", "risk_assessment"]
      output: "execution_report"
      validation:
        required_sections: ["executive_summary", "detailed_analysis", "execution_log", "risk_assessment", "backup_status"]

# Collaboration with Other Agents
collaboration:
  with_project_concluder:
    trigger: "parallel_execution_on_conclude"
    integration:
      - "file_classification_results"
      - "cleanup_execution_log"
      - "risk_assessment_summary"
    output_format: "structured_data_for_conclusion_report"

  with_knowledge_curator:
    trigger: "after_classification_complete"
    integration:
      - "file_organization_best_practices"
      - "knowledge_management_structure"
    output_format: "knowledge_base_contributions"

  with_architecture_documenter:
    trigger: "after_dependency_analysis"
    integration:
      - "file_structure_organization"
      - "module_boundary_definitions"
    output_format: "architecture_documentation_updates"

# Output Format Definitions
output_formats:
  classification_report:
    format: "markdown"
    sections:
      - "executive_summary"
      - "file_inventory"
      - "classification_results"
      - "execution_log"
      - "risk_assessment"
      - "backup_status"

  cleanup_scripts:
    format: "shell_script"
    features:
      - "safety_checks"
      - "backup_creation"
      - "dry_run_mode"
      - "error_handling"
      - "comprehensive_logging"

  risk_assessment:
    format: "structured_data"
    risk_levels:
      - "low": "minimal_impact"
      - "medium": "moderate_impact"
      - "high": "significant_impact"
      - "critical": "severe_impact"

# Validation and Quality Assurance
validation_and_quality:
  pre_execution_checks:
    - "required_files_available"
    - "permissions_validated"
    - "dependencies_resolved"

  execution_monitoring:
    - "progress_tracking"
    - "performance_monitoring"
    - "error_tracking"

  post_execution_validation:
    - "classification_accuracy"
    - "completeness_check"
    - "consistency_verification"

  quality_metrics:
    - "classification_precision"
    - "risk_assessment_accuracy"
    - "cleanup_safety_score"
    - "execution_efficiency"

# Error Handling and Recovery
error_handling:
  classification_errors:
    action: "log_and_continue"
    fallback: "mark_for_manual_review"

  analysis_failures:
    action: "retry_with_reduced_scope"
    fallback: "skip_and_warn"

  risk_assessment_failures:
    action: "halt_execution"
    fallback: "generate_manual_review_list"

  cleanup_execution_failures:
    action: "halt_execution"
    fallback: "generate_manual_cleanup_guide"

# Execution Configuration
execution_config:
  timeout:
    file_scanning: "5m"
    classification_analysis: "10m"
    risk_assessment: "5m"
    cleanup_execution: "5m"

  retry_policy:
    max_retries: 3
    retry_delay: "30s"
    exponential_backoff: true

  resource_limits:
    max_memory: "2GB"
    max_cpu_percent: 80
    max_disk_io: "100MB/s"
