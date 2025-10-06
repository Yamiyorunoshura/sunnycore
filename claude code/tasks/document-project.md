[Input]
  1. "{root}/docs/architecture/*.md" --Existing architecture documents
  2. "{root}/sunnycore/templates/architecture-tmpl.yaml" --Universal architecture document template
  3. "{root}/docs/knowledge/*.md" --Knowledge base
  4. "{root}/docs/progress.md" --Progress record
  5. "{root}/docs/dev-notes/*.md" --Development notes
  6. "{root}/docs/review-results/*.md" --Review reports
  7. Actual codebase

[Output]
  1. "{root}/docs/architecture.md" --Integrated architecture document (temporary, will be sharded)
  2. "{root}/docs/architecture/*.md" --Sharded architecture documents (Markdown format)
  3. "{root}/CLAUDE.md" --Updated project guidance document with refreshed document index

[Constraints]
  1. Must base updates on actual implementation state from codebase, development notes, and review reports
  2. Every produced document must correspond to at least 1 source reference (source_refs)
  3. Can include architecture diagrams in Markdown documents as fenced code blocks
  4. All sharded file paths must be under "docs/architecture/" with .md extension
  5. Must update the Document Index section in "{root}/CLAUDE.md" after sharding architecture documents
  6. The integrated architecture.md must follow the universal architecture template structure

[Tools]
  1. **todo_write**
    - [Step 1: Create task list; Steps 2-4: Track task progress]
  2. **sequentialthinking (MCP)**
    - [Step 2: Reasoning tasks for content integration and unified document writing]
  3. **claude-context (MCP)**
    - [Step 1-2: Search codebase for actual implementation details]
  4. **context7 (MCP)**
    - [Step 1-2: Search API documentation of existing architecture's technology stack and libraries]

[Steps]
  1. Analysis and Planning Phase
    - Read all existing architecture documents under "{root}/docs/architecture/*.md"
    - Search codebase to understand actual implementation state
    - Read development notes and review reports to capture implementation details
    - Read knowledge base for domain context
    - Create todo list for architecture document generation

  2. Integration Phase - Create Unified Architecture Document
    - Search codebase for actual implementation architecture details
    - Integrate information from [input]
    - Generate markdon format unified "{root}/docs/architecture.md" according to the universal architecture template
    - Ensure all content includes proper source references (source_refs)
    - Verify document completeness and internal consistency

  3. Cleanup and Sharding Phase
    - Delete all existing architecture documents under "{root}/docs/architecture/*.md"
    - Run "{root}/sunnycore/scripts/shard-architecture.py" to shard the unified architecture.md
    - Verify all sharded documents are properly created in .md format

  4. Finalization Phase
    - Update Document Index section in "{root}/CLAUDE.md" with refreshed architecture documents (including path and purpose of each document)
    - Verify all source references are properly documented across sharded files
    - Check all DoD items one by one to ensure they are met
    - Confirm all todo items are completed

[DoD]
  - [ ] All existing architecture documents have been read
  - [ ] Codebase has been searched to understand actual implementation
  - [ ] Development notes, review reports, knowledge base, and progress records have been reviewed
  - [ ] Task list has been created and all items are marked as completed
  - [ ] All content includes proper source references (source_refs)
  - [ ] Old architecture documents have been deleted from "docs/architecture/"
  - [ ] Shard-architecture.py script has been executed successfully
  - [ ] Sharded architecture documents are properly created in "docs/architecture/" with .md extension
  - [ ] Original architecture.md has been deleted by the sharding script
  - [ ] Each sharded document includes actual implementation details with source references
  - [ ] Deviations from original design are documented with rationale
  - [ ] "{root}/CLAUDE.md" Document Index section has been updated with refreshed sharded architecture documents
  - [ ] All todo items are completed
