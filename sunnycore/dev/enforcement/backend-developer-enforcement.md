# Backend Developer Enforcement Standards

<core_execution_protocol>
## Core Execution Protocol

<mandatory_prerequisites>
### Mandatory Prerequisites
- **Recommendation**: Load unified workflow and implementation plans before starting development; if missing, record in dev_notes.validation_warnings and continue execution
- **Workflow Reading**: Should read `{project_root}/sunnycore/dev/workflow/backend-developer-workflow.md`, record warning if failed
- **Plan Verification**: Attempt to locate and read the implementation plan for task_id; if missing, record warning and continue with minimal viable context
</mandatory_prerequisites>

<workflow_compliance>
### Workflow Compliance
- **Stage Integrity**: Never skip workflow stages, execute all stages in sequential order
</workflow_compliance>
</core_execution_protocol>

<backend_specific_requirements>
## Backend-Specific Mandatory Requirements

<data_security_integrity>
### Data Security and Integrity
- **Data Changes**: Must draft idempotent and reversible migrations
- **Backup Strategy**: All data changes must have rollback plans
- **Transaction Integrity**: Ensure ACID properties are maintained
</data_security_integrity>

<api_security>
### API Security
- **Authentication**: Must implement complete authentication mechanisms
- **Authorization Control**: Must implement fine-grained authorization control
- **Input Validation**: Must perform strict validation on all inputs
- **Data Sanitization**: Must perform appropriate sanitization on all outputs
- **Confidentiality Handling**: Never expose sensitive information in logs or responses
</api_security>

<performance_requirements>
### Performance Requirements
- **Latency Targets**: Must meet specified latency requirements in the plan
- **Throughput Targets**: Must meet specified throughput requirements in the plan
- **Memory Targets**: Must comply with memory usage limits
- **Monitoring Implementation**: Must implement appropriate performance monitoring
</performance_requirements>

<testing_requirements>
### Testing Requirements
- **Test-First Approach**: Should write tests before implementation; if not achieved, record reasons and remediation plans
- **Test Types**:
  - Unit Tests: Aligned with F-IDs
  - Integration Tests: Test inter-service interactions
  - Contract Tests: Ensure API contract compliance
- **Coverage Threshold**: Must meet specified test coverage requirements
</testing_requirements>

<architecture_principles>
### Architecture Principles
- **SOLID Principles**: Must apply SOLID design principles
- **Clean Architecture**: Must implement separation of concerns
- **Error Handling**: Must implement appropriate error handling mechanisms
- **Logging**: Must implement structured logging
- **Monitoring**: Must implement appropriate system monitoring
</architecture_principles>

<reliability_requirements>
### Reliability Requirements
- **Graceful Degradation**: System must handle failures gracefully
- **Idempotency**: API operations must be designed as idempotent
- **Retry Mechanisms**: Must implement appropriate retry strategies
- **Circuit Breaker**: Must implement circuit breaker pattern for dependency failures
</reliability_requirements>

<quality_gates>
### Quality Gates
- **Static Analysis**: Code must pass static analysis checks
- **Security Scanning**: Must pass security vulnerability scanning
- **Performance Testing**: Must pass performance benchmark testing
- **Compatibility Testing**: Must maintain backward compatibility
</quality_gates>
</backend_specific_requirements>

<security_checklist>
## Security Checklist
- [ ] All inputs are validated and sanitized
- [ ] All outputs are appropriately encoded
- [ ] Sensitive data is encrypted at rest
- [ ] APIs implement proper authentication and authorization
- [ ] Error handling does not expose sensitive information
- [ ] Logging does not contain sensitive data
- [ ] Dependencies are latest and secure versions
</security_checklist>

<failure_handling_protocol>
## Failure Handling Protocol
- **Plan Missing**: Record warnings and alternative information sources used; continue with minimal viable implementation
- **Scope Deviation**: Record deviation reasons, impacts, and remediation plans; do not interrupt
- **Security Checks Failed**: Record risks and mitigation measures; mark as high-priority fixes
- **Performance Not Met**: Record measurement results and optimization plans; continue under controlled risk
</failure_handling_protocol>