# Task Breakdown: Rich Library Integration for Console Todo App

**Feature**: `2-enhance-rich-ui`
**Created**: 2025-12-07
**Total Tasks**: 50
**Estimated Effort**: 24-33 tasks (phased approach)
**Status**: Ready for Implementation

---

## PHASE 1: Rich Library Setup (Tasks T001-T004)

### T001: Add Rich Dependency
**Description**: Install Rich library via UV package manager
**File**: `pyproject.toml`
**Command**: `uv add rich`

**Success Criteria**:
- [ ] Rich library added to `pyproject.toml` dependencies
- [ ] Command executes without errors
- [ ] `uv lock` completes successfully
- [ ] Rich package downloaded to `.venv/`

**Dependencies**: None
**Priority**: P0 (blocker)
**Estimated Effort**: 5 minutes

**Verification**:
```bash
uv add rich
uv lock
```

---

### T002: Verify Rich Installation
**Description**: Confirm Rich library is correctly installed and accessible
**Command**: `uv run python -c "import rich; print(rich.__version__)"`

**Success Criteria**:
- [ ] Command executes without import errors
- [ ] Rich version number prints (e.g., "13.7.0")
- [ ] No warnings or errors in output
- [ ] Rich is accessible in Python environment

**Dependencies**: T001
**Priority**: P0 (blocker)
**Estimated Effort**: 2 minutes

**Verification**:
```bash
uv run python -c "import rich; print(rich.__version__)"
```

---

### T003: Create Theme Configuration File
**Description**: Create `ui/theme.py` file with placeholder structure and color constants
**File**: `src/console_todo_app/ui/theme.py` (NEW)

**Success Criteria**:
- [ ] File created at correct path
- [ ] Docstring explains theme module purpose
- [ ] Color constants defined as class variables
- [ ] File has valid Python syntax
- [ ] Can be imported without errors

**Acceptance Test**:
```python
from console_todo_app.ui.theme import Theme, default_theme
assert hasattr(Theme, 'PRIMARY')
assert hasattr(Theme, 'SUCCESS')
```

**Dependencies**: T002
**Priority**: P0
**Estimated Effort**: 10 minutes

**Implementation Guidance**:
```python
"""Color theme and styling configuration for Rich UI."""

class Theme:
    """Centralized theme configuration for Rich components."""

    # Colors
    PRIMARY = "blue"
    SUCCESS = "green"
    ERROR = "red"
    WARNING = "yellow"
    MUTED = "dim white"

    # Symbols (will be used by components)
    SYMBOL_SUCCESS = "✓"
    SYMBOL_ERROR = "✗"
    SYMBOL_INFO = "ℹ"

default_theme = Theme()
```

---

### T004: Create Rich Components Skeleton
**Description**: Create `ui/rich_components.py` with class stubs for all builders
**File**: `src/console_todo_app/ui/rich_components.py` (NEW)

**Success Criteria**:
- [ ] File created at correct path
- [ ] All 4 builder classes have stubs
- [ ] Module docstring present
- [ ] File has valid Python syntax
- [ ] Can be imported without errors
- [ ] All classes have `__init__` method

**Classes to Create**:
1. `RichTableBuilder`
2. `RichMessageFormatter`
3. `RichMenuBuilder`
4. `RichPromptHelper`

**Dependencies**: T003
**Priority**: P0
**Estimated Effort**: 15 minutes

**Verification**:
```python
from console_todo_app.ui.rich_components import (
    RichTableBuilder,
    RichMessageFormatter,
    RichMenuBuilder,
    RichPromptHelper
)
```

---

## PHASE 2: Theme Configuration & Console Singleton (Tasks T005-T009)

### T005: Create Test File for Theme Configuration
**Description**: Write unit tests for Theme class in Red phase (tests fail)
**File**: `tests/test_theme.py` (NEW)

**Success Criteria**:
- [ ] Test file created with pytest structure
- [ ] All color constant tests present
- [ ] All symbol constant tests present
- [ ] Tests are organized by theme attribute
- [ ] Tests currently FAIL (Red phase)

**Test Categories**:
```python
# Test color constants exist
def test_theme_primary_color():
    assert hasattr(Theme, 'PRIMARY')
    assert Theme.PRIMARY == "blue"

def test_theme_success_color():
    assert hasattr(Theme, 'SUCCESS')
    assert Theme.SUCCESS == "green"

def test_theme_error_color():
def test_theme_warning_color():
def test_theme_muted_color():

# Test symbols exist
def test_theme_symbol_success():
    assert Theme.SYMBOL_SUCCESS == "✓"

def test_theme_symbol_error():
def test_theme_symbol_info():

# Test default instance
def test_default_theme_instance():
    assert default_theme is not None
    assert isinstance(default_theme, Theme)
```

**Dependencies**: T004
**Priority**: P1
**Estimated Effort**: 20 minutes

---

### T006: Implement Theme Class with Color Constants
**Description**: Implement Theme class in `ui/theme.py` (Green phase - make tests pass)
**File**: `src/console_todo_app/ui/theme.py`

**Success Criteria**:
- [ ] All color constants defined with correct values
- [ ] All symbol constants defined
- [ ] Class has proper docstring
- [ ] All tests from T005 pass
- [ ] No type errors when imported

**Implementation**:
- Define PRIMARY, SUCCESS, ERROR, WARNING, MUTED
- Define SYMBOL_SUCCESS, SYMBOL_ERROR, SYMBOL_INFO, SYMBOL_COMPLETE, SYMBOL_INCOMPLETE
- Create default_theme instance
- Add module-level docstring

