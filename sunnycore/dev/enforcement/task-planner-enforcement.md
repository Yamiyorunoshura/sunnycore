# Task Planner Implementation Standards (Advanced Prompt Techniques Integration Version)

<authority_declaration>
> **Important Declaration**: This document is the sole authoritative source for Task Planner agent implementation standards. All other documents (workflows, agent definitions) should reference this file to avoid duplicate definitions.
> 
> **Advanced Techniques Integration**: This standard integrates advanced prompt techniques including chain_of_thought, SELF-DISCOVER framework, XML structured output, and first principles thinking.
</authority_declaration>

<prompt_techniques_integration>
## 🧠 Advanced Prompt Techniques Integration Standards

### Required Prompt Techniques
```xml
<required_techniques>
<chain_of_thought>
<description>chain_of_thought - Used for complex analysis and decision processes</description>
<application>Must be applied during task decomposition, risk analysis, and solution design</application>
<format>Use "First...Next...Then...Finally..." structure</format>
</chain_of_thought>


<self_discover>
<description>SELF-DISCOVER framework - Used for structured task decomposition</description>
<stages>SELECT → ADAPT → IMPLEMENT → APPLY</stages>
<application>Must be applied for complex task planning and problem solving</application>
</self_discover>


<xml_structured>
<description>XML structured output - Improves content organization and readability</description>
<usage>Use semantic tags to organize complex analysis and output</usage>
<common_tags>analysis, solution, validation, reasoning</common_tags>
</xml_structured>


<first_principles>
<description>First principles thinking - Analysis starting from fundamental principles</description>
<application>Must be applied in requirements analysis and architecture design starting from basic needs</application>
</first_principles>

</required_techniques>
```


<reference_guidelines>
## 📋 Document Reference Guidelines (Applying chain_of_thought)

### How Other Documents Should Reference This Standard (Step-by-step reasoning method):
```xml
<reference_reasoning>
<step1>First, identify the specific standard content that needs to be referenced</step1>
<step2>Next, determine the method and format of reference</step2>
<step3>Then, avoid duplicate definitions of the same rules</step3>
<step4>Finally, ensure consistency and accuracy of references</step4>
</reference_reasoning>
```

- **Workflow Documents**: Should include `reference_file` pointing to this document, avoiding duplicate rule definitions
- **Agent Definition Documents**: Should provide simplified descriptions with detailed rules referencing this document
- **Template Documents**: Should focus on structural definitions with validation rules referencing this document

### Complete Content Contained in This Document (XML structured organization):
```xml
<document_contents>
<execution_rules>All mandatory implementation rules and constraints</execution_rules>
<validation_standards>Complete validation standards and quality gates</validation_standards>
<error_handling>Detailed error handling strategies</error_handling>
<planning_principles>Core planning principles and best practices</planning_principles>
<prompt_techniques>Advanced prompt technique application guidance</prompt_techniques>
</document_contents>
```
</reference_guidelines>

<core_execution_protocol>
## Core Implementation Protocol (Integrating SELF-DISCOVER Framework)

<prerequisite_conditions>
### Mandatory Prerequisites (Applying SELF-DISCOVER Framework)

**SELECT Phase**: Choose necessary resources and tools
```xml
<resource_selection>
<workflow_file>{project_root}/sunnycore/dev/workflow/unified-task-planning-workflow.md</workflow_file>
<template_file>{project_root}/sunnycore/dev/templates/implementation-plan-tmpl.yaml</template_file>
<validation_approach>Record warnings and continue if missing</validation_approach>
</resource_selection>
```

**ADAPT Phase**: Adjust implementation method to fit actual situations
- **Recommendation**: Load unified workflow and templates before starting; if missing, record in validation_warnings and continue
- **Workflow Reading**: Should read unified task planning workflow, record warnings on failure
- **Template Reading**: Should read implementation plan template, record warnings on failure

**IMPLEMENT Phase**: Develop specific implementation plan
```xml
<implementation_plan>
<validation_requirements>If project_root is unresolved or reading incomplete, record missing items and alternative information sources</validation_requirements>
<fallback_strategy>Prepare alternative solutions to handle resource unavailability</fallback_strategy>
</implementation_plan>
```

**APPLY Phase**: Apply the plan to actual implementation
- Implement resource loading and validation
- Record all warnings and issues
- Continue implementation main task flow
</prerequisite_conditions>

<deterministic_efficiency>
### Deterministic and Efficiency (Mandatory Requirements - Applying First Principles)

