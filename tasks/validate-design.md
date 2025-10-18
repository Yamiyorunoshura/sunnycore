**GOAL**: Validate design consistency across project documents ensuring no fabricated content, conflicts, or missing mappings.

## [Context]
**You must read the following context:**
- {workflow} parameter (required) - "prd" or "full"
- (If workflow=prd) `{PRD}`
- (If workflow=prd) `{ARCH}/*.md`(Only the related documents) (optional, for alignment check)
- (If workflow=full) `{REQ}/*.md`(Only the related documents)
- (If workflow=full) `{ARCH}/*.md`(Only the related documents)
- (If workflow=full) `{EPIC}`
- `{TMPL}/design-validation-tmpl.yaml`

## [Products]
- `{root}/docs/design-validation.md`

## [Constraints]
- **MUST** process only "prd" or "full" workflow, **MUST NOT** process other workflows
- **MUST** perform all validation check types (fabrication, conflicts, coverage, consistency), **MUST NOT** skip any
- **MUST** categorize issues by severity, **MUST NOT** produce report without categorization

## [Steps]
**You should work along to the following steps:**
1. **Validate workflow and scope** - Confirm workflow parameter and determine validation boundaries
2. **Extract and index entities** - Build comprehensive inventory of all requirements, components, tasks, and plans
3. **Execute validation checks** - Perform systematic verification of references, coverage, and consistency
4. **Generate validation report** - Create categorized findings report with actionable recommendations

## [Instructions]

### Entity Extraction Techniques
**Extract entities systematically from each document type:**

**From PRD/Requirements Documents:**
- Scan for requirement IDs: Pattern `REQ-\d{3}` (e.g., REQ-001, REQ-002)
- Extract functional and non-functional requirements (NFR-\d{3})
- Note acceptance criteria and dependencies between requirements
- Identify all component/service names mentioned in architecture sections

**From Architecture Documents:**
- Extract component names from component sections and diagrams
- Collect API endpoints, service interfaces, and integration points
- Note technology stack selections and architectural decisions (ADR-\d{3})
- Map components to requirements through traceability tables

**From Epic Documents:**
- Extract task IDs: Pattern `Task-\d+` (e.g., Task-1, Task-2)
- Note task descriptions, dependencies, and quality gates
- Collect requirement mappings and architecture component references

**From Implementation Plans:**
- Identify plan files by task ID pattern: `{task_id}-plan.md`
- Extract task context and implementation approach
- Note file paths, dependencies, and test coverage details

### Validation Methodology
**Execute these validation checks in sequence:**

**1. Fabrication Detection (Critical Priority)**
- Cross-reference all mentioned entities against source documents
- Flag any `REQ-XXX` mentioned but not defined in requirements
- Identify components referenced but missing from architecture
- Detect `Task-X` references without corresponding epic entries
- Mark missing plan files for tasks that should have them

**2. Reference Integrity Verification**
- Verify all requirement → component mappings exist in both directions
- Check task → requirement relationships are valid
- Validate component → task assignments match architecture
- Ensure plan files exist for all implementation tasks

**3. Coverage Analysis**
- Calculate requirement coverage: `(mapped_reqs / total_reqs) * 100`
- Measure architecture coverage: `(tasks_with_components / total_tasks) * 100`
- Assess plan coverage: `(plans_exist / implementation_tasks) * 100`
- Identify orphaned entities (defined but never referenced)

**4. Consistency Validation**
- Compare entity names across documents for variations
- Check technical specifications for contradictions
- Verify dependency chains are logical and non-circular
- Validate priority and status consistency

### Workflow-Specific Focus
**PRD Workflow:**
- Prioritize internal consistency within single PRD document
- If existing architecture exists, verify alignment without breaking changes
- Focus on requirement → architecture → task traceability within PRD

**Full Workflow:**
- Ensure complete bidirectional traceability across all documents
- Verify 100% coverage at each level: REQ → ARCH → TASK → PLAN
- Validate end-to-end workflow integrity and dependency resolution

### Issue Severity Assessment
**Apply these severity criteria:**
- **Critical**: Fabricated references, missing required documents, broken traceability chains
- **High**: Coverage gaps >10%, orphaned requirements/components, missing task mappings
- **Medium**: Naming inconsistencies, minor specification mismatches
- **Low**: Formatting issues, style inconsistencies, documentation gaps

## [Validation-Criteria]
**PRD Workflow**: Internal consistency (all internal refs valid, no circular dependencies, requirements-architecture-tasks alignment), External alignment if existing arch exists (no breaking changes, integration points correct, compatible with tech stack), Completeness (all req have arch mapping, all arch components have task mapping, no orphaned entities)

**Full Workflow**: Bidirectional integrity (forward and backward references complete, no broken links), Coverage metrics (requirement→architecture: 100%, architecture→tasks: 100%, tasks→plans: 100%), Consistency (terminology uniform, technical specs match, no contradictions), Authenticity (all refs exist, no fabricated content, all entities verifiable)

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Workflow parameter validated, scope determined correctly
- [ ] All entities extracted and indexed from relevant documents
- [ ] All validation checks executed (fabrication, references, coverage, consistency)
- [ ] Validation report generated using design-validation-tmpl.yaml with severity categorization
- [ ] Clear recommendations provided based on findings

## [Example]

### Good: PRD Workflow Validation
**Input**: Workflow="prd", PRD at docs/PRD.md with 3 requirements, 2 components, 3 tasks  
**Process**: Extract entities (REQ-001 to REQ-003, Component-A/B, Task-1 to Task-3) → Verify all references exist → Check 100% requirement-to-architecture and architecture-to-task mappings → Validate external alignment with existing architecture (no breaking changes) → Generate report with PASS status  
**Result**: "Validation passed. PRD internally consistent and compatible with existing architecture."

### Good: Full Workflow with Issues  
**Input**: Workflow="full", 5 requirements, 3 components, 4 tasks, 3 plans (missing Task-4 plan)  
**Process**: Extract all entities → Detect REQ-005 referenced but not defined (Critical) → Identify REQ-002 unmapped to components (High) → Find Task-4 missing plan (High) → Note "UserService" vs "User Service" inconsistency (Medium) → Generate categorized report → Recommend `/sunnycore_po *fix-design-conflicts`  
**Result**: Systematic issue identification with actionable remediation guidance.

### Bad: Invalid Workflow
**Wrong**: Accept workflow="custom" and proceed with mixed validation criteria  
**Correct**: Halt immediately, return error "Invalid workflow parameter 'custom'. Valid options: 'prd' or 'full'"
