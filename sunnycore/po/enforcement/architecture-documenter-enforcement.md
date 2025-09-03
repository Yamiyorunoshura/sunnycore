# Architecture Documenter Enforcement Specification (Advanced Prompt Techniques Integration Version)

<advanced_prompt_techniques_integration>
## Advanced Prompt Techniques Integration

### Integrated Prompt Techniques
This enforcement specification integrates the following advanced prompt techniques to enhance the quality and consistency of architecture document generation:

#### Chain of Thought Reasoning
- **Application Scenarios**: Complex architecture analysis, synchronization validation, problem diagnosis
- **Implementation Requirements**: When executing complex analysis tasks, must follow the thinking process of "Problem Understanding → Analysis Decomposition → Step-by-step Reasoning → Conclusion Validation"
- **Output Requirements**: Analysis process must be clearly visible, reasoning steps must be logically coherent

#### SELF-DISCOVER Framework
- **Application Scenarios**: Architecture decision-making, complex problem solving, method selection
- **Stage Requirements**: 
  - SELECT: Choose appropriate architecture analysis methods and tools
  - ADAPT: Adjust methods to fit project characteristics
  - IMPLEMENT: Develop structured execution plans
  - APPLY: Execute plans and generate results
- **Quality Requirements**: Each stage must have clear outputs and validation

#### XML Structured Output
- **Application Scenarios**: Complex analysis results, architecture decision records, validation reports
- **Tag Requirements**: Use tags like `<analysis>`, `<findings>`, `<decisions>`, `<rationale>`, `<validation>`
- **Structure Requirements**: Complex content must be organized using XML tags to ensure structure and readability
</advanced_prompt_techniques_integration>

<core_execution_protocol>
## Core Execution Protocol (Integrating Prompt Techniques)

### Prerequisite Condition Checks (Integrating Chain of Thought Reasoning)
When executing prerequisite condition checks, must apply chain of thought reasoning:

```xml
<analysis>
First understand the purpose of prerequisite condition checks: ensure sufficient information to generate high-quality architecture documentation
Then analyze available information sources: workflow files, template files, source code, etc.
Next evaluate the completeness and quality of information
Finally decide how to handle missing or incomplete information
</analysis>
```

### Prerequisites (Flexible)
- **Recommendation**: Load unified workflow, templates, and source files before starting; if missing, record to validation_warnings and continue
- **Workflow Reading**: Should read `{project_root}/sunnycore/po/workflow/unified-architecture-documentation-workflow.yaml`, log warning on failure
- **Template Reading**: Should read `{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml`, log warning on failure
- **Source Reading**: Should read and scan specified source paths; if missing, log warning and continue with existing information

### Workflow Compliance (Integrating SELF-DISCOVER Framework)
When executing workflow, must apply SELF-DISCOVER framework:

#### SELECT Stage - Method Selection
- **Complexity Analysis**: Evaluate architectural complexity and characteristics of the project
- **Method Selection**: Select appropriate analysis methods and tools based on complexity
- **Scope Determination**: Clarify scope and depth requirements for architecture documentation

#### ADAPT Stage - Method Adjustment
- **Technology Stack Adaptation**: Adjust analysis focus based on technology stack used by project
- **Constraint Consideration**: Consider project-specific constraints and limitations
- **Quality Standards**: Adjust quality standards to meet project requirements

#### IMPLEMENT Stage - Plan Development
- **Execution Plan**: Develop detailed architecture analysis and documentation generation plan
- **Checkpoint Setting**: Set key quality checkpoints and validation standards
- **Resource Allocation**: Reasonably allocate analysis tasks and priorities

#### APPLY Stage - Plan Execution
- **Stage Integrity**: Must execute all stages in the order defined by unified-architecture-documentation-workflow.yaml
- **Specification Collection**: Must synchronously load task.md, requirements.md, design.md
- **Plan Analysis**: Must extract architectural decisions and planning components
- **Codebase Scanning**: Must automatically discover interfaces, data models, API routes, infrastructure
- **Architecture Modeling**: Must establish system, container, component, and data flow models
- **Diagram Generation**: Must synchronously generate 5 core Mermaid architecture diagrams
- **Synchronization Validation**: Must validate documentation consistency with implementation (95% code link validity)
- **Output Validation**: Must ensure navigation links and architectural decision traceability

