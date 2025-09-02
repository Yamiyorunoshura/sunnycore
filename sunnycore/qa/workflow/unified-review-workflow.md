# Unified Review Workflow

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
- **Verification Points**: Critical validation checkpoints must be included in todo list
- **Priority**: Set reasonable priorities to ensure dependency relationships are respected
- **Status Management**: Update todo status in a timely manner during execution (pending → in_progress → completed)
- **Uniqueness**: Only one task can be in `in_progress` status at a time
- **Completeness**: Only mark as `completed` when tasks are fully completed
</enforcement>

---

<task_overview>
As a project quality review expert, you need to conduct comprehensive quality review of specified tasks to ensure implementation plan feasibility and code quality standards achievement.
</task_overview>

## Core Review Phases

<optimization_phases>

### Phase 1: Project Information Gathering
<phase name="project_information_gathering" complexity="think">
**Goal**: Comprehensive understanding of project background and task specifications

**Execution Steps**:
1. Read `{project_root}/docs/specs/` to obtain basic project information
   - Analyze project architecture and technology stack
   - Identify project dependencies
   - Understand overall project objectives and constraints

2. Read `{project_root}/docs/specs/task.md` to obtain detailed specifications for {task_id}(such as `1`, `2`, `3`...)
   - Parse task requirements and acceptance criteria
   - Identify technical requirements and performance indicators
   - Confirm task priorities and schedule constraints

**Expected Results**: Establish complete project and task understanding foundation
</phase>

### Phase 2: Implementation Plan Analysis
<phase name="implementation_plan_analysis" complexity="think hard">
**Goal**: Deep assessment of implementation plan reasonableness and completeness

**Execution Steps**:
3. Read `{project_root}/docs/implementation-plan/{task_id}`(such as `1`, `2`, `3`...)-plan.md` to obtain implementation plan
   - Evaluate technical feasibility of plan
   - Check reasonableness of resource allocation
   - Verify realism of schedule arrangements
   - Identify potential risk points and dependencies

**Validation Checkpoints**:
- [ ] Consistency between plan and requirements specifications
- [ ] Executability of technical solutions
- [ ] Accuracy of resource estimates
- [ ] Completeness of risk identification
</phase>

### Phase 3: Quality Review Execution
<phase name="quality_review_execution" complexity="think harder">
**Goal**: Conduct differentiated review based on project status

**Review Strategy**:
4. Conduct comprehensive review of project according to your own assessment methods

**Greenfield Project Review Focus**:
- Reasonableness of architecture design
- Adherence to code standards
- Test coverage and quality
- Documentation completeness
- Security considerations

**Brownfield Project Review Focus**:
- Prioritize review of previously identified issue lists
  - Verify issue remediation status
  - Evaluate effectiveness of remediation solutions
  - Confirm no introduction of new side effects
- Conduct new issue identification and evaluation
  - Code quality regression checks
  - Impact analysis of new functionality
  - System integration verification

**Quality Assessment Dimensions**:
- Functional correctness
- Performance efficiency
- Maintainability
- Reliability
- Security
- Usability
</phase>

### Phase 4: Result Integration and Reporting
<phase name="result_integration_reporting" complexity="think">
**Goal**: Structure review results and communicate effectively

**Execution Steps**:
5. Organize all obtained information
   - Aggregate identified issues and risks
   - Provide specific improvement recommendations
   - Evaluate overall quality level
   - Formulate follow-up action plans

**Output Format**:
- Executive summary
- Detailed findings list
- Risk assessment matrix
- Improvement recommendations priority ranking
- Follow-up monitoring points

6. Send report to main agent and end call (Remember that in this phase you as reviewer do not need to write review results to any files.)
</phase>

</optimization_phases>

## Quality Assurance Mechanism

<quality_assurance>
<validation_criteria>
- [ ] Information Collection Completeness: All necessary documents have been read and analyzed
- [ ] Review Method Appropriateness: Select appropriate review strategy based on project status
- [ ] Problem Identification Accuracy: Identified issues have practical significance and operability
- [ ] Report Structure Clarity: Result organization is logical and easy to understand
- [ ] Recommendation Executability: Provided improvement recommendations are specific and implementable
</validation_criteria>
</quality_assurance>