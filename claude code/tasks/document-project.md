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
  4. **context7 (MCP)**
    - [Step 1-2: Search API documentation of existing architecture's technology stack and libraries]

[Steps]
  1. Analysis and Planning Phase
    - Read all existing architecture documents under "{root}/docs/architecture/*.md"
    - Search codebase to understand actual implementation state
    - Read development notes and review reports to capture implementation details
    - Identify gaps between planned architecture and actual implementation
    - Create todo list for architecture documents to update

  2. Update Architecture Documents Phase
    - if architecture documents are missing or do not exist then proceed to 2.1, else proceed to 2.2
      
      2.1. Generate New Architecture Documents
        - Search codebase to understand actual implementation architecture
        - Generate architecture documents according to universal architecture template
        - Run "{root}/sunnycore/scripts/shard-architecture.py" to shard large architecture documents
        - Ensure all generated documents follow template structure and are in .md format
      
      2.2. Update Existing Architecture Documents
        - For each architecture document in "{root}/docs/architecture/*.md", review existing content and identify sections needing updates
        - if document structure does not align with universal architecture template fields then restructure the document to match template structure and rename the file if necessary, else proceed with incremental updates
        - Search codebase for actual implementation details
        - Integrate information from dev-notes and review-reports
        - Update document according to universal architecture template structure
    - Verify document completeness and internal consistency
    - Ensure all documents follow template structure and are in .md format

  3. Finalization Phase
    - Update Document Index section in "{root}/CLAUDE.md" with refreshed architecture documents (including path and purpose of each document)
    - Verify all source references are properly documented
    - Check all DoD items one by one to ensure they are met
    - Confirm all todo items are completed

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
