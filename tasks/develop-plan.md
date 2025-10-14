**GOAL**: Execute TDD development based on implementation plan.

## [Input]
- `{PLAN}/{task_id}-plan.md`
- `{ARCH}/*.md`
- `{TMPL}/dev-notes-tmpl.yaml`

## [Output]
- `{DEVNOTES}/{task_id}-dev-notes.md`
- High-quality code (tests passing, aligned with plan)
- Complete test coverage (unit + integration + behavior)

## [Constraints]
- **MUST** follow TDD cycle (RED→GREEN→REFACTOR), **MUST NOT** skip any phase
- **MUST** align with plan acceptance criteria and architecture, **MUST NOT** deviate without rationale
- **MUST** deliver with all tests passing (exit code 0), **MUST NOT** deliver failing tests
- **MUST** document out-of-scope changes in dev notes, **MUST NOT** modify files silently outside plan scope
- **MUST** follow [develop-guidelines], **MUST NOT** violate code quality standards

## [Blocking-Conditions]
- Missing critical inputs, unexpected RED failures, risky irreversible actions, tools lacking non-interactive flags

## [Steps]
1. Read plan + architecture, conceive solution → TDD phases understood and outline documented
2. **RED**: Implement all test cases, execute and verify they fail correctly → All tests failing as expected
3. **GREEN**: Minimal implementation aligned with architecture, execute tests → All tests passing (exit code 0)
4. **REFACTOR**: Enhance code quality, maintain green tests → High-quality code with tests still passing
5. Create or update `{DEVNOTES}/{task_id}-dev-notes.md`, validate acceptance criteria → Dev notes completed

## [DoD]
- [ ] Full TDD cycle (RED→GREEN→REFACTOR) completed with all tests passing
- [ ] Code quality standards met (SOLID, DRY, functions ≤50 lines, coverage ≥80%)
- [ ] Dev notes exist at `{DEVNOTES}/{task_id}-dev-notes.md`

## [Example]

### Good #1
**Input**: Plan for article publishing (Express, PostgreSQL), template available  
**Decision**: Read plan → RED: write all tests (unit/integration/behavior), verify fail → GREEN: minimal code (Article model, API endpoints), all tests pass → REFACTOR: add validation + error handling + patterns, tests stay green → Update existing dev notes  
**Why Good**: Full TDD cycle executed with verification at each phase, dev notes updated (not new file), 85% coverage meets DoD

### Good #2
**Input**: Transaction reports plan with NFR <2s query time (TimescaleDB)  
**Decision**: RED: write tests including performance <2s, verify fail → GREEN: minimal query + indexed columns, all pass (120ms) → REFACTOR: add Redis caching + optimizations, tests green → Create new dev notes from template (doesn't exist)  
**Why Good**: Validates performance NFR explicitly, creates dev notes when needed, tracking shows full TDD progression

### Good #3
**Input**: User notification service plan (WebSocket, Redis pub/sub), architecture specifies event-driven pattern  
**Decision**: Read plan + arch → RED: write unit tests (event handlers), integration tests (Redis pub/sub), behavior tests (notification delivery), verify all fail correctly → GREEN: minimal WebSocket server + event handlers + Redis subscriber, all tests pass (exit code 0) → REFACTOR: extract event bus pattern, add error recovery, tests stay green → Update existing dev notes with implementation  
**Why Good**: Aligns with architecture (event-driven), completes full TDD cycle with verification, achieves 88% coverage (exceeds DoD 80%), updates not creates dev notes

### Bad #1
**Input**: Plan exists, need to implement  
**Decision**: Skip RED → Code with optimizations immediately → Skip tests → No dev notes → Mark complete  
**Why Bad**: Violates Constraint 1 (no TDD cycle), violates DoD (no passing tests, no dev notes), unverified implementation  
**Correct Approach**: RED (all tests, verify fail) → GREEN (minimal code, tests pass) → REFACTOR (quality improvements) → Dev notes

### Bad #2
**Input**: Task implementation with acceptance criteria  
**Decision**: Deliver with failing tests → Modify out-of-scope files silently → Claim "self-documenting code" → Create red-phase-result.md, green-phase-result.md separately  
**Why Bad**: Violates Constraint 3 (exit code ≠ 0), Constraint 4 (no rationale for scope changes), DoD (no dev notes), creates unnecessary files  
**Correct Approach**: Ensure exit code 0 → Document all out-of-scope changes in dev notes → Always create/update dev notes → Use plan.md only for tracking (temporary)

### Bad #3
**Input**: API endpoint plan with security requirements (rate limiting, input validation)  
**Decision**: Skip RED → Write implementation with all features (validation + rate limiting + caching + logging) at once → Run tests: 8/12 pass, 4 fail → Debug for hours → Give up, commit partial work → No dev notes "will document later"  
**Why Bad**: Violates Constraint 1 (no TDD cycle), implements everything at once instead of minimal GREEN, violates Constraint 3 (exit code ≠ 0), DoD violated (failing tests, no dev notes), unverifiable which piece failed  
**Correct Approach**: RED: write all 12 tests, verify fail → GREEN: minimal implementation for JUST passing tests (no extra features) → REFACTOR: add rate limiting, then caching, then logging one by one with tests green → Dev notes with complete documentation
