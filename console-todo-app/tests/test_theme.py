"""Unit tests for Theme configuration."""

import pytest
from console_todo_app.ui.theme import Theme, default_theme


class TestThemeColors:
    """Test color constants in Theme class."""

    def test_theme_primary_color(self):
        """Test PRIMARY color is defined correctly."""
        assert hasattr(Theme, 'PRIMARY')
        assert Theme.PRIMARY == "blue"

    def test_theme_success_color(self):
        """Test SUCCESS color is defined correctly."""
        assert hasattr(Theme, 'SUCCESS')
        assert Theme.SUCCESS == "green"

    def test_theme_error_color(self):
        """Test ERROR color is defined correctly."""
        assert hasattr(Theme, 'ERROR')
        assert Theme.ERROR == "red"

    def test_theme_warning_color(self):
        """Test WARNING color is defined correctly."""
        assert hasattr(Theme, 'WARNING')
        assert Theme.WARNING == "yellow"

    def test_theme_muted_color(self):
        """Test MUTED color is defined correctly."""
        assert hasattr(Theme, 'MUTED')
        assert Theme.MUTED == "dim white"


class TestThemeSymbols:
    """Test symbol constants in Theme class."""

    def test_theme_symbol_success(self):
        """Test SUCCESS symbol is defined correctly."""
        assert hasattr(Theme, 'SYMBOL_SUCCESS')
        assert Theme.SYMBOL_SUCCESS == "[OK]"

    def test_theme_symbol_error(self):
        """Test ERROR symbol is defined correctly."""
        assert hasattr(Theme, 'SYMBOL_ERROR')
        assert Theme.SYMBOL_ERROR == "[X]"

    def test_theme_symbol_info(self):
        """Test INFO symbol is defined correctly."""
        assert hasattr(Theme, 'SYMBOL_INFO')
        assert Theme.SYMBOL_INFO == "[i]"

    def test_theme_symbol_complete(self):
        """Test COMPLETE symbol is defined correctly."""
        assert hasattr(Theme, 'SYMBOL_COMPLETE')
        assert Theme.SYMBOL_COMPLETE == "[OK]"

    def test_theme_symbol_incomplete(self):
        """Test INCOMPLETE symbol is defined correctly."""
        assert hasattr(Theme, 'SYMBOL_INCOMPLETE')
        assert Theme.SYMBOL_INCOMPLETE == "[ ]"


class TestThemeTableStyling:
    """Test table styling configuration in Theme class."""

    def test_theme_table_border_style(self):
        """Test TABLE_BORDER_STYLE is defined correctly."""
        assert hasattr(Theme, 'TABLE_BORDER_STYLE')
        assert Theme.TABLE_BORDER_STYLE == "blue"

    def test_theme_table_header_style(self):
        """Test TABLE_HEADER_STYLE is defined correctly."""
        assert hasattr(Theme, 'TABLE_HEADER_STYLE')
        assert Theme.TABLE_HEADER_STYLE == "bold blue"

    def test_theme_table_title(self):
        """Test TABLE_TITLE is defined correctly."""
        assert hasattr(Theme, 'TABLE_TITLE')
        assert Theme.TABLE_TITLE == "[Tasks]"

    def test_theme_table_show_lines(self):
        """Test TABLE_SHOW_LINES is defined correctly."""
        assert hasattr(Theme, 'TABLE_SHOW_LINES')
        assert Theme.TABLE_SHOW_LINES is True


class TestThemeMenuStyling:
    """Test menu styling configuration in Theme class."""

    def test_theme_menu_border_style(self):
        """Test MENU_BORDER_STYLE is defined correctly."""
        assert hasattr(Theme, 'MENU_BORDER_STYLE')
        assert Theme.MENU_BORDER_STYLE == "blue"

    def test_theme_menu_title_style(self):
        """Test MENU_TITLE_STYLE is defined correctly."""
        assert hasattr(Theme, 'MENU_TITLE_STYLE')
        assert Theme.MENU_TITLE_STYLE == "bold blue"

    def test_theme_menu_title_text(self):
        """Test MENU_TITLE_TEXT is defined correctly."""
        assert hasattr(Theme, 'MENU_TITLE_TEXT')
        assert Theme.MENU_TITLE_TEXT == "TODO APPLICATION"


class TestThemePromptStyling:
    """Test prompt styling configuration in Theme class."""

    def test_theme_prompt_style(self):
        """Test PROMPT_STYLE is defined correctly."""
        assert hasattr(Theme, 'PROMPT_STYLE')
        assert Theme.PROMPT_STYLE == "cyan"


class TestDefaultTheme:
    """Test default theme instance."""

    def test_default_theme_instance_exists(self):
        """Test default_theme instance is created."""
        assert default_theme is not None

    def test_default_theme_is_theme_instance(self):
        """Test default_theme is an instance of Theme."""
        assert isinstance(default_theme, Theme)

    def test_default_theme_has_primary_color(self):
        """Test default_theme can access colors."""
        assert default_theme.PRIMARY == "blue"

    def test_default_theme_has_symbols(self):
        """Test default_theme can access symbols."""
        assert default_theme.SYMBOL_SUCCESS == "[OK]"
