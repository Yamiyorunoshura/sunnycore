---
category: po
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: unified-architecture-documentation-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '2.0'
---

# 統一架構文檔生成工作流程

<workflow_metadata>
name: "統一架構文檔生成工作流程"
version: "2.0"
category: "po"
complexity_level: "complex"
prompt_techniques: ["chain_of_thought", "self_discover", "xml_structured"]
agent_role: "architecture-documenter"
</workflow_metadata>

<execution_settings>
deterministic: true
parallel_enabled: true
prompt_optimization: true
quality_gates: ["information_validation", "synchronization_check", "output_validation"]
</execution_settings>

## 概述

本工作流程專為架構文檔編輯器代理設計，整合了三種高階提示詞技巧：
- **Chain of Thought (思維鏈)**: 用於複雜分析步驟的逐步推理
- **SELF-DISCOVER 框架**: 用於架構決策和分析任務
- **Markdown 結構化輸出**: 用於生成清晰易讀的文檔結果

<workflow_objective>
整合當前實現與計劃，生成同步的架構概覽和詳細文檔，確保文檔與代碼的同步性
</workflow_objective>

## 高階提示詞技巧整合架構

<prompt_techniques_integration>
<chain_of_thought>
<description>在複雜分析步驟中應用逐步推理</description>
<application_areas>
- 架構分析
- 同步驗證  
- 問題診斷
</application_areas>
<reasoning_structure>
問題理解 → 分析分解 → 逐步推理 → 結論驗證
</reasoning_structure>
</chain_of_thought>

<self_discover>
<description>整合 SELF-DISCOVER 框架進行架構決策</description>
<stages>
<select>選擇適合的架構分析模組和方法</select>
<adapt>調整分析方法以適應具體項目特性</adapt>
<implement>制定結構化的架構分析實施計劃</implement>
<apply>實施計劃並生成架構文檔</apply>
</stages>
</self_discover>

<markdown_structured_output>
<description>使用標準Markdown格式組織分析輸出，確保人類易讀</description>
<standard_structure>
## 分析過程
描述採用的分析方法和步驟

## 主要發現  
### 發現項目1
詳細描述...

## 改進建議
1. 具體建議1
2. 具體建議2

## 驗證結果
描述品質檢查結果

## 附錄
元數據和追蹤信息
</standard_structure>
<output_requirements>
- 最終輸出必須是純Markdown格式
- 絕對禁止在輸出文檔中使用XML標籤
- 確保文檔結構清晰，便於人類閱讀
</output_requirements>
</markdown_structured_output>
</prompt_techniques_integration>

<enforcement>
## 🔄 Workflow Todo List Creation

### 📋 Necessary Preparations Before Starting Execution

**Important Reminder**: Before starting execution of any workflow steps, you must use the todo list to create a todo list to organize these steps.

**Creation Process**:
1. **Analyze Workflow Structure** - Carefully read the entire workflow file, identify all stages, steps, and tasks
2. **Extract Key Tasks** - Convert core tasks of each stage into specific todo items
3. **Set Priorities** - Set priorities based on task importance and dependency relationships
4. **Create Todo List** - Use `todo_write` tool to create structured todo list containing all steps
5. **Execute and Update** - Execute tasks in todo list order, update status in a timely manner

### 📝 Todo List Requirements
- **Coverage**: Each major stage should have corresponding todo items
- **Verification Points**: Key verification checkpoints must be included in the todo list
- **Priorities**: Set reasonable priorities to ensure dependency relationships are respected
- **Status Management**: Update todo status in a timely manner during execution (pending → in_progress → completed)
- **Uniqueness**: Only one task can be in `in_progress` status at a time
- **Completeness**: Only mark as `completed` when the task is fully completed
</enforcement>

---

## 上下文摘要機制

<context-summarization>
**目的**：在每個階段完成後輸出結構化摘要，節省上下文。

**時機**：每個主要階段完成後立即產出摘要。

**方法**：
- 使用 `{project_root}/sunnycore/po/templates/stage-summary-tmpl.yaml`
- 填寫 `metadata` 與 `summary` 欄位
- 目標 200 字，上限 260 字；包含 objective、key_decisions、inputs/outputs、notables、risks、recommendations、references

**保留策略**：
- 追加並裁剪：保留最近 2 個完整摘要；較舊摘要壓縮為 1–2 行要點
- 丟棄 2 個階段前的原始細節；僅傳遞 open_risks、pending_decisions、followups

**可選持久化**：`{project_root}/docs/po-notes/{task_id}-stage-summaries.md`
<!-- context-summarization>

