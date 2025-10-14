**GOAL**: Validate design consistency across project documents ensuring no fabricated content, conflicts, or missing mappings.

## [Input]
- {workflow} parameter (required) - "prd" or "full"
- (If workflow=prd) `{PRD}`
- (If workflow=prd) `{ARCH}/*.md` (optional, for alignment check)
- (If workflow=full) `{REQ}/*.md`
- (If workflow=full) `{ARCH}/*.md`
- (If workflow=full) `{EPIC}`
- (If workflow=full) `{PLAN}/*.md`

## [Output]
- `{root}/docs/design-validation.md`

## [Constraints]
- **MUST** process only "prd" or "full" workflow, **MUST NOT** process other workflows
- **MUST** perform all validation check types (fabrication, conflicts, coverage, consistency), **MUST NOT** skip any
- **MUST** categorize issues by severity, **MUST NOT** produce report without categorization

## [Instructions]

### 1. Workflow Parameter Validation
Validate the workflow parameter before proceeding:

**Valid Workflows**:
- `"prd"`: Validate PRD workflow (single PRD document)
- `"full"`: Validate full workflow (requirements, architecture, epic, plans)

**Validation**:
- If parameter is NOT "prd" or "full", HALT immediately
- Return error: "Invalid workflow parameter '{value}'. Valid options: 'prd' or 'full'"
- Do NOT proceed with validation until valid parameter is provided

### 2. Content Extraction and Indexing
Extract all entities and create comprehensive internal index:

#### For PRD Workflow:
- Extract all requirements (REQ-001, REQ-002, etc.) from PRD
- Extract all architecture components from PRD
- Extract all tasks from PRD
- Create internal index mapping all entities and their references

#### For Full Workflow:
- Extract all requirements from `{REQ}/*.md`
- Extract all architecture components from `{ARCH}/*.md`
- Extract all tasks from `{EPIC}`
- Extract all plans from `{PLAN}/*.md`
- Create comprehensive index with bidirectional references

### 3. Validation Checks
Perform ALL validation checks systematically:

#### Check 1: Fabrication Detection (CRITICAL)
Identify any fabricated or non-existent entities:
- Requirements referenced but don't exist in source documents
- Components referenced but not defined in architecture
- Tasks referenced but not in epic
- Plans referenced but files don't exist

**Severity**: Critical (fabricated content blocks development)

#### Check 2: Broken References (CRITICAL)
Identify invalid cross-references:
- Requirements referencing non-existent components
- Tasks referencing non-existent requirements
- Plans referencing non-existent tasks

**Severity**: Critical (broken references prevent traceability)

#### Check 3: Coverage Gaps (HIGH)
Identify missing mappings:
- Requirements without architecture components
- Architecture components without tasks
- Tasks without implementation plans
- Orphaned entities (defined but never referenced)

**Severity**: High (gaps prevent 100% traceability)

#### Check 4: Consistency Issues (MEDIUM)
Identify inconsistencies:
- Naming variations ("UserService" vs "User Service")
- Contradictory specifications
- Technical spec mismatches (e.g., PostgreSQL vs MySQL)

**Severity**: Medium (affects clarity and maintainability)

#### Check 5: Workflow-Specific Validations

**For PRD Workflow**:
- **Internal Consistency**: All internal references valid, no circular dependencies
- **External Alignment** (if existing arch exists): No breaking changes, integration points correct, tech stack compatible

**For Full Workflow**:
- **Bidirectional Integrity**: Forward and backward references complete
- **Coverage Metrics**: 
  - Requirement → Architecture: 100%
  - Architecture → Tasks: 100%
  - Tasks → Plans: 100%

### 4. Issue Categorization and Reporting
Categorize all issues by severity and type:

**Severity Levels**:
- **Critical**: Fabricated content, broken references, missing required files
- **High**: Coverage gaps, missing mappings
- **Medium**: Inconsistencies, naming variations
- **Low**: Minor formatting or stylistic issues

**Report Structure**:
```markdown
# Design Validation Report

## Summary
- Total Issues: X
- Critical: Y
- High: Z
- Medium: A
- Low: B

## Critical Issues
[List all critical issues with details]

## High Severity Issues
[List all high issues with details]

## Medium Severity Issues
[List all medium issues with details]

## Low Severity Issues
[List all low issues with details]

## Validation Metrics
- Requirement Coverage: X%
- Architecture Coverage: Y%
- Task Coverage: Z%
```