**Test Verification**:
```bash
uv run pytest tests/test_theme.py -v
```

**Dependencies**: T005
**Priority**: P1
**Estimated Effort**: 10 minutes

---

### T007: Add Table Styling Configuration to Theme
**Description**: Extend Theme with table-specific styling constants
**File**: `src/console_todo_app/ui/theme.py`

**Success Criteria**:
- [ ] TABLE_BORDER_STYLE added with value "blue"
- [ ] TABLE_HEADER_STYLE added with value "bold blue"
- [ ] TABLE_TITLE added with emoji title
- [ ] TABLE_SHOW_LINES added as boolean
- [ ] All tests still pass

**Constants to Add**:
```python
TABLE_BORDER_STYLE = "blue"
TABLE_HEADER_STYLE = "bold blue"
TABLE_TITLE = "📋 Your Tasks"
TABLE_SHOW_LINES = True
```

**Test Verification**:
```bash
uv run pytest tests/test_theme.py -v
```

**Dependencies**: T006
**Priority**: P1
**Estimated Effort**: 10 minutes

---

### T008: Add Menu Styling Configuration to Theme
**Description**: Extend Theme with menu-specific styling constants
**File**: `src/console_todo_app/ui/theme.py`

**Success Criteria**:
- [ ] MENU_BORDER_STYLE added with value "blue"
- [ ] MENU_TITLE_STYLE added with value "bold blue"
- [ ] MENU_TITLE_TEXT added with "TODO APPLICATION"
- [ ] PROMPT_STYLE added with value "cyan"
- [ ] All tests still pass

**Constants to Add**:
```python
MENU_BORDER_STYLE = "blue"
MENU_TITLE_STYLE = "bold blue"
MENU_TITLE_TEXT = "TODO APPLICATION"
PROMPT_STYLE = "cyan"
```

**Test Verification**:
```bash
uv run pytest tests/test_theme.py -v
```

**Dependencies**: T007
**Priority**: P1
**Estimated Effort**: 10 minutes

---

### T009: Add Type Hints and Docstrings to Theme
**Description**: Add comprehensive type hints and documentation to Theme class
**File**: `src/console_todo_app/ui/theme.py`

**Success Criteria**:
- [ ] All attributes have type hints (str, bool)
- [ ] Class has comprehensive docstring
- [ ] Each attribute has inline comment explaining purpose
- [ ] No type checking errors (mypy clean)
- [ ] All tests still pass

**Documentation Template**:
```python
class Theme:
    """Color and styling theme for the Rich console application.

    Attributes:
        PRIMARY: Primary brand color (used for titles, headers)
        SUCCESS: Color for success messages and completed items
        ERROR: Color for error messages
        WARNING: Color for warning messages and pending items
        ...
    """
    PRIMARY: str = "blue"
    SUCCESS: str = "green"
    # ...
```

**Type Hints**:
- All color attributes: `str`
- All boolean attributes: `bool`
- Class variables: Use class attribute annotations

**Test Verification**:
```bash
uv run pytest tests/test_theme.py -v
```

**Dependencies**: T008
**Priority**: P1
**Estimated Effort**: 15 minutes

---

## PHASE 3: Console Singleton & Helper Functions (Tasks T010-T012)

### T010: Implement Console Singleton in Rich Components
**Description**: Create get_console() factory function and Rich Console instance in `ui/rich_components.py`
**File**: `src/console_todo_app/ui/rich_components.py`

**Success Criteria**:
- [ ] get_console() function defined
- [ ] Returns Rich Console instance
- [ ] Singleton pattern implemented (one instance)
- [ ] Can be imported without errors
- [ ] Type hints include Rich.Console

**Implementation**:
```python
from rich.console import Console
from typing import Optional

_console: Optional[Console] = None

def get_console() -> Console:
    """Get or create the Rich Console singleton instance.

    Returns:
        Console: Shared Rich console instance for all UI operations
    """
    global _console
    if _console is None:
        _console = Console()
    return _console
```

**Test Verification**:
```python
from console_todo_app.ui.rich_components import get_console
console1 = get_console()
console2 = get_console()
assert console1 is console2  # Same instance
```

**Dependencies**: T009
**Priority**: P1
**Estimated Effort**: 10 minutes

---

### T011: Create Test File for Rich Components
**Description**: Write unit tests for all Rich builder classes (Red phase)
**File**: `tests/test_rich_components.py` (NEW)

**Success Criteria**:
- [ ] Test file created with pytest structure
- [ ] Tests for RichTableBuilder present (empty)
- [ ] Tests for RichMessageFormatter present (empty)
- [ ] Tests for RichMenuBuilder present (empty)
- [ ] Tests for RichPromptHelper present (empty)
- [ ] All tests currently FAIL (Red phase)

**Test Structure**:
```python
"""Tests for Rich component builders."""

import pytest
from console_todo_app.ui.rich_components import (
    RichTableBuilder,
    RichMessageFormatter,
    RichMenuBuilder,
    RichPromptHelper,
    get_console
)
from console_todo_app.ui.theme import Theme

class TestRichTableBuilder:
    def test_builder_initialization(self):
        """Test RichTableBuilder can be instantiated."""
        builder = RichTableBuilder()
        assert builder is not None

    # More tests (will expand in T013-T022)

class TestRichMessageFormatter:
    # Tests for message formatter

class TestRichMenuBuilder:
    # Tests for menu builder

class TestRichPromptHelper:
    # Tests for prompt helper
```

**Dependencies**: T010
**Priority**: P1
**Estimated Effort**: 30 minutes

---

