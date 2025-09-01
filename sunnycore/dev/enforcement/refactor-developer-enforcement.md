# Refactor Developer Mandatory Enforcement Standards

<core_execution_protocol>
## Core Execution Protocol

<prerequisite_conditions>
### Necessary Prerequisites (Relaxed)
- **Recommendation**: Load unified workflow and plan before starting; if missing, record in dev_notes.validation_warnings and continue
- **Workflow Reading**: Should read `{project_root}/sunnycore/dev/workflow/refactor-developer-workflow.md`, record warning if failed
- **Plan Check**: Attempt to locate and read the implementation plan for task_id; if missing, record warning and continue with minimal context
</prerequisite_conditions>

<behavioral_equivalence>
### Behavioral Equivalence (Absolute Mandatory)
- **Functional Invariance**: Absolutely cannot change any external behavior
- **API Preservation**: Must keep all public interfaces unchanged
- **Contract Maintenance**: All existing contracts must be completely maintained
- **Backward Compatibility**: Must ensure complete backward compatibility
</behavioral_equivalence>

<scope_compliance>
### Scope Compliance (Relaxed Recording)
- **Scope Boundaries**: Should stay within `scope.in_scope`; record warnings and reasons/remedies when deviated
- **Violation Handling**: Do not interrupt flow, record in dev_notes.validation_warnings and challenges_and_deviations
- **Impact Assessment**: If scope-outside impacts are involved, record risks and mitigation solutions
</scope_compliance>

<workflow_compliance>
### Workflow Compliance
- **Stage Integrity**: Never skip workflow stages, execute all stages in order
- **Specialization Requirements**: Must execute specialized actions defined in developer_specializations.refactor
</workflow_compliance>

<refactor_specialized_enforcement>
### Refactor Specialized Mandatory Requirements

<baseline_capture>
#### Baseline Capture (Mandatory Execution)
- **Test Suite Execution**: Must run complete test suite and ensure all pass
- **API Capture**: Must capture signatures and behaviors of all public APIs
- **Performance Baseline**: Must measure and record current performance baseline
- **Behavioral Baseline**: Must record all observable external behaviors
</baseline_capture>

<characterization_testing>
#### Characterization Testing (Mandatory Implementation)
- **Behavioral Testing**: Must create tests for all existing behaviors
- **Invariant Assertions**: Must assert all important invariants
- **Contract Testing**: Must create tests for all contracts
- **Regression Testing**: Must create tests to prevent regressions
</characterization_testing>

<incremental_refactoring>
#### Incremental Refactoring (Mandatory Method)
- **Atomic Commits**: Each change must be atomic, verifiable independently
- **Small Steps**: Each change must be small enough for easy review and understanding
- **Green State**: Tests must remain passing after each commit
- **API Migration**: If API changes are needed, must use incremental migration strategy
</incremental_refactoring>

<validation_requirements>
#### Validation Requirements (Mandatory Execution)
- **Baseline Comparison**: Must compare with baseline after each change
- **API Breaking Check**: Must ensure no API breaking changes
- **Performance Validation**: Must validate performance has not regressed
- **Behavioral Validation**: Must validate external behavior is completely consistent
</validation_requirements>
</refactor_specialized_enforcement>

<testing_requirements>
### Testing Requirements (Mandatory Maintenance)
- **Coverage Maintenance**: Must maintain or improve existing test coverage
- **Test Quality**: Tests after refactoring must be clearer and more maintainable
- **Test Refactoring**: Test code may also need refactoring, but must maintain verification capability
- **Regression Protection**: Must ensure refactoring does not cause test regressions
</testing_requirements>

<code_quality_principles>
### Code Quality Principles (Mandatory Application)
- **SOLID Principles**: Must apply SOLID design principles
- **KISS Principle**: Keep code simple and clear
- **DRY Principle**: Eliminate duplication, but avoid over-abstraction
- **Separation of Concerns**: Ensure appropriate separation of concerns
</code_quality_principles>

<performance_requirements>
### Performance Requirements (Mandatory Maintenance)
- **Performance Maintenance**: Must maintain or improve runtime performance
- **Memory Efficiency**: Must maintain or improve memory usage
- **Regression Avoidance**: Must avoid any performance regressions
- **Benchmark Testing**: Must conduct benchmark testing after major refactoring
</performance_requirements>

<incremental_change_requirements>
### Incremental Change Requirements (Mandatory Execution)
- **Reviewable Changes**: Each change must be small enough for effective review
- **Clear Checkpoints**: Each stage must have clear checkpoints
- **Rollback Capability**: Each change must be safely rollbackable
- **Change Documentation**: Each change must have clear documentation and explanation
</incremental_change_requirements>

<standards_compliance>
### Standards Compliance (Mandatory Compliance)
- **Coding Standards**: Must follow project's coding standards
- **Tool Compliance**: Must pass linter and formatter checks
- **Convention Following**: Must follow language and framework best practices
- **Documentation Standards**: Code documentation must comply with project standards
</standards_compliance>

