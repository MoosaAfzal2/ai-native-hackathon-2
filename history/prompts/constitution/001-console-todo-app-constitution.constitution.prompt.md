---
id: 001
title: Console Todo App Constitution
stage: constitution
date: 2025-12-06
surface: agent
model: claude-sonnet-4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["constitution", "python", "todo-app", "phase-1"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - No tests required for constitution
---

## Prompt

/sp.constitution

Project: In-Memory Python Console Todo Application (Phase I)

Core Principles:
- Code Quality: All code must follow Python best practices and PEP 8 standards
- Object-Oriented Design: Use proper OOP principles (encapsulation, single responsibility, inheritance where appropriate)
- Clean Code: Write readable, maintainable code with clear separation of concerns
- Testing Mindset: Code must be testable even if tests aren't required in this phase
- User Experience: Console interface must be intuitive and provide clear feedback
- Data Integrity: In-memory storage must maintain data consistency during runtime

Development Standards:
- Python Version: Python 3.13+ required
- Package Manager: Use `uv` exclusively for all package management and project initialization
- Project Structure: Must be initialized with `uv init --package console-todo-app`
- Type Hints: All functions and methods must include proper type hints
- Code Formating: All Code must be properly formatted with ruff.
- Docstrings: All classes and public methods must have clear docstrings
- Error Handling: All user inputs and operations must have proper error handling
- Input Validation: All user inputs must be validated before processing
- Code Organization: Clear separation between data models, business logic, and UI layers

Technical Constraints:
- Storage: In-memory only (no database or file persistence)
- Dependencies: Minimal external dependencies; use standard library where possible
- Platform: Must run on Linux (WSL 2), macOS, and native Linux
- Python Style: Follow PEP 8, use snake_case for functions/variables, PascalCase for classes

Quality Gates:
- All code must pass type checking (mypy)
- All code must pass code formatting (ruff)
- All functions must have proper error handling
- No hardcoded values; use configuration where appropriate
- Console output must be clear and formatted
- User prompts must be descriptive and guide the user
- Edge cases must be handled gracefully

Success Criteria:
- Application runs without errors on Python 3.13+
- All user operations work as specified
- Code is modular and follows OOP principles
- User interface is intuitive and provides feedback
- Data persists correctly during runtime session
- Code is ready for Claude Code to generate from specifications

This Constitution applies to ALL features in Phase I: Basic Level (Add, Delete, Update, View, Mark Complete tasks).

## Response snapshot

Constitution successfully created at `.specify/memory/constitution.md` with comprehensive principles covering:

1. **Core Principles**: Code Quality, OOP Design, Testing Mindset, User Experience, Data Integrity, Error Handling
2. **Development Standards**: Technology stack (Python 3.13+, uv, ruff), code standards (type hints, docstrings, PEP 8)
3. **Technical Constraints**: In-memory storage, minimal dependencies, cross-platform compatibility
4. **Quality Gates**: Type checking, code formatting, error handling, input validation
5. **Success Criteria**: Functional requirements and code quality benchmarks

The constitution establishes clear, measurable standards for Phase I development of the console todo application.

## Outcome

- ✅ Impact: Project constitution created defining all development principles and quality gates for Phase I
- 🧪 Tests: No tests required for constitution document
- 📁 Files: Created/Updated `.specify/memory/constitution.md`
- 🔁 Next prompts: `/sp.specify` to create feature specification, or begin implementing features following constitution principles
- 🧠 Reflection: Constitution provides comprehensive framework balancing code quality (type hints, PEP 8, ruff), architecture (OOP, separation of concerns), and user experience (intuitive console interface, clear feedback)

## Evaluation notes (flywheel)

- Failure modes observed: None - constitution creation successful
- Graders run and results (PASS/FAIL): PASS - all required sections populated with specific, actionable guidance
- Prompt variant (if applicable): N/A - initial constitution creation
- Next experiment (smallest change to try): Monitor adherence to quality gates during implementation; adjust if gates prove too restrictive or permissive