### T012: Implement RichTableBuilder Class - Initialization
**Description**: Implement RichTableBuilder `__init__` and basic structure (Green phase)
**File**: `src/console_todo_app/ui/rich_components.py`

**Success Criteria**:
- [ ] Class definition complete
- [ ] `__init__` method accepts optional theme parameter
- [ ] Stores theme instance (or uses default)
- [ ] Has docstring explaining purpose
- [ ] Type hints include Theme parameter
- [ ] Tests from T011 pass

**Implementation**:
```python
from console_todo_app.ui.theme import Theme, default_theme

class RichTableBuilder:
    """Builder class for creating styled Rich tables.

    Attributes:
        theme: Theme instance for styling
    """

    def __init__(self, theme: Theme | None = None):
        """Initialize RichTableBuilder with optional theme.

        Args:
            theme: Optional Theme instance. Defaults to default_theme.
        """
        self.theme = theme or default_theme
```

**Test Verification**:
```bash
uv run pytest tests/test_rich_components.py::TestRichTableBuilder -v
```

**Dependencies**: T011
**Priority**: P1
**Estimated Effort**: 10 minutes

---

## PHASE 4: Rich Table Implementation (Tasks T013-T016)

### T013: Write Tests for RichTableBuilder.build_task_table()
**Description**: Write detailed tests for task table building (Red phase)
**File**: `tests/test_rich_components.py`

**Success Criteria**:
- [ ] Test for empty task list
- [ ] Test for single task
- [ ] Test for multiple tasks
- [ ] Test for table column structure
- [ ] Test for status formatting (complete vs incomplete)
- [ ] Test for date formatting
- [ ] All tests FAIL (Red phase)

**Test Cases**:
```python
def test_build_task_table_empty_list(self):
    """Test creating table with empty task list."""
    builder = RichTableBuilder()
    table = builder.build_task_table([])
    assert table is not None
    # Verify table has correct columns

def test_build_task_table_single_task(self):
    """Test creating table with single task."""
    builder = RichTableBuilder()
    task = Task(id=1, title="Test Task", is_complete=False)
    table = builder.build_task_table([task])
    assert table is not None

def test_build_task_table_multiple_tasks(self):
    """Test creating table with multiple tasks."""
    tasks = [
        Task(id=1, title="Task 1", is_complete=False),
        Task(id=2, title="Task 2", is_complete=True),
    ]
    builder = RichTableBuilder()
    table = builder.build_task_table(tasks)
    assert table is not None

def test_build_empty_state_table(self):
    """Test creating empty state message."""
    builder = RichTableBuilder()
    panel = builder.build_empty_state_table()
    assert panel is not None
```

**Dependencies**: T012
**Priority**: P1
**Estimated Effort**: 30 minutes

---

### T014: Implement RichTableBuilder.build_task_table()
**Description**: Implement task table creation with Rich (Green phase)
**File**: `src/console_todo_app/ui/rich_components.py`

**Success Criteria**:
- [ ] Method signature: `build_task_table(tasks: List[Task]) -> Table`
- [ ] Creates Rich Table with 4 columns: ID, Title, Status, Created
- [ ] Status shows color-coded badges (green for complete, yellow for incomplete)
- [ ] Date formatted as "YYYY-MM-DD HH:MM"
- [ ] Column widths appropriate (ID=4, Title=40, Status=12, Created=16)
- [ ] Column alignment correct (ID=right, Title=left, Status=center, Date=left)
- [ ] Tests from T013 pass
- [ ] Has type hints and docstring

**Implementation**:
```python
from rich.table import Table
from typing import List
from console_todo_app.models.task import Task

def build_task_table(self, tasks: List[Task]) -> Table:
    """Build a styled Rich table from task list.

    Args:
        tasks: List of Task objects to display

    Returns:
        Rich Table configured with task data
    """
    table = Table(
        title=self.theme.TABLE_TITLE,
        border_style=self.theme.TABLE_BORDER_STYLE,
        header_style=self.theme.TABLE_HEADER_STYLE,
        show_lines=self.theme.TABLE_SHOW_LINES,
    )

    # Add columns
    table.add_column("ID", style="cyan", justify="right", width=4)
    table.add_column("Title", style="white", width=40)
    table.add_column("Status", justify="center", width=12)
    table.add_column("Created", style="dim", width=16)

    # Add rows
    for task in tasks:
        status = f"[{self.theme.SUCCESS}]{self.theme.SYMBOL_COMPLETE}[/] Complete" \
                 if task.is_complete \
                 else f"[{self.theme.WARNING}]{self.theme.SYMBOL_INCOMPLETE}[/] Pending"
        table.add_row(
            str(task.id),
            task.title,
            status,
            task.created_at.strftime("%Y-%m-%d %H:%M")
        )

    return table
```

**Test Verification**:
```bash
uv run pytest tests/test_rich_components.py::TestRichTableBuilder::test_build_task_table -v
```

**Dependencies**: T013
**Priority**: P1
**Estimated Effort**: 30 minutes

---

### T015: Implement RichTableBuilder.build_empty_state_table()
**Description**: Implement empty state message panel (Green phase)
**File**: `src/console_todo_app/ui/rich_components.py`

**Success Criteria**:
- [ ] Method signature: `build_empty_state_table() -> Panel`
- [ ] Returns Rich Panel with "No tasks found" message
- [ ] Panel uses theme colors
- [ ] Message is centered and styled
- [ ] Tests from T013 pass
- [ ] Has type hints and docstring

