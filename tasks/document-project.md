**GOAL**: Update or create comprehensive project architecture documentation.

## [Input]
- `{ARCH}/*.md`
- `{TMPL}/architecture-tmpl.yaml`
- `{KNOWLEDGE}/*.md`
- `{PROGRESS}`
- `{DEVNOTES}/*.md`
- `{REVIEW}/*.md`
- Actual codebase

## [Output]
- `{root}/docs/architecture.md` (temporary, will be sharded)
- `{ARCH}/*.md`
- `{root}/CLAUDE.md` (updated with refreshed index)

## [Constraints]
- **MUST** base on actual implementation, **MUST NOT** base on original design
- **MUST** include source references (source_refs), **MUST NOT** produce content without
- **MUST** delete old architecture docs before sharding, **MUST NOT** skip
- **MUST** update CLAUDE.md index after sharding, **MUST NOT** skip

## [Steps]
1. Understand existing architecture and actual implementation → Complete understanding of current state
2. Create unified architecture.md with source references → Complete unified architecture document
3. Remove old architecture docs, run sharding script, verify output → Successfully sharded architecture in "{ARCH}/*.md"
4. Update CLAUDE.md with refreshed architecture index → CLAUDE.md updated with current index

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Architecture sharded to "{ARCH}/" with source references (format: file_path:line_number)
- [ ] All deviations from original design documented with rationale
- [ ] CLAUDE.md updated with current architecture index

## [Example]

### Good #1
**Input**: Outdated architecture exists. Codebase changed from sync to async payment. Dev notes document decision  
**Decision**: Read existing arch→Analyze codebase (OrderService.js, PaymentGateway.js)→Identify drift: sync→async payment→Extract rationale from dev notes (ADR-005: async for scalability)→Create unified architecture.md with actual async implementation, source refs (OrderService.js:L20-L45, dev-notes/3-dev-notes.md [Payment Decision])→Delete old arch files→Shard to components.md, data-flows.md, decisions.md→Update CLAUDE.md index  
**Why Good**: Reconciles with living codebase, records rationale, performs full workflow (sharding, indexing, cleanup)

### Good #2
**Input**: No existing architecture (greenfield just completed). Codebase has device registry, telemetry, dashboard. Dev notes have 8 tasks with decisions. Reviews document optimizations  
**Decision**: Analyze codebase structure (device-registry/, telemetry/, dashboard/)→Extract decisions from dev notes (ADR-001: Kafka over RabbitMQ)→Gather context from reviews (performance patterns)→Create architecture.md from scratch based on actual implementation→Document components, data flows, ADRs with source refs (telemetry/TelemetryIngester.js:L5-L80, dev-notes/2-dev-notes.md [Kafka Decision])→Shard→Create CLAUDE.md with index  
**Why Good**: Builds from real implementation evidence, delivers every artifact with references

### Bad #1
**Input**: Existing arch describes sync payment. Actual codebase implements async  
**Bad Decision**: Read existing arch→Update by copying most content verbatim→Keep original sync description because arch doc says so→Add small note mentioning async exists→Don't verify with codebase  
**Why Bad**: Violates constraint (must base on actual implementation). Architecture must reflect actual state, not original design. Keeps outdated sync description, misleads developers  
**Correct**: Analyze actual codebase FIRST→Document what's actually implemented (async payment), not original design (sync)→Reference actual code with source_refs (OrderService.js:L20-L45)→Document drift in ADR with rationale→Architecture must match reality
