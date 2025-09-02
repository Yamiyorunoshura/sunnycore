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
- **Limited Parallelism**: Maximum 2-3 tasks can be in `in_progress` status simultaneously (for independent review phases)
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

**State Management Requirements**:
<state_management_phase_1>
- **Phase Entry**: Update status to "in_progress", current_phase to "project_information_gathering", progress_percentage to 10%
- **Heartbeat Updates**: Update last_heartbeat every 5-10 minutes during phase execution
- **Phase Completion**: Update progress_percentage to 25% upon phase completion
</state_management_phase_1>

**Execution Steps**:
1. Read `{project_root}/docs/specs/` to obtain basic project information
   - Analyze project architecture and technology stack
   - Identify project dependencies
   - Understand overall project objectives and constraints
   - **State Update**: Progress to 15% after specs loading

2. Read `{project_root}/docs/specs/task.md` to obtain detailed specifications for {task_id}(such as `1`, `2`, `3`...)
   - Parse task requirements and acceptance criteria
   - Identify technical requirements and performance indicators
   - Confirm task priorities and schedule constraints
   - **State Update**: Progress to 25% after task analysis

**Expected Results**: Establish complete project and task understanding foundation
</phase>

### Phase 2: Implementation Plan Analysis
<phase name="implementation_plan_analysis" complexity="think hard">
**Goal**: Deep assessment of implementation plan reasonableness and completeness

**State Management Requirements**:
<state_management_phase_2>
- **Phase Entry**: Update current_phase to "implementation_plan_analysis", progress_percentage to 30%
- **Heartbeat Updates**: Continue regular heartbeat updates during analysis
- **Phase Completion**: Update progress_percentage to 50% upon phase completion
</state_management_phase_2>

**Execution Steps**:
3. Read `{project_root}/docs/implementation-plan/{task_id}`(such as `1`, `2`, `3`...)-plan.md` to obtain implementation plan
   - Evaluate technical feasibility of plan
   - Check reasonableness of resource allocation
   - Verify realism of schedule arrangements
   - Identify potential risk points and dependencies
   - **State Update**: Progress to 50% after plan analysis

**Validation Checkpoints**:
- [ ] Consistency between plan and requirements specifications
- [ ] Executability of technical solutions
- [ ] Accuracy of resource estimates
- [ ] Completeness of risk identification
</phase>

### Phase 3: Quality Review Execution
<phase name="quality_review_execution" complexity="think harder">
**Goal**: Conduct differentiated review based on project status

**State Management Requirements**:
<state_management_phase_3>
- **Phase Entry**: Update current_phase to "quality_review_execution", progress_percentage to 55%
- **Frequent Heartbeat Updates**: Update last_heartbeat every 3-5 minutes during intensive review work
- **Progress Milestones**: Update progress incrementally based on review completion (60%, 70%, 80%, 90%)
- **Error Handling**: Update status to "error" if critical issues block review progress
</state_management_phase_3>

**Review Strategy**:
4. Conduct comprehensive review of project according to your own assessment methods
   - **State Update**: Progress to 60% after review strategy determination

**Greenfield Project Review Focus**:
- Reasonableness of architecture design
- Adherence to code standards
- Test coverage and quality
- Documentation completeness
- Security considerations
- **State Update**: Progress incrementally (70%, 80%) based on review dimension completion

**Brownfield Project Review Focus**:
- Prioritize review of previously identified issue lists
  - Verify issue remediation status
  - Evaluate effectiveness of remediation solutions
  - Confirm no introduction of new side effects
- Conduct new issue identification and evaluation
  - Code quality regression checks
  - Impact analysis of new functionality
  - System integration verification
- **State Update**: Progress incrementally (70%, 80%) based on review completion

**Quality Assessment Dimensions**:
- Functional correctness
- Performance efficiency
- Maintainability
- Reliability
- Security
- Usability
- **State Update**: Progress to 90% after completing all quality assessments
</phase>

### Phase 4: Result Integration and Reporting
<phase name="result_integration_reporting" complexity="think">
**Goal**: Structure review results and communicate effectively

**State Management Requirements**:
<state_management_phase_4>
- **Phase Entry**: Update current_phase to "result_integration_reporting", progress_percentage to 92%
- **Final Heartbeat**: Update last_heartbeat before entering completion protocol
- **Pre-Completion Preparation**: Progress to 95% before initiating two-phase completion
</state_management_phase_4>

**Execution Steps**:
5. Organize all obtained information
   - Aggregate identified issues and risks
   - Provide specific improvement recommendations
   - Evaluate overall quality level
   - Formulate follow-up action plans
   - **State Update**: Progress to 95% after information organization

**Output Format**:
- Executive summary
- Detailed findings list
- Risk assessment matrix
- Improvement recommendations priority ranking
- Follow-up monitoring points

6. **State-Managed Completion Protocol**
   <state_managed_completion>
   **Phase 6a: Pre-completion State Update**
   - Update reviewer status to "completing" in session state
   - Set progress_percentage to 95%
   - Generate preliminary report summary
   - Signal readiness to orchestrator via state update
   
   **Phase 6b: Orchestrator Acknowledgment**
   - Wait for orchestrator acknowledgment signal
   - Monitor session state for orchestrator response
   - Maintain "completing" status during wait period
   
   **Phase 6c: Final Completion**
   - Upon receiving orchestrator acknowledgment
   - Update status to "completed" in session state
   - Set progress_percentage to 100%
   - Record completion timestamp
   - Send final report to main agent
   - Terminate reviewer session gracefully
   
   **Note**: Remember that in this phase you as reviewer do not need to write review results to any files - the orchestrator handles final report generation.
   </state_managed_completion>

**🔄 Orchestrator Parallel Coordination Guidance**
<orchestrator_parallel_coordination>
**Parallel Execution Responsibilities as a Called Reviewer**:

#### Execution Environment Awareness
- **Parallel Awareness**: Understand that you are one of multiple reviewers called in parallel by orchestrator
- **Responsibility Boundaries**: Strictly execute according to review focus specified by orchestrator, avoid overstepping
- **State Synchronization**: Timely update progress status to facilitate orchestrator monitoring and coordination

#### Parallel Execution Best Practices
1. **Rapid Startup**: Start execution immediately upon receiving call, don't wait for other reviewers
2. **Focused Execution**: Focus on assigned review dimensions, don't duplicate other reviewers' work
3. **Regular Heartbeat**: Update progress_percentage and last_heartbeat every 5-10 minutes
4. **Avoid Conflicts**: Don't attempt to read or modify resources that other reviewers might use

#### State Update Protocol
```yaml
# Standard state updates as parallel reviewer
reviewer_state_updates:
  startup:
    status: "registered" → "starting" → "in_progress"
    heartbeat_frequency: "every_5_minutes"
    
  progress_reporting:
    progress_percentage: # Update based on actual completion 0-95%
    current_phase: # Current execution phase
    
  completion_signaling:
    pre_completion: # status: "completing", progress: 95%
    final_completion: # status: "completed", progress: 100%
```

#### Exception Handling
- **Autonomous Recovery**: Attempt autonomous recovery when encountering non-fatal errors, don't affect other reviewers
- **Failure Isolation**: If termination is necessary, ensure errors don't propagate to other parallel reviewers
- **Status Reporting**: Timely report error status to allow orchestrator to adjust coordination strategy
</orchestrator_parallel_coordination>
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