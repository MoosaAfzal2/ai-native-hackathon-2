# UV Project Manager Skill

**Quick reference for creating UV-based Python projects**

## At a Glance

Create professional UV projects in 5-10 minutes with:
- ✅ Flexible folder structures (src/ or flat)
- ✅ Multiple quality levels (Minimal, Standard, Strict)
- ✅ Sensible defaults per project type
- ✅ Optional GitHub Actions CI/CD
- ✅ All configuration templates included

## When to Use

```
"Create a new UV project called my-api, type API, Standard quality"
"Set up a UV script project called data-processor"
"Initialize a UV library for crypto utilities"
```

## The 6 Decisions

| Decision | Options |
|----------|---------|
| **Project Type** | API, Library, Script, Service |
| **Folder Structure** | src/ (production) or flat (simple) |
| **Python Version** | Default 3.12 or custom 3.9-3.12+ |
| **Code Quality** | Minimal, Standard (recommended), Strict |
| **GitHub Actions** | No, Basic (lint+type), Full (+ tests+coverage) |
| **Dependencies** | Minimal, Opinionated (defaults), Custom |

## What You Get

**Core (Always)**:
- pyproject.toml with proper metadata
- README.md with setup instructions
- .gitignore for Python
- Package structure: `src/project_name/` with organized subdirectories:
  - `models/` - Data models and schemas
  - `core/` - Core business logic
  - `agents/` - Agent implementations
  - `tools/` - Tools and utilities
  - `config.py` - Configuration management
  - `main.py` - Application entry point

**Optional (if Standard/Strict)**:
- ruff.toml (linting config)
- mypy.ini (type checking config)
- pytest.ini (testing config)
- tests/ directory with example test

**Optional (if GitHub Actions)**:
- .github/workflows/lint.yml
- .github/workflows/test.yml

## Example Projects

See `examples/` for complete working examples:
- `api-project/` - FastAPI microservice (Standard)
- `script-project/` - Python script (Minimal)
- `library-project/` - Reusable library (Standard)

## Templates

All configuration templates in `templates/`:
- pyproject-api.toml
- pyproject-script.toml
- pyproject-library.toml
- ruff.toml, mypy.ini, pytest.ini
- GitHub Actions workflows

## Validation

Use `scripts/validate-uv-project.py` to verify your generated project:
```bash
python scripts/validate-uv-project.py /path/to/project
```

Checks:
- ✅ Valid TOML syntax
- ✅ Correct folder structure
- ✅ All required files present
- ✅ No hardcoded secrets
- ✅ Ready for `uv sync`

## Quick Start

1. Read: `SKILL.md` (full documentation)
2. Review: `examples/` (real projects)
3. Try: "Create a UV project for my-app"
4. Validate: `python scripts/validate-uv-project.py my-app/`

## Organized Project Structure (New!)

All generated projects now use a professional, modular structure inspired by production codebases like `rag-agent`:

```
project-name/
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py              # Entry point
│       ├── config.py            # Configuration
│       ├── models/              # Data models (Pydantic, schemas)
│       │   └── __init__.py
│       ├── core/                # Core business logic
│       │   ├── __init__.py
│       │   └── utils.py
│       ├── agents/              # Agent implementations
│       │   └── __init__.py
│       └── tools/               # Tools and utilities
│           └── __init__.py
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
```

This structure provides:
- **Separation of concerns** - Different modules for different purposes
- **Scalability** - Easy to add new modules as project grows
- **Team readiness** - Clear organization for collaborative development
- **Production-ready** - Matches industry standards

## Project Type Recommendations

| Type | Layout | Quality | Framework |
|------|--------|---------|-----------|
| **API** | src/ | Standard+ | FastAPI |
| **Library** | src/ | Standard | (none) |
| **Script** | flat | Minimal | (none) |
| **Service** | src/ | Standard | (custom) |

## File Structure

```
uv-project-manager/
├── SKILL.md                    # Full skill definition
├── README.md                   # This file
├── CHANGELOG.md                # Version history
├── templates/                  # Config templates
│   ├── pyproject-api.toml
│   ├── pyproject-script.toml
│   ├── pyproject-library.toml
│   ├── ruff.toml
│   ├── mypy.ini
│   ├── pytest.ini
│   ├── github-workflows-lint.yml
│   └── github-workflows-test.yml
├── scripts/                    # Helper scripts
│   └── validate-uv-project.py
├── examples/                   # Real examples
│   ├── api-project/
│   ├── script-project/
│   └── library-project/
└── docs/                       # Additional docs
    ├── DECISION-GUIDE.md
    └── TROUBLESHOOTING.md
```

## Common Questions

**Q: Should I use src/ or flat?**
A: Use src/ for production/team code. Use flat for scripts/prototypes.

**Q: What quality level should I choose?**
A: Standard for most projects. Strict for production. Minimal for quick prototypes.

**Q: Can I change options after creation?**
A: Yes! Edit pyproject.toml directly, add/remove config files as needed.

**Q: What if creation fails?**
A: Check error message, fix the issue, and try again. Projects are just files—safe to delete and retry.

**Q: Do I need GitHub Actions?**
A: No, but recommended for team/library projects. Great for CI/CD.

## Version

- **Version**: 1.0.0
- **Updated**: 2025-12-09
- **Python**: 3.9+
- **UV**: 0.5+

## See Also

- Full skill docs: `SKILL.md`
- Decision guide: `docs/DECISION-GUIDE.md`
- Troubleshooting: `docs/TROUBLESHOOTING.md`
- Example projects: `examples/`
- Templates: `templates/`
