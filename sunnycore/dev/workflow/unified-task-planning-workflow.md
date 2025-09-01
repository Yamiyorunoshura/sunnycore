# Unified Task Planning Workflow

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
- **Uniqueness**: Only one task can be in `in_progress` status at a time
- **Completeness**: Only mark as `completed` when the task is fully completed
</enforcement>

---

<task_overview>
As a task planning expert, you need to conduct comprehensive and structured planning for specified tasks to ensure the feasibility, completeness, and optimal execution strategy of implementation plans.
</task_overview>

## Core Planning Phases

<optimization_phases>

### Phase 1: Project Specification Understanding and Analysis
<phase name="project_specification_analysis" complexity="think hard">
**Goal**: Comprehensive understanding of project requirements, specifications, and architecture design

**Execution Steps**:
1. **Project Specification Loading**: Completely read all documents under the `{project_root}/docs/specs/` path
   - Analyze project business requirements and functional specifications
   - Identify technical constraints and dependencies
   - Establish project context understanding model
   - Extract key design decisions and principles

2. **Architecture Document Analysis**: Read all documents under the `{project_root}/docs/architecture/` path in detail
   - Understand system architecture design and component relationships
   - Analyze technology stack selection and integration strategies
   - Identify architectural constraints and performance requirements
   - Establish overall system architecture view

**Validation Checkpoints**:
- [ ] Project requirements have been fully understood and recorded
- [ ] Architecture design has been comprehensively analyzed and mastered
- [ ] Technical constraints and dependencies have been identified
- [ ] Project context model has been established

**Expected Results**: Establish complete project understanding foundation to provide accurate context support for subsequent task planning
</phase>

### Phase 2: Task Parsing and Decomposition
<phase name="task_decomposition" complexity="think hard">
**Goal**: Precisely parse and decompose specified tasks and their subtasks

**Execution Steps**:
3. **Task File Parsing**: Read task.md file and perform structured analysis
   - Locate main tasks matching `{task_id}` (such as: 1, 2, 3)
   - Extract all subtasks under that task (such as: 1.1, 1.2, 1.3)
   - Collect unordered list items for each task and subtask
   - Analyze dependencies between tasks and execution order

4. **Task Granularity Decomposition**: Break down tasks into minimum executable units
   - Convert unordered list items into specific functional requirements (F-1, F-2...)
   - Identify non-functional requirements (N-1, N-2...)
   - Define acceptance criteria and measurement standards for each requirement
   - Establish priority ranking for task execution

**Validation Checkpoints**:
- [ ] Specified tasks and subtasks have been correctly identified
- [ ] Task requirements have been decomposed into minimum executable units
- [ ] Functional and non-functional requirements have been clearly classified
- [ ] Acceptance criteria have been completely defined

**Expected Results**: Generate structured, executable task decomposition results to lay the foundation for implementation plans
</phase>

### Phase 3: Implementation Plan Generation and Output
<phase name="implementation_plan_generation" complexity="think harder">
**Goal**: Generate complete implementation plan documents based on templates

**Execution Steps**:
5. **Template Loading and Understanding**: Read template `{project_root}/sunnycore/dev/templates/implementation-plan-tmpl.yaml`
   - Understand template structure and required field requirements
   - Analyze output format specifications and quality standards
   - Prepare planning content that meets template requirements

6. **Plan Content Filling**: Systematically fill task planning results into template
   - Fill in project metadata and context information
   - Map functional and non-functional requirements to template structure
   - Complete execution steps and validation mechanisms
   - Ensure content completeness and consistency

7. **Document Output and Formatting**: Generate final implementation plan document
   - Convert completed plan to Markdown format
   - Output to `{project_root}/docs/implementation-plan/` path
   - Use standardized file naming: `{task_id}-plan.md` (such as: 1-plan.md, 2-plan.md)
   - Perform final format and content validation

**Validation Checkpoints**:
- [ ] Template has been correctly loaded and understood
- [ ] All required fields have been completely filled
- [ ] Plan content meets template specification requirements
- [ ] Document has been successfully output to specified path
- [ ] File naming meets standard specifications

**Expected Results**: Generate high-quality, structured implementation plan documents to provide complete guidance for task execution
</phase>

</optimization_phases>

## Error Handling and Quality Assurance

<quality_assurance>

### Error Handling Mechanism
<error_handling>
- **File Access Error**: When unable to read files at specified paths, record error and provide alternative solutions
- **Format Parsing Error**: When file format does not meet expectations, perform error reporting and attempt repair
- **Content Validation Failure**: When planning content is incomplete, mark missing items and request supplementation
- **Output Path Error**: When target path does not exist, automatically create directory structure
</error_handling>

### Validation Standards
<validation_criteria>
- [ ] **Completeness Verification**: All necessary project specifications and architecture documents have been loaded and analyzed
- [ ] **Accuracy Verification**: Task parsing results are consistent with original requirements
- [ ] **Structural Verification**: Generated plans conform to template specifications and format requirements
- [ ] **Executability Verification**: Plan content is specific, clear, and operable
- [ ] **Traceability Verification**: Clear correspondence exists between plan elements and source requirements
- [ ] **Consistency Verification**: Terminology usage and style remain unified
</validation_criteria>

</quality_assurance>

## Output Format Specifications

<output_format>
**File Path**: `{project_root}/docs/implementation-plan/{task_id}-plan.md`

**File Naming Examples**:
- Main Task 1: `1-plan.md`
- Main Task 2: `2-plan.md`
- Main Task 3: `3-plan.md`

**Content Structure**: Strictly follow `implementation-plan-tmpl.yaml` template specifications, ensure all required fields are completely filled, avoid using generic statements such as "as needed" or "to be determined".
</output_format>