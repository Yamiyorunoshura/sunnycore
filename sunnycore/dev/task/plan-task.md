# Task Planning Execution Instruction

<task_overview>
As a task planning coordination expert, you need to comprehensively plan specified tasks to ensure implementation plan feasibility and optimal execution strategies.
</task_overview>

## Core Planning Stages

<optimization_phases>

### Phase One: Mandatory Prerequisites Validation
<phase name="mandatory_prerequisite_validation" complexity="think">
**Objective**: Load and validate all necessary execution standards and workflow definitions

**Execution Steps**:
1. **Load Mandatory Execution Standards**: Completely read `{project_root}/sunnycore/dev/enforcement/developer-orchestrator-enforcement.md`
   - This contains all mandatory execution rules and validation standards
   - If unable to load, immediately stop and report error

2. **Load Workflow Definitions**: Completely read `{project_root}/sunnycore/dev/workflow/developer-orchestrator-workflow.md`
   - Understand all stages, checkpoints, and validation requirements
   - If unable to load, immediately stop and report error

**Validation Checkpoints**:
- [ ] Mandatory execution standards fully loaded
- [ ] Workflow definitions fully loaded
- [ ] All execution rules understood and ready for application

**Expected Outcomes**: Establish complete standards and workflow understanding foundation
</phase>

### Phase Two: Project Information Collection and Analysis
<phase name="project_information_analysis" complexity="think hard">
**Objective**: Comprehensively understand project background and establish planning foundation

**Execution Steps**:
3. **Load Project Specifications**: Completely read all documents under `{project_root}/docs/specs/` path
   - Analyze project architecture and technology stack
   - Identify project dependencies and constraints
   - Understand overall project goals and business requirements

**Validation Checkpoints**:
- [ ] Project specifications fully read and understood
- [ ] Project context model established
- [ ] Technical constraints and dependencies identified

**Expected Outcomes**: Establish complete project understanding and planning context
</phase>

### Phase Three: Task Planning Delegation Execution
<phase name="task_planning_delegation" complexity="think">
**Objective**: Delegate well-prepared task context to specialized planning agent

**Execution Steps**:
4. **Delegate to Sub-agent**: Pass task to sub-agent `task-planner`
   - Provide complete project context and specification information
   - Ensure all necessary planning data is prepared
   - Monitor planning process and provide necessary support

**Validation Checkpoints**:
- [ ] All necessary information prepared completely
- [ ] Sub-agent successfully received task
- [ ] Planning context correctly transmitted

**Expected Outcomes**: Successful initiation and execution of specialized task planning
</phase>

</optimization_phases>

## Quality Assurance Mechanism

<quality_assurance>
<validation_criteria>
- [ ] Standards Loading Completeness: All necessary standard documents loaded and understood
- [ ] Project Understanding Depth: Project context analysis sufficient and accurate
- [ ] Delegation Readiness: All necessary information prepared for sub-agent use
- [ ] Process Consistency: Follow unified task planning workflow
- [ ] Error Handling: Appropriate error checking and exception handling mechanisms
</validation_criteria>
</quality_assurance>