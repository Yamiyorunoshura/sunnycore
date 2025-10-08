**GOAL**: Validate design consistency and alignment across project documents, ensuring no fabricated content, conflicts, or missing mappings.

## [Input]
  1. {workflow} parameter (required) - Validation workflow type: "prd" or "full"
  2. (If workflow=prd) "{PRD}" --Product Requirements Document
  3. (If workflow=prd) (Optional) "{ARCH}/*.md" --Existing architecture (for alignment check)
  4. (If workflow=full) "{REQ}/*.md" --Requirements documents
  5. (If workflow=full) "{ARCH}/*.md" --Architecture documents
  6. (If workflow=full) "{EPIC}" --Epic task list
  7. (If workflow=full) "{PLAN}/*.md" --Implementation plans

## [Output]
  1. "{root}/docs/design-validation.md" --Comprehensive validation report

## [Constraints]
  1. Must support two workflows: "prd" and "full"
  2. Must perform bidirectional validation (forward and backward references)
  3. Must detect fabricated content (references to non-existent requirements, components, or files)
  4. Must identify conflicts and inconsistencies across documents
  5. Must calculate coverage metrics for completeness analysis
  6. Must categorize issues by severity: Critical, High, Medium, Low
  7. Must provide actionable recommendations for each issue

## [Tools]
  1. **todo_write**
    - [Step 1: Create todo list; Steps 2-5: Track validation progress]
  2. **sequentialthinking (MCP)**
    - [Step 1: Analyze workflow and scope; Step 2-4: Reason about validation logic and issue prioritization]
  3. **claude-context (MCP)**
    - [Step 2: Search codebase for referenced components to verify existence]

## [Steps]
  1. Initialization Phase
    - Read all workflow steps to understand expected work
    - Validate workflow parameter (must be "prd" or "full")
    - if workflow == "prd" then proceed to 1.1, else proceed to 1.2
      
      1.1. PRD Workflow Initialization
        - Verify "{PRD}" exists and is readable
        - Check if "{ARCH}/" directory exists for alignment validation
        - Create todo list for PRD validation tasks
      
      1.2. Full Workflow Initialization
        - Verify all required directories and files exist
        - Index all requirements, architecture, epic, and plan files
        - Create todo list for full validation tasks

  2. Content Extraction and Indexing Phase
    - if workflow == "prd" then proceed to 2.1, else proceed to 2.2
      
      2.1. Extract PRD Content
        - Parse PRD structure and extract:
          - All requirement IDs and descriptions
          - All architecture components and technical stack
          - All tasks and their details
        - Build internal index of PRD entities
        - If existing architecture exists, parse and index architecture components
      
      2.2. Extract Full Workflow Content
        - Parse all requirements files and extract requirement IDs
        - Parse all architecture files and extract components, modules, interfaces
        - Parse epic and extract all task IDs and descriptions
        - Parse all implementation plans and extract referenced requirements/components
        - Build comprehensive internal index of all entities

  3. Validation Phase
    - if workflow == "prd" then proceed to 3.1, else proceed to 3.2
      
      3.1. PRD Validation
        - 3.1.1. Internal Consistency Check
          - Verify all requirements referenced in architecture section actually exist in requirements section
          - Verify all architecture components referenced in tasks actually exist in architecture section
          - Verify all tasks reference valid requirements and architecture components
          - Check for circular dependencies or logical conflicts
        
        - 3.1.2. Terminology and Naming Consistency
          - Identify all technical terms, component names, API names across PRD
          - Flag inconsistent naming (e.g., "UserService" vs "User Service" vs "userService")
          - Verify interface definitions are consistent across sections
        
        - 3.1.3. Coverage Analysis
          - Check if all requirements map to at least one architecture component
          - Check if all architecture components map to at least one task
          - Identify orphaned requirements, components, or tasks
        
        - 3.1.4. Alignment with Existing Architecture (if applicable)
          - Compare PRD architecture against existing architecture documents
          - Identify breaking changes to existing contracts (APIs, data models, events)
          - Verify integration points are correctly referenced
          - Flag potential conflicts with existing system
        
        - 3.1.5. Content Authenticity Check
          - Verify all file paths, module names, and external references are concrete (not placeholders)
          - Flag vague or unverifiable statements
          - Ensure all technical specifications are precise and measurable
      
      3.2. Full Workflow Validation
        - 3.2.1. Bidirectional Reference Validation
          - Forward: Requirements → Architecture → Epic → Plans
            - Verify each requirement is referenced by at least one architecture component
            - Verify each architecture component is referenced by at least one task
            - Verify each task has a corresponding implementation plan
          - Backward: Plans → Epic → Architecture → Requirements
            - Verify all requirements referenced in plans exist in requirements files
            - Verify all architecture components referenced in plans exist in architecture files
            - Verify all tasks in plans exist in epic
        
        - 3.2.2. Completeness and Coverage
          - Calculate requirement coverage: % of requirements mapped to architecture
          - Calculate architecture coverage: % of components mapped to tasks
          - Calculate task coverage: % of tasks with implementation plans
          - Identify gaps and orphaned entities
        
        - 3.2.3. Consistency Across Documents
          - Compare terminology and naming across all documents
          - Verify interface definitions are identical across documents
          - Check data model consistency (field names, types, constraints)
          - Validate technical stack consistency
        
        - 3.2.4. Conflict Detection
          - Identify contradictory requirements
          - Detect conflicting architecture decisions
          - Find duplicate or overlapping tasks
          - Flag incompatible technical specifications
        
        - 3.2.5. Content Authenticity Check
          - Verify all referenced entities actually exist
          - Flag fabricated requirement IDs, component names, or file paths
          - Ensure all cross-references are valid and resolvable
          - Validate that implementation plans reference actual requirements and architecture

  4. Report Generation Phase
    - Categorize all issues by severity:
      - Critical: Fabricated content, broken references, major conflicts
      - High: Missing mappings, inconsistent naming, coverage gaps
      - Medium: Terminology inconsistencies, minor conflicts
      - Low: Recommendations for improvement
    
    - Structure the report:
      - Executive Summary (overall status, critical issues count)
      - Validation Scope (workflow type, files analyzed)
      - Coverage Metrics (percentages and statistics)
      - Issues by Category (grouped by severity)
      - Detailed Findings (with file references and line numbers if available)
      - Actionable Recommendations (prioritized fix list)
    
    - Generate report to "{root}/docs/design-validation.md"

  5. Finalization Phase
    - Present validation summary to user
    - if critical or high severity issues found then proceed to 5.1, else proceed to 5.2
      
      5.1. Issues Found
        - Recommend running `/sunnycore_po *fix-design-conflicts` to address issues
        - Highlight top 3-5 critical issues requiring immediate attention
      
      5.2. No Major Issues
        - Confirm design is validated and consistent
        - Provide quality score or confidence level

