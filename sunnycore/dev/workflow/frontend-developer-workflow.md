---
category: dev
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: frontend-developer-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '1.0'
---

# Frontend Developer Workflow

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
**Goal**: Reduce context length via stage-end structured summaries and pruning.

**When**: Immediately after completing each numbered stage.

**How**:
- Use `{project_root}/sunnycore/dev/templates/stage-summary-tmpl.yaml`
- Fill stage metadata and `summary` fields
- Target 250 words (hard limit 300)
- Include: objective, key decisions, inputs/outputs, notable changes, risks/blockers, next steps, references

**Retention**:
- Append and prune running summary
- Keep last 2 full summaries; collapse older ones to 1–2 line epoch summaries
- Drop raw context older than 2 stages; carry forward only open_risks, pending_decisions, critical_dependencies

Example:
```yaml
kind: stage_summary
metadata:
  workflow_name: frontend-developer-workflow
  workflow_type: dev
  task_id: "{task_id}"
  stage_number: {n}
  stage_name: "{stage_title}"
  timestamp: "{iso8601}"
summary:
  objective: "..."
  key_decisions: ["..."]
  inputs: ["..."]
  outputs: ["..."]
  notable_changes: ["..."]
  risks_and_blockers: ["..."]
  next_steps: ["..."]
  references: ["path:line_or_anchor"]
```

Quality gate: [ ] <=300 words [ ] decisions [ ] risks/next steps [ ] references
<!-- context-summarization>

<workflow type="frontend-developer" -->

## Mandatory Preconditions Verification
<mandatory-preconditions>

### 1. Load Execution Standards

<stage name="Load Execution Standards" number="1" critical="true">
**Mandatory Execution Standards Loading**
- **Description**: Completely read `{project_root}/sunnycore/dev/enforcement/frontend-developer-enforcement.md`
- **Requirements**:
  <requirements>
  - Understand all mandatory rules, UI/UX standards, and quality gates
  - If unable to load, immediately stop and report error
  <!-- requirements>



### 2. Project Context Establishment

<stage name="Project Context Establishment" number="2" critical="true">

**Project Specifications Understanding**

- **Description**: Read all documents under the `{project_root}/docs/specs/` path
- **Requirements**:
  <requirements>
  <think>
  Frontend developers need to focus on the following types of project specification content:

  1. **User Interface Specifications**:
     - UI design system and component library standards
     - Visual design guidelines (colors, fonts, spacing)
     - Interaction design patterns and animation effects
     - Responsive design breakpoints and layout strategies

  2. **User Experience Specifications**:
     - User journey and process design
     - Accessibility requirements (WCAG compliance)
     - User research insights and pain point analysis
     - Interface usability and navigation structure

  3. **Technical Architecture Specifications**:
     - Frontend framework selection and configuration
     - State management strategies and data flow design
     - API integration and data structure definition
     - Component architecture and code organization structure

  4. **Performance and Optimization Specifications**:
     - Loading time and performance benchmarks
     - Resource optimization strategies (images, fonts, code splitting)
     - Caching strategies and CDN configuration
     - SEO requirements and meta tag specifications

  5. **Compatibility and Testing Specifications**:
     - Browser support matrix
     - Device and screen size compatibility
     - Testing strategies (unit testing, integration testing, E2E testing)
     - Quality assurance checklists
  <!-- think>

  Based on the above thinking analysis, execute the following tasks:
  - Understand project requirements, design systems, and user experience requirements
  - Establish a complete project context model
  - Identify UI/UX dependencies and accessibility requirements
  - Pay special attention to frontend systems' component architecture, user interaction flows, and visual design specifications
  - Confirm performance benchmarks and compatibility requirements
  

**Implementation Plan Verification**
- **Description**: Confirm `{project_root}/docs/implementation-plan/{task_id}`(such as `1`, `2`, `3`...)-plan.md` exists and is readable
<critical-checkpoint>
If implementation plan does not exist, immediately stop and notify user that planning stage needs to be executed first
<!-- critical-checkpoint>

- **Requirements**:
  <requirements -->
  <think hard>
  - Validate plan completeness, scope definition, and UI/UX feasibility
  - Confirm accessibility requirements and performance targets
  <think hard>
  <!-- requirements>



### 3. Frontend Specialization Preparation

<stage name="Frontend Specialization Preparation" number="3" critical="true">
**Frontend Development Checklist Preparation**
Prepare frontend checklist according to mandatory execution standards:

<frontend-checklist>
<think hard>
- [ ] Analyze plan content, identify frontend development requirements
- [ ] Confirm UI component architecture and design system
- [ ] Validate responsive design and accessibility requirements
- [ ] Establish test-driven development (TDD) strategy
<think hard>
<!-- frontend-checklist>

**Performance and Experience Targets Confirmation**
Confirm and record frontend performance requirements:
<performance-targets -->
<think>
- Page loading time and interaction response time targets
- Resource optimization and caching strategies
- User experience metrics and measurement methods
<think>
<!-- performance-targets>

<!-- mandatory-preconditions>

---

## Development Execution Process
<development-execution -->

### 4. TDD Development Process

<stage name="Test-Driven Development" number="4" critical="true">
**Follow TDD Process for Development**
- **Description**: Follow red-green-refactor cycle for frontend development
- **Requirements**:
  <requirements>
  <Ultra think>
  - Write tests first, then implementation
  - Ensure test coverage and quality
  - Continuously refactor and optimize code
  <Ultra think>
  <!-- requirements>


<!-- development-execution>
