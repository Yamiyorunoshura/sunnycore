**GOAL**: Produce an actionable `CLAUDE.md` playbook that equips Claude Code with the minimum viable context to work safely and fast.

## [Input]
  1. "{ARCH}/*.md" — Architecture decisions, directory maps, deployment guidance
  2. "{REQ}/*.md" — Business goals, user journeys, acceptance criteria
  3. "README.md" and top-level docs — High-level positioning, onboarding notes
  4. Repository manifests (e.g., package.json, pyproject.toml, Dockerfile) — Concrete tech stack evidence
  5. Existing standards docs under "{root}/docs" (if present) — Style, testing, review conventions
  6. "{TMPL}/instruction-tmpl.yaml"

## [Output]
  1. "{root}/CLAUDE.md" generated from `instruction-tmpl.yaml` and containing the following top-level sections (no reordering):
     - Project Info
     - Tech Stack
     - Key Architecture
     - Coding Standard
  2. Every fact in the document cites its source file (inline parenthetical references are fine)
  3. Unknown or missing information is clearly marked as TODO for the human team

## [Constraints]
  1. Capture only verified facts; do not speculate or infer unstated tooling
  2. Summaries must stay concise (bullet lists or short paragraphs)
  3. Highlight mismatches between documents as TODO items rather than resolving them
  4. Preserve existing headings or anchors if CLAUDE.md already exists; update content in place

## [Procedure]
  1. Discovery
     - Assemble primary facts from the input sources, starting with architecture → requirements → manifests
     - Record exact file paths or section headers used for each fact
  2. Synthesis
     - Draft each section with bullet lists that answer: what, why, and how it affects day-to-day coding
     - Surface critical dependencies, integration points, and expectations that shape developer workflow
  3. Template Application
     - Populate `instruction-tmpl.yaml` verbatim for headings, expanding bullets as needed
     - Flag unknown items as `TODO: question` to prompt follow-up
  4. Review
     - Re-read the compiled CLAUDE.md for clarity and actionable tone
     - Confirm every section can be understood without opening the source documents

## [Instruction Template]
Canonical template lives at `instruction-tmpl.yaml` (mirrored here for quick reference).
```markdown
# Project Info
- Name:
- Mission:
- Stakeholders:
- Current status:
- Relevant timelines or milestones:

# Tech Stack
- Languages and frameworks:
- Runtime environments & hosting:
- Tooling & services (CI/CD, observability, integrations):
- Data storage & messaging:

# Key Architecture
- System overview:
- Core components/modules:
- Data flow & critical integrations:
- Deployment topology:
- Operational considerations:

# Coding Standard
- Style guides & linting rules:
- Testing strategy & quality gates:
- Branching, review, and release process:
- Documentation expectations:
```

## [DoD]
  - [ ] `CLAUDE.md` exists and follows the headings from `instruction-tmpl.yaml` in order
  - [ ] Each bullet either states a sourced fact or a TODO with next step
  - [ ] Conflicting or missing information is called out for humans to resolve
  - [ ] Final document is scannable (no paragraphs longer than five sentences)
