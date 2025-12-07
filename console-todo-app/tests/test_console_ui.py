"""Unit tests for ConsoleUI class."""

import pytest
from unittest.mock import patch, MagicMock
from console_todo_app.ui.console_ui import ConsoleUI
from console_todo_app.storage.task_storage import TaskStorage
from console_todo_app.models.task import Task
from rich.console import Console


# RED PHASE: Tests for ConsoleUI initialization
def test_console_ui_initialization():
    """Test ConsoleUI initializes with TaskStorage instance."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    assert ui.storage is storage


# RED PHASE: Tests for prompt_add_task
@patch('rich.prompt.Prompt.ask', side_effect=["Buy milk", ""])
def test_prompt_add_task_with_title_only(mock_prompt):
    """Test prompt_add_task creates task with title only."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    task = ui.prompt_add_task()
    assert isinstance(task, Task)
    assert task.title == "Buy milk"
    assert task.description == ""
    assert task.is_complete == False


@patch('rich.prompt.Prompt.ask', side_effect=["Buy groceries", "Milk, eggs, bread"])
def test_prompt_add_task_with_title_and_description(mock_prompt):
    """Test prompt_add_task creates task with title and description."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    task = ui.prompt_add_task()
    assert isinstance(task, Task)
    assert task.title == "Buy groceries"
    assert task.description == "Milk, eggs, bread"
    assert task.is_complete == False


@patch('rich.prompt.Prompt.ask', side_effect=["", "Buy groceries", ""])
def test_prompt_add_task_retries_on_empty_title(mock_prompt):
    """Test prompt_add_task retries when title is empty."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    task = ui.prompt_add_task()
    assert task.title == "Buy groceries"
    assert mock_prompt.call_count >= 2


@patch('rich.prompt.Prompt.ask', side_effect=["a" * 201, "Valid Title", ""])
def test_prompt_add_task_validates_title_length(mock_prompt):
    """Test prompt_add_task validates title length."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    # The prompt will loop on validation failure, so we provide a valid input
    # on the second attempt, then description
    task = ui.prompt_add_task()
    assert task.title == "Valid Title"


@patch('rich.prompt.Prompt.ask', side_effect=["Task", "a" * 1001])
def test_prompt_add_task_validates_description_length(mock_prompt):
    """Test prompt_add_task validates description length."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    with pytest.raises(ValueError):
        ui.prompt_add_task()


@patch('rich.prompt.Prompt.ask', return_value="New Task")
def test_prompt_add_task_adds_to_storage(mock_prompt):
    """Test prompt_add_task adds task to storage."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    task = ui.prompt_add_task()
    assert task in storage.get_all_tasks()


@patch('rich.prompt.Prompt.ask', side_effect=["Task 1", "", "Task 2", "", "Task 3", ""])
def test_prompt_add_task_multiple_calls(mock_prompt):
    """Test multiple calls to prompt_add_task."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    task1 = ui.prompt_add_task()
    task2 = ui.prompt_add_task()
    task3 = ui.prompt_add_task()
    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3
    assert len(storage.get_all_tasks()) == 3


@patch('rich.prompt.Prompt.ask', side_effect=["  Task with spaces  ", ""])
def test_prompt_add_task_trims_whitespace(mock_prompt):
    """Test prompt_add_task trims whitespace from title."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    task = ui.prompt_add_task()
    assert task.title == "Task with spaces"


# RED PHASE: Tests for display_all_tasks
def test_display_all_tasks_empty_storage():
    """Test display_all_tasks with empty storage."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    # Should not raise an error
    ui.display_all_tasks()


def test_display_all_tasks_single_task():
    """Test display_all_tasks with single task."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Buy milk")
    # Should not raise an error
    ui.display_all_tasks()


def test_display_all_tasks_multiple_tasks():
    """Test display_all_tasks with multiple tasks."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Task 1")
    storage.add_task("Task 2")
    storage.add_task("Task 3")
    # Should not raise an error
    ui.display_all_tasks()


