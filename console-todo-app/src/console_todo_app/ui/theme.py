"""Color theme and styling configuration for Rich UI."""


class Theme:
    """Color and styling theme for the Rich console application.

    Attributes:
        PRIMARY: Primary brand color used for titles and headers
        SUCCESS: Color for success messages and completed items
        ERROR: Color for error messages and failed operations
        WARNING: Color for warning messages and pending items
        MUTED: Color for secondary text and less important information

        SYMBOL_SUCCESS: Symbol displayed with success messages (checkmark)
        SYMBOL_ERROR: Symbol displayed with error messages (X mark)
        SYMBOL_INFO: Symbol displayed with info messages
        SYMBOL_COMPLETE: Symbol for completed tasks
        SYMBOL_INCOMPLETE: Symbol for incomplete tasks

        TABLE_BORDER_STYLE: Style for table borders
        TABLE_HEADER_STYLE: Style for table headers
        TABLE_TITLE: Title text for task table
        TABLE_SHOW_LINES: Whether to show grid lines in tables

        MENU_BORDER_STYLE: Style for menu panel borders
        MENU_TITLE_STYLE: Style for menu title text
        MENU_TITLE_TEXT: Text content for menu title
        PROMPT_STYLE: Style for input prompts
    """

    # Primary colors
    PRIMARY: str = "blue"
    SUCCESS: str = "green"
    ERROR: str = "red"
    WARNING: str = "yellow"
    MUTED: str = "dim white"

    # Symbols
    SYMBOL_SUCCESS: str = "✓"
    SYMBOL_ERROR: str = "✗"
    SYMBOL_INFO: str = "ℹ"
    SYMBOL_COMPLETE: str = "✓"
    SYMBOL_INCOMPLETE: str = "○"

    # Table styling
    TABLE_BORDER_STYLE: str = "blue"
    TABLE_HEADER_STYLE: str = "bold blue"
    TABLE_TITLE: str = "📋 Your Tasks"
    TABLE_SHOW_LINES: bool = True

    # Menu styling
    MENU_BORDER_STYLE: str = "blue"
    MENU_TITLE_STYLE: str = "bold blue"
    MENU_TITLE_TEXT: str = "TODO APPLICATION"

    # Prompt styling
    PROMPT_STYLE: str = "cyan"


# Global default theme instance
default_theme: Theme = Theme()
