# Fullstack Developer Enforcement Standards

<specification_metadata>
name: "Fullstack Developer Enforcement Standards"
version: "2.0.0"
category: "fullstack_development_enforcement"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## Core Execution Protocol

<prerequisites>
<file path="sunnycore/dev/workflow/fullstack-developer-workflow.md" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
<file path="implementation_plan_{task_id}.md" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
</prerequisites>

<determinism temperature="0" top_p="0" top_k="1" seed="42" stable_sort="true"/>

<workflow>
  <stage id="S1" name="prerequisite_validation" optional="false" parallel="forbidden">
    <inputs>
      <source path="sunnycore/dev/workflow/fullstack-developer-workflow.md" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Load and validate fullstack workflow requirements and implementation plans</select>
        <adapt>Adjust validation criteria for dual frontend-backend specialization</adapt>
        <implement>Execute prerequisite checks with comprehensive scope validation</implement>
        <apply>Continue execution with documented warnings and scope compliance tracking</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="workflow_integrity">
        <criteria>Never skip workflow stages, execute all stages in sequential order</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
      <gate name="dual_specialization">
        <criteria>Must execute frontend and backend specialized actions</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
  
  <stage id="S2" name="end_to_end_consistency_validation" optional="false" parallel="forbidden">
    <inputs>
      <source path="api_contracts.yaml" required="true"/>
      <source path="data_models.yaml" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Validate complete consistency between frontend, backend, and database contracts</select>
        <adapt>Adjust consistency checks based on architectural patterns and data flows</adapt>
        <implement>Execute comprehensive contract alignment and type consistency validation</implement>
        <apply>Generate end-to-end consistency report with synchronization verification</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="contract_alignment">
        <criteria>Complete consistency of contracts between all layers</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
      <gate name="type_consistency">
        <criteria>Type definitions consistent across all layers</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>

## Fullstack-Specific Mandatory Requirements

<reasoning>
  <analysis>Fullstack development requires comprehensive end-to-end consistency, dual specialization in frontend and backend, and seamless integration across all system layers</analysis>
  <findings>Critical areas include contract alignment, data model synchronization, API consistency, type safety, and unified error handling</findings>
  <decisions>Implement strict consistency enforcement with comprehensive validation across all system layers</decisions>
  <rationale>Fullstack systems require seamless integration between frontend and backend to ensure system reliability and maintainability</rationale>
  <validation>All requirements validated against architectural consistency and integration best practices</validation>
</reasoning>

### End-to-End Consistency (Absolute Mandatory)
- **Contract Alignment**: Must ensure complete consistency of contracts between frontend, backend, and database
- **Data Model Synchronization**: Ensure synchronization of data models between frontend and backend
- **API Contracts**: Frontend and backend API contracts must match precisely
- **Type Consistency**: Type definitions must remain consistent across layers

### Backend Integration Requirements
- **Data Changes**: Must draft idempotent and reversible migrations
- **API Security**: Must implement complete authentication, authorization, validation, and sanitization mechanisms
- **Performance Achievement**: Must meet latency, throughput, and memory targets
- **Error Handling**: Must implement unified error handling strategy

### Frontend Integration Requirements
- **UX Requirements**: Must extract all UI-IDs and verify design assets
- **Component Architecture**: Must create component skeleton and define types and interfaces
- **Accessibility**: Should ensure A11Y compliance; if temporarily not met, record risks and remediation plans
- **State Management**: Must implement consistent state management across frontend and API layers

### Architecture Integration Standards
- **Layered Architecture**: Must implement clear separation between presentation, business logic, and data layers
- **Service Integration**: Must ensure proper service-to-service communication patterns
- **Data Flow**: Must implement consistent data flow patterns throughout the application
- **Configuration Management**: Must maintain consistent configuration across all environments

### Testing Integration Requirements
- **End-to-End Testing**: Must implement comprehensive E2E tests covering full user workflows
- **Integration Testing**: Must test all API and database integration points
- **Contract Testing**: Must validate API contracts between frontend and backend
- **Performance Testing**: Must validate performance across the full stack

### Monitoring and Observability
- **Distributed Tracing**: Must implement tracing across frontend and backend services
- **Centralized Logging**: Must implement consistent logging strategy across all layers
- **Performance Monitoring**: Must monitor performance metrics across the full stack
- **Error Tracking**: Must implement unified error tracking and alerting

<output>
  <report>
    <summary>Fullstack development enforcement standards with comprehensive end-to-end consistency and integration requirements</summary>
    <details>Covers contract alignment, data model synchronization, API consistency, dual specialization requirements, testing integration, and monitoring standards</details>
    <checklist>
      <item checked="true">Contract alignment validated across all layers</item>
      <item checked="true">Data model synchronization verified</item>
      <item checked="true">API contracts precisely matched</item>
      <item checked="true">Type consistency enforced</item>
      <item checked="true">Backend integration requirements met</item>
      <item checked="true">Frontend integration requirements met</item>
      <item checked="false">End-to-end testing completed</item>
    </checklist>
  </report>
</output>

<security>
  <read_only_paths>
    <path>sunnycore/dev/workflow/fullstack-developer-workflow.md</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="password|secret|key|token|api_key" action="redact"/>
  </sensitive_filters>
  <access_control>
    <permission level="developer" scope="fullstack_development"/>
  </access_control>
</security>

<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="contract_inconsistency">
      <description>Critical inconsistency detected between frontend and backend contracts</description>
      <action>immediate_stop</action>
    </condition>
    <condition type="type_mismatch">
      <description>Type definition mismatch detected across system layers</description>
      <action>immediate_stop</action>
    </condition>
    <condition type="missing_workflow">
      <description>Critical fullstack workflow file not accessible</description>
      <action>record_warning_continue</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>EMERGENCY_STOP</status>
    <partial_results>Contract consistency validation failed, fullstack development halted</partial_results>
  </minimal_viable_output>
</fast_stop_mechanism>