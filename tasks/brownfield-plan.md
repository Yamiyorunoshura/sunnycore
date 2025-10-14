**GOAL**: Fix code that failed review based on feedback.

## [Input]
- `{TMPL}/dev-notes-tmpl.yaml`
- `{REVIEW}/{task_id}-review.md`
- `{ARCH}/*.md`
- `{KNOWLEDGE}/*.md` (if exist)

## [Output]
- Fixed code (tests passing)
- Updated `{DEVNOTES}/{task_id}-dev-notes.md`

## [Constraints]
- **MUST** implement fixes that pass all tests, **MUST NOT** deliver non-functional code
- **MUST** follow architecture specs and [develop-guidelines], **MUST NOT** deviate from design specifications
- **MUST** preserve existing functionality, **MUST NOT** introduce breaking changes

## [Steps]
1. Read review report + architecture context, identify root causes → Issues understood with fix plan outlined
2. Implement RED→GREEN→REFACTOR cycle, run all tests → All unit and integration tests passing
3. Update existing `{DEVNOTES}/{task_id}-dev-notes.md` with fix summary + evidence → Dev notes updated with complete fix record

## [DoD]
- [ ] All tests passed
- [ ] Dev notes updated

## [Example]

### Good #1
**Input**: "Auth token validation fails - test_expired_token_rejection failing"  
**Decision**: Analyze review + arch → Identify missing expiry check → TDD cycle → Fix at TokenValidator.js:L25-30 → All tests pass → Update dev notes with change + evidence  
**Why Good**: Follows review→architecture→TDD→documentation flow with verified results

### Good #2
**Input**: "API returns {user_id: 123} but frontend expects {userId: 123} - test_api_contract failing"  
**Decision**: Read review + API spec in arch → Add response transformer in UserController.js → RED: test fails with old format → GREEN: implement camelCase mapper → REFACTOR: extract to ResponseFormatter util → All contract tests pass → Document in dev notes  
**Why Good**: Respects API contract design, uses TDD, creates reusable solution, maintains backward compatibility

### Good #3
**Input**: "Race condition: concurrent orders create duplicate inventory records - test_concurrent_checkout failing"  
**Decision**: Review report → Check arch (distributed lock pattern required) → Analyze knowledge base → RED: reproduce race with parallel test → GREEN: implement Redis lock at InventoryService.js:L45 → REFACTOR: add timeout + retry logic → Load test passes → Update dev notes with concurrency metrics  
**Why Good**: Diagnoses timing issue via architecture, applies specified pattern, proves fix with load testing, provides performance evidence

### Bad #1
**Input**: "Registration endpoint 500 error - test_create_user failing"  
**Decision**: Add try-catch to suppress error → Skip tests → Mark complete  
**Why Bad**: Masks root cause (violates Constraint 1), skips DoD verification, creates tech debt  
**Correct Approach**: Analyze error → Trace architecture → TDD cycle (RED/GREEN/REFACTOR) → Verify tests → Document

### Bad #2
**Input**: "Payment webhook signature validation fails - test_webhook_auth failing"  
**Decision**: See error mentions "invalid signature" → Google for solution → Copy-paste Stack Overflow code → Test passes locally → Push to prod  
**Why Bad**: No architecture review (may conflict with security design), no understanding of crypto implementation, skips dev notes (violates DoD), no RED phase verification  
**Correct Approach**: Read review → Check arch security specs → Understand HMAC requirements → Write failing test → Implement per spec → Verify all tests → Document algorithm + rollback plan

### Bad #3
**Input**: "User profile update returns stale data - 3 related tests failing"  
**Decision**: Modify 15 files across models/controllers/services without tracking → Some tests pass, some still fail → "I think cache is the issue" → Add cache.clear() everywhere → New tests start failing → Give up, rollback  
**Why Bad**: No systematic approach (violates Step 1), changes too broad without root cause analysis, breaks existing functionality (violates Constraint 3), no progress tracking  
**Correct Approach**: Read review for all 3 failures → Trace data flow in architecture → Identify single root cause (cache invalidation timing) → Create focused fix plan → TDD one issue at time → Track in dev notes: Issue 1 (done)→Issue 2 (done)→Issue 3 (done) → Verify full test suite
