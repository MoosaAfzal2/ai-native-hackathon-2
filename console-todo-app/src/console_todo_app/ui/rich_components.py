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
        pass

    def build_empty_state_table(self) -> Panel:
        """Build a styled panel for empty task list.

        Returns:
            Rich Panel with empty state message.
        """
        pass


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
        pass

    def error(self, message: str) -> str:
        """Format an error message with red color and X mark.

        Args:
            message: Message text to format.

        Returns:
            Rich markup formatted string ready for console output.
        """
        pass

    def info(self, message: str) -> str:
        """Format an info message with blue color and info symbol.

        Args:
            message: Message text to format.

        Returns:
            Rich markup formatted string ready for console output.
        """
        pass


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
        pass


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
        pass

    def prompt_integer(self, prompt: str) -> int:
        """Prompt for integer input with error handling.

        Args:
            prompt: Prompt text to display.

        Returns:
            Valid integer from user input.

        Raises:
            ValueError: If input is not a valid integer.
        """
        pass

    def prompt_confirmation(self, prompt: str) -> bool:
        """Prompt for yes/no confirmation.

        Args:
            prompt: Prompt text to display.

        Returns:
            True if user confirms, False otherwise.
        """
        pass
