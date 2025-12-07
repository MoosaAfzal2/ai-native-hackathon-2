# Implementation Plan: Rich Library Integration for Console Todo App

**Feature**: `2-enhance-rich-ui`
**Created**: 2025-12-07
**Status**: Draft
**Target Completion**: Phase 1-7 (see workflow below)

---

## 1. Architecture Overview

### Current Architecture (Phase I)
```
Models Layer (task.py)
         ↓
Storage Layer (task_storage.py)
         ↓
UI Layer (console_ui.py) → print() statements
         ↓
Main Layer (main.py) → Event loop
```

### New Architecture (Phase II with Rich)
```
Models Layer (task.py) - NO CHANGES
         ↓
Storage Layer (task_storage.py) - NO CHANGES
         ↓
UI Layer (console_ui.py) - REFACTORED
         ↓
Rich Components Layer (NEW):
  ├── rich_components.py (Table, Panel, Message builders)
  ├── theme.py (Color constants)
  └── Rich Console (singleton at module level)
         ↓
Main Layer (main.py) - NO CHANGES
```

### Key Design Principles
1. **Minimal Changes**: Only UI layer changes; no model or storage changes
2. **Abstraction**: Rich complexity hidden in component wrappers
3. **Testability**: Mock-friendly interfaces with clear contracts
4. **Maintainability**: Separation of concerns (theme, components, UI logic)
5. **Backward Compatibility**: All existing tests pass without modification

---

## 2. Detailed Component Specifications

### 2.1 Theme Configuration (`ui/theme.py`)

**Purpose**: Centralize color and styling configuration for consistent application appearance.

**Contents**:
```python
"""Color theme and styling configuration for Rich UI."""

from typing import Optional
from dataclasses import dataclass

@dataclass
class Theme:
    """Color and styling theme for the application."""

    # Primary colors
    PRIMARY = "blue"
    SUCCESS = "green"
    WARNING = "yellow"
    ERROR = "red"
    MUTED = "dim white"

    # Symbols (with fallback)
    SYMBOL_SUCCESS = "✓"
    SYMBOL_ERROR = "✗"
    SYMBOL_INFO = "ℹ"
    SYMBOL_INCOMPLETE = "○"
    SYMBOL_COMPLETE = "✓"

    # Table styling
    TABLE_BORDER_STYLE = "blue"
    TABLE_HEADER_STYLE = "bold blue"
    TABLE_TITLE = "📋 Your Tasks"
    TABLE_SHOW_LINES = True

    # Menu styling
    MENU_BORDER_STYLE = "blue"
    MENU_TITLE_STYLE = "bold blue"
    MENU_TITLE_TEXT = "TODO APPLICATION"

    # Prompt styling
    PROMPT_STYLE = "cyan"

# Global theme instance
default_theme = Theme()
```

**Rationale**:
- Centralized theme configuration for easy customization
- Matches hardcoded color decision from clarifications
- Easy to test (can create test themes)
- Supports future theme switching without code changes

---

### 2.2 Rich Components Wrapper (`ui/rich_components.py`)

**Purpose**: Encapsulate Rich library complexity behind clean, testable interfaces.

**Components**:

#### `RichTableBuilder` Class
```python
class RichTableBuilder:
    """Builds and returns Rich Table for task display."""

    def __init__(self, theme: Theme = None):
        self.theme = theme or default_theme

    def build_task_table(self, tasks: List[Task]) -> Table:
        """Create a styled Rich Table from task list."""
        # Implementation: Create Table with columns, add rows
        # Returns: Fully configured Rich Table object

    def build_empty_state_table(self) -> Panel:
        """Create a styled message for empty task list."""
        # Implementation: Panel with "No tasks found" message
        # Returns: Rich Panel object
```

**Methods**:
- `build_task_table(tasks: List[Task]) -> Table`:
  - Creates Rich Table with columns: ID, Title, Status, Created
  - Applies theme styling
  - Formats status with color-coded badges
  - Returns Rich Table ready for console.print()

- `build_empty_state_table() -> Panel`:
  - Creates styled Panel for empty task list
  - Uses theme colors and border style
  - Returns Rich Panel

