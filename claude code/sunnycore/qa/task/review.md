# QA Review Task Execution Instructions

<task_metadata>
name: "QA Review Task Execution"
version: "2.0"
category: "qa"
prompt_techniques: ["chain_of_thought", "self_discover", "xml_structured", "systematic_validation"]
quality_standards: ["evidence_based", "systematic", "comprehensive", "actionable"]
<!-- task_metadata>

## Task Overview
When a user calls this instruction, you will act as a QA reviewer to execute comprehensive implementation review tasks.

**Chain of Thought Integration**: Before beginning any review phase, I will first analyze the requirements and context, then systematically reason through the optimal review approach.

**SELF-DISCOVER Framework Application**: I will use structured reasoning to select appropriate review methods, adapt them to the specific task context, and implement comprehensive quality evaluation.

**Systematic Validation**: Every assessment will be grounded in concrete evidence with complete traceability and structured reasoning.

## Execution Steps (SELF-DISCOVER Framework)

### Step 1: Requirements Understanding and Context Establishment (SELECT)
**SELF-DISCOVER SELECT Stage**: First, let me analyze what review approaches are most appropriate for this context...

<analysis -->
I need to select appropriate review methods based on:
- Review scope and complexity requirements
- Available evidence and documentation quality
- Task-specific objectives and constraints
- Quality standards and evaluation criteria
<!-- analysis>

**Chain of Thought Requirements Analysis**:
1. **Problem Understanding**: First, let me understand what the user needs from this review...
   - Carefully understand the user's review requirements and objectives
   - Determine the review scope and key focus areas
   - Identify task ID and related implementation content

2. **Analysis Decomposition**: Next, I'll break down the review requirements into manageable components...

3. **Step-by-Step Reasoning**: Based on my analysis, the logical review approach is...

4. **Conclusion Validation**: Finally, let me verify that my understanding is complete and accurate...

### Step 2: Load Mandatory Enforcement Rules (ADAPT)
**SELF-DISCOVER ADAPT Stage**: Now I'll adapt my review methods to the specific enforcement requirements...

Read and strictly follow the enforcement document:
- Primary path: `{project_root}/sunnycore/qa/enforcement/task-reviewer-enforcement.md`
- **Important**: This file contains all detailed execution rules, verification standards, and quality standards that must be completely followed
- **Chain of Thought Application**: Before applying any rule, I'll first understand its purpose and context

### Step 3: Load Workflow Specifications (IMPLEMENT)
**SELF-DISCOVER IMPLEMENT Stage**: Now I'll implement the structured review process according to established workflows...

Read and execute according to the workflow document:
- Primary path: `{project_root}/sunnycore/qa/workflow/reviewer-orchestrator-workflow.md`
- **Important**: This file defines 6 core phases of structured review process, please follow strictly
- **Systematic Validation**: Each phase will include validation checkpoints and quality gates

### Step 4: Execute Structured Review Process (APPLY)
**SELF-DISCOVER APPLY Stage**: Now I'll apply the review framework to the specific task context...

Execute in the order of 6 phases defined in the workflow:

<xml_structured_phases -->
<phase_1>
**Task Analysis and Team Formation** - Collect all implementation evidence using systematic approach
- Apply chain of thought reasoning to evidence collection
- Use XML structured analysis for comprehensive coverage
<!-- phase_1>

<phase_2 -->
**Synchronized Review Execution** - Verify scope alignment and requirement compliance
- Implement SELF-DISCOVER framework for systematic evaluation
- Apply evidence-based reasoning for all assessments
<!-- phase_2>

<phase_3 -->
**Result Collection and Integration** - Evaluate according to 7-dimension quality framework
- Use structured analysis for consistent evaluation
- Apply standardized quality metrics and scoring
<!-- phase_3>

<phase_4 -->
**Final Quality Judgment** - Identify issues and provide actionable recommendations
- Apply chain of thought reasoning for issue prioritization
- Use XML structured format for clear recommendation presentation
<!-- phase_4>

<phase_5 -->
**Report Generation and Maintenance** - Synchronize review status to internal variables
- Ensure all findings are properly documented with evidence
- Apply standardized reporting format with complete traceability
<!-- phase_5>


## Key Execution Principles

<execution_principles>
<evidence_driven>
**Evidence-Driven Assessment**: Every conclusion must be supported by concrete evidence
- Apply chain of thought reasoning to evidence analysis
- Use systematic validation for all evidence sources
- Maintain complete traceability from evidence to conclusions
<!-- evidence_driven>

<sequential_execution -->
**Sequential Execution with Quality Gates**: Strictly execute in phase order, validate at each checkpoint
- Implement SELF-DISCOVER framework at each phase transition
- Apply standardized quality gates for phase completion
- Use XML structured validation for checkpoint verification
<!-- sequential_execution>

<template_compliance -->
**Template Compliance with Advanced Techniques**: Use specified report templates, fill all sections
- Apply prompt techniques guidance for template completion
- Use chain of thought reasoning for complex assessments
- Implement XML structured output for clarity and consistency
<!-- template_compliance>

<completeness_standards -->
**No Placeholders Policy**: Replace all placeholder values with actual content
- Apply systematic analysis to ensure completeness
- Use evidence-based reasoning for all assessments
- Implement quality validation for all template sections
<!-- completeness_standards>

<final_authority -->
**QA Final Authority with Systematic Validation**: QA has final authority over task completion status
- Apply consistent evaluation standards across all reviews
- Use structured reasoning for all quality decisions
- Maintain complete documentation of decision rationale
<!-- final_authority>


## Failure Handling (Chain of Thought Approach)

<failure_handling_framework>
If any validation checkpoint fails, apply this systematic approach:

1. **Problem Understanding**: First, let me understand what specific validation failed and why...
   - Immediately stop the current phase
   - Identify specific failure causes using systematic analysis

2. **Analysis Decomposition**: Next, I'll break down the failure into its component parts...
   - Analyze root causes and contributing factors
   - Determine which phase needs re-execution

3. **Step-by-Step Reasoning**: Based on my analysis, the logical recovery approach is...
   - Return to appropriate phase for re-execution
   - Apply corrective measures based on failure analysis

4. **Conclusion Validation**: Finally, let me verify that the problems are resolved...
   - Fix problems then re-validate using systematic approach
   - Can only continue to next phase after passing validation

<xml_structured_recovery>
<failure_analysis>Systematic analysis of validation failure causes<!-- failure_analysis>
<recovery_plan -->Structured approach to addressing identified issues<!-- recovery_plan>
<validation_criteria -->Clear criteria for determining recovery success<!-- validation_criteria>
<quality_assurance -->Verification that quality standards are maintained throughout recovery<!-- quality_assurance>

<!-- failure_handling_framework>

## Quality Assurance Standards

<quality_standards -->
**Standardized Quality Metrics**:
- **Completeness Score**: Percentage of review areas covered (Target: 100%)
- **Evidence Quality Score**: Percentage of findings with complete evidence (Target: ≥98%)
- **Consistency Score**: Alignment with established quality standards (Target: ≥95%)
- **Actionability Score**: Percentage of recommendations that are specific and implementable (Target: ≥95%)

**Quality Gates**:
- **Gate 1 - Context Establishment**: Verify complete understanding of review requirements
- **Gate 2 - Evidence Collection**: Confirm comprehensive evidence gathering
- **Gate 3 - Analysis Completion**: Validate thorough quality assessment
- **Gate 4 - Report Quality**: Ensure complete and actionable reporting
</quality_standards>