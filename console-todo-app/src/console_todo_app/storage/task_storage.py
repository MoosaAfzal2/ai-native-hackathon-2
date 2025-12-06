"""Task storage with in-memory CRUD operations."""

from typing import List, Dict, Optional
from console_todo_app.models.task import Task


class TaskStorage:
    """In-memory storage for tasks with CRUD operations."""

    def __init__(self):
        """Initialize empty task storage."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task to storage.

        Args:
            title: Task title (1-200 characters)
            description: Task description (optional, max 1000 characters)

        Returns:
            Created Task object with auto-incremented ID

        Raises:
            ValueError: If title or description validation fails
        """
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks in insertion order.

        Returns:
            List of all Task objects. Returns empty list if no tasks exist.
        """
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Task:
        """Get a specific task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task object with matching ID

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        return self._tasks[task_id]

    def delete_task(self, task_id: int) -> None:
        """Delete a task from storage by ID.

        Args:
            task_id: The ID of the task to delete

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        del self._tasks[task_id]

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """Update task title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (optional). If provided, must be 1-200 characters.
            description: New description (optional). If provided, must be max 1000 characters.

        Returns:
            Updated Task object

        Raises:
            KeyError: If task with given ID doesn't exist
            ValueError: If new title or description validation fails
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} not found")

        original_task = self._tasks[task_id]
        new_title = title if title is not None else original_task.title
        new_description = description if description is not None else original_task.description

        # Create new task with updated fields (validation happens in Task.__post_init__)
        updated_task = Task(
            id=original_task.id,
            title=new_title,
            description=new_description,
            created_at=original_task.created_at,
            is_complete=original_task.is_complete
        )

        self._tasks[task_id] = updated_task
        return updated_task

    def toggle_task_status(self, task_id: int) -> None:
        """Toggle task completion status.

        Args:
            task_id: The ID of the task to toggle

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} not found")
        self._tasks[task_id].toggle_status()
