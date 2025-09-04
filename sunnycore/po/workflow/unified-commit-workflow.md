# Unified Commit Workflow

## Workflow Overview
This document defines the comprehensive workflow for coordinating 5 parallel commit-agents to handle software development document editing, updating, and compliance verification. The workflow implements systematic parallel execution with convergence strategies and fast-stop mechanisms.

## Workflow Architecture

### Phase 1: Initialization and Context Analysis
```xml
<phase1_initialization>
  <duration>0-90 seconds</duration>
  <participants>commit-orchestrator + all 5 agents</participants>
  
  <step1_prerequisite_validation>
    <action>Validate all mandatory files and enforcement standards</action>
    <validation_targets>
      <file>sunnycore/po/task/commit.md</file>
      <file>sunnycore/po/enforcement/commit-orchestrator-enforcement.md</file>
      <directory>sunnycore/po/templates/</directory>
    </validation_targets>
    <fast_stop_trigger>Missing enforcement standards or task specification</fast_stop_trigger>
  </step1_prerequisite_validation>
  
  <step2_git_context_analysis>
    <action>Analyze current git state and commit context</action>
    <analysis_scope>
      <commit_message>Parse and validate commit message format</commit_message>
      <changed_files>Identify modified documentation and source files</changed_files>
      <diff_analysis>Analyze changes to understand update requirements</diff_analysis>
      <branch_validation>Verify branch compliance with git integration standards</branch_validation>
    </analysis_scope>
    <output_format>shared_context_json</output_format>
  </step2_git_context_analysis>
  
  <step3_agent_initialization>
    <action>Initialize all 5 parallel agents with shared context</action>
    <agents>
      <agent id="commit-parser" priority="high"/>
      <agent id="document-updater" priority="high"/>
      <agent id="compliance-validator" priority="medium"/>
      <agent id="cicd-monitor" priority="medium"/>
      <agent id="specs-synchronizer" priority="low"/>
    </agents>
    <shared_state>git_context + enforcement_rules + template_registry</shared_state>
  </step3_agent_initialization>
</phase1_initialization>
```