### 5. Recommendations and Next Steps
Based on validation results, provide clear recommendations:

**If Issues Found**:
- Recommend using `/sunnycore_po *fix-design-conflicts` to resolve issues
- Prioritize critical and high severity issues
- Provide estimated effort (simple fixes vs major rework)

**If No Issues Found**:
- Report validation PASSED
- Confirm design is consistent and complete
- Recommend proceeding to next phase (implementation or review)

## [Steps]
1. Validate workflow parameter ("prd" or "full"), determine validation scope. This determines validation scope and workflow.
2. Extract content, create comprehensive internal index. This indexes all entities extracted.
3. Perform workflow-appropriate validation checks. This completes validation with all issues identified.
4. Create comprehensive validation report at "{root}/docs/design-validation.md". This produces detailed validation report with categorized issues.
5. Present summary, provide recommendations based on findings. This informs user with clear next-step guidance.

## [Validation-Criteria]
**PRD Workflow**: Internal consistency (all internal refs valid, no circular dependencies, requirements-architecture-tasks alignment), External alignment if existing arch exists (no breaking changes, integration points correct, compatible with tech stack), Completeness (all req have arch mapping, all arch components have task mapping, no orphaned entities)

**Full Workflow**: Bidirectional integrity (forward and backward references complete, no broken links), Coverage metrics (requirement→architecture: 100%, architecture→tasks: 100%, tasks→plans: 100%), Consistency (terminology uniform, technical specs match, no contradictions), Authenticity (all refs exist, no fabricated content, all entities verifiable)

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Bidirectional validation complete with 100% coverage verification and no fabricated references
- [ ] Complete validation report at "{root}/docs/design-validation.md" with issues categorized by severity
- [ ] User informed with clear next-step guidance

## [Example]

### Good #1
**Input**: Workflow="prd". PRD at docs/PRD.md with 3 requirements, 2 components, 3 tasks  
**Decision**: Validate workflow="prd" ✓. Determine scope (PRD internal consistency + external alignment if arch exists). Extract all entities from PRD: REQ-001, REQ-002, REQ-003, Component-A, Component-B, Task-1, Task-2, Task-3. Create internal index. Validate internal consistency (all REQ IDs referenced exist, no circular dependencies). Check requirements→architecture mapping (100%), architecture→tasks mapping (100%). No orphaned entities. Check external alignment with docs/architecture/ (no breaking changes, integration points valid). Generate docs/design-validation.md with status PASS, all checks successful. Present summary: "Validation passed. PRD internally consistent and compatible with existing architecture."  
**Why Good**: This applies PRD validation scope precisely, verifies both internal and external consistency, and provides clear next-step guidance.

### Good #2
**Input**: Workflow="full". Requirements in docs/requirements/*.md (5 requirements), architecture in docs/architecture/*.md (3 components), epic at docs/epic.md (4 tasks), plans in docs/plans/*.md (3 files, missing plan for Task-4)  
**Decision**: Validate workflow="full" ✓. Determine full workflow validation scope. Extract entities: 5 REQs, 3 components, 4 tasks, 3 plans. Index all. Validate bidirectional integrity: REQ-005 referenced in arch but doesn't exist in requirements (fabricated - Critical severity). Check coverage: REQ-002 not mapped to any component (coverage gap - High severity), Task-4 has no plan file (missing plan - High severity). Check consistency: "UserService" vs "User Service" naming inconsistency (Medium severity). Generate docs/design-validation.md with detailed issues by severity and type. Recommend fix using /sunnycore_po *fix-design-conflicts.  
**Why Good**: This systematically surfaces gaps across all documents, honors full workflow scope, and delivers actionable categorization and remediation guidance.

### Bad #1
**Input**: Workflow parameter="custom" (not "prd" or "full")  
**Bad Decision**: Proceed with validation using guessed workflow type. Skip workflow parameter validation. Create report with incomplete checks. Mix prd and full validation criteria incorrectly.  
**Why Bad**: This violates constraint (only process "prd" or "full"). Invalid workflow leads to incorrect scope and mixed criteria produces unreliable results.  
**Correct**: Validate workflow parameter. If not "prd" or "full", halt immediately. Report error: "Invalid workflow parameter 'custom'. Valid options: 'prd' or 'full'". List expected parameter format. Request user provide correct workflow type. Do not proceed until valid parameter provided.