**Implementation**:
```python
from rich.panel import Panel

def build_empty_state_table(self) -> Panel:
    """Build a styled panel for empty task list.

    Returns:
        Rich Panel with empty state message
    """
    return Panel(
        "[yellow]No tasks found[/]",
        border_style=self.theme.TABLE_BORDER_STYLE,
        title="Tasks",
        expand=False,
    )
```

**Test Verification**:
```bash
uv run pytest tests/test_rich_components.py::TestRichTableBuilder::test_build_empty_state_table -v
```

**Dependencies**: T014
**Priority**: P1
**Estimated Effort**: 15 minutes

---

### T016: Write Tests for ConsoleUI.display_all_tasks()
**Description**: Write tests for display_all_tasks() integration with RichTableBuilder
**File**: `tests/test_console_ui.py` (update existing)

**Success Criteria**:
- [ ] Test that display_all_tasks() calls RichTableBuilder
- [ ] Test that output is printed via console
- [ ] Test with empty task list
- [ ] Test with multiple tasks
- [ ] Tests verify Rich table is used (not basic print)

**Test Cases**:
```python
@patch('console_todo_app.ui.console_ui.get_console')
def test_display_all_tasks_uses_rich_table(mock_get_console, mock_storage):
    """Test that display_all_tasks uses RichTableBuilder."""
    mock_console = MagicMock()
    mock_get_console.return_value = mock_console

    ui = ConsoleUI(mock_storage)
    ui.display_all_tasks()

    # Verify console.print was called
    assert mock_console.print.called
```

**Dependencies**: T015
**Priority**: P2
**Estimated Effort**: 20 minutes

---

## PHASE 5: Message Formatting (Tasks T017-T020)

### T017: Write Tests for RichMessageFormatter
**Description**: Write tests for message formatting (Red phase)
**File**: `tests/test_rich_components.py`

**Success Criteria**:
- [ ] Test success message format
- [ ] Test error message format
- [ ] Test info message format
- [ ] Test that output contains correct symbols
- [ ] Test that output contains correct colors
- [ ] All tests FAIL (Red phase)

**Test Cases**:
```python
class TestRichMessageFormatter:
    def test_success_message_format(self):
        """Test success message includes green color and check mark."""
        formatter = RichMessageFormatter()
        msg = formatter.success("Task created")
        # Should contain green markup and ✓ symbol
        assert "✓" in msg or "[green]" in msg

    def test_error_message_format(self):
        """Test error message includes red color and X mark."""
        formatter = RichMessageFormatter()
        msg = formatter.error("Task not found")
        # Should contain red markup and ✗ symbol
        assert "✗" in msg or "[red]" in msg

    def test_info_message_format(self):
        """Test info message includes blue color and info symbol."""
        formatter = RichMessageFormatter()
        msg = formatter.info("Please confirm")
        # Should contain blue markup and ℹ symbol
        assert "ℹ" in msg or "[blue]" in msg
```

**Dependencies**: T016
**Priority**: P1
**Estimated Effort**: 20 minutes

---

### T018: Implement RichMessageFormatter Class
**Description**: Implement message formatting methods (Green phase)
**File**: `src/console_todo_app/ui/rich_components.py`

**Success Criteria**:
- [ ] Class definition complete
- [ ] `__init__` accepts optional theme
- [ ] `success(message: str) -> str` implemented
- [ ] `error(message: str) -> str` implemented
- [ ] `info(message: str) -> str` implemented
- [ ] Returns Rich markup strings (not printing)
- [ ] All tests from T017 pass
- [ ] Has type hints and docstrings

**Implementation**:
```python
class RichMessageFormatter:
    """Formatter for styled console messages using Rich markup.

    Attributes:
        theme: Theme instance for styling
    """

    def __init__(self, theme: Theme | None = None):
        """Initialize RichMessageFormatter with optional theme."""
        self.theme = theme or default_theme

    def success(self, message: str) -> str:
        """Format a success message with green color and checkmark.

        Args:
            message: Message text to format

        Returns:
            Rich markup formatted string
        """
        return f"[{self.theme.SUCCESS}]{self.theme.SYMBOL_SUCCESS}[/] {message}"

    def error(self, message: str) -> str:
        """Format an error message with red color and X mark."""
        return f"[{self.theme.ERROR}]{self.theme.SYMBOL_ERROR}[/] {message}"

    def info(self, message: str) -> str:
        """Format an info message with blue color and info symbol."""
        return f"[{self.theme.PRIMARY}]{self.theme.SYMBOL_INFO}[/] {message}"
```

**Test Verification**:
```bash
uv run pytest tests/test_rich_components.py::TestRichMessageFormatter -v
```

**Dependencies**: T017
**Priority**: P1
**Estimated Effort**: 20 minutes

---

### T019: Update ConsoleUI Message Display Methods
**Description**: Update display_message(), display_success(), display_error() to use RichMessageFormatter
**File**: `src/console_todo_app/ui/console_ui.py`

**Success Criteria**:
- [ ] Create message_formatter instance in ConsoleUI.__init__
- [ ] Update prompt_add_task() to display success message
- [ ] Update prompt_update_task() to display success/error messages
- [ ] Update prompt_delete_task() to display success/error messages
- [ ] Update prompt_toggle_task_status() to display status message
- [ ] All messages use Rich formatting with colors
- [ ] No plain print() statements for messages
- [ ] ConsoleUI constructor updated with message_formatter

**Implementation Pattern**:
```python
# In ConsoleUI.__init__
from console_todo_app.ui.rich_components import (
    RichTableBuilder,
    RichMessageFormatter,
    get_console
)

self.console = get_console()
self.message_formatter = RichMessageFormatter(theme)

# In prompt_add_task()
# OLD: print(f"Task created: {task}")
# NEW:
success_msg = self.message_formatter.success(f"Task created: {task}")
self.console.print(success_msg)
```