### Phase 2: Parallel Agent Execution
```xml
<phase2_parallel_execution>
  <duration>90-600 seconds</duration>
  <execution_model>synchronous_parallel</execution_model>
  
  <agent_commit_parser>
    <role>解析與上下文分析專家</role>
    <execution_time>90-120 seconds</execution_time>
    <responsibilities>
      <primary>Parse commit message and extract change semantics</primary>
      <secondary>Analyze file changes and determine documentation impact</secondary>
      <tertiary>Identify dependencies between changed components</tertiary>
    </responsibilities>
    
    <workflow_steps>
      <step1>Load and parse git commit context (commit message, diff, changed files)</step1>
      <step2>Extract semantic information using natural language processing</step2>
      <step3>Categorize changes (features, fixes, docs, refactor, etc.)</step3>
      <step4>Identify impacted documentation sections and update requirements</step4>
      <step5>Generate structured change analysis report in JSON format</step5>
    </workflow_steps>
    
    <output_schema>
      <commit_analysis>
        <type>string</type>
        <scope>string</scope>
        <description>string</description>
        <breaking_changes>boolean</breaking_changes>
        <impacted_docs>array</impacted_docs>
        <change_categories>array</change_categories>
      </commit_analysis>
    </output_schema>
    
    <quality_checkpoints>
      <checkpoint1>Commit message parsing accuracy ≥ 95%</checkpoint1>
      <checkpoint2>Change categorization completeness ≥ 90%</checkpoint2>
      <checkpoint3>Documentation impact identification ≥ 85%</checkpoint3>
    </quality_checkpoints>
  </agent_commit_parser>
  
  <agent_document_updater>
    <role>文檔更新實作專家</role>
    <execution_time>120-180 seconds</execution_time>
    <responsibilities>
      <primary>Update README.md according to template standards</primary>
      <secondary>Update CHANGELOG.md with semantic versioning compliance</secondary>
      <tertiary>Ensure template compliance and content quality</tertiary>
    </responsibilities>
    
    <workflow_steps>
      <step1>Load current README.md and CHANGELOG.md content</step1>
      <step2>Load appropriate templates from sunnycore/po/templates/</step2>
      <step3>Analyze change requirements from commit-parser output</step3>
      <step4>Generate updated documentation content following templates</step4>
      <step5>Validate content quality and template compliance</step5>
      <step6>Prepare final documentation updates in structured format</step6>
    </workflow_steps>
    
    <template_compliance>
      <readme_requirements>
        <sections>project_description, installation, usage, api, contributing, license</sections>
        <quality_gates>readability ≥ 8, completeness ≥ 95%, link_validation</quality_gates>
      </readme_requirements>
      <changelog_requirements>
        <format>keep_a_changelog standard</format>
        <versioning>semantic_versioning</versioning>
        <categories>added, changed, deprecated, removed, fixed, security</categories>
      </changelog_requirements>
    </template_compliance>
    
    <output_schema>
      <document_updates>
        <readme_content>string</readme_content>
        <changelog_content>string</changelog_content>
        <template_compliance_score>number</template_compliance_score>
        <quality_metrics>object</quality_metrics>
      </document_updates>
    </output_schema>
  </agent_document_updater>
  
  <agent_compliance_validator>
    <role>合規品質驗證專家</role>
    <execution_time>90-150 seconds</execution_time>
    <responsibilities>
      <primary>Validate compliance with commit-orchestrator-enforcement.md standards</primary>
      <secondary>Check git integration compliance (branch, message format)</secondary>
      <tertiary>Validate documentation quality gates</tertiary>
    </responsibilities>
    
    <workflow_steps>
      <step1>Load enforcement standards XML schema</step1>
      <step2>Validate git commit compliance (message format, branch rules)</step2>
      <step3>Check documentation update compliance with standards</step3>
      <step4>Validate template compliance and content quality</step4>
      <step5>Perform security and access control validation</step5>
      <step6>Generate comprehensive compliance report</step6>
    </workflow_steps>
    
    <validation_framework>
      <git_compliance>
        <commit_message_format>regex validation against enforcement standards</commit_message_format>
        <branch_restrictions>validate against protected branches and patterns</branch_restrictions>
        <change_analysis>validate file type monitoring and priority assessment</change_analysis>
      </git_compliance>
      <documentation_compliance>
        <template_adherence>validate template population rate ≥ 95%</template_adherence>
        <quality_standards>validate against readability and completeness criteria</quality_standards>
        <content_validation>validate code examples and link accessibility</content_validation>
      </documentation_compliance>
    </validation_framework>
    
    <output_schema>
      <compliance_report>
        <overall_status>string</overall_status>
        <git_compliance>object</git_compliance>
        <documentation_compliance>object</documentation_compliance>
        <violations>array</violations>
        <warnings>array</warnings>
        <recommendations>array</recommendations>
      </compliance_report>
    </output_schema>
  </agent_compliance_validator>
  
  <agent_cicd_monitor>
    <role>CI/CD 狀態監控專家</role>
    <execution_time>60-300 seconds</execution_time>
    <responsibilities>
      <primary>Monitor CI/CD pipeline execution and status</primary>
      <secondary>Generate detailed failure reports if CI/CD fails</secondary>
      <tertiary>Validate deployment and functionality after successful CI/CD</tertiary>
    </responsibilities>
    
    <workflow_steps>
      <step1>Connect to CI/CD system and retrieve current pipeline status</step1>
      <step2>Monitor pipeline execution with 30-second intervals</step2>
      <step3>Analyze build, test, deployment stages for success/failure</step3>
      <step4>If successful: validate deployment and functionality</step4>
      <step5>If failed: perform detailed failure analysis and root cause identification</step5>
      <step6>Generate comprehensive CI/CD status report</step6>
    </workflow_steps>
    
    <monitoring_framework>
      <status_monitoring>
        <check_frequency>30 seconds</check_frequency>
        <timeout_threshold>1800 seconds</timeout_threshold>
        <retry_count>2</retry_count>
      </status_monitoring>
      <failure_analysis>
        <categorization>build, test, deployment, linting, security</categorization>
        <severity_assessment>low, medium, high, critical</severity_assessment>
        <remediation_suggestions>automated analysis and recommendations</remediation_suggestions>
      </failure_analysis>
    </monitoring_framework>
    
    <output_schema>
      <cicd_status_report>
        <pipeline_status>string</pipeline_status>
        <stage_results>array</stage_results>
        <failure_analysis>object</failure_analysis>
        <remediation_plan>object</remediation_plan>
        <deployment_validation>object</deployment_validation>
      </cicd_status_report>
    </output_schema>
  </agent_cicd_monitor>
  
  <agent_specs_synchronizer>
    <role>規格同步稽核專家</role>
    <execution_time>120-240 seconds</execution_time>
    <responsibilities>
      <primary>Synchronize specs documentation with actual development state</primary>
      <secondary>Prepare requirements/design/task specs for re-development if needed</secondary>
      <tertiary>Maintain traceability between specs and implementation</tertiary>
    </responsibilities>
    
    <workflow_steps>
      <step1>Load current specs from docs/specs/ directory</step1>
      <step2>Analyze git changes and implementation state</step2>
      <step3>Identify discrepancies between specs and implementation</step3>
      <step4>If CI/CD failed: prepare specs updates for re-development</step4>
      <step5>Validate traceability links and dependency mappings</step5>
      <step6>Generate specs synchronization report</step6>
    </workflow_steps>
    
    <synchronization_framework>
      <specs_analysis>
        <requirements_alignment>validate requirements against implementation</requirements_alignment>
        <design_consistency>check design document consistency with code</design_consistency>
        <task_completion>verify task completion against specifications</task_completion>
      </specs_analysis>
      <re_development_preparation>
        <trigger_condition>CI/CD failure or major discrepancies</trigger_condition>
        <update_strategy>minimal viable updates for continuation</update_strategy>
        <rollback_planning>prepare rollback options and strategies</rollback_planning>
      </re_development_preparation>
    </synchronization_framework>
    
    <output_schema>
      <specs_sync_report>
        <synchronization_status>string</synchronization_status>
        <discrepancies>array</discrepancies>
        <specs_updates_needed>boolean</specs_updates_needed>
        <re_development_plan>object</re_development_plan>
        <traceability_matrix>object</traceability_matrix>
      </specs_sync_report>
    </output_schema>
  </agent_specs_synchronizer>
</phase2_parallel_execution>
```

