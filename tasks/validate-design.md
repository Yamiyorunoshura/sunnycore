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

## [Steps]
1. Validate workflow parameter ("prd" or "full"), determine validation scope → Validation scope and workflow determined
2. Extract content, create comprehensive internal index → All entities extracted and indexed
3. Perform workflow-appropriate validation checks → Complete validation with all issues identified
4. Create comprehensive validation report at "{root}/docs/design-validation.md" → Detailed validation report with categorized issues
5. Present summary, provide recommendations based on findings → User informed with clear next-step guidance

## [Validation-Criteria]
**PRD Workflow**: Internal consistency (all internal refs valid, no circular dependencies, requirements-architecture-tasks alignment), External alignment if existing arch exists (no breaking changes, integration points correct, compatible with tech stack), Completeness (all req have arch mapping, all arch components have task mapping, no orphaned entities)

**Full Workflow**: Bidirectional integrity (forward and backward references complete, no broken links), Coverage metrics (requirement→architecture: 100%, architecture→tasks: 100%, tasks→plans: 100%), Consistency (terminology uniform, technical specs match, no contradictions), Authenticity (all refs exist, no fabricated content, all entities verifiable)

## [DoD]
- [ ] Bidirectional validation complete with 100% coverage verification and no fabricated references
- [ ] Complete validation report at "{root}/docs/design-validation.md" with issues categorized by severity
- [ ] User informed with clear next-step guidance

## [Example]

### Good #1
**Input**: Workflow="prd". PRD at docs/PRD.md with 3 requirements, 2 components, 3 tasks  
**Decision**: Validate workflow="prd"→Determine scope (PRD internal consistency + external alignment if arch exists)→Extract all entities from PRD: REQ-001, REQ-002, REQ-003, Component-A, Component-B, Task-1, Task-2, Task-3→Create internal index→Validate internal consistency (all REQ IDs referenced exist, no circular dependencies)→Check requirements→architecture mapping (100%), architecture→tasks mapping (100%)→No orphaned entities→Check external alignment with docs/architecture/ (no breaking changes, integration points valid)→Generate docs/design-validation.md with status PASS, all checks successful→Present summary: "Validation passed. PRD internally consistent and compatible with existing architecture."  
**Why Good**: Applies PRD validation scope precisely, verifies both internal and external consistency, provides clear next-step guidance

### Good #2
**Input**: Workflow="full". Requirements in docs/requirements/*.md (5 requirements), architecture in docs/architecture/*.md (3 components), epic at docs/epic.md (4 tasks), plans in docs/plans/*.md (3 files, missing plan for Task-4)  
**Decision**: Validate workflow="full"→Determine full workflow validation scope→Extract entities: 5 REQs, 3 components, 4 tasks, 3 plans→Index all→Validate bidirectional integrity: REQ-005 referenced in arch but doesn't exist in requirements (fabricated - Critical severity)→Check coverage: REQ-002 not mapped to any component (coverage gap - High severity), Task-4 has no plan file (missing plan - High severity)→Check consistency: "UserService" vs "User Service" naming inconsistency (Medium severity)→Generate docs/design-validation.md with detailed issues by severity and type→Recommend fix using /sunnycore_po *fix-design-conflicts  
**Why Good**: Systematically surfaces gaps across all documents, honors full workflow scope, delivers actionable categorization and remediation guidance

### Bad #1
**Input**: Workflow parameter="custom" (not "prd" or "full")  
**Bad Decision**: Proceed with validation using guessed workflow type→Skip workflow parameter validation→Create report with incomplete checks→Mix prd and full validation criteria incorrectly  
**Why Bad**: Violates constraint (only process "prd" or "full"). Invalid workflow leads to incorrect scope, mixed criteria produces unreliable results  
**Correct**: Validate workflow parameter→If not "prd" or "full", halt immediately→Report error: "Invalid workflow parameter 'custom'. Valid options: 'prd' or 'full'"→List expected parameter format→Request user provide correct workflow type→Do not proceed until valid parameter provided
