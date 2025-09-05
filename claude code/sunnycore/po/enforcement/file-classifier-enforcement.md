# File Classifier Enforcement Standards

<specification_metadata>
name: "File Classifier Enforcement Standards"
version: "2.0.0"
category: "file_classification_enforcement"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## Core Execution Protocol

<prerequisites>
<file path="sunnycore/po/workflow/unified-file-classification-workflow.yaml" required="true">
  <failure_action>emergency_stop</failure_action>
</file>
<file path="file_classification_rules.yaml" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
</prerequisites>

<determinism temperature="0" top_p="0" top_k="1" seed="42" stable_sort="true"/>

<workflow>
  <stage id="S1" name="file_analysis_initialization" optional="false" parallel="forbidden">
    <inputs>
      <source path="sunnycore/po/workflow/unified-file-classification-workflow.yaml" required="true"/>
      <source path="target_file_set" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Analyze file characteristics and select appropriate classification methods</select>
        <adapt>Adapt classification criteria based on file types, content patterns, and project structure</adapt>
        <implement>Execute comprehensive file analysis with structured classification rules</implement>
        <apply>Generate standardized file classification results with validation and verification</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="file_analysis_completeness">
        <criteria>All target files must be analyzed and categorized</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
  
  <stage id="S2" name="classification_validation" optional="false" parallel="forbidden">
    <inputs>
      <source path="classification_results" required="true"/>
      <source path="validation_rules" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Validate classification accuracy and consistency across all analyzed files</select>
        <adapt>Adjust validation criteria based on classification complexity and project requirements</adapt>
        <implement>Execute comprehensive validation with error detection and correction</implement>
        <apply>Generate final classification report with quality assurance and compliance verification</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="classification_accuracy">
        <criteria>Classification accuracy must meet minimum threshold standards</criteria>
        <threshold>95%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
      <gate name="consistency_validation">
        <criteria>Classification consistency across similar files must be maintained</criteria>
        <threshold>98%</threshold>
        <failure_action>record_warning_continue</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>

## File Classification Mandatory Requirements

<reasoning>
  <analysis>File classification requires systematic analysis of file characteristics, content patterns, and project structure to ensure accurate categorization</analysis>
  <findings>Critical areas include file type identification, content analysis, pattern recognition, structural classification, and validation consistency</findings>
  <decisions>Implement comprehensive classification framework with automated validation and quality assurance</decisions>
  <rationale>Accurate file classification is essential for project organization, code analysis, and automated tooling effectiveness</rationale>
  <validation>All requirements validated against file classification best practices and project management standards</validation>
</reasoning>

### File Analysis Standards (Mandatory Requirements)
- **File Type Identification**: Must accurately identify file types based on extensions, headers, and content
- **Content Pattern Analysis**: Must analyze content patterns to determine file purpose and classification
- **Structural Analysis**: Must analyze file structure and organization patterns
- **Dependency Mapping**: Must identify and map file dependencies and relationships

### Classification Methodology Requirements
- **Multi-Criteria Classification**: Must apply multiple classification criteria for comprehensive categorization
- **Pattern Recognition**: Must implement pattern recognition for consistent classification
- **Context-Aware Classification**: Must consider project context and file relationships
- **Hierarchical Classification**: Must support hierarchical classification structures

### Quality Assurance and Validation Standards
- **Accuracy Validation**: Must validate classification accuracy against known standards
- **Consistency Checks**: Must ensure consistent classification across similar files
- **Error Detection**: Must implement automated error detection and correction
- **Manual Review Integration**: Must support manual review and override capabilities

### Classification Categories and Standards
- **Source Code Files**: Must classify by programming language, framework, and purpose
- **Configuration Files**: Must identify configuration types, environments, and dependencies
- **Documentation Files**: Must categorize by type, audience, and content focus
- **Build and Deployment Files**: Must classify by build systems, deployment targets, and environments
- **Test Files**: Must categorize by test types, frameworks, and scope
- **Asset Files**: Must classify by asset types, usage patterns, and optimization requirements

### Integration and Reporting Requirements
- **Classification Database**: Must maintain comprehensive classification database
- **Reporting Standards**: Must generate standardized classification reports
- **Integration APIs**: Must provide APIs for integration with other development tools
- **Export Capabilities**: Must support export to various formats and systems

### Maintenance and Evolution Standards
- **Classification Rule Updates**: Must support updates to classification rules and criteria
- **Performance Monitoring**: Must monitor classification performance and accuracy
- **Feedback Integration**: Must integrate feedback for continuous improvement
- **Version Control**: Must maintain version control for classification rules and results

### Security and Compliance Requirements
- **Sensitive File Detection**: Must detect and flag sensitive files requiring special handling
- **Compliance Classification**: Must classify files based on compliance requirements
- **Access Control Integration**: Must integrate with access control systems
- **Audit Trail**: Must maintain audit trail of all classification activities

<output>
  <report>
    <summary>File classifier enforcement standards with comprehensive analysis and classification requirements</summary>
    <details>Covers file analysis, classification methodology, quality assurance, categorization standards, integration requirements, maintenance procedures, and security compliance</details>
    <checklist>
      <item checked="true">File type identification completed</item>
      <item checked="true">Content pattern analysis executed</item>
      <item checked="true">Multi-criteria classification applied</item>
      <item checked="true">Accuracy validation performed</item>
      <item checked="true">Consistency checks completed</item>
      <item checked="true">Classification database updated</item>
      <item checked="false">Manual review integration verified</item>
    </checklist>
  </report>
</output>

<security>
  <read_only_paths>
    <path>sunnycore/po/workflow/unified-file-classification-workflow.yaml</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="password|secret|key|token|api_key|confidential|private|credential" action="redact"/>
  </sensitive_filters>
  <access_control>
    <permission level="classifier" scope="file_classification"/>
  </access_control>
</security>

<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="mandatory_file_missing">
      <description>Required workflow file not accessible</description>
      <action>immediate_stop</action>
    </condition>
    <condition type="classification_accuracy_failure">
      <description>Classification accuracy falls below minimum threshold</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="analysis_completeness_failure">
      <description>File analysis incomplete or insufficient</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="sensitive_file_exposure">
      <description>Sensitive file detected without proper handling</description>
      <action>emergency_stop</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>EMERGENCY_STOP</status>
    <partial_results>File classification failed, manual intervention required</partial_results>
  </minimal_viable_output>
</fast_stop_mechanism>