### Phase 3: Barrier Synchronization and Validation
```xml
<phase3_barrier_synchronization>
  <duration>600-720 seconds</duration>
  <synchronization_points>
    <barrier1_completion_check>
      <condition>All 5 agents complete or 4 out of 5 with acceptable results</condition>
      <timeout>600 seconds</timeout>
      <failure_action>proceed_with_warnings_if_4_complete</failure_action>
    </barrier1_completion_check>
    
    <barrier2_quality_validation>
      <condition>Quality gates validation across all completed agent outputs</condition>
      <validation_criteria>
        <documentation_quality>≥ 95% template compliance</documentation_quality>
        <compliance_status>All critical violations resolved</compliance_status>
        <cicd_status>Success or detailed failure analysis complete</cicd_status>
      </validation_criteria>
      <failure_action>require_remediation_or_minimal_output</failure_action>
    </barrier2_quality_validation>
  </synchronization_points>
  
  <template_existence_validation>
    <required_templates>
      <template>readme-update-template.yaml</template>
      <template>changelog-template.yaml</template>
      <template>cicd-failure-report-template.yaml</template>
      <template>specs-update-template.yaml</template>
    </required_templates>
    <validation_action>Check template accessibility and structural integrity</validation_action>
    <failure_handling>Record missing templates and continue with available ones</failure_handling>
  </template_existence_validation>
</phase3_barrier_synchronization>
```