#### `RichMessageFormatter` Class
```python
class RichMessageFormatter:
    """Formats and returns styled console messages."""

    def __init__(self, theme: Theme = None):
        self.theme = theme or default_theme

    def success(self, message: str) -> str:
        """Format success message with green color and ✓ symbol."""
        # Returns formatted Rich text string ready for console.print()

    def error(self, message: str) -> str:
        """Format error message with red color and ✗ symbol."""
        # Returns formatted Rich text string

    def info(self, message: str) -> str:
        """Format info message with blue color and ℹ symbol."""
        # Returns formatted Rich text string
```

**Methods**:
- `success(message: str) -> str`: Returns green text with ✓ prefix
- `error(message: str) -> str`: Returns red text with ✗ prefix
- `info(message: str) -> str`: Returns blue text with ℹ prefix
- Each returns a formatted Rich markup string (e.g., `"[green]✓[/] Task created"`)

#### `RichMenuBuilder` Class
```python
class RichMenuBuilder:
    """Builds and returns Rich Panels for application menu."""

    def __init__(self, theme: Theme = None):
        self.theme = theme or default_theme

    def build_menu(self) -> Group:
        """Create styled menu with multiple panels."""
        # Panel 1: Title ("TODO APPLICATION")
        # Panel 2: Menu options (1-6)
        # Panel 3: Footer (optional)
        # Returns: Group of Panels or single Panel
```

**Methods**:
- `build_menu() -> Union[Panel, Group]`:
  - Creates title panel with "TODO APPLICATION"
  - Creates options panel with 1-6 menu choices
  - Creates optional footer panel
  - Returns displayable object (Panel or Group)

#### `RichPromptHelper` Class
```python
class RichPromptHelper:
    """Wraps Rich Prompt with validation and consistent styling."""

    def __init__(self, console: Console = None, theme: Theme = None):
        self.console = console or get_console()
        self.theme = theme or default_theme

    def prompt_text(self, prompt: str, max_length: Optional[int] = None) -> str:
        """Prompt for text input with optional max length validation."""
        # Uses Rich Prompt with validation callback
        # Returns validated user input

    def prompt_integer(self, prompt: str) -> int:
        """Prompt for integer input with error handling."""
        # Uses Rich IntPrompt
        # Returns valid integer or raises ValueError

    def prompt_confirmation(self, prompt: str) -> bool:
        """Prompt for yes/no confirmation."""
        # Uses Rich Prompt with yes/no constraint
        # Returns boolean
```

**Methods**:
- `prompt_text(prompt, max_length)`: Prompts with text validation
- `prompt_integer(prompt)`: Prompts for integer with validation
- `prompt_confirmation(prompt)`: Yes/no confirmation prompt
- All use Rich's built-in validation

---

### 2.3 Console Singleton (`ui/__init__.py` or `ui/console_ui.py`)

**Purpose**: Create a single Rich Console instance for consistent output.

**Implementation**:
```python
# In ui/__init__.py or top of console_ui.py
from rich.console import Console

# Singleton instance created at module load
_console: Optional[Console] = None

def get_console() -> Console:
    """Get or create the Rich Console singleton."""
    global _console
    if _console is None:
        _console = Console()
    return _console
```

**Rationale**:
- Single console instance ensures consistent styling
- Lazy initialization (only created when needed)
- Easy to mock in tests
- Follows singleton pattern for resource management

---

## 3. Updated ConsoleUI Class (`ui/console_ui.py`)

### Current vs. New Structure

**Current Methods** (Phase I):
- `prompt_add_task()` → Uses `input()`
- `display_all_tasks()` → Uses `print()` with manual formatting
- `prompt_update_task()` → Uses `input()`
- `prompt_delete_task()` → Uses `input()` and `print()`
- `prompt_toggle_task_status()` → Uses `input()` and `print()`

**Refactored Methods** (Phase II with Rich):
- `prompt_add_task()` → Uses `RichPromptHelper.prompt_text()`
- `display_all_tasks()` → Uses `RichTableBuilder.build_task_table()`
- `prompt_update_task()` → Uses `RichPromptHelper.prompt_text()`
- `prompt_delete_task()` → Uses `RichPromptHelper.prompt_confirmation()`
- `prompt_toggle_task_status()` → Uses `RichPromptHelper.prompt_integer()`

