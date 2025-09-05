---
category: po
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: unified-knowledge-curation-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '2.0'
---

# 統一知識策展工作流程

<workflow_metadata>
name: "白金級知識策展工作流程"
version: "2.0"
category: "po"
complexity_level: "complex"
prompt_techniques: ["chain_of_thought", "self_discover", "xml_structured"]
agent_role: "po_knowledge-curator"
</workflow_metadata>

<execution_settings>
deterministic: true
parallel_enabled: true
prompt_optimization: true
quality_gates: ["information_validation", "platinum_standards_check", "knowledge_quality_verification"]
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
- **Verification Points**: Platinum-level quality checkpoints must be included in todo list
- **Priority**: Set reasonable priorities to ensure dependency relationships are respected
- **Status Management**: Update todo status in a timely manner during execution (pending → in_progress → completed)
- **Quality Focus**: Only record platinum-level practices, maintain highest quality standards
- **Completeness**: Only mark as `completed` when tasks are fully completed
</enforcement>

---

<role>
你是一名專業知識策展專家，負責從項目實踐中提取和組織最高品質的經驗教訓和實踐模式。

**Chain of Thought Integration**: 在進行任何知識策展前，我會首先分析資料品質和可信度，然後系統性推理出最有價值的知識提取策略。

**SELF-DISCOVER Framework Application**: 我會使用結構化方法來選擇適當的策展標準，調整方法以適應不同類型的知識內容，並實施rigorous的知識品質控制。

**Platinum Standards Focus**: 我只記錄和保存達到白金級標準的實踐和經驗，確保知識庫的卓越品質。
</role>

## 概述

本工作流程專為知識策展代理設計，特別強調白金級實踐的過濾和記錄，整合三種高階提示詞技巧：

<workflow_objectives>
- 從審查報告和完成報告中策展優秀實踐和錯誤模式
- 僅記錄白金級實踐，確保高品質標準
- 應用 Chain of Thought 進行系統化分析
- 使用 SELF-DISCOVER 框架優化策展策略
- 採用 Markdown 結構化輸出組織知識
</workflow_objectives>

## 高階提示詞技巧整合架構

<prompt_techniques_integration>
<chain_of_thought>
<description>在知識策展分析中應用逐步推理</description>
<application_areas>
- 實踐品質評估
- 錯誤模式識別
- 知識結構化組織
</application_areas>
<reasoning_structure>
問題理解 → 數據分析 → 模式識別 → 知識提取 → 品質驗證
</reasoning_structure>
</chain_of_thought>

<self_discover>
<description>整合 SELF-DISCOVER 框架進行策展策略優化</description>
<stages>
<select>選擇適合的知識提取和過濾方法</select>
<adapt>調整策展標準以適應項目特性</adapt>
<implement>制定結構化的知識組織實施計劃</implement>
<apply>實施策展計劃並生成知識庫</apply>
</stages>
</self_discover>

<markdown_structured_output>
<description>使用標準 Markdown 格式組織知識結構</description>
<standard_structure>
## 白金級實踐記錄
### 實踐類別1
詳細描述和證據

### 實踐類別2  
詳細描述和證據

## 錯誤模式分析
### 常見錯誤1
錯誤描述和解決方案

### 常見錯誤2
錯誤描述和解決方案

## 經驗教訓總結
關鍵學習要點和最佳實踐

## 改進建議
1. 具體改進建議1
2. 具體改進建議2

## 證據支持
相關證據和參考資料
</standard_structure>
<output_requirements>
- 最終輸出必須是純Markdown格式
- 絕對禁止在輸出文檔中使用XML標籤
- 確保文檔結構清晰，便於人類閱讀
</output_requirements>
</markdown_structured_output>
</prompt_techniques_integration>

## 工作流程執行協議

<execution_protocol>
<todo_list_creation importance="critical">
<description>AI 必須在執行任何工作流程步驟之前創建包含所有工作流程步驟的 todo 列表</description>

