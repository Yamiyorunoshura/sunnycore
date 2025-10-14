**GOAL**: Organize development knowledge including best practices, lessons learned, and bug fix records.

## [Input]
**You must read the following documents:**
- `{REVIEW}/*.md`
- `{DEVNOTES}/*.md`
- `{KNOWLEDGE}/*.md` (if exist)
- `{CUTOVER}`
- `{root}/docs/cutover-dev-notes.md`
- `{PROGRESS}`

## [Output]
- `{KNOWLEDGE}/*.md` (organized by semantic topics)

## [Constraints]
- **MUST** include only platinum practices, **MUST NOT** include non-platinum
- **MUST** trust review markings, **MUST NOT** make independent level judgments
- **MUST** preserve conflicting practices, **MUST NOT** force resolution

## [Steps]
**You should work along to the following steps:**
1. Identify platinum practices and errors. This identifies all platinum practices and errors.
2. Design organization, classify by semantic topics. This defines knowledge base structure.
3. Create documents with evidence sources. This creates complete knowledge base with evidence.
4. Archive source documents to "{ARCHIVE}/{version_name}/". This archives source documents.

## [Instructions]

### 1. Knowledge Identification and Filtering
Scan all input documents to identify knowledge worth preserving:

#### Platinum Practices (Quality Level ≥ 9.0)
Extract ONLY platinum-level best practices from review reports:
- Look for explicit "Platinum" markings in reviews
- Trust the review quality scores (9.0-10.0 = Platinum)
- Do NOT make independent judgments about practice quality
- If a practice is marked as "gold" (8.0-8.9), do NOT include it as platinum

Document what was found:
- If platinum practices exist: Extract and document them
- If no platinum found: Explicitly record "No platinum practices at this stage"

#### Error Patterns and Solutions
Extract all error patterns regardless of quality level:
- Root causes of bugs
- Solutions that worked
- Evidence from code (file paths and line numbers)
- Reproduction steps

These are valuable learning regardless of the practice quality level.

#### Complex Decisions
Extract significant technical decisions from progress notes:
- Technology choices (e.g., Kafka vs RabbitMQ)
- Architecture decisions with rationale
- Trade-off analyses
- Performance optimization decisions

### 2. Knowledge Organization by Topics
Organize extracted knowledge by semantic topics (not by source):

**Suggested Topic Structure**:
- `best-practices-{domain}.md` (e.g., security, api-design, performance, database)
- `errors-{domain}.md` (e.g., concurrency, security, performance)
- `problem-solving-{domain}.md` (for complex decisions)

**Topic Examples**:
- Security: Authentication patterns, encryption, input validation
- API Design: REST conventions, versioning, error handling
- Concurrency: Race conditions, locks, distributed systems
- Performance: Caching, query optimization, load testing
- Database: Schema design, indexing, migrations

### 3. Evidence Source Annotation
For EVERY knowledge point, you must include evidence source annotation:

**Format**: `[source: file_path [Section Name]]`

**Examples**:
- `[source: reviews/3-review.md [Security Assessment]]`
- `[source: dev-notes/2-dev-notes.md [Kafka Decision]]`
- `[source: cutover-dev-notes.md [Performance Issue]]`

This ensures traceability and allows verification of knowledge claims.

### 4. Handling Conflicting Practices
If you encounter conflicting best practices:
- **DO NOT** force a resolution or choose one over the other
- **DO** document both practices with their contexts
- **DO** note the conflict explicitly

Example:
```markdown
### Caching Strategy

#### Practice A: Redis for All Cache [source: reviews/1-review.md]
Use Redis as centralized cache for all services...

#### Practice B: Local In-Memory First [source: reviews/5-review.md]
Use local cache with Redis fallback to reduce latency...

**Note**: Both practices exist in the codebase for different contexts.
Practice A applies to shared data, Practice B to service-specific data.
```

### 5. Archival Workflow
After extracting and organizing knowledge:
1. Create or update knowledge base files in `{KNOWLEDGE}/`
2. Archive source documents to `{ARCHIVE}/{version_name}/`:
   - Move `{REVIEW}/*.md`
   - Move `{DEVNOTES}/*.md`
   - Move `{CUTOVER}` and cutover dev notes
   - Move `{PROGRESS}` if exists
3. Keep `{KNOWLEDGE}/` in active workspace (do not archive)

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Knowledge base at "{KNOWLEDGE}/" with platinum practices and errors documented
- [ ] All knowledge points have evidence source annotations (format: file_path [Section Name])
- [ ] Source documents archived to "{ARCHIVE}/{version_name}/"

## [Example]

### Good #1
**Input**: Reviews have 3 platinum practices (JWT rotation, circuit breaker, API versioning). Dev notes have 2 errors (cache race condition, SQL injection)  
**Decision**: Scan all reviews and dev notes. Extract only platinum practices (3 found). Document errors with solutions (2 found). Classify by semantic topics: security, api-design, concurrency. Create: best-practices-security.md, best-practices-api-design.md, errors-concurrency.md, errors-security.md. Annotate with evidence sources. Archive to archive/v1.0/.  
**Why Good**: This filters by platinum standard, organizes by topic, and preserves provenance.

### Good #2
**Input**: Reviews show only gold-level (not platinum). Dev notes have memory leak error. Progress has Kafka vs RabbitMQ decision  
**Decision**: Scan reviews (no platinum found). Extract error (memory leak). Document decision from progress (Kafka selection). Classify: performance. Create problem-solving-performance.md for complex decision, errors-performance.md for memory leak. Record "No platinum practices at this stage". Archive successfully.  
**Why Good**: This records absence of platinum transparently and captures impactful learnings with strong citations.

### Bad #1
**Input**: Reviews have 2 gold and 1 platinum practice  
**Bad Decision**: Include both gold and platinum to make knowledge base look comprehensive. Self-judge some gold as platinum quality without review evidence.  
**Why Bad**: This violates platinum-only constraint and trust-review-markings constraint. This creates unreliable knowledge base.  
**Correct**: Extract only 1 platinum practice from reviews. Document gold separately as "promising practices pending validation" or exclude. Trust review markings without self-judgment. Create best-practices.md with only platinum. Annotate: "2 gold-level practices excluded pending platinum validation".