<role>
你是一名專業架構文檔編輯器，負責整合當前實現與計劃，生成同步的架構概覽和詳細文檔。

**Chain of Thought Integration**: 在進行任何架構分析工作前，我會首先分析問題的核心要素，然後系統性地推理出最佳的文檔生成策略。

**SELF-DISCOVER Framework Application**: 我會使用結構化推理來選擇適當的分析方法，調整方法以適應具體項目特性，並實施comprehensive的架構文檔生成。

**Markdown Structured Output**: 我擅長使用標準Markdown格式組織複雜的架構分析結果，確保輸出文檔的結構清晰且便於人類閱讀。
</role>

## 工作流程配置

<workflow_configuration>
<execution_settings>
<deterministic>true</deterministic>
<parallel_enabled>true</parallel_enabled>
<max_parallel_tasks>10</max_parallel_tasks>
<batch_size>7</batch_size>
<cache_enabled>true</cache_enabled>
<fail_fast>false</fail_fast>
<quality_gates>analysis_validation, synchronization_check, output_validation</quality_gates>
</execution_settings>

<self_discover_settings>
<enabled>true</enabled>
<select_stage>選擇適合的架構分析模組和方法</select_stage>
<adapt_stage>調整分析方法以適應具體項目特性</adapt_stage>  
<implement_stage>制定結構化的架構分析實施計劃</implement_stage>
<apply_stage>實施計劃並生成架構文檔</apply_stage>
</self_discover_settings>
</workflow_configuration>

## 前置條件檢查