## [Validation-Criteria]

### PRD Workflow Checks:
  1. **Internal Consistency**
    - All internal references are valid
    - No circular dependencies
    - Requirements-Architecture-Tasks alignment
  
  2. **External Alignment** (if existing architecture exists)
    - No breaking changes to public contracts
    - Integration points correctly referenced
    - Compatible with existing technical stack
  
  3. **Completeness**
    - All requirements have architecture mapping
    - All architecture components have task mapping
    - No orphaned entities

### Full Workflow Checks:
  1. **Bidirectional Integrity**
    - Forward references are complete
    - Backward references are valid
    - No broken links between documents
  
  2. **Coverage Metrics**
    - Requirement → Architecture: 100%
    - Architecture → Tasks: 100%
    - Tasks → Plans: 100%
  
  3. **Consistency**
    - Terminology is uniform
    - Technical specifications match
    - No contradictory statements
  
  4. **Authenticity**
    - All references exist
    - No fabricated content
    - All entities are concrete and verifiable

## [Error-Handling]
  1. Invalid workflow parameter: Report error and list valid options ("prd" or "full")
  2. Missing required files: List missing files and cannot proceed
  3. Parse errors: Document which files failed to parse and continue with available data
  4. No issues found: Generate clean report confirming validation passed

## [DoD]
  - [ ] Workflow parameter has been validated
  - [ ] All required documents have been read and indexed
  - [ ] Bidirectional reference validation is complete
  - [ ] Coverage analysis is complete with metrics calculated
  - [ ] Consistency checks across documents are complete
  - [ ] Content authenticity verification is complete
  - [ ] Conflict detection is complete
  - [ ] All issues are categorized by severity
  - [ ] Validation report has been generated to "{root}/docs/design-validation.md"
  - [ ] User has been informed of validation results and next steps

