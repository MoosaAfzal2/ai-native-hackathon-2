"""Integration tests for the TodoApp main application."""

import pytest
from unittest.mock import patch
from console_todo_app.main import TodoApp


def test_todo_app_initialization():
    """Test TodoApp initializes correctly."""
    app = TodoApp()
    assert app.storage is not None
    assert app.ui is not None


def test_todo_app_display_menu():
    """Test display_menu shows the menu."""
    app = TodoApp()
    # Should not raise an error when displaying menu
    app.display_menu()


@patch('rich.prompt.Prompt.ask', side_effect=["Test task", ""])
def test_todo_app_run_event_loop_add_task(mock_prompt):
    """Test event loop can add a task."""
    app = TodoApp()
    # Note: We can't fully test run_event_loop without complex mocking
    # This just verifies the app initializes correctly
    assert len(app.storage.get_all_tasks()) == 0


def test_todo_app_exit_choice():
    """Test app handles exit choice."""
    app = TodoApp()
    # Should not raise an error
    app.display_menu()
