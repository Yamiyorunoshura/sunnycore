[Input]
  1. "{root}/docs/architecture/*.md" --Existing architecture documents
  2. "{root}/sunnycore/templates/architecture-tmpl.yaml" --Universal architecture document template
  3. "{root}/docs/knowledge/*.md" --Knowledge base
  4. "{root}/docs/progress.md" --Progress record
  5. "{root}/docs/dev-notes/*.md" --Development notes
  6. "{root}/docs/review-results/*.md" --Review reports
  7. Actual codebase

[Output]
  1. "{root}/docs/architecture/*.md" --Updated architecture documents (Markdown format)
  2. "{root}/CLAUDE.md" --Updated project guidance document with refreshed document index

[Constraints]
  1. Must base updates on actual implementation state from codebase, development notes, and review reports
  2. Every produced document must correspond to at least 1 source reference (source_refs)
  3. Can include architecture diagrams in Markdown documents as fenced code blocks
  4. All file paths must be under "docs/architecture/" with .md extension
  5. Must update the Document Index section in "{root}/CLAUDE.md" after updating architecture documents
  6. Should preserve existing architecture structure while updating with actual implementation details

[Tools]
  1. **todo_write**
    - [Step 1: Create task list; Steps 2-3: Track task progress]
  2. **sequentialthinking (MCP)**
    - [Step 2: Reasoning tasks for content integration and document writing]
  3. **claude-context (MCP)**
    - [Step 1: Search codebase for actual implementation details]

[Steps]
  1. Analysis and Planning Phase
    - Read all existing architecture documents under "{root}/docs/architecture/*.md"
    - Search codebase to understand actual implementation state
    - Read development notes and review reports to capture implementation details
    - Identify gaps between planned architecture and actual implementation
    - Create todo list for architecture documents to update
    - Deliverable: Task list and identified gaps

  2. Update Architecture Documents Phase
    - For each architecture document in "{root}/docs/architecture/*.md":
      * Review existing content and identify sections needing updates
      * Search codebase for actual implementation details
      * Integrate information from dev-notes and review-reports
      * Update document according to universal architecture template structure
      * Add actual implementation details, deviations, and lessons learned
      * Ensure all changes are traceable to source references
    - Verify document completeness and internal consistency
    - Ensure all documents follow template structure and are in .md format
    - Deliverable: Updated architecture documents

  3. Finalization Phase
    - Update Document Index section in "{root}/CLAUDE.md" with refreshed architecture documents (including path and purpose of each document)
    - Verify all source references are properly documented
    - Check all DoD items one by one to ensure they are met
    - Confirm all todo items are completed
    - Deliverable: Updated architecture documentation reflecting actual implementation

[DoD]
  - [ ] All existing architecture documents have been read
  - [ ] Codebase has been searched to understand actual implementation
  - [ ] Development notes and review reports have been reviewed
  - [ ] Task list has been created and all items are marked as completed
  - [ ] All architecture documents have been updated according to universal template
  - [ ] Each updated document includes actual implementation details with source references
  - [ ] All file paths are under "docs/architecture/" with .md extension
  - [ ] Deviations from original design are documented with rationale
  - [ ] "{root}/CLAUDE.md" Document Index section has been updated with refreshed architecture documents
  - [ ] All todo items are completed