### Phase 4: Result Convergence and Output Generation
```xml
<phase4_result_convergence>
  <duration>720-900 seconds</duration>
  
  <convergence_strategy>
    <json_result_aggregation>
      <method>Collect all agent JSON outputs into unified result set</method>
      <conflict_resolution>Apply severity matrix for conflicting recommendations</conflict_resolution>
      <consensus_building>Prioritize high-confidence results over uncertain ones</consensus_building>
    </json_result_aggregation>
    
    <severity_matrix_arbitration>
      <critical_issues>Immediate attention required, blocks deployment</critical_issues>
      <high_issues>Important improvements, affects quality significantly</high_issues>
      <medium_issues>Moderate improvements, affects quality moderately</medium_issues>
      <low_issues>Minor suggestions, minimal quality impact</low_issues>
    </severity_matrix_arbitration>
    
    <final_decision_framework>
      <documentation_updates>
        <condition>If document-updater succeeded and compliance-validator approves</condition>
        <action>Apply README.md and CHANGELOG.md updates</action>
      </documentation_updates>
      
      <cicd_success_path>
        <condition>If cicd-monitor reports pipeline success</condition>
        <action>Complete documentation updates and generate success report</action>
      </cicd_success_path>
      
      <cicd_failure_path>
        <condition>If cicd-monitor reports pipeline failure</condition>
        <action>Generate detailed failure report and prepare re-development specs</action>
      </cicd_failure_path>
    </final_decision_framework>
  </convergence_strategy>
  
  <output_generation>
    <success_output>
      <updated_readme>Apply README.md updates using readme-update-template.yaml</updated_readme>
      <updated_changelog>Apply CHANGELOG.md updates using changelog-template.yaml</updated_changelog>
      <compliance_report>Generate comprehensive compliance status report</compliance_report>
      <cicd_success_confirmation>Validate and confirm successful deployment</cicd_success_confirmation>
    </success_output>
    
    <failure_output>
      <cicd_failure_report>Generate detailed failure analysis using cicd-failure-report-template.yaml</cicd_failure_report>
      <specs_update_preparation>Prepare requirements/design/task specs updates using specs-update-template.yaml</specs_update_preparation>
      <remediation_plan>Generate comprehensive remediation and re-development plan</remediation_plan>
      <rollback_strategy>Provide rollback options and recovery procedures</rollback_strategy>
    </failure_output>
    
    <minimal_viable_output>
      <emergency_stop_report>
        <status>EMERGENCY_STOP</status>
        <trigger_code>Specific failure condition code</trigger_code>
        <available_results>Summary of completed agent results</available_results>
        <required_actions>Minimal actions needed for system recovery</required_actions>
        <continuation_plan>Steps to resume workflow after issue resolution</continuation_plan>
      </emergency_stop_report>
    </minimal_viable_output>
  </output_generation>
</phase4_result_convergence>
```

## Fast-Stop Implementation Strategy

### Fast-Stop Trigger Monitoring
```xml
<fast_stop_monitoring>
  <continuous_monitoring>
    <check_interval>30 seconds</check_interval>
    <monitored_conditions>
      <prerequisite_failures>Missing enforcement or workflow files</prerequisite_failures>
      <agent_coordination_failures>More than 50% agents fail to execute</agent_coordination_failures>
      <template_system_failures>Critical templates missing or corrupted</template_system_failures>
      <timeout_violations>Total execution time exceeds 900 seconds</timeout_violations>
      <critical_compliance_failures>Security or data protection violations</critical_compliance_failures>
    </monitored_conditions>
  </continuous_monitoring>
  
  <immediate_response_protocol>
    <stop_signal_propagation>
      <method>Broadcast stop signal to all active agents within 5 seconds</method>
      <agent_acknowledgment>Require acknowledgment from all agents within 15 seconds</agent_acknowledgment>
      <forced_termination>Force terminate unresponsive agents after 30 seconds</forced_termination>
    </stop_signal_propagation>
    
    <minimal_output_generation>
      <data_preservation>Preserve all completed work and partial results</data_preservation>
      <status_documentation>Document exact failure condition and system state</status_documentation>
      <recovery_instructions>Generate specific recovery instructions based on failure type</recovery_instructions>
    </minimal_output_generation>
  </immediate_response_protocol>
</fast_stop_monitoring>
```

