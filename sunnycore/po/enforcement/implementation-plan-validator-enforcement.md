# Implementation Plan Validator Enforcement Specification

## Core Execution Protocol

### Prerequisites (Flexible)
- **Recommendation**: Load all necessary files before starting validation; record gaps and alternative information sources if missing
- **Recommended Reading Order**:
  1. `{project_root}/sunnycore/po/enforcement/implementation-plan-validator-enforcement.md`
  2. `{project_root}/sunnycore/po/workflow/unified-plan-validation-workflow.yaml`
  3. `{project_root}/sunnycore/po/templates/implementation-plan-tmpl.yaml`
  4. `{project_root}/sunnycore/po/templates/plan-validation-report-tmpl.yaml`
- **File Loading Verification**: Record gaps and alternative information sources if unable to load completely

### Evidence-based Validation (Absolute Mandatory)
- **Evidence Requirements**: All judgments must be supported by concrete evidence
- **Citation Format**: Must include file paths, line numbers, paragraph references
- **Traceability**: Every finding must be traceable to source files
- **Objectivity**: Avoid subjective judgments, base only on verifiable facts

### Workflow Compliance (Flexible)
- **Stage Integrity**: Should execute in order; record reasons and remediation plans when incomplete
- **Validation Checkpoints**: Record warnings and minimize continuation when not passed
- **Failure Handling**: Record warnings and continue for non-blocking failures; stop only for blocking failures

### Template Compliance (Mandatory but Non-blocking)
- **Structure Validation**: Plan must conform to required fields of `{project_root}/sunnycore/po/templates/implementation-plan-tmpl.yaml` template
- **Completeness Check**: All required sections must have actual content
- **Placeholder Removal**: Should remove `<placeholder>`; record and supplement if remaining
- **Format Consistency**: Must conform to format requirements of template

### Cross-reference Validation (Mandatory Enforcement)

#### Requirements Cross-reference
- **Functional Requirements**: Every functional item must find correspondence in `requirements.md`, `task.md`, or `design.md`
- **Non-functional Requirements**: Measurement targets must be clear and traceable to specifications or quality thresholds
- **Requirements Completeness**: All referenced requirements must have clear sources

#### Design Cross-reference
- **Architecture Alignment**: Architecture, modules, interfaces must be traceable in `design.md`
- **Design Documents**: Design diagrams and documents must be consistent with plan
- **Technology Selection**: Technology choices must have design document support

#### Scope Cross-reference
- **Scope Definition**: in_scope/out_of_scope must be traceable to explicit boundary definitions in specifications
- **Scope Consistency**: Scope definitions must be consistent with project documents
- **Scope Reasonableness**: Scope size must match resource and time arrangements

### Project Specification Compliance (Mandatory Verification)
- **Security Requirements**: Never modify any files in `docs/specs/`
- **File Integrity**: All referenced files must exist and be readable
- **Path Correctness**: All file paths must be correct and resolvable

### Detailed Validation Requirements

#### Metadata Validation (Mandatory Check)
- **Path Existence**: All referenced paths must exist and be readable
- **File Integrity**: Ensure all source files are complete and uncorrupted
- **Version Consistency**: Ensure consistency of file versions

#### Target Validation (Mandatory Enforcement)
- **Functional Objectives**: Every item must have correspondence in `requirements.md`, `task.md`, or `design.md`
- **Non-functional Targets**: Measurement targets must be clear, measurable, and traceable
- **Target Achievability**: Targets must be achievable within given constraints

#### Scope Validation (Mandatory Confirmation)
- **Boundary Clarity**: Scope boundaries must be clearly defined
- **Inclusion Rationale**: in_scope items must have sufficient justification
- **Exclusion Rationale**: out_of_scope items must have clear reasons
- **Scope Traceability**: Scope definitions must be traceable to specifications or plan background

#### Approach Validation (Mandatory Check)
- **Architecture Reasonableness**: Architecture choices must have design document support
- **Module Design**: Module division must be reasonable and traceable
- **Interface Definition**: Interface design must have correspondence in design documents

#### Data Validation (Mandatory Confirmation)
- **Data Structure**: Must be based on design or migration documents
- **Migration Strategy**: Data migration must have clear strategy and steps
- **Data Integrity**: Ensure data changes do not break integrity

#### Testing Strategy Validation (Mandatory Check)
- **Testing Completeness**: Testing strategy must cover all functional points
- **Quality Thresholds**: Quality thresholds must be concrete and verifiable
- **Testing Feasibility**: Testing methods must be feasible and effective

#### Timeline Validation (Mandatory Confirmation)
- **Milestone Reasonableness**: Timelines and milestones must be reasonable and achievable
- **Dependency Relations**: Dependencies must be clear and logical
- **Resource Matching**: Time arrangements must match available resources

#### Risk Assessment Validation (Mandatory Check)
- **Risk Identification**: Risk identification must be comprehensive and actual
- **Mitigation Measures**: Every risk must have corresponding mitigation measures
- **Contingency Plans**: Major risks must have contingency plans

#### Severity Quantification (Mandatory Convention)
- **Level Definitions**:
  - Critical (Critical): Blocks workflow, needs immediate repair; corresponds to blocker in workflow rules
  - High (High): Significantly affects quality/timeline; needs repair before report or prioritization as action items
  - Medium (Medium): Suggest correction; does not block output
  - Low (Low): Best practices or improvable items
