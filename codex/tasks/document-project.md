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
- `{root}/AGENTS.md` (updated with refreshed index)

## [Constraints]
- **MUST** based on actual implementation, **MUST NOT** based on original design
- **MUST** include source references (source_refs), **MUST NOT** produce content without
- **MUST** delete old architecture docs before sharding, **MUST NOT** skip
- **MUST** update AGENTS.md index after sharding, **MUST NOT** skip

## [Instructions]
[Instructions]
1. **Step 1: Reconcile Architecture with Implementation**
- **GOAL:** Establish an evidence-backed understanding of how the live system behaves versus the recorded design.
- **STEPS:**
  - Review relevant `{ARCH}/*.md`, `{KNOWLEDGE}/*.md`, and `{PROGRESS}` entries to capture stated intent and historical context.
  - Inspect the codebase to map components, data flows, integrations, and technology usage as they currently exist.
  - Log every drift, rationale, and supporting reference from `{DEVNOTES}/*.md`, `{REVIEW}/*.md`, and other authoritative sources.
- **QUESTIONS:**
  - Where does the implemented system differ from the documented architecture?
  - Which files or records verify each current component, integration, or technology choice?
  - What rationale explains the drifts you observe, and where is it recorded?
  - Are there undocumented components or behaviors that require fresh coverage?
- **CHECKLIST:**
  - [ ] Relevant architecture, knowledge, and progress materials reviewed
  - [ ] Actual implementations mapped with candidate source references
  - [ ] Drift notes and rationales captured for later documentation

2. **Step 2: Build Unified architecture.md with Evidence**
- **GOAL:** Produce `{root}/docs/architecture.md` that mirrors the actual system and cites sources for every claim.
- **STEPS:**
  - Follow `{TMPL}/architecture-tmpl.yaml` to structure required sections (components, data flows, ADRs, deviations).
  - Draft content so each statement is anchored to `[source: file_path:line_number]` or `[source: file_path [Section]]` citations.
  - Ensure every section highlights how the implementation satisfies or diverges from prior intent with the gathered evidence.
- **QUESTIONS:**
  - Does every component, flow, and decision include an up-to-date source reference?
  - Are ADRs tied to concrete decisions in dev notes or review threads?
  - Have you documented each deviation from the original design with rationale?
  - Is any required template section missing detail or evidence?
- **CHECKLIST:**
  - [ ] Components, data flows, ADRs, and deviations populated per template
  - [ ] All assertions linked to precise source references
  - [ ] Narrative reflects the current implementation, not legacy designs

3. **Step 3: Shard Architecture Documentation**
- **GOAL:** Regenerate clean `{ARCH}/*.md` shards directly from the unified source.
- **STEPS:**
  - Delete existing `{ARCH}/*.md` artifacts so stale shards cannot persist.
  - Run `python {SCRIPTS}/shard-architecture.py {root}/docs/architecture.md {ARCH}/` to emit the new shard set.
  - Review each shard to confirm content integrity, source references, and navigation links.
- **QUESTIONS:**
  - Were legacy architecture files removed before regeneration?
  - Did the sharding script execute successfully and output the expected files?
  - Do the new shards preserve references and cross-links without regressions?
  - Is any manual cleanup needed after sharding completes?
- **CHECKLIST:**
  - [ ] Legacy architecture files removed prior to sharding
  - [ ] Sharding script completed without errors
  - [ ] Generated shards validated for structure and references

4. **Step 4: Refresh AGENTS.md Index**
- **GOAL:** Update `{root}/AGENTS.md` so it accurately indexes the regenerated architecture set.
- **STEPS:**
  - Enumerate the new `{ARCH}/*.md` files and summarize each file’s scope.
  - Revise the architecture section in `AGENTS.md` with file listings, concise descriptions, and a fresh timestamp.
  - Verify cross-references and navigation cues reflect the regenerated structure.
- **QUESTIONS:**
  - Does the index list every shard with a truthful, succinct summary?
  - Is the "Last Updated" entry aligned with this documentation cycle?
  - Do links and references in `AGENTS.md` match the actual file paths?
  - Are any follow-up tasks required to keep the index synchronized?
- **CHECKLIST:**
  - [ ] Architecture shard listings refreshed with accurate summaries
  - [ ] Metadata and timestamps updated
  - [ ] Index links and references verified against actual files

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Architecture sharded to "{ARCH}/" with source references (format: file_path:line_number)
- [ ] All deviations from original design documented with rationale
- [ ] AGENTS.md updated with current architecture index

## [Example]

### Good #1
**Input**: Outdated architecture exists. Codebase changed from sync to async payment. Dev notes document decision  
**Decision**: Read existing arch. Analyze codebase (OrderService.js, PaymentGateway.js). Identify drift: sync→async payment. Extract rationale from dev notes (ADR-005: async for scalability). Create unified architecture.md with actual async implementation, source refs (OrderService.js:L20-L45, dev-notes/3-dev-notes.md [Payment Decision]). Delete old arch files. Shard to components.md, data-flows.md, decisions.md. Update AGENTS.md index.  
**Why Good**: This reconciles with living codebase, records rationale, and performs full workflow (sharding, indexing, cleanup).

### Good #2
**Input**: No existing architecture (greenfield just completed). Codebase has device registry, telemetry, dashboard. Dev notes have 8 tasks with decisions. Reviews document optimizations  
**Decision**: Analyze codebase structure (device-registry/, telemetry/, dashboard/). Extract decisions from dev notes (ADR-001: Kafka over RabbitMQ). Gather context from reviews (performance patterns). Create architecture.md from scratch based on actual implementation. Document components, data flows, ADRs with source refs (telemetry/TelemetryIngester.js:L5-L80, dev-notes/2-dev-notes.md [Kafka Decision]). Shard successfully. Create AGENTS.md with index.  
**Why Good**: This builds from real implementation evidence and delivers every artifact with references.

### Bad #1
**Input**: Existing arch describes sync payment. Actual codebase implements async  
**Bad Decision**: Read existing arch. Update by copying most content verbatim. Keep original sync description because arch doc says so. Add small note mentioning async exists. Don't verify with codebase.  
**Why Bad**: This violates constraint (must base on actual implementation). Architecture must reflect actual state, not original design. This keeps outdated sync description and misleads developers.  
**Correct**: Analyze actual codebase FIRST. Document what's actually implemented (async payment), not original design (sync). Reference actual code with source_refs (OrderService.js:L20-L45). Document drift in ADR with rationale. Architecture must match reality.
