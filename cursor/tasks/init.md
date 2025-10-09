**GOAL**: Initialize development environment and project documentation structure.

## [Input]
  1. "{ARCH}/*.md" --Architecture design documents (extract technology stack, development environment requirements)
  2. "{REQ}/*.md" --Project requirement documents
  3. "{EPIC}" --Task list

## [Output]
  1. "{root}/cursor.mdc" --Project guidance document (including technology stack, development standards, requirement overview, project goals, document index)
  2. Initialized development environment (such as virtual environment, database, toolchain, etc.)

## [Constraints]
  1. Do not add tools or configurations not explicitly required in architecture documents
  2. Do not skip creating document index in cursor.mdc

## [Tools]
  1. **todo_write**
    - [Step 1: Create todo list; Steps 2-4: Track execution progress]
  2. **context7 (MCP)**
    - [Step 2: Query official documentation for tech stack mentioned in architecture documents and environment setup guides]
    - When to use: After extracting tech stack from {ARCH}/*.md, query official installation and configuration docs for corresponding versions

## [Steps]
  1. Preparation & Analysis
    - Understand project's technology stack, environment requirements, and goals
    - Establish progress tracking mechanism
    - Outcome: Project requirements and stack understood

  2. Environment Setup
    - Configure fully operational development environment
    - Install and verify all dependencies
    - Outcome: Development environment ready

  3. Documentation Generation
    - Create complete project guidance document at "{root}/cursor.mdc"
    - Include all required sections with accurate information
    - Create clear document index for navigation
    - Outcome: cursor.mdc created with complete project guidance

  4. Verification
    - Verify development environment successfully initialized and usable
    - Verify "{root}/cursor.mdc" contains complete and accurate information
    - Outcome: Environment and documentation verified

## [Initialization-Guidelines]
  1. **Extract from Architecture**
    - Identify all technology stack, tools, and environment requirements explicitly stated in architecture docs
    - Do not add undefined tools or configurations
    - Set up only what's documented in requirements and architecture
  
  2. **cursor.mdc Structure**
    - Include: technology stack, development standards, requirement overview, project goals, document index
    - Create comprehensive document index for architecture and requirement documents
    - Enable easy navigation for subsequent development tasks

## [DoD]
  - [ ] Development environment fully initialized and operational with all tools installed and verified
  - [ ] Complete cursor.mdc exists with all required sections (tech stack, standards, requirements overview, document index)

## [Example]

### Example 1: Microservices Platform with Docker
[Input]
- Architecture: docs/architecture/tech-stack.md specifies Node.js, PostgreSQL, Redis, Docker
- Requirements: docs/requirements/*.md (3 services to implement)
- Epic: docs/epic.md (5 tasks)

[Decision]
- Environment setup: Install Docker, docker-compose, Node.js v18, PostgreSQL client
- Initialize: Create docker-compose.yml with services (postgres, redis, api)
- cursor.mdc: Include tech stack, document index, development commands

[Expected Outcome]
- Working environment: docker-compose up runs all services
- cursor.mdc with: tech stack (Node.js, Docker), document index (architecture/*, requirements/*), dev standards (TDD, SOLID)

### Example 2: Python Data Pipeline
[Input]
- Architecture: docs/architecture/*.md specifies Python 3.11, Airflow, Spark, S3
- Requirements: docs/requirements/*.md (ETL pipeline requirements)
- Epic: docs/epic.md (4 data processing tasks)

[Decision]
- Environment: Setup Python venv, install Airflow, PySpark, AWS CLI
- Initialize: Configure Airflow DAGs folder, S3 bucket connections
- cursor.mdc: Document Airflow setup, data flow diagrams, S3 bucket structure

[Expected Outcome]
- Airflow webserver accessible at localhost:8080
- S3 connections configured and tested
- cursor.mdc with: Python stack, Airflow DAG index, data pipeline overview, testing approach

### Example 3: React Native Mobile App
[Input]
- Architecture: docs/architecture/*.md specifies React Native, Expo, Firebase
- Requirements: docs/requirements/*.md (mobile app features)
- Epic: docs/epic.md (6 screen implementation tasks)

[Decision]
- Environment: Install Node.js, Expo CLI, Android Studio, Xcode (macOS)
- Initialize: expo init, Firebase project setup, configure app.json
- cursor.mdc: Document app structure, navigation flow, Firebase config, testing setup

[Expected Outcome]
- App runs on iOS/Android simulators via expo start
- Firebase connected (auth, firestore configured)
- cursor.mdc with: React Native stack, screen navigation index, component library docs, Firebase setup guide
