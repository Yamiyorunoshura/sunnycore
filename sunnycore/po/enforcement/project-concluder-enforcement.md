# Project Concluder Enforcement Specification

## Core Execution Protocol

### Prerequisites (Flexible)
- **Recommendation**: Load necessary files before starting conclusion; record to validation_warnings if missing and continue
- **Recommended Reading Order**:
  1. `{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml`
  2. `{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml`
- **File Loading Verification**: Record gaps and alternative information sources if unable to load completely

### Determinism and Synchronization (New Mandatory)
- **Determinism**: All automated steps must be executed with temperature 0, top_p 1, seed 42
- **Consistency**: List output adopts stable lexicographic order, and all paths are normalized to absolute paths
- **Synchronization**: Allow sub-steps in `evidence_collection` and `delivery_synthesis` stages to execute synchronously, ensuring data dependencies are not broken
- **Fail-fast Strategy**: If prerequisites or essential files are missing, must stop immediately and report, not continue to subsequent stages
- **Cache Requirements**: Adopt content hash caching; reuse results when `docs/specs/**` and `docs/implementation-plan/**` have no changes

### Evidence-based Conclusion (Absolute Mandatory)
- **Evidence Requirements**: All conclusions must be supported by concrete evidence
- **Evidence Types**: File paths, PR links, test reports, measurement results, QA comments
- **Traceability**: Every completion statement must be traceable to concrete implementation evidence
- **Objectivity**: Avoid subjective judgments, base only on verifiable facts

### Workflow Compliance (Flexible)
- **Stage Integrity**: Should execute in order; record reasons and remediation plans when incomplete
- **Validation Checkpoints**: Record warnings and minimize continuation when not passed
- **Failure Handling**: Record warnings and continue for non-blocking failures; stop only for blocking failures

### Template Compliance (Mandatory Enforcement)
- **Structure Consistency**: Report must conform to `{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml` structure
- **Content Completeness**: All required sections must have actual content
- **Placeholder Removal**: Must not have unfilled `<placeholder>` values
- **Format Standards**: Must conform to format requirements of template

