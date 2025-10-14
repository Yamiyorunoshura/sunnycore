**GOAL**: Create architecture change documentation for Brownfield projects.

## [Context]
**You must read the following context:**
- `{REQ}`
- `{ARCH}/*.md`
- `{SCRIPTS}/shard-architecture.py`
- `{TMPL}/architecture-tmpl.yaml`
- `{KNOWLEDGE}/*.md`

## [Products]
- `{root}/docs/architecture.md` (temporary)
- `{ARCH}/*.md` (updated)

## [Constraints]
- **MUST** review existing architecture first, **MUST NOT** design without review
- **MUST** include Impact Analysis for contract changes, **MUST NOT** break existing contracts
- **MUST** follow template structure, **MUST NOT** deviate
- **MUST** execute shard-architecture.py, **MUST NOT** skip

## [Steps]
**You should work along to the following steps:**
1. Evaluate existing architecture, identify extension points. This ensures current architecture is understood with extension points identified.
2. Design new module with impact analysis. This creates complete new module with impact analysis.
3. Create architecture.md, obtain approval, shard. This results in approved and sharded architecture.
4. Verify compatibility. This confirms new and existing modules are compatible.

## [Instructions]

### 1. Existing Architecture Review
Before designing any changes, you must thoroughly review all existing architecture documents:
- Read ALL files in `{ARCH}/*.md` to understand current state
- Identify existing components, their boundaries, and responsibilities
- Document current technology stack and design patterns
- Map existing contracts (APIs, events, messages)
- Identify extension points where new functionality can be added without breaking changes

### 2. Extension Strategy
Design new modules to extend the existing architecture without breaking it:

**Preferred Integration Patterns** (in order of preference):
1. **Extension Points**: Use existing extension points (event bus, plugin architecture, hooks)
2. **New Components**: Add isolated components that integrate via existing interfaces
3. **Wrapper/Adapter**: Wrap existing components with new functionality
4. **Contract Evolution**: Extend contracts with backward compatibility (versioning, optional fields)

**Avoid**: Direct modification of core components unless absolutely necessary

### 3. Impact Analysis
For ANY change to existing components or contracts, you must create a detailed **Impact Analysis Table**:
| Changed Element | Type | Impact Scope | Affected Components | Migration Required | Risk Level |
|----------------|------|--------------|---------------------|-------------------|------------|
| User API | Contract change | API Gateway, Auth Service | 3 clients | Add new endpoint version | Medium |
| Event schema | Schema evolution | All subscribers | 5 services | Gradual migration | High |

Include:
- **Breaking Changes**: Document all breaking changes with migration paths
- **Backward Compatibility**: Specify how existing functionality is preserved
- **Rollback Plan**: Define how changes can be reverted if needed

### 4. Reference Format
When referencing existing architecture, use the proper citation format:
- Format: `docs/architecture/[file-name].md#[section-name]`
- Example: Reference `docs/architecture/components.md#user-service` when discussing User Service integration

### 5. Approval and Sharding Workflow
After creating the architecture update:
1. Present the complete Impact Analysis to the user
2. Obtain approval for all changes (especially breaking changes)
3. Execute `shard-architecture.py` to update architecture files
4. Verify compatibility between old and new components

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] New module design with impact analysis for all changes
- [ ] Compatibility verified (no breaking changes or migration path provided)
- [ ] Architecture sharded to "{ARCH}/"

## [Example]

### Good #1
**Input**: Existing REST API with basic auth. REQ-001: OAuth2 authentication  
**Decision**: Read existing architecture (User Service, API Gateway). Design OAuth2 Server integrating with User Service. Preserve API contracts (add Authorization header). Impact Analysis on Gateway middleware. Reference docs/architecture/components.md#user-service. Shard successfully.  
**Why Good**: This extends without breaking contracts, documents impacts explicitly, and completes approval and sharding.

### Good #2
**Input**: Existing CMS with PostgreSQL+Redis. REQ-001 (analytics), REQ-002 (behavior analysis)  
**Decision**: Identify Brownfield. Design Analytics Collector+ClickHouse. Use event bus as extension point (analytics subscribes). No CMS changes. ADR for ClickHouse. Map requirements. Reference existing docs. Shard successfully.  
**Why Good**: This introduces via extension points, preserves legacy stability, and maintains traceability.

### Bad #1
**Input**: Need feature in existing system  
**Bad Decision**: Design without reading existing docs, assume integration points, skip Impact Analysis, fabricate component names, shard without compatibility check.  
**Why Bad**: This violates review requirement, provides no Impact Analysis for changes, and creates incompatible design.  
**Correct**: Read ALL docs/architecture/*.md. Understand components/contracts/extension points. Design ensuring compatibility. Create Impact Analysis for ANY changes. Use proper reference format citations. Shard successfully.