**Test Verification**:
```bash
uv run pytest tests/test_console_ui.py -v
```

**Dependencies**: T018
**Priority**: P1
**Estimated Effort**: 30 minutes

---

### T020: Write Tests for ConsoleUI Message Display
**Description**: Write tests verifying message formatting in ConsoleUI
**File**: `tests/test_console_ui.py` (update)

**Success Criteria**:
- [ ] Test success message in prompt_add_task()
- [ ] Test error message when task not found
- [ ] Test status message after toggle
- [ ] Verify message formatter is called
- [ ] Verify Rich formatting is applied

**Test Cases**:
```python
@patch('console_todo_app.ui.console_ui.get_console')
def test_prompt_add_task_displays_success_message(mock_get_console, mock_storage):
    """Test that success message uses Rich formatting."""
    mock_console = MagicMock()
    mock_get_console.return_value = mock_console

    with patch('builtins.input', side_effect=["Test Task", ""]):
        ui = ConsoleUI(mock_storage)
        ui.prompt_add_task()

    # Verify console.print was called with formatted message
    calls = mock_console.print.call_args_list
    assert any("✓" in str(call) for call in calls)
```

**Dependencies**: T019
**Priority**: P2
**Estimated Effort**: 20 minutes

---

## PHASE 6: Menu Display (Tasks T021-T023)

### T021: Write Tests for RichMenuBuilder
**Description**: Write tests for menu panel building (Red phase)
**File**: `tests/test_rich_components.py`

**Success Criteria**:
- [ ] Test menu panel creation
- [ ] Test menu contains all 6 options
- [ ] Test menu has title
- [ ] Test menu has borders
- [ ] All tests FAIL (Red phase)

**Test Cases**:
```python
class TestRichMenuBuilder:
    def test_build_menu_returns_panel(self):
        """Test that build_menu returns a Panel object."""
        builder = RichMenuBuilder()
        menu = builder.build_menu()
        from rich.panel import Panel
        assert isinstance(menu, (Panel, list))

    def test_menu_contains_title(self):
        """Test that menu contains TODO APPLICATION title."""
        builder = RichMenuBuilder()
        menu = builder.build_menu()
        # Will verify in implementation
```

**Dependencies**: T020
**Priority**: P1
**Estimated Effort**: 15 minutes

---

### T022: Implement RichMenuBuilder Class
**Description**: Implement menu panel creation (Green phase)
**File**: `src/console_todo_app/ui/rich_components.py`

**Success Criteria**:
- [ ] Class definition complete
- [ ] `__init__` accepts optional theme
- [ ] `build_menu() -> Union[Panel, Group]` implemented
- [ ] Returns panel(s) with menu structure
- [ ] Title is "TODO APPLICATION"
- [ ] Uses theme colors and styling
- [ ] All tests from T021 pass
- [ ] Has type hints and docstrings

**Implementation**:
```python
from rich.panel import Panel
from rich.text import Text
from typing import Union

class RichMenuBuilder:
    """Builder class for creating styled Rich menu panels."""

    def __init__(self, theme: Theme | None = None):
        """Initialize RichMenuBuilder with optional theme."""
        self.theme = theme or default_theme

    def build_menu(self) -> Union[Panel, list]:
        """Build styled menu panel(s).

        Returns:
            Panel or list of Panels with menu structure
        """
        # Create title panel
        title_panel = Panel(
            f"[{self.theme.MENU_TITLE_STYLE}]{self.theme.MENU_TITLE_TEXT}[/]",
            border_style=self.theme.MENU_BORDER_STYLE,
            padding=(0, 2),
        )

        # Create options panel
        options_text = Text()
        options = [
            "1. Add a new task",
            "2. View all tasks",
            "3. Update a task",
            "4. Delete a task",
            "5. Mark task complete/incomplete",
            "6. Exit",
        ]
        for option in options:
            options_text.append(option + "\n")

        options_panel = Panel(
            options_text,
            border_style=self.theme.MENU_BORDER_STYLE,
            padding=(1, 2),
        )

        return [title_panel, options_panel]
```

**Test Verification**:
```bash
uv run pytest tests/test_rich_components.py::TestRichMenuBuilder -v
```

**Dependencies**: T021
**Priority**: P1
**Estimated Effort**: 25 minutes

---

### T023: Update TodoApp.display_menu()
**Description**: Update main menu display to use RichMenuBuilder
**File**: `src/console_todo_app/main.py`

**Success Criteria**:
- [ ] Import RichMenuBuilder
- [ ] Create menu_builder instance in TodoApp.__init__
- [ ] Update display_menu() to use menu_builder
- [ ] Output menu panels instead of print() statements
- [ ] All Phase I tests still pass
- [ ] Menu displays correctly when running app

**Implementation**:
```python
# In TodoApp.__init__
from console_todo_app.ui.rich_components import RichMenuBuilder, get_console

self.console = get_console()
self.menu_builder = RichMenuBuilder()

# In display_menu()
# OLD: Uses print() with "=" * 70
# NEW:
menu_panels = self.menu_builder.build_menu()
for panel in menu_panels:
    self.console.print(panel)
```

**Test Verification**:
```bash
uv run pytest tests/test_main.py -v
```

**Dependencies**: T022
**Priority**: P1
**Estimated Effort**: 15 minutes

---

## PHASE 7: Rich Prompts for Input (Tasks T024-T027)

