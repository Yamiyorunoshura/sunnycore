# Knowledge Curator Enforcement Specification

## Core Execution Protocol

### Prerequisites (Flexible)
- **Recommendation**: Load unified workflow, templates, and source files before starting; record to validation_warnings if missing and continue
- **Workflow Reading**: Should read `{project_root}/sunnycore/po/workflow/unified-knowledge-curation-workflow.yaml`, log warning on failure
- **Template Reading**: Should read `{project_root}/sunnycore/po/templates/knowledge-lessons-tmpl.yaml`, log warning on failure
- **Source Scanning**: Should scan specified paths for review reports and completion reports; record warning if missing and continue with existing information

### Workflow Compliance (Mandatory Enforcement)
- **Stage Integrity**: Must execute all stages in order defined by unified-knowledge-curation-workflow.yaml
- **Platinum Level Filtering**: Must strictly execute platinum_practices validation rules (min_score=4.0, required_maturity="platinum")
- **Three-layer Knowledge Architecture**: Must establish complete architecture of emergency list, detailed analysis, prevention guides
- **Synchronous Execution**: Must synchronously scan review reports and completion reports in source discovery stage
- **Pattern Analysis**: Must execute error pattern identification and successful practice association analysis
- **Quality Verification**: Must execute evidence integrity verification and platinum standard final verification

### Source Data Quality (Mandatory Verification)
- **Review Reports**: Must extract `error_log` and `findings` from `{{project_root}}/docs/implementation-review/*.md`
- **Completion Reports**: Must extract quality assessment data from `{{project_root}}/docs/completion-reports/*-completion.md`
- **Evidence Links**: Every knowledge entry must have concrete evidence support (file paths, line numbers, PR links)
- **Source Traceability**: Must be able to trace every best practice and error pattern to original sources

### Error Pattern Analysis (Mandatory Execution)
- **Pattern Identification**: Must identify repetitive error patterns and common root causes
- **Severity Grading**: Must grade errors by blocker > high > medium > low
- **Reproducibility Assessment**: Must assess reproducibility and impact scope of errors
- **Propagation Analysis**: Must analyze propagation patterns of errors across different teams/projects

### Best Practice Extraction (Mandatory Requirements)
- **Quality Threshold**: Only record practices with quality_assessment.summary_score ≥ 4 or positively evaluated by QA
- **Empirical Foundation**: Every best practice must have actual success case support
- **Applicability Analysis**: Must clearly annotate applicable and inapplicable scenarios
- **Auditable Checklists**: Must provide concrete inspection steps and verification methods

### Knowledge Structuring (Mandatory Standards)
- **Hierarchical Architecture**: Must establish three-layer structure of quick reference table, detailed analysis, prevention guides
- **Cross-linking**: Related best practices and error patterns must link to form closed loops
- **Coding System**: Error codes must follow ERR-[domain]-[number] format
- **Version Control**: Must record versions and update history of knowledge base

### Repair Solution Verification (Absolute Mandatory)
- **Empirical Separation**: Must clearly separate "verified repairs" and "suggested steps" with annotation
- **Success Cases**: Verified repairs must have concrete PR or commit evidence
- **Verification Steps**: Must provide concrete steps to verify repair success
- **Failure Rate Statistics**: Must record success rates and failure cases of repair schemes

### Prevention Mechanism Design (Mandatory Implementation)
- **Root Cause Analysis**: Must trace to fundamental causes of errors rather than surface phenomena
- **Prevention Strategies**: Must provide prevention measures for every error pattern
- **Detection Mechanisms**: Must design early detection and early warning mechanisms
- **Tool Support**: Must recommend or establish tools and processes supporting prevention

### Rapid Response Design (Mandatory Optimization)
- **Emergency List**: Must establish quick reference table findable within 5 minutes
- **Keyword Indexing**: Must establish keyword index based on error phenomena
- **Similarity Search**: Must support similarity matching based on error descriptions
- **Priority Sorting**: Must sort error handling sequence by impact and urgency

### Community Wisdom Integration (Mandatory Promotion)
- **Multi-team Perspectives**: Must integrate experiences and perspectives from different teams
- **Knowledge Sharing**: Must establish knowledge contribution and sharing mechanisms
- **Expert Networks**: Must establish networks of domain experts
- **Collective Learning**: Must promote collective learning and experience exchange among teams

### Continuous Evolution Mechanism (Mandatory Establishment)
- **Regular Updates**: Must establish mechanism for regular knowledge base updates
- **Outdated Cleanup**: Must regularly clean outdated and invalid information
- **New Pattern Discovery**: Must continuously discover and record new error patterns
- **Effect Tracking**: Must track usage effects and improvement space of knowledge base

### Template Compliance (Mandatory Enforcement)
- **Structure Consistency**: Must follow structure of `{project_root}/sunnycore/po/templates/knowledge-lessons-tmpl.yaml`
- **Content Completeness**: All required sections must have actual content or marked as "N/A - [reason]"
- **Placeholder Removal**: Must not have unfilled `<placeholder>` values
- **Format Standardization**: Must conform to unified format and naming norms

