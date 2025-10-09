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
  2. **sequential-thinking (MCP)**
    - [Step 1: Analyze workflow type and validation scope]
    - [Step 2-4: Reason about validation logic and issue priority ranking]
    - When to use: When need complex bidirectional validation logic or conflict impact analysis
  3. **claude-context (MCP)**
    - [Step 2: Verify whether components referenced in documents exist in the codebase]
    - Query examples: "Does component X exist?" "Where is requirement Y implemented?"

## [Steps]
  1. Initialization Phase
    - Validate workflow parameter and determine validation scope
    - Ensure proper handling of both PRD and Full workflow types
    - Establish progress tracking mechanism for validation tasks

  2. Content Extraction and Indexing Phase
    - Ensure appropriate content extraction for workflow type
    - Achieve comprehensive internal index of all entities
    - Ensure proper handling of both workflow-specific extraction paths

  3. Validation Phase
    - Ensure workflow-appropriate validation checks are performed
    - Achieve complete validation coverage across all criteria
    - Ensure proper detection of all issue types (consistency, coverage, conflicts, authenticity)

  4. Report Generation Phase
    - Achieve comprehensive validation report at "{root}/docs/design-validation.md"
    - Ensure issues are properly categorized by severity
    - Ensure report structure includes all required sections

  5. Finalization Phase
    - Ensure validation summary is presented to user
    - Ensure appropriate recommendations based on findings
    - Ensure proper guidance for next steps

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

## [Validation-Focus-Areas]
  1. **Bidirectional Integrity**
    - Verify forward references (requirements → architecture → tasks → plans)
    - Verify backward references (plans → tasks → architecture → requirements)
    - Detect broken links and fabricated content
  
  2. **100% Coverage Requirement**
    - All requirements must map to architecture components
    - All architecture components must map to tasks
    - All tasks must have implementation plans (if full workflow)
    - No orphaned entities in any document
  
  3. **Consistency Checks**
    - Terminology uniformity across all documents
    - Technical specifications match between documents
    - No contradictory statements or conflicts
  
  4. **Authenticity Verification**
    - All references must point to existing entities
    - No fabricated requirement IDs, component names, or file paths
    - Cross-check entity existence in actual documents

## [DoD]
  - [ ] Workflow parameter is validated as "prd" or "full"
  - [ ] All required documents are fully understood and indexed
  - [ ] Bidirectional reference validation is complete (forward and backward references verified)
  - [ ] Coverage analysis is complete with all metrics calculated (100% requirement coverage verified)
  - [ ] Consistency checks across all documents are complete
  - [ ] Content authenticity verification is complete (no fabricated references)
  - [ ] Conflict detection is complete across all document types
  - [ ] All identified issues are categorized by severity (Critical/High/Medium/Low)
  - [ ] Complete validation report exists at "{root}/docs/design-validation.md" with findings and recommendations
  - [ ] User is informed of validation results with clear guidance on next steps

## [Example]

### Example 1: PRD Workflow Validation - Success
[Input]
- Workflow: "prd"
- PRD: docs/PRD.md (3 requirements, 2 architecture components, 3 tasks)
- Existing architecture: docs/architecture/*.md (API Gateway, Database)

[Decision]
- Internal consistency: All REQ-001, REQ-002, REQ-003 referenced correctly ✓
- External alignment: New API endpoints compatible with existing API Gateway ✓
- Completeness: All requirements → architecture (100%), all architecture → tasks (100%) ✓
- Authenticity: All components exist, no fabricated references ✓
- Result: Validation passed, no issues found

[Expected Outcome]
- docs/design-validation.md with status: PASS
- Summary: "All validation checks passed. PRD is internally consistent and aligns with existing architecture."
- Recommendation: "Proceed with development using `/sunnycore_dev *develop-prd`"

### Example 2: Full Workflow Validation - Issues Found
[Input]
- Workflow: "full"
- Requirements: docs/requirements/*.md (5 requirements)
- Architecture: docs/architecture/*.md (3 components)
- Epic: docs/epic.md (4 tasks)
- Plans: docs/plans/*.md (3 plans, missing plan for Task-4)

[Decision]
- Bidirectional integrity: REQ-005 referenced in arch but doesn't exist ✗ (Critical)
- Coverage: REQ-002 not mapped to any architecture component ✗ (High)
- Coverage: Task-4 exists but no implementation plan ✗ (High)
- Consistency: "UserService" named "User Service" in architecture ✗ (Medium)
- Issues: 1 Critical, 2 High, 1 Medium

[Expected Outcome]
- docs/design-validation.md with detailed issues:
  - Critical: Fabricated REQ-005 reference in docs/architecture/components.md
  - High: Coverage gap - REQ-002 unmapped
  - High: Missing plan - docs/plans/4-plan.md doesn't exist
  - Medium: Inconsistent naming - "UserService" vs "User Service"
- Recommendation: "Fix issues using `/sunnycore_po *fix-design-conflicts` before proceeding with development"

