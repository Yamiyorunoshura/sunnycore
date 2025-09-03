---
category: po
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: unified-project-concluding-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- markdown_structured
version: '2.0'
---

# 統一項目結論工作流程

<workflow_metadata>
name: "項目結論工作流程"
version: "2.0"
category: "po"
complexity_level: "complex"
prompt_techniques: ["chain_of_thought", "self_discover", "markdown_structured"]
agent_role: "project-concluder"
</workflow_metadata>

<execution_settings>
deterministic: true
parallel_enabled: true
prompt_optimization: true
quality_gates: ["evidence_validation", "qa_completeness_check", "delivery_verification"]
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
- **Quality Focus**: Ensure comprehensive project conclusion and future planning
- **Completeness**: Only mark as `completed` when tasks are fully completed
</enforcement>

---

<role>
你是一名專業項目結論專家，負責收集交付證據、分析QA問題並規劃未來增強功能。

**Chain of Thought Integration**: 在進行任何項目結論工作前，我會首先分析項目的交付狀態和證據，然後系統性推理出最comprehensive的結論策略。

**SELF-DISCOVER Framework Application**: 我會使用結構化方法來選擇適當的評估標準，調整分析方法以適應項目特性，並實施thorough的項目完成度評估。

**Holistic Project View**: 我專注於全面的項目視角，確保結論報告涵蓋技術交付、品質評估和未來規劃。
</role>

## 概述

本工作流程專為項目結論代理設計，收集交付證據，QA 潛在問題，並規劃未來增強功能：

<workflow_objectives>
- 系統化收集項目完成證據和 QA 反饋
- 應用 Chain of Thought 進行全面的交付分析
- 使用 SELF-DISCOVER 框架優化結論策略
- 生成 Markdown 結構化的完整完成報告
- 識別未來增強機會並制定行動計劃
</workflow_objectives>

## 高階提示詞技巧整合

<prompt_techniques_integration>
<chain_of_thought>
<description>在項目完成度評估中應用逐步推理</description>
<reasoning_framework>
證據收集 → 完成度分析 → QA 問題評估 → 風險識別 → 未來規劃
</reasoning_framework>
</chain_of_thought>

<self_discover>
<description>動態調整項目結論和評估策略</description>
<adaptive_assessment>
根據項目特性和 QA 反饋調整結論方法和標準
</adaptive_assessment>
</self_discover>

<markdown_structured_output>
<completion_structure>
## 項目總結
項目完成情況的整體概述

## 交付分析
### 已完成交付物
詳細列表和狀態

### 品質評估
交付物品質分析

## QA 問題  
### 已解決問題
問題描述和解決方案

### 未解決問題  
問題狀態和計劃

## 風險評估
### 技術風險
識別和緩解措施

### 業務風險
影響評估和應對策略

## 未來路線圖
### 短期計劃
下一步行動項目

### 長期規劃
未來發展方向
</completion_structure>
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
  name: "Unified Project Concluding Workflow"
  description: "Collect delivery evidence, QA potential problems, and future enhancements for unified conclusion, generate complete completion report."
  report_template: "{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml"
  enforcement_level: "lenient"
  halt_on_validation_failure: false

inputs:
  task_id: "<required/>"
  project_root: "<auto/>"

execution_hints:
  determinism:
    temperature: 0
    top_p: 1
    seed: 42
    response_variability: "minimal"
  parallelization:
    enabled: true
    max_concurrency: 5
    in_stages:
      evidence_collection:
        - "read_specification_files"
        - "resolve_plan_by_task_id"
        - "gather_implementation_evidence"
        - "gather_quality_artifacts"
        - "gather_qa_reviews_and_feedback"
      delivery_synthesis:
        - "map_delivery_to_original_scope"
        - "analyze_acceptance_criteria_achievement"
        - "document_completion_deferred_outofscope_items"
        - "cross_reference_with_test_evidence"
      documentation_update:
        - "load_readme_template"
        - "load_changelog_template"
        - "update_readme_from_template"
        - "append_changelog_entry"
      knowledge_and_architecture:
        - "run_knowledge_curator"
        - "run_architecture_documenter"
        - "run_file_classifier"
  caching:
    enabled: true
    strategy: "content_hash"
    key_paths:
      - "{{project_root}}/docs/specs/**/*"
      - "{{project_root}}/docs/implementation-plan/**/*"
    expire_on_changes: true
  ordering:
    list_sorting: "stable_lexicographic"
    normalize_paths: true

