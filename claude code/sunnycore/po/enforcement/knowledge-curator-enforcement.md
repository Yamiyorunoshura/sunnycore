# Knowledge Curator Enforcement Standards

<specification_metadata>
name: "Knowledge Curator Enforcement Standards"
version: "2.0.0"
category: "knowledge_curation_enforcement"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## Core Execution Protocol

<prerequisites>
<file path="sunnycore/po/workflow/unified-knowledge-curation-workflow.yaml" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
<file path="sunnycore/po/templates/knowledge-lessons-tmpl.yaml" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
</prerequisites>

<determinism temperature="0" top_p="0" top_k="1" seed="42" stable_sort="true"/>

<workflow>
  <stage id="S1" name="knowledge_extraction_analysis" optional="false" parallel="forbidden">
    <inputs>
      <source path="sunnycore/po/workflow/unified-knowledge-curation-workflow.yaml" required="true"/>
      <source path="review_reports_directory" required="true"/>
      <source path="completion_reports_directory" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Extract and analyze knowledge from project artifacts, reports, and documentation</select>
        <adapt>Adapt knowledge extraction methods based on content types and knowledge domains</adapt>
        <implement>Execute comprehensive knowledge analysis with pattern recognition and categorization</implement>
        <apply>Generate structured knowledge artifacts with validation and quality assurance</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="knowledge_extraction_completeness">
        <criteria>All available knowledge sources must be analyzed and processed</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
  
  <stage id="S2" name="knowledge_synthesis_curation" optional="false" parallel="forbidden">
    <inputs>
      <source path="sunnycore/po/templates/knowledge-lessons-tmpl.yaml" required="true"/>
      <source path="extracted_knowledge_artifacts" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Synthesize extracted knowledge into structured lessons learned and best practices</select>
        <adapt>Adapt synthesis approach based on knowledge complexity and organizational requirements</adapt>
        <implement>Execute comprehensive knowledge curation with validation and peer review integration</implement>
        <apply>Generate final knowledge repository with access controls and distribution mechanisms</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="knowledge_synthesis_quality">
        <criteria>Synthesized knowledge must meet quality and relevance standards</criteria>
        <threshold>95%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
      <gate name="accessibility_validation">
        <criteria>Knowledge artifacts must be accessible and usable by target audiences</criteria>
        <threshold>90%</threshold>
        <failure_action>record_warning_continue</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>

## Knowledge Curation Mandatory Requirements

<reasoning>
  <analysis>Knowledge curation requires systematic extraction, analysis, synthesis, and organization of organizational knowledge from various sources</analysis>
  <findings>Critical areas include knowledge extraction, pattern recognition, synthesis methodology, quality validation, accessibility, and distribution mechanisms</findings>
  <decisions>Implement comprehensive knowledge curation framework with automated validation and structured organization</decisions>
  <rationale>Effective knowledge curation ensures organizational learning, knowledge retention, and continuous improvement</rationale>
  <validation>All requirements validated against knowledge management best practices and organizational learning frameworks</validation>
</reasoning>

### Knowledge Extraction Standards (Mandatory Requirements)
- **Source Identification**: Must identify and catalog all available knowledge sources
- **Content Analysis**: Must analyze content for extractable knowledge patterns and insights
- **Pattern Recognition**: Must implement pattern recognition for identifying recurring themes and lessons
- **Context Preservation**: Must preserve context and applicability information for extracted knowledge

### Knowledge Classification and Organization
- **Taxonomy Development**: Must develop and maintain knowledge taxonomy and classification systems
- **Categorization Standards**: Must categorize knowledge by domain, complexity, and applicability
- **Relationship Mapping**: Must map relationships between knowledge items and concepts
- **Hierarchical Organization**: Must organize knowledge in hierarchical structures for easy navigation

### Quality Assurance and Validation Standards
- **Accuracy Validation**: Must validate accuracy and relevance of extracted knowledge
- **Currency Assessment**: Must assess currency and timeliness of knowledge items
- **Peer Review Integration**: Must integrate peer review processes for knowledge validation
- **Bias Detection**: Must implement bias detection and mitigation in knowledge curation

### Synthesis and Integration Requirements
- **Knowledge Synthesis**: Must synthesize related knowledge items into comprehensive insights
- **Best Practice Identification**: Must identify and document best practices and successful approaches
- **Lessons Learned**: Must extract and document lessons learned from project experiences
- **Anti-Pattern Documentation**: Must document anti-patterns and approaches to avoid

### Accessibility and Usability Standards
- **User-Centric Design**: Must design knowledge repositories with user needs in mind
- **Search and Discovery**: Must implement effective search and discovery mechanisms
- **Multiple Format Support**: Must support multiple knowledge formats and presentation styles
- **Progressive Disclosure**: Must implement progressive disclosure for complex knowledge items

### Distribution and Communication Requirements
- **Distribution Channels**: Must establish appropriate distribution channels for different knowledge types
- **Audience Targeting**: Must target knowledge distribution to appropriate audiences
- **Communication Standards**: Must establish communication standards for knowledge sharing
- **Feedback Integration**: Must integrate feedback mechanisms for continuous improvement

### Maintenance and Evolution Standards
- **Knowledge Updates**: Must establish procedures for updating and maintaining knowledge items
- **Version Control**: Must maintain version control for knowledge artifacts
- **Archival Procedures**: Must establish archival procedures for outdated knowledge
- **Performance Monitoring**: Must monitor knowledge repository usage and effectiveness

### Integration and Collaboration Requirements
- **System Integration**: Must integrate with existing organizational systems and processes
- **Collaboration Tools**: Must provide collaboration tools for knowledge development and review
- **Expert Networks**: Must facilitate connections with subject matter experts
- **Community Building**: Must support knowledge sharing communities and practices

<output>
  <report>
    <summary>Knowledge curator enforcement standards with comprehensive extraction, synthesis, and curation requirements</summary>
    <details>Covers knowledge extraction, classification, quality assurance, synthesis, accessibility, distribution, maintenance, and collaboration requirements</details>
    <checklist>
      <item checked="true">Knowledge sources identified and analyzed</item>
      <item checked="true">Pattern recognition and extraction completed</item>
      <item checked="true">Knowledge classification and organization established</item>
      <item checked="true">Quality validation and peer review integrated</item>
      <item checked="true">Synthesis and best practices documentation completed</item>
      <item checked="false">Distribution mechanisms activated</item>
      <item checked="false">Community feedback integration verified</item>
    </checklist>
  </report>
</output>

<security>
  <read_only_paths>
    <path>sunnycore/po/workflow/unified-knowledge-curation-workflow.yaml</path>
    <path>sunnycore/po/templates/knowledge-lessons-tmpl.yaml</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="password|secret|key|token|api_key|confidential|proprietary|classified" action="redact"/>
  </sensitive_filters>
  <access_control>
    <permission level="curator" scope="knowledge_curation"/>
  </access_control>
</security>

<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="knowledge_extraction_failure">
      <description>Critical failure in knowledge extraction from available sources</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="quality_validation_failure">
      <description>Knowledge quality validation fails to meet minimum standards</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="synthesis_completeness_failure">
      <description>Knowledge synthesis incomplete or insufficient</description>
      <action>emergency_stop</action>
    </condition>
    <condition type="accessibility_critical_failure">
      <description>Knowledge accessibility requirements not met for critical audiences</description>
      <action>record_warning_continue</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>EMERGENCY_STOP</status>
    <partial_results>Knowledge curation failed, extraction or synthesis must be corrected</partial_results>
  </minimal_viable_output>
</fast_stop_mechanism>