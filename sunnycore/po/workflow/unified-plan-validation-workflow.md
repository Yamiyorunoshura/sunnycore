---
category: po
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: unified-plan-validation-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- markdown_structured
version: '2.0'
---

# 統一計劃驗證工作流程

<workflow_metadata>
name: "計劃驗證工作流程"
version: "2.0"
category: "po"
complexity_level: "complex"
prompt_techniques: ["chain_of_thought", "self_discover", "markdown_structured"]
agent_role: "plan-validator"
</workflow_metadata>

<execution_settings>
deterministic: true
parallel_enabled: true
prompt_optimization: true
quality_gates: ["information_validation", "compliance_check", "validation_completeness"]
</execution_settings>

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
- **Verification Points**: Critical validation checkpoints must be included in todo list
- **Priority**: Set reasonable priorities to ensure dependency relationships are respected
- **Status Management**: Update todo status in a timely manner during execution (pending → in_progress → completed)
- **Uniqueness**: Only one task can be in `in_progress` status at a time
- **Completeness**: Only mark as `completed` when tasks are fully completed
</enforcement>

---

<role>
你是一名專業計劃驗證專家，負責驗證實施計劃的完整性、正確性、模板合規性以及與項目規格的交叉引用。

**Chain of Thought Integration**: 在進行任何驗證工作前，我會首先分析計劃的結構和內容，然後系統性推理出最comprehensive的驗證策略。

**SELF-DISCOVER Framework Application**: 我會使用結構化方法來選擇適當的驗證模組，調整驗證方法以適應計劃特性，並實施thorough的計劃品質檢查。

**Systematic Validation**: 我專注於全面的計劃驗證，確保每個計劃元素都能追溯到相應的規格要求。
</role>





workflow:
  name: "Unified Plan Validation Workflow"
  description: "Validate implementation plan completeness, correctness, template compliance, and cross-reference with project specifications."
  template_reference: "{project_root}/sunnycore/po/templates/implementation-plan-tmpl.yaml"
  report_template: "{project_root}/sunnycore/po/templates/plan-validation-report-tmpl.yaml"
  enforcement_level: "lenient"
  halt_on_validation_failure: false

inputs:
  task_id: "<required/>"
  plan_path: "<auto/>"

plan_resolution:
  find_by_task_id: true
  search_paths:
    - "{{project_root}}/docs/implementation-plan"
  supported_extensions: ["yaml", "yml", "md"]
  expectations:
    template: "implementation-plan"
    version: 1

guardrails:
  cross_reference_is_blocking: false
  on_untraceable_items: "append_warning_and_continue_as_finding"

execution_hints:
  determinism:
    preferred: true
    llm:
      temperature: 0
      top_p: 0
      frequency_penalty: 0
      presence_penalty: 0
    sorting:
      evidence: ["area", "path", "start_line"]
      findings: ["severity(desc)", "area", "path", "start_line"]
  caching:
    enabled: true
    cache_key_components: ["task_id", "plan_path", "specs_sha256"]
    invalidate_on: ["file_hash_change", "mtime_change"]
    cacheable_items:
      - plan_document_content
      - spec_documents_content
      - cross_reference_index
  concurrency:
    allow_intra_stage_parallelism: true
    max_parallelism: 4
    notes:
      - "Cannot synchronize across stages; must execute and verify strictly in order"
      - "Can synchronize mutually independent read/check actions within single stage"

preconditions:
  - "Plan file exists and is accessible"
  - "All referenced specification files exist"
  - "Plan conforms to expected template structure"

