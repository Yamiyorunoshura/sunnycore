# Task Planner Enforcement Standards

<authority_declaration>
> **Important Declaration**: This document is the sole authoritative source for Task Planner agent execution standards. All other documents (workflows, agent definitions) should reference this file to avoid duplicate definitions.
</authority_declaration>

<reference_guidelines>
## 📋 Document Reference Guidelines

### How other documents should reference this standard:
- **Workflow Documents**: Should include `reference_file` pointing to this document, avoiding duplicate rule definitions
- **Agent Definition Documents**: Should provide simplified descriptions with detailed rules referencing this document
- **Template Documents**: Should focus on structure definitions with validation rules referencing this document

### Complete content contained in this document:
- All mandatory execution rules and constraints
- Complete validation standards and quality gates
- Detailed error handling strategies
- Core planning principles and best practices
</reference_guidelines>

<core_execution_protocol>
## Core Execution Protocol

<prerequisite_conditions>
### Mandatory Prerequisites (Relaxed)
- **Recommendation**: Load unified workflow and templates before starting; if missing, record in validation_warnings and continue
- **Workflow Reading**: Should read `{project_root}/sunnycore/dev/workflow/unified-task-planning-workflow.md`, record warning if failed
- **Template Reading**: Should read `{project_root}/sunnycore/dev/templates/implementation-plan-tmpl.yaml`, record warning if failed
- **Validation Requirements**: If project_root is unresolved or reading incomplete, record missing items and alternative information sources
</prerequisite_conditions>

<deterministic_efficiency>
### Determinism and Efficiency (Mandatory)
- **Zero Randomness**: Generation phase must use fixed parameters (temperature≤0.2, top_p≤0.3, penalties=0)
- **Idempotent Output**: Use `task_id + sources_content_hash` as run_key, output must be consistent when input unchanged
- **I/O Synchronization and Caching**: Specification reading must be synchronous with content hash-based result caching
- **Failure Retry**: Only I/O operations can be retried (maximum 2 times), generation cannot be blindly retried
</deterministic_efficiency>

<workflow_compliance>
### Workflow Compliance (Relaxed)
- **Stage Sequencing**: Should execute in unified workflow order; if skipped, record reasons and remedies
- **Stage Completeness**: When checkpoints fail, record warnings and minimize continuation
- **Stage Requirements**:
  - workflow_initialization: Load workflows and templates
  - input_collection: Collect all specification documents
  - sequential_thinking: Analyze requirements and strategies
  - template_population: Populate all template sections
  - document_output: Generate and save plans
  - finalization: Final validation and certification
</workflow_compliance>

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
</core_execution_protocol>

<planning_principles>
## Core Planning Principles (Mandatory Execution)

<mandatory_principles>
1. **Safety First**: Never modify any files in `docs/specs/`
2. **RCSD Compliance**: Must define functional and non-functional requirements; clearly define scope boundaries
3. **MD Principle**: Must decompose work into small, reusable modules
4. **KISS Principle**: Must prefer the simplest viable approach
5. **DRY Principle**: Must avoid duplication; reuse existing modules
6. **TQA Requirements**: Must plan unit, integration, and acceptance tests with explicit conditions
7. **RACP Requirements**: Must identify risks and mitigation/contingency measures
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
</planning_principles>

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
</output_validation>

<failure_handling>
## Failure Handling Protocol (Record and Continue)

<failure_protocols>
- **Validation Failed**: Record warnings and gaps; do not interrupt and include in follow-up list
- **File Loading Failed**: Record failure and alternative paths; downgrade process if necessary
- **Scope Resolution Failed**: Record gaps and continue with minimal viable assumptions; simultaneously request clarification
- **Blacklist Hit**: Record and rollback corrections; include in follow-up if cannot fix immediately
- **Consistency Defects**: Record differences and completion plans; do not interrupt
</failure_protocols>
</failure_handling>

<quality_gates>
## Quality Gates

<quality_requirements>
- All template sections must have actual content
- All technical choices must have adequate research support
- All risks must have corresponding mitigation measures
- All test plans must have explicit acceptance conditions
- Zero blacklist hits; zero consistency validation defects
</quality_requirements>
</quality_gates>

<standard_operating_procedure>
## SOP (Minimal Closed Loop)

<sop_steps>
1. Synchronous + cached specification reading (task/requirements/design)
2. Structured extraction (FR/NFR/constraints/dependencies → JSON)
3. Template section-by-section population (allow "N/A - reason")
4. Lint (blacklist/placeholders/consistency/Schema)
5. Idempotent persistence and index deduplication
6. Re-read final check (template consistency/context fidelity/blacklist and consistency green light)
</sop_steps>
</standard_operating_procedure>