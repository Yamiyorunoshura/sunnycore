# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🔴 Critical Priority: Environment and Project Structure

### Project Overview
This is the **Sunnycore Context Engineering Project** - a multi-platform AI agent workflow system that provides role-based professional AI agents for development workflow optimization, supporting Test-Driven Development (TDD) and quality assurance processes.

### Key Commands and Development Workflow

#### Package Management
- **Primary Package Manager**: `uv` (detected via `uv.lock`)
- **Dependency Installation**: `uv add <package>` or `uv sync`
- **Script Execution**: `uv run <command>` (ensures proper environment)
- **Environment Activation**: Not required when using `uv run`

#### Testing and Quality Assurance
- **Run Tests**: `uv run pytest` or `uv run python -m pytest`
- **Test with Coverage**: `uv run pytest --cov=src --cov-report=html`
- **Type Checking**: `uv run mypy src/`
- **Linting**: `uv run black .` and `uv run isort .`
- **Security Checks**: `uv run bandit -r src/`

#### Common Development Commands
```bash
# Install dependencies
uv sync

# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src --cov-report=html --cov-report=term-missing

# Type checking
uv run mypy src/

# Code formatting
uv run black .
uv run isort .

# Security scanning
uv run bandit -r src/
```

## 🟡 Important Priority: Code Architecture and Components

### Core Architecture
The system is built around a **multi-stage testing framework** with the following key components:

#### Main Directories
- `src/` - Core framework implementation
  - `behavior/` - Behavior-driven testing components
  - `rag_evaluation/` - RAG (Retrieval-Augmented Generation) evaluation tools
  - `rag_integration/` - RAG integration components
  - `security/` - Security testing and validation
  - `validation/` - Data validation frameworks
  - `robustness/` - Robustness testing utilities
  - `retrieval/` - Information retrieval components
  - `tools/` - Development tools and utilities

- `sunnycore/` - Multi-platform AI agent system
  - `tasks/` - Task execution workflows
  - `templates/` - Standardized templates
  - `scripts/` - Utility scripts
  - `agents/` - Agent definitions and configurations

- `tests/` - Comprehensive test suite
- `docs/` - Documentation
- `config/` - Configuration files

### Multi-Platform Support
The system supports three major platforms:

1. **Sunnycore for Claude Code** (`claude code/`) - Professional specialization platform for large teams
2. **Sunnycore for Warp Code** (`warp code/`) - General role-based platform for small/medium teams
3. **Sunnycore for Codex** (`codex/`) - Basic version with core functionality

### Key Features
- **Role-based AI Agents**: Specialized agents for different development roles (Dev, PM, PO, QA)
- **XML-based Prompt Framework**: Structured prompting system with standardized tags
- **Template-driven Development**: Standardized templates for consistent documentation
- **Environment-aware Execution**: Adapts to different execution environments
- **TDD Support**: Built-in test-driven development workflow

## 🟢 Normal Priority: Development Standards and Conventions

### Code Standards
- **Python**: Follow PEP 8, enforced by `black` and `isort`
- **Type Hints**: Required, enforced by `mypy`
- **Testing**: Minimum 85% coverage required, uses `pytest`
- **Documentation**: Traditional Chinese with technical English terms

### File Organization
- **Naming**: kebab-case for files and folders
- **Structure**: Modular organization with clear separation of concerns
- **Templates**: Standardized templates in `sunnycore/templates/`
- **Configuration**: YAML-based configuration with 2-space indentation

### Agent System Integration
The project integrates with multiple AI agent systems:
- **Claude Code**: Professional development agents
- **Warp Code**: General-purpose workflow agents
- **Codex**: Basic agent functionality

### Development Workflow
1. **Environment Setup**: Use `uv sync` for dependency management
2. **Testing**: Always run tests before committing (`uv run pytest`)
3. **Type Checking**: Ensure type safety with `mypy`
4. **Code Quality**: Apply linting and formatting standards
5. **Documentation**: Maintain documentation alongside code changes

## ⚪ Optional Priority: Specialized Tools and Integrations

### Specialized Testing Tools
- **DeepEval**: For LLM-based evaluation
- **RAGAS**: For RAG evaluation metrics
- **NLTK/SpaCy**: Natural language processing utilities
- **Playwright**: Browser automation for web testing

### Configuration Files
- `pyproject.toml`: Project configuration and dependencies
- `uv.lock`: Locked dependency versions
- `config/security_config.yaml`: Security configuration

### Development Notes
- The project uses a sophisticated XML-based prompt framework
- Agents follow strict priority hierarchies for rule enforcement
- Environment-aware execution is critical for proper operation
- Template-driven documentation ensures consistency across outputs