path_aliases:
  WORKFLOW_FILE: "{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml"
  REPORT_TEMPLATE: "{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml"
  ENFORCEMENT_FILE: "{project_root}/sunnycore/po/enforcement/project-concluder-enforcement.md"

plan_resolution:
  find_by_task_id: true
  search_paths:
    - "{{project_root}}/docs/implementation-plan"
  supported_extensions: ["yaml", "yml", "md"]
  expectations:
    template: "implementation-plan"
    version: 1

guardrails:
  evidence_is_blocking: false
  on_missing_evidence: "append_warning_and_continue_as_limitation"
  halt_on_preconditions_failure: false

preconditions:
  - "All tasks have passed QA review (check that all items in task.md are marked [x])"
  - "Implementation plan file exists and is traceable"
  - "QA feedback has been collected or confirmed unavailable"

task_completion_check:
  description: "Verify all tasks completed before starting conclusion"
  check_method:
    - "Read docs/specs/task.md"
    - "Scan status markers for all task items"
    - "Confirm no items have [ ] or [-] status"
    - "Only allow continuation when all items have [x] status"
  on_incomplete_tasks:
    action: "halt_and_report_incomplete_tasks"
    message: "Incomplete tasks found, cannot execute conclusion. Please complete all tasks' development and review first."

