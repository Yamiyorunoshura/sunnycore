**GOAL**: Fix code that failed review based on feedback with complete quality assurance and operational readiness.

## [Input]
- `{TMPL}/dev-notes-tmpl.yaml`
- `{REVIEW}/{task_id}-review.md`
- `{ARCH}/*.md`
- `{KNOWLEDGE}/*.md` (if exist)

## [Input-Validation]
- You **MUST** verify that all required inputs exist before proceeding with any work.
- **IF** `{REVIEW}/{task_id}-review.md` is missing, you **MUST RETURN** an uncertainty message along with the required information needed.
- **IF** `{ARCH}/*.md` is missing or incomplete, you **MUST RETURN** an uncertainty message along with the required architecture specifications.
- You **MUST NOT** guess or assume any missing specifications.
- You **MUST NOT** proceed without a complete input set.

## [Output]
- Fixed code (all quality gates passing)
- Root-cause Traceability Table
- Change Diff Summary
- Updated `{DEVNOTES}/{task_id}-dev-notes.md` with observability points
- Migration/Rollback scripts (if applicable)

## [Constraints]
- You **MUST** implement fixes that pass all tests. You **MUST NOT** deliver non-functional code.
- You **MUST** follow architecture specifications and [develop-guidelines]. You **MUST NOT** deviate from design specifications.
- You **MUST** preserve existing functionality. You **MUST NOT** introduce breaking changes.
- You **MUST** use only approved code from this repository or `{KNOWLEDGE}`. You **MUST NOT** use external or unreviewed code snippets.
- You **MUST** maintain backward compatibility for public APIs and events. You **MUST NOT** break contracts.
- You **MUST** stay within the performance budget. You **MUST NOT** degrade p95 latency by more than 10%.

## [Instructions]

### 1. Root Cause Analysis
You must create a **Root-cause Traceability Table** with the following columns:
| Symptom | Root Cause | Changed Files | Affected Tests | Verification Evidence |
|---------|-----------|---------------|----------------|----------------------|
| Description of failure | Underlying issue | file.js:L10-25 | test_name | Screenshot/log link |

This table establishes complete traceability from observed symptoms to root causes, changed files, affected tests, and verification evidence.

### 2. Change Documentation
For each modification, you must provide a **Diff Summary** that includes:
- File: `path/to/file.js`
- Lines: L45-67
- Reason: Fix race condition per architecture requirement ADR-023
- Impact: Critical path (checkout flow)

This summary documents the exact scope of changes, the rationale tied to architecture requirements, and the impact on critical paths.

### 3. Performance & Compatibility
- **Performance Budget**: The p95 latency must not increase by more than 10%, and p99 latency must not increase by more than 20%.
- **Load Test**: You must run load tests with 2x the expected traffic before marking the task as complete.
- **Backward Compatibility**: All contract tests for APIs, events, and messages must pass.
- **Breaking Changes**: If breaking changes are unavoidable, you must document both the migration path and the deprecation timeline.

### 4. Data & Schema Changes
- **IF** the database schema is modified, you must provide both migration **AND** rollback scripts.
- **IF** the API contract is changed, you must update the contract tests and bump the version number.
- **IF** the event schema is changed, you must ensure consumer backward compatibility is maintained.

### 5. Observability & Operations
You **MUST** add observability signals to all changed critical paths:
  - **Logs**: Include error context and correlation IDs to enable debugging and request tracing.
  - **Metrics**: Implement success/failure counters and latency histograms to track performance.
  - **Traces**: Add span tags for failure scenarios to enable distributed tracing.

You **MUST** document alert conditions (e.g., error_rate > 1%, p99 > 500ms) so operators know when to respond.

You **MUST** record all observability points in the dev notes for future reference and operational support.

## [Steps]
1. **Validate Inputs**: Verify that all required files (`{REVIEW}`, `{ARCH}`, `{KNOWLEDGE}`) exist. If any are missing, return an uncertainty message. This ensures you have a complete input set before proceeding.

2. **Analyze Root Causes**: Read the review report and architecture documentation. Create a Root-cause Table that maps all issues with complete traceability from symptoms to evidence.

3. **Plan Changes**: Draft a Diff Summary for each fix. This documents the change scope including file paths, line ranges, rationale, and impact.

4. **TDD Cycle**: Follow the RED→GREEN→REFACTOR cycle while tracking test coverage. Ensure all tests are passing and coverage has not decreased from the baseline.

5. **Quality Gates**: Run the full test suite including static analysis and contract tests. Verify that all gates are green before proceeding.

6. **Performance Validation**: Execute load tests and verify that latency increases are less than 10% for p95. Confirm that the performance budget is met.

