# Architecture Documenter Enforcement Specification

## Core Execution Protocol

### Prerequisites (Flexible)
- **Recommendation**: Load unified workflow, templates, and source files before starting; if missing, record to validation_warnings and continue
- **Workflow Reading**: Should read `{project_root}/sunnycore/po/workflow/unified-architecture-documentation-workflow.yaml`, log warning on failure
- **Template Reading**: Should read `{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml`, log warning on failure
- **Source Reading**: Should read and scan specified source paths; if missing, log warning and continue with existing information

### Workflow Compliance (Mandatory Enforcement)
- **Stage Integrity**: Must execute all stages in the order defined by unified-architecture-documentation-workflow.yaml
- **Specification Collection**: Must synchronously load task.md, requirements.md, design.md
- **Plan Analysis**: Must extract architectural decisions and planning components
- **Codebase Scanning**: Must automatically discover interfaces, data models, API routes, infrastructure
- **Architecture Modeling**: Must establish system, container, component, and data flow models
- **Diagram Generation**: Must synchronously generate 5 core Mermaid architecture diagrams
- **Synchronization Validation**: Must validate documentation consistency with implementation (95% code link validity)
- **Output Validation**: Must ensure navigation links and architectural decision traceability

### Documentation Integrity (Mandatory Enforcement)
- **Structural Compliance**: Must follow the structure of `{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml`
- **Content Completeness**: All required sections must have actual content or be marked as "N/A - [reason]"
- **Placeholder Removal**: Must not contain unfilled `<placeholder>` values
- **Diagram Requirements**: Must include at least system context diagram, container diagram, component diagram

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

### Authenticity and Synchronization (Absolute Mandatory)
- **Code Consistency**: Architecture descriptions must be consistent with actual codebase
- **API Contract Synchronization**: API documentation must reflect actual interface implementations
- **Data Model Alignment**: Data models must align with actual database structure
- **Difference Annotation**: If inconsistencies exist, must clearly annotate differences and evolution plans

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

### Output Locations (Fixed)
- **Main Document**: `{{project_root}}/docs/architecture/architecture.md`
- **Diagrams Directory**: `{{project_root}}/docs/architecture/diagrams/`
- **ADR Directory**: `{{project_root}}/docs/architecture/decisions/`
- **Template Reference**: `{project_root}/sunnycore/po/templates/architecture-doc-tmpl.yaml`

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

## Quality Thresholds (Mandatory Pass)
- **Synchronization**: Architecture descriptions must be 100% consistent with actual implementation
- **Code Link Validity**: 95% of code links must be valid and accurate
- **API Contract Precision**: 100% exact match with actual API implementation
- **Data Model Consistency**: Structure must be synchronized with actual database
- **Component Interface Verification**: Public methods and dependencies must be verified correct
- **Infrastructure Configuration**: Configuration consistency must pass verification
- **Completeness**: All required components must have complete descriptions
- **Readability**: Documentation must be easily understandable by target audience
- **Maintainability**: Documentation must support long-term maintenance and updates

## Failure Handling Protocol (Record and Continue)
- **Missing Source Files**: Record missing sources and alternative information sources; continue with existing information processing
- **Code Synchronization Failure**: Record inconsistencies and synchronization plans; annotate differences and continue
- **Diagram Generation Failure**: Record failure reasons and manual supplementation plans; do not interrupt
- **Missing ADR Links**: Record missing links and supplementation plans; continue documentation compilation
- **Template Non-compliance**: Record differences and correction plans; do not interrupt output
