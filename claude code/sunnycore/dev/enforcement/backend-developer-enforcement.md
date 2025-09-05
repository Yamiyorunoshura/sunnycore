# Backend Developer Enforcement Standards

<specification_metadata>
name: "Backend Developer Enforcement Standards"
version: "2.0.0"
category: "backend_development_enforcement"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## Core Execution Protocol

<prerequisites>
<file path="sunnycore/dev/workflow/backend-developer-workflow.md" required="recommended">
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
      <source path="sunnycore/dev/workflow/backend-developer-workflow.md" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Load and validate workflow requirements and implementation plans</select>
        <adapt>Adjust validation criteria based on available resources</adapt>
        <implement>Execute prerequisite checks with warning collection</implement>
        <apply>Continue execution with documented warnings for missing resources</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="workflow_integrity">
        <criteria>Never skip workflow stages, execute all stages in sequential order</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
  
  <stage id="S2" name="backend_requirements_validation" optional="false" parallel="forbidden">
    <inputs>
      <source path="security_requirements.md" required="true"/>
      <source path="performance_requirements.md" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Validate security, performance, and reliability requirements</select>
        <adapt>Adjust requirements based on project constraints</adapt>
        <implement>Execute comprehensive validation checks</implement>
        <apply>Generate compliance report with remediation plans</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="security_validation">
        <criteria>All security requirements must be validated</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
      <gate name="performance_validation">
        <criteria>Performance targets must be defined and achievable</criteria>
        <threshold>95%</threshold>
        <failure_action>record_warning_continue</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>

## Backend-Specific Mandatory Requirements

<reasoning>
  <analysis>Backend development requires comprehensive security, performance, and reliability controls</analysis>
  <findings>Critical areas include data integrity, API security, performance optimization, and testing coverage</findings>
  <decisions>Implement layered security approach with comprehensive testing and monitoring</decisions>
  <rationale>Backend systems are foundational to application security and performance</rationale>
  <validation>All requirements validated against industry standards and security frameworks</validation>
</reasoning>

### Data Security and Integrity
- **Data Changes**: Must draft idempotent and reversible migrations
- **Backup Strategy**: All data changes must have rollback plans  
- **Transaction Integrity**: Ensure ACID properties are maintained

### API Security
- **Authentication**: Must implement complete authentication mechanisms
- **Authorization Control**: Must implement fine-grained authorization control
- **Input Validation**: Must perform strict validation on all inputs
- **Data Sanitization**: Must perform appropriate sanitization on all outputs
- **Confidentiality Handling**: Never expose sensitive information in logs or responses

### Performance Requirements
- **Latency Targets**: Must meet specified latency requirements in the plan
- **Throughput Targets**: Must meet specified throughput requirements in the plan
- **Memory Targets**: Must comply with memory usage limits
- **Monitoring Implementation**: Must implement appropriate performance monitoring

### Testing Requirements
- **Test-First Approach**: Should write tests before implementation; if not achieved, record reasons and remediation plans
- **Test Types**:
  - Unit Tests: Aligned with F-IDs
  - Integration Tests: Test inter-service interactions
  - Contract Tests: Ensure API contract compliance
- **Coverage Threshold**: Must meet specified test coverage requirements

### Architecture Principles
- **SOLID Principles**: Must apply SOLID design principles
- **Clean Architecture**: Must implement separation of concerns
- **Error Handling**: Must implement appropriate error handling mechanisms
- **Logging**: Must implement structured logging
- **Monitoring**: Must implement appropriate system monitoring

### Reliability Requirements
- **Graceful Degradation**: System must handle failures gracefully
- **Idempotency**: API operations must be designed as idempotent
- **Retry Mechanisms**: Must implement appropriate retry strategies
- **Circuit Breaker**: Must implement circuit breaker pattern for dependency failures

<output>
  <report>
    <summary>Backend development enforcement standards with comprehensive security and performance requirements</summary>
    <details>Covers data integrity, API security, performance optimization, testing coverage, architecture principles, and reliability requirements</details>
    <checklist>
      <item checked="true">All inputs are validated and sanitized</item>
      <item checked="true">All outputs are appropriately encoded</item>
      <item checked="true">Sensitive data is encrypted at rest</item>
      <item checked="true">APIs implement proper authentication and authorization</item>
      <item checked="true">Error handling does not expose sensitive information</item>
      <item checked="true">Logging does not contain sensitive data</item>
      <item checked="true">Dependencies are latest and secure versions</item>
    </checklist>
  </report>
</output>

<security>
  <read_only_paths>
    <path>sunnycore/dev/workflow/backend-developer-workflow.md</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="password|secret|key|token" action="redact"/>
  </sensitive_filters>
  <access_control>
    <permission level="developer" scope="backend_development"/>
  </access_control>
</security>

<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="security_violation">
      <description>Critical security check failed</description>
      <action>immediate_stop</action>
    </condition>
    <condition type="missing_critical_workflow">
      <description>Required workflow file not accessible</description>
      <action>record_warning_continue</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>EMERGENCY_STOP</status>
    <partial_results>Security validation completed with violations detected</partial_results>
  </minimal_viable_output>
</fast_stop_mechanism>