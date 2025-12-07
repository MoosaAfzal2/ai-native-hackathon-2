"""Unit tests for Rich component builders."""

import pytest
from io import StringIO
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from console_todo_app.ui.rich_components import (
    RichTableBuilder,
    RichMessageFormatter,
    RichMenuBuilder,
    RichPromptHelper,
    get_console,
)
from console_todo_app.ui.theme import Theme, default_theme
from console_todo_app.models.task import Task


class TestRichTableBuilder:
    """Test RichTableBuilder class."""

    def test_builder_initialization(self):
        """Test RichTableBuilder can be instantiated."""
        builder = RichTableBuilder()
        assert builder is not None

    def test_builder_initialization_with_theme(self):
        """Test RichTableBuilder accepts custom theme."""
        theme = Theme()
        builder = RichTableBuilder(theme)
        assert builder.theme is theme

    def test_builder_default_theme(self):
        """Test RichTableBuilder uses default_theme if none provided."""
        builder = RichTableBuilder()
        assert builder.theme is default_theme

    def test_build_task_table_empty_list(self):
        """Test creating table with empty task list."""
        builder = RichTableBuilder()
        table = builder.build_task_table([])
        assert isinstance(table, Table)

    def test_build_task_table_single_task(self):
        """Test creating table with single task."""
        builder = RichTableBuilder()
        task = Task(id=1, title="Test Task", is_complete=False)
        table = builder.build_task_table([task])
        assert isinstance(table, Table)

    def test_build_task_table_multiple_tasks(self):
        """Test creating table with multiple tasks."""
        tasks = [
            Task(id=1, title="Task 1", is_complete=False),
            Task(id=2, title="Task 2", is_complete=True),
            Task(id=3, title="Task 3", is_complete=False),
        ]
        builder = RichTableBuilder()
        table = builder.build_task_table(tasks)
        assert isinstance(table, Table)

    def test_build_task_table_returns_table(self):
        """Test build_task_table returns Rich Table."""
        builder = RichTableBuilder()
        tasks = [Task(id=1, title="Test", is_complete=False)]
        table = builder.build_task_table(tasks)
        assert isinstance(table, Table)

    def test_build_empty_state_table(self):
        """Test creating empty state panel."""
        builder = RichTableBuilder()
        panel = builder.build_empty_state_table()
        assert isinstance(panel, Panel)

    def test_build_empty_state_panel_type(self):
        """Test build_empty_state_table returns Panel."""
        builder = RichTableBuilder()
        result = builder.build_empty_state_table()
        assert isinstance(result, Panel)


class TestRichMessageFormatter:
    """Test RichMessageFormatter class."""

    def test_formatter_initialization(self):
        """Test RichMessageFormatter can be instantiated."""
        formatter = RichMessageFormatter()
        assert formatter is not None

    def test_formatter_initialization_with_theme(self):
        """Test RichMessageFormatter accepts custom theme."""
        theme = Theme()
        formatter = RichMessageFormatter(theme)
        assert formatter.theme is theme

    def test_formatter_default_theme(self):
        """Test RichMessageFormatter uses default_theme if none provided."""
        formatter = RichMessageFormatter()
        assert formatter.theme is default_theme

    def test_success_message_format(self):
        """Test success message formatting."""
        formatter = RichMessageFormatter()
        msg = formatter.success("Task created")
        assert msg is not None
        assert isinstance(msg, str)
        assert "✓" in msg

    def test_success_message_contains_green(self):
        """Test success message contains green color markup."""
        formatter = RichMessageFormatter()
        msg = formatter.success("Task created")
        assert "[green]" in msg or "[g]" in msg.lower()

    def test_error_message_format(self):
        """Test error message formatting."""
        formatter = RichMessageFormatter()
        msg = formatter.error("Task not found")
        assert msg is not None
        assert isinstance(msg, str)
        assert "✗" in msg

    def test_error_message_contains_red(self):
        """Test error message contains red color markup."""
        formatter = RichMessageFormatter()
        msg = formatter.error("Task not found")
        assert "[red]" in msg or "[r]" in msg.lower()

    def test_info_message_format(self):
        """Test info message formatting."""
        formatter = RichMessageFormatter()
        msg = formatter.info("Please confirm")
        assert msg is not None
        assert isinstance(msg, str)
        assert "ℹ" in msg

    def test_info_message_contains_blue(self):
        """Test info message contains blue color markup."""
        formatter = RichMessageFormatter()
        msg = formatter.info("Please confirm")
        assert "[blue]" in msg or "[b]" in msg.lower()


class TestRichMenuBuilder:
    """Test RichMenuBuilder class."""

    def test_builder_initialization(self):
        """Test RichMenuBuilder can be instantiated."""
        builder = RichMenuBuilder()
        assert builder is not None

    def test_builder_initialization_with_theme(self):
        """Test RichMenuBuilder accepts custom theme."""
        theme = Theme()
        builder = RichMenuBuilder(theme)
        assert builder.theme is theme

    def test_builder_default_theme(self):
        """Test RichMenuBuilder uses default_theme if none provided."""
        builder = RichMenuBuilder()
        assert builder.theme is default_theme

    def test_build_menu_returns_panel_or_list(self):
        """Test build_menu returns Panel or list of Panels."""
        builder = RichMenuBuilder()
        menu = builder.build_menu()
        assert menu is not None
        assert isinstance(menu, (Panel, list))

    def test_build_menu_returns_items(self):
        """Test build_menu returns valid menu structure."""
        builder = RichMenuBuilder()
        menu = builder.build_menu()
        # Either a Panel or list of Panels
        if isinstance(menu, list):
            assert len(menu) > 0
            assert all(isinstance(item, Panel) for item in menu)
        else:
            assert isinstance(menu, Panel)


class TestRichPromptHelper:
    """Test RichPromptHelper class."""

    def test_helper_initialization(self):
        """Test RichPromptHelper can be instantiated."""
        helper = RichPromptHelper()
        assert helper is not None

    def test_helper_initialization_with_theme(self):
        """Test RichPromptHelper accepts custom theme."""
        theme = Theme()
        helper = RichPromptHelper(theme=theme)
        assert helper.theme is theme

    def test_helper_default_theme(self):
        """Test RichPromptHelper uses default_theme if none provided."""
        helper = RichPromptHelper()
        assert helper.theme is default_theme

    def test_helper_initialization_with_console(self):
        """Test RichPromptHelper accepts custom console."""
        console = Console()
        helper = RichPromptHelper(console=console)
        assert helper.console is console

    def test_helper_default_console(self):
        """Test RichPromptHelper uses singleton console if none provided."""
        helper = RichPromptHelper()
        assert helper.console is not None

    def test_helper_methods_exist(self):
        """Test RichPromptHelper has required methods."""
        helper = RichPromptHelper()
        assert hasattr(helper, 'prompt_text')
        assert hasattr(helper, 'prompt_integer')
        assert hasattr(helper, 'prompt_confirmation')
        assert callable(helper.prompt_text)
        assert callable(helper.prompt_integer)
        assert callable(helper.prompt_confirmation)


class TestGetConsole:
    """Test console singleton pattern."""

    def test_get_console_returns_console(self):
        """Test get_console returns a Console instance."""
        console = get_console()
        assert isinstance(console, Console)

    def test_get_console_singleton(self):
        """Test get_console returns same instance (singleton)."""
        console1 = get_console()
        console2 = get_console()
        assert console1 is console2