7. **Observability**: Add logs, metrics, and traces to all changed critical paths. Ensure monitoring is ready for production deployment.

8. **Document**: Update `{DEVNOTES}` with the Root-cause Table, Diff Summary, observability points, and verification evidence. This creates a complete audit trail for future reference.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Full test suite passed (unit + integration + e2e)
- [ ] Changed code coverage ≥ baseline (no decrease)
- [ ] Static analysis: 0 errors (linter + type checker)
- [ ] Contract tests: all green (API/events/messages)
- [ ] Performance budget: p95 latency increase ≤10%, p99 ≤20%
- [ ] Backward compatibility: verified for public interfaces
- [ ] Observability: critical paths instrumented with logs/metrics/traces
- [ ] Migration scripts: tested (both up + down) if DB/schema changed
- [ ] Root-cause Table: complete with verification evidence
- [ ] Dev notes: updated with complete traceability

## [Example]

### Good #1: Token Validation Fix
**Input**: "Auth token validation fails - test_expired_token_rejection failing"  

**Decision**: 
1. Validated inputs: Both the review and architecture files exist ✓
2. Created Root-cause Table:
   | Symptom | Root Cause | Changed Files | Affected Tests | Evidence |
   |---------|-----------|---------------|----------------|----------|
   | Expired tokens accepted | Missing expiry check in validator | TokenValidator.js:L25-30 | test_expired_token_rejection | Test log showing token.exp not validated |
3. Documented Diff Summary: `TokenValidator.js:L25-30` - Added JWT expiry validation per security-arch.md Section 4.2
4. Completed TDD cycle: All tests pass, coverage increased from 95% to 97%
5. Added observability: Implemented "token_expired" event logs with correlation_id, added metric: `auth_rejection_reason{reason="expired"}`
6. Updated dev notes with Root-cause Table and observability points

**Why Good**: This example demonstrates complete input validation, proper traceability table creation, observability implementation, and passes all quality gates.

### Good #2: API Contract Compatibility
**Input**: "API returns {user_id: 123} but frontend expects {userId: 123} - test_api_contract failing"  

**Decision**: 
1. Validated inputs: The review shows contract violation, and the architecture defines camelCase standard ✓
2. Created Root-cause Table:
   | Symptom | Root Cause | Changed Files | Affected Tests | Evidence |
   |---------|-----------|---------------|----------------|----------|
   | Frontend parse error | snake_case response violates API spec | UserController.js:L78<br>ResponseFormatter.js (new) | test_api_contract<br>test_user_get_response | Contract test diff showing case mismatch |
3. Documented Diff Summary: 
   - `UserController.js:L78` - Applied ResponseFormatter to User endpoints
   - `ResponseFormatter.js` (new) - Created reusable snake→camel converter
4. Completed TDD cycle: RED (old format fails), GREEN (mapper works), REFACTOR (extracted util)
5. Verified contract tests: All 12 API contracts are green ✓
6. Ensured backward compatibility: Added `?response_format=snake_case` query parameter for legacy clients (deprecated in 6 months)
7. Added metric: `api_response_format{format="camel|snake"}` for migration tracking
8. Updated dev notes: Included Root-cause Table, deprecation timeline, and monitoring query

**Why Good**: This example maintains backward compatibility, verifies all contract tests, documents the migration path, and provides observability for rollout tracking.

### Good #3: Concurrency Fix with Performance Budget
**Input**: "Race condition: concurrent orders create duplicate inventory records - test_concurrent_checkout failing"  

**Decision**: 
1. Validated inputs: The review, architecture (ADR-045: Redis distributed lock), and knowledge base all exist ✓
2. Created Root-cause Table:
   | Symptom | Root Cause | Changed Files | Affected Tests | Evidence |
   |---------|-----------|---------------|----------------|----------|
   | Duplicate inventory records on concurrent checkout | Missing distributed lock per ADR-045 | InventoryService.js:L45-89<br>RedisLockManager.js (new) | test_concurrent_checkout<br>test_inventory_consistency | Load test logs showing 2 orders decrementing same record |
3. Documented Diff Summary:
   - `InventoryService.js:L45-89` - Wrapped reserve() in Redis lock with 5s timeout
   - `RedisLockManager.js` (new) - Created reusable lock manager with retry logic
4. Completed TDD cycle: RED (reproduced with 50 parallel requests), GREEN (lock prevents race), REFACTOR (extracted manager and added retry logic)
5. Validated performance:
   - Before: p95=120ms, p99=180ms
   - After: p95=125ms (+4.2%), p99=195ms (+8.3%) ✓ Within budget
   - Load test: 2x traffic (1000 req/s) sustained for 5 minutes, 0 duplicates ✓
