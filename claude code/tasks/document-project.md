<input>
  <context>
  1. Project documentation requirements and standards
  2. Existing project files and structure
  </context>
  <templates>
  1. {root}/sunnycore/templates/project-documentation-tmpl.yaml
  </templates>
</input>

<output>
1. {root}/docs/project-documentation.md - Comprehensive project documentation
</output>

<constraints, importance = "Important">
- Follow project documentation standards and templates
- Include all necessary sections for project understanding
- Use clear, concise language and proper formatting
</constraints>

<workflow, importance = "Normal">
  <stage id="1: analyze">
  - Review existing project structure and documentation
  - Identify documentation gaps and requirements
  - Plan documentation structure and content
  
  <questions>
  - What are the key project components that need documentation?
  - Are there existing documentation standards to follow?
  - What level of detail is appropriate for the target audience?
  </questions>
  </stage>

  <stage id="2: create">
  - Generate comprehensive project documentation
  - Follow template structure and formatting guidelines
  - Include all necessary sections and cross-references
  
  <checks>
  - [ ] All required sections are complete and accurate
  - [ ] Documentation follows established templates and standards
  - [ ] Cross-references and links are valid and functional
  - [ ] Content is clear, comprehensive, and well-organized
  </checks>
  </stage>
</workflow>


