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
  1. Do not process workflow parameters other than "prd" or "full"
  2. Do not skip any validation check type (fabrication, conflicts, coverage, consistency)
  3. Do not produce validation report without severity categorization

## [Steps]
  1. Initialization & Scope Determination
    - Validate workflow parameter (prd or full)
    - Determine validation scope for workflow type
    - Conceive the best solution for the task that needs to be completed
    - Outcome: Validation scope and workflow determined, plan outline documented

  2. Content Extraction & Indexing
    - Extract content appropriate for workflow type
    - Create comprehensive internal index of all entities
    - Handle workflow-specific extraction paths
    - Outcome: All entities extracted and indexed

  3. Validation Execution
    - Perform workflow-appropriate validation checks
    - Achieve complete validation coverage across all criteria
    - Detect all issue types (consistency, coverage, conflicts, authenticity)
    - Outcome: Complete validation performed with all issues identified

  4. Report Generation & Categorization
    - Create comprehensive validation report at "{root}/docs/design-validation.md"
    - Categorize issues properly by severity
    - Include all required report sections
    - Outcome: Detailed validation report with categorized issues

  5. Summary & Recommendations
    - Present validation summary to user
    - Provide appropriate recommendations based on findings
    - Guide user on next steps
    - Outcome: User informed with clear next-step guidance

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
  - [ ] Bidirectional validation complete with 100% coverage verification and no fabricated references
  - [ ] Complete validation report at "{root}/docs/design-validation.md" with issues categorized by severity
  - [ ] User informed of results with clear guidance for next steps

## [Example]

### Good Example 1
[INPUT]
Workflow parameter: "prd". PRD exists at docs/PRD.md with 3 requirements, 2 architecture components, 3 tasks.

[DECISION]
Step 1: Validate workflow="prd", determine scope (PRD internal consistency + external alignment if architecture exists). Step 2: Extract all entities from PRD - REQ-001, REQ-002, REQ-003, Component-A, Component-B, Task-1, Task-2, Task-3. Create internal index. Step 3: Validate internal consistency - all REQ IDs referenced exist, no circular dependencies. Check requirements→architecture mapping (100%), architecture→tasks mapping (100%). No orphaned entities. Check external alignment with existing docs/architecture/ - no breaking changes, integration points valid. Step 4: Generate docs/design-validation.md with status PASS, all checks successful. Step 5: Present summary: "Validation passed. PRD internally consistent and compatible with existing architecture."

[OUTCOME]
Complete docs/design-validation.md with status PASS. All validation checks documented: internal consistency ✓, external alignment ✓, completeness 100%. No issues found. Recommendation provided: proceed with development using /sunnycore_dev *develop-prd.

[WHY-GOOD]
- Applies the PRD validation scope precisely, ensuring both internal and external consistency are verified.
- Provides clear next-step guidance backed by documented evidence, enabling confident progression.

### Good Example 2
[INPUT]
Workflow parameter: "full". Requirements in docs/requirements/*.md (5 requirements), architecture in docs/architecture/*.md (3 components), epic at docs/epic.md (4 tasks), plans in docs/plans/*.md (3 files, missing plan for Task-4).

[DECISION]
Step 1: Validate workflow="full", determine full workflow validation scope. Step 2: Extract entities - 5 REQs, 3 components, 4 tasks, 3 plans. Index all. Step 3: Validate bidirectional integrity - REQ-005 referenced in architecture but doesn't exist in requirements (fabricated - Critical severity). Check coverage - REQ-002 not mapped to any component (coverage gap - High severity). Task-4 has no plan file (missing plan - High severity). Check consistency - "UserService" vs "User Service" naming inconsistency (Medium severity). Step 4: Generate docs/design-validation.md with detailed issues by severity and type. Step 5: Recommend fix using /sunnycore_po *fix-design-conflicts.

[OUTCOME]
docs/design-validation.md with 4 issues categorized: 1 Critical (fabricated REQ-005), 2 High (REQ-002 unmapped, Task-4 plan missing), 1 Medium (naming inconsistency). Clear guidance: fix conflicts before development. Traceability gaps identified for correction.

[WHY-GOOD]
- Systematically surfaces gaps across requirements, architecture, tasks, and plans, honoring the full workflow scope.
- Delivers actionable categorization and remediation guidance, preventing flawed execution downstream.

### Bad Example 1
[INPUT]
Workflow parameter provided but value is "custom" (not "prd" or "full").

[BAD-DECISION]
Proceed with validation using guessed workflow type. Skip workflow parameter validation. Create report with incomplete checks. Mix prd and full validation criteria incorrectly.

[WHY-BAD]
Violates Constraint 1 (do not process workflow other than prd/full). Invalid workflow leads to incorrect validation scope. Mixed criteria produces unreliable results. Error-Handling rule 1 requires reporting invalid parameter error.

[CORRECT-APPROACH]
Step 1: Validate workflow parameter. If not "prd" or "full", halt immediately. Report error: "Invalid workflow parameter 'custom'. Valid options: 'prd' or 'full'". List expected parameter format. Request user to provide correct workflow type. Do not proceed with validation until valid parameter provided.

### Bad Example 2
[INPUT]
Full workflow validation required. Some documents exist, some missing.

[BAD-DECISION]
Skip bidirectional integrity check entirely. Only check forward references (requirements→architecture), ignore backward references. Skip coverage metrics calculation. Don't check for fabricated content. Generate report claiming "validation complete" despite incomplete checks. No severity categorization.

[WHY-BAD]
Violates Constraint 2 (skip validation check types). Violates Validation-Criteria full workflow section 1 (bidirectional integrity required). Missing backward reference check means broken links undetected. No fabrication check allows invalid references. No severity categorization violates Constraint 3. Incomplete validation is useless.

[CORRECT-APPROACH]
Execute Step 3 completely per Validation-Focus-Areas. Check bidirectional integrity: forward (requirements→architecture→tasks→plans) AND backward (plans→tasks→architecture→requirements). Calculate coverage: requirements→architecture 100%, architecture→tasks 100%, tasks→plans 100%. Check consistency: terminology, technical specs. Verify authenticity: all referenced entities exist, no fabricated IDs. Categorize ALL issues by severity (Critical/High/Medium/Low) per Constraint 3. Only declare validation complete after all check types executed.