### T024: Write Tests for Rich Prompt Integration
**Description**: Write tests for Rich Prompt usage (Red phase)
**File**: `tests/test_console_ui.py`

**Success Criteria**:
- [ ] Test Rich Prompt for text input
- [ ] Test Rich IntPrompt for numeric input
- [ ] Test Rich Confirm for yes/no
- [ ] Test input validation
- [ ] Test error handling
- [ ] All tests FAIL (Red phase)

**Test Cases**:
```python
@patch('console_todo_app.ui.rich_components.Prompt.ask')
def test_prompt_helper_uses_rich_prompt(mock_ask, mock_storage):
    """Test that prompt helper uses Rich Prompt."""
    mock_ask.return_value = "Test Task"

    helper = RichPromptHelper()
    result = helper.prompt_text("Enter task: ")

    assert result == "Test Task"
    mock_ask.assert_called_once()
```

**Dependencies**: T023
**Priority**: P1
**Estimated Effort**: 20 minutes

---

### T025: Implement RichPromptHelper Class
**Description**: Implement Rich Prompt wrapper methods (Green phase)
**File**: `src/console_todo_app/ui/rich_components.py`

**Success Criteria**:
- [ ] Class definition complete
- [ ] `__init__` accepts optional console and theme
- [ ] `prompt_text(prompt: str, max_length: Optional[int]) -> str` implemented
- [ ] `prompt_integer(prompt: str) -> int` implemented
- [ ] `prompt_confirmation(prompt: str) -> bool` implemented
- [ ] Uses Rich.Prompt for input
- [ ] Validation callbacks for constraints
- [ ] All tests from T024 pass
- [ ] Has type hints and docstrings

**Implementation**:
```python
from rich.prompt import Prompt, IntPrompt, Confirm

class RichPromptHelper:
    """Wrapper for Rich Prompt components with validation."""

    def __init__(self, console: Console | None = None, theme: Theme | None = None):
        """Initialize helper with optional console and theme."""
        self.console = console or get_console()
        self.theme = theme or default_theme

    def prompt_text(self, prompt: str, max_length: Optional[int] = None) -> str:
        """Prompt for text input with optional length validation.

        Args:
            prompt: Prompt text to display
            max_length: Maximum length constraint (optional)

        Returns:
            User input string
        """
        while True:
            result = Prompt.ask(
                f"[{self.theme.PROMPT_STYLE}]{prompt}[/]",
                console=self.console
            )
            if max_length and len(result) > max_length:
                error_msg = self.message_formatter.error(
                    f"Text too long (max {max_length}). Current: {len(result)}"
                )
                self.console.print(error_msg)
                continue
            return result

    def prompt_integer(self, prompt: str) -> int:
        """Prompt for integer input."""
        while True:
            try:
                return IntPrompt.ask(
                    f"[{self.theme.PROMPT_STYLE}]{prompt}[/]",
                    console=self.console
                )
            except ValueError:
                error_msg = self.message_formatter.error("Please enter a valid number")
                self.console.print(error_msg)

    def prompt_confirmation(self, prompt: str) -> bool:
        """Prompt for yes/no confirmation."""
        return Confirm.ask(
            f"[{self.theme.PROMPT_STYLE}]{prompt}[/]",
            console=self.console
        )
```

**Test Verification**:
```bash
uv run pytest tests/test_rich_components.py::TestRichPromptHelper -v
```

**Dependencies**: T024
**Priority**: P1
**Estimated Effort**: 30 minutes

---

### T026-T027: Update ConsoleUI Input Methods
**Description**: Update all input methods to use RichPromptHelper
**Files**: `src/console_todo_app/ui/console_ui.py`

**Success Criteria** (T026-T027 combined):
- [ ] Create prompt_helper instance in ConsoleUI.__init__
- [ ] Update prompt_add_task() to use RichPromptHelper.prompt_text()
- [ ] Update prompt_update_task() to use RichPromptHelper.prompt_text()
- [ ] Update prompt_delete_task() to use RichPromptHelper.prompt_confirmation()
- [ ] Update prompt_toggle_task_status() to use RichPromptHelper.prompt_integer()
- [ ] All validation works correctly
- [ ] Error messages display on invalid input
- [ ] All Phase I tests still pass

**Implementation Pattern**:
```python
# In ConsoleUI.__init__
from console_todo_app.ui.rich_components import RichPromptHelper

self.prompt_helper = RichPromptHelper(self.console, theme)

# In prompt_add_task()
# OLD: title = input("Enter task title: ")
# NEW:
title = self.prompt_helper.prompt_text("Enter task title: ", max_length=200)
```

**Test Verification**:
```bash
uv run pytest tests/test_console_ui.py -v
uv run pytest tests/ -v
```

**Estimated Effort**: T026: 20 min, T027: 20 min (combined: 40 min)

---

## PHASE 8: Integration & Testing (Tasks T028-T030)

### T028: Run Full Test Suite
**Description**: Execute all tests to verify integration
**Command**: `uv run pytest tests/ -v`

**Success Criteria**:
- [ ] All 79 Phase I tests pass
- [ ] All 15-20 new Rich component tests pass
- [ ] Total: 94-99 tests passing
- [ ] No test failures
- [ ] No import errors
- [ ] All type hints validated

**Verification**:
```bash
cd console-todo-app
uv run pytest tests/ -v
```

**Expected Output**:
```
tests/test_task.py ✓ (all pass)
tests/test_task_storage.py ✓ (all pass)
tests/test_console_ui.py ✓ (all pass, updated for Rich)
tests/test_main.py ✓ (all pass)
tests/test_theme.py ✓ (all pass)
tests/test_rich_components.py ✓ (all pass)

===== test session starts =====
collected 94-99 items
... PASSED [100%]
```