### Class Structure After Refactoring
```python
from rich.console import Console
from ui.rich_components import (
    RichTableBuilder,
    RichMessageFormatter,
    RichPromptHelper
)
from ui.theme import default_theme

class ConsoleUI:
    """Console-based UI using Rich for formatting."""

    def __init__(self, storage: TaskStorage, theme = None):
        self.storage = storage
        self.console = get_console()
        self.theme = theme or default_theme

        # Initialize component helpers
        self.table_builder = RichTableBuilder(self.theme)
        self.message_formatter = RichMessageFormatter(self.theme)
        self.prompt_helper = RichPromptHelper(self.console, self.theme)

    def prompt_add_task(self) -> Task:
        """Prompt user to add a new task (UPDATED)."""
        # Uses RichPromptHelper for input
        # Returns Task from storage
        # Displays success message via message_formatter

    def display_all_tasks(self) -> None:
        """Display all tasks in Rich Table (UPDATED)."""
        # Gets tasks from storage
        # Uses table_builder.build_task_table()
        # Prints via console.print()

    def prompt_update_task(self) -> None:
        """Prompt user to update a task (UPDATED)."""
        # Displays tasks via display_all_tasks()
        # Uses RichPromptHelper for input
        # Displays success/error via message_formatter

    def prompt_delete_task(self) -> None:
        """Prompt user to delete a task (UPDATED)."""
        # Displays tasks via display_all_tasks()
        # Uses RichPromptHelper.prompt_confirmation()
        # Displays success/error via message_formatter

    def prompt_toggle_task_status(self) -> None:
        """Prompt user to toggle task status (UPDATED)."""
        # Displays tasks via display_all_tasks()
        # Uses RichPromptHelper.prompt_integer()
        # Displays success/error via message_formatter
```

### Interface Preservation
- All public methods maintain same signatures
- Behavior unchanged from user perspective
- Input/output format preserved (except for Rich styling)
- Existing tests pass without modification

---

## 4. Updated Main Class (`main.py`)

**Changes**: MINIMAL
- Update `display_menu()` to use `RichMenuBuilder`
- Add import for Rich components
- Everything else unchanged

```python
from ui.rich_components import RichMenuBuilder

class TodoApp:
    """Main application class (minimally changed)."""

    def __init__(self):
        self.storage = TaskStorage()
        self.ui = ConsoleUI(self.storage)
        self.menu_builder = RichMenuBuilder()  # NEW

    def display_menu(self) -> None:
        """Display main menu using Rich Panel (UPDATED)."""
        # OLD: Used print() with "=" * 70
        # NEW: Uses menu_builder.build_menu()
        # Behavior unchanged from user perspective

    def run_event_loop(self) -> None:
        """Run event loop (UNCHANGED)."""
        # Same logic, same behavior
        # Only difference: menu uses Rich Panel
```

---

## 5. Dependencies & Setup

### New Dependency
**Rich Library**:
- Latest stable version (currently 13.7.0+)
- Added via: `uv add rich`
- No other new dependencies needed

### Update `pyproject.toml`
```toml
[project]
dependencies = ["rich"]  # ADD THIS LINE

[dependency-groups]
dev = [
    "pytest>=9.0.1",
    "pytest-cov>=7.0.0",
]
```

---

## 6. Testing Strategy

### Test Categories

#### 1. Unit Tests (Existing - NO CHANGES)
- Test all business logic in `test_task.py`, `test_task_storage.py`, `test_main.py`
- Existing tests use `mock.patch` for `input()` and `print()`
- **These tests pass without any modification**

#### 2. Rich Component Tests (NEW - `test_rich_components.py`)
```python
def test_table_builder_creates_table_with_correct_columns(mock_tasks):
    """Verify RichTableBuilder creates table with ID, Title, Status, Created columns."""
    builder = RichTableBuilder()
    table = builder.build_task_table(mock_tasks)
    # Assert: table has 4 columns with correct names
    # Assert: first column is "ID", second is "Title", etc.

def test_message_formatter_success_uses_green_color(message):
    """Verify success messages are green with ✓ symbol."""
    formatter = RichMessageFormatter()
    result = formatter.success("Task created")
    # Assert: result contains "[green]" markup
    # Assert: result contains "✓" symbol

def test_message_formatter_error_uses_red_color(message):
    """Verify error messages are red with ✗ symbol."""
    formatter = RichMessageFormatter()
    result = formatter.error("Task not found")
    # Assert: result contains "[red]" markup
    # Assert: result contains "✗" symbol

def test_menu_builder_creates_multiple_panels():
    """Verify menu builder creates multiple panels."""
    builder = RichMenuBuilder()
    menu = builder.build_menu()
    # Assert: returns Panel or Group of Panels
    # Assert: title panel contains "TODO APPLICATION"

def test_prompt_helper_validates_text_length():
    """Verify prompt helper validates max length."""
    helper = RichPromptHelper()
    # Use mocking to simulate user input > max_length
    # Assert: validation error is raised or input is re-prompted
```

