---
name: uv-project-manager
description: "Create and manage UV-based Python projects with sensible defaults, flexible folder structures (flat or src/), and optional code quality standards (Ruff, Mypy, pytest). Supports APIs, libraries, scripts, and services."
allowed-tools: Glob, Grep, Read, Write, Bash
---

# UV Project Manager Skill

Create and manage UV-based Python projects with professional structure, sensible defaults, and optional code quality enforcement.

## When to Use This Skill

Use **UV-Project-Manager** when you need to:
- Create a new UV-based Python project from scratch
- Set up folder structure that matches project type (API, library, script, service)
- Configure `pyproject.toml` with appropriate dependencies
- Establish code quality standards (Ruff, Mypy, pytest) if desired
- Generate GitHub Actions workflows for CI/CD
- Ensure consistency across your project portfolio

Invocation triggers:
- "Create a new UV project called [name]"
- "Set up a UV project for [description]"
- "Initialize a UV [project_type] called [name]"
- "Help me structure a UV project"

## Decision Points (6 Choices)

This skill guides you through **6 key decisions** to customize your project:

### 1. Project Type (Required)
Choose the primary purpose of your project:
- **API/Microservice**: FastAPI or similar web framework; `src/` layout required; includes tests/
- **Library/Package**: Distributable package; `src/` layout; includes tests/; version pinning in pyproject.toml
- **Script/CLI**: Standalone or small command-line tool; flat structure allowed; minimal boilerplate
- **Service**: Long-running service (worker, daemon); `src/` layout; includes monitoring/health checks

### 2. Folder Structure (Required)
Choose how to organize your code:
- **src/ Layout** (recommended for production code):
  ```
  project-name/
  ├── src/
  │   └── project_name/
  │       ├── __init__.py
  │       ├── main.py
  │       ├── models/        # Data models, Pydantic schemas
  │       │   └── __init__.py
  │       ├── core/          # Core business logic
  │       │   ├── __init__.py
  │       │   └── utils.py
  │       ├── agents/        # Agent implementations (if applicable)
  │       │   └── __init__.py
  │       ├── tools/         # Tools and utilities
  │       │   └── __init__.py
  │       └── config.py      # Configuration
  ├── tests/
  ├── pyproject.toml
  └── README.md
  ```
  - Best for: APIs, libraries, services, team projects
  - Enforces clean package separation
  - Supports `from project_name import ...` imports
  - Organized subdirectories for models, core logic, agents, and tools

- **Flat Structure** (for simple projects):
  ```
  project-name/
  ├── main.py
  ├── config.py
  ├── pyproject.toml
  └── README.md
  ```
  - Best for: Scripts, CLIs, small utilities
  - Less boilerplate
  - Faster to start

### 3. Python Version (Optional)
- **Default**: 3.12 (latest stable)
- **Custom**: 3.9, 3.10, 3.11, 3.12 or higher
- Determines minimum Python version in `pyproject.toml`

### 4. Code Quality Level (Required)
Choose how strict to be with code standards:

- **Minimal** (no linting/typing):
  - Just `pyproject.toml` and dependencies
  - No Ruff, Mypy, or pytest enforced
  - Best for: Quick prototypes, learning projects

- **Standard** (recommended):
  - Includes: Ruff (linting), Mypy (type checking), pytest
  - `ruff.toml` with sensible defaults
  - `mypy.ini` with basic type checking
  - `pytest.ini` with 80%+ coverage target
  - Best for: Most projects, team environments

- **Strict** (production-ready):
  - Includes: Ruff strict mode, Mypy strict mode, pytest with coverage enforcement
  - All project standards from constitution applied
  - CI/CD workflows for lint + test
  - Pre-commit hooks ready
  - Best for: Production APIs, shared libraries, flagship projects

### 5. GitHub Actions CI/CD (Optional)
- **No**: Skip GitHub Actions setup
- **Yes - Basic**: Lint + type check workflow
- **Yes - Full**: Lint + type check + tests + coverage reporting

### 6. Dependencies Style (Required)
- **Minimal dependencies**: Only runtime deps in `dependencies`; all dev tools optional
- **Opinionated defaults**: Include framework (FastAPI for APIs) + standard tooling
- **Custom**: User specifies exact dependencies