### Markdown Format Conversion (Absolute Mandatory)
- **YAML to Markdown**: Must completely convert `completion-report-tmpl.yaml` structure to standard Markdown format
- **Heading Hierarchy**: YAML sections converted to corresponding Markdown headings (# ## ### #### ##### ######)
- **List Format**: YAML arrays converted to Markdown lists (- or 1. format)
- **Code Blocks**: Code snippets, configurations, test results use standard Markdown code blocks (```language)
- **Table Format**: Completion status, QA results, performance data use Markdown table format | Field | Value |
- **Link Format**: PR links, document references use standard Markdown link format [text](URL)
- **Block Quotes**: Important discoveries, risk warnings use > quote format
- **Emphasis Markers**: Use **bold** and *italic* to appropriately emphasize key achievements and risks
- **Status Indicators**: Use emojis to clearly indicate completion status (✅ Completed, ⚠️ Partially completed, ❌ Not completed, 🔄 In progress)

### Scope Compliance (Flexible Recording)
- **Plan Alignment**: Should follow plan and requirements; record reasons and impacts for deviations
- **Scope Definition**: Mark scope-out items as deviations and risks, do not interrupt
- **Completion Definition**: Based on acceptance conditions; record limitations and supplementation plans if evidence insufficient
- **Change Recording**: Supplement in report if unable to record in real-time and explain

### Evidence Collection Requirements (Mandatory Enforcement)

#### Planning Document Collection
- **Implementation Plan**: Must collect corresponding files from `docs/implementation-plan/`
- **Specification Documents**: Must collect `docs/specs/task.md`, `requirements.md`, `design.md`
- **Plan Alignment**: Must verify consistency between implementation and plan

#### Implementation Evidence Collection
- **Code Changes**: Must collect all related PR and commit records
- **File List**: Must list all modified files
- **Migration Scripts**: Must record all data migrations and structure changes
- **Configuration Changes**: Must record all environment and configuration changes

#### Testing and Quality Evidence
- **Test Reports**: Must collect complete test reports
- **Coverage Data**: Must collect test coverage statistics
- **CI/CD Records**: Must collect continuous integration and deployment records
- **Static Analysis**: Must collect static analysis and security scan results

#### QA Review Evidence
- **QA Reports**: Must collect QA review summaries or links
- **Issue List**: Must record all problems discovered by QA
- **Processing Status**: Must record current processing status of each problem
- **Acceptance Status**: Must record QA's final acceptance status

#### Performance and Non-functional Evidence
- **Performance Baseline**: Must collect performance test results
- **Resource Usage**: Must record system resource usage
- **Observability**: Must verify monitoring and logging systems
- **Security Verification**: Must collect security test and audit results

### Conclusion Framework Check (Mandatory Enforcement)

#### Completion Status Evaluation
- **Delivery Deliverables**: Must list all delivery deliverables and evaluate completion rates
- **Completion Classification**: Must classify items as completed/delayed/scope-out changes
- **Completion Evidence**: Every completion statement must have concrete evidence support

#### Acceptance Criteria Verification
- **Functional Acceptance**: Must verify functions meet acceptance standards
- **Cross-reference**: Must cross-reference plan/acceptance conditions with tests/evidence
- **Acceptance Status**: Clearly record achievement status of each acceptance condition

#### QA Problem Summary
- **Problem List**: Must summarize all concerns and problems raised during QA review
- **Processing Status**: Must record current processing status of each problem
- **Impact Assessment**: Must assess impact of problems on project delivery

#### Known Issues Recording
- **Defect List**: Must record all defects currently existing
- **Risk Assessment**: Must assess known risks and trade-offs
- **Temporary Solutions**: Must record all temporary solutions and limitations

#### Documentation and Maintainability Evaluation
- **Documentation Completeness**: Must evaluate completeness of README, API specifications, migration documents
- **Maintainability**: Must evaluate code maintainability and technical debt
- **Handover Documentation**: Must prepare appropriate handover documentation

#### Non-functional Evaluation
- **Performance Evaluation**: Must evaluate whether performance meets standards
- **Security Evaluation**: Must evaluate whether security meets requirements
- **Observability**: Must evaluate whether monitoring and observability are adequate

#### Future Enhancement Suggestions
- **Gap Analysis**: Identify specific enhancement opportunities based on gaps
- **QA Feedback**: Propose improvements based on QA feedback
- **Product Direction**: Consider future enhancement suggestions based on product direction

### Report Quality Standards (Mandatory Achievement)
- **Objectivity**: Report must be objective, based on verifiable facts
- **Comprehensiveness**: Report must cover all important aspects of project
- **Accuracy**: All statements must be accurate and evidence-based
- **Practicality**: Report results must have actual value for future decisions

### Value-oriented Evaluation (Mandatory Enforcement)
- **Business Value**: Must evaluate value of delivery deliverables from business perspective
- **User Value**: Must evaluate actual value obtained by users
- **ROI Evaluation**: Must evaluate reasonableness of project investment and output
- **Success Definition**: Must define success based on actual value rather than technical completion

### Security Requirements (Mandatory Compliance)
- **Document Protection**: Never modify any files in `docs/specs/`
- **Data Integrity**: Ensure integrity and accuracy of all collected evidence
- **Access Control**: Ensure only authorized files and resources are accessed

### Output Location (Fixed)
- **Main Report**: `{{project_root}}/docs/completion-reports/{{task_id}}-completion.md`
- **Template Reference**: `{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml`

### Documentation and Handover Requirements
- **Complete Recording**: All important decisions and discoveries must be recorded
- **Clear Expression**: Use clear, professional language to express
- **Structuring**: Organize content according to template structure
- **Traceability**: Ensure all statements can be traced to source evidence

### Path Aliases (New)
- `WORKFLOW_FILE` → `{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml`
- `REPORT_TEMPLATE` → `{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml`
- `ENFORCEMENT_FILE` → `{project_root}/sunnycore/po/enforcement/project-concluder-enforcement.md`

### Collaboration Requirements with file-classifier (Mandatory)
- **Synchronous Execution**: Must execute synchronously when *conclude is called
- **Result Integration**: Must integrate classification results from file-classifier into conclusion report
- **Cleanup Execution Record**: Must include records of executed file cleanup operations and risk assessments by file-classifier
- **Coordination Execution**: Ensure execution of two agents does not conflict, share necessary project information

## Conclusion Checklist (Mandatory Enforcement)

### Pre-checks
- [ ] Unified workflow file loaded
- [ ] Completion report template loaded
- [ ] Related project files identified and readable

### Evidence Collection Checks
- [ ] Planning documents collected and analyzed
- [ ] Implementation evidence collected and verified
- [ ] Testing and quality evidence collected
- [ ] QA review evidence collected
- [ ] Performance and non-functional evidence collected

### Evaluation Checks
- [ ] Completion status accurately evaluated
- [ ] Acceptance criteria verified one by one
- [ ] QA problems comprehensively summarized
- [ ] Known issues clearly recorded
- [ ] Documentation and maintainability evaluated
- [ ] Non-functional requirements evaluated

### Report Quality Checks
- [ ] All statements have evidence support
- [ ] Report structure conforms to template requirements
- [ ] No unfilled placeholders
- [ ] Language expression clear and professional
- [ ] Suggestions concrete and actionable

### Value Evaluation Checks
- [ ] Business value evaluated
- [ ] User value considered
- [ ] ROI analyzed
- [ ] Success criteria clearly defined

## Severity Classification (Mandatory Application)
- **Critical**: Problems affecting project successful delivery
- **High**: Problems affecting project quality or future maintenance
- **Medium**: Problems that can be improved but do not affect core objectives
- **Low**: Best practice suggestions and future enhancement directions

## Failure Handling Protocol (Record and Continue)
- **File Loading Failure**: Record missing sources and fallback paths; supplement scope if necessary
- **Evidence Collection Insufficiency**: Record gaps and supplementation plans; do not interrupt other sections
- **Template Non-compliance**: Record differences and correction plans; do not interrupt
- **Verification Not Passed**: Record failure details and remediation plans; downgrade if necessary
- **Quality Not Met**: Record gaps and improvement timelines; arrange subsequent review
