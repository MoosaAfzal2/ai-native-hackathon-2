# Console Todo Application Constitution

## Core Principles

### I. Code Quality
All code must follow Python best practices and PEP 8 standards. Every function and method must include proper type hints. All classes and public methods must have clear docstrings. Code must be readable, maintainable, and follow clean code principles.

### II. Object-Oriented Design
Use proper OOP principles including encapsulation, single responsibility, and inheritance where appropriate. Clear separation of concerns between data models, business logic, and UI layers is mandatory. Each class should have a single, well-defined purpose.

### III. Test-Driven Development (TDD) - NON-NEGOTIABLE
TDD is mandatory for all features. Follow the Red-Green-Refactor cycle strictly:
1. **Red**: Write a failing test first that defines desired behavior
2. **Green**: Implement minimum code to make the test pass
3. **Refactor**: Improve code quality while keeping tests green

All code must be unit testable with clear interfaces. Design with testability as a primary concern - loosely coupled components, dependency injection where appropriate, and well-defined interfaces between layers.

### IV. User Experience
Console interface must be intuitive and provide clear feedback. User prompts must be descriptive and guide the user. Console output must be clear and formatted. All user operations must provide immediate, understandable feedback.

### V. Data Integrity
In-memory storage must maintain data consistency during runtime. Operations must be atomic where appropriate. Edge cases must be handled gracefully. No data corruption or inconsistent states allowed during runtime session.

### VI. Error Handling & Validation
All user inputs must be validated before processing. All user inputs and operations must have proper error handling. Error messages must be clear and actionable. No unhandled exceptions should reach the user.

## Development Standards

### Technology Stack
- **Python Version**: Python 3.13+ required
- **Package Manager**: Use `uv` exclusively for all package management and project initialization
- **Project Structure**: Must be initialized with `uv init --package console-todo-app`
- **Testing Framework**: Use pytest for all unit tests

### TDD Workflow
- **Red-Green-Refactor**: Mandatory cycle for all features
- **Test First**: Write failing tests before any implementation code
- **Test Coverage**: Aim for high test coverage of business logic, models, and core functionality
- **Test Organization**: Tests should mirror source structure; clear, descriptive test names

### Code Standards
- **Type Hints**: Required for all functions and methods
- **Code Formatting**: All code must be properly formatted with ruff
- **Docstrings**: Required for all classes and public methods
- **Naming Conventions**: snake_case for functions/variables, PascalCase for classes
- **Style Guide**: Follow PEP 8 strictly

### Architecture Principles
- **Separation of Concerns**: Clear separation between data models, business logic, and UI layers
- **Minimal Dependencies**: Use standard library where possible; minimize external dependencies
- **No Hardcoding**: Use configuration where appropriate; no hardcoded values
- **Modularity**: Code must be modular and follow OOP principles

## Technical Constraints

### Storage & Platform
- **Storage**: In-memory only (no database or file persistence in Phase I)
- **Platform**: Must run on Linux (WSL 2), macOS, and native Linux
- **Dependencies**: Minimal external dependencies; pytest for testing, prefer standard library otherwise
- **TDD Workflow**: Write failing tests first, implement to pass, refactor for quality

### Quality Gates
All code must pass the following before being considered complete:
- ✓ All unit tests pass (pytest)
- ✓ All code has corresponding unit tests (TDD requirement)
- ✓ High test coverage for models and business logic
- ✓ Type checking with mypy
- ✓ Code formatting with ruff
- ✓ Proper error handling for all functions
- ✓ Input validation for all user inputs
- ✓ Edge cases handled gracefully
- ✓ Application runs without errors on Python 3.13+

## Success Criteria

### Functional Requirements
- All user operations work as specified (Add, Delete, Update, View, Mark Complete)
- Data persists correctly during runtime session
- Application runs without errors on Python 3.13+
- All unit tests pass (pytest)

### Code Quality Requirements
- Code is modular and follows OOP principles
- User interface is intuitive and provides feedback
- TDD cycle (Red-Green-Refactor) was followed for all features
- High test coverage for core functionality
- All quality gates pass

## Governance

This Constitution supersedes all other practices and applies to ALL features in Phase I: Basic Level (Add, Delete, Update, View, Mark Complete tasks).

All development must verify compliance with these principles. Any deviation must be documented and justified. Complexity must be justified and aligned with project goals.

**Version**: 1.1.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06
