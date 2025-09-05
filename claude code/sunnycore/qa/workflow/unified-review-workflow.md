---
category: qa
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: unified-review-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '1.0'
---

# Unified Review Workflow

<workflow_metadata>
name: "Unified Quality Review Workflow"
version: "2.0"
category: "qa"
complexity_level: "complex"
prompt_techniques: ["chain_of_thought", "self_discover", "xml_structured"]
<!-- workflow_metadata>

<execution_settings -->
deterministic: true
parallel_enabled: false
prompt_optimization: true
quality_gates: ["information_validation", "plan_compliance", "review_completeness", "result_integration"]
<!-- execution_settings>

<enforcement -->
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
<!-- enforcement>

---

## Context Summarization Protocol

<context-summarization>
**Goal**: Reduce review context length via stage-end structured summaries and pruning.

**When**: After each review phase.

**How**:
- Use `{project_root}/sunnycore/qa/templates/stage-summary-tmpl.yaml`
- Target 200 words (hard limit 260)
- Include: objective, key_findings, evidence, defects(severity/status), risks, recommendations, references

**Retention**:
- Append-and-prune
- Keep last 3 full summaries; collapse older to 1–2 line epoch summaries
- Drop raw context older than 1 phase; carry forward open_defects, blocking_risks, critical_findings
<!-- context-summarization>

<task_overview -->
As a project quality review expert, you need to conduct comprehensive quality review of specified tasks to ensure implementation plan feasibility and code quality standards achievement.

**Chain of Thought Integration**: Before beginning any review phase, I will first analyze the problem's core elements, then systematically reason through the optimal review approach.

**SELF-DISCOVER Framework Application**: I will use structured reasoning to select appropriate review modules, adapt them to the specific context, and implement a comprehensive review strategy.
<!-- task_overview>

## Core Review Phases

<optimization_phases -->

### Phase 1: Project Information Gathering (SELF-DISCOVER: SELECT)
<phase name="project_information_gathering" complexity="think" prompt_technique="self_discover">
**Goal**: Comprehensive understanding of project background and task specifications

**SELF-DISCOVER SELECT Stage**: First, let me analyze what information gathering modules are most relevant for this review context...

<analysis>
I need to select appropriate information gathering approaches based on:
- Project complexity and scope
- Available documentation quality
- Review objectives and constraints
- Technical domain requirements
<!-- analysis>

**Chain of Thought Execution Steps**:
1. **Problem Understanding**: Let me first understand what information is critical for effective quality review...
   - Read `{project_root}/docs/specs/` to obtain basic project information
   - Analyze project architecture and technology stack
   - Identify project dependencies
   - Understand overall project objectives and constraints

2. **Analysis Decomposition**: Next, I'll break down the task-specific information requirements...
   - Read `{project_root}/docs/specs/task.md` to obtain detailed specifications for {task_id}(such as `1`, `2`, `3`...)
   - Parse task requirements and acceptance criteria
   - Identify technical requirements and performance indicators
   - Confirm task priorities and schedule constraints

3. **Step-by-Step Reasoning**: Based on the above analysis, my reasoning process for information gathering is...

4. **Conclusion Validation**: Finally, let me verify that this information foundation is complete...

**Expected Results**: 
<solution -->
Establish complete project and task understanding foundation with structured analysis of:
- Project context and constraints
- Task-specific requirements and criteria
- Technical specifications and dependencies
<!-- solution>


### Phase 2: Implementation Plan Analysis (SELF-DISCOVER: ADAPT)
<phase name="implementation_plan_analysis" complexity="think hard" prompt_technique="self_discover">
**Goal**: Deep assessment of implementation plan reasonableness and completeness

**SELF-DISCOVER ADAPT Stage**: Now I'll adapt my analysis methods to the specific implementation plan characteristics...

<analysis>
Let me first understand the core elements of this implementation plan analysis:
- What are the key feasibility factors I need to evaluate?
- How should I assess the alignment between plan and requirements?
- What risk assessment framework is most appropriate?
<!-- analysis>

