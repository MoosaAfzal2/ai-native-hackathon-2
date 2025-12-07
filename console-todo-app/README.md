# Console Todo Application

A sophisticated, in-memory Python console-based todo application with professional Rich UI, implementing core task management features with TDD principles.

## Features

### Phase I: Core Functionality
- **Add Task**: Create new tasks with title and optional description
- **View Tasks**: Display all tasks in a formatted table
- **Update Task**: Modify task title and/or description
- **Delete Task**: Remove tasks from the list
- **Mark Complete/Incomplete**: Toggle task completion status

### Phase II: Rich UI Enhancement
- **Professional Rich Tables**: Formatted task display with color-coded status indicators
- **Styled Menu System**: Multi-panel menu with visual hierarchy and clear options
- **Rich Prompts**: Input validation with inline error messages
- **Formatted Messages**: Color-coded success, error, and info messages
- **Windows Compatibility**: Full support for Windows console with ASCII-safe symbols

## Requirements

- Python 3.13+
- UV package manager
- Rich 14.2.0+ (for terminal formatting and styling)

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
│       ├── main.py                 # Application entry point
│       ├── models/
│       │   ├── __init__.py
│       │   └── task.py              # Task data model
│       ├── storage/
│       │   ├── __init__.py
│       │   └── task_storage.py      # In-memory CRUD operations
│       └── ui/
│           ├── __init__.py
│           ├── console_ui.py        # Console UI orchestration
│           ├── rich_components.py   # Rich component builders
│           └── theme.py             # Color and styling theme
├── tests/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_task_storage.py
│   ├── test_console_ui.py
│   ├── test_main.py
│   ├── test_rich_components.py
│   └── test_theme.py
└── README.md
```

## Architecture

The application follows a layered architecture with Rich UI integration:

### Layer 1: Models Layer (`models/task.py`)
- Immutable Task data model with frozen dataclass
- Immutable IDs and timestamps
- Mutable completion status using controlled mutations
- Comprehensive validation (title: 1-200 chars, description: max 1000 chars)

### Layer 2: Storage Layer (`storage/task_storage.py`)
- In-memory CRUD operations
- Sequential ID generation (auto-incrementing from 1)
- Task lifecycle management
- 100% code coverage

### Layer 3: UI Layer (`ui/`)
- **console_ui.py**: Console interaction orchestration
- **rich_components.py**: Rich component builders (Table, Messages, Menu, Prompts)
- **theme.py**: Centralized color and styling configuration
- Input validation with inline error messages
- Formatted output with color-coding and symbols

### Layer 4: Main Layer (`main.py`)
- Application orchestration
- Event loop and menu-driven navigation
- Integration of all layers

## Test Coverage

- **132 total tests** across 7 test files
- **87% code coverage** (exceeds 80% requirement)
- **100% coverage** on core models, storage, and theme layers
- **96% coverage** on Rich components
- **92% coverage** on UI layer

### Test Breakdown
- **Phase I Tests (79 tests)**: Models, Storage, and UI
  - test_task.py: 19 tests
  - test_task_storage.py: 27 tests
  - test_console_ui.py: 24 tests
  - test_main.py: 4 tests
- **Phase II Tests (53 tests)**: Rich UI components
  - test_rich_components.py: 31 tests
  - test_theme.py: 22 tests

### Testing Approach
- TDD (Test-Driven Development) methodology
- All tests follow Red-Green-Refactor cycle
- Comprehensive mocking of Rich components
- Input validation testing
- Edge case coverage

## Code Quality

- **PEP 8 compliant**: Code formatted according to Python standards
- **Type hints**: Full type annotations throughout all modules
- **Docstrings**: Comprehensive documentation on all classes and methods
- **Error handling**: Proper validation and exception handling for edge cases
- **Data validation**:
  - Title: 1-200 characters
  - Description: max 1000 characters
  - ID and timestamp immutability enforced
- **Component separation**:
  - Rich components encapsulated in wrapper classes
  - Theme configuration centralized
  - Clear layer boundaries

## Implementation Notes

- **Immutable Task Model**: Frozen dataclass with controlled mutations via `object.__setattr__()`
- **Sequential ID Generation**: Auto-incrementing IDs starting from 1
- **In-memory Storage**: No persistence (Phase III feature)
- **Retry Logic**: Allows users to retry on empty title input
- **Confirmation Prompts**: Delete operation requires user confirmation
- **Rich UI Components**:
  - RichTableBuilder: Creates formatted task tables with color-coded status
  - RichMessageFormatter: Formats messages with colors and symbols
  - RichMenuBuilder: Creates structured menu panels
  - RichPromptHelper: Wraps Rich Prompt with validation
- **Theme System**: Centralized color and styling configuration
- **Windows Compatibility**: ASCII-safe symbols for Windows console support
- **Singleton Console**: Single Rich Console instance shared across application

## Rich UI Features

### Tables
- Color-coded borders and headers
- Task ID, Title, Status (Complete/Pending), and Created date columns
- Status symbols with colors ([OK] for complete, [ ] for pending)
- Grid lines for better readability

### Menu
- Multi-panel display with title and options
- Styled borders and text
- Clear numbered options (1-6)

### Messages
- Color-coded success ([OK] symbol) in green
- Color-coded error ([X] symbol) in red
- Color-coded info ([i] symbol) in blue
- Messages embedded in user interactions

### Input Prompts
- Cyan-styled prompts for better visibility
- Length validation with inline error messages
- Integer input validation
- Confirmation prompts for destructive operations
