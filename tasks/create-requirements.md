**GOAL**: Create detailed functional and non-functional requirements documentation.

## [Input]
- `{TMPL}/requirement-tmpl.yaml`
- User-provided ideas and descriptions

## [Output]
- `{root}/docs/requirements.md` (temporary, will be sharded)
- `{REQ}/*.md`

## [Constraints]
- **MUST** create measurable requirements, **MUST NOT** create vague ones
- **MUST** follow template structure, **MUST NOT** deviate
- **MUST** exclude sensitive data in examples, **MUST NOT** include
- **MUST** execute shard-requirements.py, **MUST NOT** skip

## [Steps]
1. Define requirements gathering scope → Scope clearly defined
2. Extract complete, deduplicated functional requirements → Complete functional requirements documented
3. Define quantified non-functional requirements → Quantified non-functional requirements established
4. Create testable acceptance criteria (Given-When-Then) → All requirements have acceptance criteria
5. Ensure consistency, obtain approval, run shard-requirements.py → Approved requirements sharded successfully

## [DoD]
- [ ] Functional and non-functional requirements with quantified metrics and Given-When-Then criteria
- [ ] Requirements sharded to "{REQ}/*.md" using shard-requirements.py
- [ ] Final requirement set approved by user

## [Example]

### Good #1
**Input**: "Customers search products by category, price, ratings with fast response"  
**Decision**: Define scope: product search→Extract functional: REQ-001 (category filter UI+logic), REQ-002 (price range slider+query), REQ-003 (rating filter 1-5 stars)→Deduplicate and atomize→Define NFRs: NFR-001 (P95 <500ms), NFR-002 (100 concurrent users)→Quantify→Acceptance: Given user on product page, When applies category "Electronics" and price "$100-$500", Then returns filtered results <500ms→Binary pass/fail→Generate requirements.md→Approval→Shard to functional.md and non-functional.md  
**Why Good**: Turns vague request into atomic, measurable requirements with explicit acceptance tests

### Good #2
**Input**: "Send real-time notifications to iOS/Android when events occur with high reliability"  
**Decision**: Define scope: push notification system→Functional: REQ-001 (event subscription), REQ-002 (cross-platform delivery iOS/Android), REQ-003 (notification templates)→Organized by capabilities→NFRs: NFR-001 (<2s latency), NFR-002 (99.9% delivery success), NFR-003 (10K notifications/min)→All quantified→Acceptance: Given event occurs, When notification sent, Then delivered within 2s→Approval→Shard successfully  
**Why Good**: Captures functional breadth and demanding NFRs, eliminates ambiguity

### Bad #1
**Input**: Multiple vague ideas  
**Bad Decision**: Create vague: "REQ-001: user-friendly", "NFR-001: fast system"→No quantification→No Given-When-Then→Mix functional and non-functional→Skip deduplication→No sharding→Save as single file without template  
**Why Bad**: Vague unmeasurable requirements, not verifiable, no clear success criteria, "user-friendly" and "fast" not testable  
**Correct**: Transform "user-friendly" to specific REQ: "Users complete checkout in ≤3 clicks"→Transform "fast" to quantified NFR: "API P95 <200ms"→Given-When-Then→Separate functional from non-functional→Execute shard-requirements.py
