"""Rich component builders for styled console output.

This module provides wrapper classes around Rich library components
to encapsulate complexity and provide clean interfaces for UI layer.
"""

from typing import Optional, List, Union
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from console_todo_app.models.task import Task
from console_todo_app.ui.theme import Theme, default_theme


# Singleton console instance
_console: Optional[Console] = None


def get_console() -> Console:
    """Get or create the Rich Console singleton instance.

    Returns:
        Console: Shared Rich console instance for all UI operations.
    """
    global _console
    if _console is None:
        _console = Console()
    return _console


class RichTableBuilder:
    """Builder class for creating styled Rich tables.

    Attributes:
        theme: Theme instance for styling configuration.
    """

    def __init__(self, theme: Optional[Theme] = None) -> None:
        """Initialize RichTableBuilder with optional theme.

        Args:
            theme: Optional Theme instance. Defaults to default_theme.
        """
        self.theme = theme or default_theme

    def build_task_table(self, tasks: List[Task]) -> Table:
        """Build a styled Rich table from task list.

        Args:
            tasks: List of Task objects to display.

        Returns:
            Rich Table configured with task data and styling.
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
            status = (
                f"[{self.theme.SUCCESS}]{self.theme.SYMBOL_COMPLETE}[/] Complete"
                if task.is_complete
                else f"[{self.theme.WARNING}]{self.theme.SYMBOL_INCOMPLETE}[/] Pending"
            )
            table.add_row(
                str(task.id),
                task.title,
                status,
                task.created_at.strftime("%Y-%m-%d %H:%M"),
            )

        return table

    def build_empty_state_table(self) -> Panel:
        """Build a styled panel for empty task list.

        Returns:
            Rich Panel with empty state message.
        """
        return Panel(
            "[yellow]No tasks found[/]",
            border_style=self.theme.TABLE_BORDER_STYLE,
            title="Tasks",
            expand=False,
        )


class RichMessageFormatter:
    """Formatter for styled console messages using Rich markup.

    Attributes:
        theme: Theme instance for styling configuration.
    """

    def __init__(self, theme: Optional[Theme] = None) -> None:
        """Initialize RichMessageFormatter with optional theme.

        Args:
            theme: Optional Theme instance. Defaults to default_theme.
        """
        self.theme = theme or default_theme

    def success(self, message: str) -> str:
        """Format a success message with green color and checkmark.

        Args:
            message: Message text to format.

        Returns:
            Rich markup formatted string ready for console output.
        """
        return f"[{self.theme.SUCCESS}]{self.theme.SYMBOL_SUCCESS}[/] {message}"

    def error(self, message: str) -> str:
        """Format an error message with red color and X mark.

        Args:
            message: Message text to format.

        Returns:
            Rich markup formatted string ready for console output.
        """
        return f"[{self.theme.ERROR}]{self.theme.SYMBOL_ERROR}[/] {message}"

    def info(self, message: str) -> str:
        """Format an info message with blue color and info symbol.

        Args:
            message: Message text to format.

        Returns:
            Rich markup formatted string ready for console output.
        """
        return f"[{self.theme.PRIMARY}]{self.theme.SYMBOL_INFO}[/] {message}"


class RichMenuBuilder:
    """Builder class for creating styled Rich menu panels.

    Attributes:
        theme: Theme instance for styling configuration.
    """

    def __init__(self, theme: Optional[Theme] = None) -> None:
        """Initialize RichMenuBuilder with optional theme.

        Args:
            theme: Optional Theme instance. Defaults to default_theme.
        """
        self.theme = theme or default_theme

    def build_menu(self) -> Union[Panel, list]:
        """Build styled menu panel(s).

        Returns:
            Panel or list of Panels with menu structure.
        """
        from rich.text import Text

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
        for i, option in enumerate(options):
            if i > 0:
                options_text.append("\n")
            options_text.append(option)

        options_panel = Panel(
            options_text,
            border_style=self.theme.MENU_BORDER_STYLE,
            padding=(1, 2),
        )

        return [title_panel, options_panel]


class RichPromptHelper:
    """Wrapper for Rich Prompt components with validation.

    Attributes:
        console: Rich Console instance for output.
        theme: Theme instance for styling configuration.
    """

    def __init__(
        self,
        console: Optional[Console] = None,
        theme: Optional[Theme] = None,
    ) -> None:
        """Initialize helper with optional console and theme.

        Args:
            console: Optional Console instance. Defaults to singleton.
            theme: Optional Theme instance. Defaults to default_theme.
        """
        self.console = console or get_console()
        self.theme = theme or default_theme

    def prompt_text(
        self, prompt: str, max_length: Optional[int] = None
    ) -> str:
        """Prompt for text input with optional length validation.

        Args:
            prompt: Prompt text to display.
            max_length: Maximum length constraint (optional).

        Returns:
            User input string.

        Raises:
            ValueError: If max_length validation fails.
        """
        from rich.prompt import Prompt

        while True:
            result = Prompt.ask(
                f"[{self.theme.PROMPT_STYLE}]{prompt}[/]",
                console=self.console,
            )
            if max_length and len(result) > max_length:
                error_msg = self.error(
                    f"Text too long (max {max_length}). Current: {len(result)}"
                )
                self.console.print(error_msg)
                continue
            return result

    def prompt_integer(self, prompt: str) -> int:
        """Prompt for integer input with error handling.

        Args:
            prompt: Prompt text to display.

        Returns:
            Valid integer from user input.

        Raises:
            ValueError: If input is not a valid integer.
        """
        from rich.prompt import IntPrompt

        while True:
            try:
                return IntPrompt.ask(
                    f"[{self.theme.PROMPT_STYLE}]{prompt}[/]",
                    console=self.console,
                )
            except ValueError:
                error_msg = self.error("Please enter a valid number")
                self.console.print(error_msg)

    def prompt_confirmation(self, prompt: str) -> bool:
        """Prompt for yes/no confirmation.

        Args:
            prompt: Prompt text to display.

        Returns:
            True if user confirms, False otherwise.
        """
        from rich.prompt import Confirm

        return Confirm.ask(
            f"[{self.theme.PROMPT_STYLE}]{prompt}[/]",
            console=self.console,
        )

    def error(self, message: str) -> str:
        """Format error message (helper method).

        Args:
            message: Error message text.

        Returns:
            Formatted error message.
        """
        return f"[{self.theme.ERROR}]{self.theme.SYMBOL_ERROR}[/] {message}"