---

## Step-by-Step Workflow

### Phase 1: Clarify Requirements
1. Ask project name (required, lowercase with hyphens)
2. Ask project type (API, Library, Script, Service)
3. Ask folder structure preference (src/ vs flat)
4. Ask Python version (default 3.12)
5. Ask code quality level (Minimal, Standard, Strict)
6. Ask about GitHub Actions (optional)

### Phase 2: Design Structure
1. Propose folder structure based on choices
2. Propose `pyproject.toml` template with dependencies
3. Propose config files (ruff.toml, mypy.ini, pytest.ini) if applicable
4. Get user confirmation before creating files

### Phase 3: Generate Project Files
1. Create project root directory
2. Create folder structure (src/ with organized subdirectories, tests/, or flat)
3. Create `__init__.py` files in all packages:
   - `src/project_name/__init__.py`
   - `src/project_name/models/__init__.py`
   - `src/project_name/core/__init__.py`
   - `src/project_name/agents/__init__.py`
   - `src/project_name/tools/__init__.py`
   - `tests/__init__.py`
4. Generate `pyproject.toml` with appropriate metadata and dependencies
5. Generate config files (ruff.toml, mypy.ini, pytest.ini) if Standard/Strict
6. Generate `.gitignore` for Python projects
7. Generate `README.md` with setup instructions
8. Generate skeleton files for organized subdirectories
9. Optionally generate `.github/workflows/` YAML files

### Phase 4: Add Type Stubs and Examples
1. Create example files showing project structure
2. For APIs: example route/endpoint
3. For Libraries: example function with docstring
4. For Scripts: example main() entry point
5. For Services: example service loop

### Phase 5: Validate Everything
1. Verify pyproject.toml is valid TOML
2. Verify folder structure matches specification
3. Check all required files exist
4. Verify no hardcoded secrets/tokens
5. Optionally: `uv sync` dry-run to check dependencies

### Phase 6: Provide Next Steps
1. Show "Getting Started" instructions
2. Suggest: `uv sync` to install dependencies
3. If Strict: suggest pre-commit setup
4. If tests: suggest `uv run pytest`
5. If GitHub Actions: explain workflow triggers

---

## Decision Matrix & Defaults

| Project Type | Recommended Folder | Recommended Quality | Default Framework |
|---|---|---|---|
| API/Microservice | src/ | Standard or Strict | FastAPI |
| Library/Package | src/ | Standard | (none, utilities only) |
| Script/CLI | Flat or src/ | Minimal | (none, just Python) |
| Service | src/ | Standard | (depends on service type) |

---

## Output Format

After running this skill, your project directory will contain:

**Core Files** (always):
- `pyproject.toml` - Project metadata, dependencies, tool configuration
- `README.md` - Setup instructions and project overview
- `.gitignore` - Python standard ignores
- `src/project_name/__init__.py` - Package entry point
- `src/project_name/main.py` - Application entry point
- `src/project_name/config.py` - Configuration management
- `src/project_name/models/__init__.py` - Data models and schemas
- `src/project_name/core/__init__.py` - Core business logic
- `src/project_name/agents/__init__.py` - Agent implementations (if applicable)
- `src/project_name/tools/__init__.py` - Tools and utilities

**Optional Files** (if code quality selected):
- `ruff.toml` - Linter configuration
- `mypy.ini` - Type checker configuration
- `pytest.ini` - Test runner configuration
- `tests/__init__.py` - Test package marker

**Optional Files** (if CI/CD selected):
- `.github/workflows/lint.yml` - Lint and type-check workflow
- `.github/workflows/test.yml` - Test and coverage workflow

---

## Configuration Templates

Refer to `templates/` directory for:
- `pyproject-api.toml` - API project template
- `pyproject-script.toml` - Script project template
- `pyproject-library.toml` - Library project template
- `ruff.toml` - Linter configuration template
- `mypy.ini` - Type checker configuration template
- `pytest.ini` - Test runner configuration template
- `github-workflows-lint.yml` - GitHub Actions lint workflow
- `github-workflows-test.yml` - GitHub Actions test workflow

