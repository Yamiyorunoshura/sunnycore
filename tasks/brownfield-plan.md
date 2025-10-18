**GOAL**: Fix code that failed review based on feedback with complete quality assurance and operational readiness.

## [Context]
**You must read the following context in order:**
- `{TMPL}/dev-notes-tmpl.yaml` - Template structure and guidance for documentation
- `{DEVNOTES}/{task_id}-dev-notes.md` - What was implemented in the last development cycle
- `{REVIEW}/{task_id}-review.md` - What issues were found and need fixing
- `{ARCH}/*.md`(Only the related documents) - System architecture and design specifications
- `{KNOWLEDGE}/*.md` (if exist) - Approved patterns and solutions

## [Input-Validation]
- You **MUST** verify that all required inputs exist before proceeding with any work.
- **IF** `{REVIEW}/{task_id}-review.md` is missing, you **MUST RETURN** an uncertainty message: "Cannot proceed without review report at {REVIEW}/{task_id}-review.md. Please provide the review findings."
- **IF** `{DEVNOTES}/{task_id}-dev-notes.md` is missing, you **MUST RETURN** an uncertainty message: "Cannot proceed without development notes at {DEVNOTES}/{task_id}-dev-notes.md. Please provide the original implementation notes."
- **IF** `{ARCH}/*.md`(Only the related documents) is missing or incomplete, you **MUST RETURN** an uncertainty message: "Cannot proceed without architecture specifications at {ARCH}/. Please provide the complete architecture documentation."
- You **MUST NOT** guess or assume any missing specifications.
- You **MUST NOT** proceed without a complete input set.

## [Products]
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

## [Steps]
**Follow this high-level workflow:**

1. **Validate Inputs**: Verify all required files exist (`{DEVNOTES}`, `{REVIEW}`, `{ARCH}`). If missing, return uncertainty message.

2. **Understand Context**: Read dev notes (what was done) → review report (what failed) → architecture (what should be done).

3. **Analyze Root Causes**: Connect the three sources to create Root-cause Traceability Table.

4. **Plan Changes**: Create Diff Summary for each fix with minimal, surgical scope.

5. **Implement Fixes**: Follow TDD cycle (RED → GREEN → REFACTOR) for each fix.

6. **Verify Quality Gates**: Run full test suite, check coverage, static analysis, contract tests, performance.

7. **Add Observability**: Instrument critical paths with logs, metrics, traces, and alerts.

8. **Update Documentation**: Add Brownfield Fix Details section to dev notes following template structure.

## [Instructions]

### 1. How to Understand Context (Step 2 Details)

**Read in this order to build complete understanding:**

**1.1 Read Dev Notes (`{DEVNOTES}/{task_id}-dev-notes.md`):**
- **Purpose**: Understand what was implemented in the original development
- **Key sections to read**:
  - `Implementation Summary` → Overall approach and features delivered
  - `Implementation Details` → Files created/modified, components built
  - `Technical Decisions` → Choices made during development
  - `Testing` → Test coverage baseline and what was verified
- **Extract**: Mental model of "what the last developer did and why"

**1.2 Read Review Report (`{REVIEW}/{task_id}-review.md`):**
- **Purpose**: Identify specific failures and quality issues
- **Key sections to read**:
  - `Acceptance Decision` → Accept/Accept with Changes/Reject and rationale
  - `Detailed Findings` → Each issue with severity, location, evidence
  - `Test Execution Summary` → Which tests failed and why
  - `Alignment Verification` → Requirements not met, architecture deviations
- **Extract**: Complete list of issues that need fixing with their evidence

**1.3 Read Architecture (`{ARCH}/*.md`(Only the related documents)):**
- **Purpose**: Understand correct specifications for each issue
- **For each issue from review, locate**:
  - `Technical Stack` → Verify correct technology/version should be used
  - `Components` → Verify component responsibilities and interfaces
  - `ADRs (Architecture Decision Records)` → Verify which decisions apply
  - `Cross-Cutting Concerns` → Verify security/performance/observability patterns
  - `Requirements Traceability Matrix` → Map requirements to components
- **Extract**: Architecture requirements and patterns for fixing each issue

### 2. How to Analyze Root Causes (Step 3 Details)

**Methodology**: Connect Dev Notes → Review Issues → Architecture Violations

**For each issue in the review report:**
1. **Symptom**: What failed? (from Review "Detailed Findings" or "Test Execution Summary")
2. **Original Implementation**: What did the developer do? (from Dev Notes "Implementation Details" or "Technical Decisions")
3. **Architecture Requirement**: What should have been done? (from Architecture ADRs, Components, or Cross-Cutting Concerns)
4. **Root Cause**: Why is there a gap?
   - Deviation from architecture pattern
   - Missing requirement implementation
   - Logic error or incorrect algorithm
   - Technology misuse or version mismatch