#### 3. UI Integration Tests (NEW - `test_console_ui.py` UPDATES)
```python
def test_display_all_tasks_uses_rich_table(mock_storage, mock_console):
    """Verify display_all_tasks uses Rich Table."""
    ui = ConsoleUI(mock_storage)
    ui.display_all_tasks()
    # Assert: console.print() called with Table object
    # Assert: table has correct columns and data

def test_prompt_add_task_displays_success_message(mock_storage, mock_input):
    """Verify success message uses Rich formatting."""
    ui = ConsoleUI(mock_storage)
    task = ui.prompt_add_task()
    # Assert: console.print() called with green formatted message
    # Assert: ✓ symbol present in output
```

### Testing Implementation Approach

**Option A**: Mock Rich Console
```python
from unittest.mock import MagicMock, patch

@patch('console_todo_app.ui.console_ui.get_console')
def test_something(mock_get_console):
    mock_console = MagicMock()
    mock_get_console.return_value = mock_console
    # Test code
    mock_console.print.assert_called_once()
```

**Option B**: Capture Rich Output
```python
from rich.console import Console
from io import StringIO

def test_with_capture():
    output = StringIO()
    test_console = Console(file=output)
    # Use test_console in code
    result = output.getvalue()
    assert "✓" in result
```

**Selected Approach**: Both
- Use mocking for unit tests (fast, isolated)
- Use capture for integration tests (verify actual output)

### Test Coverage Goals
- **Existing tests**: 100% pass without modification
- **New Rich component tests**: ≥80% coverage of new code
- **Overall coverage**: Maintain ≥80% coverage
- **All tests**: Run with `pytest tests/ --cov=src`

---

## 7. Development Workflow (TDD Approach)

### Phase 0: Setup & Research
**Tasks**:
- [ ] Add Rich library to dependencies: `uv add rich`
- [ ] Verify Rich installation: `uv run python -c "import rich; print(rich.__version__)"`
- [ ] Read Rich documentation for Table, Panel, Prompt, Console
- [ ] Run existing tests to establish baseline: `uv run pytest tests/ -v`
- [ ] Verify baseline test coverage: `uv run pytest tests/ --cov=src`

**Deliverable**: Setup complete, all Phase I tests passing

**Estimated Tasks**: 1-2

---

### Phase 1: Theme & Component Wrappers (TDD)
**Red Phase**: Write tests for new components
- `test_rich_components.py`: Test RichTableBuilder, RichMessageFormatter, RichMenuBuilder, RichPromptHelper

**Green Phase**: Implement component wrappers
- `ui/theme.py`: Color constants and Theme configuration
- `ui/rich_components.py`: All builder classes with minimal functionality

**Refactor Phase**: Optimize and clean up

**Key Tests**:
- RichTableBuilder creates Table with correct columns
- RichTableBuilder formats status with correct colors
- RichMessageFormatter produces green success messages
- RichMessageFormatter produces red error messages
- RichMenuBuilder creates menu panels

**Deliverable**: theme.py and rich_components.py complete with 80%+ test coverage

**Estimated Tasks**: 5-7

---

### Phase 2: Task Table Display (TDD)
**Red Phase**: Write tests for `display_all_tasks()` with Rich Table
- Test that Rich Table is created
- Test that columns are correctly configured
- Test that tasks are formatted correctly
- Test that empty state shows "No tasks found"

**Green Phase**: Update `ConsoleUI.display_all_tasks()`
- Use `RichTableBuilder.build_task_table()`
- Use `console.print()` with Rich Table

**Refactor Phase**: Ensure code quality and performance

**Key Test Scenarios**:
- Empty task list → displays "No tasks found" message
- Single task → table displays correctly
- Multiple tasks → all tasks shown in order
- Task with long title → text wraps or truncates appropriately
- Task with unicode characters → displays correctly

**Deliverable**: display_all_tasks() working with Rich Table

**Estimated Tasks**: 3-4

---

### Phase 3: Success/Error Messages (TDD)
**Red Phase**: Write tests for message formatting
- Test success messages are green with ✓
- Test error messages are red with ✗
- Test info messages are blue with ℹ

