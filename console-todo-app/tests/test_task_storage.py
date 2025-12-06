"""Unit tests for TaskStorage class."""

import pytest
from console_todo_app.models.task import Task
from console_todo_app.storage.task_storage import TaskStorage


# RED PHASE: Tests for TaskStorage initialization
def test_task_storage_initialization():
    """Test TaskStorage initializes with empty storage and ID counter at 1."""
    storage = TaskStorage()
    assert storage.get_all_tasks() == []


def test_task_storage_next_id_starts_at_one():
    """Test that next_id starts at 1."""
    storage = TaskStorage()
    task = storage.add_task("First task")
    assert task.id == 1


# RED PHASE: Tests for add_task
def test_add_task_creates_task_with_title_only():
    """Test add_task creates a task with title only."""
    storage = TaskStorage()
    task = storage.add_task("Buy milk")
    assert task.title == "Buy milk"
    assert task.description == ""
    assert task.is_complete == False


def test_add_task_creates_task_with_title_and_description():
    """Test add_task creates a task with title and description."""
    storage = TaskStorage()
    task = storage.add_task("Buy groceries", "Milk, eggs, bread")
    assert task.title == "Buy groceries"
    assert task.description == "Milk, eggs, bread"
    assert task.is_complete == False


def test_add_task_increments_id():
    """Test add_task increments ID for each new task."""
    storage = TaskStorage()
    task1 = storage.add_task("Task 1")
    task2 = storage.add_task("Task 2")
    task3 = storage.add_task("Task 3")
    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3


def test_add_task_returns_task_object():
    """Test add_task returns a Task object."""
    storage = TaskStorage()
    task = storage.add_task("New task")
    assert isinstance(task, Task)


# RED PHASE: Tests for get_all_tasks
def test_get_all_tasks_returns_empty_list_initially():
    """Test get_all_tasks returns empty list initially."""
    storage = TaskStorage()
    assert storage.get_all_tasks() == []


def test_get_all_tasks_returns_all_added_tasks():
    """Test get_all_tasks returns all added tasks."""
    storage = TaskStorage()
    task1 = storage.add_task("Task 1")
    task2 = storage.add_task("Task 2")
    task3 = storage.add_task("Task 3")
    tasks = storage.get_all_tasks()
    assert len(tasks) == 3
    assert task1 in tasks
    assert task2 in tasks
    assert task3 in tasks


def test_get_all_tasks_returns_tasks_in_order():
    """Test get_all_tasks returns tasks in insertion order."""
    storage = TaskStorage()
    task1 = storage.add_task("First")
    task2 = storage.add_task("Second")
    task3 = storage.add_task("Third")
    tasks = storage.get_all_tasks()
    assert tasks[0].id == 1
    assert tasks[1].id == 2
    assert tasks[2].id == 3


def test_get_all_tasks_returns_copy_not_reference():
    """Test get_all_tasks returns a copy, not reference to internal storage."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    tasks1 = storage.get_all_tasks()
    storage.add_task("Task 2")
    tasks2 = storage.get_all_tasks()
    assert len(tasks1) == 1
    assert len(tasks2) == 2


# RED PHASE: Tests for get_task
def test_get_task_returns_task_by_id():
    """Test get_task returns the correct task by ID."""
    storage = TaskStorage()
    task1 = storage.add_task("First task")
    task2 = storage.add_task("Second task")
    retrieved = storage.get_task(2)
    assert retrieved.id == 2
    assert retrieved.title == "Second task"


def test_get_task_raises_key_error_for_nonexistent_id():
    """Test get_task raises KeyError when task doesn't exist."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    with pytest.raises(KeyError):
        storage.get_task(999)


def test_get_task_with_zero_id_raises_key_error():
    """Test get_task with ID 0 raises KeyError."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    with pytest.raises(KeyError):
        storage.get_task(0)


def test_get_task_with_negative_id_raises_key_error():
    """Test get_task with negative ID raises KeyError."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    with pytest.raises(KeyError):
        storage.get_task(-1)


# RED PHASE: Tests for delete_task
def test_delete_task_removes_task():
    """Test delete_task removes a task from storage."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    storage.add_task("Task 2")
    storage.add_task("Task 3")
    storage.delete_task(2)
    tasks = storage.get_all_tasks()
    assert len(tasks) == 2
    assert all(t.id != 2 for t in tasks)


def test_delete_task_raises_key_error_for_nonexistent_id():
    """Test delete_task raises KeyError when task doesn't exist."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    with pytest.raises(KeyError):
        storage.delete_task(999)