5. **Verification**: How to prove it's fixed? (specific test name or performance metric)

**Create Root-cause Traceability Table:**

| Symptom | Root Cause | Architecture Ref | Changed Files | Affected Tests | Verification Evidence |
|---------|-----------|------------------|---------------|----------------|----------------------|
| {from review findings} | {why it happened} | {ARCH section} | {files:lines} | {test names} | {how to verify} |

**Table columns explained:**
- **Symptom**: Observable failure (test name, error message, metric deviation)
- **Root Cause**: Why it happened (missing validation, wrong algorithm, violated ADR)
- **Architecture Ref**: Which architecture section/ADR was violated (e.g., "ADR-023: Security", "Components/AuthService")
- **Changed Files**: Exact file:line ranges that need modification
- **Affected Tests**: Which tests verify this fix
- **Verification Evidence**: How to prove fix works (test output, metrics, log excerpts)

### 3. How to Plan Changes (Step 4 Details)

**Goal**: Minimal, surgical changes that directly address root causes

**For each root cause, create a Diff Summary:**

- **File**: `path/to/file.ext`
- **Lines**: L{start}-{end}
- **Issue**: {issue identifier from review}
- **Root Cause**: {from traceability table}
- **Fix Strategy**: {what to change and why}
- **Architecture Alignment**: {which ADR/component/pattern this follows}
- **Impact**: {critical path / shared module / isolated feature}

**Change Planning Principles:**
- **Surgical Focus**: Change only what's necessary to fix the root cause
- **Architecture Alignment**: Every change must reference an architecture requirement
- **Impact Assessment**: Classify each change (critical path / shared module / isolated)
- **Test Coverage**: Identify existing tests that verify the fix
- **Minimal Scope**: Prefer modifying existing code over rewriting

### 4. How to Implement Fixes (Step 5 Details)

**For each fix in the Diff Summary:**

1. **RED Phase**: 
   - Run the failing test identified in review
   - Confirm it fails with expected error
   - Document failure output

2. **GREEN Phase**:
   - Implement minimal fix per Diff Summary
   - Run test again → must pass
   - Do NOT refactor yet

3. **REFACTOR Phase**:
   - Clean up code while keeping test green
   - Run test after each refactor → must stay green
   - Apply architecture patterns

4. **VERIFY Phase**:
   - Run full test suite
   - Confirm no regressions
   - Document all tests passing

**Track progress:**
- [ ] Fix 1: {issue} - RED ✓ GREEN ✓ REFACTOR ✓ VERIFY ✓
- [ ] Fix 2: {issue} - RED ✓ GREEN ✓ REFACTOR ✓ VERIFY ✓

### 5. How to Verify Quality Gates (Step 6 Details)

**Run all quality gates and document results:**

- [ ] **Full test suite**: {pass/fail} ({count} unit + {count} integration + {count} e2e)
- [ ] **Test coverage**: {percentage}% (baseline: {baseline}%, change: {delta}%)
- [ ] **Static analysis**: {errors count} errors (must be 0)
- [ ] **Contract tests**: {pass/fail} for API/events/messages
- [ ] **Performance**: p95={value}ms (baseline: {baseline}ms, change: {delta}%)
- [ ] **Backward compatibility**: {pass/fail}

**IF any gate fails**:
- Analyze why it failed
- Fix the issue
- Re-verify all gates before proceeding

### 6. How to Add Observability (Step 7 Details)

**For each changed file affecting critical paths:**

**Logs**:
- Add error context with correlation IDs
- Include relevant entity IDs (user_id, order_id, etc.)
- Log at appropriate levels (ERROR, WARN, INFO)

**Metrics**:
- Add success/failure counters (e.g., `auth_attempts_total{status="success|failure"}`)
- Add latency histograms (e.g., `auth_duration_ms`)
- Tag with relevant dimensions

**Traces**:
- Add span tags for failure scenarios
- Include error messages in span attributes
- Link spans with correlation IDs

**Alerts**:
- Define alert conditions (e.g., `error_rate > 1%`, `p99 > 500ms`)
- Document severity and who gets paged
- Include runbook link or quick fix steps

**Document all observability points in dev notes** (see Brownfield Fix Details section in template)

### 7. Performance & Compatibility Standards
- **Performance Budget**: p95 latency ≤ +10%, p99 latency ≤ +20%
- **Load Test**: 2x expected traffic before completion
- **Backward Compatibility**: All contract tests must pass (APIs/events/messages)
- **Breaking Changes**: Must document migration path + deprecation timeline

### 8. Data & Schema Change Requirements
- **Database schema**: Provide migration + rollback scripts
- **API contract**: Update contract tests + bump version
- **Event schema**: Maintain consumer backward compatibility

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