**Dependencies**: T027
**Priority**: P0
**Estimated Effort**: 10 minutes

---

### T029: Verify Test Coverage
**Description**: Check test coverage is ≥80%
**Command**: `uv run pytest tests/ --cov=src`

**Success Criteria**:
- [ ] Coverage report generated
- [ ] Overall coverage ≥80%
- [ ] New code coverage ≥80%
- [ ] No coverage regressions

**Verification**:
```bash
uv run pytest tests/ --cov=src --cov-report=term-missing
```

**Expected Output**:
```
Name                          Stmts   Miss  Cover   Missing
...
src/console_todo_app/ui/theme.py         X      0   100%
src/console_todo_app/ui/rich_components.py X   0   100%
src/console_todo_app/ui/console_ui.py    X    Y    Z%
src/console_todo_app/main.py             X    Y    Z%
...
TOTAL                                    X    Y   ≥80%
```

**Dependencies**: T028
**Priority**: P0
**Estimated Effort**: 5 minutes

---

### T030: Manual Visual Testing - Add Task
**Description**: Manually test Add Task flow to verify Rich output
**Instructions**:
1. Run: `uv run python -m console_todo_app`
2. Select "1. Add a new task"
3. Enter task title (e.g., "Buy groceries")
4. Enter task description (e.g., "Milk, eggs, bread")
5. Observe output

**Success Criteria**:
- [ ] Menu displays in styled panels
- [ ] Prompts use Rich formatting
- [ ] Success message is green with ✓
- [ ] Task is created successfully
- [ ] Output is visually improved over Phase I

**Expected Behavior**:
- Menu appears in blue borders
- Prompts show cyan text
- Success message shows: "✓ Task created"
- Message is green colored

**Dependencies**: T029
**Priority**: P2
**Estimated Effort**: 10 minutes

---

## PHASE 9: Manual Testing & Edge Cases (Tasks T031-T035)

### T031: Manual Visual Testing - View Tasks
**Description**: Test View Tasks with Rich table display
**Instructions**:
1. Run: `uv run python -m console_todo_app`
2. Select "2. View all tasks"
3. Observe table display

**Success Criteria**:
- [ ] Table displays with styled borders
- [ ] Table has 4 columns: ID, Title, Status, Created
- [ ] Headers are bold and blue
- [ ] Status badges are color-coded:
  - Green ✓ for complete
  - Yellow ○ for incomplete
- [ ] Table is readable and well-formatted
- [ ] Empty state shows styled message if no tasks

**Dependencies**: T030
**Priority**: P2
**Estimated Effort**: 10 minutes

---

### T032: Manual Visual Testing - Update Task
**Description**: Test Update Task with Rich prompts
**Instructions**:
1. Run: `uv run python -m console_todo_app`
2. Add a task first (or use existing)
3. Select "3. Update a task"
4. Enter task ID
5. Update title and/or description

**Success Criteria**:
- [ ] Task table displays with Rich formatting
- [ ] Prompts use Rich formatting (cyan)
- [ ] Success message is green with ✓
- [ ] Error messages are red with ✗
- [ ] Updated task appears in table correctly

**Dependencies**: T031
**Priority**: P2
**Estimated Effort**: 10 minutes

---

### T033: Manual Visual Testing - Delete Task
**Description**: Test Delete Task with Rich confirmation
**Instructions**:
1. Run: `uv run python -m console_todo_app`
2. Add a task (or use existing)
3. Select "4. Delete a task"
4. Enter task ID
5. Confirm deletion (yes)

**Success Criteria**:
- [ ] Table displays correctly
- [ ] Confirmation prompt shows clearly
- [ ] Success message is green with ✓
- [ ] Task is deleted and no longer in table
- [ ] Visual output is clear and professional

**Dependencies**: T032
**Priority**: P2
**Estimated Effort**: 10 minutes

---

### T034: Manual Visual Testing - Mark Complete
**Description**: Test Mark Complete with status badge colors
**Instructions**:
1. Run: `uv run python -m console_todo_app`
2. Add an incomplete task
3. Select "5. Mark task complete/incomplete"
4. Enter task ID
5. Toggle status

**Success Criteria**:
- [ ] Table displays correctly
- [ ] Status changes from yellow ○ to green ✓
- [ ] Success message displayed
- [ ] Color contrast is clear
- [ ] Status can be toggled back

**Dependencies**: T033
**Priority**: P2
**Estimated Effort**: 10 minutes

---

### T035: Test Edge Cases
**Description**: Test application with edge case inputs
**Test Cases**:
1. Long task title (near 200 chars) - verify text wrapping/display
2. Unicode characters in task - verify rendering
3. Multiple tasks (5+) - verify table scrolling/layout
4. Empty task list - verify "No tasks found" message
5. Invalid task ID - verify error message

**Success Criteria**:
- [ ] App doesn't crash on edge cases
- [ ] Error messages display correctly
- [ ] Output remains readable
- [ ] All operations complete <1 second

**Dependencies**: T034
**Priority**: P2
**Estimated Effort**: 20 minutes

---

## PHASE 10: Documentation & Finalization (Tasks T036-T040)

### T036: Update README.md with Rich Features
**Description**: Add Rich library section to README
**File**: `README.md`

**Success Criteria**:
- [ ] Rich library added to requirements section
- [ ] Installation instructions include `uv add rich`
- [ ] New "Phase II Features" section describes Rich enhancements
- [ ] Section describes: Tables, Panels, Messages, Prompts
- [ ] Includes examples or screenshots