6. Added observability:
   - Log: `inventory.lock_acquired`, `inventory.lock_timeout` with order_id
   - Metric: `inventory_lock_duration_ms`, `inventory_lock_failures_total`
   - Trace: Span tag `lock.wait_time_ms`
   - Alert: `inventory_lock_failures_total > 10/min` triggers page to oncall
7. Updated dev notes: Included Root-cause Table, performance metrics, lock timeout tuning rationale, and alert runbook

**Why Good**: This example follows the architecture decision record, proves the fix with load testing, stays within the performance budget, provides complete observability, and includes an operational runbook.

### Bad #1: Missing Input Validation
**Input**: "Registration endpoint 500 error - test_create_user failing"  

**Bad Decision**: Noticed that the review file is missing, assumed it's a validation error from the stack trace, added try-catch to suppress the error, skipped tests, and marked the task as complete.

**Why Bad**: 
- Violates [Input Validation]: Proceeds without the required `{REVIEW}` file
- No Root-cause Table was created (violates Quality Gates)
- Masks the root cause (violates Constraint 1)
- No observability was added to the critical registration path
- Skips Quality-Gate verification and creates technical debt

**Correct**: First validate all inputs. When `{REVIEW}` is found missing, immediately RETURN an uncertainty message: "Cannot proceed without {REVIEW}/{task_id}-review.md. Please provide the review report specifying the root cause of the 500 error."

### Bad #2: External Unreviewed Code
**Input**: "Payment webhook signature validation fails - test_webhook_auth failing"  

**Bad Decision**: Saw the error message mentions "invalid signature", Googled for a solution, copy-pasted Stack Overflow HMAC code, verified the test passes locally, and pushed to production without observability.

**Why Bad**: 
- Uses external unreviewed code (violates Constraint 4: MUST use only approved repository or knowledge code)
- No architecture review was conducted (may conflict with security design per PCI-DSS requirements)
- No Root-cause Table or Diff Summary was created
- No observability was added: payment failures are on the critical path but no alerts were implemented
- Skips contract tests and backward compatibility checks
- No understanding of the crypto implementation creates a security risk

**Correct**: First read the review, then check the architecture security specifications (which specify to use the crypto library approved in {KNOWLEDGE}/security-libs.md). Create a Root-cause Table identifying that the webhook signature doesn't match the computed HMAC-SHA256. Implement the fix using the approved library per specification. Add observability by logging validation failures with webhook_id and adding the metric `webhook_auth_failures_total`. Ensure all contract tests pass. Finally, document the algorithm, alert conditions, and rollback plan.

### Bad #3: No Traceability or Performance Validation
**Input**: "User profile update returns stale data - 3 related tests failing"  

**Bad Decision**: Modified 15 files across models/controllers/services without tracking changes. Some tests passed while others still failed. Guessed "I think cache is the issue" and added cache.clear() everywhere. New tests started failing, and P95 latency jumped from 80ms to 450ms. No performance tests were run before giving up and rolling back.

**Why Bad**: 
- No systematic approach was followed (violates Step 1: Analyze Root Causes)
- No Root-cause Table was created, resulting in changes that were too broad without proper root cause analysis
- Broke existing functionality (violates Constraint 3)
- Violated the performance budget with a +462% latency increase (violates Quality Gates: ≤10% allowed)
- No Diff Summary was created, resulting in no progress tracking
- No observability was added, making it impossible to diagnose cache behavior
- No migration plan was created for the cache invalidation strategy change

**Correct**: 
1. Validate inputs: Confirmed that all required files exist ✓
2. Read the review for all 3 failures and trace the data flow in the architecture. Create a Root-cause Table:
   | Symptom | Root Cause | Changed Files | Affected Tests | Evidence |
   |---------|-----------|---------------|----------------|----------|
   | Stale user.name | Cache TTL too long per review | CacheConfig.js:L12 | test_update_name | Cache shows 1h TTL, arch requires 5min |
   | Stale user.avatar | Cache key missing user_id | UserCache.js:L34 | test_update_avatar | Cache key collision found |
   | Profile GET stale | No cache invalidation on PUT | UserController.js:L67 | test_update_flow | Missing invalidate() call |
3. Identify the single root cause: Cache invalidation timing combined with incorrect key strategy
4. Create a focused fix plan with Diff Summary covering only 3 files and 8 lines total
5. Apply TDD one issue at a time and track progress in dev notes: Issue 1 (done), Issue 2 (done), Issue 3 (done)
6. Validate performance: p95=78ms (-2.5%) ✓, p99=115ms (no change) ✓
7. Add observability: Implement cache hit/miss metrics and invalidation event logs
8. Verify the full test suite and all quality gates pass ✓
