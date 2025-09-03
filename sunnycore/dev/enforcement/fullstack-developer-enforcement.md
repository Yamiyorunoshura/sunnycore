# Fullstack Developer Enforcement Standards

<core_execution_protocol>
## Core Execution Protocol

<mandatory_prerequisites>
### Mandatory Prerequisites (Relaxed)
- **Recommendation**: Load unified workflow and implementation plans before starting; if missing, record in dev_notes.validation_warnings and continue
- **Workflow Reading**: Should read `{project_root}/sunnycore/dev/workflow/fullstack-developer-workflow.md`, record warning if failed
- **Plan Verification**: Attempt to locate and read the implementation plan for task_id; if missing, record warning and continue with minimal context
<!-- mandatory_prerequisites>

<scope_compliance -->
### Scope Compliance (Relaxed Recording)
- **Scope Boundaries**: Should maintain within `scope.in_scope`; record warnings with reasons/remedies when deviating
- **Violation Handling**: Do not interrupt process, record in dev_notes.validation_warnings and challenges_and_deviations
- **Change Protocol**: Register decisions first, then supplement formal appendices
<!-- scope_compliance>

<workflow_compliance -->
### Workflow Compliance
- **Stage Integrity**: Never skip workflow stages, execute all stages in sequential order
- **Dual Specialization**: Must execute frontend and backend specialized actions defined in developer_specializations.fullstack
<!-- workflow_compliance>


<fullstack_enforcement_requirements>
## Fullstack Specialization Mandatory Requirements

<end_to_end_consistency>
### End-to-End Consistency (Absolute Mandatory)
- **Contract Alignment**: Must ensure complete consistency of contracts between frontend, backend, and database
- **Data Model Synchronization**: Ensure synchronization of data models between frontend and backend
- **API Contracts**: Frontend and backend API contracts must match precisely
- **Type Consistency**: Type definitions must remain consistent across layers
<!-- end_to_end_consistency>

<backend_integration_requirements -->
### Backend Integration Requirements
- **Data Changes**: Must draft idempotent and reversible migrations
- **API Security**: Must implement complete authentication, authorization, validation, and sanitization mechanisms
- **Performance Achievement**: Must meet latency, throughput, and memory targets
- **Error Handling**: Must implement unified error handling strategy
<!-- backend_integration_requirements>

<frontend_integration_requirements -->
### Frontend Integration Requirements (Relaxed)
- **UX Requirements**: Must extract all UI-IDs and verify design assets
- **Component Architecture**: Must create component skeleton and define types and interfaces
- **Accessibility**: Should ensure A11Y compliance; if temporarily not met, record risks and remediation plans
- **State Management**: Must define routing, enumerate application states, and identify global state
<!-- frontend_integration_requirements>

<frontend_backend_flow_integration -->
### Frontend-Backend Flow Integration (Mandatory Execution)
- **wire_frontend_to_backend_flows**: Must execute frontend-backend flow integration
- **Data Flow Validation**: Ensure correct data flow between frontend and backend
- **State Synchronization**: Frontend state must remain synchronized with backend state
- **Error Propagation**: Backend errors must be properly propagated to frontend and displayed appropriately
<!-- frontend_backend_flow_integration>


<quality_requirements>
## Quality Requirements

<testing_requirements>
### Testing Requirements (Mandatory but Non-Disruptive)
- **Test-First Approach**: Should write tests before implementation; when not achieved, record reasons and remediation plans
- **Comprehensive Test Coverage**:
  - Unit Tests: Cover F-IDs
  - Integration Tests: Frontend-backend integration tests
  - Contract Tests: API contract tests
  - E2E Tests: End-to-end user flow tests
- **Coverage Threshold**: Must meet specified test coverage requirements
<!-- testing_requirements>

<performance_requirements -->
### Performance Requirements (Mandatory Achievement)
- **Core Web Vitals**: Must achieve LCP, INP, TTI targets
- **API Latency**: Must comply with API response time requirements
- **Database Efficiency**: Must optimize query performance
- **Resource Optimization**: Both frontend and backend resources must be optimized
<!-- performance_requirements>

<security_requirements -->
### Security Requirements (Mandatory Execution)
- **Multi-Layer Security**: Apply security best practices across frontend, backend, and database layers
- **Data Validation**: Both frontend and backend must perform data validation
- **Authentication**: Unified authentication mechanism
- **Authorization Control**: Consistent authorization strategy
- **Data Encryption**: Sensitive data must be encrypted in both transit and storage
<!-- security_requirements>

<observability_requirements -->
### Observability Requirements (Mandatory Implementation)
- **Logging**: Unified logging format and strategy across frontend and backend
- **Metrics Monitoring**: Monitoring of key business and technical metrics
- **Error Tracking**: End-to-end error tracking mechanism
- **Performance Monitoring**: Full-stack performance monitoring
<!-- observability_requirements>


<architectural_principles>
## Architecture Principles

