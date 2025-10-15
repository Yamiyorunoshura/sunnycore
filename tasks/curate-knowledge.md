**GOAL**: Organize development knowledge including best practices, lessons learned, and bug fix records into a searchable knowledge base.

## [Context]
Read and analyze these source documents:
- `{REVIEW}/*.md` - Quality assessments with scores and findings
- `{DEVNOTES}/*.md` - Implementation decisions and challenges
- `{KNOWLEDGE}/*.md` - Existing knowledge (if present)
- `{CUTOVER}` and cutover notes - Deployment issues and solutions
- `{PROGRESS}` - Project decisions and trade-offs

## [Products]
- `{KNOWLEDGE}/*.md` - Knowledge base organized by technical domains

## [Steps]
1. **Scan and Extract**: Identify high-value practices, errors, and decisions across all documents
2. **Organize by Domain**: Group knowledge into technical categories (security, performance, etc.)
3. **Document with Evidence**: Create knowledge files with clear source references
4. **Archive Sources**: Move source documents to archive for version control

## [Instructions]

### 1. Knowledge Scanning and Extraction

**How to identify valuable knowledge:**
- **High-Quality Practices**: Look for practices with scores ≥9.0 in review documents, marked as "Platinum"
- **Error Patterns**: Extract all bugs, failures, and their solutions regardless of quality level
- **Technical Decisions**: Capture significant technology choices, architecture decisions, and trade-off analyses

**Scanning approach:**
- Read review documents to find scored practices and identified issues
- Extract technical decisions and challenges from dev notes
- Look for deployment issues and solutions in cutover reports
- Identify recurring patterns across multiple documents

**What to capture:**
- Root causes and solutions for technical problems
- Proven practices with evidence of effectiveness
- Technology choices with rationale
- Performance optimization decisions
- Security implementation patterns

### 2. Domain-Based Organization

**How to organize knowledge:**
- Group by technical domain, not by source document
- Create natural categories based on the knowledge found
- Use consistent naming: `{type}-{domain}.md`

**Common domain categories:**
- **Security**: Authentication, authorization, encryption, validation
- **Performance**: Caching, optimization, load handling
- **API Design**: REST patterns, versioning, error handling
- **Database**: Schema design, queries, migrations
- **Concurrency**: Race conditions, locks, distributed systems
- **Infrastructure**: Deployment, monitoring, configuration

**Organization patterns:**
- `best-practices-{domain}.md` - Proven techniques (score ≥9.0)
- `errors-{domain}.md` - Bug patterns and solutions
- `decisions-{domain}.md` - Architecture and technology choices

### 3. Knowledge Documentation

**Evidence linking approach:**
- Include source reference for every knowledge point
- Format: `[source: file_path [section_name]]`
- Link to specific sections or findings in source documents

**Documentation structure per knowledge point:**
- **Practice/Problem**: Clear description
- **Context**: When/where this applies
- **Solution/Approach**: What works and why
- **Evidence**: Source reference with specific location

**Handle conflicting practices:**
- Document all valid approaches with their contexts
- Note conflicts explicitly rather than forcing resolution
- Preserve different solutions for different scenarios

### 4. Archival Process

**How to archive:**
1. Verify knowledge base is complete and properly referenced
2. Move all source documents to `{ARCHIVE}/{version_name}/`
3. Keep knowledge base in active workspace for ongoing use
4. Ensure traceability from knowledge back to archived sources

## [Quality Gates]
- [ ] Knowledge base created with domain-organized files
- [ ] All knowledge points have source references
- [ ] Source documents archived with version control
- [ ] No high-value knowledge lost from source documents

## [Example]

**Input**: Review has JWT implementation (9.2/10), API versioning (8.5/10). Dev notes show caching race condition solved, Redis vs memory cache decision.

**Approach**: Extract JWT practice (≥9.0 threshold), capture race condition solution and caching decision. Organize into security and performance domains.

**Output**: 
- `best-practices-security.md` - JWT implementation with review reference
- `errors-performance.md` - Race condition pattern with dev notes reference  
- `decisions-performance.md` - Caching strategy with rationale and trade-offs

**Why Effective**: Preserves valuable knowledge with evidence, organized for future reference and reuse.
