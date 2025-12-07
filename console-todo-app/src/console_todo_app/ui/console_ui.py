"""Console-based user interface for todo application."""

from console_todo_app.storage.task_storage import TaskStorage
from console_todo_app.models.task import Task
from console_todo_app.ui.rich_components import (
    RichTableBuilder,
    RichMessageFormatter,
    RichPromptHelper,
    get_console,
)
from console_todo_app.ui.theme import default_theme
from typing import Optional


class ConsoleUI:
    """Handles console interactions for the todo application."""

    def __init__(self, storage: TaskStorage, theme=None):
        """Initialize ConsoleUI with a TaskStorage instance.

        Args:
            storage: TaskStorage instance for managing tasks
            theme: Optional Theme instance for styling
        """
        self.storage = storage
        self.console = get_console()
        self.theme = theme or default_theme
        self.table_builder = RichTableBuilder(self.theme)
        self.message_formatter = RichMessageFormatter(self.theme)
        self.prompt_helper = RichPromptHelper(self.console, self.theme)

    def prompt_add_task(self) -> Task:
        """Prompt user to add a new task.

        Returns:
            Created Task object

        Raises:
            ValueError: If validation fails
        """
        while True:
            try:
                title = self.prompt_helper.prompt_text("Enter task title: ", max_length=200)
                if not title:
                    self.console.print(self.message_formatter.error("Title cannot be empty"))
                    continue
                description = self.prompt_helper.prompt_text("Enter task description (optional): ")
                task = self.storage.add_task(title, description)
                self.console.print(self.message_formatter.success(f"Task created: {task}"))
                return task
            except ValueError as e:
                self.console.print(self.message_formatter.error(str(e)))
                raise

    def display_all_tasks(self) -> None:
        """Display all tasks in formatted output."""
        tasks = self.storage.get_all_tasks()
        if not tasks:
            self.console.print(self.table_builder.build_empty_state_table())
            return

        table = self.table_builder.build_task_table(tasks)
        self.console.print(table)

    def prompt_update_task(self) -> None:
        """Prompt user to update a task."""
        self.display_all_tasks()
        try:
            task_id = self.prompt_helper.prompt_integer("Enter task ID to update: ")
            task = self.storage.get_task(task_id)
            self.console.print(f"Current task: {task}")

            new_title = self.prompt_helper.prompt_text(
                "Enter new title (leave blank to keep current): ",
                max_length=200
            )
            new_title = new_title if new_title else None

            new_description = self.prompt_helper.prompt_text(
                "Enter new description (leave blank to keep current): "
            )
            new_description = new_description if new_description else None

            updated_task = self.storage.update_task(task_id, title=new_title, description=new_description)
            self.console.print(self.message_formatter.success(f"Task updated: {updated_task}"))
        except KeyError:
            self.console.print(self.message_formatter.error(f"Task with ID {task_id} not found."))
        except ValueError as e:
            self.console.print(self.message_formatter.error(str(e)))

    def prompt_delete_task(self) -> None:
        """Prompt user to delete a task."""
        self.display_all_tasks()
        try:
            task_id = self.prompt_helper.prompt_integer("Enter task ID to delete: ")
            task = self.storage.get_task(task_id)
            self.console.print(f"Task to delete: {task}")
            confirmation = self.prompt_helper.prompt_confirmation("Are you sure?")
            if confirmation:
                self.storage.delete_task(task_id)
                self.console.print(self.message_formatter.success(f"Task {task_id} deleted."))
            else:
                self.console.print(self.message_formatter.info("Delete cancelled."))
        except KeyError:
            self.console.print(self.message_formatter.error(f"Task with ID {task_id} not found."))
        except ValueError as e:
            self.console.print(self.message_formatter.error(str(e)))

    def prompt_toggle_task_status(self) -> None:
        """Prompt user to toggle a task's completion status."""
        self.display_all_tasks()
        try:
            task_id = self.prompt_helper.prompt_integer("Enter task ID to toggle: ")
            task = self.storage.get_task(task_id)
            self.storage.toggle_task_status(task_id)
            updated_task = self.storage.get_task(task_id)
            status_text = "complete" if updated_task.is_complete else "incomplete"
            self.console.print(self.message_formatter.success(f"Task marked as {status_text}."))
        except KeyError:
            self.console.print(self.message_formatter.error(f"Task with ID {task_id} not found."))
        except ValueError as e:
            self.console.print(self.message_formatter.error(str(e)))

