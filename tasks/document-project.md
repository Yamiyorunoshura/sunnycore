**GOAL**: Update or create comprehensive project architecture documentation.

## [Input]
  1. "{ARCH}/*.md" --Existing architecture documents
  2. "{TMPL}/architecture-tmpl.yaml" --Universal architecture document template
  3. "{KNOWLEDGE}/*.md" --Knowledge base
  4. "{PROGRESS}" --Progress record
  5. "{DEVNOTES}/*.md" --Development notes
  6. "{REVIEW}/*.md" --Review reports
  7. Actual codebase
  8. "{TMPL}/plan-tmpl.yaml" --Unified planning template; emphasize codebase evidence collection, sharding checkpoints, and CLAUDE.md updates for this task

## [Output]
  1. "{root}/docs/architecture.md" --Integrated architecture document (Markdown format)(temporary, will be sharded)
  2. "{ARCH}/*.md" --Sharded architecture documents (Markdown format)
  3. "{root}/CLAUDE.md" --Updated project guidance document with refreshed document index
  4. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking
  
## [Constraints]
  1. Do not base updates on original design (must use actual implementation state)
  2. Do not produce content without source references (source_refs)
  3. Do not skip deleting old architecture documents before sharding
  4. Do not skip updating CLAUDE.md Document Index after sharding

## [Steps]
  1. Analysis & Context Gathering
    - Understand existing architecture and actual implementation state
    - Gather comprehensive context from all documentation sources
    - Create plan.md at "{root}/docs/plan.md" using the plan template to log evidence sources, drift analysis, and sharding/CLAUDE update checkpoints
    - Outcome: Complete understanding of current state, context gathered, and plan.md initialized

  2. Architecture Integration & Documentation
    - Create unified architecture document at "{root}/docs/architecture.md"
    - Include proper source references (source_refs) for all content
    - Ensure completeness and internal consistency
    - Outcome: Complete unified architecture document

  3. Cleanup & Sharding
    - Remove old architecture documents from "{ARCH}/"
    - Run sharding script with verified output
    - Verify all sharded documents created properly
    - Outcome: Successfully sharded architecture in "{ARCH}/*.md"

  4. Finalization & Index Update
    - Update "{root}/CLAUDE.md" with refreshed architecture index
    - Verify all source references properly documented
    - Outcome: CLAUDE.md updated with current architecture index


## [Documentation-Guidelines]
  1. **Base on Actual Implementation**
    - Update architecture based on actual codebase state, not original design
    - Document architecture drift and deviations with rationale
    - Use source references (source_refs) for all statements (format: file_path:line_number)
  
  2. **Template Compliance & Completeness**
    - Follow universal architecture template structure
    - Include all necessary sections: overview, components, data flows, ADRs
    - Maintain consistent terminology and naming conventions
  
  3. **Decision & Change Tracking**
    - Record key decisions with context, rationale, and trade-offs
    - Document technical choices with pros/cons analysis
    - Track issues encountered with root cause and solutions
  
  4. **Integration & Synchronization**
    - Consolidate information from dev notes, reviews, knowledge base, and codebase
    - Ensure alignment between documentation and actual implementation
    - Update CLAUDE.md document index after sharding

## [DoD]
  - [ ] Architecture successfully sharded to "{ARCH}/" with all content including source references by running the scripts (format: file_path:line_number)
  - [ ] All deviations from original design documented with clear rationale
  - [ ] CLAUDE.md updated with current architecture document index

## [Example]

### Good Example 1
[INPUT]
Existing outdated architecture documents exist. Codebase shows actual implementation changed from synchronous to async payment processing. Dev notes document the decision rationale. Reviews confirm architecture drift.

