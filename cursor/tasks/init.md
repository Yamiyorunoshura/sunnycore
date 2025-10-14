**GOAL**: Initialize development environment and create minimal viable skeleton with all module structures but no implementation.

## [Context]
**You must read the following context:**
1. "{ARCH}/*.md" -- Architecture design documents (extract technology stack, development environment requirements, module structure)
2. "{TMPL}/instruction-tmpl.yaml" -- Instruction template

## [Products]
1. "{root}/CURSOR.mdc" -- Project guidance document (including technology stack, development standards, requirement overview, project goals, document index)
2. Initialized development environment (such as virtual environment, database, toolchain, etc.)
3. Complete directory structure (extracted from work-directory-structure in {ARCH}/*.md)
4. All module skeletons with interface definitions, type declarations, and placeholder implementations (應無法啟動因為尚未實作)
5. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) -- For progress tracking

## [Constraints]
1. Do not add tools or configurations not explicitly required in architecture documents.
2. Do not skip creating document index in CURSOR.mdc.
3. Do not skip codebase indexing for Brownfield projects.
4. Must create directories from work-directory-structure in architecture documents, do not assume directory structure.
5. Must create all modules mentioned in architecture with clear interfaces but NO implementation - use placeholders like `raise NotImplementedError()`, `throw new Error('Not implemented')`, or similar.
6. Application SHOULD NOT be runnable at this stage - this is intentional as no business logic is implemented yet.

## [Steps]
**You should work along to the following steps:**
1. Preparation & Analysis. Understand project's technology stack, environment requirements, module architecture, and goals. Create comprehensive plan.md at "{root}/docs/plan.md" using the plan template to track the working progress. This ensures project requirements, stack, and module structure are understood, and plan.md is initialized.

2. Environment Setup & Indexing. Configure fully operational development environment. Install and verify all dependencies. Index codebase for efficient searching (if Brownfield). This ensures development environment is ready and codebase is indexed.

3. Directory Structure & Module Skeletons. Extract work-directory-structure and module architecture from architecture documents. Create all required directories. Create ALL module files with clear interfaces, type definitions, class/function signatures, but use placeholder implementations (NotImplementedError, throw Error, TODO comments). Configure basic configuration files and dependency declarations. This ensures complete module structure is in place but NOT runnable.

4. Documentation Generation. Create complete project guidance document at "{root}/CURSOR.mdc". Include all required sections with accurate information. Create clear document index for navigation. Document all created modules and their intended interfaces. This ensures CURSOR.mdc is created with complete project guidance including module overview.

5. Verification. Verify development environment successfully initialized and usable. Verify all required directories have been created. Verify all modules mentioned in architecture have corresponding skeleton files with clear interfaces. Verify "{root}/CURSOR.mdc" contains complete and accurate information. Note: Application should NOT be runnable at this stage. This confirms environment, directory structure, module skeletons, and documentation are in place.

## [Initialization-Guidelines]
1. **Extract from Architecture**
  - Identify all technology stack, tools, and environment requirements explicitly stated in architecture docs.
  - Identify all modules, components, services, layers mentioned in architecture.
  - Do not add undefined tools or configurations.
  - Set up only what's documented in requirements and architecture.

2. **Codebase Indexing**
  - Build searchable index of existing codebase (if Brownfield).
  - Enable efficient searching during development phases.

3. **Directory Structure & Module Skeleton Creation**
  - Extract directory structure from work-directory-structure field in {ARCH}/*.md.
  - Create all specified directories.
  - For EACH module/component/service mentioned in architecture:
    * Create corresponding file(s) with appropriate naming
    * Define all public interfaces, classes, functions with proper signatures
    * Add type hints/type declarations where applicable
    * Use placeholder implementations: `raise NotImplementedError("To be implemented")` (Python), `throw new Error('Not implemented')` (JavaScript/TypeScript), `panic!("not implemented")` (Rust), etc.
    * Add TODO comments indicating what needs to be implemented
  - Create configuration files (e.g., package.json, requirements.txt, Cargo.toml) with dependencies
  - DO NOT implement any actual business logic
  - Application SHOULD NOT run successfully at this stage - this is expected and correct

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Development environment fully initialized and operational with all tools installed and verified
- [ ] Codebase indexed and ready for semantic search (if Brownfield)
- [ ] All directory structure specified in architecture documents has been created
- [ ] ALL modules mentioned in architecture have skeleton files with clear interface definitions and placeholder implementations
- [ ] All module files contain type definitions, function/class signatures but NO actual implementation (should use NotImplementedError or equivalent)
- [ ] Application is NOT runnable yet (expected behavior - no implementation exists)
- [ ] Complete CURSOR.mdc is generated based on the template with module structure documented
- [ ] All the checkbox in plan.md are marked as done
- [ ] plan.md is deleted

## [Example]

### Example 1: Microservices Platform with Docker
[Input]
- Architecture: docs/architecture/tech-stack.md specifies Node.js, PostgreSQL, Redis, Docker
- Architecture: work-directory-structure specifies: src/, services/, config/, docker/, tests/
- Architecture: modules include UserService, OrderService, PaymentService with REST APIs
- Requirements: docs/requirements/*.md (3 services to implement)
- Epic: docs/epic.md (5 tasks)

[Decision]
- Environment setup: Install Docker, docker-compose, Node.js v18, PostgreSQL client
- Initialize: Create docker-compose.yml with services (postgres, redis, api)
- Directory: Create src/, services/, config/, docker/, tests/ directories
- Module skeletons:
  * services/user-service/index.js with UserController class, methods createUser(), getUser(), updateUser() throwing Error('Not implemented')
  * services/order-service/index.js with OrderController class, methods createOrder(), getOrder() throwing Error('Not implemented')
  * services/payment-service/index.js with PaymentController class, methods processPayment() throwing Error('Not implemented')
  * src/database/connection.js with connectDB() throwing Error('Not implemented')
  * src/middleware/auth.js with authenticate() throwing Error('Not implemented')
- Index codebase: Run claude-context index for existing shared libraries
- CURSOR.mdc: Include tech stack, document index, development commands, module structure overview
- Verification: Confirm all module files exist with proper interfaces but NO implementation

[Expected Outcome]
- Working environment: dependencies installed, docker-compose.yml configured
- All directories created: src/, services/, config/, docker/, tests/
- All modules created with clear interfaces but throwing NotImplementedError - application CANNOT run yet
- Codebase indexed for semantic search
- CURSOR.mdc with: tech stack (Node.js, Docker), document index (architecture/*, requirements/*), module structure (UserService, OrderService, PaymentService), dev standards (TDD, SOLID)

### Example 2: Python Data Pipeline
[Input]
- Architecture: docs/architecture/*.md specifies Python 3.11, Airflow, Spark, S3
- Architecture: work-directory-structure specifies: dags/, plugins/, data/, scripts/, tests/
- Architecture: modules include DataExtractor, DataTransformer, DataLoader, ValidationEngine
- Requirements: docs/requirements/*.md (ETL pipeline requirements)
- Epic: docs/epic.md (4 data processing tasks)

[Decision]
- Environment: Setup Python venv, install Airflow, PySpark, AWS CLI
- Initialize: Configure Airflow DAGs folder, S3 bucket connections in config files
- Directory: Create dags/, plugins/, data/, scripts/, tests/ directories
- Module skeletons:
  * plugins/data_extractor.py with DataExtractor class, extract_from_s3() raising NotImplementedError
  * plugins/data_transformer.py with DataTransformer class, transform(), validate_schema() raising NotImplementedError
  * plugins/data_loader.py with DataLoader class, load_to_warehouse() raising NotImplementedError
  * plugins/validation_engine.py with ValidationEngine class, validate_data_quality() raising NotImplementedError
  * dags/main_pipeline.py with DAG definition and task placeholders (all tasks raise NotImplementedError)
- Index: Build codebase index for existing data transformers
- CURSOR.mdc: Document Airflow setup, data flow diagrams, S3 bucket structure, module overview
- Verification: Confirm all module files exist with proper class definitions and type hints but NO implementation

[Expected Outcome]
- Environment configured: venv created, dependencies in requirements.txt, Airflow config files present
- All directories created: dags/, plugins/, data/, scripts/, tests/
- All modules created with clear interfaces but raising NotImplementedError - DAG CANNOT execute yet
- S3 connection configuration files present but not tested
- CURSOR.mdc with: Python stack, Airflow DAG structure, data pipeline architecture (Extractor → Transformer → Loader), module interfaces, testing approach

### Example 3: React Native Mobile App
[Input]
- Architecture: docs/architecture/*.md specifies React Native, Expo, Firebase
- Architecture: work-directory-structure specifies: src/, src/components/, src/screens/, src/navigation/, assets/, tests/
- Architecture: modules include AuthService, UserProfileService, NotificationService, 6 main screens
- Requirements: docs/requirements/*.md (mobile app features)
- Epic: docs/epic.md (6 screen implementation tasks)

[Decision]
- Environment: Install Node.js, Expo CLI, Android Studio, Xcode (macOS)
- Initialize: expo init, Firebase project configuration files, configure app.json, package.json
- Directory: Create src/, src/components/, src/screens/, src/navigation/, assets/, tests/ directories
- Module skeletons:
  * src/services/AuthService.ts with login(), logout(), register() throwing Error('Not implemented')
  * src/services/UserProfileService.ts with getProfile(), updateProfile() throwing Error('Not implemented')
  * src/services/NotificationService.ts with subscribe(), sendNotification() throwing Error('Not implemented')
  * src/screens/LoginScreen.tsx, HomeScreen.tsx, ProfileScreen.tsx, etc. (6 screens) with component structure but placeholder JSX
  * src/navigation/AppNavigator.tsx with navigation structure but routes pointing to placeholder screens
  * src/components/Button.tsx, Card.tsx, etc. with TypeScript interfaces but placeholder implementations
- Index: Index existing component library and navigation structure
- CURSOR.mdc: Document app structure, navigation flow, Firebase config, module services, testing setup
- Verification: Confirm all module and screen files exist with proper TypeScript types and interfaces but NO implementation

[Expected Outcome]
- Environment configured: package.json with dependencies, Firebase config files, app.json configured
- All directories created: src/, src/components/, src/screens/, src/navigation/, assets/, tests/
- All modules and screens created with TypeScript interfaces and component structures but throwing errors - app CANNOT run yet
- Firebase configuration files present but not initialized
- CURSOR.mdc with: React Native stack, screen navigation structure (Login → Home → Profile → ...), service module interfaces (AuthService, UserProfileService, NotificationService), component library structure, Firebase setup guide