---

## Quality Checks & Validation

Before completing project setup, this skill validates:

✅ **Project Name**:
- Contains only lowercase letters, numbers, hyphens
- Matches pyproject.toml [project] name field
- No reserved Python keywords

✅ **pyproject.toml**:
- Valid TOML syntax (parseable)
- Contains required fields: [project] name, version, requires-python
- Dependencies are valid package names
- Tool configurations are valid

✅ **Folder Structure**:
- Correct layout (src/ or flat) matches specification
- All __init__.py files present in packages
- tests/ directory exists if quality level includes pytest
- No conflicting files (no duplicate main.py in multiple places)

✅ **No Secrets**:
- No hardcoded API keys, tokens, passwords
- .gitignore covers common secret patterns

✅ **Ready to Run**:
- `uv sync` can install dependencies (or dry-run verification)
- Project imports work (`python -c "import project_name"`)

---

## Common Patterns & Examples

See `examples/` directory for:
- `api-project/` - Complete API project example (FastAPI, Standard)
- `script-project/` - Complete script project example (Minimal)
- `library-project/` - Complete library project example (Standard)

Each example includes full folder structure, actual pyproject.toml, and getting started instructions.

---

## Troubleshooting

**Problem**: Project creation fails because folder already exists
- **Solution**: Rename project or delete existing folder first

**Problem**: `pyproject.toml` is invalid TOML
- **Solution**: Check tool configuration syntax, especially in [tool.ruff] and [tool.mypy]

**Problem**: `uv sync` fails with dependency resolution errors
- **Solution**: Check Python version compatibility, verify package names are correct

**Problem**: Imports fail after project creation
- **Solution**: Ensure __init__.py files exist in all package directories; run `uv sync` first

**Problem**: Ruff/Mypy report errors on generated files
- **Solution**: This is expected; fix with `uv run ruff check --fix` and review mypy errors

---

## Next Steps After Project Creation

1. **Navigate to project**: `cd project-name`
2. **Install dependencies**: `uv sync`
3. **Verify setup**: `python -c "import project_name"`
4. **If Standard/Strict**:
   - Check linting: `uv run ruff check src/ tests/`
   - Check types: `uv run mypy src/ tests/`
   - Run tests: `uv run pytest`
5. **Initialize git**: `git init && git add . && git commit -m "Initial project structure"`
6. **Start development**: Edit files in `src/` directory

---

## Requirements & Constraints

- **UV**: Must be installed and available in PATH
- **Python**: 3.9+ (configurable per project)
- **TOML Knowledge**: Not required; templates handle configuration
- **Git**: Optional but recommended (for .gitignore)

## When NOT to Use This Skill

- If you have an existing project that just needs dependency management → use `uv sync`
- If you need project migration from pip to uv → see Migration Skills
- If you need specialized setups (Jupyter, ML frameworks, etc.) → may need custom guidance

---

## Skill Metadata

- **Version**: 1.0.0
- **Created**: 2025-12-09
- **Category**: Project Setup & Management
- **Complexity**: 4-6 decision points
- **Time to Complete**: 5-10 minutes per project
- **Reusability**: High (every new project)
- **Dependencies**: UV, Python 3.9+
- **Tested With**: Python 3.12, UV 0.5+

---

## Files This Skill Manages

This skill can:
- **Create**: pyproject.toml, folder structure, __init__.py, config files, README.md, .gitignore, .github/workflows/
- **Modify**: Existing pyproject.toml (add/update dependencies, tool configs)
- **Validate**: Project structure, TOML syntax, dependency resolution
- **Does NOT**: Run package builds, publish to PyPI, create virtual environments (UV does this)

---

## Success Criteria

After using this skill, you should have:
- ✅ A valid UV project with `pyproject.toml`
- ✅ Appropriate folder structure (src/ or flat)
- ✅ Example files showing project pattern
- ✅ All code quality files if Standard/Strict selected
- ✅ GitHub Actions workflows if CI/CD selected
- ✅ README with setup instructions
- ✅ Ready to run `uv sync` and start development
- ✅ All files valid and self-documenting
