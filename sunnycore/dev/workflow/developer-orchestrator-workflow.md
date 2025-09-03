---
category: dev
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: developer-orchestrator-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '1.0'
---

# Developer Orchestrator Workflow

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
- **Parallel Execution**: Support multiple tasks in `in_progress` status simultaneously to improve efficiency
- **Dependency Management**: Ensure tasks with dependencies execute in correct order
- **Completeness**: Only mark as `completed` when the task is fully completed
<!-- enforcement>

---

<stage name="Plan Verification Phase" number="1" -->
<description>Check and verify the existence and completeness of implementation plans<!-- description>

<execution_actions -->
- Read the implementation plan corresponding to task_id from `{project_root}/docs/implementation-plan/{task_id}`(such as `1`, `2`, `3`...)-plan.md` (such as `1-plan.md`, `2-plan.md`, `3-plan.md`...)
- Validate plan format and required fields (metadata, scope, assumptions, constraints)
- Confirm plan scope and constraints
- Verify resolvability of sources paths
<!-- execution_actions>

<validation_checkpoints -->
- Plan file exists and is readable
- Required fields complete (task_id, project_name, owner, date)
- Scope definition clear and executable
- Constraints explicit and reasonable
<!-- validation_checkpoints>


<stage name="Task Classification Phase" number="2">
<description>Analyze plan content and classify task types and technical domains<!-- description>

<think harder -->
<execution_actions>
- Deeply analyze technical domains and complexity involved in plan content
- Intelligently identify frontend, backend, fullstack, or refactoring requirements
- Evaluate inter-task dependencies and synchronous execution possibilities
- Calculate task complexity and required resource estimation
- Check if `docs/review-results/{task_id}-review.md` (such as `1-review.md`, `2-review.md`, `3-review.md`...) exists for previous review documents (brownfield state detection)
- If in brownfield state, read the issue list, repair recommendations, and priorities from `docs/review-results/{task_id}-review.md` (such as `1-review.md`, `2-review.md`, `3-review.md`...) and use them as reference for task classification.
<!-- execution_actions>


<classification_checkpoints>
- Technical domains correctly identified
- Task types accurately classified
- Dependencies clearly mapped
- Brownfield state correctly detected
<!-- classification_checkpoints>


<stage name="Developer Team Formation" number="2.5">
<description>Analyze development requirements and assemble appropriate developer team based on task classification<!-- description>

<think harder -->
<execution_actions>
- **Development Content Analysis**: Based on task classification results, analyze the development content to be implemented
- **Technical Domain Identification**: Identify specific technical domains involved (backend, frontend, fullstack, refactoring)
- **Development Dimension Assessment**: Determine development dimensions needed (database, api, security, performance, testing, infrastructure, ui-ux, framework, accessibility, architecture, integration, devops, code-quality)
- **Developer Team Assembly**: Select appropriate developer agents based on content analysis and domain requirements
- **Team Coordination Strategy**: Define coordination approach for selected developer team to ensure efficient collaboration
<!-- execution_actions>

**Development Content Analysis**
<content_analysis_task -->
- **Description**: Analyze the development content based on implementation plan and task classification results
- **Analysis Requirements**:
  <analysis_requirements>
  - Identify primary technical domains (backend, frontend, fullstack, refactoring)
  - Determine specific development dimensions within each domain
  - Assess development complexity and scope requirements
  - Consider brownfield status and previous review recommendations
  - Evaluate inter-domain dependencies and integration requirements
  <!-- analysis_requirements>


**Developer Team Assembly**
<team_assembly_task>
- **Description**: Select and assemble appropriate developer agents based on content analysis
- **Available Developer Agents**:
  <available_developers>
  - **Backend Domain Experts**:
    - `backend-developer_database`: Database design, optimization, migration
    - `backend-developer_api`: RESTful API, GraphQL, microservices
    - `backend-developer_security`: Authentication, authorization, security protection
    - `backend-developer_performance`: Performance optimization, load testing
    - `backend-developer_testing`: Testing strategy, automated testing
    - `backend-developer_infrastructure`: Deployment, monitoring, DevOps
  - **Frontend Domain Experts**:
    - `frontend-developer_ui-ux`: User interface, user experience
    - `frontend-developer_framework`: React, Vue, Angular
    - `frontend-developer_performance`: Frontend optimization, bundle optimization
    - `frontend-developer_accessibility`: Accessibility design
    - `frontend-developer_testing`: Frontend testing, E2E testing
  - **Fullstack Domain Experts**:
    - `fullstack-developer_architecture`: System architecture, technology selection
    - `fullstack-developer_integration`: System integration, third-party services
    - `fullstack-developer_performance`: Fullstack performance optimization
    - `fullstack-developer_devops`: CI/CD, containerization, cloud deployment
  - **Refactoring Domain Experts**:
    - `refactor-developer_code-quality`: Code refactoring, architecture improvement
    - `refactor-developer_performance`: Performance refactoring, optimization refactoring
  <!-- available_developers>
- **Selection Criteria**:
  <selection_criteria -->
  - **Domain-Specific Selection**: Select developers based on primary technical domains identified
  - **Complexity-Based Selection**: Include specialized developers for complex requirements (performance, security, testing)
  - **Integration Requirements**: Include fullstack developers for multi-domain integration tasks
  - **Quality Assurance**: Include testing developers for comprehensive test coverage
  - **Refactoring Needs**: Include refactoring developers for code quality improvement or performance optimization
  - **Infrastructure Requirements**: Include infrastructure/devops developers for deployment and operational concerns
  <!-- selection_criteria>
- **Team Formation Rules**:
  <formation_rules -->
  - Minimum team size: 1 developer (domain-specific primary developer)
  - Maximum team size: 8 developers (comprehensive coverage across all domains)
  - Ensure comprehensive coverage without redundancy
  - Consider development efficiency and resource optimization
  - Prioritize parallel execution capabilities
  <!-- formation_rules>


**Development Coordination Strategy**
<coordination_strategy>
- **Description**: Define coordination approach for selected developer team
- **Coordination Requirements**:
  <coordination_requirements>
  - Assign specific development focus areas to each developer to avoid overlap
  - Define development sequence and dependencies if any
  - Establish communication protocols between developers
  - Set development completion timeline and checkpoints
  - Ensure consistency across different development domains
  <!-- coordination_requirements>

<!-- think harder>

<team_formation_checkpoints -->
- Development content analysis completed and technical domains identified
- Developer team formation appropriate and coverage complete
- Development coordination strategy defined and communicated
- Team selection meets development requirements and complexity
- Parallel execution strategy prepared
<!-- team_formation_checkpoints>


<stage name="Agent Assignment Phase" number="3">
<description>Execute coordinated development using the assembled developer team from Stage 2.5<!-- description>

<think harder -->
<execution_actions>
- **Coordinated Team Execution**: Execute development using the assembled developer team from Stage 2.5
- **Simultaneous Agent Invocation**: Invoke all selected developer agents from the formed team simultaneously
- **Parallel Execution Protocol**: Initiate parallel execution protocol for maximum efficiency when there are no strong dependencies
- **Context Distribution**: Provide each developer with specific focus areas, development scope, and coordination requirements
- **Real-time Coordination**: Establish real-time coordination mechanisms and conflict resolution strategies between agents
- **Quality Requirements Transmission**: Transmit complete task context, execution parameters, and quality requirements to all team members
- **Brownfield Integration**: If in brownfield state, precisely transmit the issue list and repair recommendations from review documents to relevant agents
- **Progress Monitoring**: Monitor all developers' progress and quality in real-time
- **Cross-Domain Validation**: Ensure consistency and integration between different development domains
<!-- execution_actions>

**Multiple Developer Coordination**
<orchestration_task -->
- **Description**: Execute coordinated development using the assembled developer team from Stage 2.5
- **Execution Requirements**:
  <requirements>
  - Simultaneously invoke all selected developer agents from the formed team
  - Provide each developer with specific focus areas and development scope
  - Ensure parallel execution for maximum efficiency
  - Monitor all developers' progress and quality in real-time
  - Handle any developer failures or delays gracefully
  - Collect results from all developers upon completion
  - Ensure cross-domain consistency and integration
  <!-- requirements>
- **Parallel Execution Strategy**:
  <parallel_strategy -->
  - **Simultaneous Invocation**: Call all selected developers at the same time
  - **Independent Development**: Each developer works on their assigned focus areas independently
  - **Progress Monitoring**: Track completion status of each developer
  - **Result Aggregation**: Collect and organize results from all developers
  - **Quality Assurance**: Ensure all developers complete their implementations thoroughly
  - **Integration Validation**: Validate consistency between different development domains
  <!-- parallel_strategy>
- **Developer Communication**:
  <communication_protocol -->
  - Each developer receives clear instructions on their specific development focus
  - Developers are informed of other team members' areas of responsibility
  - Cross-referencing is encouraged for overlapping concerns and integration points
  - Final results are consolidated by the orchestrator
  - Consistency validation is performed across all development outputs
  <!-- communication_protocol>

<!-- think harder>

<assignment_checkpoints -->
- All selected developer agents from formed team successfully invoked
- Parallel execution strategy implemented and coordinated
- Real-time coordination mechanism established between developers
- Complete task context and focus areas transmitted to all team members
- Cross-domain communication protocols activated
- Progress monitoring systems operational
<!-- assignment_checkpoints>


<stage name="Progress Monitoring Phase" number="4">
<description>Real-time monitoring of execution status and progress of all active developer team members<!-- description>

<execution_actions -->
- Establish real-time tracking dashboard for all developer team members' execution progress
- Monitor system resource usage (CPU, memory, network) across all parallel executions
- Intelligently detect potential bottlenecks, risks, and abnormal patterns in team coordination
- Maintain detailed execution status logs and timeline records for each developer
- Monitor cross-domain integration progress and consistency validation
- If in brownfield state, specially monitor progress and quality of issue remediation across all developers
- Implement early warning mechanisms to identify potential execution issues and team coordination problems in advance
- Track parallel execution efficiency and team collaboration effectiveness
<!-- execution_actions>

<monitoring_checkpoints -->
- All developer team member statuses visible and tracked
- Resource usage within reasonable ranges across all parallel executions
- No blocking bottlenecks in individual developers or team coordination
- Execution logs completely recorded for each developer and team interactions
- Cross-domain integration progress monitored
- Team collaboration effectiveness measured
<!-- monitoring_checkpoints>


<stage name="Problem Resolution Phase" number="5">
<description>Identify and resolve issues and conflicts during team execution process<!-- description>

<think -->
<execution_actions>
- Intelligently detect conflicts between developer team members, dependency issues, and resource competition
- Coordinate technical decision conflicts and implementation strategy differences across multiple developers
- Resolve cross-domain integration conflicts and consistency issues
- Implement automatic recovery and manual intervention mechanisms for abnormal situations in team coordination
- Dynamically optimize execution strategies, resource allocation, and team collaboration patterns
- If in brownfield state, ensure all issues from previous reviews are properly resolved and verified across all team members
- Establish issue escalation mechanisms to handle complex technical decisions requiring team consensus
- Mediate conflicts between different development domains (backend vs frontend vs fullstack)
- Ensure alignment of architectural decisions across all team members
<!-- execution_actions>


<resolution_checkpoints>
- Inter-developer team conflicts resolved
- Cross-domain integration conflicts addressed
- Technical decisions reached consensus across all team members
- Abnormal situations recovered in team coordination
- Brownfield issues remediation completed across all developers
- Architectural alignment achieved across different development domains
<!-- resolution_checkpoints>


<stage name="Completion Report Phase" number="6">
<description>Generate comprehensive development records and final reports from all team members<!-- description>

<think hard -->
<execution_actions>
- Collect and integrate all developer team members' execution results, decision records, and deliverables
- Consolidate cross-domain integration results and consistency validation outcomes
- Read standard template `{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml`
- Fill content according to template and convert to markdown format, output to `{project_root}/docs/dev-notes/` path, with filename `{task_id}`(such as `1`, `2`, `3`...)-dev-notes.md` (such as `1-dev-notes.md`, `2-dev-notes.md`, `3-dev-notes.md`...)
- Verify completeness of development record format and accuracy of content from all team members
- Document team collaboration patterns, coordination effectiveness, and parallel execution outcomes
- If in brownfield state, detail issue remediation status, verification results, and quality improvements across all developers in development records
- Generate comprehensive execution summary including individual and team contributions, key decision records, and follow-up recommendations
- Establish traceable deliverable lists and quality inspection reports covering all development domains
- Document architectural decisions and their impact across different development areas
- Record lessons learned from team coordination and parallel execution
<!-- execution_actions>


<completion_checkpoints>
- All developer team member results collected and integrated
- Cross-domain integration results consolidated
- Development record format correct and comprehensive
- Content complete and accurate from all team members
- Team collaboration patterns and coordination effectiveness documented
- Brownfield remediation status recorded across all developers and dev notes file updated (especially iteration count related details)
- Deliverable list complete covering all development domains
- Architectural decisions and cross-domain impacts documented
- Lessons learned from parallel execution recorded
<!-- completion_checkpoints>



## Quality Assurance Checkpoints

<quality_assurance>
<validation_criteria>
- [ ] All necessary documents successfully loaded and format correct
- [ ] Plan compliance validation completed and task classification accurate
- [ ] Development content analysis completed and technical domains identified
- [ ] Developer team formation appropriate and coverage complete
- [ ] Development coordination strategy defined and communicated
- [ ] All selected developer agents successfully invoked and completed
- [ ] Cross-domain integration validated and consistency ensured
- [ ] Result integration logic clear and without omissions
- [ ] Output format meets standards and easy to read
- [ ] Development records comprehensive and cover all team contributions
- [ ] Orchestrator status report completed
<!-- validation_criteria>


