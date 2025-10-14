**GOAL**: Create architecture change documentation for Brownfield projects.

## [Input]
- `{REQ}`
- `{ARCH}/*.md`
- `{SCRIPTS}/shard-architecture.py`
- `{TMPL}/architecture-tmpl.yaml`
- `{KNOWLEDGE}/*.md`

## [Output]
- `{root}/docs/architecture.md` (temporary)
- `{ARCH}/*.md` (updated)

## [Constraints]
- **MUST** review existing architecture first, **MUST NOT** design without review
- **MUST** include Impact Analysis for contract changes, **MUST NOT** break existing contracts
- **MUST** follow template structure, **MUST NOT** deviate
- **MUST** execute shard-architecture.py, **MUST NOT** skip

## [Steps]
1. Evaluate existing architecture, identify extension points → Current architecture understood with extension points identified
2. Design new module with impact analysis → Complete new module with impact analysis
3. Create architecture.md, obtain approval, shard → Approved and sharded successfully
4. Verify compatibility → New and existing modules compatible

## [DoD]
- [ ] New module design with impact analysis for all changes
- [ ] Compatibility verified (no breaking changes or migration path provided)
- [ ] Architecture sharded to "{ARCH}/"

## [Example]

### Good #1
**Input**: Existing REST API with basic auth. REQ-001: OAuth2 authentication  
**Decision**: Read existing architecture (User Service, API Gateway)→Design OAuth2 Server integrating with User Service→Preserve API contracts (add Authorization header)→Impact Analysis on Gateway middleware→Reference docs/architecture/components.md#user-service→Shard  
**Why Good**: Extends without breaking contracts, documents impacts explicitly, completes approval and sharding

### Good #2
**Input**: Existing CMS with PostgreSQL+Redis. REQ-001 (analytics), REQ-002 (behavior analysis)  
**Decision**: Identify Brownfield→Design Analytics Collector+ClickHouse→Use event bus as extension point (analytics subscribes)→No CMS changes→ADR for ClickHouse→Map requirements→Reference existing docs→Shard  
**Why Good**: Introduces via extension points, preserves legacy stability, maintains traceability

### Bad #1
**Input**: Need feature in existing system  
**Bad Decision**: Design without reading existing docs, assume integration points, skip Impact Analysis, fabricate component names, shard without compatibility check  
**Why Bad**: Violates review requirement, no Impact Analysis for changes, creates incompatible design  
**Correct**: Read ALL docs/architecture/*.md→Understand components/contracts/extension points→Design ensuring compatibility→Impact Analysis for ANY changes→Reference format citations→Shard