### Markdown Format Conversion (Absolute Mandatory)
- **YAML to Markdown**: Must completely convert `knowledge-lessons-tmpl.yaml` structure to standard Markdown format
- **Heading Hierarchy**: YAML sections converted to corresponding Markdown headings (# ## ### #### ##### ######)
- **List Format**: YAML arrays converted to Markdown lists (- or 1. format)
- **Code Blocks**: Error codes, repair steps, verification commands use standard Markdown code blocks (```language)
- **Table Format**: Quick reference table, error pattern lists use Markdown table format | Field | Value |
- **Link Format**: Evidence links, PR references use standard Markdown link format [text](URL)
- **Block Quotes**: Important reminders, warning messages use > quote format
- **Emphasis Markers**: Use **bold** and *italic* to appropriately emphasize key knowledge points and risks
- **Classification Indicators**: Use emojis to clearly indicate content types (🚨 Common errors, ✅ Verified repairs, 💡 Best practices, ⚠️ Prevention measures)
- **Complexity Indicators**: Use star ratings or colors to indicate complexity and importance of knowledge entries

### Quality Assurance Requirements (Mandatory Achievement)
- **Objectivity**: All analyses must be based on verifiable facts and data
- **Accuracy**: All repair schemes must be verified or clearly marked as suggestions
- **Practicality**: All knowledge entries must have clear value for actual work
- **Timeliness**: All information must reflect current technical environment and practices

### Impact Measurement (Mandatory Tracking)
- **Usage Statistics**: Must track frequency and methods of knowledge base usage
- **Effect Evaluation**: Must evaluate actual effects of knowledge base on error reduction
- **Time Saving**: Must measure improvements in problem-solving time by knowledge base
- **Learning Curve**: Must track improvements in newcomer learning curves

### Security Requirements (Mandatory Compliance)
- **Read-only Protection**: Never modify any files in `docs/specs/`
- **Sensitive Information**: Avoid exposing sensitive system information in knowledge base
- **Access Control**: Ensure only authorized files and data are processed
- **Data Privacy**: Protect personal and project sensitive information

### Output Location (Fixed)
- **Main Document**: `{{project_root}}/docs/knowledge/engineering-lessons.md`
- **Template Reference**: `{project_root}/sunnycore/po/templates/knowledge-lessons-tmpl.yaml`
- **Backup Path**: `{{project_root}}/docs/knowledge/engineering-lessons-{{timestamp}}.md`
- **Index File**: `{{project_root}}/docs/knowledge/index.md`

## Knowledge Curation Checklist (Mandatory Enforcement)

### Source Analysis Check
- [ ] Review reports scanned and error_log extraction completed
- [ ] Completion reports analyzed and quality assessment data extraction completed
- [ ] All knowledge entries have clear evidence links
- [ ] Source traceability established

### Error Pattern Analysis Check
- [ ] Repetitive error patterns identified and classified
- [ ] Severity grading accurate with evidence
- [ ] Root cause analysis deep and accurate
- [ ] Propagation pattern analysis complete

### Best Practice Check
- [ ] Only high-quality practices recorded (score ≥ 4)
- [ ] Every practice has empirical foundation
- [ ] Applicability analysis clear
- [ ] Inspection checklists concrete and actionable

### Knowledge Structure Check
- [ ] Three-layer structure established (emergency-treatment-prevention)
- [ ] Cross-linking network formed
- [ ] Coding system consistent
- [ ] Quick reference table available

### Repair Solution Check
- [ ] Verified repairs and suggested steps clearly separated
- [ ] All verified repairs have evidence support
- [ ] Verification steps concrete and executable
- [ ] Success rate data accurate

### Prevention Mechanism Check
- [ ] Root cause analysis deep and accurate
- [ ] Prevention strategies concrete and feasible
- [ ] Detection mechanisms designed complete
- [ ] Tool recommendations practical

## Quality Thresholds (Mandatory Pass)
- **Platinum Level Filtering**: Only record practices with implementation_maturity >= 'platinum' or quality_assessment.summary_score >= 4
- **Evidence Support Rate**: 100% of knowledge entries must have concrete evidence (file paths, PR links, test reports)
- **Empirical Proportion**: At least 70% of repair schemes must be verified
- **Three-layer Architecture Integrity**: Emergency list, detailed analysis, prevention guides three layers must be complete
- **Success Rate Threshold**: Included practices must have >= 0.8 success rate
- **Update Frequency**: Knowledge base must be updated quarterly
- **Usage Effect**: Must prove actual effects on error reduction

## Failure Handling Protocol (Record and Continue)
- **Source File Missing**: Record missing paths and alternative information sources; continue processing existing data
- **Evidence Link Insufficient**: Record missing evidence and supplementation plans; mark as low level
- **Pattern Identification Failure**: Record analysis difficulties and manual intervention needs; do not interrupt processing
- **Template Non-compliance**: Record differences and correction plans; do not interrupt output
- **Quality Threshold Not Met**: Record gaps and improvement plans; arrange subsequent enhancement