- **Quantification Dimensions (at least two)**: Impact scope (scope), reproducibility (reproducibility), repair cost (effort), time criticality (time criticality)
- **Decision Rules**: Classified as critical if any blocking condition (missing critical chapters, cross-reference failures, placeholder residues, no evidence findings)

### Report Generation Requirements (Mandatory Enforcement)
- **Template Compliance**: Report must conform to `{project_root}/sunnycore/po/templates/plan-validation-report-tmpl.yaml` structure
- **Content Completeness**: All template sections must have actual content
- **Evidence Support**: All findings must have concrete evidence
- **Suggestions Concrete**: Improvement suggestions must be concrete and actionable
- **Execution Metadata**: Suggest including run_id, start/end times, stage durations, synchronization, cache hit rate in appendix

### Markdown Format Conversion (Absolute Mandatory)
- **YAML to Markdown**: Must completely convert `plan-validation-report-tmpl.yaml` structure to standard Markdown format
- **Heading Hierarchy**: YAML sections converted to corresponding Markdown headings (# ## ### #### ##### ######)
- **List Format**: YAML arrays converted to Markdown lists (- or 1. format)
- **Code Blocks**: Code snippets and evidence references use standard Markdown code blocks (```language)
- **Table Format**: Validation results and finding lists use Markdown table format | Field | Value |
- **Link Format**: Evidence links use standard Markdown link format [text](URL)
- **Block Quotes**: Important findings and suggestions use > quote format
- **Emphasis Markers**: Use **bold** and *italic* to appropriately emphasize key findings and risks
- **Severity Indicators**: Use emojis or markers to clearly indicate problem severity (🚨 Critical, ⚠️ High, ℹ️ Medium, 💡 Low)

### Output Location (Fixed)
- **Main Report**: `{{project_root}}/docs/validation-reports/{{task_id}}-plan-validation.md`
- **Template Reference**: `{project_root}/sunnycore/po/templates/plan-validation-report-tmpl.yaml`

### Quality Standards (Mandatory Achievement)
- **Objectivity**: Validation must be objective, based on verifiable facts
- **Comprehensiveness**: Validation must cover all important aspects of plan
- **Accuracy**: All findings must be accurate and evidence-based
- **Practicality**: Validation results must have actual value for plan improvement

### Severity Evaluation (Mandatory Classification)
- **Critical**: Problems that may lead to project failure
- **High**: Problems that may affect project quality or timeline
- **Medium**: Problems that can be improved but do not affect core objectives
- **Low**: Best practice suggestions and future enhancement directions

### Documentation and Traceability
- **Evidence Recording**: Every finding must record concrete evidence
- **Citation Format**: Use standardized citation format
- **Traceability**: Ensure all judgments can be traced to source files
- **Version Control**: Record file versions at validation time

### Efficiency and Determinism Guidelines (Not Changing Core Workflow)
- **Prefetch and Synchronization (Allowed)**: Can synchronize mutually independent read and check actions within single stage; cross-stage must execute and verify strictly in order
- **Cache Strategy (Recommended)**: Establish unique addressing cache based on `task_id + plan_path + source file hashes`; invalidate unconditionally when file hashes or mtimes change
- **Deterministic Reasoning (Recommended)**: Set `temperature=0`, `top_p=0` for LLM/tools used (if supported), close random sampling; adopt stable sorting for output lists (region → path → start line)
- **Fail-fast (Strengthened)**: Stop subsequent steps immediately and return to corresponding stage for repair once blocker-level (blocker) deficiency/violation occurs
- **Placeholder Scanning (Strengthened)**: Scan `<[^>]+>`, `TBD`, `TODO`, `INSERT` placeholders with rules before report output; regard as format violation if hit
- **Evidence Minimum Unit (Standardized)**: Each finding must include at least `relative file path`, `line range`, `reference snippet (if necessary)`; encourage attaching `sha256` of source file to strengthen reproducibility
- **Execution Telemetry (Recommended)**: Generate `run_id (UUID)` for each validation, record start/completion times of each stage, synchronization, cache hit rate, write to report appendix

## Validation Checklist (Mandatory Enforcement)

### Pre-checks
- [ ] Unified workflow file loaded
- [ ] Implementation plan template loaded
- [ ] Validation report template loaded
- [ ] Target plan file exists and readable

### Structure Checks
- [ ] Plan conforms to template structure
- [ ] All required fields have content
- [ ] No unfilled placeholders
- [ ] Format conforms to requirements

### Content Checks
- [ ] All functional requirements traceable
- [ ] All non-functional requirements measurable
- [ ] Scope definition clear and reasonable
- [ ] Architecture design has document support
- [ ] Testing strategy complete and feasible
- [ ] Timeline reasonable and achievable
- [ ] Risk assessment comprehensive with mitigation measures

### Quality Checks
- [ ] All judgments have evidence support
- [ ] Citation format correct
- [ ] Suggestions concrete and actionable
- [ ] Severity classification reasonable

## Failure Handling Protocol (Record and Continue)
- **File Loading Failure**: Record missing sources and fallback paths; supplement scope if necessary
- **Plan File Non-existence**: Record missing sources and alternative information sources; do not interrupt evidence collection
- **Cross-reference Failure**: Record as findings and annotate severity with remediation suggestions
- **Template Non-compliance**: Record differences and propose correction plans; do not interrupt
- **Evidence Insufficiency**: Record gaps and supplementation plans; allow delayed supplementation