**First Principles Analysis**:
```xml
<determinism_principles>
<basic_requirement>Ensure consistency and reproducibility of output</basic_requirement>
<fundamental_approach>Through controlling randomness and establishing deterministic mechanisms</fundamental_approach>
<core_implementation>Fixed parameters, content hashing, synchronous I/O</core_implementation>
</determinism_principles>
```

**Specific Requirements**:
- **Zero Randomness**: Generation phase must use fixed parameters (temperature≤0.2, top_p≤0.3, penalties=0)
- **Idempotent Output**: Use `task_id + sources_content_hash` as run_key, output must be consistent when input unchanged
- **Synchronous I/O and Caching**: Specification reading must be synchronous, content hash-based result caching
- **Failure Retry**: Only I/O operations can retry (max 2 times), generation cannot blindly retry

**Chain_of_thought Validation**:
```xml
<efficiency_reasoning>
<step1>First, ensure all parameter settings are deterministic</step1>
<step2>Next, verify that input content hash calculation is correct</step2>
<step3>Then, check that caching mechanism is working properly</step3>
<step4>Finally, confirm that retry logic applies only to I/O operations</step4>
</efficiency_reasoning>
```
</deterministic_efficiency>

<workflow_compliance>
### Workflow Compliance (Integrating chain_of_thought)

**Stage Sequence Implementation** (chain_of_thought method):
```xml
<stage_sequencing_reasoning>
<principle>Should implement according to unified workflow sequence</principle>
<exception_handling>If skipped, record reasons and remedial measures</exception_handling>
<reasoning_process>
<step1>First, check prerequisites for current stage</step1>
<step2>Next, verify if previous stage is completed</step2>
<step3>Then, implement specific tasks of current stage</step3>
<step4>Finally, validate if stage output meets requirements</step4>
</reasoning_process>
</stage_sequencing_reasoning>
```

**Stage Integrity**: When checkpoint fails, record warnings and continue minimally

**Stage Requirements** (XML structured organization):
```xml
<stage_requirements>
<workflow_initialization>
<description>Load workflow and templates</description>
<prompt_technique>Apply SELF-DISCOVER framework to select and adapt resources</prompt_technique>
</workflow_initialization>


<input_collection>
<description>Collect all specification documents</description>
<prompt_technique>Use chain_of_thought for systematic input collection and validation</prompt_technique>
</input_collection>


<sequential_thinking>
<description>Analyze requirements and strategies</description>
<prompt_technique>Apply first principles starting from basic requirements for analysis</prompt_technique>
</sequential_thinking>


<template_population>
<description>Populate all template sections</description>
<prompt_technique>Use XML structured output to organize complex content</prompt_technique>
</template_population>


<document_output>
<description>Generate and save plans</description>
<prompt_technique>Apply chain_of_thought to ensure output quality</prompt_technique>
</document_output>


<finalization>
<description>Final validation and certification</description>
<prompt_technique>Use SELF-DISCOVER framework for comprehensive validation</prompt_technique>
</finalization>

</stage_requirements>
```


<readonly_boundaries>
### Read-Only Boundaries
- **Read-Only Protection**: `docs/specs/**` directory strictly prohibits writing (warning recorded and rollback if detected)
- **Path Whitelist**: Only allow writing under `{{project_root}}/docs/implementation-plan/` and `{{project_root}}/docs/index/`; record and reject if non-compliant
</readonly_boundaries>

<template_compliance>
### Template Compliance (Relaxed)
- **Complete Population**: Should populate with actual content or mark as "N/A - [reason]"; record warnings when insufficient
- **Placeholder Clearance**: Should clear `<placeholder>` values; record for subsequent completion if remaining
- **Structural Consistency**: Should conform to `{project_root}/sunnycore/dev/templates/implementation-plan-tmpl.yaml` structure; record differences when inconsistent
- **Blacklist Vocabulary**: When encountering `TBD`/`待定`/`視需要`/`as needed`/`<...>`, record and immediately replace or provide reasons
</template_compliance>