<risk_management>
### Risk Management (Mandatory Implementation)
- **Change Impact Assessment**: Each change must assess impact scope
- **Dependency Analysis**: Must analyze impact of changes on dependencies
- **Rollback Planning**: Each refactoring stage must have a rollback plan
- **Risk Mitigation**: Identified risks must have corresponding mitigation measures
</risk_management>

<documentation_and_traceability>
### Documentation and Traceability
- **Refactoring Decision Recording**: Important refactoring decisions must be recorded
- **Change Documentation**: Each change must have clear documentation
- **Traceability**: Must reference task_id in PRs, commits, and code comments
- **Impact Documentation**: Impact of refactoring on the system must be recorded
</documentation_and_traceability>

<dev_notes_requirements>
### DEV_NOTES Fill Requirements (🚨 Mandatory Recording Without Interruption 🚨)
- **handover_docs Stage Execution**: Must execute complete handover_docs stage after refactoring completion
- **detailed_changes Recording**: Must record all refactoring changes in detail in dev_notes
- **F-IDs/N-IDs Mapping**: Mapping gaps do not interrupt; record gap list and temporary mapping/reasoning
- **Refactoring Strategy Recording**: Must record adopted refactoring strategy, incremental steps, and decision rationale
- **Behavioral Preservation Verification**: Must record behavioral invariance verification process and test results
- **Performance Impact Analysis**: Must record pre/post-refactoring performance comparisons and optimization results
- **Risk Mitigation Recording**: Must record identified risks, mitigation measures, and rollback plans
- **Code Quality Improvement**: Must record code quality improvement indicators and maintainability enhancements
- **Technical Debt Cleanup**: Must record cleaned technical debt and future improvement suggestions
- **Fill Quality Requirements**: dev_notes cannot be omitted or perfunctory, must provide sufficient details for future maintenance reference
</dev_notes_requirements>

<markdown_format_conversion>
### Markdown Format Conversion (Absolute Mandatory)
- **YAML to Markdown**: Must completely convert `{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml` structure to standard Markdown format
- **Header Levels**: YAML sections convert to corresponding Markdown headers (# ## ### #### ##### ######)
- **List Format**: YAML arrays convert to Markdown lists (- or 1. format)
- **Code Blocks**: Code snippets use standard Markdown code blocks (```language)
- **Table Format**: Structured data uses Markdown table format | Field | Value |
- **Link Format**: Use standard Markdown link format [text](URL)
- **Block Quotes**: Important notes use > quote format
- **Emphasis Markers**: Use **bold** and *italic* to appropriately emphasize key content
- **Refactoring Specific**: Use appropriate tables and code block markers for before/after refactoring comparisons, performance test results, code quality measurements
</markdown_format_conversion>

<validation_checklist>
### Validation Checklist (Mandatory Execution)
- [ ] All tests still pass
- [ ] No API breaking changes
- [ ] Performance baseline maintained or improved
- [ ] Code coverage maintained or improved
- [ ] External behavior completely consistent
- [ ] All public interfaces remain unchanged
- [ ] Coding standards followed
- [ ] Documentation appropriately updated
</validation_checklist>

<output_locations>
### Output Locations (Fixed)
- **Development Records**: `{{project_root}}/docs/dev-notes/{{task_id}`(such as `1`, `2`, `3`...)}-dev-notes.md`
- **Template Reference**: `{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml`
</output_locations>

<quality_gates>
### Quality Gates (Mandatory Pass)
- **Static Analysis**: Refactored code must pass all static analysis checks
- **Security Scanning**: Must ensure refactoring introduces no security issues
- **Performance Testing**: Must pass all performance tests
- **Compatibility Testing**: Must pass all compatibility tests
</quality_gates>
</core_execution_protocol>

<refactor_stage_checkpoints>
## Refactoring Stage Checkpoints (Mandatory Validation)

<preparation_stage>
### Preparation Stage
- [ ] Baseline tests all pass
- [ ] Performance baseline recorded
- [ ] API signatures captured
- [ ] Refactoring plan formulated
</preparation_stage>

<execution_stage>
### Execution Stage
- [ ] Tests still pass after each change
- [ ] Changes are small and atomic
- [ ] No API breaking changes
- [ ] No significant performance regression
</execution_stage>

<verification_stage>
### Verification Stage
- [ ] Completely consistent with baseline
- [ ] All tests pass
- [ ] Code quality improved
- [ ] Documentation updated
</verification_stage>
</refactor_stage_checkpoints>

<failure_handling_protocol>
## Failure Handling Protocol (Record and Continue)
- **Plan Missing**: Record warning and alternative information sources; continue
- **Baseline Tests Not All Green**: Record risks and remediation plans; downgrade scope if necessary
- **Behavioral Change Risk**: Record detection results and rollback strategy; do not interrupt
- **Performance Regression**: Record measurements and optimization plans; continue under controllable risk
- **Test Coverage Decline**: Record gaps and recovery timeline
</failure_handling_protocol>