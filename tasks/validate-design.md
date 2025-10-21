**GOAL**: Validate design consistency across project documents ensuring no fabricated content, conflicts, or missing mappings.

## [Context]
**You must read the following context:**
- `{workflow}` parameter (required) - "prd" or "full"
- If `workflow = prd`: `{PRD}`
- If `workflow = prd`: `{ARCH}/*.md` (only the related documents; optional for alignment check)
- If `workflow = full`: `{REQ}/*.md` (only the related documents)
- If `workflow = full`: `{ARCH}/*.md` (only the related documents)
- If `workflow = full`: `{EPIC}`
- `{TMPL}/design-validation-tmpl.yaml`

## [Products]
- `{root}/docs/design-validation.md`

## [Constraints]
- **MUST** process only `prd` or `full` workflows; **MUST NOT** process other values.
- **MUST** perform all validation check types (fabrication, conflicts, coverage, consistency); **MUST NOT** skip any.
- **MUST** categorize issues by severity; **MUST NOT** produce a report without categorization.

## [Instructions]
1. **Step 1: Validate Workflow and Scope**
- **GOAL:** Confirm the provided workflow and define validation boundaries before analysis begins.
- **STEPS:**
  - Validate that `{workflow}` is either `prd` or `full`; halt if any other value appears.
  - Enumerate required documents per workflow (PRD, ARCH, REQ, EPIC, PLAN) and lock the review scope.
  - Review `{TMPL}/design-validation-tmpl.yaml` to understand mandatory report sections and data points.
- **QUESTIONS:**
  - Which workflow value is supplied, and does it match `prd` or `full` exactly?
  - Which document sets are in scope for this workflow?
  - Does the template require any additional metadata before proceeding?
- **CHECKLIST:**
  - [ ] Workflow validated as `prd` or `full` with scope boundaries documented.
  - [ ] Source documents collected and access paths confirmed.
  - [ ] Reporting template requirements reviewed and understood.

2. **Step 2: Extract and Index Entities**
- **GOAL:** Build a comprehensive inventory of every requirement, component, task, and plan involved in the workflow.
- **STEPS:**
  - Parse PRD/requirements for IDs (`REQ-###`, `NFR-###`), acceptance criteria, and dependencies.
  - Capture architecture elements: components, interfaces, ADR references, and their requirement mappings.
  - Catalog epic tasks (`Task-#`) alongside related plan files (`{task_id}-plan.md`), dependencies, and file paths.
  - Record technology stack mentions and cross-document component names for later consistency checks.
- **QUESTIONS:**
  - Are all requirement and task identifiers present with supporting context?
  - Do architecture documents provide mappings back to the identified requirements?
  - Which plans correspond to each task, and are any missing?
- **CHECKLIST:**
  - [ ] Entity index completed covering requirements, architecture, tasks, and plans.
  - [ ] Traceability mappings recorded for every entity relationship.
  - [ ] Data structured for quick lookup during validation checks.

3. **Step 3: Execute Validation Checks**
- **GOAL:** Verify authenticity, coverage, and consistency across all scoped documents.
- **STEPS:**
  - Run fabrication detection by cross-referencing every entity mention against its source; flag missing definitions or files.
  - Verify reference integrity and compute coverage metrics (REQ→ARCH, ARCH→TASK, TASK→PLAN) using `(satisfied / total) * 100`.
  - Apply workflow-specific focus: PRD emphasizes internal traceability; Full demands end-to-end bidirectional validation.
  - Assess naming consistency, technical alignment, and dependency logic; classify findings using severity criteria (Critical: fabricated references, missing documents, or broken traceability; High: coverage gaps >10% or orphaned mappings; Medium: naming or spec mismatches; Low: formatting or documentation gaps).
- **QUESTIONS:**
  - Do any referenced IDs lack a corresponding definition or document?
  - Where do coverage percentages fall below expected thresholds?
  - Are there contradictions or circular dependencies across documents?
- **CHECKLIST:**
  - [ ] Fabrication, reference, coverage, and consistency checks completed.
  - [ ] Severity assigned to each issue (Critical, High, Medium, Low) based on impact.
  - [ ] Workflow-specific validation goals satisfied.

4. **Step 4: Generate Validation Report**
- **GOAL:** Produce an actionable report using the template with categorized findings and clear remediation guidance.
- **STEPS:**
  - Populate all sections of `design-validation-tmpl.yaml`, including summary, issue catalog, metrics, scope, and appendix.
  - Document each finding with evidence, impact, and required or recommended actions aligned to its severity level.
  - Summarize coverage results, highlight recommendations (e.g., `/sunnycore_po *fix-design-conflicts`), and define next steps based on the workflow outcome.
  - Confirm every quality gate is satisfied before marking the validation complete.
- **QUESTIONS:**
  - Does the report clearly categorize issues by severity with supporting evidence?
  - Are coverage metrics and entity counts reported for the applicable workflow?
  - Do recommendations guide the team toward resolving blockers and revalidation?
- **CHECKLIST:**
  - [ ] Report generated with all template sections completed accurately.
  - [ ] Recommendations and next steps documented per severity and workflow.
  - [ ] Quality gates reviewed and confirmed as passed.

## [Validation Criteria]
**PRD Workflow:** Internal consistency (all internal refs valid, no circular dependencies, requirements-architecture-tasks alignment); external alignment if an existing architecture exists (no breaking changes, integration points correct, compatible with tech stack); completeness (all requirements have architecture mappings, all architecture components have task mappings, no orphaned entities).

**Full Workflow:** Bidirectional integrity (forward and backward references complete, no broken links); coverage metrics (requirement→architecture: 100%, architecture→tasks: 100%, tasks→plans: 100%); consistency (terminology uniform, technical specs match, no contradictions); authenticity (all refs exist, no fabricated content, all entities verifiable).

## [Quality Gates]
All gates **MUST** pass before marking complete:
- [ ] Workflow parameter validated and scope determined correctly.
- [ ] All entities extracted and indexed from relevant documents.
- [ ] All validation checks executed (fabrication, references, coverage, consistency).
- [ ] Validation report generated using `design-validation-tmpl.yaml` with severity categorization.
- [ ] Clear recommendations provided based on findings.