def test_delete_task_does_not_reuse_deleted_id():
    """Test that deleting a task doesn't reuse its ID for new tasks."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    task2 = storage.add_task("Task 2")
    storage.add_task("Task 3")
    storage.delete_task(2)
    task4 = storage.add_task("Task 4")
    assert task4.id == 4


# RED PHASE: Tests for update_task
def test_update_task_updates_title():
    """Test update_task updates task title."""
    storage = TaskStorage()
    storage.add_task("Old title")
    storage.update_task(1, title="New title")
    task = storage.get_task(1)
    assert task.title == "New title"


def test_update_task_updates_description():
    """Test update_task updates task description."""
    storage = TaskStorage()
    storage.add_task("Task", "Old description")
    storage.update_task(1, description="New description")
    task = storage.get_task(1)
    assert task.description == "New description"


def test_update_task_updates_both_title_and_description():
    """Test update_task updates both title and description."""
    storage = TaskStorage()
    storage.add_task("Old", "Old desc")
    storage.update_task(1, title="New", description="New desc")
    task = storage.get_task(1)
    assert task.title == "New"
    assert task.description == "New desc"


def test_update_task_does_not_modify_other_fields():
    """Test update_task doesn't modify id, created_at, or is_complete."""
    storage = TaskStorage()
    task_orig = storage.add_task("Original")
    original_id = task_orig.id
    original_created_at = task_orig.created_at
    original_is_complete = task_orig.is_complete
    storage.update_task(1, title="Updated")
    task_updated = storage.get_task(1)
    assert task_updated.id == original_id
    assert task_updated.created_at == original_created_at
    assert task_updated.is_complete == original_is_complete


def test_update_task_raises_key_error_for_nonexistent_id():
    """Test update_task raises KeyError when task doesn't exist."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    with pytest.raises(KeyError):
        storage.update_task(999, title="New title")


def test_update_task_validates_title():
    """Test update_task validates new title."""
    storage = TaskStorage()
    storage.add_task("Task")
    with pytest.raises(ValueError):
        storage.update_task(1, title="")


def test_update_task_validates_description():
    """Test update_task validates new description."""
    storage = TaskStorage()
    storage.add_task("Task")
    with pytest.raises(ValueError):
        storage.update_task(1, description="a" * 1001)


# RED PHASE: Tests for toggle_task_status
def test_toggle_task_status_changes_incomplete_to_complete():
    """Test toggle_task_status changes incomplete task to complete."""
    storage = TaskStorage()
    storage.add_task("Task")
    storage.toggle_task_status(1)
    task = storage.get_task(1)
    assert task.is_complete == True


def test_toggle_task_status_changes_complete_to_incomplete():
    """Test toggle_task_status changes complete task to incomplete."""
    storage = TaskStorage()
    storage.add_task("Task")
    storage.toggle_task_status(1)
    storage.toggle_task_status(1)
    task = storage.get_task(1)
    assert task.is_complete == False


def test_toggle_task_status_raises_key_error_for_nonexistent_id():
    """Test toggle_task_status raises KeyError when task doesn't exist."""
    storage = TaskStorage()
    storage.add_task("Task")
    with pytest.raises(KeyError):
        storage.toggle_task_status(999)


# RED PHASE: Tests for storage boundary conditions
def test_storage_handles_many_tasks():
    """Test storage can handle many tasks."""
    storage = TaskStorage()
    for i in range(100):
        storage.add_task(f"Task {i}")
    tasks = storage.get_all_tasks()
    assert len(tasks) == 100
    assert tasks[0].id == 1
    assert tasks[99].id == 100


def test_storage_with_unicode_characters():
    """Test storage handles unicode characters in title and description."""
    storage = TaskStorage()
    task = storage.add_task("买菜 🛒", "牛奶、鸡蛋、面包 🥛🥚🍞")
    assert task.title == "买菜 🛒"
    assert task.description == "牛奶、鸡蛋、面包 🥛🥚🍞"


def test_storage_with_special_characters():
    """Test storage handles special characters."""
    storage = TaskStorage()
    task = storage.add_task("Task with @#$%^&*()", "Description with <>?:\"|{}")
    assert task.title == "Task with @#$%^&*()"
    assert task.description == "Description with <>?:\"|{}"


def test_get_all_tasks_after_multiple_operations():
    """Test get_all_tasks after add, delete, update sequence."""
    storage = TaskStorage()
    storage.add_task("Task 1")
    storage.add_task("Task 2")
    storage.add_task("Task 3")
    storage.delete_task(2)
    storage.update_task(1, title="Updated Task 1")
    tasks = storage.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Updated Task 1"
    assert tasks[1].id == 3
