---
category: dev
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: backend-developer-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '1.0'
---

# Backend Developer Workflow

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
<!-- enforcement>

---

## Context Summarization Protocol

<context-summarization>
**Goal**: Reduce context length by summarizing each completed stage into a compact, structured summary and pruning earlier raw content.

**When to summarize**: Immediately after completing each numbered stage in this workflow.

**How to summarize**:
- Use template `{project_root}/sunnycore/dev/templates/stage-summary-tmpl.yaml`
- Fill `metadata.stage_number`, `metadata.stage_name`, `metadata.task_id`, and `summary` fields
- Keep summary within target 250 words (hard limit 300)
- Include: objective, key decisions, inputs, outputs, notable changes, risks/blockers, next steps, references

**Running summary retention**:
- Merge strategy: append_and_prune
- Keep last 2 full stage summaries
- Collapse older summaries to a 1–2 line epoch summary
- Drop raw context older than 2 stages; carry forward only: open_risks, pending_decisions, critical_dependencies

**Usage**:
- Replace earlier detailed context with the running summary; keep full details only for the current and previous stage
- Optionally persist a lightweight log at `{project_root}/docs/dev-notes/{task_id}-stage-summaries.md`

Example payload (fill at stage end):
```yaml
kind: stage_summary
metadata:
  workflow_name: backend-developer-workflow
  workflow_type: dev
  task_id: "{task_id}"
  stage_number: {n}
  stage_name: "{stage_title}"
  timestamp: "{iso8601}"
summary:
  objective: "..."
  key_decisions: ["...", "..."]
  inputs: ["..."]
  outputs: ["..."]
  notable_changes: ["..."]
  risks_and_blockers: ["..."]
  next_steps: ["..."]
  references: ["path:line_or_anchor"]
```

Quality gate:
- [ ] <= 300 words; [ ] decisions explicit; [ ] risks and next steps captured; [ ] references present when applicable
<!-- context-summarization>

<workflow type="backend-developer" -->

## Mandatory Preconditions Verification
<mandatory-preconditions>

### 1. Load Execution Standards

<stage name="Load Execution Standards" number="1" critical="true">
**Mandatory Execution Standards Loading**
- **Description**: Completely read `{project_root}/sunnycore/dev/enforcement/backend-developer-enforcement.md`
- **Requirements**:
  <requirements>
  - Understand all mandatory rules, security requirements, and quality gates
  - If unable to load, immediately stop and report error
  <!-- requirements>



### 2. Project Context Establishment

<stage name="Project Context Establishment" number="2" critical="true">

**Project Specifications Understanding**

- **Description**: Read all documents under the `{project_root}/docs/specs/` path
- **Requirements**:
  <requirements>
  <think>
  Backend developers need to focus on the following types of project specification content:

  1. **System Architecture Specifications**:
     - Microservices architecture design
     - Database design and relational models
     - API interface design and communication protocols
     - System integration points and external dependencies

  2. **Security Specifications**:
     - Authentication and authorization strategies
     - Data encryption and privacy protection requirements
     - API security standards and rate limiting
     - Security vulnerability protection mechanisms

  3. **Performance and Scalability Specifications**:
     - Performance metrics and benchmarking requirements
     - Load handling and scaling strategies
     - Caching strategies and data optimization
     - Monitoring and logging requirements

  4. **Data Management Specifications**:
     - Data models and structure design
     - Data migration and versioning strategies
     - Backup and disaster recovery plans
     - Data integrity and consistency requirements

  5. **Business Logic Specifications**:
     - Core business processes and rules
     - Transaction processing and state management
     - Error handling and exception management
     - Business validation rules
  <!-- think>

  Based on the above thinking analysis, execute the following tasks:
  - Understand project requirements, architecture design, technical constraints
  - Establish a complete project context model
  - Identify key dependencies and security requirements
  - Pay special attention to backend systems' data flow, API design, and security architecture
  - Confirm performance benchmarks and scalability strategies
  

**Implementation Plan Verification**
- **Description**: Confirm `{project_root}/docs/implementation-plan/{task_id}`(such as `1`, `2`, `3`...)-plan.md` exists and is readable
<critical-checkpoint>
If implementation plan does not exist, immediately stop and notify user that planning stage needs to be executed first
<!-- critical-checkpoint>

- **Requirements**:
  <requirements -->
  <think hard>
  - Validate plan completeness, scope definition, and technical feasibility
  - Confirm security requirements and performance targets
  <think hard>
  <!-- requirements>



### 3. Backend Specialization Preparation

<stage name="Backend Specialization Preparation" number="3" critical="true">
**Security Checklist Preparation**
Prepare security checklist according to mandatory execution standards:

<security-checklist>
<think>
- [ ] Input validation strategy
- [ ] Authentication and authorization mechanisms
- [ ] Data encryption and sensitive information handling
- [ ] API security design
<think>
<!-- security-checklist>

**Performance Targets Confirmation**
Confirm and record performance requirements:
<performance-targets -->
<think>
- Latency targets and throughput requirements
- Memory usage limits
- Monitoring and measurement strategies
<think>
<!-- performance-targets>

<!-- mandatory-preconditions>

---

## Execution Protocol
<execution-protocol -->

### TDD Development Process
<stage name="TDD Development Process" number="4" critical="true">

#### Test-First Development
Strictly follow TDD principles:
<tdd-requirements>
<think harder>
- **Write tests before implementation**
- **Ensure test coverage meets required thresholds**
- **Implement unit tests, integration tests, and contract tests**
<think harder>
<!-- tdd-requirements>

#### Architecture Principles Application
Apply the following principles during development:
<architecture-principles -->
<think harder>
1. **SOLID design principles**
2. **Clean architecture and separation of concerns**
3. **Error handling and logging mechanisms**
<think harder>
<!-- architecture-principles>


### Quality Assurance
<stage name="Quality Assurance" number="5" critical="true">
#### Continuous Validation
Continuously execute during development:
<quality-validations>
<think hard>
- **Static analysis checks**
- **Security vulnerability scanning**
- **Performance benchmarking**
- **Backward compatibility verification**
<think hard>
<!-- quality-validations>

<!-- execution-protocol>

---

## Failure Handling Mechanism
<failure-handling -->
| Failure Scenario | Handling Action |
|---------|---------|
| **Precondition Failure** | Immediately stop, report specific missing files or conditions |
| **Plan Missing** | Stop development, guide user to execute planning stage first |
| **Security Check Failed** | Record risks and require fixes before continuing |
| **Performance Not Met** | Record measurement results and formulate optimization plan |

<critical-failures>
**Any critical failure must immediately stop the process and report**
<!-- critical-failures>



</workflow>
