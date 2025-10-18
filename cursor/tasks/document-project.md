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
- `{root}/CURSOR.mdc` (updated with refreshed index)

## [Constraints]
- **MUST** based on actual implementation, **MUST NOT** based on original design
- **MUST** include source references (source_refs), **MUST NOT** produce content without
- **MUST** delete old architecture docs before sharding, **MUST NOT** skip
- **MUST** update CURSOR.mdc index after sharding, **MUST NOT** skip

## [Instructions]
[Instructions]
1. **Step 1: Reconcile Architecture with Implementation**
- **GOAL:** Achieve a complete understanding of the actual system versus the documented design.
- **STEPS:**
  - Review relevant `{ARCH}/*.md`, `{KNOWLEDGE}/*.md`, and `{PROGRESS}` entries to capture recorded intent and context.
  - Analyze codebase components, data flows, and technology usage to confirm what is truly implemented.
  - Capture divergences and supporting rationale from `{DEVNOTES}/*.md`, `{REVIEW}/*.md`, and other evidence sources.
- **QUESTIONS:**
  - Which components or flows differ between the documented architecture and the running implementation?
  - What code or records verify each current technology choice and integration?
  - Why did each identified drift occur, and where is the rationale recorded?
  - Are there undocumented components or behaviors that must be surfaced?
- **CHECKLIST:**
  - [ ] Relevant architecture, knowledge, and progress materials reviewed
  - [ ] Actual implementations mapped to candidate source references
  - [ ] Drifts and rationales captured for later documentation

2. **Step 2: Build Unified architecture.md with Evidence**
- **GOAL:** Produce an evidence-backed `docs/architecture.md` that reflects the live system.
- **STEPS:**
  - Structure the document using required sections (components, data flows, ADRs, deviations) from `{TMPL}/architecture-tmpl.yaml`.
  - Gather precise `[source: path:line]` references from code, dev notes, reviews, and knowledge files for every statement.
  - Draft the unified narrative so all content mirrors actual implementation and noted drifts.
- **QUESTIONS:**
  - Does every component or integration include an evidence-backed source reference?
  - Are all ADRs linked to decisions in dev notes or review records?
  - Have deviations from the original design been explained with rationale and evidence?
  - Is any required section from the template missing or under-detailed?
- **CHECKLIST:**
  - [ ] Components, data flows, ADRs, and deviations documented
  - [ ] Every claim includes a ready source reference
  - [ ] Content reflects current implementation rather than legacy design

3. **Step 3: Shard Architecture Documentation**
- **GOAL:** Generate clean architecture shards derived from the unified source.
- **STEPS:**
  - Delete existing `{ARCH}/*.md` files to eliminate stale shards.
  - Run `python {SCRIPTS}/shard-architecture.py {root}/docs/architecture.md {ARCH}/` to produce fresh shards.
  - Inspect each generated shard to ensure structure, references, and cross-links remain accurate.
- **QUESTIONS:**
  - Were all legacy architecture files removed before sharding?
  - Did the sharding script complete without errors and output the expected files?
  - Do the new shards preserve source references and navigability?
  - Is any additional cleanup or regeneration required after sharding?
- **CHECKLIST:**
  - [ ] Legacy architecture files removed
  - [ ] Sharding script executed successfully
  - [ ] Sharded documents validated for accuracy and references

4. **Step 4: Refresh CURSOR.mdc Index**
- **GOAL:** Update `CURSOR.mdc` so it accurately indexes the sharded architecture set.
- **STEPS:**
  - Enumerate the generated architecture shards and summarize their focus areas.
  - Update the architecture section of `CURSOR.mdc` with file listings, brief descriptions, and refreshed timestamp.
  - Verify the index aligns with actual file paths and highlights key components and decisions.
- **QUESTIONS:**
  - Does the updated index list every architecture shard with accurate summaries?
  - Is the "Last Updated" metadata current and aligned with this documentation pass?
  - Are cross-references or navigation notes still correct after the update?
  - Is additional follow-up needed to keep the index synchronized with future changes?
- **CHECKLIST:**
  - [ ] All architecture files listed with concise descriptions
  - [ ] Metadata and timestamps refreshed
  - [ ] Index references match actual files and structure

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Architecture sharded to "{ARCH}/" with source references (format: file_path:line_number)
- [ ] All deviations from original design documented with rationale
- [ ] CURSOR.mdc updated with current architecture index

## [Example]

### Good #1
**Input**: Outdated architecture exists. Codebase changed from sync to async payment. Dev notes document decision  
**Decision**: Read existing arch. Analyze codebase (OrderService.js, PaymentGateway.js). Identify drift: sync→async payment. Extract rationale from dev notes (ADR-005: async for scalability). Create unified architecture.md with actual async implementation, source refs (OrderService.js:L20-L45, dev-notes/3-dev-notes.md [Payment Decision]). Delete old arch files. Shard to components.md, data-flows.md, decisions.md. Update CURSOR.mdc index.  
**Why Good**: This reconciles with living codebase, records rationale, and performs full workflow (sharding, indexing, cleanup).

### Good #2
**Input**: No existing architecture (greenfield just completed). Codebase has device registry, telemetry, dashboard. Dev notes have 8 tasks with decisions. Reviews document optimizations  
**Decision**: Analyze codebase structure (device-registry/, telemetry/, dashboard/). Extract decisions from dev notes (ADR-001: Kafka over RabbitMQ). Gather context from reviews (performance patterns). Create architecture.md from scratch based on actual implementation. Document components, data flows, ADRs with source refs (telemetry/TelemetryIngester.js:L5-L80, dev-notes/2-dev-notes.md [Kafka Decision]). Shard successfully. Create CURSOR.mdc with index.  
**Why Good**: This builds from real implementation evidence and delivers every artifact with references.

### Bad #1
**Input**: Existing arch describes sync payment. Actual codebase implements async  
**Bad Decision**: Read existing arch. Update by copying most content verbatim. Keep original sync description because arch doc says so. Add small note mentioning async exists. Don't verify with codebase.  
**Why Bad**: This violates constraint (must base on actual implementation). Architecture must reflect actual state, not original design. This keeps outdated sync description and misleads developers.  
**Correct**: Analyze actual codebase FIRST. Document what's actually implemented (async payment), not original design (sync). Reference actual code with source_refs (OrderService.js:L20-L45). Document drift in ADR with rationale. Architecture must match reality.
