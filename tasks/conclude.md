**GOAL**: Summarize project development outcomes and generate comprehensive delivery report.

## [Input]
  1. "{root}/docs/*.md" --All files in docs/ directory recursively (required)
  2. "{LOCK}" --Version information (required)
  3. "{TMPL}/completion-report-tmpl.yaml" --Completion report template (required)
  4. "{TMPL}/plan-tmpl.yaml" --Unified planning template; tailor sections to capture version analysis, report assembly, and archiving steps

## [Output]
  1. Completion report: "{root}/docs/completion-report.md" (Markdown format)
  2. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not omit any of the 5 core content items (decisions, tech choices, issues/solutions, evidence, recommendations)
  2. Do not incorrectly parse or miss version number from lock file
  3. Do not move architecture/, knowledge/, or completion-report.md during archiving
  4. Do not proceed if required input files are missing (must list missing files and halt)
  5. Do not remove architectural decisions or technical knowledge when cleaning requirements—only remove requirement-specific content (acceptance criteria, functional requirements, version-specific features)

## [Steps]
  1. Input Validation & Setup
    - Parse version number from lock file
    - Validate all required input files exist
    - Create comprehensive plan.md at "{root}/docs/plan.md" using the plan template to track the working progress
    - Outcome: All inputs validated, version identified, and plan.md initialized

  2. Information Extraction & Mapping
    - Extract all 5 core content items (decisions, tech choices, issues/solutions, evidence, recommendations)
    - Map extracted information to template fields
    - Supplement code evidence where needed
    - Outcome: Complete information extraction with proper mapping

  3. Report Generation & Quality Check
    - Write complete completion report at "{root}/docs/completion-report.md"
    - Verify report meets template requirements
    - Ensure all 5 core content items are clearly presented
    - Outcome: High-quality completion report generated

  4. Archive Preparation
    - Create archive directory "{ARCHIVE}/{version_name}/"
    - Verify directory creation successful
    - Outcome: Archive directory ready for file migration

  5. File Archiving & Reference Updates
    - Move files to archive (preserve architecture/, knowledge/, completion-report.md)
    - Update document references to point to archive paths
    - Verify all operations successful
    - Outcome: Files archived and references updated correctly

  6. Requirements Cleanup for Next Development Cycle
    - Remove all requirement-related content from active documents
    - Clean requirement sections from architecture/ documents
    - Clear requirement references from knowledge/ documents
    - Reset project for next development iteration
    - Outcome: Clean workspace ready for next development cycle

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
    - Parse version from *.lock file (format: "version = x.x.x")
    - Archive all docs to "{ARCHIVE}/{version_name}/" except architecture/, knowledge/, completion-report.md
    - Update references in preserved docs to point to archive paths
  
  4. **Requirements Cleanup**
    - Remove requirement-specific sections from architecture/ documents (e.g., functional requirements, acceptance criteria tied to current version)
    - Clean requirement references from knowledge/ documents
    - Preserve only architectural decisions and technical knowledge base
    - Ensure workspace is clean and ready for next development cycle

## [DoD]
  - [ ] Completion report generated at "{root}/docs/completion-report.md" with all 5 core items (decisions, tech choices, issues/solutions, evidence, recommendations)
  - [ ] All docs/ files EXCEPT architecture/, knowledge/, and completion-report.md moved to "{ARCHIVE}/{version_name}/"
  - [ ] Document references updated to point to correct archive paths
  - [ ] All requirement-related content removed from architecture/ and knowledge/ documents
  - [ ] Workspace cleaned and ready for next development cycle

## [Example]

### Good Example 1
[INPUT]
Lock file shows version = 1.2.0. Found PRD.md, prd-dev-notes.md, cutover-report.md in docs/. Template requires 5 core items: decisions, tech choices, issues/solutions, evidence, recommendations.

[DECISION]
Parse version from lock file. Identify PRD workflow (PRD.md exists). Extract key decisions from dev notes (async payment processing - ADR-003). Extract tech choices (Stripe API selected over PayPal). Extract issues (rate limiting bug in /api/checkout). Gather code evidence (src/services/PaymentService.js:L42-L56). Compile recommendations (add request throttling). Generate completion report. Create archive/1.2.0/ directory. Move PRD.md, dev-notes, cutover-report to archive. Preserve architecture/, knowledge/, completion-report.md in docs/. Remove requirement-related content from active documents.

