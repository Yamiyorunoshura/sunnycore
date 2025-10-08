**GOAL**: Summarize project development outcomes and generate comprehensive delivery report.

## [Input]
  1. "{root}/docs/*.md" --All files in docs/ directory recursively (required)
  2. "{LOCK}" --Version information (required)
  3. "{TMPL}/completion-report-tmpl.yaml" --Completion report template (required)

## [Output]
  1. Completion report: "{root}/docs/completion-report.md" (Markdown format)

## [Constraints]
  1. Must ensure completion report complies with template requirements
  2. Completion report must include the following core content:
    (1) All key decisions and their rationale
    (2) Technology choices and alternative solution comparisons
    (3) Problems encountered, root cause analysis, and solutions
    (4) Future recommendations
    (5) DoD verification evidence (format as "file path:line number", e.g., "src/main.py:L42-L56")
  3. If required input files (sunnycore.lock, template) are missing or incorrectly formatted, must generate a missing file list in the terminal and halt execution, waiting for user to provide supplementary files
  4. If any of the 5 core content items are completely missing from source documents, should annotate "To be supplemented: missing XX item" in the corresponding chapter of the completion report and continue execution
  5. Version name must be parsed from sunnycore.lock file (format: "version = x.x.x")
  6. When archiving files, must preserve docs/architecture/, docs/knowledge/, and docs/completion-report.md in their original locations

## [Tools]
  1. **todo_write**: Create and manage task list
    - [Step 1: Create todo list; Steps 2-7: Track task progress]
  2. **sequentialthinking (MCP)**: Perform structured reasoning and verification
    - [Step 2: Reasoning tasks for conceiving the report; Step 3: Verify if DoD is satisfied]
  3. **claude-context (MCP)**: Search codebase to locate implementation details
    - [Step 2: Find relevant code; Step 3: Precise keyword search]
    - Prerequisite: Codebase has been indexed through index_codebase
    - Failure handling: If not indexed or search fails, switch to grep tool for keyword search, or annotate "Unable to locate code evidence" and continue execution

## [Steps]
  1. Input Validation Phase
    - Ensure version number is parsed from lock file
    - Ensure all required input files exist and are valid
    - Establish progress tracking mechanism for conclusion tasks

  2. Information Extraction and Mapping Phase
    - Achieve complete extraction of all 5 core content items
    - Ensure proper mapping to template fields
    - Ensure code evidence is supplemented where needed

  3. Write Report Phase
    - Achieve complete completion report at "{root}/docs/completion-report.md"
    - Ensure all sections follow template structure

  4. Quality Check Phase
    - Ensure report meets template requirements with complete structure
    - Ensure all 5 core content items are clearly presented
    - Ensure proper handling of deficiencies with iterative fixes

  5. Create Archive Directory Phase
    - Ensure archive directory "{ARCHIVE}/{version_name}/" is created and verified

  6. Move Files to Archive Phase
    - Ensure proper file archiving with architecture/, knowledge/, and completion-report.md preserved
    - Ensure verification of archive operations with proper error handling

  7. Update Document References Phase
    - Ensure all document references are updated to point to correct archive paths
    - Ensure reference updates are verified for correctness

## [Completion-Report-Guidelines]
  1. **Core Content (5 Required Items)**
    - **Decisions**: Key decisions with rationale, context, and trade-offs
    - **Technical Choices**: Technology selection with pros/cons and alternatives
    - **Issues & Solutions**: Problems encountered, root cause, solutions, preventive measures
    - **Evidence**: Verifiable evidence for all statements (format: file_path:line_number)
    - **Recommendations**: Future improvements and optimization directions
  
  2. **Traceability & Verification**
    - Link all statements to actual code, test results, or document sections
    - Use DoD verification evidence format: "file_path:Lstart-Lend"
    - If any core item missing from sources, annotate "To be supplemented: missing XX item"
  
  3. **Version & Archiving**
    - Parse version from sunnycore.lock file (format: "version = x.x.x")
    - Archive all docs to "{ARCHIVE}/{version_name}/" except architecture/, knowledge/, completion-report.md
    - Update references in preserved docs to point to archive paths

## [DoD]
  - [ ] *.lock file has been read and version number has been parsed successfully
  - [ ] Workflow type (Traditional/PRD) has been determined
  - [ ] All files in docs/ directory have been scanned recursively
  - [ ] Completion report has been generated and complies with template structure (including all necessary sections in the template)
  - [ ] Completion report content fully covers the 5 core content items listed in constraint 2
  - [ ] All files and directories in docs/ EXCEPT architecture/, knowledge/, and completion-report.md have been moved to {ARCHIVE}/{version_name}/
  - [ ] Only architecture/, knowledge/, and completion-report.md remain in docs/ directory
  - [ ] Document references in architecture/ and knowledge/ have been updated to point to correct archive paths

## [Example]

### Example 1: E-commerce Feature Completion
[Input]
- Lock file: sunnycore.lock (version = 1.2.0)
- Documents: docs/PRD.md, docs/prd-dev-notes.md, docs/cutover-report.md
- Template: completion-report-tmpl.yaml

[Decision]
- Version: 1.2.0 (parsed from lock file)
- Workflow: PRD (PRD.md exists)
- Extract: Key decisions (async payment processing - ADR-003), tech choices (Stripe over PayPal), issues (rate limit bug fixed), evidence (src/services/PaymentService.js:L42-L56)
- Archive: Move PRD.md, prd-dev-notes.md, cutover-report.md to docs/archive/1.2.0/

[Expected Outcome]
- docs/completion-report.md with all 5 core items (decisions, tech choices, issues/solutions, evidence, recommendations)
- docs/archive/1.2.0/ contains PRD.md, dev-notes, cutover-report.md
- docs/ only has architecture/, knowledge/, completion-report.md
- References updated: knowledge/best-practices.md now references docs/archive/1.2.0/prd-dev-notes.md

### Example 2: Microservices Migration Project
[Input]
- Lock file: sunnycore.lock (version = 2.0.0)
- Documents: docs/requirements/*.md, docs/architecture/*.md, docs/epic.md, docs/plans/*.md, docs/dev-notes/*.md (8 tasks), docs/review/*.md
- Template: completion-report-tmpl.yaml

[Decision]
- Version: 2.0.0 (major version, architecture change)
- Workflow: Traditional/Full (epic.md, plans/ exist)
- Extract: Decisions (strangler fig pattern - ADR-001), tech choices (gRPC for inter-service communication), issues (data migration challenges), evidence (src/services/OrderService/server.js:L10-L80)
- Archive: Move requirements/, plans/, dev-notes/, review/, epic.md to docs/archive/2.0.0/

[Expected Outcome]
- docs/completion-report.md documenting microservices migration journey
- All 5 core items covered with detailed evidence from codebase
- docs/archive/2.0.0/ contains all project artifacts except architecture/ and knowledge/
- architecture/components.md references updated to point to archive for historical decisions
