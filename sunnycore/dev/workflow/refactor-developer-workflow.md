# Refactor Developer Workflow

<enforcement>
## 🔄 Workflow Todo List Creation

### 📋 Necessary Preparations Before Starting Execution

**Important Reminder**: Before starting any workflow steps, you must use a todo list to create a todo list to organize these steps.

**Creation Process**:
1. **Analyze Workflow Structure** - Carefully read the entire workflow file, identify all stages, steps, and tasks
2. **Extract Key Tasks** - Convert core tasks of each stage into specific todo items
3. **Set Priorities** - Set priorities based on task importance and dependency relationships
4. **Create Todo List** - Use `todo_write` tool to create a structured todo list containing all steps
5. **Execute and Update** - Execute tasks in todo list order, update status in a timely manner

### 📝 Todo List Requirements
- **Coverage**: Each major stage should have corresponding todo items
- **Validation Points**: Key validation checkpoints must be included in the todo list
- **Priorities**: Set reasonable priorities to ensure dependencies are respected
- **State Management**: Update todo status in a timely manner during execution (pending → in_progress → completed)
- **Uniqueness**: Only one task can be in `in_progress` state at the same time
- **Completeness**: Only mark as `completed` when tasks are completely finished
</enforcement>

<workflow type="refactor-developer">

## Mandatory Preconditions Validation
<mandatory-preconditions>

### 1. Load Execution Standards

<stage name="Load Execution Standards" number="1" critical="true">
**Mandatory Execution Standards Loading**
- **Description**: Completely read `{project_root}/sunnycore/dev/enforcement/refactor-developer-enforcement.md`
- **Requirements**:
  <requirements>
  - Understand all mandatory rules, refactoring standards, and quality gates
  - If unable to load, immediately stop and report error
  </requirements>

</stage>

### 2. Project Context Establishment

<stage name="Project Context Establishment" number="2" critical="true">

**Project Specifications Understanding**

- **Description**: Read all documents under `{project_root}/docs/specs/` path
- **Requirements**:
  <requirements>
  <think>
  Refactor Developer needs to focus on the following types of project specification content:

  1. **Architecture Design Specifications**:
     - Existing system architecture design and component relationships
     - Design pattern usage and architectural debt
     - Inter-module dependency relationships and coupling analysis
     - Scalability bottlenecks and improvement opportunities

  2. **Code Quality Specifications**:
     - Coding standards, naming conventions, and style guides
     - Code review standards and quality gates
     - Technical debt identification standards and priorities
     - Refactoring safety and test coverage requirements

  3. **Performance and Optimization Specifications**:
     - Performance benchmarks and bottleneck identification standards
     - Memory usage, CPU efficiency, and I/O optimization requirements
     - Algorithm complexity improvement targets
     - Resource usage monitoring and optimization indicators

  4. **Maintainability Specifications**:
     - Code readability and documentation standards
     - Modular design and reusability requirements
     - Error handling and logging standards
     - Version compatibility and migration strategies

  5. **Security Specifications**:
     - Security vulnerability repair standards and verification processes
     - Secure coding practices and risk assessments
     - Sensitive data handling and encryption requirements
     - Dependency security and vulnerability scanning standards

  6. **Testing and Validation Specifications**:
     - Pre/post-refactoring testing strategies and coverage requirements
     - Regression testing and integration testing standards
     - Performance testing and load testing benchmarks
     - Automated testing and continuous integration requirements
  </think>

  Based on the above thinking analysis, execute the following tasks:
  - Understand project requirements, existing architecture design, and code quality standards
  - Establish project context model covering technical debt, performance bottlenecks, and maintainability issues
  - Identify refactoring target areas, risk points, and dependencies
  - Pay special attention to code architecture improvement opportunities, performance optimization space, and security enhancement needs
  - Confirm refactoring scope boundaries, testing strategies, and backward compatibility requirements
  - Evaluate refactoring complexity and resource requirements, formulate incremental improvement plans
  </requirements>

**Implementation Plan Verification**
- **Description**: Confirm `{project_root}/docs/implementation-plan/{task_id}`(such as `1`, `2`, `3`...)-plan.md` exists and is readable
<critical-checkpoint>
If implementation plan does not exist, immediately stop and notify user that planning stage needs to be executed first
</critical-checkpoint>

- **Requirements**:
  <requirements>
  <think hard>
  - Validate plan completeness, scope definition, and refactoring feasibility
  - Confirm refactoring goals and quality improvement requirements
  <think hard>
  </requirements>

</stage>

### 3. Refactoring Specialization Preparation

<stage name="Refactoring Specialization Preparation" number="3" critical="true">
**Refactoring Checklist Preparation**
Prepare refactoring checklist according to mandatory execution standards:

<refactor-checklist>
<ultra think>
- [ ] Analyze plan content, identify refactoring scope and goals
- [ ] Assess existing code quality and technical debt
- [ ] Confirm refactoring strategy and risk assessment
- [ ] Establish incremental refactoring and test-driven development (TDD) strategy
- [ ] Validate backward compatibility and performance impact
<ultra think>
</refactor-checklist>

**Quality Target Confirmation**
Confirm and record refactoring quality requirements:
<quality-targets>
<think>
- Code readability and maintainability improvement targets
- Performance optimization and resource usage improvements
- Technical debt reduction and architecture improvement indicators
<think>
</quality-targets>
</stage>
</mandatory-preconditions>

---

## Development Execution Process
<development-execution>

### 4. Refactoring Analysis Process

<stage name="Refactoring Analysis" number="4" critical="true">
**Deep Code Analysis**
- **Description**: Comprehensive analysis of existing code structure and refactoring requirements
- **Requirements**:
  <requirements>
  <Ultra think>
  - Identify code smells and design pattern issues
  - Analyze dependency relationships and coupling degree
  - Assess refactoring risks and impact scope
  - Formulate detailed refactoring step plan
  <Ultra think>
  </requirements>

**Refactoring Strategy Formulation**
Formulate refactoring strategy based on analysis results:
<refactor-strategy>
<ultra think>
- Determine refactoring priorities and execution sequence
- Select appropriate refactoring techniques and patterns
- Establish safety net tests and rollback mechanisms
- Formulate incremental delivery plan
<ultra think>
</refactor-strategy>
</stage>

### 5. TDD Refactoring Process

<stage name="Test-Driven Refactoring" number="5" critical="true">
**Perform Refactoring According to TDD Process**
- **Description**: Follow test-first refactoring methodology
- **Requirements**:
  <requirements>
  <Ultra think>
  - Establish comprehensive test coverage to ensure refactoring safety
  - Adopt small-step, high-frequency refactoring strategy
  - Continuously validate functional correctness and performance
  - Maintain code quality and design principles
  <Ultra think>
  </requirements>

**Refactoring Execution Checkpoints**
Continuously validate during refactoring process:
<refactor-checkpoints>
<think hard>
- Test pass rate after each refactoring step
- Code coverage and quality indicator improvements
- Performance indicators and resource usage changes
- Architectural consistency and design principle adherence
<think hard>
</refactor-checkpoints>
</stage>
</development-execution>
</workflow>