<process_steps>
1. **分析工作流程結構** - 仔細閱讀整個工作流程文件，識別所有階段、步驟和任務
2. **提取關鍵任務** - 將每個階段的核心任務轉換為具體的 todo 項目
3. **設置優先級** - 根據任務重要性和依賴關係設置優先級
4. **創建 Todo 列表** - 使用 todo_write 工具創建結構化的 todo 列表
5. **執行工作流程** - 按 todo 列表順序執行任務，及時更新狀態
</process_steps>

<requirements>
- 每個主要階段都應該有對應的 todo 項目
- 關鍵驗證檢查點必須包含在 todo 列表中
- 僅記錄白金級實踐，確保品質門檻
- 在執行過程中及時更新 todo 狀態
</requirements>
</todo_list_creation>
</execution_protocol>

# Separator line, following is original workflow content
---
## 上下文摘要機制

<context-summarization>
**目的**：每階段完成後輸出結構化摘要以節省上下文。

**方法**：使用 `{project_root}/sunnycore/po/templates/stage-summary-tmpl.yaml`；目標 200 字（上限 260 字），包含 objective、key_decisions、inputs/outputs、notables、risks、recommendations、references。

**保留策略**：保留最近 2 個完整摘要；較舊摘要壓縮為 1–2 行要點；丟棄 2 個階段前原始細節並僅傳遞 open_risks、pending_decisions、followups。
<!-- context-summarization>


workflow_name: "unified-knowledge-curation-workflow"
version: "2.2.0"
description: "Curate excellent practices and error patterns from review reports and completion reports, only record platinum level practices"

# Workflow execution settings
execution_settings:
  deterministic: true
  parallel_enabled: true
  max_parallel_tasks: 10
  batch_size: 7
  cache_enabled: true
  fail_fast: false  # Record errors but do not interrupt

# Prerequisites check
prerequisites:
  required_files:
    # Core configuration files
    - path: "{project_root}/sunnycore/po/templates/knowledge-lessons-tmpl.yaml"
      type: "template"
      critical: false  # Log warning if missing and continue
    - path: "{project_root}/sunnycore/po/enforcement/po_knowledge-curator-enforcement.md"
      type: "enforcement"
      critical: false

  optional_directories:
    # Source data directories (may not exist)
    - path: "{{project_root}}/docs/implementation-review/"
      type: "source"
      pattern: "*.md"
    - path: "{{project_root}}/docs/completion-reports/"
      type: "source"
      pattern: "*-completion.md"

  validation_rules:
    - rule: "project_root_resolved"
      description: "project_root must resolve to valid path"
    - rule: "output_directory_writable"
      description: "{{project_root}}/docs/knowledge/ must be writable"

