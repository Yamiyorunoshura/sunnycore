**GOAL**: Initialize development environment and create complete directory structure for the project.

## [Context]
**You must read the following context:**
1. "{ARCH}/*.md" -- Architecture design documents
2. "{TMPL}/instruction-tmpl.yaml" -- Instruction template for CLAUDE.md structure

**Extract from Architecture:**
- Technology stack and specific versions
- Development environment requirements
- Complete directory structure from `work-directory-structure` field
- All modules, components, and services mentioned

## [Products]
1. "{root}/CLAUDE.md" -- Project guidance document
2. Fully initialized development environment
3. Complete directory structure as specified in architecture
4. Indexed codebase (for Brownfield projects only)

## [Constraints]
1. Only use tools and configurations explicitly required in architecture documents
2. Must create document index in CLAUDE.md
3. Must index codebase for Brownfield projects
4. Must follow directory structure from architecture documents exactly

## [Instructions]
1. **Step 1: Analyze Architecture Inputs**
- **GOAL:** Understand every technical requirement and constraint from the architecture set before modifying the environment.
- **STEPS:**
  - Read each architecture document in {ARCH}/*.md.
  - Capture the complete technology stack with mandated version numbers.
  - List environment setup requirements, dependencies, and tooling expectations.
  - Extract the exact `work-directory-structure` specification.
  - Record all modules, components, services, and Brownfield integration notes.
- **QUESTIONS:**
  - Which documents define required versions, tools, or sequencing?
  - Are any prerequisites or external dependencies unclear?
  - Does the architecture call for Brownfield indexing or integrations?
  - Are there ambiguities in the `work-directory-structure` that need clarification?
- **CHECKLIST:**
  - [ ] Tech stack with versions summarized.
  - [ ] Environment and tooling requirements captured.
  - [ ] Directory structure copied verbatim.
  - [ ] Modules, services, and Brownfield notes documented.

2. **Step 2: Configure Development Environment**
- **GOAL:** Build a fully operational environment that matches the architecture specifications.
- **STEPS:**
  - Install each required language, runtime, and framework using the specified versions.
  - Install supporting libraries, CLIs, and tooling called out in the architecture.
  - Provision databases, queues, or infrastructure services and apply required configurations.
  - Configure IDE/editor integrations, linters, formatters, and test runners.
  - Execute smoke commands to confirm every installation works as expected.
- **QUESTIONS:**
  - Do installation steps require platform-specific commands or credentials?
  - Are there environment variables or secrets that must be configured now?
  - What verification commands prove each dependency is healthy?
  - Does Brownfield indexing require additional tools or agents here?
- **CHECKLIST:**
  - [ ] Core runtimes and frameworks installed at specified versions.
  - [ ] Supporting tooling configured and accessible.
  - [ ] Infrastructure services provisioned and reachable.
  - [ ] Smoke checks executed with successful output.
  - [ ] Brownfield indexing tools prepared (if applicable).

3. **Step 3: Build Project Directory Structure**
- **GOAL:** Mirror the architecture's `work-directory-structure` exactly within the workspace.
- **STEPS:**
  - Reference the extracted directory map from Step 1.
  - Create directories using commands that preserve casing and nesting exactly.
  - Avoid inventing or omitting directories beyond what the architecture specifies.
  - Validate permissions and relative paths after creation.
- **QUESTIONS:**
  - Are there conditional directories for Brownfield vs Greenfield scenarios?
  - Do any directories depend on prior environment steps?
  - What verification method best confirms the structure matches the specification?
- **CHECKLIST:**
  - [ ] Each required directory created with correct name and depth.
  - [ ] No extra or missing directories detected.
  - [ ] Directory creation commands or scripts recorded for reuse.

4. **Step 4: Draft CLAUDE.md Guidance**
- **GOAL:** Produce {root}/CLAUDE.md that aligns with `instruction-tmpl.yaml` and reflects current architecture data.
- **STEPS:**
  - Use {TMPL}/instruction-tmpl.yaml to determine required headings and citation rules.
  - Populate each section with facts gathered from architecture and related sources, adding TODOs where data is missing.
  - Document the project tech stack, architecture, standards, workflows, and quality expectations with precise citations.
  - Build a document index that links readers to architecture, requirements, and task files.
- **QUESTIONS:**
  - Which sources supply authoritative data for each template section?
  - Are any sections missing information that should be marked TODO?
  - How should citations be formatted to satisfy the template policy?
  - What documents must appear in the index for discoverability?
- **CHECKLIST:**
  - [ ] All template sections populated or marked with TODO plus next action.
  - [ ] Citations or TODOs present for every bullet.
  - [ ] Document index added with accurate paths.
  - [ ] CLAUDE.md saved at {root}/CLAUDE.md.

5. **Step 5: Validate Initialization Completion**
- **GOAL:** Confirm environment, structure, documentation, and indexing meet readiness criteria.
- **STEPS:**
  - Run validation commands or tests to prove tools, runtimes, and services function.
  - Inspect directory tree against the architecture specification to ensure fidelity.
  - Review CLAUDE.md for completeness, citation compliance, and navigability.
  - Execute Brownfield indexing or search validation if the project requires it.
- **QUESTIONS:**
  - Did every verification command succeed without warnings?
  - Is any directory or documentation element still pending data?
  - Are there project-specific acceptance criteria to revisit before sign-off?
  - Does the Brownfield index respond to sample queries?
- **CHECKLIST:**
  - [ ] Environment and tooling verified operational.
  - [ ] Directory structure matches specification.
  - [ ] CLAUDE.md content and index confirmed.
  - [ ] Brownfield indexing complete and validated (if required).
  - [ ] Outstanding issues documented with next steps.

## [Quality Standards]

**Environment Quality:**
- All dependencies install without errors
- Version numbers match architecture specifications exactly
- Tools run successfully (can execute test commands, linters, etc.)

**Directory Quality:**
- Structure matches `work-directory-structure` exactly
- No assumed or extra directories
- All paths are correctly formed

**Documentation Quality:**
- CLAUDE.md follows template structure
- All sections populated with accurate information
- Every statement cites source file or marked TODO
- Document index includes all relevant files

**Brownfield Quality:**
- Codebase fully indexed
- Index is searchable and returns relevant results
- Integration points with existing code identified

## [Example]

### Microservices Platform with Docker

**Input:**
- Architecture specifies: Node.js v18, PostgreSQL 15, Redis 7, Docker
- Directory structure: src/, services/, config/, docker/, tests/
- Modules: UserService, OrderService, PaymentService

**Execution:**

**Step 1 - Analyze:**
- Read architecture, extract tech stack table
- Note directory structure requirement
- Identify 3 services to scaffold

**Step 2 - Setup Environment:**
```bash
# Install Node.js v18
# Install Docker and docker-compose
# Install PostgreSQL client
# Verify installations
node --version  # v18.x.x
docker --version
psql --version  # 15.x
```

**Step 3 - Create Directories:**
```
project/
├── src/
├── services/
│   ├── user-service/
│   ├── order-service/
│   └── payment-service/
├── config/
├── docker/
└── tests/
```

**Step 4 - Generate CLAUDE.md:**
```markdown
# Project Info
- Name: Microservices Platform
- Stack: Node.js, PostgreSQL, Redis, Docker
- Source: docs/architecture/tech-stack.md

# Tech Stack
| Technology | Version | Purpose |
|------------|---------|---------|
| Node.js | 18.x | Runtime |
| PostgreSQL | 15 | Database |
| Redis | 7 | Cache |
| Docker | latest | Containerization |

# Key Architecture
- Microservices pattern
- 3 services: User, Order, Payment
- REST APIs for communication
- Source: docs/architecture/system.md

# Document Index
- Architecture: docs/architecture/*.md
- Requirements: docs/requirements/*.md
- Tasks: docs/tasks/*.md
```

**Step 5 - Verify:**
- ✅ Environment: All tools installed
- ✅ Directories: All created per architecture
- ✅ CLAUDE.md: Complete with document index
- ✅ Ready for development

**Outcome:**
- Fully initialized environment
- Complete directory structure
- Comprehensive CLAUDE.md
- Ready to begin implementation
