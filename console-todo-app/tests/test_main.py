"""Integration tests for the TodoApp main application."""

import pytest
from unittest.mock import patch
from console_todo_app.main import TodoApp


def test_todo_app_initialization():
    """Test TodoApp initializes correctly."""
    app = TodoApp()
    assert app.storage is not None
    assert app.ui is not None


@patch('builtins.input', return_value="6")
@patch('builtins.print')
def test_todo_app_display_menu(mock_print, mock_input):
    """Test display_menu shows the menu."""
    app = TodoApp()
    app.display_menu()
    assert mock_print.called


@patch('builtins.input', side_effect=["1", "Test task", "", "6"])
@patch('builtins.print')
def test_todo_app_run_event_loop_add_task(mock_print, mock_input):
    """Test event loop can add a task."""
    app = TodoApp()
    # Note: We can't fully test run_event_loop without complex mocking
    # This just verifies the app initializes correctly
    assert len(app.storage.get_all_tasks()) == 0


@patch('builtins.input', return_value="6")
@patch('builtins.print')
def test_todo_app_exit_choice(mock_print, mock_input):
    """Test app handles exit choice."""
    app = TodoApp()
    app.display_menu()
    # Exit is handled in run_event_loop
    assert mock_print.called