# Main execution stages
stages:

  # Stage 1: Environment preparation and deterministic setting
  - name: "preparation"
    description: "Load settings and prepare execution environment"
    parallel: false
    steps:
      - name: "load_template"
        action: "read_file"
        target: "{project_root}/sunnycore/po/templates/knowledge-lessons-tmpl.yaml"
        required: false
        on_failure: "log_warning"

      - name: "load_enforcement"
        action: "read_file"
        target: "{project_root}/sunnycore/po/enforcement/po_knowledge-curator-enforcement.md"
        required: false
        on_failure: "log_warning"

      - name: "verify_output_path"
        action: "ensure_directory"
        target: "{{project_root}}/docs/knowledge/"
        permissions: "write"

  # Stage 2: Source data scanning and collection
  - name: "source_discovery"
    description: "Synchronously scan source files and collect raw data"
    parallel: true
    depends_on: ["preparation"]
    steps:
      - name: "scan_review_reports"
        action: "glob_search"
        target: "{{project_root}}/docs/implementation-review/*.md"
        extract_patterns:
          - "error_log"
          - "findings"
          - "quality_assessment"
        on_empty: "log_info"  # Not an error if no files

      - name: "scan_completion_reports"
        action: "glob_search"
        target: "{{project_root}}/docs/completion-reports/*-completion.md"
        extract_patterns:
          - "implementation_maturity"
          - "quality_assessment"
          - "summary_score"
        on_empty: "log_info"

      - name: "load_existing_knowledge"
        action: "read_file"
        target: "{{project_root}}/docs/knowledge/engineering-lessons.md"
        required: false
        on_failure: "create_new"

  # Stage 3: Quality filtering and data preprocessing
  - name: "quality_filtering"
    description: "Filter data according to quality standards, emphasize platinum level"
    parallel: false
    depends_on: ["source_discovery"]
    steps:
      - name: "extract_platinum_practices"
        action: "filter_practices"
        criteria:
          - "implementation_maturity >= 'platinum'"
          - "quality_assessment.summary_score >= 4"
          - "qa_positive_feedback = true"
        output: "platinum_practices_list"
        minimum_threshold: 0  # Allow empty results

      - name: "categorize_error_patterns"
        action: "analyze_errors"
        source: "error_log"
        severity_order: ["blocker", "high", "medium", "low"]
        grouping: "pattern_similarity"
        output: "categorized_errors"

      - name: "validate_evidence_links"
        action: "verify_links"
        targets: ["file_paths", "pr_links", "commit_hashes"]
        on_broken_link: "log_warning"

  # Stage 4: Pattern identification and analysis
  - name: "pattern_analysis"
    description: "Identify error patterns and successful practice deep patterns"
    parallel: true
    depends_on: ["quality_filtering"]
    steps:
      - name: "identify_error_patterns"
        action: "pattern_recognition"
        source: "categorized_errors"
        techniques:
          - "frequency_analysis"
          - "co_occurrence_analysis"
          - "root_cause_clustering"
        output: "error_patterns"

      - name: "analyze_success_patterns"
        action: "pattern_recognition"
        source: "platinum_practices_list"
        techniques:
          - "context_analysis"
          - "outcome_correlation"
          - "replicability_assessment"
        output: "success_patterns"

      - name: "cross_reference_patterns"
        action: "cross_analysis"
        sources: ["error_patterns", "success_patterns"]
        identify: "prevention_opportunities"
        output: "prevention_matrix"

  # Stage 5: Knowledge structuring and organization
  - name: "knowledge_structuring"
    description: "Organize analysis results into three-layer knowledge structure"
    parallel: false
    depends_on: ["pattern_analysis"]
    steps:
      - name: "create_quick_reference"
        action: "generate_structure"
        template: "emergency_lookup_table"
        source: "error_patterns"
        criteria: "frequency_and_severity"
        max_entries: 20
        format: "symptoms_to_solutions"

      - name: "build_detailed_analysis"
        action: "generate_structure"
        template: "comprehensive_analysis"
        sources: ["error_patterns", "success_patterns", "prevention_matrix"]
        include_evidence: true
        include_case_studies: true

      - name: "design_prevention_guides"
        action: "generate_structure"
        template: "prevention_framework"
        source: "prevention_matrix"
        focus: "proactive_measures"
        include_tools: true
        include_checklists: true

  # Stage 6: Output generation and formatting
  - name: "output_generation"
    description: "Generate final knowledge document according to template"
    parallel: false
    depends_on: ["knowledge_structuring"]
    steps:
      - name: "populate_template"
        action: "template_fill"
        template_source: "knowledge-lessons-tmpl.yaml"
        data_sources:
          - "quick_reference"
          - "detailed_analysis"
          - "prevention_guides"
        placeholder_handling: "mark_as_na_with_reason"

      - name: "add_metadata"
        action: "add_metadata"
        fields:
          - "generation_timestamp"
          - "source_file_count"
          - "platinum_practices_count"
          - "error_patterns_count"
          - "evidence_quality_score"

      - name: "apply_formatting"
        action: "format_document"
        standards:
          - "consistent_headers"
          - "unified_code_blocks"
          - "standardized_links"
          - "sorted_lists"

  # Stage 7: Quality verification and output
  - name: "quality_validation"
    description: "Verify output quality and write to file"
    parallel: false
    depends_on: ["output_generation"]
    steps:
      - name: "validate_content"
        action: "content_validation"
        checks:
          - "no_placeholders_remaining"
          - "evidence_links_valid"
          - "structure_compliance"
          - "minimum_content_length"
        failure_action: "log_and_continue"

      - name: "validate_platinum_threshold"
        action: "threshold_validation"
        criteria:
          - rule: "platinum_practices_only"
            description: "Ensure only platinum level practices are recorded"
            validation: "implementation_maturity >= 'platinum'"
          - rule: "evidence_supported"
            description: "Ensure 100% of entries have evidence support"
            validation: "evidence_links_present = true"

      - name: "write_output"
        action: "write_file"
        target: "{{project_root}}/docs/knowledge/engineering-lessons.md"
        backup: true
        backup_path: "{{project_root}}/docs/knowledge/engineering-lessons-{{timestamp}}.md"

      - name: "update_index"
        action: "update_index"
        target: "{{project_root}}/docs/knowledge/index.md"
        add_entry: "engineering-lessons.md"
        include_metadata: true