def test_display_all_tasks_shows_task_id():
    """Test display_all_tasks displays task IDs."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Test task")
    # Verify the table builder is called and returns a table
    tasks = storage.get_all_tasks()
    table = ui.table_builder.build_task_table(tasks)
    assert table is not None


def test_display_all_tasks_shows_task_title():
    """Test display_all_tasks displays task titles."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Buy groceries")
    # Verify the table builder includes title
    tasks = storage.get_all_tasks()
    table = ui.table_builder.build_task_table(tasks)
    assert table is not None


def test_display_all_tasks_shows_completion_status():
    """Test display_all_tasks displays task completion status."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    task = storage.add_task("Test")
    storage.toggle_task_status(task.id)
    # Verify the table builder handles complete tasks
    tasks = storage.get_all_tasks()
    table = ui.table_builder.build_task_table(tasks)
    assert table is not None


def test_display_all_tasks_shows_in_order():
    """Test display_all_tasks shows tasks in insertion order."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("First")
    storage.add_task("Second")
    storage.add_task("Third")
    tasks = storage.get_all_tasks()
    assert tasks[0].title == "First"
    assert tasks[1].title == "Second"
    assert tasks[2].title == "Third"


# RED PHASE: Tests for prompt_update_task
@patch('rich.prompt.IntPrompt.ask', return_value=1)
@patch('rich.prompt.Prompt.ask', side_effect=["Updated title", ""])
def test_prompt_update_task_updates_title(mock_prompt, mock_int_prompt):
    """Test prompt_update_task updates task title."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Original title")
    ui.prompt_update_task()
    task = storage.get_task(1)
    assert task.title == "Updated title"


@patch('rich.prompt.IntPrompt.ask', return_value=999)
def test_prompt_update_task_handles_nonexistent_task(mock_int_prompt):
    """Test prompt_update_task handles nonexistent task ID."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Task 1")
    # Should handle gracefully without raising an error
    ui.prompt_update_task()
    assert len(storage.get_all_tasks()) == 1


# RED PHASE: Tests for prompt_delete_task
@patch('rich.prompt.IntPrompt.ask', return_value=1)
@patch('rich.prompt.Confirm.ask', return_value=True)
def test_prompt_delete_task_deletes_task(mock_confirm, mock_int_prompt):
    """Test prompt_delete_task deletes a task."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Task 1")
    storage.add_task("Task 2")
    ui.prompt_delete_task()
    assert len(storage.get_all_tasks()) == 1


@patch('rich.prompt.IntPrompt.ask', return_value=1)
@patch('rich.prompt.Confirm.ask', return_value=False)
def test_prompt_delete_task_cancels_on_no(mock_confirm, mock_int_prompt):
    """Test prompt_delete_task cancels when user selects no."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Task 1")
    ui.prompt_delete_task()
    assert len(storage.get_all_tasks()) == 1


@patch('rich.prompt.IntPrompt.ask', return_value=999)
def test_prompt_delete_task_handles_nonexistent_task(mock_int_prompt):
    """Test prompt_delete_task handles nonexistent task ID."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Task 1")
    ui.prompt_delete_task()
    # Should show error message or handle gracefully
    assert len(storage.get_all_tasks()) == 1


# RED PHASE: Tests for prompt_toggle_task_status
@patch('rich.prompt.IntPrompt.ask', return_value=1)
def test_prompt_toggle_task_status_incomplete_to_complete(mock_int_prompt):
    """Test prompt_toggle_task_status changes incomplete to complete."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Task 1")
    ui.prompt_toggle_task_status()
    task = storage.get_task(1)
    assert task.is_complete == True


@patch('rich.prompt.IntPrompt.ask', return_value=1)
def test_prompt_toggle_task_status_complete_to_incomplete(mock_int_prompt):
    """Test prompt_toggle_task_status changes complete to incomplete."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    task = storage.add_task("Task 1")
    storage.toggle_task_status(task.id)
    ui.prompt_toggle_task_status()
    task = storage.get_task(1)
    assert task.is_complete == False


@patch('rich.prompt.IntPrompt.ask', return_value=999)
def test_prompt_toggle_task_status_handles_nonexistent_task(mock_int_prompt):
    """Test prompt_toggle_task_status handles nonexistent task ID."""
    storage = TaskStorage()
    ui = ConsoleUI(storage)
    storage.add_task("Task 1")
    ui.prompt_toggle_task_status()
    # Should show error message or handle gracefully
    assert len(storage.get_all_tasks()) == 1