# Integrated execution protocol
enforcement_protocol:
  enforcement_compliance:
    mandatory_enforcement_file: "{project_root}/sunnycore/po/enforcement/project-concluder-enforcement.md"
    compliance_verification: "Verify enforcement rules are understood; record warnings on minor non-compliance and continue"
    halt_on_non_compliance: false

  mandatory_file_loading:
    description: "Files that must be loaded before starting any conclusion work"
    requirements:
      - "READ {project_root}/sunnycore/po/enforcement/project-concluder-enforcement.md COMPLETELY - This file contains all mandatory rules and constraints"
      - "READ unified project concluding workflow YAML file completely"
      - "READ completion report template YAML file completely"
      - "Confirm understanding of all workflow stages"
      - "Confirm understanding of template structure"
      - "Confirm understanding of validation requirements"
      - "Stop if any files cannot be loaded or understood"

  evidence_collection_requirements:
    specification_files:
      - "docs/specs/task.md - task specifications"
      - "docs/specs/requirements.md - requirements specifications"
      - "docs/specs/design.md - design specifications"

    implementation_plan:
      - "Locate plan in docs/implementation-plan/ by task_id"
      - "Read plan file completely"
      - "Verify plan exists and conforms to expected template"

    implementation_evidence:
      - "PRs: collect PR links and descriptions"
      - "Commits: record relevant commit hashes and messages"
      - "Changed Files: list modified files and their purposes"
      - "Migrations: record database/architecture changes"
      - "Configurations: record environment/configuration changes"

    quality_artifacts:
      - "Test Reports: collect unit, integration, acceptance test results"
      - "Coverage: record actual coverage percentages"
      - "CI Status: include build and deployment status"
      - "Performance: collect actual performance measurements"
      - "Security Scans: include security analysis results"

    qa_reviews:
      - "QA Feedback: collect QA review comments and issues"
      - "Issue Status: record current processing status"
      - "Resolution Plans: record resolution plans and improvements"

    project_md_documents:
      - "Scan entire project directory structure, collect all .md documents"
      - "Analyze document content, extract relevant information and insights"
      - "Identify associations and dependencies between documents"
      - "Record completeness and quality status of documents"
      - "Provide comprehensive document analysis foundation for completion report"

  stage_execution_checkpoints:
    before_stage:
      - "Explain stage being started"
      - "Reference specific stage requirements in workflow file"

    during_stage:
      - "Execute all actions listed in stage"
      - "Perform systematic analysis and evaluation"
      - "Collect all required evidence"

    after_stage:
      - "Verify stage completion against validation rules"
      - "Confirm all required outputs generated"
      - "Link evidence to record discoveries"

  synthesis_requirements:
    delivery_mapping:
      - "Cross-reference completed deliverables with original scope"
      - "Record completion status of each planned item"
      - "Identify any delays or scope-out changes"
      - "Provide evidence for all completion statements"

    acceptance_criteria_analysis:
      - "Compare implemented functions with acceptance standards"
      - "Reference test results and verification evidence"
      - "Record any unmet or partially met standards"
      - "Link to specific test reports or verification artifacts"

    qa_problem_extraction:
      - "Summarize QA feedback and concerns"
      - "Categorize by severity and current status"
      - "Record resolution plans and timelines"
      - "Track ongoing issues and workarounds"

    known_issues_documentation:
      - "List all defects and limitations currently existing"
      - "Describe technical debt and trade-offs made"
      - "Record existing temporary solutions"
      - "Assess risk levels and impacts"

    project_documentation_analysis:
      - "Comprehensively analyze all collected project documents"
      - "Identify coverage gaps and overlaps in documentation"
      - "Evaluate documentation quality, consistency, and maintainability"
      - "Record documentation architecture strengths and improvement opportunities"
      - "Provide concrete suggestions for future documentation improvements"

  enhancement_planning:
    gap_based_enhancements:
      - "Identify opportunities from incomplete functions"
      - "Derive improvements from QA feedback"
      - "Consider performance optimization opportunities"
      - "Evaluate maintainability improvements"

    success_criteria_definition:
      - "Define measurable success criteria for each enhancement"
      - "Set realistic timelines and effort estimates"
      - "Identify dependencies and prerequisites"
      - "Prioritize by business value and technical impact"

  template_population_enforcement:
    mandatory_steps:
      - "Always read template file before writing"
      - "Populate section by section according to template requirements"
      - "Never leave placeholder text like {task_id} or INSERT VALUE"
      - "Each completion statement must include concrete evidence"
      - "Include actual measurement results, not estimates"
      - "Completeness check: each template section must be populated"

  validation_checkpoints:
    after_document_generation:
      - "Read generated document back"
      - "Compare section by section with template structure"
      - "Verify no placeholder values remain"
      - "Confirm all completion statements have evidence support"
      - "Validate markdown format and structure"

    completion_criteria:
      - "All workflow stages completed"
      - "All template sections populated with actual content"
      - "All validation rules satisfied"
      - "All completion statements have evidence support"
      - "QA potential problems analyzed and recorded"
      - "Future enhancements concrete with priorities"
      - "Document ready for handover to stakeholders"

  error_handling:
    validation_failures:
      - "Stop immediately if validation fails"
      - "Identify specific validation failures"
      - "Return to corresponding workflow stage"
      - "Retry after correction"
      - "Re-verify before continuation"

    evidence_collection_failures:
      - "Record as limitations if evidence missing"
      - "Record QA review unavailable if not obtainable"
      - "Collect available metrics if performance data incomplete"
      - "Record coverage gaps if testing insufficient"

  critical_success_factors:
    - "Read workflow and template files first - never start without them"
    - "Collect comprehensive evidence - PRs, commits, tests, QA feedback"
    - "Systematic analysis - define conclusion strategy first"
    - "Map delivery to original scope - clear completion status"
    - "Analyze acceptance criteria achievement - with test evidence"
    - "Extract and categorize QA problems - with resolution status"
    - "Clearly record known issues - with workarounds"
    - "Plan future enhancements - with success criteria"
    - "Validate at checkpoints - ensure quality per stage"
    - "Comprehensively analyze project documents - collect all relevant information"
    - "Clean up temporary documents after completion - preserve important deliverables"

  workflow_violation_responses:
    missing_stage_execution: "Return and complete skipped stages"
    incomplete_evidence_collection: "Collect all required artifacts"
    unsupported_completion_claims: "Provide evidence for all statements"
    missing_qa_analysis: "Record QA feedback and problems"
    generic_assessments: "Replace with concrete data and measurements"
    incomplete_template: "Identify missing sections and populate them"
    invalid_format: "Correct format to fully conform to template"
    incomplete_document_analysis: "Complete analysis of all project documents"
    missing_document_cleanup: "Execute temporary document cleanup procedure"

