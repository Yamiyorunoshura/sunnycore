# Fullstack Developer Workflow

<enforcement>
## 🔄 Workflow Todo List Creation

### 📋 Necessary Preparation Before Execution

**Important Reminder**: Before starting any workflow steps, you must use the todo list to create a todo list to organize these steps.

**Creation Process**:
1. **Analyze Workflow Structure** - Carefully read the entire workflow file, identify all stages, steps, and tasks
2. **Extract Key Tasks** - Convert each stage's core tasks into specific todo items
3. **Set Priorities** - Set priorities based on task importance and dependencies
4. **Create Todo List** - Use the `todo_write` tool to create a structured todo list containing all steps
5. **Execute and Update** - Execute tasks in todo list order, update status in a timely manner

### 📝 Todo List Requirements
- **Coverage**: Each major stage should have a corresponding todo item
- **Verification Points**: Key verification checkpoints must be included in the todo list
- **Priorities**: Set reasonable priorities to ensure dependencies are respected
- **Status Management**: Update todo status in a timely manner during execution (pending → in_progress → completed)
- **Uniqueness**: Only one task can be in `in_progress` status at a time
- **Completeness**: Only mark as `completed` when the task is fully completed
</enforcement>

---

<workflow type="fullstack-developer">

## Mandatory Preconditions Verification
<mandatory-preconditions>

### 1. Load Execution Standards

<stage name="Load Execution Standards" number="1" critical="true">
**Mandatory Execution Standards Loading**
- **Description**: Completely read `{project_root}/sunnycore/dev/enforcement/fullstack-developer-enforcement.md`
- **Requirements**:
  <requirements>
  - Understand all mandatory rules, fullstack development standards, and quality gates
  - If unable to load, immediately stop and report error
  </requirements>

</stage>

### 2. Project Context Establishment

<stage name="Project Context Establishment" number="2" critical="true">

**Project Specifications Understanding**

- **Description**: Read all documents under the `{project_root}/docs/specs/` path
- **Requirements**:
  <requirements>
  <think>
  Fullstack developers need to focus on the following types of project specification content:

  1. **System Architecture Specifications**:
     - Microservices architecture design and inter-service communication
     - Frontend-backend separation architecture and API Gateway configuration
     - Database design, relational models, and data synchronization strategies
     - System integration points, external dependencies, and third-party services

  2. **Frontend Specifications**:
     - UI/UX design system and component library standards
     - Responsive design, accessibility requirements, and browser compatibility
     - Frontend state management and data flow architecture
     - Client-side performance optimization and SEO requirements

  3. **Backend Specifications**:
     - Server architecture, load balancing, and scaling strategies
     - Database design, index optimization, and query performance
     - Background task processing and asynchronous job management
     - Monitoring, logging, and error tracking

  4. **API Design Specifications**:
     - RESTful API design standards and OpenAPI specifications
     - GraphQL schema design and query optimization
     - Version control strategies and backward compatibility
     - API documentation and testing strategies

  5. **Security Specifications**:
     - Authentication and authorization mechanisms (OAuth, JWT)
     - Data encryption, privacy protection, and GDPR compliance
     - CORS policies, CSP settings, and security headers
     - Input validation, SQL injection, and XSS protection

  6. **DevOps and Deployment Specifications**:
     - CI/CD pipeline design and automated testing
     - Containerization strategies and Kubernetes configuration
     - Environment management and configuration management
     - Disaster recovery and backup strategies
  </think>

  Based on the above thinking analysis, execute the following tasks:
  - Understand project requirements, complete system architecture, and frontend-backend integration requirements
  - Establish a project context model covering frontend, backend, API, and database
  - Identify key technology dependencies, API design patterns, and data flow architecture
  - Pay special attention to frontend-backend integration points, security strategies, and performance optimization requirements
  - Confirm DevOps processes, deployment strategies, and monitoring mechanisms
  - Verify cross-layer consistency and technical debt management strategies
  </requirements>

**Implementation Plan Verification**
- **Description**: Confirm `{project_root}/docs/implementation-plan/{task_id}`(e.g. `1`, `2`, `3`...)-plan.md` exists and is readable
<critical-checkpoint>
If implementation plan does not exist, immediately stop and notify user that planning stage needs to be executed first
</critical-checkpoint>

- **Requirements**:
  <requirements>
  <think hard>
  - Validate plan completeness, scope definition, and fullstack technical feasibility
  - Confirm frontend-backend integration requirements and performance targets
  <think hard>
  </requirements>

</stage>

### 3. Fullstack Specialization Preparation

<stage name="Fullstack Specialization Preparation" number="3" critical="true">
**Fullstack Development Checklist Preparation**
Prepare fullstack checklist according to mandatory execution standards:

<fullstack-checklist>
<think hard>
- [ ] Analyze plan content, identify frontend and backend development requirements
- [ ] Confirm API design and database architecture
- [ ] Validate frontend-backend integration strategy and security requirements
- [ ] Establish unified test-driven development (TDD) strategy
- [ ] Confirm deployment and DevOps processes
<think hard>
</fullstack-checklist>

**Performance and Security Targets Confirmation**
Confirm and record fullstack performance requirements:
<performance-targets>
<think>
- Frontend loading time and backend API response time targets
- Database query performance and system scalability requirements
- Security, availability, and monitoring strategies
<think>
</performance-targets>
</stage>
</mandatory-preconditions>

---

## Execution Protocol
<execution-protocol>

### TDD Fullstack Development Process
<stage name="TDD Fullstack Development Process" number="4" critical="true">

#### Test-First Fullstack Development
Strictly follow TDD principles for fullstack development:
<tdd-requirements>
<think harder>
- **Write tests before implementation (frontend and backend)**
- **Ensure frontend-backend integration test coverage meets required thresholds**
- **Implement unit tests, integration tests, end-to-end tests**
- **API contract tests and database tests**
<think harder>
</tdd-requirements>

#### Fullstack Architecture Principles Application
Apply the following principles during development:
<architecture-principles>
<think harder>
1. **Frontend-backend separation and API design principles**
2. **Unified error handling and logging mechanisms**
3. **Data consistency and transaction management**
4. **Security design and authentication integration**
<think harder>
</architecture-principles>
</stage>

### Quality Assurance
<stage name="Quality Assurance" number="5" critical="true">
#### Continuous Validation
Continuously execute during development:
<quality-validations>
<think hard>
- **Frontend-backend static analysis checks**
- **Fullstack security vulnerability scanning**
- **API performance and frontend loading performance testing**
- **Cross-browser and responsive design validation**
- **Database performance and data integrity checks**
<think hard>
</quality-validations>
</stage>
</execution-protocol>

---

## Failure Handling Mechanism
<failure-handling>
| Failure Scenario | Handling Action |
|---------|---------|
| **Precondition Failure** | Immediately stop, report specific missing files or conditions |
| **Plan Missing** | Stop development, guide user to execute planning stage first |
| **Frontend-Backend Integration Failure** | Record integration issues and formulate remediation plan |
| **Performance Not Met** | Record measurement results and formulate optimization plan |
| **Security Check Failed** | Record risks and require fixes before continuing |

<critical-failures>
**Any critical failure must immediately stop the process and report**
</critical-failures>

</failure-handling>

</workflow>