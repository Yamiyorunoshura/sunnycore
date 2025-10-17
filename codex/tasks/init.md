**GOAL**: Initialize development environment and create complete directory structure for the project.

## [Context]
**You must read the following context:**
1. "{ARCH}/*.md" -- Architecture design documents
2. "{TMPL}/instruction-tmpl.yaml" -- Instruction template for AGENTS.md structure

**Extract from Architecture:**
- Technology stack and specific versions
- Development environment requirements
- Complete directory structure from `work-directory-structure` field
- All modules, components, and services mentioned

## [Products]
1. "{root}/AGENTS.md" -- Project guidance document
2. Fully initialized development environment
3. Complete directory structure as specified in architecture
4. Indexed codebase (for Brownfield projects only)

## [Constraints]
1. Only use tools and configurations explicitly required in architecture documents
2. Must create document index in AGENTS.md
3. Must index codebase for Brownfield projects
4. Must follow directory structure from architecture documents exactly

## [Steps]

### 1. Analyze Architecture
**Objective:** Understand project requirements and technical specifications.

**Actions:**
- Read all architecture documents in {ARCH}/*.md
- Extract technology stack with specific versions
- Identify all environment setup requirements
- Extract complete directory structure from `work-directory-structure`
- Identify all modules, components, and services
- Note any Brownfield integration requirements

**Focus:** Ensure complete understanding before proceeding. This prevents rework.

### 2. Setup Development Environment
**Objective:** Configure fully operational development environment.

**Actions:**
- Install required languages and runtimes (exact versions from architecture)
- Install frameworks and dependencies
- Setup databases, message queues, or other infrastructure
- Configure development tools (linters, formatters, test runners)
- Verify all installations are functional

**For Brownfield Projects:**
- Index existing codebase using appropriate indexing tool
- Verify index is searchable

**Focus:** Environment must be production-ready. All dependencies installed and verified.

### 3. Create Directory Structure
**Objective:** Establish complete project directory structure.

**Actions:**
- Extract directory structure from `work-directory-structure` in architecture
- Create all specified directories exactly as documented
- Do not assume or modify the structure
- Verify all directories are created

**Focus:** Directory structure is the foundation. Follow architecture specification exactly.

### 4. Generate Project Guidance (AGENTS.md)
**Objective:** Create comprehensive project reference document.

**How to Create AGENTS.md:**
- Use "{TMPL}/instruction-tmpl.yaml" as your guide for structure
- Read architecture documents to extract accurate information
- Include all required sections from template

**What to Include:**
- **Project Info:** Name, mission, status, key timelines (from architecture/requirements)
- **Tech Stack:** All technologies with versions (from architecture tech stack section)
- **Key Architecture:** System components, data flow, integrations (from architecture)
- **Coding Standard:** Style guides, linting, testing requirements (from architecture or use common standards for the tech stack)
- **Development Workflow:** Task execution process, version control, quality gates (from project standards)
- **Quality Standards:** Code quality criteria, review process, acceptance criteria (from templates)
- **Document Index:** Clear navigation to all project documents

**Focus:** AGENTS.md is the single source of truth for developers. Make it comprehensive and well-organized with proper citations.

### 5. Verify Initialization
**Objective:** Confirm all initialization is complete and correct.

**Verification Checklist:**
- [ ] Development environment fully operational
- [ ] All required tools installed and functional
- [ ] Codebase indexed (if Brownfield)
- [ ] All directories from architecture created
- [ ] AGENTS.md exists with complete information
- [ ] Document index is accurate and navigable

**Focus:** Quality gate before proceeding to development. All items must pass.

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
- AGENTS.md follows template structure
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

**Step 4 - Generate AGENTS.md:**
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
- ✅ AGENTS.md: Complete with document index
- ✅ Ready for development

**Outcome:**
- Fully initialized environment
- Complete directory structure
- Comprehensive AGENTS.md
- Ready to begin implementation
