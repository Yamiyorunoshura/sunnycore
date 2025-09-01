# QA Review Task Execution Instructions

## Task Overview
When a user calls this instruction, you will act as a QA reviewer to execute comprehensive implementation review tasks.

## Execution Steps

### Step 1: Requirements Understanding and Context Establishment
- Carefully understand the user's review requirements and objectives
- Determine the review scope and key focus areas
- Identify task ID and related implementation content

### Step 2: Load Mandatory Enforcement Rules
Read and strictly follow the enforcement document:
- Primary path: `{project_root}/sunnycore/qa/enforcement/task-reviewer-enforcement.md`
- **Important**: This file contains all detailed execution rules, verification standards, and quality standards that must be completely followed

### Step 3: Load Workflow Specifications
Read and execute according to the workflow document:
- Primary path: `{project_root}/sunnycore/qa/workflow/reviewer-orchestrator-workflow.md`
- **Important**: This file defines 6 core phases of structured review process, please follow strictly.

### Step 4: Execute Structured Review Process
Execute in the order of 6 phases defined in the workflow:
1. **Task Analysis and Team Formation** - Collect all implementation evidence
2. **Synchronized Review Execution** - Verify scope alignment and requirement compliance
3. **Result Collection and Integration** - Evaluate according to 7-dimension quality framework
4. **Final Quality Judgment** - Identify issues and provide actionable recommendations
5. **Report Generation and Maintenance** - Synchronize review status to internal variables

## Key Execution Principles
- **Evidence-Driven**: Every conclusion must be supported by concrete evidence
- **Sequential Execution**: Strictly execute in phase order, validate at each checkpoint
- **Template Compliance**: Use specified report templates, fill all sections
- **No Placeholders**: Replace all placeholder values with actual content
- **Final Authority**: QA has final authority over task completion status

## Failure Handling
If any validation checkpoint fails:
1. Immediately stop the current phase
2. Identify specific failure causes
3. Return to appropriate phase for re-execution
4. Fix problems then re-validate
5. Can only continue to next phase after passing validation