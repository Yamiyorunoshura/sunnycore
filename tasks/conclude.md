**GOAL**: Generate completion report, archive deliverables, and clean workspace for next cycle.

## [Context]
**You must read the following context:**
- `{root}/docs/*.md`
- `{LOCK}`
- `{TMPL}/completion-report-tmpl.yaml`

## [Products]
- `{root}/docs/completion-report.md`

## [Constraints]
- **MUST** parse version from lock file correctly, **MUST NOT** guess or fabricate version
- **MUST** preserve architecture/, knowledge/, completion-report.md during archiving, **MUST NOT** move them
- **MUST** only remove requirement-specific content from preserved docs, **MUST NOT** remove architectural decisions

## [Instructions]
[Instructions]
1. **Step 1: Parse Version and Validate Inputs**
- **GOAL:** Confirm the release version and required source documents before continuing.
- **STEPS:**
  - Read `{LOCK}` and extract the semantic version (`x.x.x`); stop if missing or malformed.
  - Verify required documents exist: dev-notes in `{DEVNOTES}/` or `{root}/docs/prd-dev-notes.md`, review reports in `{REVIEW}/`, cutover reports, and architecture docs in `{root}/docs/architecture/` or `{root}/docs/architecture.md`.
  - Capture version and validation outcomes for later reporting.
- **QUESTIONS:**
  - Does `{LOCK}` contain a valid semantic version without guessing?
  - Are any mandatory source documents missing or corrupted?
  - What blockers need escalation before proceeding?
- **CHECKLIST:**
  - [ ] Version copied directly from `{LOCK}` in `x.x.x` format.
  - [ ] All required source documents confirmed accessible.
  - [ ] Issues escalated when validation fails.

2. **Step 2: Extract Source Insights**
- **GOAL:** Gather evidence from project artifacts to populate the completion report.
- **STEPS:**
  - Review dev-note files for technical decisions, challenges, debt, and supporting evidence (paths, metrics).
  - Summarize review reports for quality issues resolved, test coverage, and performance findings.
  - Capture cutover outcomes covering acceptance, readiness, configuration, and user verification.
  - Distill architecture materials for ADRs, design patterns, integrations, and cross-cutting concerns.
- **QUESTIONS:**
  - Which artifacts provide quantifiable evidence (paths, tests, metrics)?
  - How do technical decisions connect to business outcomes?
  - Are there information gaps requiring additional digging?
- **CHECKLIST:**
  - [ ] Dev-note insights recorded with clear evidence.
  - [ ] Review and cutover findings summarized for reuse.
  - [ ] Architecture highlights documented for future reference.

3. **Step 3: Assemble Completion Report**
- **GOAL:** Produce `{root}/docs/completion-report.md` using the official template.
- **STEPS:**
  - Inspect `{TMPL}/completion-report-tmpl.yaml` to confirm required sections and ordering.
  - Populate `{root}/docs/completion-report.md` with extracted evidence, aligning strictly with template structure.
  - Cite sources or mark TODOs rather than inventing data.
- **QUESTIONS:**
  - Are all template sections filled with verified content?
  - Do citations trace back to the correct source documents?
  - Where are TODO markers needed for missing information?
- **CHECKLIST:**
  - [ ] Completion report drafted at `{root}/docs/completion-report.md`.
  - [ ] Template sections populated without custom formatting.
  - [ ] Evidence and citations recorded accurately.

4. **Step 4: Archive Deliverables Safely**
- **GOAL:** Archive requirement-specific artifacts while preserving mandated directories.
- **STEPS:**
  - Create `{ARCHIVE}/{version_name}/` using the parsed version identifier.
  - Move PRD, requirements, epic, implementation plans, dev-notes, reviews, and cutover reports into the archive without breaking structure.
  - Confirm `architecture/`, `knowledge/`, and `completion-report.md` stay in place and update references accordingly.
- **QUESTIONS:**
  - Does the archive contain every requirement-specific artifact?
  - Have preserved directories remained untouched?
  - Do any references need updates after relocation?
- **CHECKLIST:**
  - [ ] Archive directory created with correct version name.
  - [ ] Required documents moved while preserving structure.
  - [ ] Preserved assets verified in original locations with refreshed references.

5. **Step 5: Clean and Validate Workspace**
- **GOAL:** Prepare the workspace for the next cycle without losing architectural knowledge.
- **STEPS:**
  - Strip requirement-specific details from preserved architecture and knowledge documents while retaining ADRs, patterns, and rationale.
  - Ensure `completion-report.md` and related docs reference archived materials correctly and that no links are broken.
  - Reconfirm all constraints and quality gates before declaring completion.
- **QUESTIONS:**
  - Did cleanup retain architectural decisions and reusable insights?
  - Are any references broken after archival and cleanup?
  - Is additional follow-up needed before handoff?
- **CHECKLIST:**
  - [ ] Preserved docs cleaned while keeping architectural value.
  - [ ] Cross-references validated with no broken links.
  - [ ] All gating criteria satisfied for the next cycle.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Completion report generated at "{root}/docs/completion-report.md"
- [ ] Version parsed correctly from lock file
- [ ] All source documents validated and information extracted
- [ ] Files archived to "{ARCHIVE}/{version_name}/" (excluding architecture/, knowledge/, completion-report.md)
- [ ] Workspace cleaned of requirement-specific content
- [ ] Cross-references updated, no broken links
