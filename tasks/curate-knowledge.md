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

## [Instructions]
1. **Step 1: Scan and Extract**
- **GOAL:** Surface high-value practices, recurring errors, and key decisions from every source document.
- **STEPS:**
  - Review `{REVIEW}/*.md` for practices scored ≥9.0 and documented issues worth capturing.
  - Pull significant decisions, challenges, and trade-offs from `{DEVNOTES}/*.md` and `{PROGRESS}` records.
  - Extract deployment incidents, resolutions, and existing insights from `{CUTOVER}` notes and `{KNOWLEDGE}/*.md`.
- **QUESTIONS:**
  - Which practices meet or exceed the ≥9.0 quality threshold?
  - What recurring failures or bugs appear across the sources?
  - Which technology choices or trade-offs need to be preserved?
- **CHECKLIST:**
  - [ ] High-value practices, errors, and decisions enumerated with source pointers.
  - [ ] Root causes and solutions captured for each issue.
  - [ ] Performance and security items noted for later categorization.

2. **Step 2: Organize by Domain**
- **GOAL:** Group extracted knowledge into domain-focused files that are easy to navigate.
- **STEPS:**
  - Cluster each knowledge item into a natural technical domain (security, performance, API design, database, concurrency, infrastructure, etc.).
  - Apply `{type}-{domain}.md` naming for best practices, errors, and decisions.
  - Create or update the corresponding files under `{KNOWLEDGE}` with grouped entries.
- **QUESTIONS:**
  - Does every knowledge item sit in the most specific domain available?
  - Are naming conventions applied consistently across files?
  - Do any new domains need to be introduced to avoid miscategorizing data?
- **CHECKLIST:**
  - [ ] All knowledge items assigned to domain categories.
  - [ ] File names follow the `{type}-{domain}.md` convention.
  - [ ] No extracted item remains uncategorized.

3. **Step 3: Document with Evidence**
- **GOAL:** Record each knowledge item with clear context, solution, and traceable evidence.
- **STEPS:**
  - Write each entry with practice/problem, context, and solution/approach sections.
  - Attach precise references using `[source: file_path [section_name]]` for every entry.
  - Capture conflicting practices with contextual qualifiers rather than merging them.
- **QUESTIONS:**
  - Does each entry explain when the knowledge applies?
  - Is the recommended solution backed by a cited source?
  - Are conflicting approaches clearly labeled with their applicable scenarios?
- **CHECKLIST:**
  - [ ] Entries include description, context, solution, and evidence.
  - [ ] Source references use the required citation format.
  - [ ] Conflicting practices documented with contextual notes.

4. **Step 4: Archive Sources**
- **GOAL:** Preserve source materials while maintaining traceability to the knowledge base.
- **STEPS:**
  - Confirm the knowledge base reflects all extracted insights with citations.
  - Move processed source documents to `{ARCHIVE}/{version_name}/`, keeping knowledge files active in `{KNOWLEDGE}`.
  - Verify each knowledge entry links back to an accessible archived source.
- **QUESTIONS:**
  - Have all source insights been captured before archiving?
  - Does the archive path follow the expected version naming?
  - Can every knowledge entry be traced to its archived document?
- **CHECKLIST:**
  - [ ] Knowledge base coverage validated before archiving.
  - [ ] Sources relocated to `{ARCHIVE}/{version_name}/`.
  - [ ] Traceability confirmed between knowledge entries and archived files.

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
