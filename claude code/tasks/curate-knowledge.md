<input>
  <context>
  1. {root}/docs/review-results/*.md - Code Review results and practice level assessments.
  2. {root}/docs/dev-notes/*.md - Development Notes capturing error cases and fixes.
  </context>
  <templates>
  1. {root}/sunnycore/project-knowledge-tmpl.yaml - Project knowledge base structure template.
  </templates>
</input>

<output>
1. {root}/docs/project-knowledge.md - Consolidated Project Knowledge Base summarizing Error Cases and Best Practices with source references.
  Format: Markdown (UTF-8); human-readable; file path must resolve within repo.
  Example:
  - Title: Project Knowledge Base
  - Sections: Error Cases | Best Practices | Source References
  - Link style: relative paths (e.g., docs/review-results/file.md)
</output>

<constraints importance="Important">
- MUST: Derive content strictly from provided files; do not invent information.
- MUST: Cite source file paths for each best practice and error case.
- MUST: Align sections and fields to the template structure.
- MUST: Keep all prompt sections in English; ascii_letter_ratio_v1 ≥ 0.95.
- SHOULD: Prefer concise bullet points; average sentence length < 20 words.
</constraints>

<workflow importance="Important">
  <stage id="1: conclude_review_results">
  <tools>
    <tool name="sequential_thinking"/>
    <tool name="todo_write"/>
  </tools>
  - Read the review results.
  - Extract best practices and error cases with file references.
  - Summarize patterns and practice levels if available.
  Deliverable: Evidence set of best practices/error cases with source references and pattern summary.

  <questions>
  - Are there repeated failure patterns across files?
  - Which practices have clear acceptance criteria?
  </questions>
  </stage>

  <stage id="2: conclude_development_notes">
  <tools>
    <tool name="sequential_thinking"/>
    <tool name="todo_write"/>
  </tools>
  - Read the development notes.
  - Extract best practices and error cases with file references.
  - Normalize naming for similar issues.
  Deliverable: Normalized catalogue of best practices and error cases with citations.
  </stage>

  <stage id="3: curate_knowledge">
  <tools>
    <tool name="sequential_thinking"/>
    <tool name="todo_write"/>
  </tools>
  - Use the project knowledge template to structure content.
  - Output to {root}/docs/project-knowledge.md in Markdown.
  - Ensure cross-references and links resolve.
  Deliverable: Generated {root}/docs/project-knowledge.md with validated links and references.

  <checks>
  - [ ] All required sections from the template are present.
  - [ ] Each item cites at least one source file path.
  - [ ] No unverifiable claims or missing references.
  - [ ] Links and paths resolve within the repo.
  </checks>
  </stage>
</workflow>