**Chain of Thought Execution Steps**:
3. **Problem Understanding**: First, let me understand what makes an implementation plan robust and executable...
   - Read `{project_root}/docs/implementation-plan/{task_id}`(such as `1`, `2`, `3`...)-plan.md` to obtain implementation plan

4. **Analysis Decomposition**: Next, I'll break down the plan evaluation into these components...
   - Evaluate technical feasibility of plan
   - Check reasonableness of resource allocation
   - Verify realism of schedule arrangements
   - Identify potential risk points and dependencies

5. **Step-by-Step Reasoning**: Based on my analysis, the logical evaluation sequence is...

6. **Conclusion Validation**: Finally, let me verify that my assessment covers all critical aspects...

**XML Structured Validation Checkpoints**:
<validation -->
- [ ] Consistency between plan and requirements specifications
- [ ] Executability of technical solutions
- [ ] Accuracy of resource estimates
- [ ] Completeness of risk identification
- [ ] Alignment with quality standards and best practices
- [ ] Consideration of technical constraints and dependencies
<!-- validation>


### Phase 3: Quality Review Execution (SELF-DISCOVER: IMPLEMENT)
<phase name="quality_review_execution" complexity="think harder" prompt_technique="self_discover">
**Goal**: Conduct differentiated review based on project status

**SELF-DISCOVER IMPLEMENT Stage**: Now I'll implement a structured review plan based on the project context and requirements...

<analysis>
First, let me analyze the optimal review strategy:
- What is the current project status (greenfield vs brownfield)?
- Which quality dimensions are most critical for this specific task?
- How should I prioritize my review efforts for maximum impact?
<!-- analysis>

**Chain of Thought Review Strategy**:
4. **Problem Understanding**: Let me first understand the most effective review approach for this context...

5. **Analysis Decomposition**: I'll structure my review into these key areas based on project status...

**Greenfield Project Review Focus**:
<solution -->
- Reasonableness of architecture design
- Adherence to code standards and best practices
- Test coverage and quality assurance
- Documentation completeness and clarity
- Security considerations and vulnerability assessment
- Performance optimization opportunities
<!-- solution>

**Brownfield Project Review Focus**:
<solution -->
- **Priority 1**: Review of previously identified issue lists
  - Verify issue remediation status and effectiveness
  - Evaluate quality of remediation solutions
  - Confirm no introduction of new side effects or regressions
- **Priority 2**: New issue identification and evaluation
  - Code quality regression checks
  - Impact analysis of new functionality
  - System integration verification
  - Compatibility and migration considerations
<!-- solution>

6. **Step-by-Step Reasoning**: My systematic review process will follow this logic...

7. **Conclusion Validation**: Finally, I'll validate my findings against these quality standards...

**XML Structured Quality Assessment Dimensions**:
<assessment_framework -->
<functional_correctness>Requirements compliance and feature completeness<!-- functional_correctness>
<performance_efficiency -->Resource utilization and response time optimization<!-- performance_efficiency>
<maintainability -->Code clarity, modularity, and documentation quality<!-- maintainability>
<reliability -->Error handling, fault tolerance, and system stability<!-- reliability>
<security -->Vulnerability assessment and data protection measures<!-- security>
<usability -->User experience and interface design quality<!-- usability>

<!-- phase>

### Phase 4: Result Integration and Reporting (SELF-DISCOVER: APPLY)
<phase name="result_integration_reporting" complexity="think" prompt_technique="self_discover" -->
**Goal**: Structure review results and communicate effectively

**SELF-DISCOVER APPLY Stage**: Now I'll apply my review findings to create actionable recommendations and structured reporting...

<analysis>
Let me first understand how to best structure and communicate my review results:
- What are the most critical findings that need immediate attention?
- How should I prioritize recommendations for maximum impact?
- What format will be most useful for the development team?
<!-- analysis>

**Chain of Thought Execution Steps**:
5. **Problem Understanding**: First, let me understand how to effectively organize and present my review findings...

6. **Analysis Decomposition**: I'll structure my results into these key components...
   - Aggregate identified issues and risks by severity and impact
   - Provide specific, actionable improvement recommendations
   - Evaluate overall quality level with quantitative metrics where possible
   - Formulate prioritized follow-up action plans

7. **Step-by-Step Reasoning**: My logical approach to result integration is...

8. **Conclusion Validation**: Finally, let me verify that my reporting is comprehensive and actionable...

**XML Structured Output Format**:
<reporting_structure -->
<executive_summary>High-level quality assessment and key findings overview<!-- executive_summary>
<detailed_findings -->
  <critical_issues>Issues requiring immediate attention<!-- critical_issues>
  <major_issues -->Significant problems affecting quality or functionality<!-- major_issues>
  <minor_issues -->Improvements and optimizations<!-- minor_issues>

<risk_assessment>
  <high_risk>Critical risks that could impact project success<!-- high_risk>
  <medium_risk -->Moderate risks requiring monitoring<!-- medium_risk>
  <low_risk -->Minor risks with limited impact<!-- low_risk>

<recommendations>
  <priority_1>Immediate action required<!-- priority_1>
  <priority_2 -->Important improvements<!-- priority_2>
  <priority_3 -->Nice-to-have enhancements<!-- priority_3>

<follow_up>Monitoring points and validation criteria<!-- follow_up>


**Final Communication**:
9. Send structured report to main agent and end call (Remember that in this phase you as reviewer do not need to write review results to any files.)

<validation>
Ensure all findings are:
- Specific and actionable
- Prioritized by impact and effort
- Clearly communicated with examples
- Aligned with project objectives and constraints
<!-- validation>


<!-- optimization_phases>

## Quality Assurance Mechanism

<quality_assurance -->
<standardized_quality_metrics>
**Completeness Score**: Percentage of required review areas covered (Target: 100%)
**Accuracy Score**: Percentage of findings that are valid and actionable (Target: ≥95%)
**Consistency Score**: Alignment with established quality standards (Target: ≥90%)
**Timeliness Score**: Review completion within allocated timeframe (Target: 100%)
<!-- standardized_quality_metrics>

<validation_criteria -->
- [ ] **Information Collection Completeness**: All necessary documents have been read and analyzed using chain of thought reasoning
- [ ] **Review Method Appropriateness**: Selected appropriate review strategy based on project status using SELF-DISCOVER framework
- [ ] **Problem Identification Accuracy**: Identified issues have practical significance and operability, validated through systematic analysis
- [ ] **Report Structure Clarity**: Result organization is logical and easy to understand, using XML structured format
- [ ] **Recommendation Executability**: Provided improvement recommendations are specific, prioritized, and implementable
- [ ] **Quality Standards Compliance**: All assessments align with standardized quality metrics and evaluation criteria
- [ ] **Chain of Thought Documentation**: Review reasoning process is clearly documented and traceable
- [ ] **XML Structure Adherence**: All outputs follow standardized XML tagging for consistency and clarity
<!-- validation_criteria>

<quality_gates -->
**Gate 1 - Information Validation**: Verify all required documents are accessible and complete
**Gate 2 - Plan Compliance**: Confirm implementation plan aligns with specifications
**Gate 3 - Review Completeness**: Ensure all quality dimensions have been thoroughly assessed
**Gate 4 - Result Integration**: Validate that findings are properly structured and actionable
<!-- quality_gates>
