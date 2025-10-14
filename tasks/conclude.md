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
1. Parse version from lock, validate inputs → Version identified with all inputs verified
2. Extract 5 core items, map to template → Complete extraction with evidence
3. Generate completion report → Report created with all 5 core items
4. Create archive directory, move files (preserve architecture/, knowledge/, completion-report.md) → Files archived successfully
5. Update references, clean requirement-specific content from preserved docs → Workspace ready for next cycle

## [DoD]
- [ ] Completion report with 5 core items at "{root}/docs/completion-report.md"
- [ ] Files archived to "{ARCHIVE}/{version_name}/" (excluding architecture/, knowledge/, completion-report.md)
- [ ] Workspace cleaned of requirement-specific content

## [Example]

### Good #1
**Input**: Lock file version = 1.2.0. Found PRD.md, prd-dev-notes.md, cutover-report.md. Template requires 5 core items  
**Decision**: Parse version from lock→Identify PRD workflow→Extract key decisions (async payment processing - ADR-003), tech choices (Stripe API), issues (rate limiting bug), evidence (PaymentService.js:L42-L56), recommendations (add throttling)→Generate completion report→Create archive/1.2.0/→Move PRD.md, dev-notes, cutover-report to archive→Preserve architecture/, knowledge/, completion-report.md→Remove requirement-related content from active docs  
**Why Good**: Follows archive workflow meticulously, updates cross-references preventing broken links, removes version-specific requirements from active documents

### Good #2
**Input**: Lock file version = 2.0.0. Full workflow project with requirements/, architecture/, epic.md, plans/*.md (8 files), dev-notes/*.md (8 files), review/*.md  
**Decision**: Parse major version 2.0.0→Extract decisions (strangler fig pattern - ADR-001, service mesh - ADR-004), tech choices (gRPC, Kubernetes), issues/solutions (data migration with dual-write), evidence (OrderService/server.js:L10-L80), recommendations (monitoring strategy)→Generate comprehensive completion report→Archive all docs except architecture/, knowledge/, completion-report.md→Clean requirement-specific content from preserved docs  
**Why Good**: Treats full workflow with proportional thoroughness, executes archival boundaries precisely, cleans requirement-specific content ensuring workspace ready for next cycle

### Bad #1
**Input**: Lock file missing or corrupted. Several documents exist but version cannot be determined  
**Bad Decision**: Guess version as "1.0.0"→Proceed with archiving→Generate completion report without proper version→Skip validation of required inputs  
**Why Bad**: Violates correct version parsing (using guessed version creates confusion, breaks traceability). Proceeding without required inputs creates incorrect archive structure  
**Correct**: Halt execution immediately→Report error: "Lock file missing or cannot parse version number. Required format: version = x.x.x"→List expected lock file location→Request user fix lock file before proceeding→Do not guess or fabricate version information

### Bad #2
**Input**: All required documents exist. Completion report should include 5 core items. Some items have no supporting evidence  
**Bad Decision**: Fabricate evidence for missing items to make report look complete→Invent architectural decisions never documented→Generate vague recommendations without specific details  
**Why Bad**: Violates do not omit core content (fabricating evidence creates false documentation misleading future developers). Violates traceability principle  
**Correct**: If core items lack evidence, annotate clearly: "To be supplemented: missing evidence for tech choice rationale"→Extract only verifiable information from actual documents and code→Generate specific recommendations based on actual issues→Maintain integrity even if some sections incomplete
