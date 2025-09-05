# Task Reviewer Enforcement Standards

<specification_metadata>
name: "Task Reviewer Enforcement Standards"
version: "2.0.0"
category: "qa_review_enforcement"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## Core Execution Protocol

<prerequisites>
<file path="sunnycore/qa/workflow/unified-review-workflow.md" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
<file path="sunnycore/qa/templates/review-tmpl.yaml" required="true">
  <failure_action>emergency_stop</failure_action>
</file>
<file path="agents/qa_task-reviewer_*.md" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
</prerequisites>

<determinism temperature="0" top_p="0" top_k="1" seed="42" stable_sort="true"/>

<workflow>
  <stage id="S1" name="review_initialization" optional="false" parallel="forbidden">
    <inputs>
      <source path="development_artifacts" required="true"/>
      <source path="review_requirements" required="true"/>
      <source path="quality_standards" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Analyze development artifacts and determine appropriate review domains and strategies</select>
        <adapt>Adapt review approach based on artifact type, complexity, and organizational requirements</adapt>
        <implement>Initialize specialized reviewers and establish review coordination framework</implement>
        <apply>Execute comprehensive multi-domain review with evidence-based assessment</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="reviewer_selection">
        <criteria>Appropriate specialized reviewers must be selected based on artifact requirements</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
  
  <stage id="S2" name="specialized_review_execution" optional="false" parallel="allowed">
    <inputs>
      <source path="reviewer_assignments" required="true"/>
      <source path="domain_standards" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Execute parallel specialized reviews across all required domains</select>
        <adapt>Adapt review intensity and focus based on domain-specific requirements</adapt>
        <implement>Perform comprehensive review with domain-specific tools and methodologies</implement>
        <apply>Generate structured findings with evidence-based recommendations</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="domain_completeness">
        <criteria>All required review domains must be comprehensively covered</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
      <gate name="evidence_quality">
        <criteria>All findings must be supported by concrete evidence and citations</criteria>
        <threshold>95%</threshold>
        <failure_action>record_warning_continue</failure_action>
      </gate>
    </quality_gates>
  </stage>

  <stage id="S3" name="review_consolidation" optional="false" parallel="forbidden">
    <inputs>
      <source path="domain_review_reports" required="true"/>
      <source path="quality_standards" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Consolidate findings across all review domains and identify conflicts</select>
        <adapt>Resolve inter-domain conflicts and prioritize findings based on impact</adapt>
        <implement>Generate unified review report with integrated recommendations</implement>
        <apply>Validate final assessment against organizational quality standards</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="consolidation_completeness">
        <criteria>All domain findings must be properly integrated and conflicts resolved</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>

## Review Domain Standards

<reasoning>
  <analysis>Task reviewers require specialized domain expertise with standardized enforcement mechanisms across code quality, security, performance, testing, documentation, and integration domains</analysis>
  <findings>Critical success factors include domain specialization, evidence-based assessment, standardized reporting, and integrated quality validation</findings>
  <decisions>Implement comprehensive multi-domain review framework with specialized enforcement standards for each review area</decisions>
  <rationale>Specialized domain expertise ensures comprehensive quality assessment while standardized enforcement ensures consistency and reliability</rationale>
  <validation>All requirements validated against software engineering best practices and quality assurance frameworks</validation>
</reasoning>

### Code Quality Review Standards (Mandatory Requirements)
- **Readability Assessment**: Must evaluate code readability, naming conventions, function length, and structural clarity
- **Architecture Evaluation**: Must validate SOLID principles, design patterns, modularity, and dependency management  
- **Complexity Analysis**: Must assess cyclomatic complexity, cognitive complexity, and maintainability metrics
- **Best Practices Compliance**: Must verify coding standards, error handling, resource management, and performance considerations
- **Quality Metrics**: Code readability ≥85%, architecture score ≥80%, complexity score ≤10, maintainability index ≥70%

