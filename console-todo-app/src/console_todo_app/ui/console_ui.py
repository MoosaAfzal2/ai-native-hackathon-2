"""Console-based user interface for todo application."""

from console_todo_app.storage.task_storage import TaskStorage
from console_todo_app.models.task import Task


class ConsoleUI:
    """Handles console interactions for the todo application."""

    def __init__(self, storage: TaskStorage):
        """Initialize ConsoleUI with a TaskStorage instance.

        Args:
            storage: TaskStorage instance for managing tasks
        """
        self.storage = storage

    def prompt_add_task(self) -> Task:
        """Prompt user to add a new task.

        Returns:
            Created Task object

        Raises:
            ValueError: If validation fails
        """
        while True:
            try:
                title = input("Enter task title: ").strip()
                if not title:
                    print("Title cannot be empty. Please try again.")
                    continue
                description = input("Enter task description (optional): ").strip()
                task = self.storage.add_task(title, description)
                print(f"Task created: {task}")
                return task
            except ValueError as e:
                print(f"Error: {e}")
                raise

    def display_all_tasks(self) -> None:
        """Display all tasks in formatted output."""
        tasks = self.storage.get_all_tasks()
        if not tasks:
            print("\nNo tasks found.")
            return

        print("\n" + "=" * 70)
        print("TASK LIST")
        print("=" * 70)
        for task in tasks:
            print(task)
        print("=" * 70 + "\n")

    def prompt_update_task(self) -> None:
        """Prompt user to update a task."""
        self.display_all_tasks()
        try:
            task_id = int(input("Enter task ID to update: "))
            task = self.storage.get_task(task_id)
            print(f"Current task: {task}")

            new_title = input("Enter new title (leave blank to keep current): ").strip() or None
            new_description = input("Enter new description (leave blank to keep current): ").strip() or None

            updated_task = self.storage.update_task(task_id, title=new_title, description=new_description)
            print(f"Task updated: {updated_task}")
        except KeyError:
            print(f"Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def prompt_delete_task(self) -> None:
        """Prompt user to delete a task."""
        self.display_all_tasks()
        try:
            task_id = int(input("Enter task ID to delete: "))
            task = self.storage.get_task(task_id)
            print(f"Task to delete: {task}")
            confirmation = input("Are you sure? (yes/no): ").strip().lower()
            if confirmation == "yes":
                self.storage.delete_task(task_id)
                print(f"Task {task_id} deleted.")
            else:
                print("Delete cancelled.")
        except KeyError:
            print(f"Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def prompt_toggle_task_status(self) -> None:
        """Prompt user to toggle a task's completion status."""
        self.display_all_tasks()
        try:
            task_id = int(input("Enter task ID to toggle: "))
            task = self.storage.get_task(task_id)
            self.storage.toggle_task_status(task_id)
            updated_task = self.storage.get_task(task_id)
            status_text = "complete" if updated_task.is_complete else "incomplete"
            print(f"Task marked as {status_text}.")
        except KeyError:
            print(f"Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")
