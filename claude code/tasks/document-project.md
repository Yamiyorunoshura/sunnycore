**GOAL**: Update or create comprehensive project architecture documentation.

## [Input]
  1. "{ARCH}/*.md" --Existing architecture documents
  2. "{TMPL}/architecture-tmpl.yaml" --Universal architecture document template
  3. "{KNOWLEDGE}/*.md" --Knowledge base
  4. "{PROGRESS}" --Progress record
  5. "{DEVNOTES}/*.md" --Development notes
  6. "{REVIEW}/*.md" --Review reports
  7. Actual codebase

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
    - Establish progress tracking mechanism
    - Outcome: Complete understanding of current state and context

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
  - [ ] Architecture successfully sharded to "{ARCH}/" with all content including source references (format: file_path:line_number)
  - [ ] All deviations from original design documented with clear rationale
  - [ ] CLAUDE.md updated with current architecture document index

## [Example]

### Example 1: E-commerce Order Processing System
[Input]
- Existing architecture: docs/architecture/*.md (outdated, before recent refactoring)
- Codebase: src/ (Order Service, Payment Gateway, Inventory Service)
- Dev notes: docs/dev-notes/*.md (5 tasks completed)
- Reviews: docs/review/*.md (architecture drift documented)
- Template: architecture-tmpl.yaml

[Decision]
- Search codebase for actual implementation (OrderService.js, PaymentGateway.js)
- Update architecture based on actual state (async payment processing added)
- Document architecture drift: Changed from synchronous to async payment (ADR-005)
- Source refs: src/services/OrderService.js:L20-L45, docs/dev-notes/3-dev-notes.md#payment-decision

[Expected Outcome]
- docs/architecture.md with actual implementation state (async payment flow)
- Sharded to docs/architecture/components.md, data-flows.md, decisions.md
- CLAUDE.md Document Index updated with new architecture file list
- All content has source_refs (file_path:line_number format)

### Example 2: Healthcare Patient Portal - Brownfield Update
[Input]
- Existing: docs/architecture/*.md (before adding FHIR integration)
- Codebase: New FHIR adapter in src/integrations/FhirAdapter.py
- Knowledge base: docs/knowledge/best-practices-api-integration.md
- Progress: docs/progress.md (FHIR integration milestones)
- Template: architecture-tmpl.yaml

[Decision]
- Integrate FHIR adapter documentation into existing architecture
- Update component diagram showing FHIR integration point
- Document decision: Why FHIR R4 over R5 (ADR-008)
- Source refs: src/integrations/FhirAdapter.py:L1-L120, docs/knowledge/best-practices-api-integration.md

[Expected Outcome]
- docs/architecture.md updated with FHIR integration architecture
- Old architecture files deleted before sharding
- New shards include FHIR components and integration patterns
- CLAUDE.md updated with FHIR integration documentation references

### Example 3: IoT Platform - Post-Development Documentation
[Input]
- No existing architecture (new project just completed)
- Codebase: Device registry, telemetry pipeline, dashboard (all implemented)
- Dev notes: docs/dev-notes/*.md (8 tasks, multiple architecture decisions)
- Reviews: docs/review/*.md (performance optimizations documented)
- Template: architecture-tmpl.yaml

[Decision]
- Create architecture from scratch based on actual implementation
- Extract component boundaries from codebase structure (src/device-registry/, src/telemetry/)
- Document key decisions from dev notes (Kafka vs RabbitMQ choice - ADR-001)
- Source refs: src/telemetry/TelemetryIngester.js:L5-L80, docs/dev-notes/2-dev-notes.md#kafka-decision

[Expected Outcome]
- docs/architecture.md created with complete system architecture
- Sharded to overview.md, components.md, data-flows.md, decisions.md
- All ADRs extracted from dev notes with proper source references
- CLAUDE.md created with architecture index and tech stack overview