# Unified stage execution flow
stages:
  - id: "workflow_initialization"
    title: "Workflow Initialization"
    description: "Load necessary files and set up conclusion environment"
    completion_requirements:
      - workflow_file_parsed: true
      - template_structure_understood: true
      - validation_rules_loaded: true
    actions:
      - load_workflow_file: "{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml"
      - load_template_from: "{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml"
      - verify_file_accessibility

  - id: "conclusion_strategy"
    title: "Conclusion Strategy Setup"
    description: "Establish conclusion strategy and evidence collection plan"
    completion_requirements:
      - conclusion_strategy_defined: true
      - conclusion_focus_areas_defined: true
      - evidence_collection_strategy_established: true
    actions:
      - analyze_conclusion_requirements: ["scope", "delivery", "qa_reviews", "enhancements"]
      - define_conclusion_focus_areas
      - establish_evidence_collection_strategy

  - id: "evidence_collection"
    title: "Comprehensive Evidence Collection"
    description: "Collect all necessary project completion evidence"
    completion_requirements:
      - all_required_specs_read: true
      - plan_document_located_and_read: true
      - implementation_evidence_documented: true
      - quality_evidence_collected: true
      - qa_feedback_gathered_or_noted_absent: true
      - all_project_md_documents_analyzed: true
    actions:
      - read_specification_files: ["docs/specs/task.md", "docs/specs/requirements.md", "docs/specs/design.md"]
      - resolve_plan_by_task_id: "{{task_id}}"
      - read_dev_notes: "docs/dev-notes/{{task_id}}-dev-notes.md"
      - gather_implementation_evidence: ["PRs", "commits", "changed_files", "migrations", "configs"]
      - gather_quality_artifacts: ["test_reports", "coverage", "CI_status", "performance", "security_scans"]
      - gather_qa_reviews_and_feedback: "docs/implementation-review/{{task_id}}-review.md"
      - analyze_all_project_md_documents: "{{project_root}}"
      - document_evidence_gaps_as_limitations

  - id: "delivery_synthesis"
    title: "Delivery Deliverables Comprehensive Analysis"
    description: "Analyze delivery deliverables and original scope alignment"
    completion_requirements:
      - delivery_mapped_to_scope: true
      - acceptance_criteria_analyzed: true
      - completion_status_clearly_documented: true
    actions:
      - map_delivery_to_original_scope
      - analyze_acceptance_criteria_achievement
      - document_completion_deferred_outofscope_items
      - cross_reference_with_test_evidence
      - summarize_deliverable_status

  - id: "qa_problem_analysis"
    title: "QA Potential Problems Analysis"
    description: "Extract and analyze potential problems from QA feedback"
    completion_requirements:
      - qa_potential_problems_extracted: true
      - known_issues_and_risks_documented: true
      - evidence_linked_to_all_findings: true
    actions:
      - extract_qa_potential_problems_from_reviews
      - categorize_problems_by_severity_and_type
      - document_current_handling_status
      - identify_known_issues_and_risks
      - document_workarounds_and_solutions
      - link_all_findings_to_evidence

  - id: "enhancement_planning"
    title: "Future Enhancement Planning"
    description: "Formulate future enhancement plans based on gaps and QA feedback"
    completion_requirements:
      - enhancement_opportunities_identified: true
      - enhancements_derived_from_gaps_and_qa: true
      - success_criteria_defined_for_enhancements: true
      - enhancement_priorities_established: true
    actions:
      - derive_enhancements_from_incomplete_features
      - identify_opportunities_from_qa_feedback
      - consider_performance_optimization_opportunities
      - evaluate_maintainability_improvements
      - define_measurable_success_criteria
      - set_realistic_timelines_and_estimates
      - prioritize_by_business_value_and_impact

  - id: "report_generation"
    title: "Completion Report Generation"
    description: "Generate structured project completion report"
    completion_requirements:
      - template_structure_followed: true
      - no_placeholder_values: true
      - all_evidence_linked: true
      - completion_status_clearly_documented: true
    actions:
      - load_report_template: "{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml"
      - populate_metadata_with_actual_values
      - populate_sections: [
          "metadata",
          "summary",
          "acceptance",
          "qa_potential_problems",
          "project_documentation_analysis",
          "known_issues_and_risks",
          "future_enhancements",
          "handover_next_steps",
          "appendix"
        ]
      - ensure_all_completion_claims_have_evidence
      - include_actual_measurements_not_estimates
      - verify_no_placeholder_content_remains

  - id: "finalization"
    title: "Completion and Quality Confirmation"
    description: "Final verification and quality checks"
    completion_requirements:
      - final_document_read_back: true
      - completeness_verified: true
      - template_compliance_confirmed: true
      - completion_report_ready_for_stakeholders: true
      - temporary_documents_cleaned: true
    actions:
      - self_check_against_workflow
      - read_generated_document_back
      - compare_against_template_structure
      - verify_no_placeholder_values_remain
      - confirm_all_completion_claims_supported_by_evidence
      - validate_markdown_formatting_and_structure
      - request_feedback_if_needed
      - cleanup_temporary_documents: "{{project_root}}"

