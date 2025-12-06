# Console Todo Application

A simple, in-memory Python console-based todo application implementing core task management features.

## Features (Phase I)

- **Add Task**: Create new tasks with title and optional description
- **View Tasks**: Display all tasks in a formatted table
- **Update Task**: Modify task title and/or description
- **Delete Task**: Remove tasks from the list
- **Mark Complete/Incomplete**: Toggle task completion status

## Requirements

- Python 3.13+
- UV package manager

## Setup

1. Navigate to the project directory:
```bash
cd console-todo-app
```

2. Create a virtual environment and install dependencies:
```bash
uv sync
```

## Running the Application

Start the todo application:
```bash
uv run python -m console_todo_app
```

## Running Tests

Run all unit tests:
```bash
uv run pytest tests/
```

Run tests with verbose output:
```bash
uv run pytest tests/ -v
```

Check test coverage:
```bash
uv run pytest tests/ --cov=src
```

## Project Structure

```
console-todo-app/
├── src/
│   └── console_todo_app/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── task.py
│       ├── storage/
│       │   ├── __init__.py
│       │   └── task_storage.py
│       └── ui/
│           ├── __init__.py
│           └── console_ui.py
├── tests/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_task_storage.py
│   ├── test_console_ui.py
│   └── test_main.py
└── README.md
```

## Architecture

The application follows a 4-layer architecture:

1. **Models Layer** (`models/task.py`): Core data model with immutable IDs and timestamps, mutable completion status, and comprehensive validation
2. **Storage Layer** (`storage/task_storage.py`): In-memory CRUD operations with sequential ID generation and task lifecycle management
3. **UI Layer** (`ui/console_ui.py`): Console-based user interaction with input prompts, formatted output, and error handling
4. **Main Layer** (`main.py`): Application orchestration with event loop and menu-driven navigation

## Test Coverage

- **79 total tests** across 4 test files
- **81% code coverage** (exceeds 80% requirement)
- **100% coverage** on core models and storage layers
- **92% coverage** on UI layer
- All tests follow TDD (Red-Green-Refactor) cycle

## Code Quality

- **PEP 8 compliant**: Validated with ruff
- **Type hints**: Full type annotations throughout
- **Docstrings**: Comprehensive documentation on all classes and methods
- **Error handling**: Proper validation and exception handling for edge cases
- **Data validation**: Title (1-200 chars), description (max 1000 chars), immutability of IDs and timestamps

## Implementation Notes

- **Immutable Task Model**: Uses frozen dataclass with controlled mutations via `object.__setattr__()`
- **Sequential ID Generation**: Auto-incrementing IDs starting from 1
- **In-memory Storage**: No persistence (Phase II feature)
- **Retry Logic**: Allows users to retry on empty title input
- **Confirmation Prompts**: Delete operation requires user confirmation
- **Unicode Support**: Full support for international characters and emoji