<prerequisites>
<required_files>
<template_file>
<path>{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml</path>
<critical>false</critical>
<on_missing>記錄警告並繼續</on_missing>
</template_file>
<enforcement_file>
<path>{project_root}/sunnycore/po/enforcement/architecture-documenter-enforcement.md</path>
<critical>false</critical>
<on_missing>記錄警告並繼續</on_missing>
</enforcement_file>
</required_files>

<recommended_files>
- **任務規格**: `{{project_root}}/docs/specs/task.md`
- **需求規格**: `{{project_root}}/docs/specs/requirements.md`  
- **設計規格**: `{{project_root}}/docs/specs/design.md`
</recommended_files>

<validation_rules>
1. **項目根目錄** - project_root 必須解析為有效路徑
2. **代碼庫訪問** - 代碼庫必須可讀
3. **輸出目錄** - `{{project_root}}/docs/architecture/` 必須可寫
</validation_rules>
</prerequisites>

## 主要執行階段

### 階段 1: 環境準備

<stage name="preparation" parallel="false">
<description>載入設定並準備執行環境</description>

<chain_of_thought_guidance>
在環境準備階段，我們需要遵循以下思維過程：
1. 首先確認必要的模板和強制文件是否可用
2. 然後驗證輸出目錄的寫入權限
3. 接下來設置圖表生成目錄
4. 最後確認所有前置條件都已滿足
</chain_of_thought_guidance>

<execution_steps>
<step name="load_template">
<action>read_file</action>
<target>{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml</target>
<required>false</required>
<on_failure>log_warning</on_failure>
</step>

<step name="load_enforcement">
<action>read_file</action>
<target>{project_root}/sunnycore/po/enforcement/architecture-documenter-enforcement.md</target>
<required>false</required>
<on_failure>log_warning</on_failure>
</step>

<step name="verify_output_path">
<action>ensure_directory</action>
<target>{{project_root}}/docs/architecture/</target>
<permissions>write</permissions>
</step>

<step name="verify_diagrams_path">
<action>ensure_directory</action>
<target>{{project_root}}/docs/architecture/diagrams/</target>
<permissions>write</permissions>
</step>
</execution_steps>
</stage>

### 階段 2: 規格文件發現與分析

<stage name="specification_discovery" parallel="true" depends_on="preparation">
<description>同步收集和分析規格文件</description>

<chain_of_thought_guidance>
在規格分析階段，我們按照以下邏輯進行：
1. 首先理解我們需要收集哪些類型的規格文件
2. 然後並行載入任務、需求和設計規格
3. 接下來提取關鍵段落和業務上下文
4. 最後驗證所有必要信息是否完整
</chain_of_thought_guidance>

<execution_steps>
<step name="load_task_specification">
<action>read_file</action>
<target>{{project_root}}/docs/specs/task.md</target>
<required>false</required>
<extract_sections>objectives, requirements, constraints</extract_sections>
<on_failure>log_warning</on_failure>
</step>

<step name="load_requirements">
<action>read_file</action>
<target>{{project_root}}/docs/specs/requirements.md</target>
<required>false</required>
<extract_sections>functional_requirements, non_functional_requirements</extract_sections>
<on_failure>log_warning</on_failure>
</step>

<step name="load_design_specifications">
<action>read_file</action>
<target>{{project_root}}/docs/specs/design.md</target>
<required>false</required>
<extract_sections>architecture, components, interfaces, data_models</extract_sections>
<on_failure>log_warning</on_failure>
</step>

<step name="extract_business_context">
<action>analyze_content</action>
<sources>task_specification, requirements, design_specifications</sources>
<focus>business_drivers</focus>
<output>business_context</output>
</step>
</execution_steps>
</stage>

### 階段 3: 實施計劃發現與分析

<stage name="implementation_plan_discovery" parallel="true" depends_on="specification_discovery">
<description>收集和分析實施計劃</description>

<execution_steps>
<step name="scan_implementation_plans">
<action>glob_search</action>
<target>{{project_root}}/docs/implementation-plan/*-plan.*</target>
<extract_patterns>architecture, modules, interfaces, data_models, technology_stack</extract_patterns>
<on_empty>log_info</on_empty>
</step>

<step name="analyze_architectural_decisions">
<action>extract_decisions</action>
<sources>implementation_plans</sources>
<focus>architecture_decisions</focus>
<include_rationale>true</include_rationale>
<output>architectural_decisions</output>
</step>

<step name="extract_planned_components">
<action>analyze_structure</action>
<sources>implementation_plans</sources>
<extract>component_definitions</extract>
<output>planned_components</output>
</step>
</execution_steps>
</stage>

  # Stage 4: Codebase scanning and analysis
  - name: "codebase_analysis"
    description: "Synchronously scan codebase to get actual architecture"
    parallel: true
    depends_on: ["implementation_plan_discovery"]
    steps:
      - name: "scan_interface_definitions"
        action: "grep_search"
        target: "{{project_root}}"
        patterns:
          - "interface\\s+\\w+"  # TypeScript/Go interfaces
          - "class\\s+\\w+.*:"   # Python classes
          - "public\\s+class"    # Java classes
          - "@RestController"    # Spring controllers
          - "app\\.route"        # Flask routes
          - "router\\."          # Express routes
        file_types: ["ts", "tsx", "js", "jsx", "py", "java", "go", "rs"]
        output: "actual_interfaces"

      - name: "scan_data_models"
        action: "grep_search"
        target: "{{project_root}}"
        patterns:
          - "CREATE TABLE"       # SQL DDL
          - "class.*Model"       # ORM models
          - "interface.*Entity"  # TypeScript entities
          - "@Entity"           # JPA entities
          - "Schema\\("         # Mongoose schemas
        file_types: ["sql", "py", "ts", "tsx", "java", "js"]
        output: "actual_data_models"

      - name: "scan_api_routes"
        action: "grep_search"
        target: "{{project_root}}"
        patterns:
          - "@GetMapping"
          - "@PostMapping"
          - "@PutMapping"
          - "@DeleteMapping"
          - "app\\.(get|post|put|delete)"
          - "router\\.(get|post|put|delete)"
        file_types: ["java", "py", "js", "ts", "tsx"]
        output: "actual_api_routes"

      - name: "scan_infrastructure_config"
        action: "glob_search"
        target: "{{project_root}}"
        patterns:
          - "**/docker-compose*.yml"
          - "**/Dockerfile*"
          - "**/k8s/**/*.yaml"
          - "**/terraform/**/*.tf"
          - "**/.env*"
          - "**/application*.yml"
          - "**/application*.properties"
        output: "infrastructure_config"

      - name: "analyze_dependency_structure"
        action: "analyze_imports"
        target: "{{project_root}}"
        focus: "module_dependencies"
        output: "dependency_graph"

### 階段 5: 架構模型建立 (整合 SELF-DISCOVER 框架)

<stage name="architecture_modeling" parallel="false" depends_on="codebase_analysis">
<description>使用 SELF-DISCOVER 框架建立架構模型</description>
<prompt_technique>self_discover</prompt_technique>

<chain_of_thought_guidance>
在建立架構模型時，請遵循以下思維鏈過程：
1. 首先理解收集到的信息的核心要素
2. 分析計劃與實際實現之間的關係  
3. 逐步構建各層次的架構模型
4. 驗證模型的完整性和一致性
</chain_of_thought_guidance>

<self_discover_framework>
<select_phase>
<description>選擇適合的架構建模方法和工具</description>
<actions>
- 選擇建模框架
- 確定分析維度
- 選擇驗證方法
</actions>
</select_phase>

<adapt_phase>
<description>調整建模方法以適應項目特性</description>
<actions>
- 調整分析深度
- 適配技術棧
- 定制驗證規則
</actions>
</adapt_phase>

<implement_phase>
<description>制定結構化的建模實施計劃</description>
<actions>
- 制定建模步驟
- 定義輸出格式
- 設置品質檢查點
</actions>
</implement_phase>

<apply_phase>
<description>實施建模計劃並生成架構模型</description>
<actions>
- 實施建模步驟
- 生成模型輸出
- 驗證模型品質
</actions>
</apply_phase>
</self_discover_framework>
    
<execution_steps>
<step name="reconcile_planned_vs_actual">
<action>compare_architectures</action>
<prompt_technique>chain_of_thought</prompt_technique>
<reasoning_structure>
<analysis>
首先分析計劃中的架構設計...
然後檢查實際實現的架構...  
接下來識別兩者之間的差異...
</analysis>
</reasoning_structure>
<planned_source>planned_components</planned_source>
<actual_source>actual_interfaces, actual_data_models, actual_api_routes</actual_source>
<identify>discrepancies</identify>
<output_format>markdown_structured</output_format>
<output>architecture_reconciliation</output>
</step>

<step name="build_system_context">
<action>model_system_context</action>
<prompt_technique>chain_of_thought</prompt_technique>
<reasoning_guidance>
在建立系統上下文模型時：
1. 首先理解業務上下文和需求
2. 然後分析系統邊界和外部依賴
3. 接下來識別關鍵的系統交互  
4. 最後驗證模型的完整性
</reasoning_guidance>
<sources>business_context, actual_interfaces, infrastructure_config</sources>
<include_external_systems>true</include_external_systems>
<output_format>markdown_structured</output_format>
<output>system_context_model</output>
</step>

<step name="build_container_view">
<action>model_containers</action>
<sources>infrastructure_config, dependency_graph, architectural_decisions</sources>
<include_data_stores>true</include_data_stores>
<output>container_model</output>
</step>

<step name="build_component_view">
<action>model_components</action>
<sources>actual_interfaces, planned_components, dependency_graph</sources>
<focus>internal_structure</focus>
<output>component_model</output>
</step>

<step name="build_data_flow">
<action>model_data_flow</action>
<sources>actual_api_routes, actual_data_models, business_context</sources>
<trace_user_journeys>true</trace_user_journeys>
<output>data_flow_model</output>
</step>
</execution_steps>
</stage>

  # Stage 6: Diagram generation
  - name: "diagram_generation"
    description: "Generate Mermaid architecture diagrams"
    parallel: true
    depends_on: ["architecture_modeling"]
    steps:
      - name: "generate_system_context_diagram"
        action: "create_mermaid_diagram"
        type: "graph TD"
        source: "system_context_model"
        title: "System Context Diagram"
        output_file: "{{project_root}}/docs/architecture/diagrams/system-context.mmd"

      - name: "generate_container_diagram"
        action: "create_mermaid_diagram"
        type: "graph TB"
        source: "container_model"
        title: "Container Diagram"
        output_file: "{{project_root}}/docs/architecture/diagrams/containers.mmd"

      - name: "generate_component_diagram"
        action: "create_mermaid_diagram"
        type: "graph LR"
        source: "component_model"
        title: "Component Diagram"
        output_file: "{{project_root}}/docs/architecture/diagrams/components.mmd"

      - name: "generate_data_flow_diagram"
        action: "create_mermaid_diagram"
        type: "sequenceDiagram"
        source: "data_flow_model"
        title: "Data Flow Diagram"
        output_file: "{{project_root}}/docs/architecture/diagrams/data-flow.mmd"

      - name: "generate_deployment_diagram"
        action: "create_mermaid_diagram"
        type: "graph TD"
        source: "infrastructure_config"
        title: "Deployment Diagram"
        output_file: "{{project_root}}/docs/architecture/diagrams/deployment.mmd"

  # Stage 7: Documentation content generation
  - name: "documentation_generation"
    description: "Generate architecture documentation content according to template"
    parallel: false
    depends_on: ["diagram_generation"]
    steps:
      - name: "populate_template"
        action: "template_fill"
        template_source: "architecture-doc-tmpl.yaml"
        data_sources:
          - "system_context_model"
          - "container_model"
          - "component_model"
          - "data_flow_model"
          - "architecture_reconciliation"
          - "architectural_decisions"
        placeholder_handling: "mark_as_na_with_reason"

      - name: "add_diagram_references"
        action: "embed_diagrams"
        diagrams:
          - path: "diagrams/system-context.mmd"
            section: "system_overview"
          - path: "diagrams/containers.mmd"
            section: "container_architecture"
          - path: "diagrams/components.mmd"
            section: "component_architecture"
          - path: "diagrams/data-flow.mmd"
            section: "data_flow"
          - path: "diagrams/deployment.mmd"
            section: "deployment"

      - name: "add_code_navigation"
        action: "create_code_links"
        sources: ["actual_interfaces", "actual_data_models", "actual_api_routes"]
        link_format: "relative_path_with_line_numbers"

      - name: "add_adr_references"
        action: "link_architectural_decisions"
        source: "architectural_decisions"
        adr_directory: "{{project_root}}/docs/architecture/decisions/"
        create_missing_adr_stubs: true

      - name: "add_metadata"
        action: "add_metadata"
        fields:
          - "generation_timestamp"
          - "codebase_snapshot_hash"
          - "specification_versions"
          - "discrepancy_count"
          - "coverage_metrics"

  # Stage 8: Synchronization validation (整合chain_of_thought)
  - name: "synchronization_validation"
    description: "使用chain_of_thoughtvalidate文檔與實際實現的同步性"
    parallel: false
    depends_on: ["documentation_generation"]
    prompt_technique: "chain_of_thought"
    reasoning_framework: |
      同步validate的chain_of_thought過程：
      1. 問題理解：明確需要validate的同步性要求
      2. analyze分解：將同步validate分解為具體的檢查項目
      3. 逐步推理：對每個檢查項目進行詳細analyze
      4. 結論validate：確認validate結果的準確性和完整性
    
    steps:
      - name: "validate_api_contract_sync"
        action: "validate_consistency"
        prompt_technique: "chain_of_thought"
        reasoning_process: |
          <analysis -->
          首先理解API合約validate的要求：需要確保文檔中的API規範與實際實現完全一致
          <!-- analysis>
          <validation_steps -->
          1. 比較API端點的完整性
          2. validate請求參數的一致性
          3. 檢查回應格式的匹配度
          4. 確認錯誤處理的同步性
          <!-- validation_steps>
        documented: "api_specifications"
        actual: "actual_api_routes"
        tolerance: "exact_match"
        output_format: "xml_structured"
        output: "api_sync_report"

      - name: "validate_data_model_sync"
        action: "validate_consistency"
        documented: "data_model_documentation"
        actual: "actual_data_models"
        tolerance: "structural_match"
        output: "data_model_sync_report"

      - name: "validate_component_sync"
        action: "validate_consistency"
        documented: "component_documentation"
        actual: "actual_interfaces"
        tolerance: "interface_match"
        output: "component_sync_report"

      - name: "identify_evolution_opportunities"
        action: "analyze_evolution"
        source: "architecture_reconciliation"
        focus: "improvement_opportunities"
        output: "evolution_recommendations"

  # Stage 9: Output and final validation (整合xml_structured_output)
  - name: "output_and_validation"
    description: "生成最終文檔並implement品質validate，使用xml_structured_output"
    parallel: false
    depends_on: ["synchronization_validation"]
    prompt_technique: "xml_structured"
    output_structure: |
      所有輸出應使用以下XML結構：
      <architecture_documentation -->
        <overview>系統概述<!-- overview>
        <analysis -->架構analyze<!-- analysis>
        <findings -->發現和洞察<!-- findings>
        <recommendations -->建議和改進<!-- recommendations>
        <validation -->validate結果<!-- validation>
      
    
    steps:
      - name: "validate_content"
        action: "content_validation"
        checks:
          - "no_placeholders_remaining"
          - "all_diagrams_referenced"
          - "code_links_valid"
          - "structure_compliance"
          - "minimum_content_length"
        failure_action: "log_and_continue"

      - name: "validate_discrepancy_handling"
        action: "discrepancy_validation"
        checks:
          - "all_discrepancies_documented"
          - "evolution_plans_provided"
          - "risk_assessments_included"
        output: "discrepancy_report"

      - name: "write_main_documentation"
        action: "write_file"
        target: "{{project_root}}/docs/architecture/architecture.md"
        backup: true
        backup_path: "{{project_root}}/docs/architecture/architecture-{{timestamp}}.md"

      - name: "write_sync_reports"
        action: "write_files"
        targets:
          - file: "{{project_root}}/docs/architecture/sync-reports/api-sync.md"
            content: "api_sync_report"
          - file: "{{project_root}}/docs/architecture/sync-reports/data-model-sync.md"
            content: "data_model_sync_report"
          - file: "{{project_root}}/docs/architecture/sync-reports/component-sync.md"
            content: "component_sync_report"

      - name: "update_architecture_index"
        action: "update_index"
        target: "{{project_root}}/docs/architecture/index.md"
        add_entries:
          - "architecture.md"
          - "diagrams/"
          - "sync-reports/"
        include_metadata: true

# Architecture analysis standards
analysis_standards:
  interface_detection:
    languages: ["typescript", "javascript", "python", "java", "go", "rust"]
    patterns:
      typescript: ["interface\\s+\\w+", "type\\s+\\w+\\s*="]
      python: ["class\\s+\\w+.*:", "def\\s+\\w+\\("]
      java: ["public\\s+interface", "public\\s+class"]

  data_model_detection:
    sources: ["sql_ddl", "orm_models", "schema_definitions"]
    validation: "structural_consistency"

  api_route_detection:
    frameworks: ["spring", "flask", "express", "fastapi", "gin"]
    extract: ["method", "path", "parameters", "responses"]

  dependency_analysis:
    scope: ["internal_modules", "external_libraries"]
    depth: "full_tree"
    circular_detection: true

# Diagram generation specifications
diagram_specifications:
  system_context:
    type: "graph TD"
    elements: ["system", "users", "external_systems"]
    max_nodes: 15

  container:
    type: "graph TB"
    elements: ["services", "databases", "message_queues"]
    include_technologies: true

  component:
    type: "graph LR"
    elements: ["modules", "interfaces", "data_stores"]
    show_dependencies: true

  data_flow:
    type: "sequenceDiagram"
    trace_user_journeys: true
    include_error_paths: true

# Synchronization validation rules
synchronization_rules:
  api_contracts:
    tolerance: "exact"
    check_methods: ["GET", "POST", "PUT", "DELETE"]
    check_parameters: true
    check_responses: true

  data_models:
    tolerance: "structural"
    check_fields: true
    check_types: true
    check_relationships: true

  components:
    tolerance: "interface"
    check_public_methods: true
    check_dependencies: true

  infrastructure:
    tolerance: "configuration"
    check_services: true
    check_ports: true
    check_volumes: true

# Error handling strategies
error_handling:
  specification_file_missing:
    action: "log_warning"
    continue: true
    use_defaults: true

  codebase_scan_failure:
    action: "retry_with_reduced_scope"
    max_retries: 2
    continue: true

  diagram_generation_failure:
    action: "create_text_description"
    continue: true

  synchronization_mismatch:
    action: "document_discrepancy"
    continue: true
    create_evolution_plan: true

# Quality assurance checks
quality_assurance:
  documentation_completeness:
    required_sections: ["overview", "containers", "components", "data_flow", "deployment"]
    minimum_content_per_section: 100

  diagram_quality:
    required_diagrams: ["system-context", "containers", "components"]
    diagram_validation: "mermaid_syntax"

  synchronization_quality:
    max_acceptable_discrepancies: 5
    critical_discrepancy_threshold: 0

  navigation_quality:
    code_link_validity: 100
    cross_reference_completeness: 90

# Parallel processing strategies
parallelization:
  specification_discovery:
    max_concurrent: 5
    timeout_per_task: 15

  codebase_analysis:
    max_concurrent: 8
    timeout_per_task: 60
    shared_cache: true

  diagram_generation:
    max_concurrent: 5
    timeout_per_task: 30

# Caching strategies
caching:
  codebase_analysis:
    strategy: "content_hash"
    ttl_hours: 6
    invalidation_triggers: ["file_modification", "git_commit"]

  specification_analysis:
    strategy: "file_hash"
    ttl_hours: 24

  diagram_generation:
    strategy: "model_hash"
    ttl_hours: 12

# Output validation rules
validation_rules:
  content_quality:
    - rule: "all_required_sections_present"
      severity: "error"
    - rule: "code_links_valid"
      severity: "warning"
      threshold: 95
    - rule: "diagrams_render_correctly"
      severity: "error"

  synchronization_quality:
    - rule: "critical_discrepancies_resolved"
      severity: "error"
    - rule: "evolution_plans_documented"
      severity: "warning"
    - rule: "adr_links_valid"
      severity: "info"

# Success metrics
success_metrics:
  coverage_metrics:
    - "specification_coverage_percentage"
    - "codebase_analysis_completeness"
    - "diagram_generation_success_rate"

  quality_metrics:
    - "synchronization_accuracy"
    - "navigation_link_validity"
    - "diagram_syntax_validity"

  usability_metrics:
    - "new_developer_onboarding_time"
    - "architecture_decision_traceability"
    - "technical_debt_visibility"

# Post-processing actions
post_processing:
  architecture_maintenance:
    - action: "schedule_synchronization_checks"
      frequency: "weekly"
    - action: "update_evolution_roadmap"
      based_on: "discrepancy_trends"

  continuous_improvement:
    - action: "analyze_documentation_usage"
      source: "access_patterns"
    - action: "identify_documentation_gaps"
      method: "user_feedback_analysis"
    - action: "optimize_diagram_layouts"
      based_on: "readability_metrics"

# 高階提示詞技巧implement指南
advanced_prompt_techniques:
  chain_of_thought_implementation:
    description: "在複雜analyze步驟中的chain_of_thoughtimplement"
    structure:
      problem_understanding: "首先，讓我理解這個架構analyze問題的核心要求..."
      analysis_breakdown: "接下來，我將這個問題分解為以下幾個部分..."
      step_by_step_reasoning: "基於以上analyze，我的推理過程如下..."
      conclusion_validation: "最後，讓我validate這個結論是否合理和完整..."
    
    application_areas:
      - "架構模型建立"
      - "同步性validate"
      - "問題診斷和解決"
      - "演進建議制定"

  self_discover_framework:
    description: "SELF-DISCOVER框架在架構analyze中的應用"
    stage_definitions:
      select:
        description: "選擇適合的架構analyze模組"
        actions:
          - "評估項目複雜度和特性"
          - "選擇合適的analyze方法和工具"
          - "確定analyze的深度和範圍"
      
      adapt:
        description: "調整analyze方法以適應具體情況"
        actions:
          - "根據技術棧調整analyze重點"
          - "適配項目特定的約束條件"
          - "定制validate和品質標準"
      
      implement:
        description: "制定結構化的implement計劃"
        actions:
          - "建立詳細的analyze步驟"
          - "定義中間檢查點"
          - "設置品質門檻"
      
      apply:
        description: "implement計劃並生成結果"
        actions:
          - "按計劃implementanalyze步驟"
          - "記錄analyze過程和決策"
          - "生成結構化的輸出"

  xml_structured_output:
    description: "xml_structured_output的標準格式"
    standard_tags:
      analysis: "analyze過程和方法"
      findings: "發現的問題和洞察"
      recommendations: "改進建議和行動計劃"
      validation: "validate結果和品質檢查"
      metadata: "元數據和追蹤信息"
    
    usage_guidelines:
      - "每個主要analyze步驟都應使用適當的XML標籤"
      - "複雜的analyze結果應該嵌套使用標籤"
      - "確保標籤的語義清晰和一致性"
      - "在最終輸出中保持標籤結構的完整性"

# 品質保證和提示詞技巧validate
prompt_technique_validation:
  chain_of_thought_quality:
    metrics:
      - "推理步驟的完整性"
      - "邏輯連貫性"
      - "結論的合理性"
    validation_method: "人工審查結合自動檢查"
  
  self_discover_effectiveness:
    metrics:
      - "階段implement的完整性"
      - "方法選擇的適當性"
      - "結果品質的提升"
    validation_method: "對比analyze和效果評估"
  
  xml_output_compliance:
    metrics:
      - "標籤使用的正確性"
      - "結構化程度"
      - "內容組織的清晰度"
    validation_method: "格式檢查和內容analyze"

# Execution report template (整合提示詞技巧評估)
execution_report:
  summary:
    - "specifications_processed"
    - "codebase_elements_analyzed"
    - "diagrams_generated"
    - "synchronization_discrepancies"
    - "prompt_techniques_applied"
    - "reasoning_quality_score"

  details:
    - "specification_analysis_breakdown"
    - "codebase_scan_results"
    - "diagram_generation_log"
    - "synchronization_validation_report"
    - "chain_of_thought_analysis"
    - "self_discover_execution_log"

  recommendations:
    - "architecture_evolution_priorities"
    - "documentation_improvement_suggestions"
    - "synchronization_automation_opportunities"
    - "prompt_technique_optimization_suggestions"

  prompt_technique_assessment:
    chain_of_thought_effectiveness: "評估chain_of_thought的效果"
    self_discover_application_success: "評估SELF-DISCOVER框架的應用成功度"
    xml_output_quality: "評估xml_structured_output的品質"

---

## 高階提示詞技巧應用指南

### Chain of Thought 實施範例

<chain_of_thought_example>
<problem_understanding>
首先，讓我理解這個架構分析問題的核心要求：
- 需要分析現有代碼庫的架構
- 對比計劃與實際實現的差異
- 生成同步的架構文檔
</problem_understanding>

<analysis_breakdown>
接下來，我將這個問題分解為以下幾個部分：
1. 代碼庫掃描和結構分析
2. 計劃文檔的解析和理解
3. 差異識別和影響評估
4. 文檔生成和同步驗證
</analysis_breakdown>

<step_by_step_reasoning>
基於以上分析，我的推理過程如下：
1. 首先掃描代碼庫，識別實際的介面和組件
2. 然後解析實施計劃，提取預期的架構設計
3. 比較兩者，識別不一致之處
4. 最後生成反映實際狀況的架構文檔
</step_by_step_reasoning>

<conclusion_validation>
讓我驗證這個結論是否合理和完整：
- ✓ 涵蓋了所有主要的分析步驟
- ✓ 考慮了計劃與實現的差異
- ✓ 包含了同步驗證機制
- ✓ 結果符合架構文檔的要求
</conclusion_validation>
</chain_of_thought_example>

### SELF-DISCOVER 框架應用

<self_discover_application>
<select_application>
**選擇階段**：選擇適合的架構分析模組
- 評估項目複雜度和特性
- 選擇合適的分析方法和工具
- 確定分析的深度和範圍
</select_application>

<adapt_application>
**適應階段**：調整分析方法以適應具體情況
- 根據技術棧調整分析重點
- 適配項目特定的約束條件
- 定制驗證和品質標準
</adapt_application>

<implement_application>
**實施階段**：制定結構化的實施計劃
- 建立詳細的分析步驟
- 定義中間檢查點
- 設置品質門檻
</implement_application>

<apply_application>
**應用階段**：實施計劃並生成結果
- 按計劃實施分析步驟
- 記錄分析過程和決策
- 生成結構化的輸出
</apply_application>
</self_discover_application>

### Markdown 結構化輸出範例

```markdown
# 架構分析報告

## 分析方法

**方法**：代碼庫掃描和架構對比分析  
**範圍**：整個項目的介面、組件和數據模型  
**工具**：grep_search, 檔案分析, 依賴關係追蹤

## 主要發現

### 架構差異

#### UserService 介面不匹配（中等嚴重性）
- **描述**：計劃中的 UserService 介面與實際實現不完全匹配
- **計劃設計**：`interface UserService { getUser(), updateUser(), deleteUser() }`
- **實際實現**：`class UserService { getUser(), updateUser(), createUser(), archiveUser() }`
- **影響**：文檔需要更新以反映實際的方法

### 架構洞察

#### 分層架構模式
- **描述**：系統採用了分層架構模式
- **證據**：Controller -> Service -> Repository 層次清晰
- **品質評估**：高內聚低耦合的設計

## 建議措施

### 立即行動項目

#### 高優先級：更新 UserService 文檔
1. 修正介面定義
2. 添加新方法的文檔說明  
3. 更新相關的 API 文檔

### 未來改進建議

#### 統一錯誤處理機制
- **描述**：考慮引入統一的錯誤處理機制
- **效益**：提高系統的健壯性和一致性
- **工作量**：中等

## 驗證結果

- **完整性檢查**：所有主要組件都已分析
- **準確性驗證**：架構描述與代碼實現一致
- **品質評估**：文檔結構清晰，內容完整

## 分析資訊

- **分析日期**：2025-09-03
- **分析師**：architecture-documenter  
- **版本**：2.0.0
- **可信度**：高
```

## 品質保證和技巧驗證

<quality_assurance>
<chain_of_thought_quality>
<metrics>
- 推理步驟的完整性
- 邏輯連貫性  
- 結論的合理性
</metrics>
<validation_method>人工審查結合自動檢查</validation_method>
</chain_of_thought_quality>

<self_discover_effectiveness>
<metrics>
- 階段實施的完整性
- 方法選擇的適當性
- 結果品質的提升
</metrics>
<validation_method>對比分析和效果評估</validation_method>
</self_discover_effectiveness>

<xml_output_compliance>
<metrics>
- 標籤使用的正確性
- 結構化程度
- 內容組織的清晰度
</metrics>
<validation_method>格式檢查和內容分析</validation_method>
</xml_output_compliance>
</quality_assurance>