<core_principles>
### Architecture Principles (Mandatory Compliance)
- **Separation of Concerns**: Clear frontend-backend responsibility separation
- **SOLID Principles**: Apply SOLID principles in both frontend and backend
- **Consistency Principle**: Architecture decisions must remain consistent across the full stack
- **Scalability**: Design must support future expansion needs
<!-- core_principles>


<documentation_requirements>
## Documentation Requirements

<traceability_documentation>
### Documentation and Traceability
- **Full-Stack Documentation**: Must update API documentation and component documentation
- **Architecture Decision Records**: Important architecture decisions must be documented
- **Traceability**: Must reference task_id in PRs, commits, and code comments
- **Integration Documentation**: Detailed documentation of frontend-backend integration points
<!-- traceability_documentation>

<dev_notes_requirements -->
### DEV_NOTES Documentation Requirements (🚨 Mandatory Recording but Non-Disruptive 🚨)
- **handover_docs Stage Execution**: Must execute complete handover_docs stage after development completion
- **detailed_changes Recording**: Must document all frontend, backend, and integration changes in detail within dev_notes
- **F-IDs/UI-IDs Mapping**: Mapping gaps do not interrupt; record gap list with provisional mappings/reasons
- **Full-Stack Integration Recording**: Must document frontend-backend integration implementation, data flow design, and API contract realization
- **Architecture Decision Recording**: Must document cross-layer architecture decisions, technology selections, and integration strategies
- **Performance Integration Validation**: Must document end-to-end performance test results and optimization measures
- **Security Implementation Recording**: Must document multi-layer security implementation, authentication integration, and data protection measures
- **Deployment and Configuration**: Must document deployment strategy, environment configuration, and monitoring setup
- **Integration Test Recording**: Must document end-to-end tests, contract tests, and integration validation results
- **Documentation Quality Requirements**: dev_notes cannot be omitted or superficial, must provide sufficient detail for future maintenance reference
<!-- dev_notes_requirements>

<markdown_conversion -->
### Markdown Format Conversion (Absolute Mandatory)
- **YAML to Markdown**: Must completely convert `{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml` structure to standard Markdown format
- **Heading Levels**: YAML sections convert to corresponding Markdown headings (# ## ### #### ##### ######)
- **List Format**: YAML arrays convert to Markdown lists (- or 1. format)
- **Code Blocks**: Code snippets use standard Markdown code blocks (```language)
- **Table Format**: Structured data uses Markdown table format | Field | Value |
- **Link Format**: Use standard Markdown link format [text](URL)
- **Block Quotes**: Important notes use > quote format
- **Emphasis Markers**: Use **bold** and *italic* to appropriately emphasize key content
- **Full-Stack Specifications**: API contracts, data flow diagrams, architecture diagrams use appropriate code blocks and Mermaid chart markers
<!-- markdown_conversion>

<output_location -->
### Output Location (Fixed)
- **Development Records**: `{{project_root}}/docs/dev-notes/{{task_id}`(e.g. `1`, `2`, `3`...)}-dev-notes.md`
- **Template Reference**: `{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml`
<!-- output_location>


<quality_gates>
## Quality Gates

<mandatory_quality_gates>
### Quality Gates (Mandatory Passage)
- **Static Analysis**: Both frontend and backend must pass static analysis
- **Security Scanning**: Full-stack security vulnerability scanning
- **Performance Testing**: End-to-end performance testing
- **Accessibility Audit**: Frontend accessibility audit
<!-- mandatory_quality_gates>


<integration_checklist>
## Full-Stack Integration Checklist (Mandatory Execution)

<mandatory_integration_checks>
- [ ] Frontend-backend API contracts are completely consistent
- [ ] Data models remain synchronized across layers
- [ ] Error handling strategy is uniformly implemented
- [ ] Authentication mechanism is end-to-end consistent
- [ ] Performance targets are achieved across all layers
- [ ] Security measures are implemented across all layers
- [ ] Tests cover end-to-end flows
- [ ] Monitoring and logging cover the full stack
<!-- mandatory_integration_checks>


<special_considerations>
## Special Considerations

<technology_coordination>
### Technology Coordination Requirements
- **Technology Selection Consistency**: Frontend and backend technology selections must be coordinated
- **Version Synchronization**: Ensure compatibility of frontend and backend dependency versions
- **Deployment Coordination**: Frontend and backend deployments must be coordinated
- **Configuration Management**: Environment configuration must remain consistent between frontend and backend
<!-- technology_coordination>


<failure_handling_protocol>
## Failure Handling Protocol (Record and Continue)

<failure_recovery>
- **Plan Missing**: Record warnings and alternative information sources; continue
- **Scope Deviation**: Record deviations/impacts/remediation plans; do not interrupt
- **Contract Inconsistency**: Record differences and remediation plans; do not interrupt
- **Testing Not Met**: Record failures and remediation plans; do not interrupt
- **Performance Not Met**: Record measurements/optimization plans; continue under controlled risk
<!-- failure_recovery>
