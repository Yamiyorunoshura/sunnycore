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
**You should work along to the following steps:**
1. Understand existing architecture and actual implementation. This achieves complete understanding of current state.
2. Create unified architecture.md with source references. This produces complete unified architecture document.
3. Remove old architecture docs, run sharding script, verify output. This successfully shards architecture in "{ARCH}/*.md".
4. Update CLAUDE.md with refreshed architecture index. This updates CLAUDE.md with current index.

## [Instructions]

### 1. Architecture Reconciliation (Actual vs Original)
The architecture documentation must reflect ACTUAL implementation, not original design:

**Analysis Process**:
1. **Read Existing Architecture**: Review all files in `{ARCH}/*.md` to understand original design
2. **Analyze Actual Codebase**: Examine actual implementation in the codebase
3. **Identify Drift**: Document differences between original design and actual implementation
4. **Extract Rationale**: Find decision rationale in dev notes, reviews, and progress docs

**Common Drift Patterns**:
- Technology changes (e.g., MySQL → PostgreSQL)
- Pattern changes (e.g., sync → async processing)
- Component additions or removals
- Interface/contract changes

### 2. Evidence-Based Documentation
EVERY architectural statement must have source references:

**Source Reference Format**: `[source: file_path:line_number]` or `[source: file_path [Section Name]]`

**Examples**:
- "OrderService uses async payment processing [source: src/services/OrderService.js:L20-L45]"
- "ADR-005: Async for scalability [source: dev-notes/3-dev-notes.md [Payment Decision]]"
- "Redis caching strategy [source: src/middleware/cache.js:L10-L30]"

**What to Reference**:
- Code files for implementation details
- Dev notes for design decisions
- Reviews for architectural validations
- Knowledge base for best practices applied

### 3. Complete Architecture Documentation
Create unified `architecture.md` with all standard sections:

**Components Section**:
- List ALL implemented components (from actual code)
- Responsibilities and interfaces for each
- Technology stack with versions
- Dependencies between components

**Data Flows Section**:
- Document actual data flows (from code analysis)
- Include request/response patterns
- Event flows and pub/sub patterns
- Data persistence flows

**Architecture Decision Records (ADRs)**:
- Extract decisions from dev notes and reviews
- Format: Context → Decision → Consequences → Alternatives
- Link to actual implementation

**Deviations from Original Design**:
- Document ALL changes from original architecture
- Provide rationale for each change
- Link to evidence (dev notes, review comments)

### 4. Sharding Workflow
After creating unified architecture.md:

1. **Delete Old Architecture**:
   ```bash
   rm -rf {ARCH}/*.md
   ```
   This ensures clean sharding without conflicts

2. **Execute Sharding Script**:
   ```bash
   python {SCRIPTS}/shard-architecture.py {root}/docs/architecture.md {ARCH}/
   ```

3. **Verify Output**:
   - Check all sharded files in `{ARCH}/` directory
   - Verify source references are preserved
   - Confirm cross-references work correctly

### 5. CLAUDE.md Index Update
After sharding, update `{root}/CLAUDE.md` with current architecture index:

**Index Content**:
- List all architecture files with brief descriptions
- Highlight key components and decision records
- Update last-modified timestamps
- Ensure index is complete and accurate

**Format Example**:
```markdown
## Architecture Documentation

- `architecture/components.md` - System components and responsibilities
- `architecture/data-flows.md` - Data flow patterns and integrations
- `architecture/decisions.md` - ADRs and design rationale
- `architecture/api-contracts.md` - API specifications and contracts

Last Updated: 2025-10-14
```

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