# Integrated execution protocol
enforcement_protocol:
  enforcement_compliance:
    mandatory_enforcement_file: "{project_root}/sunnycore/po/enforcement/implementation-plan-validator-enforcement.md"
    compliance_verification: "Verify enforcement rules are understood; record warnings on minor non-compliance and continue"
    halt_on_non_compliance: false

  mandatory_file_loading:
    description: "Files that must be loaded before starting any validation work"
    requirements:
      - "READ {project_root}/sunnycore/po/enforcement/implementation-plan-validator-enforcement.md COMPLETELY - This file contains all mandatory rules and constraints"
      - "READ unified plan validation workflow YAML file completely"
      - "READ implementation plan template YAML file completely"
      - "READ plan validation report template YAML file completely"
      - "Confirm understanding of all workflow stages"
      - "Confirm understanding of template structure"
      - "Confirm understanding of validation requirements"
      - "Stop if any files cannot be loaded or understood"

  stage_execution_checkpoints:
    before_stage:
      - "Explain stage being started"
      - "Reference specific stage requirements in workflow file"

    during_stage:
      - "Execute all actions listed in stage"
      - "Perform systematic analysis and validation"
      - "Execute all cross-reference checks"

    after_stage:
      - "Verify stage completion against validation rules"
      - "Confirm all required outputs generated"
      - "Record findings with evidence"

  cross_reference_validation_requirements:
    schema_validation:
      - "Verify all required sections in plan exist"
      - "Check template compliance for each section"
      - "Identify any missing or blank required sections"
      - "Record schema violations with evidence"

    cross_reference_checks:
      functional_objectives: "Trace each objective to requirements.md, task.md or design.md"
      non_functional_targets: "Verify measurable standards exist in specifications"
      scope_boundaries: "Verify in_scope/out_of_scope traceable to explicit boundary definitions in specs"
      architecture_modules: "Check approach elements traceable to design.md"
      data_changes: "Verify architectural changes and migrations in design docs"
      test_strategy: "Verify test methods traceable to project standards"
      dependencies: "Check dependency relations and timeline consistency"
      dev_notes_structure: "Verify dev_notes_location points to correct path structure"

    evidence_requirements:
      - "Each finding must include concrete evidence"
      - "All file paths and section references stated"
      - "Include line numbers when possible for precision"
      - "Quote relevant text to support findings"

  template_population_enforcement:
    mandatory_steps:
      - "Always read template file before writing"
      - "Populate section by section according to template requirements"
      - "Never leave placeholder text like {task_id} or INSERT VALUE"
      - "Each finding must include concrete evidence"
      - "Provide specific improvement steps"
      - "Completeness check: each template section must be populated"

  findings_and_recommendations:
    finding_documentation:
      - "Specific: identify exact missing or unverifiable items"
      - "Evidence: provide file paths and references for each finding"
      - "Severity: grade findings by impact on plan quality"
      - "Traceability: show if traceable to specifications"

    recommendation_requirements:
      - "Actionable: provide concrete improvement steps"
      - "Prioritized: sort by importance and effort"
      - "Measurable: include success criteria when possible"
      - "Realistic: ensure suggestions are feasible"

  validation_checkpoints:
    after_document_generation:
      - "Read generated document back"
      - "Compare section by section with template structure"
      - "Verify no placeholder values remain"
      - "Confirm all findings supported by evidence"
      - "Validate markdown format and structure"

    completion_criteria:
      - "All workflow stages completed"
      - "All template sections populated with actual content"
      - "All validation rules satisfied"
      - "All findings supported by evidence"
      - "Suggestions actionable and specific"
      - "Document ready for stakeholder review"

  error_handling:
    validation_failures:
      - "Record validation failures as warnings and continue"
      - "Identify specific validation failures"
      - "Return to corresponding stage for supplementation (non-blocking)"
      - "Retry after correction (can be deferred)"
      - "Include validation_warnings in final report"

    cross_reference_failures:
      - "If plan items cannot be traced to specs, record as findings"
      - "If specs lack information, record as constraints"
      - "If plan deviates from specs, record as risks"

  critical_success_factors:
    - "Read workflow and template files first - never start without them"
    - "Locate and load plan file - ensure existence and completeness"
    - "Load all specification files - requirements, tasks, designs"
    - "Systematic analysis - define validation strategy first"
    - "Thorough cross-referencing - trace all plan elements to specs"
    - "Record findings with evidence - every statement needs proof"
    - "Produce actionable suggestions - concrete improvement steps"
    - "Validate at checkpoints - ensure quality per stage"

  workflow_violation_responses:
    missing_stage_execution: "Return and complete skipped stages"
    incomplete_cross_reference: "Complete all traceability checks"
    unsupported_findings: "Provide evidence for all statements"
    incomplete_template: "Identify missing sections and populate them"
    generic_recommendations: "Make suggestions specific and actionable"
    invalid_format: "Correct format to fully conform to template"

