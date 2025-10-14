**GOAL**: Generate completion report, archive deliverables, and clean workspace for next cycle.

## [Input]
- `{root}/docs/*.md`
- `{LOCK}`
- `{TMPL}/completion-report-tmpl.yaml`

## [Output]
- `{root}/docs/completion-report.md`

## [Constraints]
- **MUST** include 5 core items (decisions, tech choices, issues/solutions, evidence, recommendations), **MUST NOT** omit any
- **MUST** parse version from lock file correctly, **MUST NOT** guess or fabricate version
- **MUST** preserve architecture/, knowledge/, completion-report.md during archiving, **MUST NOT** move them
- **MUST** only remove requirement-specific content from preserved docs, **MUST NOT** remove architectural decisions

## [Steps]
**You should work along to the following steps:**
1. Parse version from lock, validate inputs. This identifies the version with all inputs verified.
2. Extract 5 core items, map to template. This completes the extraction with evidence.
3. Generate completion report. This creates the report with all 5 core items.
4. Create archive directory, move files (preserve architecture/, knowledge/, completion-report.md). This archives files successfully.
5. Update references, clean requirement-specific content from preserved docs. This prepares the workspace for the next cycle.

## [Instructions]

### 1. Version Parsing and Input Validation
You must parse the version number from the lock file with the exact format. The version must be in the format `x.x.x` (semantic versioning). Never guess or fabricate a version number. If the lock file is missing or corrupted, halt execution and request user intervention.

### 2. Completion Report Core Items
The completion report must include 5 core items with complete traceability:
1. **Key Decisions**: Architectural decisions with ADR references (e.g., ADR-003: async payment processing)
2. **Technology Choices**: Selected technologies with rationale (e.g., Stripe API for payment processing)
3. **Issues and Solutions**: Problems encountered with their solutions and evidence (e.g., rate limiting bug fixed in PaymentService.js:L42-L56)
4. **Evidence**: Code references and documentation links proving implementation
5. **Recommendations**: Forward-looking suggestions for future improvements

### 3. Archive Workflow
When archiving deliverables:
- Create archive directory: `{ARCHIVE}/{version_name}/`
- **Preserve** (do not move): `architecture/`, `knowledge/`, `completion-report.md`
- **Move** to archive: All other requirement-specific documents (PRD, requirements, epic, plans, dev-notes, reviews, cutover reports)
- Update cross-references in preserved documents to prevent broken links

### 4. Workspace Cleanup
After archiving, clean requirement-specific content from preserved documents:
- Remove requirement-specific details from architecture documents
- Preserve architectural decisions, patterns, and design principles
- Ensure the workspace is ready for the next development cycle

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Completion report with 5 core items at "{root}/docs/completion-report.md"
- [ ] Files archived to "{ARCHIVE}/{version_name}/" (excluding architecture/, knowledge/, completion-report.md)
- [ ] Workspace cleaned of requirement-specific content

## [Example]

### Good #1
**Input**: Lock file version = 1.2.0. Found PRD.md, prd-dev-notes.md, cutover-report.md. Template requires 5 core items  
**Decision**: Parse version from lock. Identify PRD workflow. Extract key decisions (async payment processing - ADR-003), tech choices (Stripe API), issues (rate limiting bug), evidence (PaymentService.js:L42-L56), recommendations (add throttling). Generate completion report. Create archive/1.2.0/. Move PRD.md, dev-notes, cutover-report to archive. Preserve architecture/, knowledge/, completion-report.md. Remove requirement-related content from active docs.  
**Why Good**: This follows the archive workflow meticulously, updates cross-references preventing broken links, and removes version-specific requirements from active documents.

### Good #2
**Input**: Lock file version = 2.0.0. Full workflow project with requirements/, architecture/, epic.md, plans/*.md (8 files), dev-notes/*.md (8 files), review/*.md  
**Decision**: Parse major version 2.0.0. Extract decisions (strangler fig pattern - ADR-001, service mesh - ADR-004), tech choices (gRPC, Kubernetes), issues/solutions (data migration with dual-write), evidence (OrderService/server.js:L10-L80), recommendations (monitoring strategy). Generate comprehensive completion report. Archive all docs except architecture/, knowledge/, completion-report.md. Clean requirement-specific content from preserved docs.  
**Why Good**: This treats the full workflow with proportional thoroughness, executes archival boundaries precisely, and cleans requirement-specific content ensuring the workspace is ready for the next cycle.

### Bad #1
**Input**: Lock file missing or corrupted. Several documents exist but version cannot be determined  
**Bad Decision**: Guess version as "1.0.0". Proceed with archiving. Generate completion report without proper version. Skip validation of required inputs.  
**Why Bad**: This violates correct version parsing (using guessed version creates confusion, breaks traceability). Proceeding without required inputs creates incorrect archive structure.  
**Correct**: Halt execution immediately. Report error: "Lock file missing or cannot parse version number. Required format: version = x.x.x". List expected lock file location. Request user fix lock file before proceeding. Do not guess or fabricate version information.

### Bad #2
**Input**: All required documents exist. Completion report should include 5 core items. Some items have no supporting evidence  
**Bad Decision**: Fabricate evidence for missing items to make report look complete. Invent architectural decisions never documented. Generate vague recommendations without specific details.  
**Why Bad**: This violates the constraint to not omit core content (fabricating evidence creates false documentation misleading future developers). This also violates the traceability principle.  
**Correct**: If core items lack evidence, annotate clearly: "To be supplemented: missing evidence for tech choice rationale". Extract only verifiable information from actual documents and code. Generate specific recommendations based on actual issues. Maintain integrity even if some sections incomplete.
