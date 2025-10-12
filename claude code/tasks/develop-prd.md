**GOAl**: Complete all development tasks based on PRD document in one iteration.

## [Input]
  1. "{PRD}" --Product Requirements Document
  2. "{TMPL}/dev-notes-tmpl.yaml" --Development notes template

## [Output]
  1. "{root}/docs/prd-dev-notes.md" --Complete development notes document (Markdown format)
  2. High-quality, tested, refactored code implementation for all PRD tasks highly allign with the architecture design stated
  3. Complete test coverage and test cases

## [Constraints]
  1. Do not leave any PRD tasks incomplete
  2. Do not skip TDD cycle (RED → GREEN → REFACTOR)
  3. Do not modify files outside PRD scope without recording rationale in dev notes
  4. Do not deliver with failing tests (exit code must be 0)
  5. Follow the Development-Guidelines defined in sunnycore_dev

## [Tools]
  1. **sequential-thinking (MCP)**
    - [Step 1: Analyze PRD complexity, identify dependencies and risks]
    - [Step 2-4: Reason about implementation strategies for each TDD phase (RED/GREEN/REFACTOR)]
    - When to use: When need to decompose complex features or evaluate refactoring approaches
  2. **claude-context (MCP)**
    - [Step 1: Search codebase for related modules, dependencies, implementation patterns, and test examples]
    - Query examples: "Where are related modules?" "How is similar functionality implemented?" "What are the test patterns?"
    - [TDD phases: Query reference implementations and test cases for each phase]
  3. **context7 (MCP)**
    - [Step 2-4: When need to call external APIs, query official SDK usage examples]

## [Steps]
  1. Preparation & Strategy
    - Understand all PRD requirements and architecture completely
    - Develop comprehensive TDD implementation strategy
    - Establish progress tracking respecting task dependencies
    - Outcome: Complete strategy and tracking established

  2. TDD Development Cycle
    - RED: Write all tests, ensure they fail with expected errors
    - GREEN: Implement minimal code to pass all tests
    - REFACTOR: Improve code quality while maintaining green tests
    - Outcome: All PRD features implemented with high quality

  3. Integration Testing & Validation
    - Execute complete test suite with all tests passing
    - Validate all PRD acceptance criteria met
    - Handle test failures with iterative fixes
    - Outcome: Full integration verified and acceptance criteria met

  4. Documentation
    - Create comprehensive development notes document
    - Document all technical decisions and deviations
    - Outcome: Complete dev notes at "{root}/docs/prd-dev-notes.md"

  5. Final Verification
    - Verify all requirements satisfied with implementation
    - Confirm code quality and test coverage standards met (≥80%)
    - Outcome: All requirements delivered with quality standards met

## [Error-Handling]
  1. PRD file not found: Report error and halt execution
  2. Test failures in RED phase that don't fail correctly: Fix test logic and retry
  3. Test failures in GREEN phase: Analyze failure, fix implementation, retry
  4. Test failures in REFACTOR phase: Rollback refactoring, re-evaluate strategy
  5. Integration test failures: Identify root cause, fix specific implementation, re-run integration tests

## [DoD]
  - [ ] All PRD requirements implemented through full TDD cycle (RED → GREEN → REFACTOR) with all tests passing
  - [ ] Code quality meets standards (SOLID, DRY, functions ≤50 lines, coverage ≥80%)
  - [ ] Complete development notes at "{root}/docs/prd-dev-notes.md"

## [Example]

### Example 1: User Profile Update Feature
[Input]
- PRD: docs/PRD.md with REQ-001 (update profile), REQ-002 (avatar upload), NFR-001 (< 200ms response)
- Tasks: Task-1 (profile API), Task-2 (avatar storage)
- Template: dev-notes-tmpl.yaml

[Decision]
- Create todo list: Task-1 → Task-2 (avatar depends on profile)
- RED: Write tests for PUT /profile, POST /profile/avatar; tests fail
- GREEN: Implement profile update endpoint, S3 avatar upload; tests pass
- REFACTOR: Add input validation, optimize image processing, ensure tests stay green

[Expected Outcome]
- Code: src/api/profile.js, src/services/AvatarService.js, tests/
- docs/prd-dev-notes.md documenting all tasks implementation
- All PRD acceptance criteria met, integration tests pass, coverage ≥ 80%

### Example 2: API Rate Limiting
[Input]
- PRD: docs/PRD.md with REQ-001 (rate limit per user), NFR-001 (100 req/min), NFR-002 (Redis storage)
- Tasks: Task-1 (rate limit middleware), Task-2 (limit configuration), Task-3 (monitoring)
- Template: dev-notes-tmpl.yaml

[Decision]
- RED: Write tests for rate limit enforcement, exceed limit scenario, reset after window; tests fail
- GREEN: Implement Redis-based token bucket algorithm, Express middleware; tests pass
- REFACTOR: Add configurable limits per endpoint, monitoring metrics, maintain green tests

[Expected Outcome]
- Code: src/middleware/rateLimiter.js, config/limits.json, tests/rateLimiter.test.js
- docs/prd-dev-notes.md with rate limiting algorithm explanation
- All NFRs verified (100 req/min enforced), monitoring dashboard functional

### Example 3: Multi-language Support
[Input]
- PRD: docs/PRD.md with REQ-001 (i18n support), REQ-002 (language detection), REQ-003 (translation API)
- Tasks: Task-1 (i18n setup), Task-2 (auto-detection), Task-3 (translation endpoint)
- Template: dev-notes-tmpl.yaml

[Decision]
- RED: Tests for language switching, translation loading, fallback to default; tests fail
- GREEN: Implement i18next integration, Accept-Language header parsing, translation API; tests pass
- REFACTOR: Add translation caching, lazy loading, optimize bundle size

[Expected Outcome]
- Code: src/i18n/config.js, src/api/translations.js, locales/*.json
- docs/prd-dev-notes.md documenting i18n architecture
- All tasks complete, language switching works, test coverage ≥ 80%
