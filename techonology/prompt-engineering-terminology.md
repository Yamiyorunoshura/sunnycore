# Prompt Engineering Terminology Standards

## Document Overview
This document defines the standardized English terminology and patterns used in our AI agent prompt engineering system. It serves as the authoritative reference for creating consistent, professional, and effective prompts across all agent definitions.

## Core Framework Components

### 1. Reasoning Methodologies

#### SELF-DISCOVER Framework
- **SELECT**: Analyze task complexity and select appropriate methods
- **ADAPT**: Adjust methods to fit specific project characteristics  
- **IMPLEMENT**: Establish structured execution plans
- **APPLY**: Execute plans with continuous validation

#### Cognitive Techniques
- **Chain of Thought Reasoning**: Step-by-step logical reasoning process
- **First Principles Thinking**: Breaking down complex problems to fundamental truths
- **Structured Output**: Using XML tags to organize complex analysis
- **Pre-cognitive Technique**: Thinking before responding with standard openings

### 2. Agent Architecture Standards

#### YAML Front Matter Structure
```yaml
name: agent-identifier
description: Brief description of agent's primary function
model: inherit
color: [blue|green|orange|purple|red|yellow|teal]
prompt_techniques: ["chain_of_thought", "self_discover", "xml_structured"]
version: 1.0
last_updated: YYYY-MM-DD
```

#### Core Sections Template
1. **`<role>`** - Core identity and reasoning methodology
2. **`<personality_traits>`** - Professional background and work philosophy
3. **`<startup_sequence>`** - SELF-DISCOVER integrated initialization
4. **`<prompt_techniques>`** - Advanced prompt engineering methods
5. **`<technical_expertise>`** - Domain-specific skills and tools
6. **`<success_metrics>`** - Quality standards and success indicators
7. **`<core_responsibilities>`** - Primary duties and collaboration scope

### 3. Professional Role Classifications

#### Developer Categories
- **Backend Developer**: Server-side logic, databases, APIs, infrastructure
- **Frontend Developer**: Client-side interfaces, user experience, performance
- **Fullstack Developer**: End-to-end system architecture and integration
- **Refactor Developer**: Code quality improvement and optimization

#### Specialization Areas
- **API Development**: RESTful APIs, GraphQL, interface design
- **Database Management**: Data modeling, query optimization, performance
- **Infrastructure**: Cloud architecture, DevOps, containerization
- **Performance Optimization**: Resource management, scalability, monitoring
- **Security**: Vulnerability assessment, authentication, data protection
- **Testing**: Test strategy, automation, quality assurance
- **UI/UX Design**: User interface, accessibility, interaction design
- **Architecture**: System design, technology selection, integration

#### Management and Quality Roles
- **Task Planner**: Project planning, requirement analysis, execution strategy
- **Project Concluder**: Delivery assessment, value realization, reporting
- **Knowledge Curator**: Best practices documentation, lessons learned
- **Task Reviewers**: Quality assessment across specialized domains

### 4. Technical Terminology Standards

#### Prompt Engineering Terms
- **Prompt Chaining**: Multi-round conversation optimization
- **XML Structured Output**: Organized analysis using semantic tags
- **Evidence-Based Assessment**: Conclusions supported by specific examples
- **Template-Driven Generation**: Using standardized formats and structures
- **Iterative Refinement**: Continuous improvement through feedback loops

#### Quality Assessment Framework
- **Bronze Level**: Basic delivery standards
- **Silver Level**: Mature delivery standards  
- **Gold Level**: Excellent delivery standards
- **Platinum Level**: Outstanding delivery standards

#### Work Mode Patterns
- **Analysis Phase**: `<analysis>` - Problem understanding and requirement gathering
- **Design Phase**: `<design>/<solution>/<plan>` - Strategy formulation and planning
- **Implementation Phase**: `<implementation>` - Execution steps and technical details
- **Validation Phase**: `<validation>` - Testing, verification, and quality assurance

### 5. Emergency and Safety Protocols

#### Emergency Stop Mechanism
```
**Trigger Conditions**: Tool call failures, missing files, permission issues
**Action Rules**: Immediate termination with fixed message
**Fixed Message**: "Emergency Stop: Tool/file retrieval failure detected, response stopped for consistency. Please correct and retry."
**Reason Codes**: [TOOL_FAILURE | MISSING_REQUIRED_FILE | EMPTY_CONTENT | PERMISSION_DENIED | PATH_UNAVAILABLE | INVALID_SCHEMA]
```

### 6. Collaboration Frameworks

#### Team Integration Patterns
- **Horizontal Collaboration**: Same-level expert coordination
- **Vertical Integration**: Cross-level project management
- **Specialized Consultation**: Domain-specific expertise sharing
- **Quality Assurance Chain**: Multi-reviewer validation process

#### Communication Standards
- **Professional Greeting**: Role introduction with experience background
- **Evidence Requirements**: Specific examples, file references, line numbers
- **Recommendation Format**: Prioritized, actionable improvement suggestions
- **Status Reporting**: Clear progress indicators and completion criteria

### 7. Assessment and Metrics

#### Success Indicators
- **Completion Rate**: Percentage of requirements fully satisfied
- **Quality Score**: Multi-dimensional assessment rating
- **Time Efficiency**: Delivery speed relative to complexity
- **Stakeholder Satisfaction**: User and client approval ratings

#### Quality Dimensions
- **Completeness**: All required components present and functional
- **Accuracy**: Technical correctness and requirement alignment
- **Maintainability**: Long-term sustainability and extensibility
- **Performance**: Resource efficiency and response optimization
- **Security**: Protection against threats and vulnerabilities
- **Usability**: User experience and accessibility standards

### 8. Documentation Standards

#### Content Organization
- **Hierarchical Structure**: Logical information architecture
- **Cross-References**: Linked related concepts and dependencies
- **Examples and Evidence**: Concrete illustrations and proof points
- **Actionable Guidance**: Clear implementation instructions

#### Language and Style
- **Professional Tone**: Formal, respectful, expert-level communication
- **Technical Precision**: Accurate terminology and specific details
- **Cultural Sensitivity**: Inclusive language and diverse perspectives
- **Clarity Priority**: Simple, direct expression over complex phrasing

## Implementation Guidelines

### For Agent Creators
1. Follow the YAML front matter structure exactly
2. Implement all core sections with appropriate content
3. Use standardized terminology throughout
4. Include emergency stop mechanisms
5. Define clear success metrics and quality standards

### For Agent Users
1. Understand the SELF-DISCOVER framework phases
2. Provide specific requirements and constraints
3. Expect structured, evidence-based responses
4. Allow for iterative refinement and feedback loops
5. Respect emergency stop protocols when triggered

### For System Maintainers
1. Regularly update terminology standards
2. Ensure consistency across all agent definitions
3. Monitor effectiveness and user satisfaction
4. Incorporate feedback and lessons learned
5. Maintain version control and change documentation

## Conclusion

This terminology standard ensures consistency, professionalism, and effectiveness across our AI agent ecosystem. By following these guidelines, we create reliable, maintainable, and high-quality prompt engineering solutions that deliver real value to users and stakeholders.

**Version**: 1.0  
**Last Updated**: 2025-01-15  
**Next Review**: 2025-07-15
