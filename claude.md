# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Cursor Claude AI Assistant System v2.0** - a multi-agent AI development framework built for professional software development with advanced coordination capabilities. The system features specialized agents for different development roles, structured workflows, and quality assurance mechanisms.

## Architecture

### Core Components

1. **Multi-Agent System** (`claude code/agents/`)
   - 15+ specialized development agents (frontend, backend, fullstack, security, testing, etc.)
   - Each agent has specific expertise and follows standardized XML-structured output
   - Agents use Chain of Thought reasoning and SELF-DISCOVER methodology

2. **SunnyCore Framework** (`claude code/sunnycore/`)
   - Workflow engine with template-based consistency
   - Task orchestration and validation pipelines
   - Development templates and documentation generators

3. **Custom Command System** (`claude code/commands/`)
   - Interactive command interface for task management
   - Multi-agent coordination protocols
   - Context-aware execution with structured feedback

### Key Workflow Files

- **Task Development**: `claude code/sunnycore/tasks/develop-task.md` - Core development workflow
- **Brownfield Development**: `claude code/sunnycore/tasks/brownfield-development.md` - Legacy code refactoring
- **Agent Templates**: `claude code/sunnycore/templates/` - Standardized output formats

## Custom Commands

The system provides several custom commands accessed through the SunnyCore framework:

### Available Commands
- `*help` - Display available commands and system capabilities
- `*develop-task {task_id}` - Execute development tasks with multi-agent coordination
- `*redevlop-task {task_id}` - Handle brownfield/legacy code development
- `*plan-task {task_id}` - Create comprehensive implementation plans
- `*validate-plan {task_id}` - Verify plan completeness and requirements alignment
- `*conclude` - Complete projects with systematic closure procedures
- `*review <task-id>` - Execute multi-dimensional quality reviews

### Command Processing
Commands are processed through the workflow defined in `claude code/commands/sunnycore_dev.md` with:
1. Input file validation
2. Custom command identification
3. Context construction and agent coordination
4. Structured output generation

## Development Workflow

### Standard Process
1. **Context Validation** - Read and verify all input files (specs, requirements, design docs)
2. **Implementation Plan Analysis** - Use Sequential-thinking Tool for requirement analysis
3. **Context Construction** - Index code, identify dependencies, assign tasks to appropriate agents
4. **Multi-Agent Execution** - Parallel task execution with specialized agents
5. **Development Notes Generation** - Create structured documentation using templates

### Quality Assurance
- **Practice Levels**: Bronze/Silver/Gold/Platinum scoring system
- **Milestone Checkpoints**: Required validation gates throughout development
- **Structured Output**: XML-tagged responses with evidence-based assessment
- **Cross-Agent Consistency**: Unified standards across all agent outputs

## File Structure

```
claude code/
├── agents/          # Specialized agent configurations
├── commands/        # Custom command definitions  
├── sunnycore/       # Core framework and workflows
│   ├── tasks/       # Task execution workflows
│   └── templates/   # Standardized templates
└── CLAUDE.md        # Agent system configuration
```

## Important Notes

### Language Support
- Primary language: Traditional Chinese for documentation and communication
- Technical terms: Chinese-English correspondence for accuracy
- Professional communication standards with structured XML output

### Coordination Requirements  
- Always use TodoWrite tool for task management and progress tracking
- Follow sequential thinking methodology for complex problem-solving
- Maintain context continuity across multi-agent interactions
- Use specialized agents based on task categorization (frontend, backend, security, etc.)

### Installation & Setup
- Run `./install.command` for interactive setup with language selection
- System supports both local and MCP tool configurations
- Requires Node.js >= 16.0.0 and Cursor IDE integration

## MCP Tool Integration

The system is designed to work with various MCP tools:
- **Sequential Thinking**: Complex problem-solving and reasoning
- **Context7**: Library documentation and API references  
- **Playwright**: Web automation and testing
- **Claude Context**: Codebase search and understanding

Always follow the structured approach defined in the agent configurations when using these tools for optimal coordination and results.