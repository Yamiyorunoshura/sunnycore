# Development Task Execution Instruction

<task_overview>
When this instruction is called, you will act as a developer to execute comprehensive development tasks.
</task_overview>

## Execution Steps

<stage name="Mandatory Prerequisites Validation" number="1" critical="true">
<description>Load and validate all necessary execution standards and workflow definitions</description>

<execution_actions>
1. **Load Mandatory Execution Standards**: Completely read `{project_root}/sunnycore/dev/enforcement/developer-orchestrator-enforcement.md`
   - This contains all mandatory execution rules and validation standards
   - If unable to load, immediately stop and report error

2. **Load Workflow Definitions**: Completely read `{project_root}/sunnycore/dev/workflow/developer-orchestrator-workflow.md`
   - Understand all stages, checkpoints, and validation requirements
   - If unable to load, immediately stop and report error
</execution_actions>

<validation_checkpoints>
- [ ] Mandatory execution standards fully loaded
- [ ] Workflow definitions fully loaded
- [ ] All execution rules understood and ready for application
</validation_checkpoints>
</stage>

<stage name="Project Context Understanding" number="2" critical="true">
<description>Establish complete project context model and implementation plan validation</description>

<execution_actions>
3. **Project Specifications Loading**: Read all documents under `{project_root}/docs/specs/` path
   - Understand project requirements, specifications, architecture design
   - Establish complete project context model
   - Identify key dependencies and constraints

4. **Implementation Plan Validation**: Confirm `{project_root}/docs/implementation-plan/{task_id}`(e.g.`1`, `2`, `3`...)-plan.md` (e.g.`1-plan.md`, `2-plan.md`, `3-plan.md`...) exists and is readable
   - **Critical Checkpoint**: If implementation plan does not exist, immediately stop and notify user that planning phase needs to be executed first
   - Validate plan completeness and executability
</execution_actions>

<validation_checkpoints>
- [ ] Project specifications fully understood
- [ ] Project context model established
- [ ] Implementation plan exists and format is correct
- [ ] Plan content complete and executable
</validation_checkpoints>
</stage>

<stage name="Development Execution" number="3" critical="true">
<description>Strictly execute development work according to workflow</description>

<execution_actions>
5. **Workflow Execution**: Strictly execute development work according to loaded workflow documents
   - Follow all stage sequences and checkpoint requirements
   - Ensure each validation point passes before continuing
   - Record all key decisions and implementation details
</execution_actions>

<validation_checkpoints>
- [ ] All workflow stages executed in sequence
- [ ] Each checkpoint passed validation
- [ ] Key decisions and implementation details recorded
</validation_checkpoints>
</stage>

<stage name="Write Development Log" number="4" critical="true">
<description>Write development log and record all key decisions and implementation details</description>

<execution_actions>
6. **Development Log Writing**: Write development log and record all key decisions and implementation details
   - Read the `development execution` stage from `Users/tszkinlai/Coding/cursor-claude/core/dev/templates/dev-note.md`
   - Write development log to `{project_root}/docs/dev-note/{task_id}`(e.g.`1`, `2`, `3`...)-dev-note.md` (e.g.`1-dev-note.md`, `2-dev-note.md`, `3-dev-note.md`...)
   - Development log must contain all key decisions and implementation details
</execution_actions>

<validation_checkpoints>
- [ ] Development log written
- [ ] Development log records all key decisions and implementation details
</validation_checkpoints>
</stage>

<critical_execution_principles>
- **All development work must be based on validated implementation plans**
- **Strictly follow all requirements in mandatory execution standards**
- **Ensure consistency with project specifications and architecture design**
- **Maintain complete development tracking records**
</critical_execution_principles>

<failure_handling>
<scenario type="Prerequisites Failure">
Immediately stop, report specific missing files or conditions
</scenario>

<scenario type="Plan Missing">
Stop development, guide user to execute `*plan-task {task_id}`(e.g.`1`, `2`, `3`...)` command first
</scenario>

<scenario type="Workflow Interruption">
Record interruption point, provide recovery guidance
</scenario>
</failure_handling>