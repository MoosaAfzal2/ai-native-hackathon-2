"""Main application entry point for the Console Todo App."""

from console_todo_app.storage.task_storage import TaskStorage
from console_todo_app.ui.console_ui import ConsoleUI
from console_todo_app.ui.rich_components import RichMenuBuilder, get_console


class TodoApp:
    """Main application class that orchestrates the todo app."""

    def __init__(self):
        """Initialize TodoApp with storage and UI."""
        self.storage = TaskStorage()
        self.ui = ConsoleUI(self.storage)
        self.menu_builder = RichMenuBuilder()
        self.console = get_console()

    def display_menu(self) -> None:
        """Display the main menu options."""
        menu_panels = self.menu_builder.build_menu()
        for panel in menu_panels:
            self.console.print(panel)

    def run_event_loop(self) -> None:
        """Run the main event loop."""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                try:
                    self.ui.prompt_add_task()
                except ValueError:
                    # Error already printed by UI
                    pass
            elif choice == "2":
                self.ui.display_all_tasks()
            elif choice == "3":
                self.ui.prompt_update_task()
            elif choice == "4":
                self.ui.prompt_delete_task()
            elif choice == "5":
                self.ui.prompt_toggle_task_status()
            elif choice == "6":
                self.console.print("\nThank you for using Console Todo App. Goodbye!")
                break
            else:
                self.console.print("[red]Invalid choice. Please enter a number between 1 and 6.[/]")

    def run(self) -> None:
        """Start the application."""
        self.console.print("\n[blue]Welcome to Console Todo App![/]")
        self.run_event_loop()


def main():
    """Entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()