# === New: Knowledge and Architecture Product Integration ===
extensions:
  agents_integration:
    knowledge_curator:
      agent: "knowledge-curator"
      template: "{project_root}/sunnycore/po/templates/knowledge-lessons-tmpl.yaml"
      output: "{{project_root}}/docs/knowledge/engineering-lessons.md"
      trigger: "after:report_generation"
    architecture_documenter:
      agent: "architecture-documenter"
      template: "{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml"
      output: "{{project_root}}/docs/architecture/architecture.md"
      trigger: "after:report_generation"
    file_classifier:
      agent: "file-classifier"
      template: "{project_root}/sunnycore/po/workflow/unified-file-classification-workflow.yaml"
      output: "{{project_root}}/docs/file-classification/file-classification-report.md"
      trigger: "parallel:with_conclude"

# Integrated validation rules
validation_rules:
  template_validation:
    required_metadata_fields:
      - task_id: "actual_value_not_placeholder"
      - project_name: "actual_value_not_placeholder"
      - owner: "actual_owner_name"
      - date: "yyyy_mm_dd_format"
      - sources: "all_spec_plan_and_evidence_paths_documented"

    required_content_sections:
      - project_summary: "scope_and_completion_overview"
      - completion_status: "deliverables_and_completion_rate"
      - acceptance_criteria_achievement: "cross_reference_with_tests_evidence"
      - qa_potential_problems_summary: "concerns_and_handling_status"
      - project_documentation_analysis: "comprehensive_document_analysis_and_quality_assessment"
      - known_issues_and_risks: "defects_trade_offs_workarounds"
      - future_enhancements: "specific_proposals_with_success_criteria"
      - next_steps_and_handover: "blockers_fixes_followup_actions"
      - appendix: "testing_performance_ci_cd_data"

    evidence_requirements:
      - completion_claims_supported: "pr_links_commit_hashes_file_changes"
      - qa_issues_documented: "specific_feedback_and_current_status"
      - performance_data_included: "actual_measurements_not_estimates"
      - test_coverage_reported: "actual_coverage_percentages_and_results"
      - known_issues_specific: "exact_problem_descriptions_and_workarounds"
      - documentation_analysis_supported: "specific_document_paths_and_findings"

    forbidden_content:
      - placeholder_brackets: ["<", ">"]
      - placeholder_text: ["INSERT", "TODO", "TBD"]
      - generic_placeholders: ["{task_id}", "<project_name/>", "<owner/>"]
      - unsupported_claims: "all_completion_claims_must_have_evidence"
      - vague_assessments: ["generally good", "mostly complete", "acceptable quality"]

    document_cleanup_requirements:
      preserve_files:
        - "docs/implementation-plan/**/* - implementation plan files"
        - "docs/implementation-review/**/* - implementation review files"
        - "docs/dev-notes/**/* - development notes"
        - "docs/knowledge/**/* - knowledge files"
        - "docs/architecture/**/* - architecture files"
        - "README.md - project description file"
        - "CHANGELOG.md - change log"
        - "docs/completion-reports/**/* - completion reports"
      cleanup_temporary_files:
        - "Temporary documents created during analysis process"
        - "Temporary notes used for information collection"
        - "Intermediate outputs from analysis process"
        - "Temporary files not part of final deliverables"

  error_handling:
    missing_stage:
      severity: "blocker"
      message: "Mandatory conclusion stage not completed"
      action: "halt_and_request_completion"

    incomplete_evidence_collection:
      severity: "blocker"
      message: "Required evidence not collected or documented"
      action: "halt_and_request_evidence_gathering"

    unsupported_completion_claims:
      severity: "high"
      message: "Completion claims made without supporting evidence"
      action: "flag_and_request_evidence"

    missing_qa_analysis:
      severity: "high"
      message: "QA potential problems not analyzed or documented"
      action: "request_qa_analysis_completion"

    incomplete_template:
      severity: "high"
      message: "Template section incomplete or contains placeholders"
      action: "request_template_completion"

    incomplete_document_analysis:
      severity: "high"
      message: "Project documentation analysis incomplete"
      action: "complete_document_analysis"

    missing_document_cleanup:
      severity: "medium"
      message: "Temporary documents not cleaned up"
      action: "execute_document_cleanup"

output:
  path: "{{project_root}}/docs/completion-reports/"
  filename: "{{task_id}}-completion.md"
  format: markdown
