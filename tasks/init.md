**GOAL**: Initialize development environment and project documentation structure.

## [Input]
  1. "{ARCH}/*.md" --Architecture design documents (extract technology stack, development environment requirements)
  2. "{REQ}/*.md" --Project requirement documents
  3. "{EPIC}" --Task list
  4. "{TMPL}/plan-tmpl.yaml" --Unified planning template; capture environment setup tasks, directory creation checkpoints, and documentation updates

## [Output]
  1. "{root}/CLAUDE.md" --Project guidance document (including technology stack, development standards, requirement overview, project goals, document index)
  2. Initialized development environment (such as virtual environment, database, toolchain, etc.)
  3. Complete directory structure (extracted from work-directory-structure in {ARCH}/*.md)
  4. Minimal runnable application (Hello World level entry point with verified startup)
  5. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not add tools or configurations not explicitly required in architecture documents
  2. Do not skip creating document index in CLAUDE.md
  3. Do not skip codebase indexing for Brownfield projects
  4. Must create directories from work-directory-structure in architecture documents, do not assume directory structure
  5. Minimal implementation should only include basic code needed for startup verification, do not implement business logic

## [Steps]
  1. Preparation & Analysis
    - Understand project's technology stack, environment requirements, and goals
    - Create plan.md at "{root}/docs/plan.md" using the plan template to outline environment setup tasks, dependency checks, and documentation updates
    - Outcome: Project requirements and stack understood, plan.md initialized

  2. Environment Setup & Indexing
    - Configure fully operational development environment
    - Install and verify all dependencies
    - Index codebase for efficient searching (if Brownfield)
    - Outcome: Development environment ready and codebase indexed

  3. Directory Structure & Minimal Implementation
    - Extract work-directory-structure from architecture documents
    - Create all required directories
    - Create Hello World level application entry point
    - Configure basic startup scripts/commands
    - Outcome: Directory structure in place, minimal application can start

  4. Documentation Generation
    - Create complete project guidance document at "{root}/CLAUDE.md"
    - Include all required sections with accurate information
    - Create clear document index for navigation
    - Outcome: CLAUDE.md created with complete project guidance

  5. Verification
    - Verify development environment successfully initialized and usable
    - Verify all required directories have been created
    - Verify minimal application can successfully start and run (smoke test)
    - Verify "{root}/CLAUDE.md" contains complete and accurate information
    - Outcome: Environment, directory structure, minimal app, and documentation verified

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Project analysis:
    * Technology stack identified (languages, frameworks, databases, etc.)
    * Development environment requirements (tools, versions, dependencies)
    * Project goals and requirements summary (from ARCH/*.md and REQ/*.md)
    * Work directory structure extracted (from architecture work-directory-structure field)
  - Environment setup progress:
    * Dependencies to install (list with versions)
    * Installation status for each dependency (pending/installed/verified)
    * Configuration steps performed (list)
    * Environment verification results (all tools working: yes/no)
  - Codebase indexing (if Brownfield):
    * Existing codebase scanned (directories/files indexed)
    * Search index built (yes/no)
  - Directory structure creation:
    * Directories to create (list from work-directory-structure)
    * Creation status (each directory with status: created/verified)
  - Minimal application implementation:
    * Application type (e.g., Express server, Django app, React app)
    * Entry point created (file path)
    * Startup command documented
    * Smoke test result (application starts: yes/no, response verified: yes/no)
  - CLAUDE.md creation status:
    * Document sections completed (tech stack, standards, requirements, document index)
    * Document index accuracy verified (yes/no)

## [Initialization-Guidelines]
  1. **Extract from Architecture**
    - Identify all technology stack, tools, and environment requirements explicitly stated in architecture docs
    - Do not add undefined tools or configurations
    - Set up only what's documented in requirements and architecture
  
  2. **CLAUDE.md Structure**
    - Include: technology stack, development standards, requirement overview, project goals, document index
    - Create comprehensive document index for architecture and requirement documents
    - Enable easy navigation for subsequent development tasks
  
  3. **Codebase Indexing**
    - Build searchable index of existing codebase (if Brownfield)
    - Enable efficient searching during development phases
  
  4. **Directory Structure & Minimal Implementation**
    - Extract directory structure from work-directory-structure field in {ARCH}/*.md
    - Create all specified directories
    - Create Hello World application based on tech stack (e.g., Express basic server.js, Django manage.py runserver, etc.)
    - Ensure application can start and return basic response (e.g., 200 OK or Hello World output)
    - Do not implement any business logic, only verify environment and dependencies are correct

## [DoD]
  - [ ] Development environment fully initialized and operational with all tools installed and verified
  - [ ] Codebase indexed and ready for semantic search (if Brownfield)
  - [ ] All directory structure specified in architecture documents has been created
  - [ ] Minimal Hello World application has been implemented and can successfully start and run (smoke test passed)
  - [ ] Complete CLAUDE.md exists with all required sections (tech stack, standards, requirements overview, document index)

## [Example]

### Good Example 1
[INPUT]
Architecture specifies Node.js v18, PostgreSQL 14, Redis 7, Docker. Work-directory-structure: src/, services/, config/, docker/, tests/. Requirements show 3 microservices. Epic has 5 tasks.

[DECISION]
Step 1: Extract tech stack (Node.js 18, PostgreSQL 14, Redis 7, Docker), requirements summary (3 services: Order, Payment, Notification). Step 2: Install Docker, docker-compose, Node 18, PostgreSQL client. Create docker-compose.yml with all services. Verify all dependencies operational. Step 3: Create exact directory structure from architecture: src/, services/, config/, docker/, tests/. Create src/index.js with Express server returning 200 OK on GET /health. Document startup in README. Step 4: Generate CLAUDE.md with tech stack, requirements overview (3 microservices), document index (architecture/*.md, requirements/*.md). Step 5: Run node src/index.js, test curl localhost:3000/health returns "Hello World" 200 OK. All dependencies verified working.

[OUTCOME]
Operational environment: docker-compose up runs all services (PostgreSQL, Redis, API). All directories created per architecture spec. Minimal app verified: node src/index.js starts, health endpoint returns 200. Complete CLAUDE.md with tech stack, document index, dev commands. Smoke test passed.

[WHY-GOOD]
- Builds the environment strictly from architectural directives, avoiding speculative tooling.
- Verifies the minimal application end-to-end and documents setup, giving downstream teams a reliable base.

### Good Example 2
[INPUT]
Architecture: Python 3.11, Airflow, PySpark, S3. Work-directory-structure: dags/, plugins/, data/, scripts/, tests/. Requirements show ETL pipeline. Epic has 4 tasks.

[DECISION]
Step 1: Extract stack (Python 3.11, Airflow, Spark, AWS S3), goals (ETL pipeline). Step 2: Setup Python venv, install Airflow, PySpark, AWS CLI. Configure Airflow DAGs folder, test S3 connections. Step 3: Create dags/, plugins/, data/, scripts/, tests/ per architecture. Create minimal dags/hello_world_dag.py: simple DAG printing "Hello World". Step 4: Generate CLAUDE.md: Python stack, Airflow setup, S3 bucket structure, requirements (ETL tasks), document index. Step 5: Run airflow dags test hello_world_dag - executes successfully. All services verified.

[OUTCOME]
Airflow webserver accessible localhost:8080. All directories created: dags/, plugins/, data/, scripts/, tests/. Minimal DAG verified: airflow dags test executes successfully, prints "Hello World". S3 configured and tested. CLAUDE.md complete with stack, index, testing approach. Environment fully operational.

[WHY-GOOD]
- Aligns tooling, directory structure, and documentation with the specified architecture.
- Confirms operational readiness through real commands, not assumptions.

### Bad Example 1
[INPUT]
Architecture documents exist with tech stack and directory structure defined.

[BAD-DECISION]
Add tools not in architecture (install Kubernetes, Elasticsearch, GraphQL when not specified). Guess directory structure instead of reading work-directory-structure field. Skip smoke test of minimal app. Create CLAUDE.md without document index. No environment verification. Claim initialization complete.

[WHY-BAD]
Violates Constraint 1 (add undefined tools). Violates Constraint 4 (assume directory structure instead of extracting from architecture). Violates Constraint 5 (no smoke test - minimal app not verified). Violates DoD (environment not verified). Breaks initialization completeness.

[CORRECT-APPROACH]
Step 1: Read architecture/*.md completely. Extract ONLY specified tech stack. Extract exact work-directory-structure field. Step 2: Install only documented dependencies with versions. Step 3: Create directories exactly as specified in work-directory-structure. Create minimal Hello World based on tech stack (Express for Node, FastAPI for Python, etc). Step 4: Generate CLAUDE.md with complete document index of all architecture and requirement docs. Step 5: Run smoke test - verify app starts and responds. Verify all tools working. Only declare complete after verification.

### Bad Example 2
[INPUT]
Brownfield project with existing codebase in src/. Architecture and requirements documented.

[BAD-DECISION]
Skip codebase indexing entirely. Overwrite existing src/ directory with new Hello World (destroying existing code). Install different versions of dependencies than architecture specifies. No CLAUDE.md document index. Claim Greenfield project incorrectly.

[WHY-BAD]
Violates Constraint 3 (skip codebase indexing for Brownfield). Violates Initialization-Guidelines section 3 (must index existing codebase). Destroys existing code violating preservation principle. Wrong dependency versions will break existing code. No document index prevents navigation.

[CORRECT-APPROACH]
Step 1: Identify Brownfield (existing src/ code). Read architecture to understand tech stack and existing structure. Step 2: Install exact dependency versions from architecture. DO NOT overwrite existing src/ - verify it runs. Step 3: Index codebase using claude-context for semantic search per Guidelines section 3. Verify existing app functionality intact. Step 4: Generate CLAUDE.md with tech stack, comprehensive document index for all architecture/requirements/knowledge docs. Step 5: Run existing app to verify operational, not Hello World. Verify search index built. All existing functionality preserved and searchable.