### Security Review Standards (Mandatory Requirements)
- **Vulnerability Detection**: Must identify and assess security vulnerabilities using CVSS scoring methodology
- **Authentication & Authorization**: Must evaluate identity verification, access control mechanisms, and session management
- **Data Protection**: Must verify data encryption, transmission security, storage security, and access controls
- **Input Validation**: Must assess protection against injection attacks, XSS, command injection, and path traversal
- **Security Metrics**: Vulnerability count = 0, security score ≥90%, authentication strength ≥85%, data protection level ≥95%

### Performance Review Standards (Mandatory Requirements)
- **Response Time Analysis**: Must measure and evaluate API response times, page load times, and system latency
- **Throughput Assessment**: Must evaluate system capacity, concurrent user support, and processing capabilities
- **Resource Utilization**: Must analyze CPU usage, memory consumption, disk I/O, and network bandwidth efficiency
- **Scalability Evaluation**: Must assess horizontal and vertical scaling capabilities and load balancing effectiveness
- **Performance Metrics**: Response time accuracy ≥95%, throughput assessment ≥90%, resource utilization analysis ≥90%, scalability prediction ≥85%

### Testing Review Standards (Mandatory Requirements)
- **Coverage Analysis**: Must evaluate unit test coverage, integration test coverage, and end-to-end test coverage
- **Test Strategy Assessment**: Must review test planning, test case design, test environment configuration, and test data management
- **Automation Evaluation**: Must assess test automation levels, script quality, CI/CD integration, and execution efficiency
- **Test Quality Validation**: Must verify test effectiveness, defect detection capability, and regression testing adequacy
- **Testing Metrics**: Unit test coverage ≥85%, integration test coverage ≥75%, e2e test coverage ≥60%, test execution success rate ≥95%

### Documentation Review Standards (Mandatory Requirements)
- **Technical Documentation**: Must evaluate architecture docs, design docs, implementation docs, and deployment documentation
- **User Documentation**: Must assess user manuals, installation guides, configuration instructions, and troubleshooting guides
- **API Documentation**: Must verify API specifications, interface descriptions, code examples, and error handling documentation
- **Documentation Quality**: Must evaluate completeness, accuracy, readability, and maintainability of all documentation
- **Documentation Metrics**: Coverage ≥90%, accuracy ≥95%, user satisfaction ≥85%, freshness ≤30 days

### Integration Review Standards (Mandatory Requirements)
- **System Integration**: Must evaluate inter-system communication, data synchronization, error handling, and rollback mechanisms
- **API Design Assessment**: Must validate interface specifications, version management, error handling, and documentation completeness
- **Data Flow Analysis**: Must assess data transmission security, consistency guarantees, validation mechanisms, and backup strategies
- **Integration Testing**: Must verify end-to-end testing, contract testing, performance testing, and failure recovery testing
- **Integration Metrics**: Coverage ≥95%, API contract compliance = 100%, data consistency rate ≥99%, integration test pass rate ≥95%

## Universal Quality Assurance Requirements

### Evidence-Based Assessment Standards
- **Concrete Evidence**: All findings must be supported by specific code examples, test results, or measurement data
- **Traceability**: Clear mapping from identified issues to specific file locations, line numbers, and code sections
- **Reproducibility**: All assessments must be reproducible using standardized tools and methodologies
- **Citation Standards**: Evidence must include file paths, line ranges, timestamps, and verification checksums

### Reporting and Documentation Standards
- **Structured Output**: All reports must follow standardized JSON schemas for automated processing and integration
- **Executive Summary**: High-level findings and recommendations suitable for stakeholder communication
- **Detailed Analysis**: Comprehensive technical analysis with supporting evidence and improvement recommendations
- **Action Items**: Prioritized list of required actions with estimated effort and impact assessment