### Recovery and Continuation Strategy
```xml
<recovery_strategy>
  <failure_classification>
    <recoverable_failures>
      <agent_individual_failure>Continue with remaining agents, document missing functionality</agent_individual_failure>
      <template_missing>Use default templates or simplified formats</template_missing>
      <cicd_temporary_failure>Continue with documentation updates, mark CI/CD for retry</cicd_temporary_failure>
    </recoverable_failures>
    
    <non_recoverable_failures>
      <enforcement_missing>Cannot proceed without enforcement standards</enforcement_missing>
      <workflow_corrupted>Cannot execute without valid workflow definition</workflow_corrupted>
      <system_resource_exhaustion>Cannot continue without system resources</system_resource_exhaustion>
    </non_recoverable_failures>
  </failure_classification>
  
  <continuation_procedures>
    <automatic_recovery>
      <retry_mechanisms>Implement automatic retry for transient failures</retry_mechanisms>
      <fallback_procedures>Switch to simplified workflows for degraded conditions</fallback_procedures>
      <graceful_degradation>Reduce functionality scope while maintaining core objectives</graceful_degradation>
    </automatic_recovery>
    
    <manual_intervention_required>
      <clear_instructions>Provide specific step-by-step recovery procedures</clear_instructions>
      <system_state_preservation>Maintain system state for manual inspection and correction</system_state_preservation>
      <resume_capabilities>Enable seamless resume after manual intervention</resume_capabilities>
    </manual_intervention_required>
  </continuation_procedures>
</recovery_strategy>
```

## Quality Assurance and Monitoring

### Workflow Execution Monitoring
```xml
<execution_monitoring>
  <phase_tracking>
    <phase_completion_timestamps>Record start and end time for each workflow phase</phase_completion_timestamps>
    <agent_performance_metrics>Track individual agent execution time and success rate</agent_performance_metrics>
    <quality_gate_results>Document pass/fail status for each quality gate</quality_gate_results>
  </phase_tracking>
  
  <real_time_dashboards>
    <workflow_progress>Visual progress indicator for overall workflow execution</workflow_progress>
    <agent_status>Real-time status for each of the 5 parallel agents</agent_status>
    <quality_metrics>Live quality assessment and compliance status</quality_metrics>
  </real_time_dashboards>
</execution_monitoring>
```

### Continuous Improvement Framework
```xml
<continuous_improvement>
  <metrics_collection>
    <performance_metrics>Execution time, success rate, quality scores</performance_metrics>
    <user_satisfaction>Feedback collection and satisfaction scoring</user_satisfaction>
    <system_reliability>Failure rate, recovery time, availability metrics</system_reliability>
  </metrics_collection>
  
  <optimization_opportunities>
    <workflow_refinement>Identify bottlenecks and optimization opportunities</workflow_refinement>
    <agent_coordination_improvement>Enhance parallel execution and communication</agent_coordination_improvement>
    <quality_enhancement>Improve quality gates and validation procedures</quality_enhancement>
  </optimization_opportunities>
</continuous_improvement>
```

---

**Workflow Version**: 1.0  
**Last Updated**: 2025-01-15  
**Review Cycle**: Monthly  
**Maintained By**: AI Prompt Engineering Team

*This unified commit workflow serves as the authoritative reference for coordinating 5 parallel commit-agents in software development document management, ensuring systematic execution, quality assurance, and reliable fast-stop mechanisms.*
