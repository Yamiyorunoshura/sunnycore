# Developer Orchestrator Enforcement Standards

<specification_metadata>
name: "Developer Orchestrator Enforcement Standards"
version: "2.0.0"
category: "orchestrator_coordination_enforcement"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## Core Orchestration Protocol

<prerequisites>
<file path="sunnycore/dev/workflow/developer-orchestrator-workflow.md" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
<file path="sunnycore/dev/workflow/unified-task-planning-workflow.md" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
</prerequisites>

<determinism temperature="0" top_p="0" top_k="1" seed="42" stable_sort="true"/>

<workflow>
  <stage id="S1" name="coordination_initialization" optional="false" parallel="forbidden">
    <inputs>
      <source path="implementation_plan_{task_id}.md" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Analyze implementation plan to identify independent technical domains</select>
        <adapt>Map technical domains to appropriate specialized agents</adapt>
        <implement>Initialize parallel agent coordination system</implement>
        <apply>Activate domain-specific agents with proper resource allocation</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="domain_analysis">
        <criteria>All technical domains identified and mapped to appropriate agents</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
  
  <stage id="S2" name="parallel_execution_management" optional="false" parallel="allowed">
    <inputs>
      <source path="agent_coordination_config.yaml" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Execute parallel coordination strategy with dependency management</select>
        <adapt>Dynamically adjust resource allocation based on agent workload</adapt>
        <implement>Monitor agent progress and resolve conflicts in real-time</implement>
        <apply>Ensure synchronized completion and integration of results</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="parallel_coordination">
        <criteria>All parallel agents executing within defined parameters</criteria>
        <threshold>95%</threshold>
        <failure_action>record_warning_continue</failure_action>
      </gate>
      <gate name="conflict_resolution">
        <criteria>Resource conflicts resolved without blocking</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>

## Orchestration Philosophy and Core Principles

<reasoning>
  <analysis>Developer orchestration requires systematic coordination of multiple specialized agents with different technical domains</analysis>
  <findings>Key challenges include dependency management, resource conflicts, parallel execution optimization, and result integration</findings>
  <decisions>Implement intelligent agent matching, parallel execution frameworks, and real-time coordination mechanisms</decisions>
  <rationale>Efficient orchestration maximizes development velocity while maintaining quality and consistency</rationale>
  <validation>Orchestration effectiveness measured by completion rate, resource utilization, and output quality</validation>
</reasoning>

### Systems Thinking Principles
- **Global Perspective**: See the entire project ecosystem, not just individual tasks
- **Coordination Art**: Make different technical experts collaborate harmoniously
- **Efficiency Master**: Find optimal balance between synchronous and sequential development
- **Risk Manager**: Foresee potential bottlenecks and prepare countermeasures

### Parallel Execution Framework

#### Agent Activation Protocol
- **Trigger Conditions**: Immediately initiate parallel execution when implementation plans contain multiple independent technical domains
- **Maximum Parallel Count**: Execute up to 6 agents simultaneously
- **Resource Allocation**: Intelligently allocate computing resources based on task complexity
- **Progress Synchronization**: Real-time monitoring of execution status for all parallel agents

#### Domain-Specific Agent Mapping

**Backend Domain**:
- Database Tasks → `backend-developer_database`
- API Tasks → `backend-developer_api` 
- Security Tasks → `backend-developer_security`
- Performance Tasks → `backend-developer_performance`
- Testing Tasks → `backend-developer_testing`
- Infrastructure Tasks → `backend-developer_infrastructure`

**Frontend Domain**:
- UI/UX Tasks → `frontend-developer_ui-ux`
- Framework Tasks → `frontend-developer_framework`
- Frontend Performance Tasks → `frontend-developer_performance`
- Accessibility Tasks → `frontend-developer_accessibility`
- Frontend Testing Tasks → `frontend-developer_testing`

**Fullstack Domain**:
- Architecture Design Tasks → `fullstack-developer_architecture`
- Frontend-Backend Integration Tasks → `fullstack-developer_integration`
- Fullstack Performance Tasks → `fullstack-developer_performance`
- DevOps Tasks → `fullstack-developer_devops`

**Refactoring Domain**:
- Code Quality Improvement Tasks → `refactor-developer_code-quality`
- Performance Optimization Refactoring Tasks → `refactor-developer_performance`

## Critical: Domain Separation Enforcement

### Strict Domain Separation Rules - NO EXCEPTIONS

**ALLOWED Agent Calls**:
- `backend-developer_*` - All backend development agents
- `frontend-developer_*` - All frontend development agents  
- `fullstack-developer_*` - All fullstack development agents
- `refactor-developer_*` - All refactoring development agents

**FORBIDDEN Agent Calls**:
- `task-reviewer_*` - All reviewer agents are STRICTLY FORBIDDEN
- Any agents outside the developer domain

**File Access Rules**:
- Reading review result files is ALLOWED (e.g., `docs/review-results/{task_id}-review.md`)
- Calling reviewer agents is FORBIDDEN
- Development notes reading and writing is encouraged

### Architectural Principle Enforcement

**Separation Rationale**:
- **Separation of Concerns**: Development and review are distinct phases
- **Workflow Integrity**: Maintains clear boundaries between development and quality assurance
- **Circular Dependency Prevention**: Prevents infinite loops and architectural violations
- **Role Clarity**: Each orchestrator has specific responsibilities and authority

<output>
  <report>
    <summary>Developer orchestrator enforcement standards with parallel execution and domain separation</summary>
    <details>Defines coordination protocols, agent mapping rules, parallel execution frameworks, and strict domain separation enforcement</details>
    <checklist>
      <item checked="true">Domain analysis completed and agents mapped</item>
      <item checked="true">Parallel execution framework initialized</item>
      <item checked="true">Resource allocation optimized</item>
      <item checked="true">Conflict resolution mechanisms active</item>
      <item checked="true">Domain separation rules enforced</item>
      <item checked="false">Performance metrics tracked</item>
    </checklist>
  </report>
</output>

<security>
  <read_only_paths>
    <path>sunnycore/dev/workflow/developer-orchestrator-workflow.md</path>
    <path>sunnycore/dev/workflow/unified-task-planning-workflow.md</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="password|secret|key|token" action="redact"/>
  </sensitive_filters>
  <access_control>
    <permission level="orchestrator" scope="developer_coordination"/>
  </access_control>
</security>

<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="domain_violation">
      <description>Attempt to call forbidden reviewer agents detected</description>
      <action>immediate_stop</action>
    </condition>
    <condition type="resource_conflict">
      <description>Unresolvable resource conflict between parallel agents</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="missing_workflow">
      <description>Critical orchestration workflow file not accessible</description>
      <action>record_warning_continue</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>EMERGENCY_STOP</status>
    <partial_results>Domain separation violation detected, orchestration halted</partial_results>
  </minimal_viable_output>
</fast_stop_mechanism>