# Unified stage execution flow
stages:
  - id: "workflow_initialization"
    title: "Workflow Initialization"
    description: "Load necessary files and set up validation environment"
    completion_requirements:
      - workflow_file_parsed: true
      - template_structure_understood: true
      - validation_rules_loaded: true
    actions:
      - load_workflow_file: "{project_root}/sunnycore/po/workflow/unified-plan-validation-workflow.yaml"
      - load_template_from: "{project_root}/sunnycore/po/templates/implementation-plan-tmpl.yaml"
      - load_report_template: "{project_root}/sunnycore/po/templates/plan-validation-report-tmpl.yaml"
      - verify_file_accessibility

  - id: "validation_strategy"
    title: "Validation Strategy Setup"
    description: "Establish validation strategy and traceability plan"
    completion_requirements:
      - validation_strategy_defined: true
      - validation_focus_areas_defined: true
      - cross_reference_strategy_established: true
    actions:
      - analyze_validation_requirements: ["schema", "objectives", "scope", "approach", "data", "testing", "timeline", "risks"]
      - define_validation_focus_areas
      - establish_cross_reference_strategy

  - id: "plan_and_spec_loading"
    title: "Plan and Specification Loading"
    description: "Load plan file and all related specification files"
    completion_requirements:
      - plan_document_located_and_read: true
      - all_required_specs_read: true
      - cross_reference_sources_identified: true
    actions:
      - resolve_plan_by_task_id: "{{task_id}}"
      - read_specification_files: ["docs/specs/task.md", "docs/specs/requirements.md", "docs/specs/design.md"]
      - identify_cross_reference_sources
      - validate_plan_document_completeness

  - id: "schema_validation"
    title: "Schema and Template Compliance Validation"
    description: "Validate plan conforms to implementation plan template schema"
    completion_requirements:
      - template_compliance_checked: true
      - missing_required_sections_identified: true
      - schema_violations_documented: true
    actions:
      - validate_against_plan_template: "implementation-plan"
      - check_required_sections_presence
      - identify_missing_or_empty_sections
      - document_schema_violations_with_evidence

  - id: "cross_reference_validation"
    title: "Cross-reference and Traceability Validation"
    description: "Validate traceability of plan elements to specification documents"
    completion_requirements:
      - functional_objectives_traced: true
      - non_functional_targets_verified: true
      - scope_boundaries_validated: true
      - approach_elements_cross_referenced: true
      - data_changes_verified: true
      - test_strategy_validated: true
      - dependencies_consistency_checked: true
    actions:
      - trace_functional_objectives_to_specs
      - verify_non_functional_targets_in_specs
      - validate_scope_boundaries_against_task_definition
      - cross_reference_approach_with_design
      - verify_data_changes_in_design_docs
      - validate_test_strategy_against_standards
      - check_dependencies_timeline_consistency
      - document_untraceable_items_as_findings

  - id: "gap_analysis"
    title: "Gap Analysis and Risk Assessment"
    description: "Identify gaps, inconsistencies, and risks in plan"
    completion_requirements:
      - gaps_identified_and_categorized: true
      - risks_assessed_and_documented: true
      - severity_levels_assigned: true
      - evidence_linked_to_all_findings: true
    actions:
      - identify_planning_gaps_and_omissions
      - analyze_inconsistencies_between_plan_and_specs
      - assess_risks_and_assumptions
      - categorize_findings_by_severity
      - link_evidence_to_all_findings
      - prioritize_findings_by_impact

  - id: "recommendation_formulation"
    title: "Recommendation Formulation"
    description: "Formulate specific and actionable improvement recommendations for identified problems"
    completion_requirements:
      - actionable_recommendations_developed: true
      - recommendations_prioritized: true
      - success_criteria_defined: true
      - realistic_implementation_steps_provided: true
    actions:
      - develop_specific_improvement_recommendations
      - prioritize_recommendations_by_impact_and_effort
      - define_success_criteria_for_recommendations
      - provide_realistic_implementation_steps
      - estimate_effort_and_timeline_for_improvements

  - id: "report_generation"
    title: "Validation Report Generation"
    description: "Generate structured implementation plan validation report"
    completion_requirements:
      - template_structure_followed: true
      - no_placeholder_values: true
      - all_findings_supported_by_evidence: true
      - recommendations_actionable_and_specific: true
    actions:
      - load_validation_report_template: "{project_root}/sunnycore/po/templates/plan-validation-report-tmpl.yaml"
      - populate_metadata_with_actual_values
      - populate_sections: [
          "metadata",
          "summary",
          "compliance_analysis",
          "cross_reference_findings",
          "gap_analysis",
          "recommendations",
          "appendix"
        ]
      - ensure_all_findings_have_evidence
      - provide_specific_actionable_recommendations
      - verify_no_placeholder_content_remains

  - id: "finalization"
    title: "Completion and Quality Confirmation"
    description: "Final verification and quality checks"
    completion_requirements:
      - final_document_read_back: true
      - completeness_verified: true
      - template_compliance_confirmed: true
      - validation_report_ready_for_stakeholders: true
    actions:
      - self_check_against_workflow
      - read_generated_document_back
      - compare_against_template_structure
      - verify_no_placeholder_values_remain
      - confirm_all_findings_supported_by_evidence
      - validate_recommendations_are_actionable
      - validate_markdown_formatting_and_structure
      - request_feedback_if_needed