**Green Phase**: Update all methods that print messages
- `prompt_add_task()` → displays "Task created" as green success
- `prompt_update_task()` → displays "Task updated" or error
- `prompt_delete_task()` → displays "Task deleted" or error
- Error handling → displays red error messages

**Refactor Phase**: Extract message formatting to consistent pattern

**Key Methods to Update**:
- `prompt_add_task()`: Success message after task creation
- `prompt_update_task()`: Success/error messages
- `prompt_delete_task()`: Success/error messages
- `prompt_toggle_task_status()`: Status change message
- Error handlers: All use red error messages

**Deliverable**: All user messages use Rich formatting

**Estimated Tasks**: 4-5

---

### Phase 4: Rich Prompts for Input (TDD)
**Red Phase**: Write tests for Rich Prompt integration
- Test prompt displays correctly with Rich formatting
- Test input validation works
- Test error messages appear on invalid input

**Green Phase**: Update input methods
- `prompt_add_task()`: Use RichPromptHelper.prompt_text()
- `prompt_update_task()`: Use RichPromptHelper.prompt_text()
- `prompt_delete_task()`: Use RichPromptHelper.prompt_confirmation()
- `prompt_toggle_task_status()`: Use RichPromptHelper.prompt_integer()

**Refactor Phase**: Ensure consistent prompt styling

**Key Validations**:
- Title: non-empty, max 200 chars
- Description: max 1000 chars
- Task ID: valid integer, exists in storage
- Confirmation: yes/no

**Deliverable**: All input operations use Rich Prompt with validation

**Estimated Tasks**: 4-5

---

### Phase 5: Menu Display (TDD)
**Red Phase**: Write tests for menu panel
- Test menu displays in Rich Panel
- Test title is "TODO APPLICATION"
- Test all 6 options are displayed

**Green Phase**: Update `TodoApp.display_menu()`
- Use `RichMenuBuilder.build_menu()`
- Display title panel + options panel + footer panel

**Refactor Phase**: Optimize menu layout

**Deliverable**: Main menu displays in styled Rich Panels

**Estimated Tasks**: 2-3

---

### Phase 6: Integration Testing & Visual Verification
**Manual Testing**:
- [ ] Run application and manually verify:
  - Task table displays with proper borders and colors
  - Success messages are green with ✓
  - Error messages are red with ✗
  - Menu displays in panels with proper styling
  - Input prompts show helpful hints
  - All Phase I functionality works unchanged

**Automated Testing**:
- [ ] Run all tests: `uv run pytest tests/ -v`
- [ ] Verify coverage: `uv run pytest tests/ --cov=src`
- [ ] Verify all Phase I tests pass unchanged
- [ ] Verify new Rich component tests pass

**Edge Case Testing**:
- [ ] Test with narrow terminal (< 80 cols)
- [ ] Test with long task titles (near 200 char limit)
- [ ] Test with unicode characters in tasks
- [ ] Test with empty task list

**Deliverable**: All tests pass, manual testing confirms visual improvements, coverage ≥80%

**Estimated Tasks**: 3-4

---

### Phase 7: Documentation Updates
**Tasks**:
- [ ] Update README.md:
  - Add Rich library to requirements section
  - Update installation instructions
  - Add section on Rich UI features
  - Include screenshots or examples of Rich output

- [ ] Update docstrings:
  - Add documentation to new classes in rich_components.py
  - Add documentation to theme.py
  - Update console_ui.py docstrings to mention Rich

- [ ] Create CHANGELOG entry documenting:
  - Rich library integration
  - New visual features
  - Backward compatibility notes

**Deliverable**: Complete documentation of Rich integration

**Estimated Tasks**: 2-3

---

## 8. Implementation Checklist

### Setup Phase
- [ ] Add Rich to dependencies: `uv add rich`
- [ ] Verify Rich installation
- [ ] Run existing tests baseline

### Component Development
- [ ] Create `ui/theme.py` with color constants
- [ ] Create `ui/rich_components.py` with builder classes
- [ ] Create `test_rich_components.py` with unit tests
- [ ] Achieve 80%+ coverage on new components

### UI Integration
- [ ] Update `console_ui.py`:
  - [ ] Import Rich components
  - [ ] Update display_all_tasks()
  - [ ] Update message display
  - [ ] Update input prompts
  - [ ] Update error handling
