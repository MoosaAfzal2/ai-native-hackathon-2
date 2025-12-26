# UV-Project-Manager Skill - Changelog

## [1.0.0] - 2025-12-09

### Added
- **Initial Release**: Comprehensive UV project manager skill
- **6 Decision Points**: Project type, folder structure, Python version, code quality level, GitHub Actions, dependencies style
- **4 Project Types**: API/Microservice, Library/Package, Script/CLI, Service
- **3 Quality Levels**: Minimal (basic), Standard (recommended), Strict (production)
- **2 Folder Structures**: src/ (production), flat (simple)
- **Templates**: Configuration templates for pyproject.toml, Ruff, Mypy, pytest, GitHub Actions workflows
- **Validation Script**: Python script to validate generated projects
- **Examples**: Complete working examples for API, Script, and Library projects
- **Documentation**: Comprehensive skill documentation, quick reference guide, examples
- **GitHub Actions**: Optional CI/CD workflows for lint, type-check, test, coverage

### Features
- ✅ General-purpose (works with ANY UV project type)
- ✅ Flexible configuration options per project type
- ✅ Sensible defaults aligned with project constitution
- ✅ Validation of generated project structure
- ✅ Secret scanning (API keys, tokens, passwords)
- ✅ Ready for immediate `uv sync` and development

### Project Types Supported
- **API/Microservice**: FastAPI-ready, src/ layout, tests included
- **Library/Package**: src/ layout, version pinning, distributable
- **Script/CLI**: Flat or src/ layout, minimal boilerplate
- **Service**: src/ layout, health check examples, long-running patterns

### Quality Levels
- **Minimal**: Just dependencies, no linting/typing (for quick prototypes)
- **Standard**: Includes Ruff linting, Mypy type checking, pytest (recommended)
- **Strict**: Strict mode for all tools, 80%+ coverage enforcement (production)

### Tools & Technologies
- **UV**: Modern Python package manager
- **Ruff**: Fast Python linter
- **Mypy**: Static type checker
- **Pytest**: Testing framework with coverage
- **GitHub Actions**: Optional CI/CD automation

### Files Included
- `SKILL.md` - Comprehensive skill documentation (473 lines)
- `README.md` - Quick reference guide
- `templates/` - Configuration templates
  - pyproject-api.toml, pyproject-script.toml, pyproject-library.toml
  - ruff.toml, mypy.ini, pytest.ini
  - github-workflows-lint.yml, github-workflows-test.yml
- `scripts/` - Helper utilities
  - validate-uv-project.py (validates generated projects)
- `examples/` - Real working examples
  - api-project-example.md (FastAPI microservice)
  - script-project-example.md (Python script)
  - library-project-example.md (Reusable library)
- `docs/` - Additional documentation
  - DECISION-GUIDE.md (choosing options)
  - TROUBLESHOOTING.md (common issues)

### Statistics
- **Lines of Code**: 1,200+
- **Decision Points**: 6
- **Project Types**: 4
- **Quality Levels**: 3
- **Folder Structures**: 2
- **Example Projects**: 3
- **Configuration Templates**: 8

---

## Future Enhancements (Planned)

### v1.1.0 (Planned)
- [ ] Django/Flask web framework templates
- [ ] ML project templates (Jupyter, notebooks)
- [ ] Pre-commit hooks setup automation
- [ ] Monorepo support

### v1.2.0 (Planned)
- [ ] Docker/Docker Compose templates
- [ ] Kubernetes manifests
- [ ] Poetry compatibility
- [ ] Virtual environment management

### v2.0.0 (Future)
- [ ] Interactive CLI wizard
- [ ] Project upgrade/migration tools
- [ ] Template customization system
- [ ] Community template registry

---

## Known Limitations

- Only supports UV (not pip/poetry/conda yet)
- Python 3.9+ requirement
- Single package per project (no monorepo support yet)
- No virtual environment management (UV handles this)

---

## Support

For issues or questions:
1. See `docs/TROUBLESHOOTING.md`
2. Check `examples/` for working projects
3. Review `SKILL.md` for comprehensive documentation
4. Use `scripts/validate-uv-project.py` to diagnose project issues

---

## License

Part of the AI-Native Hackathon project. See project LICENSE for details.
