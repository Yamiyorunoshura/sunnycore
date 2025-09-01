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
</enforcement>

---

<stage name="Plan Verification Phase" number="1">
<description>Check and verify the existence and completeness of implementation plans</description>

<execution_actions>
- Read the implementation plan corresponding to task_id from `{project_root}/docs/implementation-plan/{task_id}`(such as `1`, `2`, `3`...)-plan.md` (such as `1-plan.md`, `2-plan.md`, `3-plan.md`...)
- Validate plan format and required fields (metadata, scope, assumptions, constraints)
- Confirm plan scope and constraints
- Verify resolvability of sources paths
</execution_actions>

<validation_checkpoints>
- Plan file exists and is readable
- Required fields complete (task_id, project_name, owner, date)
- Scope definition clear and executable
- Constraints explicit and reasonable
</validation_checkpoints>
</stage>

<stage name="Task Classification Phase" number="2">
<description>Analyze plan content and classify task types and technical domains</description>

<think harder>
<execution_actions>
- Deeply analyze technical domains and complexity involved in plan content
- Intelligently identify frontend, backend, fullstack, or refactoring requirements
- Evaluate inter-task dependencies and synchronous execution possibilities
- Calculate task complexity and required resource estimation
- Check if `docs/review-results/{task_id}-review.md` (such as `1-review.md`, `2-review.md`, `3-review.md`...) exists for previous review documents (brownfield state detection)
- If in brownfield state, read the issue list, repair recommendations, and priorities from `docs/review-results/{task_id}-review.md` (such as `1-review.md`, `2-review.md`, `3-review.md`...) and use them as reference for task classification.
</execution_actions>
</think harder>

<classification_checkpoints>
- Technical domains correctly identified
- Task types accurately classified
- Dependencies clearly mapped
- Brownfield state correctly detected
</classification_checkpoints>
</stage>

<stage name="Agent Assignment Phase" number="3">
<description>Intelligently assign and schedule corresponding specialized agents based on task classification</description>

<think harder>
<execution_actions>
- Select the most appropriate sub-agent based on task type mapping rules in `{project_root}/sunnycore/dev/enforcement/developer-orchestrator-enforcement.md`
- Initiate synchronous execution protocol (when there are no strong dependencies between tasks)
- Apply intelligent agent mapping rules:

    <agent_mapping category="Backend Domain Experts">
    - `database` → `backend-developer_database` (Database design, optimization, migration)
    - `api` → `backend-developer_api` (RESTful API, GraphQL, microservices)
    - `security` → `backend-developer_security` (Authentication, authorization, security protection)
    - `performance` → `backend-developer_performance` (Performance optimization, load testing)
    - `testing` → `backend-developer_testing` (Testing strategy, automated testing)
    - `infrastructure` → `backend-developer_infrastructure` (Deployment, monitoring, DevOps)
    </agent_mapping>

    <agent_mapping category="Frontend Domain Experts">
    - `ui_ux` → `frontend-developer_ui-ux` (User interface, user experience)
    - `framework` → `frontend-developer_framework` (React, Vue, Angular)
    - `performance` → `frontend-developer_performance` (Frontend optimization, bundle optimization)
    - `accessibility` → `frontend-developer_accessibility` (Accessibility design)
    - `testing` → `frontend-developer_testing` (Frontend testing, E2E testing)
    </agent_mapping>

    <agent_mapping category="Fullstack Domain Experts">
    - `architecture` → `fullstack-developer_architecture` (System architecture, technology selection)
    - `integration` → `fullstack-developer_integration` (System integration, third-party services)
    - `performance` → `fullstack-developer_performance` (Fullstack performance optimization)
    - `devops` → `fullstack-developer_devops` (CI/CD, containerization, cloud deployment)
    </agent_mapping>

    <agent_mapping category="Refactoring Domain Experts">
    - `code_quality` → `refactor-developer_code-quality` (Code refactoring, architecture improvement)
    - `performance` → `refactor-developer_performance` (Performance refactoring, optimization refactoring)
    </agent_mapping>

- Establish real-time coordination mechanisms and conflict resolution strategies between agents
- Transmit complete task context, execution parameters, and quality requirements
- If in brownfield state, precisely transmit the issue list and repair recommendations from review documents to relevant agents
</execution_actions>
</think harder>

<assignment_checkpoints>
- Agent selection meets task requirements
- Synchronous execution strategy reasonable
- Coordination mechanism established
- Context transmission complete
</assignment_checkpoints>
</stage>

<stage name="Progress Monitoring Phase" number="4">
<description>Real-time monitoring of execution status and progress of all active agents</description>

<execution_actions>
- Establish real-time tracking dashboard for agent execution progress
- Monitor system resource usage (CPU, memory, network)
- Intelligently detect potential bottlenecks, risks, and abnormal patterns
- Maintain detailed execution status logs and timeline records
- If in brownfield state, specially monitor progress and quality of issue remediation
- Implement early warning mechanisms to identify potential execution issues in advance
</execution_actions>

<monitoring_checkpoints>
- All agent statuses visible
- Resource usage within reasonable ranges
- No blocking bottlenecks
- Execution logs completely recorded
</monitoring_checkpoints>
</stage>

<stage name="Problem Resolution Phase" number="5">
<description>Identify and resolve issues and conflicts during execution process</description>

<think>
<execution_actions>
- Intelligently detect conflicts between agents, dependency issues, and resource competition
- Coordinate technical decision conflicts and implementation strategy differences
- Implement automatic recovery and manual intervention mechanisms for abnormal situations
- Dynamically optimize execution strategies and resource allocation
- If in brownfield state, ensure all issues from previous reviews are properly resolved and verified
- Establish issue escalation mechanisms to handle complex technical decisions
</execution_actions>
</think>

<resolution_checkpoints>
- Inter-agent conflicts resolved
- Technical decisions reached consensus
- Abnormal situations recovered
- Brownfield issues remediation completed
</resolution_checkpoints>
</stage>

<stage name="Completion Report Phase" number="6">
<description>Generate development records and final reports</description>

<think hard>
<execution_actions>
- Collect and integrate all agents' execution results, decision records, and deliverables
- Read standard template `{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml`
- Fill content according to template and convert to markdown format, output to `{project_root}/docs/dev-notes/` path, with filename `{task_id}`(such as `1`, `2`, `3`...)-dev-notes.md` (such as `1-dev-notes.md`, `2-dev-notes.md`, `3-dev-notes.md`...)
- Verify completeness of development record format and accuracy of content
- If in brownfield state, detail issue remediation status, verification results, and quality improvements in development records
- Generate execution summary, key decision records, and follow-up recommendations
- Establish traceable deliverable lists and quality inspection reports
</execution_actions>
</think hard>

<completion_checkpoints>
- All agent results collected
- Development record format correct
- Content complete and accurate
- Brownfield remediation status recorded and dev notes file updated (especially iteration count related details)
- Deliverable list complete
</completion_checkpoints>
</stage>