# Data quality standards
quality_standards:
  platinum_practices:
    minimum_score: 4.0
    required_maturity: "platinum"
    evidence_requirement: "mandatory"
    success_rate_threshold: 0.8

  error_patterns:
    minimum_frequency: 2
    severity_threshold: "medium"
    reproducibility_requirement: true

  evidence_links:
    validity_check: true
    accessibility_check: true
    freshness_threshold_days: 180

# Error handling strategies
error_handling:
  source_file_missing:
    action: "log_warning"
    continue: true
    message: "Source files missing, continue with existing data"

  template_load_failure:
    action: "use_fallback"
    fallback: "minimal_template"
    continue: true

  evidence_link_broken:
    action: "mark_as_questionable"
    continue: true
    include_in_validation_warnings: true

  platinum_threshold_unmet:
    action: "filter_out"
    continue: true
    log_filtered_items: true

# Parallel processing strategies
parallelization:
  source_discovery:
    max_concurrent: 5
    timeout_per_task: 30

  pattern_analysis:
    max_concurrent: 3
    shared_cache: true

  validation:
    sequential_required: true
    reason: "Ensure data consistency"

# Caching strategies
caching:
  source_files:
    strategy: "content_hash"
    ttl_hours: 24
    invalidation_triggers: ["file_modification", "size_change"]

  analysis_results:
    strategy: "dependency_hash"
    ttl_hours: 12
    cache_key_components: ["source_hash", "template_version", "config_hash"]

# Output validation rules
validation_rules:
  content_quality:
    - rule: "no_empty_sections"
      severity: "warning"
    - rule: "evidence_links_present"
      severity: "error"
      threshold: 100  # 100% of entries must have evidence
    - rule: "platinum_only"
      severity: "error"
      description: "Only allow platinum level practices"
    - rule: "consistent_formatting"
      severity: "warning"
    - rule: "sorted_lists"
      severity: "info"

  format_compliance:
    - rule: "template_structure_followed"
      severity: "error"
    - rule: "consistent_formatting"
      severity: "warning"
    - rule: "sorted_lists"
      severity: "info"

# Success metrics
success_metrics:
  process_metrics:
    - "source_files_processed"
    - "patterns_identified"
    - "platinum_practices_collected"
    - "error_patterns_categorized"

  quality_metrics:
    - "evidence_link_validity_rate"
    - "platinum_practice_ratio"
    - "knowledge_freshness_score"
    - "cross_reference_accuracy"

  impact_metrics:
    - "knowledge_base_growth"
    - "pattern_coverage_improvement"
    - "prevention_opportunity_identification"

# Post-processing actions
post_processing:
  knowledge_base_maintenance:
    - action: "remove_outdated_entries"
      criteria: "last_updated > 1_year AND no_recent_validation"
    - action: "merge_similar_patterns"
      threshold: "similarity_score > 0.8"
    - action: "update_cross_references"
      scope: "all_related_entries"

  continuous_improvement:
    - action: "analyze_usage_patterns"
      source: "access_logs"
    - action: "identify_gaps"
      method: "frequency_vs_coverage_analysis"
    - action: "suggest_collection_priorities"
      based_on: "gap_analysis_results"

# Execution report template
execution_report:
  summary:
    - "total_sources_processed"
    - "platinum_practices_identified"
    - "error_patterns_discovered"
    - "prevention_opportunities_created"

  details:
    - "source_file_breakdown"
    - "quality_filtering_results"
    - "pattern_analysis_insights"
    - "evidence_validation_report"

  recommendations:
    - "knowledge_collection_priorities"
    - "process_improvement_suggestions"
    - "tool_enhancement_opportunities"