- [ ] Update `main.py`:
  - [ ] Import RichMenuBuilder
  - [ ] Update display_menu()
- [ ] Update test_console_ui.py to work with Rich

### Testing & Verification
- [ ] All Phase I tests pass (79 tests)
- [ ] New Rich component tests pass (15-20 tests)
- [ ] Total coverage ≥80%
- [ ] Manual visual testing:
  - [ ] Task table displays correctly
  - [ ] Messages are color-coded
  - [ ] Menu displays in panels
  - [ ] Prompts work with validation
- [ ] Edge case testing:
  - [ ] Narrow terminals
  - [ ] Long text
  - [ ] Unicode characters
  - [ ] Empty task lists

### Documentation
- [ ] Update README.md with Rich features
- [ ] Update docstrings
- [ ] Create CHANGELOG entry

---

## 9. Risk Analysis & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Breaking existing tests | Medium | High | Maintain interface contracts; mock Rich outputs; test with existing tests first |
| Performance degradation | Low | Medium | Benchmark before/after; optimize console singleton; profile if needed |
| Terminal incompatibility | Low | Medium | Use Rich's automatic fallback; test on multiple terminals; document requirements |
| Complex Rich API learning curve | Medium | Low | Encapsulate Rich in component wrappers; document usage; provide simple interfaces |
| Unicode/emoji not rendering | Low | Low | Let Rich handle fallbacks; test on limited terminals; use ASCII alternatives |
| Color not supported | Low | Low | Rich auto-detects and degrades gracefully; test in no-color environments |

---

## 10. Success Criteria Checklist

- [ ] **SC-001**: All 5 Phase I features work identically
- [ ] **SC-002**: All existing 79 unit tests pass without modification
- [ ] **SC-003**: Test coverage remains ≥80%
- [ ] **SC-004**: Task table displays in Rich Table with borders, headers, colors
- [ ] **SC-005**: Success/error/info messages color-coded correctly
- [ ] **SC-006**: Main menu displays in Rich Panel with title and styling
- [ ] **SC-007**: All input operations use Rich Prompt with validation
- [ ] **SC-008**: All operations complete in <1 second
- [ ] **SC-009**: Rich is only new dependency
- [ ] **SC-010**: README updated with Rich features

---

## 11. Estimated Task Breakdown

| Phase | Description | Estimated Tasks | Estimated LOC |
|-------|-------------|-----------------|----------------|
| 0 | Setup & Research | 1-2 | 0 |
| 1 | Theme & Components | 5-7 | 300-400 |
| 2 | Task Table Display | 3-4 | 150-200 |
| 3 | Message Formatting | 4-5 | 100-150 |
| 4 | Rich Prompts | 4-5 | 150-200 |
| 5 | Menu Display | 2-3 | 80-120 |
| 6 | Integration Testing | 3-4 | 100-150 |
| 7 | Documentation | 2-3 | 50-100 |
| **Total** | **Implementation** | **24-33** | **930-1320** |

---

## 12. Key Files Summary

| File | Status | Changes | Purpose |
|------|--------|---------|---------|
| `ui/theme.py` | NEW | Create | Color constants and Theme dataclass |
| `ui/rich_components.py` | NEW | Create | RichTableBuilder, RichMessageFormatter, RichMenuBuilder, RichPromptHelper |
| `ui/console_ui.py` | EXISTS | Refactor | Replace print() with Rich components; update all public methods |
| `ui/__init__.py` | EXISTS | Update | Add Rich Console singleton (or in console_ui.py) |
| `main.py` | EXISTS | Minimal | Add RichMenuBuilder import; update display_menu() |
| `pyproject.toml` | EXISTS | Update | Add "rich" to dependencies |
| `tests/test_rich_components.py` | NEW | Create | Unit tests for new Rich components |
| `tests/test_console_ui.py` | EXISTS | Update | Add tests for Rich integration (existing structure preserved) |
| `README.md` | EXISTS | Update | Add Rich features section; update installation |

---

## 13. Next Steps

1. **Immediate**: Run `/sp.tasks` to generate atomic, testable task list
2. **Review**: Validate task breakdown with user
3. **Implement**: Execute Phase 0-7 following TDD approach
4. **Test**: Verify all success criteria met
5. **Document**: Update README and create CHANGELOG entry

---

**Plan Status**: ✅ Ready for task generation
**Branch**: `2-enhance-rich-ui`
**Next Command**: `/sp.tasks`
