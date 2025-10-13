**GOAL**: Initialize development environment and project documentation structure.

## [Input]
  1. "{ARCH}/*.md" --Architecture design documents (extract technology stack, development environment requirements)
  2. "{TMPL}/instruction-tmpl.yaml" --Instruction template

## [Output]
  1. "{root}/AGENTS.md" --Project guidance document (including technology stack, development standards, requirement overview, project goals, document index)
  2. Initialized development environment (such as virtual environment, database, toolchain, etc.)
  3. Complete directory structure (extracted from work-directory-structure in {ARCH}/*.md)
  4. Minimal runnable application (Hello World level entry point with verified startup)
  5. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not add tools or configurations not explicitly required in architecture documents
  2. Do not skip creating document index in AGENTS.md
  3. Do not skip codebase indexing for Brownfield projects
  4. Must create directories from work-directory-structure in architecture documents, do not assume directory structure
  5. Minimal implementation should only include basic code needed for startup verification, do not implement business logic

## [Steps]
  1. Preparation & Analysis
    - Understand project's technology stack, environment requirements, and goals
    - Create comprehensive plan.md at "{root}/docs/plan.md" using the plan template to track the working progress
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
    - Create complete project guidance document at "{root}/AGENTS.md"
    - Include all required sections with accurate information
    - Create clear document index for navigation
    - Outcome: AGENTS.md created with complete project guidance

  5. Verification
    - Verify development environment successfully initialized and usable
    - Verify all required directories have been created
    - Verify minimal application can successfully start and run (smoke test)
    - Verify "{root}/AGENTS.md" contains complete and accurate information
    - Outcome: Environment, directory structure, minimal app, and documentation verified

## [Initialization-Guidelines]
  1. **Extract from Architecture**
    - Identify all technology stack, tools, and environment requirements explicitly stated in architecture docs
    - Do not add undefined tools or configurations
    - Set up only what's documented in requirements and architecture
  
  2. **Codebase Indexing**
    - Build searchable index of existing codebase (if Brownfield)
    - Enable efficient searching during development phases
  
  3. **Directory Structure & Minimal Implementation**
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
  - [ ] Complete AGENTS.md is generated base on the template

## [Example]

### Example 1: Microservices Platform with Docker
[Input]
- Architecture: docs/architecture/tech-stack.md specifies Node.js, PostgreSQL, Redis, Docker
- Architecture: work-directory-structure specifies: src/, services/, config/, docker/, tests/
- Requirements: docs/requirements/*.md (3 services to implement)
- Epic: docs/epic.md (5 tasks)

[Decision]
- Environment setup: Install Docker, docker-compose, Node.js v18, PostgreSQL client
- Initialize: Create docker-compose.yml with services (postgres, redis, api)
- Directory: Create src/, services/, config/, docker/, tests/ directories
- Minimal app: Create src/index.js with Express server returning "Hello World" on GET /health
- Index codebase: Run claude-context index for existing shared libraries
- AGENTS.md: Include tech stack, document index, development commands
- Verification: Run `node src/index.js` and `curl http://localhost:3000/health` returns 200 OK

[Expected Outcome]
- Working environment: docker-compose up runs all services
- All directories created: src/, services/, config/, docker/, tests/
- Minimal app verified: node src/index.js starts successfully, health endpoint returns "Hello World"
- Codebase indexed for semantic search
- AGENTS.md with: tech stack (Node.js, Docker), document index (architecture/*, requirements/*), dev standards (TDD, SOLID)

### Example 2: Python Data Pipeline
[Input]
- Architecture: docs/architecture/*.md specifies Python 3.11, Airflow, Spark, S3
- Architecture: work-directory-structure specifies: dags/, plugins/, data/, scripts/, tests/
- Requirements: docs/requirements/*.md (ETL pipeline requirements)
- Epic: docs/epic.md (4 data processing tasks)

[Decision]
- Environment: Setup Python venv, install Airflow, PySpark, AWS CLI
- Initialize: Configure Airflow DAGs folder, S3 bucket connections
- Directory: Create dags/, plugins/, data/, scripts/, tests/ directories
- Minimal app: Create dags/hello_world_dag.py with simple Airflow DAG that prints "Hello World"
- Index: Build codebase index for existing data transformers
- AGENTS.md: Document Airflow setup, data flow diagrams, S3 bucket structure
- Verification: Run `airflow dags test hello_world_dag` successfully executes

[Expected Outcome]
- Airflow webserver accessible at localhost:8080
- All directories created: dags/, plugins/, data/, scripts/, tests/
- Minimal DAG verified: airflow dags test executes successfully
- S3 connections configured and tested
- AGENTS.md with: Python stack, Airflow DAG index, data pipeline overview, testing approach

### Example 3: React Native Mobile App
[Input]
- Architecture: docs/architecture/*.md specifies React Native, Expo, Firebase
- Architecture: work-directory-structure specifies: src/, src/components/, src/screens/, src/navigation/, assets/, tests/
- Requirements: docs/requirements/*.md (mobile app features)
- Epic: docs/epic.md (6 screen implementation tasks)

[Decision]
- Environment: Install Node.js, Expo CLI, Android Studio, Xcode (macOS)
- Initialize: expo init, Firebase project setup, configure app.json
- Directory: Create src/, src/components/, src/screens/, src/navigation/, assets/, tests/ directories
- Minimal app: Create App.js with basic "Hello World" screen that renders successfully
- Index: Index existing component library and navigation structure
- AGENTS.md: Document app structure, navigation flow, Firebase config, testing setup
- Verification: Run `expo start` and app displays "Hello World" on simulator

[Expected Outcome]
- App runs on iOS/Android simulators via expo start
- All directories created: src/, src/components/, src/screens/, src/navigation/, assets/, tests/
- Minimal app verified: expo start launches successfully, displays "Hello World" screen
- Firebase connected (auth, firestore configured)
- AGENTS.md with: React Native stack, screen navigation index, component library docs, Firebase setup guide
