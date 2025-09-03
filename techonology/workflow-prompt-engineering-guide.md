# Workflow Prompt Engineering Guide
*Based on best practices analysis of dev/workflow/ and qa/workflow/*

## Overview

This guide is based on in-depth analysis of existing workflow files, extracting and organizing three core prompt engineering techniques and their best practice applications in workflow design.

## 1. Core Prompt Engineering Techniques Architecture

### 1.1 Three Core Techniques
```xml
<core_techniques>
<chain_of_thought>
<description>Step-by-step reasoning method ensuring clear and traceable logic</description>
<structure>Problem Understanding → Analysis Breakdown → Step-by-step Reasoning → Conclusion Validation</structure>
<application>Complex analysis, decision making, problem diagnosis</application>
</chain_of_thought>

<self_discover>
<description>Four-stage structured framework suitable for complex task decomposition</description>
<stages>
<select>Select appropriate analysis modules and methods</select>
<adapt>Adjust methods to fit specific situations</adapt>
<implement>Develop structured implementation plan</implement>
<apply>Apply plan and generate results</apply>
</stages>
</self_discover>

<xml_structured_output>
<description>Use XML tags to organize complex content, improve readability</description>
<benefits>Semantic tags, hierarchical structure, consistent organization</benefits>
<standard_tags>analysis, findings, recommendations, validation, metadata</standard_tags>
</xml_structured_output>
</core_techniques>
```

## 2. Workflow File Structure Standards

### ⚠️ Critical Principle: Output Format Specification

**All workflow final output documents must be in pure Markdown format and absolutely cannot contain XML tags!**

- **XML Tags**: Only used for internal LLM thinking organization within workflow files to help LLM understand and execute
- **Final Output**: Must be standard Markdown documents, convenient for human reading and editing
- **Strictly Prohibited**: Appearance of `<xml>`, `</xml>` or any XML tags in generated reports and documents

### Correct Output Format Example:

```markdown
# Architecture Documentation

## System Overview
This system adopts microservices architecture...

## Component Analysis
### Frontend Components
- React application
- Redux state management

### Backend Services
- API Gateway
- Authentication service
- Business logic service

## Recommendations
1. Optimize database connection pool configuration
2. Implement API rate limiting mechanism
3. Strengthen monitoring and logging
```

### 2.1 YAML Front Matter Specification
```yaml
---
category: po  # dev/qa/po
description: Unified architecture system workflows documentation
last_updated: '2025-09-03'
name: workflow-name
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '2.0'
---
```

### 2.2 Enforced Execution Protocol Pattern
```xml
<execution_protocol>
<todo_list_creation importance="critical">
<description>AI must create a todo list containing all workflow steps before executing any workflow procedures</description>

<process_steps>
1. **Analyze Workflow Structure** - Carefully read the entire workflow file, identify all stages, steps and tasks
2. **Extract Key Tasks** - Convert core tasks from each stage into specific todo items
3. **Set Priorities** - Set priorities based on task importance and dependencies
4. **Create Todo List** - Use todo_write tool to create structured todo list
5. **Execute Workflow** - Execute tasks according to todo list order, update status promptly
</process_steps>

<requirements>
- Each major stage should have corresponding todo items
- Key validation checkpoints must be included in the todo list
- Set reasonable priorities, ensure dependencies are respected
- Update todo status promptly during execution (pending → in_progress → completed)
</requirements>
</todo_list_creation>
</execution_protocol>
```

## 3. Detailed Implementation Guide for Prompt Techniques

### 3.1 Chain of Thought Implementation Example
```xml
<chain_of_thought_implementation>
<problem_understanding>
First, let me understand the core requirements of this problem:
- Clarify task objectives and scope
- Identify key constraints
- Determine success criteria
</problem_understanding>

<analysis_breakdown>
Next, I will break down this problem into the following parts:
1. Data collection and analysis
2. Pattern identification and classification
3. Result integration and validation
4. Output formatting and delivery
</analysis_breakdown>

<step_by_step_reasoning>
Based on the above analysis, my reasoning process is as follows:
1. First execute data collection, ensure information completeness
2. Then apply analysis methods, identify key patterns
3. Next integrate findings, form structured conclusions
4. Finally validate results, ensure quality standards
</step_by_step_reasoning>

<conclusion_validation>
Let me validate whether this conclusion is reasonable and complete:
- ✓ Covers all major analysis steps
- ✓ Logic chain is clear and traceable
- ✓ Results meet expected standards
- ✓ Can guide subsequent actions
</conclusion_validation>
</chain_of_thought_implementation>
```

### 3.2 SELF-DISCOVER Framework Application
```xml
<self_discover_application>
<select_stage>
**Selection Stage**: Choose appropriate analysis modules
- Evaluate task complexity and characteristics
- Select suitable analysis methods and tools
- Determine analysis depth and scope
</select_stage>

<adapt_stage>
**Adaptation Stage**: Adjust methods to fit specific situations
- Adjust analysis focus based on project characteristics
- Adapt to specific constraint conditions
- Customize validation and quality standards
</adapt_stage>

<implement_stage>
**Implementation Stage**: Develop structured implementation plan
- Establish detailed execution steps
- Define intermediate checkpoints
- Set quality thresholds
</implement_stage>

<apply_stage>
**Application Stage**: Implement plan and generate results
- Execute analysis steps according to plan
- Record processes and decisions
- Generate structured output
</apply_stage>
</self_discover_application>
```

### 3.3 XML Structured Thinking and Markdown Output Standards

#### Important Note: XML is only for LLM internal thinking use, final output must be pure Markdown

```xml
<!-- The following XML structure is only for LLM internal thought organization, must not appear in final output documents -->
<xml_thinking_structure>
<internal_analysis>Analysis process and adopted methods (LLM internal thinking)</internal_analysis>
<internal_findings>Discovered problems, patterns and insights (LLM internal organization)</internal_findings>
<internal_recommendations>Improvement suggestions and action plans (LLM internal conception)</internal_recommendations>
<internal_validation>Validation results and quality checks (LLM internal confirmation)</internal_validation>
</xml_thinking_structure>
```

#### Final Output Must Use Pure Markdown Format:

```markdown
# Document Title

## Overview
Brief description of document purpose and scope

## Analysis Process
Describe analysis methods and steps adopted

## Major Findings
### Finding 1
Detailed description...

### Finding 2
Detailed description...

## Recommended Actions
1. Specific recommendation 1
2. Specific recommendation 2

## Validation Results
Describe quality checks and validation results

## Appendix
Supplementary materials and reference information
```

#### XML vs Markdown Usage Principles:
- **XML Tags**: Only for LLM internal thinking organization, helping structure reasoning processes
- **Markdown Format**: For all human-facing final output documents
- **Strictly Prohibited**: Mixing XML tags in final output documents
- **User-Friendly**: Ensure all delivered documents are in standard Markdown format, convenient for reading and maintenance

## 4. Workflow Design Patterns

### 4.1 Staged Execution Pattern
```xml
<stage_execution_pattern>
<preparation_stage>
<description>Environment preparation and prerequisite checks</description>
<activities>Load configuration, verify permissions, prepare output directories</activities>
</preparation_stage>

<analysis_stage>
<description>Core analysis and processing stage</description>
<activities>Data collection, pattern identification, result generation</activities>
<parallel_enabled>true</parallel_enabled>
</analysis_stage>

<validation_stage>
<description>Quality validation and result confirmation</description>
<activities>Result validation, format checking, completeness confirmation</activities>
</validation_stage>

<output_stage>
<description>Result output and status update</description>
<activities>File writing, status updates, report generation</activities>
</output_stage>
</stage_execution_pattern>
```

### 4.2 Parallel Processing Strategy
```xml
<parallelization_strategy>
<data_collection>
<max_concurrent>5-8</max_concurrent>
<timeout_per_task>15-60 seconds</timeout_per_task>
<shared_cache>true</shared_cache>
</data_collection>

<analysis_tasks>
<max_concurrent>3-5</max_concurrent>
<dependency_aware>true</dependency_aware>
<batch_processing>true</batch_processing>
</analysis_tasks>

<validation_tasks>
<sequential_required>true</sequential_required>
<reason>Ensure data consistency</reason>
</validation_tasks>
</parallelization_strategy>
```

## 5. Quality Assurance System

### 5.1 Multi-level Validation Mechanism
```xml
<quality_assurance_system>
<input_validation>
- Prerequisite checks
- File availability verification
- Permission confirmation
</input_validation>

<process_validation>
- Intermediate result quality checks
- Progress monitoring
- Error detection and handling
</process_validation>

<output_validation>
- Completeness verification
- Format specification checks
- Content quality assessment
</output_validation>

<continuous_monitoring>
- Performance monitoring
- Resource usage tracking
- Anomaly detection
</continuous_monitoring>
</quality_assurance_system>
```

### 5.2 Quality Gate Settings
```xml
<quality_gates>
<gate_1_information_validation>
<criteria>All necessary files loaded and verified</criteria>
<threshold>100% availability</threshold>
<failure_action>Stop execution and report errors</failure_action>
</gate_1_information_validation>

<gate_2_analysis_completeness>
<criteria>Analysis covers all necessary dimensions</criteria>
<threshold>Completeness ≥95%</threshold>
<failure_action>Log warning and continue</failure_action>
</gate_2_analysis_completeness>

<gate_3_output_quality>
<criteria>Output format and content meet standards</criteria>
<threshold>Quality score ≥4/5</threshold>
<failure_action>Require correction before continuing</failure_action>
</gate_3_output_quality>
</quality_gates>
```

## 6. Error Handling and Recovery Mechanisms

### 6.1 Error Classification and Handling Strategy
```xml
<error_handling_framework>
<file_access_errors>
<response>log_warning</response>
<continue>true</continue>
<fallback>Use default configuration</fallback>
</file_access_errors>

<data_validation_errors>
<response>mark_for_review</response>
<continue>true</continue>
<fallback>Apply conservative estimates</fallback>
</data_validation_errors>

<critical_system_errors>
<response>halt_execution</response>
<continue>false</continue>
<fallback>Generate error report</fallback>
</critical_system_errors>
</error_handling_framework>
```

### 6.2 Recovery and Retry Mechanisms
```xml
<recovery_mechanisms>
<retry_policy>
<max_retries>3</max_retries>
<retry_delay>30 seconds</retry_delay>
<exponential_backoff>true</exponential_backoff>
</retry_policy>

<graceful_degradation>
<reduced_scope>Reduce analysis scope</reduced_scope>
<alternative_methods>Use backup methods</alternative_methods>
<partial_results>Accept partial results</partial_results>
</graceful_degradation>
</recovery_mechanisms>
```

## 7. Best Practices Checklist

### 7.1 Design Phase Best Practices
```xml
<design_best_practices>
<structure_design>
- Use standardized YAML front matter
- Implement enforced execution protocols
- Design clear stage divisions
- Define explicit dependencies
</structure_design>

<prompt_technique_integration>
- Apply Chain of Thought at appropriate stages
- Use SELF-DISCOVER framework for complex tasks
- Adopt XML structuring for complex content organization
- Ensure consistency in technique application
</prompt_technique_integration>

<quality_focus>
- Set multi-level validation checkpoints
- Define specific quality thresholds
- Implement error handling and recovery mechanisms
- Include continuous improvement mechanisms
</quality_focus>
</design_best_practices>
```

### 7.2 Implementation Phase Best Practices
```xml
<implementation_best_practices>
<execution_discipline>
- Always start with Todo list creation
- Strictly follow stage execution order
- Update execution status promptly
- Record all decisions and changes
</execution_discipline>

<documentation_standards>
- Use clear tags and naming
- Maintain structural consistency
- Provide sufficient context
- Ensure traceability
</documentation_standards>

<collaboration_protocols>
- Define clear interfaces and data formats
- Implement version control and change management
- Establish feedback and improvement mechanisms
- Ensure cross-team consistency
</collaboration_protocols>
</implementation_best_practices>
```

## 8. XML Thinking to Markdown Output Conversion Guide

### 8.1 Internal XML Thinking Organization (LLM Use Only)

LLM can use XML tags to organize internal thinking during workflow execution:

```xml
<!-- LLM internal thinking process, does not appear in final output -->
<internal_analysis>
<problem_scope>Analyze task scope and complexity</problem_scope>
<methodology>Select appropriate analysis methods</methodology>
<execution_plan>Develop step-by-step execution plan</execution_plan>
</internal_analysis>

<internal_findings>
<pattern_1>First identified pattern</pattern_1>
<pattern_2>Second identified pattern</pattern_2>
<implications>Meaning and impact of patterns</implications>
</internal_findings>

<internal_recommendations>
<priority_high>High priority recommendations</priority_high>
<priority_medium>Medium priority recommendations</priority_medium>
<implementation_steps>Specific implementation steps</implementation_steps>
</internal_recommendations>
```

### 8.2 Convert to Pure Markdown Output

The above internal thinking must be converted to the following pure Markdown format:

```markdown
# Analysis Report

## Analysis Scope and Methodology

This analysis covers the system's core components and key processes. We adopted a structured analysis approach, conducting in-depth evaluation from multiple dimensions.

## Major Findings

### Pattern One: Excessive Component Coupling
Through code analysis, we found tightly coupled components in the system, affecting module independence and maintainability.

### Pattern Two: Lack of Unified Error Handling Mechanism
Different service modules adopt different error handling strategies, leading to inconsistent system behavior.

## Recommended Actions

### High Priority Recommendations
1. **Refactor Core Components**: Decouple tightly dependent modules
2. **Unify Error Handling**: Implement consistent error handling mechanisms

### Medium Priority Recommendations
1. Optimize performance bottlenecks
2. Improve monitoring and logging systems

## Implementation Steps
1. Evaluate existing component dependencies
2. Design decoupling strategy
3. Gradually implement refactoring
4. Test and verify improvement effects
```

### 8.3 Output Format Checklist

Before generating final documents, please confirm:

- [ ] Document contains no XML tags (`<`, `>`, `</>`)
- [ ] Uses standard Markdown syntax (#, ##, ###, -, 1., ``` etc.)
- [ ] Title hierarchy is clear and reasonable
- [ ] List formatting is standardized
- [ ] Code blocks use correct syntax highlighting
- [ ] Links and references are formatted correctly
- [ ] Overall document structure is convenient for human reading

## 9. Continuous Improvement Mechanisms

### 9.1 Performance Monitoring and Optimization
```xml
<performance_optimization>
<metrics_collection>
- Execution time and resource usage
- Quality indicators and error rates
- User satisfaction and adoption rates
- Maintenance costs and technical debt
</metrics_collection>

<optimization_strategies>
- Parallel processing capability enhancement
- Cache mechanism optimization
- Error handling improvements
- User experience enhancement
</optimization_strategies>
</performance_optimization>
```

### 9.2 Version Management and Evolution
```xml
<version_management>
<versioning_strategy>
- Semantic version control
- Backward compatibility guarantee
- Change log maintenance
- Migration guidance documentation
</versioning_strategy>

<evolution_framework>
- Regular evaluation and updates
- User feedback integration
- New technology adoption assessment
- Architecture evolution planning
</evolution_framework>
</version_management>
```

## Summary

This guide provides a comprehensive framework for designing and implementing high-quality workflow files. By integrating three core prompt engineering techniques and adopting standardized design patterns and quality assurance mechanisms, we can ensure consistency, reliability, and maintainability of workflow files.

## ⚠️ Critical Output Format Requirements

**Most Important Principle: All user-facing final output documents must be in pure Markdown format!**

- XML tags are only for LLM internal thinking and organization
- Final generated reports, documents, analysis results must be standard Markdown
- Absolutely prohibited to have XML tags appear in user documents
- Ensure documents are easy for humans to read, edit, and maintain

Key Success Factors:
1. **Output Format Specification**: Strictly follow pure Markdown output requirements
2. **Prompt Technique Application**: Correctly integrate three core techniques
3. **Quality Assurance System**: Implement comprehensive quality control
4. **Consistency Maintenance**: Maintain standardized design and implementation
5. **Continuous Improvement Mechanisms**: Establish evolution and optimization frameworks