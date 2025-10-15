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

## [Steps]
**You should work along to the following steps:**
1. Parse version from lock, validate inputs. This identifies the version with all inputs verified.
2. Extract information from source documents. This gathers all necessary content for the completion report.
3. Generate completion report using template. This creates the comprehensive project summary.
4. Create archive directory, move files (preserve architecture/, knowledge/, completion-report.md). This archives files successfully.
5. Update references, clean requirement-specific content from preserved docs. This prepares the workspace for the next cycle.

## [Instructions]

### 1. Version Parsing and Input Validation
Parse the exact version number from the lock file using format `x.x.x` (semantic versioning). Never guess or fabricate version numbers. If the lock file is missing or corrupted, halt execution and request user intervention.

Validate that all required source documents exist:
- Check for dev-notes files in `{DEVNOTES}/` or `{root}/docs/prd-dev-notes.md`
- Look for review reports in `{REVIEW}/`
- Check for cutover reports
- Verify architecture documents exist in `{root}/docs/architecture/` or `{root}/docs/architecture.md`

### 2. Information Extraction from Source Documents
Extract key information systematically from different document types:

**From Development Notes (`*-dev-notes.md`):**
- Key technical decisions made during implementation
- Challenges encountered and solutions applied
- Technology choices and rationale
- Evidence of implementation (file paths, line numbers)
- Technical debt and known issues

**From Review Reports (`*-review.md`):**
- Quality issues identified and resolved
- Test coverage and results
- Performance metrics and improvements
- Best practices discovered

**From Cutover Reports:**
- Business acceptance outcomes
- Configuration requirements
- Production readiness status
- User-facing functionality verification

**From Architecture Documents:**
- Architecture Decision Records (ADRs)
- System design patterns used
- Component integration approaches
- Cross-cutting concerns addressed

**Extraction Focus:**
- Look for specific evidence: file paths, line numbers, test results, metrics
- Identify patterns across multiple tasks/documents
- Connect technical decisions to business requirements
- Gather quantifiable outcomes (test counts, coverage percentages, performance metrics)

### 3. Completion Report Generation
Use the completion-report template to structure findings. The template provides comprehensive guidance for formatting and required sections. Focus on populating template sections with extracted evidence rather than creating custom formats.

### 4. Archive Workflow
Create systematic archive of project deliverables:

**Archive Structure:**
- Create directory: `{ARCHIVE}/{version_name}/`
- **Move to archive:** PRD, requirements, epic, implementation plans, dev-notes, reviews, cutover reports
- **Preserve in place:** `architecture/`, `knowledge/`, `completion-report.md`

**Archive Process:**
- Maintain directory structure when moving files
- Update any cross-references to archived documents
- Verify all requirement-specific documents are archived
- Confirm preserved documents remain accessible

### 5. Workspace Cleanup
Clean requirement-specific content from preserved documents while maintaining architectural value:

**From Architecture Documents:**
- Remove specific requirement IDs and user stories
- Preserve ADRs, design patterns, and technical decisions
- Keep component definitions and integration patterns
- Maintain technology stack decisions and rationale

**From Knowledge Base:**
- Remove project-specific implementation details
- Preserve reusable patterns and lessons learned
- Keep technology evaluation criteria and outcomes
- Maintain process improvements and best practices

**Verification:**
- Ensure workspace is ready for next development cycle
- Confirm no broken references to archived content
- Validate architectural knowledge is preserved and accessible

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Completion report generated at "{root}/docs/completion-report.md"
- [ ] Version parsed correctly from lock file
- [ ] All source documents validated and information extracted
- [ ] Files archived to "{ARCHIVE}/{version_name}/" (excluding architecture/, knowledge/, completion-report.md)
- [ ] Workspace cleaned of requirement-specific content
- [ ] Cross-references updated, no broken links
