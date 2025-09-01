# File Classifier Enforcement Specification

## Core Execution Protocol

### Prerequisites (Mandatory)
- **Absolute Requirement**: Necessary files must be loaded before starting file classification; if missing, stop immediately and report error
- **Mandatory Reading Order**:
  1. `{project_root}/sunnycore/po/workflow/unified-file-classification-workflow.yaml`
- **File Loading Verification**: If unable to load completely, stop immediately and report error

### Determinism and Synchronization (Absolute Mandatory)
- **Determinism**: All automated steps must be executed with temperature 0, top_p 0, top_k 1, seed 42
- **Consistency**: List output adopts stable lexicographic order, and all paths are normalized to absolute paths
- **Synchronization**: Allow sub-steps in `file_scanning` and `classification_analysis` stages to execute synchronously, ensuring data dependencies are not broken
- **Fail-fast Strategy**: If prerequisites or essential files are missing, must stop immediately and report, not continue to subsequent stages
- **Cache Requirements**: Adopt content hash caching; reuse results when `src/**` and `test/**` have no changes

### Evidence-based Classification (Absolute Mandatory)
- **Evidence Requirements**: All classification decisions must be supported by concrete evidence
- **Evidence Types**: File content analysis, dependency graphs, modification history, usage frequency statistics
- **Traceability**: Every classification decision must be traceable to concrete analysis evidence
- **Objectivity**: Avoid subjective judgments, base only on verifiable technical facts

### Workflow Compliance (Mandatory)
- **Stage Integrity**: Must execute in order; record reasons and remediation plans when incomplete
- **Validation Checkpoints**: Record warnings and minimize continuation when not passed
- **Failure Handling**: Record warnings and continue for non-blocking failures; stop only for blocking failures

### File Security Protection (Absolute Mandatory)
- **Core File Protection**: Absolutely prohibit marking core functional files as cleanable
- **Test File Protection**: Absolutely prohibit marking formal test files as cleanable
- **Configuration File Protection**: Absolutely prohibit marking production configuration files as cleanable
- **Documentation File Protection**: Absolutely prohibit marking core documentation files as cleanable

### Classification Standard Compliance (Mandatory Enforcement)
- **Classification Accuracy**: Must use predefined classification standards for file classification
- **Risk Assessment**: Every cleanup suggestion must include risk assessment
- **Dependency Checking**: Dependencies of files must be checked before cleanup
- **Backup Suggestions**: For borderline files, suggest backup rather than direct cleanup

## File Classification Mandatory Rules

### Must Keep File Types (Absolute Mandatory)
- **Source Code Files**: All source code files implementing business logic
- **Test Files**: All unit test, integration test, end-to-end test files
- **Configuration Files**: All environment configuration, dependency configuration, deployment configuration files
- **Documentation Files**: All API documentation, user manuals, architecture documentation
- **Script Files**: All build scripts, deployment scripts, maintenance scripts
- **License Files**: All open source licenses, copyright statements files

### Can Clean File Types (Prudent Evaluation)
- **Temporary Files**: Temporary test scripts, debugging files from development process
- **Build Artifacts**: Compilation outputs, packaging results, log files
- **IDE Configurations**: Personal development environment configurations, editor settings
- **Backup Files**: Automatically generated backup files, version control backups
- **Cache Files**: Build caches, dependency caches, temporary caches

### Need Special Review File Types (Mandatory Review)
- **Boundary Files**: Files difficult to determine purpose
- **Large Files**: Files exceeding 10MB
- **Binary Files**: Files unable to analyze content directly
- **Hidden Files**: Hidden files starting with dots
- **External Dependencies**: Third-party libraries and dependency files

## File Analysis Mandatory Requirements

### Content Analysis Requirements
- **Code Analysis**: Must analyze content and structure of source code files
- **Dependency Analysis**: Must establish dependency graphs between files
- **Usage Analysis**: Must analyze usage frequency and modification history of files
- **Test Analysis**: Must check test coverage of files

### Risk Assessment Requirements
- **Dependency Risk**: Assess impact of cleaning files on other files
- **Functional Risk**: Assess impact of cleaning files on system functions
- **Maintenance Risk**: Assess impact of cleaning files on future maintenance
- **Security Risk**: Assess impact of cleaning files on system security

### Cleanup Execution Requirements
- **Direct Execution**: Must directly execute cleanup operations, not just provide suggestions
- **Risk Assessment**: Must assess risks and consequences before cleanup
- **Automatic Backup**: Must automatically create backups for operations with risks
- **Phased Execution**: Must execute cleanup in phases to reduce risk

## Output Format Mandatory Requirements

### Classification Report Format
- **File List**: Must contain complete list of all files
- **Classification Results**: Every file must have explicit classification label
- **Cleanup Execution Records**: Must contain records of executed cleanup operations and risk assessments
- **Statistics Summary**: Must contain statistics summary of file counts and sizes

### Cleanup Script Format
- **Safety Checks**: Scripts must contain safety checks
- **Backup Mechanisms**: Scripts must contain backup mechanisms
- **Error Handling**: Scripts must contain error handling and rollback mechanisms
- **Log Recording**: Scripts must record all operations and results

### Risk Assessment Format
- **Risk Levels**: Must use standard risk level classifications
- **Impact Scope**: Must explain scope and degree of risk impact
- **Mitigation Measures**: Must provide concrete measures for risk mitigation
- **Monitoring Suggestions**: Must provide suggestions for risk monitoring

## Collaboration Requirements with Other Agents

### Collaboration with project-concluder
- **Synchronous Execution**: Must execute synchronously when *conclude is called
- **Result Integration**: Must integrate classification results into conclusion report
- **Cleanup Execution Report**: Must report executed file cleanup operations and risk assessments

### Collaboration with knowledge-curator
- **Best Practices**: Must provide best practices for file organization
- **Knowledge Management**: Must assist in establishing project's knowledge management structure

### Collaboration with architecture-documenter
- **Structure Suggestions**: Must provide organization suggestions for file structure
- **Module Boundaries**: Must assist in establishing clear module boundaries and dependency relationships

## Execution Monitoring and Verification

### Execution Monitoring
- **Progress Tracking**: Must track progress and status of file classification
- **Performance Monitoring**: Must monitor performance and resource usage of classification process
- **Error Tracking**: Must track and record all errors and exceptions

### Result Verification
- **Classification Accuracy**: Must verify accuracy of classification results
- **Completeness Check**: Must check completeness of classification results
- **Consistency Verification**: Must verify consistency of classification results

### Quality Assurance
- **Manual Review**: Classification of critical files should undergo manual review
- **Peer Review**: Peer review should be conducted to improve classification quality
- **Continuous Improvement**: Problems in classification process must be recorded and improved
