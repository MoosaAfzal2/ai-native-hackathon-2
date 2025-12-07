"""Task data model."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Task:
    """A todo task with title, description, and completion status.

    Attributes:
        id: Unique sequential integer identifier (immutable)
        title: Task title (1-200 characters)
        description: Task description (optional, max 1000 characters)
        created_at: Creation timestamp (immutable)
        is_complete: Completion status (default False, mutable)
    """
    id: int
    title: str
    description: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    is_complete: bool = False

    def __post_init__(self):
        """Validate and process task data."""
        # Validate title
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        if len(self.title) > 200:
            raise ValueError(f"Title too long (max 200). Current: {len(self.title)} characters.")

        # Validate description
        if len(self.description) > 1000:
            raise ValueError(f"Description too long (max 1000). Current: {len(self.description)} characters.")

        # Trim whitespace from title and description
        object.__setattr__(self, 'title', self.title.strip())
        object.__setattr__(self, 'description', self.description.strip())

    def toggle_status(self) -> None:
        """Toggle task completion status between True and False."""
        object.__setattr__(self, 'is_complete', not self.is_complete)

    def mark_complete(self) -> None:
        """Mark task as complete."""
        object.__setattr__(self, 'is_complete', True)

    def mark_incomplete(self) -> None:
        """Mark task as incomplete."""
        object.__setattr__(self, 'is_complete', False)

    def __str__(self) -> str:
        """Return readable string representation of task."""
        status = "[OK]" if self.is_complete else "[ ]"
        return f"{self.id} | {self.title} | {status} | {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    def __repr__(self) -> str:
        """Return detailed representation for debugging."""
        return f"Task(id={self.id}, title={self.title!r}, description={self.description!r}, created_at={self.created_at}, is_complete={self.is_complete})"

