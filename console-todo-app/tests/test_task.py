"""Unit tests for Task model."""

import pytest
from datetime import datetime
from console_todo_app.models.task import Task


# RED PHASE: Tests for Task creation
def test_task_creation_with_all_attributes():
    """Test Task instantiation with all attributes."""
    created_at = datetime.now()
    task = Task(id=1, title="Buy groceries", description="Milk, eggs, bread", created_at=created_at, is_complete=False)
    assert task.id == 1
    assert task.title == "Buy groceries"
    assert task.description == "Milk, eggs, bread"
    assert task.created_at == created_at
    assert task.is_complete == False


def test_task_creation_without_description():
    """Test Task creation without description (default empty string)."""
    task = Task(id=1, title="Buy groceries")
    assert task.title == "Buy groceries"
    assert task.description == ""
    assert task.is_complete == False


def test_task_creation_sets_created_at_if_not_provided():
    """Test Task creation sets created_at to current datetime if not provided."""
    before = datetime.now()
    task = Task(id=1, title="Test task")
    after = datetime.now()
    assert before <= task.created_at <= after


def test_task_immutability_of_id():
    """Test Task id cannot be modified."""
    task = Task(id=1, title="Test")
    with pytest.raises(AttributeError):
        task.id = 2


def test_task_immutability_of_created_at():
    """Test Task created_at cannot be modified."""
    task = Task(id=1, title="Test")
    new_time = datetime.now()
    with pytest.raises(AttributeError):
        task.created_at = new_time


# RED PHASE: Tests for title validation
def test_title_validation_empty_title():
    """Test Task rejects empty title."""
    with pytest.raises(ValueError):
        Task(id=1, title="")


def test_title_validation_title_too_long():
    """Test Task rejects title > 200 characters."""
    long_title = "a" * 201
    with pytest.raises(ValueError):
        Task(id=1, title=long_title)


def test_title_validation_valid_title_200_chars():
    """Test Task accepts title of exactly 200 characters."""
    title = "a" * 200
    task = Task(id=1, title=title)
    assert len(task.title) == 200


def test_title_validation_trims_whitespace():
    """Test Task trims leading/trailing whitespace from title."""
    task = Task(id=1, title="  Buy groceries  ")
    assert task.title == "Buy groceries"


# RED PHASE: Tests for description validation
def test_description_validation_empty_description_allowed():
    """Test Task allows empty description."""
    task = Task(id=1, title="Test", description="")
    assert task.description == ""


def test_description_validation_too_long():
    """Test Task rejects description > 1000 characters."""
    long_desc = "a" * 1001
    with pytest.raises(ValueError):
        Task(id=1, title="Test", description=long_desc)


def test_description_validation_valid_description_1000_chars():
    """Test Task accepts description of exactly 1000 characters."""
    desc = "a" * 1000
    task = Task(id=1, title="Test", description=desc)
    assert len(task.description) == 1000


def test_description_validation_trims_whitespace():
    """Test Task trims leading/trailing whitespace from description."""
    task = Task(id=1, title="Test", description="  Important details  ")
    assert task.description == "Important details"


# RED PHASE: Tests for status methods
def test_toggle_status_false_to_true():
    """Test toggle_status() changes False to True."""
    task = Task(id=1, title="Test", is_complete=False)
    task.toggle_status()
    assert task.is_complete == True


def test_toggle_status_true_to_false():
    """Test toggle_status() changes True to False."""
    task = Task(id=1, title="Test", is_complete=True)
    task.toggle_status()
    assert task.is_complete == False


def test_mark_complete():
    """Test mark_complete() sets status to True."""
    task = Task(id=1, title="Test", is_complete=False)
    task.mark_complete()
    assert task.is_complete == True


def test_mark_incomplete():
    """Test mark_incomplete() sets status to False."""
    task = Task(id=1, title="Test", is_complete=True)
    task.mark_incomplete()
    assert task.is_complete == False


def test_multiple_status_changes():
    """Test multiple consecutive status changes."""
    task = Task(id=1, title="Test")
    assert task.is_complete == False
    task.toggle_status()
    assert task.is_complete == True
    task.toggle_status()
    assert task.is_complete == False
    task.mark_complete()
    assert task.is_complete == True
    task.mark_incomplete()
    assert task.is_complete == False


# RED PHASE: Tests for string representation
def test_task_str_method():
    """Test Task __str__ method returns readable representation."""
    task = Task(id=1, title="Buy groceries", description="Milk, eggs, bread")
    str_repr = str(task)
    assert "1" in str_repr
    assert "Buy groceries" in str_repr
    assert isinstance(str_repr, str)


def test_task_repr_method():
    """Test Task __repr__ method for debugging."""
    task = Task(id=1, title="Test")
    repr_str = repr(task)
    assert isinstance(repr_str, str)
    assert "Task" in repr_str

