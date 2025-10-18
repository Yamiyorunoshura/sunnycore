**GOAL**: Update or create comprehensive project architecture documentation.

## [Context]
**You must read the following context:**
- `{ARCH}/*.md`(Only the related documents)
- `{TMPL}/architecture-tmpl.yaml`
- `{KNOWLEDGE}/*.md`
- `{PROGRESS}`
- `{DEVNOTES}/*.md`
- `{REVIEW}/*.md`
- Actual codebase

## [Products]
- `{root}/docs/architecture.md` (temporary, will be sharded)
- `{ARCH}/*.md`(Only the related documents)
- `{root}/CLAUDE.md` (updated with refreshed index)

## [Constraints]
- **MUST** based on actual implementation, **MUST NOT** based on original design
- **MUST** include source references (source_refs), **MUST NOT** produce content without
- **MUST** delete old architecture docs before sharding, **MUST NOT** skip
- **MUST** update CLAUDE.md index after sharding, **MUST NOT** skip

## [Instructions]
[Instructions]
1. **Step 1: Reconcile Architecture with Implementation**
- **GOAL:** Build an evidence-backed understanding of how the real system differs from the recorded design.
- **STEPS:**
  - Review relevant `{ARCH}/*.md`, `{KNOWLEDGE}/*.md`, and `{PROGRESS}` documents to collect intent, scope, and historical notes.
  - Examine the codebase to map actual components, data flows, integrations, and technology usage.
  - Capture every drift, rationale, and supporting citation from `{DEVNOTES}/*.md`, `{REVIEW}/*.md`, and other trusted records.
- **QUESTIONS:**
  - Which components or flows in production behavior diverge from the documented architecture?
  - What specific files or records confirm each current implementation detail?
  - Why did each drift occur, and where is that rationale documented?
  - Are there undocumented behaviors that must be added to the architecture?
- **CHECKLIST:**
  - [ ] Relevant architecture, knowledge, and progress sources reviewed
  - [ ] Actual implementations mapped with candidate source references
  - [ ] Drift summaries and rationales logged for documentation

2. **Step 2: Build Unified architecture.md with Evidence**
- **GOAL:** Author `{root}/docs/architecture.md` that reflects reality and cites sources for every statement.
- **STEPS:**
  - Structure the document using required sections from `{TMPL}/architecture-tmpl.yaml` (components, data flows, ADRs, deviations).
  - Draft content so each assertion includes `[source: file_path:line_number]` or `[source: file_path [Section]]` citations.
  - Highlight how implementation satisfies or diverges from original intent using the evidence gathered.
- **QUESTIONS:**
  - Does every component, flow, and decision include a verified source reference?
  - Are ADRs connected to concrete decisions in dev notes or review artifacts?
  - Have deviations from the original design been explained with rationale?
  - Is any required template section incomplete or unsupported?
- **CHECKLIST:**
  - [ ] Components, data flows, ADRs, and deviations documented per template
  - [ ] All claims linked to precise source references
  - [ ] Narrative aligned with current implementation, not legacy design

3. **Step 3: Shard Architecture Documentation**
- **GOAL:** Regenerate `{ARCH}/*.md` shards directly from the unified source without stale content.
- **STEPS:**
  - Remove existing `{ARCH}/*.md` files to eliminate outdated shards.
  - Run `python {SCRIPTS}/shard-architecture.py {root}/docs/architecture.md {ARCH}/` to create the new shard set.
  - Inspect each shard for structure accuracy, preserved references, and correct cross-links.
- **QUESTIONS:**
  - Were the legacy shards cleared before regeneration started?
  - Did the sharding script finish successfully and output the expected files?
  - Do the refreshed shards retain all source references and navigation cues?
  - Is any additional cleanup required after sharding?
- **CHECKLIST:**
  - [ ] Legacy architecture files removed ahead of sharding
  - [ ] Sharding script executed without errors
  - [ ] Generated shards validated for structure and references

4. **Step 4: Refresh CLAUDE.md Index**
- **GOAL:** Update `{root}/CLAUDE.md` to accurately index the regenerated architecture shards.
- **STEPS:**
  - List the new `{ARCH}/*.md` files and summarize the focus of each shard.
  - Update the architecture section in `CLAUDE.md` with file names, concise descriptions, and an up-to-date timestamp.
  - Confirm navigation cues and cross-references align with the refreshed shard layout.
- **QUESTIONS:**
  - Does the index cover every shard with a clear summary?
  - Is the "Last Updated" value aligned with this documentation pass?
  - Do all references in `CLAUDE.md` point to actual file paths?
  - Are follow-up tasks needed to keep the index synchronized?
- **CHECKLIST:**
  - [ ] Architecture shard listings refreshed with accurate summaries
  - [ ] Metadata and timestamps updated
  - [ ] Index references verified against actual files

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Architecture sharded to "{ARCH}/" with source references (format: file_path:line_number)
- [ ] All deviations from original design documented with rationale
- [ ] CLAUDE.md updated with current architecture index

## [Example]

### Good #1
**Input**: Outdated architecture exists. Codebase changed from sync to async payment. Dev notes document decision  
**Decision**: Read existing arch. Analyze codebase (OrderService.js, PaymentGateway.js). Identify drift: sync→async payment. Extract rationale from dev notes (ADR-005: async for scalability). Create unified architecture.md with actual async implementation, source refs (OrderService.js:L20-L45, dev-notes/3-dev-notes.md [Payment Decision]). Delete old arch files. Shard to components.md, data-flows.md, decisions.md. Update CLAUDE.md index.  
**Why Good**: This reconciles with living codebase, records rationale, and performs full workflow (sharding, indexing, cleanup).

### Good #2
**Input**: No existing architecture (greenfield just completed). Codebase has device registry, telemetry, dashboard. Dev notes have 8 tasks with decisions. Reviews document optimizations  
**Decision**: Analyze codebase structure (device-registry/, telemetry/, dashboard/). Extract decisions from dev notes (ADR-001: Kafka over RabbitMQ). Gather context from reviews (performance patterns). Create architecture.md from scratch based on actual implementation. Document components, data flows, ADRs with source refs (telemetry/TelemetryIngester.js:L5-L80, dev-notes/2-dev-notes.md [Kafka Decision]). Shard successfully. Create CLAUDE.md with index.  
**Why Good**: This builds from real implementation evidence and delivers every artifact with references.

### Bad #1
**Input**: Existing arch describes sync payment. Actual codebase implements async  
**Bad Decision**: Read existing arch. Update by copying most content verbatim. Keep original sync description because arch doc says so. Add small note mentioning async exists. Don't verify with codebase.  
**Why Bad**: This violates constraint (must base on actual implementation). Architecture must reflect actual state, not original design. This keeps outdated sync description and misleads developers.  
**Correct**: Analyze actual codebase FIRST. Document what's actually implemented (async payment), not original design (sync). Reference actual code with source_refs (OrderService.js:L20-L45). Document drift in ADR with rationale. Architecture must match reality.
