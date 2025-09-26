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
</output>

<constraints importance="Important">
- Derive content strictly from provided files; do not invent information.
- Cite source file paths for each best practice and error case.
- Align sections and fields to the template structure.
- Prefer concise bullet points; average sentence length < 20 words.
</constraints>

<workflow importance="Important">
  <stage id="1: conclude_review_results">
  <tools>
  - read_file: Load and analyze review results documents
  - grep: Search for recurring patterns across review files
  </tools>
  - Read the review results.
  - Extract best practices and error cases with file references.
  - Summarize patterns and practice levels if available.

  <questions>
  - Are there repeated failure patterns across files?
  - Which practices have clear acceptance criteria?
  </questions>
  </stage>

  <stage id="2: conclude_development_notes">
  <tools>
  - read_file: Load and analyze development notes documents
  - grep: Extract error patterns and solutions across dev notes
  </tools>
  - Read the development notes.
  - Extract best practices and error cases with file references.
  - Normalize naming for similar issues.
  </stage>

  <stage id="3: curate_knowledge">
  <tools>
  - read_file: Load project knowledge template
  - write: Generate consolidated project knowledge documentation
  </tools>
  - Use the project knowledge template to structure content.
  - Output to {root}/docs/project-knowledge.md in Markdown.
  - Ensure cross-references and links resolve.

  <checks>
  - [ ] All required sections from the template are present.
  - [ ] Each item cites at least one source file path.
  - [ ] No unverifiable claims or missing references.
  - [ ] Links and paths resolve within the repo.
  </checks>
  </stage>
</workflow>