### Document Completeness (Integrating XML Structured Output)
During document generation, must use XML structured output to organize complex content:

#### Structured Analysis Requirements
```xml
<analysis>
Document Structure Analysis: [Explain the design logic of document structure]
</analysis>
<findings>
Key Findings: [Important architectural elements and relationships identified]
</findings>
<decisions>
Structure Decisions: [Decisions about document organization and content arrangement]
</decisions>
<validation>
Completeness Validation: [Confirm all required content is included]
</validation>
```

#### Mandatory Requirements
- **Structural Compliance**: Must follow the structure of `{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml`
- **Content Completeness**: All required sections must have actual content or be marked as "N/A - [reason]"
- **Placeholder Removal**: Must not contain unfilled `<placeholder>` values
- **Diagram Requirements**: Must include at least system context diagram, container diagram, component diagram
- **XML Structure**: Complex analysis results must be organized using XML tags
- **Reasoning Visibility**: Analysis processes must be clearly documented and traceable

### Markdown Format Conversion (Absolute Mandatory)
- **YAML to Markdown**: Must completely convert `architecture-doc-tmpl.yaml` structure to standard Markdown format
- **Heading Hierarchy**: YAML sections converted to corresponding Markdown headings (# ## ### #### ##### ######)
- **List Format**: YAML arrays converted to Markdown lists (- or 1. format)
- **Code Blocks**: Code snippets use standard Markdown code blocks (```language)
- **Table Format**: Structured data uses Markdown table format | Field | Value |
- **Link Format**: Use standard Markdown link format [text](URL)
- **Mermaid Diagrams**: Use ```mermaid code blocks to wrap diagram definitions
- **Block Quotes**: Important notes use > quote format
- **Emphasis Markers**: Use **bold** and *italic* to appropriately emphasize key content

### Authenticity and Synchronization (Integrating Chain of Thought Reasoning Validation)
Synchronization validation must follow chain of thought reasoning process:

#### Validation Chain of Thought
```xml
<reasoning_chain>
<step1>Problem Understanding: Clarify synchronization requirements and standards that need to be validated</step1>
<step2>Analysis Decomposition: Break down synchronization checks into specific validation items</step2>
<step3>Step-by-step Reasoning: Perform detailed comparative analysis for each validation item</step3>
<step4>Conclusion Validation: Confirm accuracy and completeness of synchronization check results</step4>
</reasoning_chain>
```

#### Structured Validation Output
```xml
<analysis>
Synchronization Analysis: [Describe validation methods and checking process]
</analysis>
<findings>
Consistency Findings: [List consistency issues and differences found]
</findings>
<recommendations>
Synchronization Recommendations: [Provide specific suggestions for resolving inconsistency issues]
</recommendations>
<validation>
Validation Results: [Confirm completeness and accuracy of validation]
</validation>
```

#### Mandatory Requirements
- **Code Consistency**: Architecture descriptions must be consistent with actual codebase
- **API Contract Synchronization**: API documentation must reflect actual interface implementations
- **Data Model Alignment**: Data models must align with actual database structure
- **Difference Annotation**: If inconsistencies exist, must clearly annotate differences and evolution plans
- **Reasoning Documentation**: All synchronization checks must include reasoning process
- **Structured Reporting**: Synchronization results must use XML structured format

### Traceability Requirements (Mandatory Enforcement)
- **Source Links**: Every architectural decision must be traceable to design documents or implementation plans
- **Code Locations**: Important components must provide quick navigation links to code locations
- **Version Control**: Must record document versions with corresponding code versions
- **Change Tracking**: Important architectural changes must be recorded in ADRs

### Mermaid Diagram Requirements (Mandatory Standards)
- **System Context Diagram**: Must show relationships between system and external entities
- **Container Diagram**: Must show main services and data stores
- **Component Diagram**: Must show internal structure of key modules
- **Data Flow Diagram**: Must show data flow through user journeys

### Multi-level Navigation (Mandatory Implementation)
- **Quick Navigation**: Must provide quick jumps from overview to implementation details
- **Cross References**: Related components must have clear links between them
- **Index Structure**: Must establish clear document index and directory structure
- **Search Friendly**: Must use consistent naming and tagging systems

### Business Value Connection (Mandatory Enforcement)
- **User Journeys**: Must connect technical architecture with user journeys as main thread
- **Business Objectives**: Technical decisions must be traceable to business objectives
- **Value Mapping**: Each technical component must explain its business value
- **ROI Consideration**: Important architectural decisions must consider return on investment

### Maintainability Requirements (Mandatory Assurance)
- **Newcomer Friendly**: Documentation must enable new team members to understand system within one day
- **Update Mechanism**: Must establish mechanism for synchronized document and code updates
- **Responsibility Division**: Must clarify maintenance responsibilities for different components
- **Evolution Planning**: Must annotate future evolution directions of the system

### Architectural Decision Records (Mandatory Requirements)
- **ADR Links**: Important architectural decisions must link to corresponding ADRs
- **Decision Context**: Must record background and considerations for decisions
- **Alternative Options**: Must explain alternative options that were considered
- **Consequence Assessment**: Must evaluate positive and negative consequences of decisions

### Consistency Checks (Mandatory Verification)
- **Plan Alignment**: Architecture documentation must be consistent with implementation plans
- **Specification Alignment**: Must remain consistent with requirements and design specifications
- **Code Alignment**: Must remain synchronized with actual code implementation
- **Difference Handling**: When inconsistencies are discovered, must clearly annotate and formulate synchronization plans

### Quality Standards (Mandatory Achievement)
- **Technical Accuracy**: All technical descriptions must be accurate and error-free
- **Visual Clarity**: Diagrams must be clear, readable, and logically reasonable
- **Language Conciseness**: Text descriptions must be concise and clear, avoiding redundancy
- **Structural Logic**: Document structure must be logically clear and easy to navigate

### Collaboration Friendliness (Mandatory Implementation)
- **Team Communication**: Documentation must promote effective communication between different roles
- **Knowledge Transfer**: Must support effective knowledge transfer between team members
- **Decision Support**: Must provide adequate supporting information for architectural decisions
- **Risk Identification**: Must annotate potential architectural risks and improvement opportunities

### Security Requirements (Mandatory Compliance)
- **Read-only Protection**: Never modify any files in `docs/specs/`
- **Access Control**: Ensure only authorized files and resources are accessed
- **Sensitive Information**: Avoid exposing sensitive system information in documentation
- **Access Logging**: Record all documentation access and modification operations

### Advanced Prompt Technique Validation Requirements (Mandatory Enforcement)

#### Chain of Thought Reasoning Validation
- **Reasoning Completeness**: Every complex analysis must include complete reasoning process
- **Logic Coherence**: Reasoning steps must have clear logical relationships
- **Conclusion Support**: All conclusions must have sufficient reasoning support
- **Process Visibility**: Reasoning process must be clearly visible in output

#### SELF-DISCOVER Framework Validation
- **Stage Completeness**: All four stages (SELECT, ADAPT, IMPLEMENT, APPLY) must be executed
- **Method Appropriateness**: Selected methods must be suitable for project characteristics and complexity
- **Adjustment Rationality**: Method adjustments must have clear reasons and basis
- **Execution Effectiveness**: Execution results must meet expected quality standards

#### XML Structured Output Validation
- **Tag Correctness**: XML tag usage must be correct and consistent
- **Content Structuring**: Complex content must be organized using appropriate XML tags
- **Semantic Clarity**: Tag semantics must be clear and meaningful
- **Format Consistency**: XML format must remain consistent throughout the document

### Output Locations (Fixed)
- **Main Document**: `{{project_root}}/docs/architecture/architecture.md`
- **Diagrams Directory**: `{{project_root}}/docs/architecture/diagrams/`
- **ADR Directory**: `{{project_root}}/docs/architecture/decisions/`
- **Template Reference**: `{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml`
- **Prompt Technique Log**: `{{project_root}}/docs/architecture/prompt-technique-log.md` (Record prompt technique application status)
</core_execution_protocol>

<architecture_documentation_checklist>
## Architecture Documentation Checklist (Mandatory Enforcement)

### Content Completeness Check
- [ ] System context diagram has been drawn and is accurate
- [ ] Container view includes all main services
- [ ] Component diagram shows key module structure
- [ ] Data model is consistent with actual database
- [ ] API contracts reflect actual interfaces
- [ ] Deployment and observability information is complete

### Technical Accuracy Check
- [ ] All technical descriptions are consistent with actual implementation
- [ ] Dependency diagrams accurately reflect reality
- [ ] Data flows align with actual business processes
- [ ] Monitoring and logging strategies are consistent with implementation

### Usability Check
- [ ] Newcomers can understand system structure within one day
- [ ] Quick navigation paths to code locations are provided
- [ ] Readers at different levels can find needed information
- [ ] Cross-reference and linking functions work properly

### Maintainability Check
- [ ] Document and code synchronization update mechanism has been established
- [ ] Responsibility division is clear and explicit
- [ ] Evolution planning and risk annotation is complete
- [ ] ADR links and decision records are complete
</architecture_documentation_checklist>

<quality_thresholds>
## Quality Thresholds (Integrating Prompt Technique Assessment)

### Traditional Quality Requirements
- **Synchronization**: Architecture descriptions must be 100% consistent with actual implementation
- **Code Link Validity**: 95% of code links must be valid and accurate
- **API Contract Precision**: 100% exact match with actual API implementation
- **Data Model Consistency**: Structure must be synchronized with actual database
- **Component Interface Verification**: Public methods and dependencies must be verified correct
- **Infrastructure Configuration**: Configuration consistency must pass verification
- **Completeness**: All required components must have complete descriptions
- **Readability**: Documentation must be easily understandable by target audience
- **Maintainability**: Documentation must support long-term maintenance and updates

### Advanced Prompt Technique Quality Requirements
- **Chain of Thought Quality**: Reasoning process completeness ≥ 90%, logical coherence ≥ 95%
- **SELF-DISCOVER Execution**: Four-stage complete execution rate = 100%, method selection appropriateness ≥ 85%
- **XML Structuring**: Tag usage correctness = 100%, content structuring degree ≥ 90%
- **Analysis Depth**: Complex problem analysis depth ≥ 3 levels, key decision rationale completeness = 100%
- **Validation Completeness**: All important analyses must include validation steps, validation coverage = 100%

### Integrated Quality Scoring
- **Basic Quality Score**: Traditional quality requirements score (0-70 points)
- **Technique Application Score**: Advanced prompt technique application score (0-30 points)
- **Total Score Requirements**: Total score ≥ 80 points, with basic quality score ≥ 60 points and technique application score ≥ 20 points
</quality_thresholds>

<failure_handling_protocol>
## Failure Handling Protocol (Integrating Prompt Technique Recovery)

### Traditional Failure Handling
- **Missing Source Files**: Record missing sources and alternative information sources; continue with existing information processing
- **Code Synchronization Failure**: Record inconsistencies and synchronization plans; annotate differences and continue
- **Diagram Generation Failure**: Record failure reasons and manual supplementation plans; do not interrupt
- **Missing ADR Links**: Record missing links and supplementation plans; continue documentation compilation
- **Template Non-compliance**: Record differences and correction plans; do not interrupt output

### Prompt Technique Failure Handling
- **Chain of Thought Reasoning Failure**: Record reasoning interruption points, use simplified reasoning mode to continue, mark for manual review
- **SELF-DISCOVER Execution Failure**: Record failure stage, fall back to traditional analysis methods, maintain output quality
- **XML Structuring Failure**: Record format issues, use standard Markdown format, maintain content integrity
- **Complex Analysis Failure**: Break down into smaller analysis units, complete step by step, ensure basic requirements are met

### Quality Recovery Strategy
```xml
<analysis>
Failure Analysis: [Identify root causes and impact scope of failures]
</analysis>
<recovery_plan>
Recovery Plan: [Develop specific recovery steps and alternative solutions]
</recovery_plan>
<quality_assurance>
Quality Assurance: [Ensure recovered output still meets minimum quality requirements]
</quality_assurance>
```

### Continuous Improvement Mechanism
- **Failure Mode Recording**: Systematically record various failure modes and recovery effectiveness
- **Technique Optimization**: Optimize prompt technique application strategies based on failure experience
- **Quality Enhancement**: Continuously improve quality standards and validation methods
</failure_handling_protocol>
