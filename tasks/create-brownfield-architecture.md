**GOAL**: Create architecture change documentation for Brownfield projects.

## [Context]
**You must read the following context:**
- `{REQ}` - Requirements to understand what needs to be built
- `{ARCH}/*.md`(Only the related documents) - Existing architecture to understand current system
- `{SCRIPTS}/shard-architecture.py` - Tool for distributing architecture content
- `{TMPL}/architecture-tmpl.yaml` - Template structure for architecture documentation
- `{KNOWLEDGE}/*.md` - Domain knowledge and patterns

## [Products]
- `{root}/docs/architecture.md` (temporary consolidation)
- `{ARCH}/*.md`(Only the related documents) (updated distributed architecture files)

## [Constraints]
- **MUST** understand existing architecture before designing changes
- **MUST** preserve backward compatibility or provide migration paths
- **MUST** use architecture template structure for consistency

## [Steps]
**Execute these steps to complete the architecture extension:**

1. **Understand Current State**: Read all existing architecture files to map current components, contracts, and identify extension points where new functionality can integrate without breaking changes.

2. **Design Extension Strategy**: Choose appropriate integration patterns (extension points preferred over modifications), design new components that extend existing system, document all interface changes with impact analysis.

3. **Document & Validate**: Create comprehensive architecture documentation using the template, ensure traceability to requirements, obtain approval for any breaking changes, then execute sharding.

4. **Verify Integration**: Cross-check that existing contracts remain functional, validate that new and existing components work together, confirm migration paths for any required changes.

## [Instructions]

### 1. Architecture Discovery Phase
**Focus**: Build complete understanding of current system before making any design decisions.

**Key Activities**:
- Systematically read all architecture files to understand component boundaries and responsibilities
- Map existing technology stack and identify patterns already in use
- Document current contracts (APIs, events, data flows) and their consumers
- Identify natural extension points where new functionality can plug in cleanly
- Note any architectural debt or constraints that limit extension options

**Success Criteria**: You can clearly explain how existing components interact and where new functionality should integrate.

### 2. Extension Design Phase  
**Focus**: Design changes that extend capabilities without breaking existing functionality.

**Key Activities**:
- Choose integration patterns that minimize disruption (prefer extension points over core modifications)
- Design new components to be isolated yet well-integrated
- For any interface changes, ensure backward compatibility or provide clear migration paths
- Document architectural decisions with rationale for pattern choices
- Create impact analysis for any modifications to existing components

**Success Criteria**: New functionality integrates cleanly with existing system and preserves all current capabilities.

### 3. Documentation & Approval Phase
**Focus**: Create complete, template-compliant documentation and secure stakeholder approval.

**Key Activities**:
- Use the architecture template to structure all documentation consistently
- Ensure every requirement maps to specific architectural elements (traceability)
- Present impact analysis and migration plans for any breaking changes
- Obtain explicit approval before proceeding with implementation
- Execute sharding process to distribute content to proper architecture files

**Success Criteria**: Architecture documentation is complete, approved, and properly distributed.

### 4. Integration Verification Phase
**Focus**: Confirm that new and existing components work together as designed.

**Key Activities**:
- Verify existing contracts still function as expected
- Validate integration points between new and existing components  
- Test migration paths for any required changes
- Confirm rollback procedures are viable if needed
- Document any discovered integration issues and their resolutions

**Success Criteria**: System integrity is preserved and new functionality operates correctly within existing ecosystem.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Existing architecture thoroughly understood and extension points identified  
- [ ] New components designed with impact analysis for any changes to existing system
- [ ] Architecture documentation created using template and properly sharded
- [ ] Integration compatibility verified between new and existing components

## [Example]

### Good #1: Authentication Enhancement
**Input**: Existing REST API with basic auth. REQ-001: Add OAuth2 authentication  
**Approach**: 
1. **Discovery**: Read existing User Service and API Gateway architecture, map current auth flow
2. **Design**: Design OAuth2 Server as new component, integrate via existing auth middleware extension points
3. **Documentation**: Create comprehensive architecture using template, show requirement traceability  
4. **Verification**: Confirm existing basic auth continues working, validate OAuth2 integration
**Why Good**: Follows systematic discovery, uses extension points, preserves existing functionality, complete documentation.

### Good #2: Analytics Addition  
**Input**: Existing CMS with PostgreSQL+Redis. Requirements for analytics and behavior tracking
**Approach**:
1. **Discovery**: Map existing CMS architecture, identify event bus as natural extension point
2. **Design**: Add Analytics Collector and ClickHouse as isolated components subscribing to events
3. **Documentation**: Document new components with ADRs, maintain requirement traceability
4. **Verification**: Confirm CMS performance unaffected, validate analytics data flow
**Why Good**: Leverages existing patterns, minimal system impact, complete architectural documentation.

### Bad #1: Assumption-Based Design
**Input**: Need to add new feature to existing system  
**Bad Approach**: Skip architecture review, assume integration points, design without understanding existing contracts, ignore impact analysis.  
**Why Bad**: Violates discovery phase, risks breaking existing functionality, creates integration problems.  
**Correct Approach**: Systematically read existing architecture, understand extension points, design for compatibility, document all impacts.