### Quality Gate Enforcement
- **Pass/Fail Criteria**: Clear threshold-based criteria for all quality gates with standardized scoring
- **Escalation Procedures**: Defined processes for handling quality gate failures and exception requests
- **Compliance Tracking**: Automated tracking of quality metric compliance and trend analysis
- **Continuous Improvement**: Regular review and updating of quality standards based on lessons learned

### Tool Integration Requirements
- **Static Analysis**: Integration with code analysis tools for automated quality assessment
- **Security Scanning**: Integration with vulnerability scanners and security assessment platforms
- **Performance Testing**: Integration with load testing and performance monitoring tools
- **Test Automation**: Integration with test frameworks and coverage analysis tools

## Fast-Stop Mechanisms and Emergency Procedures

<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="critical_quality_failure">
      <description>Critical code quality issues detected with maintainability index below 50</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="critical_security_vulnerability">
      <description>High or critical security vulnerabilities detected with CVSS score ≥8.0</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="critical_performance_issue">
      <description>Severe performance issues detected with response time >5 seconds</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="critical_test_gap">
      <description>Critical functionality lacks test coverage with coverage <60%</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="critical_documentation_gap">
      <description>Critical functionality lacks documentation with coverage <70%</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="critical_integration_failure">
      <description>Critical system integration failures or data inconsistency detected</description>
      <action>emergency_stop</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>EMERGENCY_STOP</status>
    <partial_results>Review terminated due to critical issues requiring immediate attention</partial_results>
    <priority_actions>Address critical findings before proceeding with development activities</priority_actions>
  </minimal_viable_output>
</fast_stop_mechanism>

## Domain Integration and Coordination

### Cross-Domain Dependency Management
- **Dependency Mapping**: Clear identification of dependencies between review domains
- **Coordination Protocols**: Standardized communication mechanisms between specialized reviewers
- **Conflict Resolution**: Systematic procedures for resolving conflicts between domain findings
- **Priority Alignment**: Unified prioritization framework across all review domains

### Workflow Integration Standards
- **Development Lifecycle**: Integration with all phases of software development lifecycle
- **CI/CD Integration**: Automated integration with continuous integration and deployment pipelines
- **Feedback Loops**: Structured mechanisms for incorporating review feedback into development processes
- **Metrics Collection**: Automated collection and analysis of review metrics for continuous improvement

### Stakeholder Communication
- **Multi-Level Reporting**: Tailored reports for different stakeholder audiences (developers, managers, executives)
- **Progress Tracking**: Real-time visibility into review progress and completion status
- **Issue Escalation**: Clear procedures for escalating critical findings to appropriate stakeholders
- **Decision Support**: Data-driven recommendations to support development and deployment decisions

<output>
  <report>
    <summary>Comprehensive task reviewer enforcement standards covering all quality assurance domains</summary>
    <details>Establishes mandatory requirements for code quality, security, performance, testing, documentation, and integration reviews with evidence-based assessment and standardized reporting</details>
    <checklist>
      <item checked="true">Code quality standards defined</item>
      <item checked="true">Security review requirements established</item>
      <item checked="true">Performance evaluation criteria specified</item>
      <item checked="true">Testing coverage standards set</item>
      <item checked="true">Documentation quality requirements defined</item>
      <item checked="true">Integration review standards established</item>
      <item checked="true">Evidence-based assessment framework implemented</item>
      <item checked="true">Fast-stop mechanisms configured</item>
      <item checked="true">Cross-domain coordination protocols defined</item>
      <item checked="false">Stakeholder training completed</item>
      <item checked="false">Tool integration validated</item>
    </checklist>
  </report>
</output>

<security>
  <read_only_paths>
    <path>sunnycore/qa/workflow/unified-review-workflow.md</path>
    <path>sunnycore/qa/templates/review-tmpl.yaml</path>
    <path>agents/qa_task-reviewer_*.md</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="password|secret|key|token|api_key|confidential|proprietary|internal" action="redact"/>
  </sensitive_filters>
  <access_control>
    <permission level="reviewer" scope="quality_assurance"/>
  </access_control>
</security>