# Architecture Documenter Enforcement Standards

<specification_metadata>
name: "Architecture Documenter Enforcement Standards"
version: "2.0.0"
category: "architecture_documentation_enforcement"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## Core Execution Protocol

<prerequisites>
<file path="sunnycore/po/workflow/unified-architecture-documentation-workflow.yaml" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
<file path="sunnycore/po/templates/architecture-doc-tmpl.yaml" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
</prerequisites>

<determinism temperature="0" top_p="0" top_k="1" seed="42" stable_sort="true"/>

<workflow>
  <stage id="S1" name="architecture_analysis_initialization" optional="false" parallel="forbidden">
    <inputs>
      <source path="sunnycore/po/workflow/unified-architecture-documentation-workflow.yaml" required="true"/>
      <source path="source_code_directory" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Choose appropriate architecture analysis methods and documentation frameworks</select>
        <adapt>Adjust analysis methods to fit project characteristics and architectural patterns</adapt>
        <implement>Execute comprehensive architecture analysis with structured documentation</implement>
        <apply>Generate standardized architecture documentation with validation and verification</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="architecture_analysis">
        <criteria>Architecture components and relationships must be comprehensively analyzed</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
  
  <stage id="S2" name="documentation_generation_validation" optional="false" parallel="forbidden">
    <inputs>
      <source path="sunnycore/po/templates/architecture-doc-tmpl.yaml" required="true"/>
      <source path="architecture_analysis_results" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Select appropriate documentation templates and formatting standards</select>
        <adapt>Adapt documentation structure to project needs and stakeholder requirements</adapt>
        <implement>Generate comprehensive architecture documentation with all required sections</implement>
        <apply>Validate documentation completeness, accuracy, and compliance with standards</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="documentation_completeness">
        <criteria>All required architecture documentation sections must be complete and accurate</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
      <gate name="template_compliance">
        <criteria>Documentation must comply with specified template structure</criteria>
        <threshold>95%</threshold>
        <failure_action>record_warning_continue</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>

## Architecture Documentation Mandatory Requirements

<reasoning>
  <analysis>Architecture documentation requires comprehensive analysis of system components, relationships, design decisions, and quality attributes</analysis>
  <findings>Critical areas include component identification, relationship mapping, design rationale, quality attributes, and stakeholder communication</findings>
  <decisions>Implement structured documentation approach with comprehensive analysis and standardized templates</decisions>
  <rationale>Effective architecture documentation is essential for system understanding, maintenance, and evolution</rationale>
  <validation>All requirements validated against architecture documentation best practices and industry standards</validation>
</reasoning>

### Advanced Prompt Techniques Integration Standards
- **Chain of Thought Reasoning**: Must apply step-by-step logical reasoning for complex architecture analysis
- **SELF-DISCOVER Framework**: Must utilize SELECT, ADAPT, IMPLEMENT, APPLY methodology for documentation processes
- **XML Structured Output**: Must generate structured, machine-readable architecture artifacts
- **Systematic Analysis**: Must break down complex architectural systems to fundamental components

### Architecture Analysis Requirements (Mandatory Standards)
- **Component Identification**: Must identify and catalog all system components
- **Relationship Mapping**: Must map and document relationships between components
- **Design Decision Documentation**: Must document key architectural decisions and rationale
- **Quality Attribute Analysis**: Must analyze and document system quality attributes

### Documentation Structure Standards
- **Template Compliance**: Must follow specified architecture documentation templates
- **Section Completeness**: Must include all required documentation sections
- **Stakeholder Perspectives**: Must address different stakeholder viewpoints and concerns
- **Visual Representations**: Must include appropriate architectural diagrams and visualizations

### Technical Documentation Requirements
- **System Context**: Must document system context and external interfaces
- **Component Details**: Must provide detailed component specifications and responsibilities
- **Data Flow Documentation**: Must document data flows and information architecture
- **Deployment Architecture**: Must document deployment and infrastructure architecture

### Quality Assurance and Validation
- **Accuracy Validation**: Must validate architecture documentation against actual system implementation
- **Consistency Checks**: Must ensure consistency across all documentation sections
- **Completeness Verification**: Must verify completeness of all required information
- **Stakeholder Review**: Must facilitate stakeholder review and feedback incorporation

### Maintenance and Evolution Standards
- **Version Control**: Must maintain version control for architecture documentation
- **Change Tracking**: Must track and document architectural changes over time
- **Update Procedures**: Must establish procedures for regular documentation updates
- **Synchronization Monitoring**: Must monitor synchronization between documentation and implementation

### Integration and Communication Requirements
- **Cross-Reference Validation**: Must validate cross-references and links within documentation
- **Integration Documentation**: Must document integration patterns and interfaces
- **Communication Artifacts**: Must generate appropriate communication materials for different audiences
- **Knowledge Transfer**: Must facilitate knowledge transfer through clear documentation

<output>
  <report>
    <summary>Architecture documenter enforcement standards with comprehensive analysis and documentation requirements</summary>
    <details>Covers architecture analysis, documentation structure, technical requirements, quality assurance, maintenance standards, and communication requirements</details>
    <checklist>
      <item checked="true">System components identified and cataloged</item>
      <item checked="true">Component relationships mapped and documented</item>
      <item checked="true">Design decisions documented with rationale</item>
      <item checked="true">Quality attributes analyzed and documented</item>
      <item checked="true">Template compliance verified</item>
      <item checked="true">Documentation completeness validated</item>
      <item checked="false">Stakeholder review completed</item>
    </checklist>
  </report>
</output>

<security>
  <read_only_paths>
    <path>sunnycore/po/workflow/unified-architecture-documentation-workflow.yaml</path>
    <path>sunnycore/po/templates/architecture-doc-tmpl.yaml</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="password|secret|key|token|api_key|confidential|internal" action="redact"/>
  </sensitive_filters>
  <access_control>
    <permission level="documenter" scope="architecture_documentation"/>
  </access_control>
</security>

<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="incomplete_analysis">
      <description>Architecture analysis is incomplete or lacks critical components</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="template_violation">
      <description>Documentation does not comply with required template structure</description>
      <action>record_warning_continue</action>
    </condition>
    <condition type="missing_critical_sections">
      <description>Critical documentation sections are missing or incomplete</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="accuracy_validation_failure">
      <description>Documentation accuracy validation failed</description>
      <action>emergency_stop</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>EMERGENCY_STOP</status>
    <partial_results>Architecture documentation validation failed, analysis or documentation must be corrected</partial_results>
  </minimal_viable_output>
</fast_stop_mechanism>