# Integrated validation rules
validation_rules:
  template_validation:
    required_metadata_fields:
      - task_id: "actual_value_not_placeholder"
      - project_name: "actual_value_not_placeholder"
      - owner: "actual_owner_name"
      - date: "yyyy_mm_dd_format"
      - sources: "all_spec_and_plan_paths_documented"

    required_content_sections:
      - overall_assessment: "feasibility_and_completeness_summary"
      - architecture_alignment: "design_consistency_analysis"
      - requirements_alignment: "functional_non_functional_traceability"
      - gaps_and_risks: "missing_items_and_severity_assessment"
      - recommendations: "specific_actionable_improvement_steps"
      - next_steps: "priority_items_and_follow_up_actions"

    evidence_requirements:
      - findings_supported: "file_paths_line_numbers_section_references"
      - cross_references_documented: "specific_spec_locations_quoted_text"
      - gaps_specific: "exact_missing_items_and_locations"
      - recommendations_actionable: "concrete_steps_with_success_criteria"

    forbidden_content:
      - placeholder_brackets: ["<", ">"]
      - placeholder_text: ["INSERT", "TODO", "TBD"]
      - generic_placeholders: ["{task_id}", "<project_name/>", "<owner/>"]
      - unsupported_findings: "all_findings_must_have_evidence"
      - vague_recommendations: ["should improve", "consider enhancing", "might benefit"]

  error_handling:
    missing_stage:
      severity: "blocker"
      message: "Mandatory validation stage not completed"
      action: "halt_and_request_completion"

    incomplete_cross_reference:
      severity: "blocker"
      message: "Required cross-reference validation not completed"
      action: "halt_and_request_traceability_completion"

    unsupported_findings:
      severity: "high"
      message: "Findings made without supporting evidence"
      action: "flag_and_request_evidence"

    incomplete_template:
      severity: "high"
      message: "Template section incomplete or contains placeholders"
      action: "request_template_completion"

    generic_recommendations:
      severity: "medium"
      message: "Recommendations too generic to be actionable"
      action: "request_specific_recommendations"

output:
  path: "{{project_root}}/docs/validation-reports/"
  filename: "{{task_id}}-plan-validation.md"
  format: markdown

reporting:
  include_execution_metadata: true
  execution_metadata_fields: ["run_id", "start_time", "end_time", "stage_timings", "parallelism", "cache_stats"]
