**GOAL**: Complete all PRD development tasks in one iteration.

## [Input]
- `{PRD}`
- `{TMPL}/dev-notes-tmpl.yaml`

## [Output]
- `{root}/docs/prd-dev-notes.md`
- High-quality tested code aligned with architecture
- Complete test coverage

## [Constraints]
- **MUST** complete all PRD tasks, **MUST NOT** leave any incomplete
- **MUST** follow TDD cycle (RED→GREEN→REFACTOR), **MUST NOT** skip
- **MUST** document out-of-scope changes in dev notes, **MUST NOT** modify files silently
- **MUST** deliver with all tests passing (exit code 0), **MUST NOT** deliver failing tests

## [Steps]
1. Understand all PRD requirements and architecture → Complete strategy established
2. TDD cycle: RED (write tests, verify fail)→GREEN (minimal code, tests pass)→REFACTOR (improve quality, tests stay green) → All features implemented with high quality
3. Execute complete test suite, validate acceptance criteria → Full integration verified and acceptance met
4. Create comprehensive dev notes at "{root}/docs/prd-dev-notes.md" → Complete dev notes created
5. Verify all requirements satisfied, confirm quality standards (≥80% coverage) → All requirements delivered with quality met

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All PRD requirements implemented through full TDD cycle with all tests passing
- [ ] Code quality met (SOLID, DRY, functions ≤50 lines, coverage ≥80%)
- [ ] Complete dev notes at "{root}/docs/prd-dev-notes.md"

## [Example]

### Good #1
**Input**: PRD with REQ-001 (update profile), REQ-002 (avatar upload), NFR-001 (<200ms). Tasks: Task-1 (profile API), Task-2 (avatar storage)  
**Decision**: Understand all PRD→Develop strategy respecting dependencies (Task-1→Task-2)→RED: write tests for PUT /profile, POST /profile/avatar (all fail correctly)→GREEN: implement profile update, S3 avatar upload (all pass)→REFACTOR: add validation, optimize image processing (tests stay green)→Create prd-dev-notes.md→Validate all acceptance criteria  
**Why Good**: Implements every requirement via full TDD loop, validates each phase, produces mandated documentation, 87% coverage

### Good #2
**Input**: PRD with REQ-001 (rate limit per user), NFR-001 (100 req/min), NFR-002 (Redis storage). Tasks: middleware, config, monitoring  
**Decision**: Read PRD completely→Plan TDD→RED: tests for rate limit enforcement, exceed limit, reset after window (all fail)→GREEN: Redis-based token bucket, Express middleware (all pass)→REFACTOR: configurable limits, monitoring metrics (tests stay green)→Document in prd-dev-notes.md→Verify NFRs (100 req/min enforced, monitoring functional)  
**Why Good**: Proves NFRs with tests and monitoring evidence, leaves thorough notes and configs, 82% coverage

### Bad #1
**Input**: PRD with multiple tasks  
**Bad Decision**: Implement Task-1 only, skip others→Skip TDD entirely (write code without tests)→Deliver with failing tests→No prd-dev-notes.md→Claim all complete  
**Why Bad**: Violates complete all tasks, skips TDD cycle, delivers with failing tests, no dev notes. Incomplete unusable  
**Correct**: Execute ALL steps for ALL tasks→Develop strategy covering ALL PRD tasks→For each: RED (tests, verify fail)→GREEN (minimal, verify pass)→REFACTOR (quality)→Create comprehensive prd-dev-notes.md→Verify ALL acceptance criteria→Exit code 0