**Content to Add**:
```markdown
## Phase II Features (Rich Library Integration)

The application has been enhanced with the [Rich](https://rich.readthedocs.io/) library for professional CLI output:

- **Rich Tables**: Task lists displayed in styled tables with color-coded status
- **Styled Messages**: Success (green ✓), error (red ✗), and info (blue ℹ) messages
- **Menu Panels**: Professional menu display in styled borders
- **Rich Prompts**: User input with helpful hints and validation feedback

### Visual Improvements
- Color-coded task status: Green (✓) for complete, Yellow (○) for pending
- Professional borders and grid lines
- Responsive terminal formatting
- Unicode emoji support with graceful fallback
```

**Dependencies**: T035
**Priority**: P2
**Estimated Effort**: 15 minutes

---

### T037: Add Docstrings to Rich Components
**Description**: Ensure all new classes have comprehensive docstrings
**File**: `src/console_todo_app/ui/rich_components.py`

**Success Criteria**:
- [ ] All classes have module-level docstring
- [ ] All public methods have docstrings
- [ ] Docstrings include Args, Returns, Raises
- [ ] Type hints referenced in docstrings
- [ ] Examples provided where helpful

**Verification**:
```bash
python -m pydoc console_todo_app.ui.rich_components
```

**Dependencies**: T036
**Priority**: P1
**Estimated Effort**: 20 minutes

---

### T038: Add Type Hint Validation
**Description**: Ensure all Rich component code passes mypy type checking
**Command**: `uv run mypy src/console_todo_app/ui/ --strict` (if available)

**Success Criteria**:
- [ ] No type errors in theme.py
- [ ] No type errors in rich_components.py
- [ ] All imports properly typed
- [ ] Rich types included in signatures

**Verification**:
```bash
uv run python -m mypy src/console_todo_app/ui/
# or
uv run ruff check src/
```

**Dependencies**: T037
**Priority**: P1
**Estimated Effort**: 15 minutes

---

### T039: Run Final Code Quality Checks
**Description**: Verify code quality and formatting
**Command**: `uv run ruff check src/`

**Success Criteria**:
- [ ] No PEP 8 violations
- [ ] No unused imports
- [ ] No undefined names
- [ ] Consistent formatting
- [ ] Code follows project standards

**Verification**:
```bash
uv run ruff check src/ --fix
uv run ruff format src/
```

**Dependencies**: T038
**Priority**: P1
**Estimated Effort**: 10 minutes

---

### T040: Final Complete Test Run
**Description**: Run full test suite one final time
**Command**: `uv run pytest tests/ -v --cov=src`

**Success Criteria**:
- [ ] All 94-99 tests pass
- [ ] Coverage ≥80%
- [ ] No warnings or errors
- [ ] No test flakiness
- [ ] All functionality works

**Verification**:
```bash
cd console-todo-app
uv run pytest tests/ -v --cov=src --cov-report=term-missing
```

**Expected Result**:
```
===== test session starts =====
collected 94-99 items
tests/ ... PASSED [100%]

====== coverage =====
TOTAL ... ≥80%
```

**Dependencies**: T039
**Priority**: P0
**Estimated Effort**: 10 minutes

---

## Task Dependencies Graph

```
T001 (Add Rich)
  ↓
T002 (Verify Rich)
  ↓
T003 (Create theme.py)
  ↓
T004 (Create rich_components.py)
  ↓
T005 (Write theme tests) → T006 → T007 → T008 → T009 (Implement Theme)
  ↓
T010 (Console Singleton) ← T009
  ↓
T011 (Create component tests)
  ↓
T012 (RichTableBuilder.__init__)
  ↓
T013 (Write table tests) → T014 → T015 (Implement RichTableBuilder)
  ↓
T016 (ConsoleUI.display_all_tasks tests) → T019 (Update display methods)
  ↓
T017 (Write message tests) → T018 (RichMessageFormatter) → T020 (ConsoleUI tests)
  ↓
T021 (Write menu tests) → T022 (RichMenuBuilder) → T023 (Update display_menu)
  ↓
T024 (Write prompt tests) → T025 (RichPromptHelper) → T026-T027 (Update input methods)
  ↓
T028 (Full test suite)
  ↓
T029 (Coverage check)
  ↓
T030-T035 (Manual testing)
  ↓
T036-T040 (Documentation & finalization)
```

---

## Summary Statistics

| Phase | Tasks | Effort | Status |
|-------|-------|--------|--------|
| 1 | T001-T004 | 30 min | Setup |
| 2 | T005-T009 | 65 min | Theme |
| 3 | T010-T012 | 30 min | Singleton |
| 4 | T013-T016 | 95 min | Tables |
| 5 | T017-T020 | 70 min | Messages |
| 6 | T021-T023 | 55 min | Menu |
| 7 | T024-T027 | 90 min | Prompts |
| 8 | T028-T030 | 25 min | Integration |
| 9 | T031-T035 | 50 min | Testing |
| 10 | T036-T040 | 70 min | Documentation |
| **TOTAL** | **40 tasks** | **580 min (9.7 hrs)** | **Ready** |

---

## Next Steps

1. **Start with Phase 1**: Setup Rich dependency and create file structure
2. **Follow TDD approach**: Write tests (Red) → Implement (Green) → Refactor
3. **Test frequently**: Run `pytest` after each phase
4. **Commit regularly**: Git commit after each completed phase
5. **Manual testing**: Verify visual output matches expectations
6. **Documentation**: Update README and docstrings as you go

**Ready to implement**: `/sp.implement`