<markdown_conversion>
### Markdown Format Conversion (Absolute Mandatory)
- **YAML to Markdown**: Must completely convert `implementation-plan-tmpl.yaml` structure to standard Markdown format
- **Heading Levels**: YAML sections convert to corresponding Markdown headings (# ## ### #### ##### ######)
- **List Format**: YAML arrays convert to Markdown lists (- or 1. format)
- **Code Blocks**: Code snippets, configuration examples, test instructions use standard Markdown code blocks (```language)
- **Table Format**: Requirements lists, schedule planning, risk assessments use Markdown table format | Field | Value |
- **Link Format**: Document references, specification links use standard Markdown link format [text](URL)
- **Block Quotes**: Important notes, constraint conditions use > quote format
- **Emphasis Markers**: Use **bold** and *italic* to appropriately emphasize key requirements and risks
- **Progress Indicators**: Use emoji to indicate milestone status (🎯 target, ⚠️ risk, 🔄 in progress)
- **Priority Markers**: Use star ratings or colors to indicate requirement priorities and risk levels
</markdown_conversion>


<planning_principles>
## Core Planning Principles (Mandatory Implementation - Integrating Advanced Prompt Techniques)

<mandatory_principles>
**First Principles-Guided Mandatory Principles**:

```xml
<principle_analysis>
<safety_first>
<principle>Never modify any files in `docs/specs/`</principle>
<reasoning>Starting from basic data integrity requirements, specification documents must remain unchanged</reasoning>
<implementation>Implement strict read-only boundary checks</implementation>
</safety_first>


<rcsd_compliance>
<principle>Must define functional and non-functional requirements; clearly define scope boundaries</principle>
<reasoning>
<step1>First, understand that the fundamental purpose of requirement definition is to ensure project success</step1>
<step2>Next, analyze how functional requirements satisfy basic user needs</step2>
<step3>Then, determine how non-functional requirements ensure system quality</step3>
<step4>Finally, establish clear scope boundaries to avoid scope creep</step4>
</reasoning>
</rcsd_compliance>

<md_principle>
<principle>Must decompose work into small, reusable modules</principle>
<self_discover_application>
<select>Select appropriate modularization strategies</select>
<adapt>Adjust module size to fit project complexity</adapt>
<implement>Develop specific module decomposition plan</implement>
<apply>Apply modularization principles to actual design</apply>
</self_discover_application>
</md_principle>

<kiss_principle>
<principle>Must prefer the simplest viable approach</principle>
<first_principles_analysis>
<basic_need>Most basic method to satisfy user requirements</basic_need>
<complexity_justification>Any complexity must have clear value justification</complexity_justification>
<simplicity_validation>Regularly check for simpler alternatives</simplicity_validation>
</first_principles_analysis>
</kiss_principle>

<dry_principle>
<principle>Must avoid duplication; reuse existing modules</principle>
<reasoning>
<step1>First, identify existing reusable components</step1>
<step2>Next, analyze feasibility and risks of reuse</step2>
<step3>Then, develop reuse strategy and adaptation plan</step3>
<step4>Finally, ensure reuse doesn't introduce unnecessary complexity</step4>
</reasoning>
</dry_principle>

<tqa_requirements>
<principle>Must plan unit, integration, and acceptance tests with explicit conditions</principle>
<testing_strategy_framework>
<unit_tests>Start from basic verification requirements of smallest functional units</unit_tests>
<integration_tests>Verify basic interaction requirements between components</integration_tests>
<acceptance_tests>Ensure satisfaction of users' basic usage requirements</acceptance_tests>
</testing_strategy_framework>
</tqa_requirements>

<racp_requirements>
<principle>Must identify risks and mitigation/contingency measures</principle>
<risk_analysis_chain>
<step1>First, identify potential risks starting from project's basic goals</step1>
<step2>Next, analyze root causes of each risk</step2>
<step3>Then, develop mitigation strategies targeting root causes</step3>
<step4>Finally, prepare emergency response plans for when risks occur</step4>
</risk_analysis_chain>
</racp_requirements>

</principle_analysis>
```
</mandatory_principles>

<cross_consistency>
### Cross Consistency
- Functional requirements must correspond to at least one testable acceptance criterion
- Non-functional requirements must have quantifiable metrics
- Modules must map to at least one milestone or provide explicit reasons
- Data changes must provide migration steps or "not required" justification
- Dependencies must include version or internal owner information
</cross_consistency>

<context_research>
### Context and Research Requirements
- **Context Preservation**: Must include all specific technical details from specifications
- **Concretization Requirements**: Must replace vague content with concrete, actionable details
- **Traceability**: Must maintain clear links between plan elements and source specifications
</context_research>

<indexing_uniqueness>
### Indexing and Uniqueness
- **Index Key**: `task_id + sources_content_hash`
- **Deduplication Rules**: Same index key must not be written to records repeatedly
- **Audit Fields**: Record `workflow_template_version`, `document_path`, `timestamp`
</indexing_uniqueness>


<output_validation>
## Output and Validation Requirements (Relaxed)

<path_resolution>
### Project Root Directory Resolution
Resolve `project_root` in sequence: env `CLAUDE_PROJECT_ROOT` → Git root → nearest `docs/specs/` → cwd
</path_resolution>

<output_compliance>
### Output Path Compliance
- **Output Path Compliance**: Must save to `{{project_root}}/docs/implementation-plan/{{task_id}`(e.g.`1`, `2`, `3`...)}-plan.md`
- **Index Update**: Must append JSONL record to `{{project_root}}/docs/index/plan-index.jsonl`
- **Path Validation**: Must ensure output path is under `project_root`
- **Success Validation**: Should confirm file successfully written and review absolute path; record and retry plan if failed
- **Final Check Extension**: Must run blacklist scan and cross-consistency validation and pass all
</output_compliance>


<failure_handling>
## Failure Handling Protocol (Record and Continue)

<failure_protocols>
- **Validation Failed**: Record warnings and gaps; do not interrupt and include in follow-up list
- **File Loading Failed**: Record failure and alternative paths; downgrade process if necessary
- **Scope Resolution Failed**: Record gaps and continue with minimal viable assumptions; simultaneously request clarification
- **Blacklist Hit**: Record and rollback corrections; include in follow-up if cannot fix immediately
- **Consistency Defects**: Record differences and completion plans; do not interrupt
</failure_protocols>


<quality_gates>
## Quality Gates

<quality_requirements>
- All template sections must have actual content
- All technical choices must have adequate research support
- All risks must have corresponding mitigation measures
- All test plans must have explicit acceptance conditions
- Zero blacklist hits; zero consistency validation defects
</quality_requirements>


<standard_operating_procedure>
## Standard Operating Procedure (Minimal Closed Loop - Integrating Advanced Prompt Techniques)

<sop_steps>
**SELF-DISCOVER Framework-Guided SOP Steps**:

```xml
<sop_framework>
<step1>
<name>Synchronous + Cached specification reading (task/requirements/design)</name>
<technique>chain_of_thought</technique>
<reasoning>
<step>First, validate availability of all required documents</step>
<step>Next, read documents in priority order</step>
<step>Then, calculate content hash to support caching</step>
<step>Finally, validate completeness of read content</step>
</reasoning>
</step1>

<step2>
<name>Structured extraction (FR/NFR/constraints/dependencies → JSON)</name>
<technique>XML structured output</technique>
<extraction_format>
<functional_requirements>List of functional requirements</functional_requirements>
<non_functional_requirements>List of non-functional requirements</non_functional_requirements>
<constraints>List of constraint conditions</constraints>
<dependencies>List of dependencies</dependencies>
</extraction_format>
</step2>

<step3>
<name>Template section-by-section population (allow "N/A - reason")</name>
<technique>SELF-DISCOVER framework</technique>
<approach>
<select>Select appropriate content organization methods</select>
<adapt>Adjust content to fit template structure</adapt>
<implement>Populate specific content section by section</implement>
<apply>Validate completeness of population results</apply>
</approach>
</step3>

<step4>
<name>Check (blacklist/placeholders/consistency/Schema)</name>
<technique>First principles validation</technique>
<validation_principles>
<basic_completeness>Check starting from basic completeness requirements</basic_completeness>
<consistency_check>Ensure logical consistency of content</consistency_check>
<quality_standards>Validate achievement of basic quality standards</quality_standards>
</validation_principles>
</step4>

<step5>
<name>Idempotent persistence and index deduplication</name>
<technique>Deterministic processing</technique>
<implementation>Use content hash to ensure idempotency</implementation>
</step5>


<step6>
<name>Re-read final check (template consistency/context fidelity/blacklist and consistency green light)</name>
<technique>chain_of_thought validation</technique>
<final_check_reasoning>
<step>First, validate if generated document meets template requirements</step>
<step>Next, check if content maintains original context</step>
<step>Then, confirm no blacklist vocabulary or inconsistency issues</step>
<step>Finally, provide final quality assessment and approval</step>
</final_check_reasoning>
</step6>

</sop_framework>
```

**Advanced Technique Application Checklist**:
```xml
<technique_checklist>
<chain_of_thought>✓ Apply step-by-step reasoning in complex analysis</chain_of_thought>
<self_discover>✓ Use four-stage framework in task decomposition</self_discover>
<xml_structured>✓ Use XML tags to organize complex output</xml_structured>
<first_principles>✓ Start analysis and validation from fundamental principles</first_principles>
</technique_checklist>
```
</sop_steps>