[OUTCOME]
Complete docs/completion-report.md with all 5 core items fully documented with evidence. Archive docs/archive/1.2.0/ contains PRD.md, prd-dev-notes.md, cutover-report.md. Root docs/ only contains architecture/, knowledge/, completion-report.md. References in knowledge/best-practices.md updated to point to docs/archive/1.2.0/prd-dev-notes.md. All requirement-related content removed from architecture/ and knowledge/ documents.

[WHY-GOOD]
- Follows the archive workflow meticulously—version detection, evidence gathering, and relocation—so historical records stay organized and compliant.
- Updates cross-references after moving files, preventing broken links for future readers.
- Removes version-specific requirements from active documents, preventing confusion in future development cycles.

### Good Example 2
[INPUT]
Lock file shows version = 2.0.0. Found requirements/*.md, architecture/*.md, epic.md, plans/*.md (8 files), dev-notes/*.md (8 files), review/*.md in docs/. This is full workflow project.

[DECISION]
Parse major version 2.0.0 indicating significant architectural changes. Extract decisions from dev-notes (strangler fig pattern - ADR-001, service mesh adoption - ADR-004). Extract tech choices (gRPC for inter-service communication, Kubernetes for orchestration). Extract issues/solutions (data migration challenges solved with dual-write pattern). Collect evidence from codebase (src/services/OrderService/server.js:L10-L80). Generate recommendations (monitoring strategy for distributed services). Create comprehensive completion report. Archive all docs except architecture/, knowledge/, completion-report.md. Clean requirement-specific content from architecture/ and knowledge/ documents to prepare for next development cycle.

[OUTCOME]
Comprehensive docs/completion-report.md documenting microservices migration with all 5 core items. Archive docs/archive/2.0.0/ contains requirements/, plans/, dev-notes/, review/, epic.md. Architecture and knowledge remain in docs/ for ongoing use. All references updated to archive paths. Requirement-specific sections removed from architecture/ documents, preserving only architectural decisions and patterns for future use.

[WHY-GOOD]
- Treats the full workflow with proportional thoroughness, capturing decisions, evidence, and recommendations across artifacts.
- Executes the archival boundaries precisely, preserving active references while relocating completed documents.
- Cleans requirement-specific content from preserved documents, ensuring workspace is ready for next development cycle without legacy requirement confusion.

### Bad Example 1
[INPUT]
Lock file missing or corrupted. Several documents exist in docs/ but version cannot be determined.

[BAD-DECISION]
Guess the version as "1.0.0" and proceed with archiving. Generate completion report without proper version number. Skip validation of required input files.

[WHY-BAD]
Violates Constraint 2 (correctly parse version from lock file). Using guessed version creates confusion and breaks traceability. Proceeding without required inputs violates Constraint 4. Archive structure becomes incorrect.

[CORRECT-APPROACH]
Halt execution immediately. Report error: "Lock file missing or cannot parse version number. Required format: version = x.x.x". List the lock file location expected. Request user to fix lock file before proceeding. Do not guess or fabricate version information.

### Bad Example 2
[INPUT]
All required documents exist. Completion report should include 5 core items. Some items have no supporting evidence in documents.

[BAD-DECISION]
Fabricate evidence for missing items to make the report look complete. For example, invent architectural decisions that were never documented. Generate vague recommendations without specific technical details.

[WHY-BAD]
Violates Constraint 1 (do not omit core content items). Fabricating evidence creates false documentation that misleads future developers. Violates traceability principle where all statements must link to actual code or documents.

[CORRECT-APPROACH]
If core items lack evidence, annotate clearly: "To be supplemented: missing evidence for tech choice rationale" as specified in Completion-Report-Guidelines. Extract only verifiable information from actual documents and code. Generate specific recommendations based on actual issues encountered. Maintain integrity of completion report even if some sections are incomplete.
