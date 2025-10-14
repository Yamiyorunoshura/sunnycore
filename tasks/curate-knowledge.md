**GOAL**: Organize development knowledge including best practices, lessons learned, and bug fix records.

## [Input]
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
1. Identify platinum practices and errors → All platinum practices and errors identified
2. Design organization, classify by semantic topics → Knowledge base structure defined
3. Create documents with evidence sources → Complete knowledge base with evidence
4. Archive source documents to "{ARCHIVE}/{version_name}/" → Source documents archived

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Knowledge base at "{KNOWLEDGE}/" with platinum practices and errors documented
- [ ] All knowledge points have evidence source annotations (format: file_path [Section Name])
- [ ] Source documents archived to "{ARCHIVE}/{version_name}/"

## [Example]

### Good #1
**Input**: Reviews have 3 platinum practices (JWT rotation, circuit breaker, API versioning). Dev notes have 2 errors (cache race condition, SQL injection)  
**Decision**: Scan all reviews and dev notes→Extract only platinum practices (3 found)→Document errors with solutions (2 found)→Classify by semantic topics: security, api-design, concurrency→Create: best-practices-security.md, best-practices-api-design.md, errors-concurrency.md, errors-security.md→Annotate with evidence sources→Archive to archive/v1.0/  
**Why Good**: Filters by platinum standard, organizes by topic, preserves provenance

### Good #2
**Input**: Reviews show only gold-level (not platinum). Dev notes have memory leak error. Progress has Kafka vs RabbitMQ decision  
**Decision**: Scan reviews (no platinum found)→Extract error (memory leak)→Document decision from progress (Kafka selection)→Classify: performance→Create problem-solving-performance.md for complex decision, errors-performance.md for memory leak→Record "No platinum practices at this stage"→Archive  
**Why Good**: Records absence of platinum transparently, captures impactful learnings with strong citations

### Bad #1
**Input**: Reviews have 2 gold and 1 platinum practice  
**Bad Decision**: Include both gold and platinum to make knowledge base look comprehensive→Self-judge some gold as platinum quality without review evidence  
**Why Bad**: Violates platinum-only constraint, violates trust-review-markings constraint. Creates unreliable knowledge base  
**Correct**: Extract only 1 platinum practice from reviews→Document gold separately as "promising practices pending validation" or exclude→Trust review markings without self-judgment→Create best-practices.md with only platinum→Annotate: "2 gold-level practices excluded pending platinum validation"