[DECISION]
Read existing architecture docs to understand baseline. Analyze actual codebase (src/services/OrderService.js, PaymentGateway.js) to understand current state. Identify architecture drift: synchronous payment changed to async. Extract decision rationale from dev notes (ADR-005: async for better scalability). Create unified architecture.md documenting actual implementation with source references (src/services/OrderService.js:L20-L45, docs/dev-notes/3-dev-notes.md [Payment Decision]). Delete old architecture files. Run sharding script to generate docs/architecture/*.md. Update CLAUDE.md Document Index with new architecture file list.

[OUTCOME]
Complete architecture.md at docs/architecture.md documenting actual async payment implementation. Successfully sharded to docs/architecture/components.md, data-flows.md, decisions.md. All content includes source references (file_path:line_number). Architecture drift documented with rationale: moved to async for scalability. CLAUDE.md updated with current architecture index. Old outdated documents removed. Plan.md shows codebase analysis complete, sharding successful, index updated.

[WHY-GOOD]
- Reconciles documentation with the living codebase, eliminating drift and recording rationale.
- Performs the full documentation workflow—sharding, indexing, cleanup—so consumers get authoritative artifacts.

### Good Example 2
[INPUT]
No existing architecture (greenfield project just completed). Codebase has device registry, telemetry pipeline, dashboard fully implemented. Dev notes contain 8 tasks with multiple architecture decisions. Reviews document performance optimizations.

[DECISION]
Analyze codebase structure to extract component boundaries (src/device-registry/, src/telemetry/, src/dashboard/). Extract architecture decisions from dev notes (ADR-001: Kafka selected over RabbitMQ for message broker). Gather context from reviews (performance optimization patterns). Create architecture.md from scratch based on actual implementation. Document all components, data flows, and ADRs with source references (src/telemetry/TelemetryIngester.js:L5-L80, docs/dev-notes/2-dev-notes.md [Kafka Decision]). Shard to multiple architecture documents. Create CLAUDE.md with architecture index.

[OUTCOME]
Complete architecture.md created documenting entire IoT platform architecture. Sharded to docs/architecture/overview.md, components.md, data-flows.md, decisions.md. All ADRs extracted from dev notes with proper source references. CLAUDE.md created with architecture document index and tech stack summary. Plan.md shows all components documented, decisions extracted, sharding completed, references validated.

[WHY-GOOD]
- Builds documentation from real implementation evidence, ensuring accuracy for a new system.
- Delivers every required artifact with references, giving future teams a reliable starting point.

### Bad Example 1
[INPUT]
Existing architecture documents describe synchronous payment. Actual codebase implements async payment. Dev notes explain the change rationale.

[BAD-DECISION]
Read existing architecture documents and update them by copying most content verbatim. Keep the original synchronous payment description because the architecture document says so. Add a small note mentioning async payment exists. Do not verify with actual codebase.

[WHY-BAD]
Violates Constraint 1 (do not base updates on original design). Architecture must reflect actual implementation state, not original design. Keeping outdated synchronous description misleads future developers. Not verifying with codebase violates Documentation-Guidelines principle of basing on actual implementation. Creates inaccurate documentation.

[CORRECT-APPROACH]
Analyze actual codebase FIRST to understand current implementation state. Document what is actually implemented (async payment), not what was originally designed (synchronous). Reference actual code with source_refs (src/services/OrderService.js:L20-L45). Document the drift in ADR section with rationale from dev notes. Architecture must always match reality of codebase.

### Bad Example 2
[INPUT]
Architecture documentation completed. Sharding script run successfully. Old architecture files still exist in docs/architecture/. CLAUDE.md not updated with new architecture index.

[BAD-DECISION]
Leave old architecture files in place alongside new sharded files. Skip updating CLAUDE.md because the architecture documents exist anyway. Reasoning: "Having more documentation is better, even if some is outdated."

[WHY-BAD]
Violates Constraint 3 (do not skip deleting old architecture documents before sharding). Leaving old files creates confusion about which architecture is current. Multiple versions of truth contradict each other. Violates Constraint 4 (do not skip updating CLAUDE.md). CLAUDE.md serves as index - must be current. Incomplete task execution.

[CORRECT-APPROACH]
Delete ALL old architecture documents from docs/architecture/ BEFORE running sharding script per Constraint 3. After sharding completes, update CLAUDE.md Document Index with the new architecture file list per Constraint 4. Verify sharded files are complete before deleting originals. Ensure only one current version of architecture exists. CLAUDE.md must always reference the current document structure.
