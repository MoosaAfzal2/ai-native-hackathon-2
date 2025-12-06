---
description: "Atomic task breakdown for Phase I Console Todo Application implementation"
---

# Tasks: Phase I - In-Memory Console Todo Application

**Input**: Design documents from `/specs/1-phase-1-todo-app/`
**Prerequisites**: spec.md (user stories), plan.md (architecture & tech stack)
**TDD Approach**: Tests FIRST (Red) → Implementation (Green) → Refactor
**Framework**: pytest for all unit tests

**Organization**: Tasks organized by user story (US1-US5) to enable independent implementation and testing of each feature.

---

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, etc.)
- **Files**: Exact file paths specified for each task

---

## Phase 1: Project Setup

**Purpose**: Initialize project structure and dependencies

- [ ] T001 Initialize Python project with `uv init --package console-todo-app`
- [ ] T002 Add pytest as dev dependency: `uv add --dev pytest`
- [ ] T003 [P] Create directory structure: `src/console_todo_app/{models,storage,ui}` and `tests/`
- [ ] T004 [P] Create `src/console_todo_app/__init__.py` (package root)
- [ ] T005 [P] Create `tests/__init__.py`
- [ ] T006 [P] Create `src/console_todo_app/models/__init__.py`
- [ ] T007 [P] Create `src/console_todo_app/storage/__init__.py`
- [ ] T008 [P] Create `src/console_todo_app/ui/__init__.py`
- [ ] T009 Create `README.md` with project description and setup instructions
- [ ] T010 Create `pyproject.toml` with correct project metadata (if not auto-generated)
- [ ] T011 Verify pytest installation: `uv run pytest --version`
- [ ] T012 Create initial test placeholder in `tests/test_task.py` to verify test runner works

**Checkpoint**: Project structure ready, pytest working

---

## Phase 2: Foundational Layer - Task Model (TDD Cycle)

**Purpose**: Implement core Task data model with validation and status management
**Dependency**: Blocks all other user stories (needed by storage and UI)

### Tests for Task Model (RED Phase)

- [ ] T013 [P] Write failing tests in `tests/test_task.py` for:
  - Task creation with all attributes (id, title, description, created_at, is_complete)
  - Task instantiation sets is_complete to False by default
  - Task creation captures current datetime for created_at
  - Test task immutability (id and created_at cannot be modified)

- [ ] T014 [P] Write failing tests in `tests/test_task.py` for validation:
  - Title validation: rejects empty title
  - Title validation: rejects title > 200 characters
  - Title validation: accepts title 1-200 characters
  - Description validation: accepts empty description
  - Description validation: rejects description > 1000 characters
  - Description validation: accepts description 0-1000 characters
  - Tests for trimming whitespace from title and description

- [ ] T015 [P] Write failing tests in `tests/test_task.py` for status methods:
  - toggle_status() changes False to True
  - toggle_status() changes True to False
  - mark_complete() sets status to True
  - mark_incomplete() sets status to False
  - Multiple status changes work correctly

- [ ] T016 [P] Write failing tests in `tests/test_task.py` for string representation:
  - __str__ method returns readable task representation
  - __repr__ method for debugging

### Implementation for Task Model (GREEN Phase)

- [ ] T017 Implement Task class in `src/console_todo_app/models/task.py` with:
  - Attributes: id (int), title (str), description (str), created_at (datetime), is_complete (bool)
  - Type hints on all attributes
  - Docstring explaining class purpose

- [ ] T018 [P] Implement Task.__init__() method:
  - Accept parameters: id, title, description, created_at, is_complete
  - Store attributes with proper types
  - Set created_at if not provided: use datetime.now()
  - Initialize is_complete to False
  - Type hints on method signature and docstring

- [ ] T019 [P] Implement validation methods in Task:
  - validate_title(title: str) → raises ValueError if invalid
  - validate_description(description: str) → raises ValueError if invalid
  - Call validators in __init__

- [ ] T020 [P] Implement status management methods:
  - toggle_status() → flips is_complete boolean
  - mark_complete() → sets is_complete = True
  - mark_incomplete() → sets is_complete = False
  - All with type hints and docstrings

- [ ] T021 Implement string representation methods:
  - __str__() → returns readable format
  - __repr__() → returns detailed representation

### Quality & Refactor (REFACTOR Phase)

- [ ] T022 Add docstrings to Task class and all methods (PEP 257)
- [ ] T023 Ensure all type hints are present (mypy-compatible)
- [ ] T024 Run ruff formatter: `uv run ruff check src/console_todo_app/models/task.py`
- [ ] T025 Run all Task tests: `uv run pytest tests/test_task.py -v`
- [ ] T026 Verify test coverage for models: `uv run pytest tests/test_task.py --cov=src/console_todo_app/models`

**Checkpoint**: Task model complete, all tests passing, ready for storage layer

---

## Phase 3: Foundational Layer - Task Storage (TDD Cycle)

**Purpose**: Implement in-memory task storage with sequential ID generation and CRUD operations
**Dependency**: Depends on Task model (T001-T026), blocks all user story implementations

### Tests for Task Storage (RED Phase)

- [ ] T027 [P] Write failing tests in `tests/test_task_storage.py` for initialization:
  - TaskStorage initializes with empty task list
  - _next_id starts at 1
  - get_all_tasks() returns empty list initially

- [ ] T028 [P] Write failing tests in `tests/test_task_storage.py` for add_task:
  - add_task() creates task with sequential ID (1, 2, 3...)
  - add_task() returns created Task object
  - add_task() sets created_at to current datetime
  - add_task() sets is_complete to False
  - Multiple add_task() calls create unique IDs
  - add_task() validates title and description

- [ ] T029 [P] Write failing tests in `tests/test_task_storage.py` for get operations:
  - get_task(id) returns correct task
  - get_task(id) raises error for non-existent ID
  - get_all_tasks() returns all tasks in creation order
  - get_all_tasks() returns empty list when no tasks

- [ ] T030 [P] Write failing tests in `tests/test_task_storage.py` for update_task:
  - update_task(id, title, description) updates both fields
  - update_task() can update title only
  - update_task() can update description only
  - update_task() prevents modifying id
  - update_task() prevents modifying created_at
  - update_task() prevents modifying is_complete
  - update_task() validates new title and description
  - update_task() raises error for non-existent ID

- [ ] T031 [P] Write failing tests in `tests/test_task_storage.py` for delete_task:
  - delete_task(id) removes task from storage
  - delete_task(id) returns True on success
  - delete_task() raises error for non-existent ID
  - deleted task no longer in get_all_tasks()

- [ ] T032 [P] Write failing tests in `tests/test_task_storage.py` for mark_complete:
  - mark_complete(id) toggles status from False to True
  - mark_complete(id) toggles status from True to False
  - mark_complete() returns updated Task
  - mark_complete() raises error for non-existent ID

- [ ] T033 [P] Write failing tests in `tests/test_task_storage.py` for boundary conditions:
  - TaskStorage handles 100+ tasks without performance degradation
  - task_exists(id) correctly checks existence
  - ID uniqueness guaranteed across operations

### Implementation for Task Storage (GREEN Phase)

- [ ] T034 Implement TaskStorage class in `src/console_todo_app/storage/task_storage.py` with:
  - Private attributes: _tasks (dict[int, Task]), _next_id (int)
  - Docstring explaining class purpose and in-memory nature

- [ ] T035 [P] Implement TaskStorage.__init__():
  - Initialize _tasks as empty dict
  - Initialize _next_id to 1
  - Type hints and docstring

- [ ] T036 [P] Implement add_task() method:
  - Signature: add_task(title: str, description: str = "") → Task
  - Validate title and description using Task validators
  - Create Task with _next_id
  - Increment _next_id
  - Store in _tasks dict
  - Return created Task
  - Type hints and docstring

- [ ] T037 [P] Implement get_task() method:
  - Signature: get_task(task_id: int) → Task
  - Return task if exists
  - Raise TaskNotFoundError if not exists
  - Type hints and docstring

- [ ] T038 [P] Implement get_all_tasks() method:
  - Signature: get_all_tasks() → List[Task]
  - Return all tasks in creation order (dict insertion order preserved in Python 3.7+)
  - Return empty list if no tasks
  - Type hints and docstring

- [ ] T039 [P] Implement update_task() method:
  - Signature: update_task(task_id: int, title: str, description: str) → Task
  - Validate task exists
  - Validate new title and description
  - Update title and description only
  - Preserve id, created_at, is_complete
  - Return updated Task
  - Type hints and docstring

- [ ] T040 [P] Implement delete_task() method:
  - Signature: delete_task(task_id: int) → bool
  - Validate task exists
  - Remove from _tasks
  - Return True
  - Raise TaskNotFoundError if not exists
  - Type hints and docstring

- [ ] T041 [P] Implement mark_complete() method:
  - Signature: mark_complete(task_id: int) → Task
  - Validate task exists
  - Toggle is_complete using task.toggle_status()
  - Return updated Task
  - Type hints and docstring

- [ ] T042 [P] Implement task_exists() method:
  - Signature: task_exists(task_id: int) → bool
  - Return True if task exists, False otherwise
  - Type hints and docstring

- [ ] T043 Create custom exceptions in `src/console_todo_app/storage/task_storage.py`:
  - TaskNotFoundError(Exception)
  - ValidationError(Exception)

### Quality & Refactor (REFACTOR Phase)

- [ ] T044 Add docstrings to TaskStorage class and all methods (PEP 257)
- [ ] T045 Ensure all type hints present and correct
- [ ] T046 Run ruff formatter: `uv run ruff check src/console_todo_app/storage/`
- [ ] T047 Run all storage tests: `uv run pytest tests/test_task_storage.py -v`
- [ ] T048 Verify test coverage for storage: `uv run pytest tests/test_task_storage.py --cov=src/console_todo_app/storage`
- [ ] T049 Verify cross-layer functionality: Create 5 tasks, update 2, delete 1, verify state

**Checkpoint**: Task model and storage layer complete, all CRUD operations working, ready for UI

---

## Phase 4: User Story 1 - Add New Todo Task (Priority: P1)

**Goal**: Users can create new tasks with title and optional description, with validation and success confirmation

**Independent Test**: Create task with title, verify ID generation, verify in task list; create second task and verify unique ID

### Implementation for US1

- [ ] T050 [US1] Implement get_task_input() in `src/console_todo_app/ui/console_ui.py`:
  - Prompt user for task title (1-200 chars)
  - Prompt user for optional description (max 1000 chars)
  - Handle "back"/"menu" escape
  - Return (title, description) tuple
  - Type hints and docstring

- [ ] T051 [US1] Implement display_success() in `src/console_todo_app/ui/console_ui.py`:
  - Format: "✓ [Action] successful"
  - Take message string as parameter
  - Print to console
  - Type hints and docstring

- [ ] T052 [US1] Implement handle_add_task() in `src/console_todo_app/main.py`:
  - Call ui.get_task_input()
  - Call storage.add_task(title, description)
  - Call ui.display_success("Task added")
  - Handle validation errors from storage
  - Catch TaskValidationError and display error message
  - Return to main menu
  - Type hints and docstring

- [ ] T053 [US1] Implement main event loop integration for "Add Task":
  - Connect menu option 1 to handle_add_task()
  - Pass through user input correctly
  - Return to menu after operation

### Testing for US1

- [ ] T054 [US1] Manual test Add Task:
  - Start application, select "Add Task"
  - Enter title "Buy groceries", no description
  - Verify task created with ID 1
  - Verify "✓ Task added" message
  - Return to menu
  - Add another task, verify ID is 2
  - Verify unique IDs working

- [ ] T055 [US1] Manual test Add Task validation:
  - Try empty title → verify error message
  - Try title > 200 chars → verify error message
  - Try description > 1000 chars → verify error message
  - Verify unlimited retries with "back" escape working

**Checkpoint**: User Story 1 complete - users can create tasks with validation

---

## Phase 5: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can see all tasks in a readable table format with ID, title, status, and creation date

**Independent Test**: Create 3-5 tasks with mixed completion statuses, view list, verify all tasks display correctly in table format; test empty list handling

### Implementation for US2

- [ ] T056 [US2] Implement format_status_symbol() in `src/console_todo_app/ui/console_ui.py`:
  - Take is_complete (bool) parameter
  - Return "✓" if True, "○" if False
  - Type hints and docstring

- [ ] T057 [US2] Implement format_task_row() in `src/console_todo_app/ui/console_ui.py`:
  - Format single task as table row: "ID | Title | Status | Created"
  - Align columns properly (ID: 3 chars, Title: 20 chars, Status: 8 chars, Created: 16 chars)
  - Call format_status_symbol() for status
  - Format created_at as "YYYY-MM-DD HH:MM"
  - Type hints and docstring

- [ ] T058 [US2] Implement format_task_table() in `src/console_todo_app/ui/console_ui.py`:
  - Take list of Task objects
  - Return formatted table string with headers and rows
  - Include separator lines (dashes)
  - Handle empty list with message "No tasks yet"
  - Type hints and docstring

- [ ] T059 [US2] Implement display_tasks() in `src/console_todo_app/ui/console_ui.py`:
  - Take list of Task objects
  - Call format_task_table()
  - Print to console
  - Type hints and docstring

- [ ] T060 [US2] Implement handle_view_tasks() in `src/console_todo_app/main.py`:
  - Call storage.get_all_tasks()
  - Call ui.display_tasks(tasks)
  - Handle empty list gracefully (message already in format_task_table)
  - Return to main menu
  - Type hints and docstring

- [ ] T061 [US2] Implement main event loop integration for "View Tasks":
  - Connect menu option 2 to handle_view_tasks()
  - Return to menu after display

### Testing for US2

- [ ] T062 [US2] Manual test View Tasks empty:
  - Start fresh application
  - Select "View Tasks"
  - Verify "No tasks yet" message displays
  - Return to menu

- [ ] T063 [US2] Manual test View Tasks with data:
  - Add 3 tasks with different titles
  - Mark one as complete
  - Select "View Tasks"
  - Verify table format with headers
  - Verify all 3 tasks display
  - Verify status symbols (✓ and ○) display correctly
  - Verify timestamps are reasonable
  - Return to menu

- [ ] T064 [US2] Manual test View Tasks formatting:
  - Add task with long title (approaching 200 chars)
  - View Tasks
  - Verify table remains readable and aligned
  - Verify no text wrapping breaks formatting

**Checkpoint**: User Story 2 complete - users can view tasks in readable table format

---

## Phase 6: User Story 3 - Update Task Details (Priority: P1)

**Goal**: Users can modify task title and/or description while protecting ID and creation date

**Independent Test**: Create task, update title, update description, verify changes in list, verify ID and creation date unchanged

### Implementation for US3

- [ ] T065 [US3] Implement get_task_id() in `src/console_todo_app/ui/console_ui.py`:
  - Prompt user for task ID
  - Validate numeric input
  - Handle "back"/"menu" escape
  - Return int or None
  - Type hints and docstring

- [ ] T066 [US3] Implement get_update_input() in `src/console_todo_app/ui/console_ui.py`:
  - Prompt user to select: update title, update description, or both
  - Get new title and/or description based on selection
  - Handle "back"/"menu" escape
  - Return (new_title, new_description) tuple
  - Type hints and docstring

- [ ] T067 [US3] Implement display_error() in `src/console_todo_app/ui/console_ui.py`:
  - Format: "✗ Error: [message]"
  - Take error message as parameter
  - Print to console
  - Type hints and docstring

- [ ] T068 [US3] Implement handle_update_task() in `src/console_todo_app/main.py`:
  - Call ui.get_task_id()
  - Call storage.get_task() to verify existence (catch TaskNotFoundError)
  - Call ui.get_update_input()
  - Call storage.update_task(id, new_title, new_description)
  - Call ui.display_success("Task updated")
  - Handle all errors: non-existent ID, validation errors
  - Return to main menu
  - Type hints and docstring

- [ ] T069 [US3] Implement main event loop integration for "Update Task":
  - Connect menu option 3 to handle_update_task()
  - Return to menu after operation

### Testing for US3

- [ ] T070 [US3] Manual test Update Task - title only:
  - Add task "Buy groceries"
  - View tasks, note the title
  - Select "Update Task", enter ID 1
  - Choose to update title only
  - Enter new title "Buy groceries and cook dinner"
  - Verify success message
  - View tasks, verify title updated, ID and date unchanged

- [ ] T071 [US3] Manual test Update Task - description only:
  - Add task with no description
  - Select "Update Task", enter ID 1
  - Choose to update description only
  - Enter description "Need milk, eggs, bread"
  - Verify success message
  - Verify title unchanged

- [ ] T072 [US3] Manual test Update Task - both fields:
  - Create task with title and description
  - Update both fields
  - Verify both updated, ID and date unchanged

- [ ] T073 [US3] Manual test Update Task - error cases:
  - Try to update non-existent ID → verify error message
  - Try empty title → verify error message
  - Try title > 200 chars → verify error message
  - Verify "back" escape working at any prompt

**Checkpoint**: User Story 3 complete - users can update tasks safely

---

## Phase 7: User Story 4 - Delete Task (Priority: P2)

**Goal**: Users can remove tasks from the list permanently

**Independent Test**: Create task, delete it, verify it no longer appears in task list

### Implementation for US4

- [ ] T074 [US4] Implement get_confirmation() in `src/console_todo_app/ui/console_ui.py`:
  - Prompt user for confirmation (y/n)
  - Accept "y", "yes", "n", "no" (case-insensitive)
  - Handle "back"/"menu" escape
  - Return bool
  - Type hints and docstring

- [ ] T075 [US4] Implement handle_delete_task() in `src/console_todo_app/main.py`:
  - Call ui.get_task_id()
  - Call storage.get_task() to verify existence and show task to user
  - Call ui.get_confirmation("Delete this task?")
  - If confirmed: call storage.delete_task(id)
  - Call ui.display_success("Task deleted")
  - If not confirmed: return to menu without deleting
  - Handle all errors: non-existent ID
  - Return to main menu
  - Type hints and docstring

- [ ] T076 [US4] Implement main event loop integration for "Delete Task":
  - Connect menu option 4 to handle_delete_task()
  - Return to menu after operation

### Testing for US4

- [ ] T077 [US4] Manual test Delete Task - successful:
  - Add 3 tasks
  - View tasks, note IDs
  - Select "Delete Task", enter ID 2
  - Confirm deletion
  - Verify success message
  - View tasks, verify task 2 is gone, tasks 1 and 3 remain

- [ ] T078 [US4] Manual test Delete Task - cancel:
  - Add task
  - Select "Delete Task"
  - Enter ID, but answer "no" to confirmation
  - Verify task still exists in list

- [ ] T079 [US4] Manual test Delete Task - error cases:
  - Try to delete non-existent ID → verify error message
  - Verify "back" escape working at any prompt

**Checkpoint**: User Story 4 complete - users can delete tasks

---

## Phase 8: User Story 5 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status to track progress

**Independent Test**: Create task, mark complete, verify status symbol changes; mark incomplete again, verify status toggles back

### Implementation for US5

- [ ] T080 [US5] Implement handle_mark_complete() in `src/console_todo_app/main.py`:
  - Call ui.get_task_id()
  - Call storage.get_task() to verify existence and show current status
  - Call storage.mark_complete(id) to toggle status
  - Call ui.display_success("Task status updated")
  - Display new status (complete or incomplete)
  - Handle all errors: non-existent ID
  - Return to main menu
  - Type hints and docstring

- [ ] T081 [US5] Implement main event loop integration for "Mark Complete/Incomplete":
  - Connect menu option 5 to handle_mark_complete()
  - Return to menu after operation

### Testing for US5

- [ ] T082 [US5] Manual test Mark Complete - incomplete to complete:
  - Add task
  - View tasks, verify status is ○
  - Select "Mark Complete/Incomplete", enter ID
  - Verify success message shows "complete"
  - View tasks, verify status changed to ✓

- [ ] T083 [US5] Manual test Mark Complete - complete to incomplete:
  - With task from previous test, select "Mark Complete/Incomplete" again
  - Verify status toggles back to ○
  - View tasks to confirm

- [ ] T084 [US5] Manual test Mark Complete - error case:
  - Try to mark non-existent ID → verify error message

**Checkpoint**: User Story 5 complete - all 5 core features working

---

## Phase 9: Main Application Integration

**Purpose**: Wire everything together with event loop and graceful exit

### Implementation

- [ ] T085 Implement TodoApp class in `src/console_todo_app/main.py`:
  - Initialize TaskStorage and ConsoleUI
  - Docstring explaining role and responsibilities

- [ ] T086 Implement TodoApp.run() main event loop:
  - Loop continuously showing menu → getting choice → calling handler → repeating
  - Handle menu choice validation
  - Handle all operation handlers
  - Graceful exit when user selects "Exit"

- [ ] T087 Implement display_menu() in `src/console_todo_app/ui/console_ui.py`:
  - Display all 6 menu options (Add, View, Update, Delete, Mark, Exit)
  - Prompt user for choice
  - Validate choice (1-6 or action name)
  - Return choice as string or number
  - Handle "back"/"menu" escape
  - Type hints and docstring

- [ ] T088 Implement main entry point in `src/console_todo_app/main.py`:
  - Create if __name__ == "__main__": block
  - Instantiate TodoApp()
  - Call .run()

### Testing for Integration

- [ ] T089 Manual test full application flow:
  - Start application: `uv run python -m console_todo_app`
  - Add 3 tasks
  - View tasks - verify all display
  - Update one task
  - Mark one as complete
  - View tasks - verify status symbols
  - Delete one task
  - View tasks - verify it's gone
  - Add task, then select Exit
  - Verify graceful exit (no errors)

- [ ] T090 Manual test edge case interactions:
  - Add task, press "back" during title entry → return to menu
  - Add task successfully
  - Try to update non-existent task → error message → return to menu
  - Try to mark task with invalid ID → error message
  - Try invalid menu option → error message, menu redisplays
  - Verify all operations work sequentially without crashes

**Checkpoint**: Full application working end-to-end

---

## Phase 10: Testing, Quality Assurance & Documentation

**Purpose**: Comprehensive testing, code quality, documentation

### Testing & Coverage

- [ ] T091 Run full test suite: `uv run pytest tests/ -v`
- [ ] T092 Check test coverage: `uv run pytest tests/ --cov=src --cov-report=html`
- [ ] T093 Verify coverage ≥ 80% for:
  - src/console_todo_app/models/ (Task model)
  - src/console_todo_app/storage/ (TaskStorage)

### Code Quality

- [ ] T094 Run ruff check all source files: `uv run ruff check src/`
- [ ] T095 Run ruff format all source files: `uv run ruff format src/`
- [ ] T096 Verify all docstrings present:
  - All classes have module-level docstrings
  - All public methods have docstrings
  - Check: grep -r "def " src/ and verify docstring

- [ ] T097 Verify type hints complete:
  - All function parameters have type hints
  - All function returns have type hints
  - Run mypy if available (optional): `mypy src/`

### Documentation

- [ ] T098 Complete README.md with:
  - Project description (in-memory console todo app)
  - Setup instructions (uv init, uv add --dev pytest)
  - How to run application: `uv run python -m console_todo_app`
  - How to run tests: `uv run pytest tests/`
  - How to check coverage: `uv run pytest tests/ --cov=src`
  - Project structure overview
  - Features implemented (5 core features)

- [ ] T099 Ensure inline code comments where complex logic exists:
  - Add comments for non-obvious algorithm choices
  - Comment any regex or complex string operations
  - Keep comments minimal (code should be self-documenting)

### Final Verification

- [ ] T100 Run complete test suite one final time: `uv run pytest tests/ -v --tb=short`
- [ ] T101 Verify application works end-to-end:
  - Manual test all 5 features (Add, View, Update, Delete, Mark)
  - Test error scenarios
  - Test menu loop
  - Test graceful exit
  - Test with 5+ tasks in list

- [ ] T102 Create summary of implementation:
  - All 5 core features working
  - All tests passing
  - Code coverage ≥ 80% for business logic
  - PEP 8 compliant (ruff check clean)
  - All docstrings and type hints present
  - README complete
  - Application ready for Phase II

**Checkpoint**: Phase I complete, all quality gates passed

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: Start immediately - no dependencies
- **Phase 2 (Task Model)**: After Phase 1 - foundational for storage and UI
- **Phase 3 (Task Storage)**: After Phase 2 - blocks all user story implementations
- **Phases 4-8 (User Stories 1-5)**: Can start after Phases 1-3 complete
  - US1 (Add) and US2 (View) should complete first (P1 priority)
  - US3 (Update) depends on US1 and US2 to be testable
  - US4 (Delete) and US5 (Mark) can proceed in parallel after Phase 3
- **Phase 9 (Integration)**: After all user stories (Phases 4-8)
- **Phase 10 (QA)**: Final phase - after all implementation complete

### Within-Story Task Dependencies

**Phase 2 (Task Model)**:
1. Tests first (T013-T016)
2. Implementation (T017-T023)
3. Quality & refactor (T024-T026)

**Phase 3 (Task Storage)**:
1. All tests first (T027-T033)
2. All implementation (T034-T043)
3. Quality & refactor (T044-T049)

**Phases 4-8 (User Stories)**:
1. Implementation tasks
2. Manual testing tasks
3. Each story should be independently testable

### Parallel Opportunities

**Phase 1 (Setup)**: Tasks marked [P] can run in parallel (directory creation, init files)

**Phase 2 (Task Model)**:
- Test writing (T013-T016) can be done in parallel
- Implementation (T017-T023) must be sequential (depends on understanding test requirements)
- Quality tasks can be done in parallel after implementation

**Phase 3 (Task Storage)**:
- Test writing (T027-T033) can be done in parallel
- Implementation can be grouped: CRUD methods (T036-T042) have some parallelization potential if split carefully
- Quality tasks (T044-T049) can be done in parallel

**Phases 4-8 (User Stories)**:
- Each user story is independent and can be developed in parallel
- E.g., Developer A works on US1, Developer B works on US2 simultaneously
- However, all depend on Phases 2-3 being complete first

### Suggested Execution Path (Sequential - Single Developer)

1. T001-T012: Project setup (30 min)
2. T013-T026: Task model TDD (1-2 hours)
3. T027-T049: Task storage TDD (2-3 hours)
4. T050-T064: US1 & US2 (Add & View) (1-2 hours)
5. T065-T073: US3 (Update) (1 hour)
6. T074-T084: US4 & US5 (Delete & Mark) (1 hour)
7. T085-T090: Integration & main loop (1 hour)
8. T091-T102: Testing, QA, documentation (1-2 hours)
**Total**: ~8-12 hours for complete Phase I implementation

### Suggested Execution Path (Parallel - Two Developers)

**Developer 1**:
1. T001-T012: Setup (parallel with Dev 2)
2. T013-T026: Task model (parallel with Dev 2)
3. T027-T049: Task storage (parallel with Dev 2)
4. T050-T064: US1 & US2
5. T085-T090: Integration

**Developer 2** (starts after Phase 3):
1. T065-T084: US3, US4, US5 (in parallel)

Both developers:
1. T091-T102: Testing, QA, documentation together

---

## Implementation Strategy

### MVP First (Recommended)

1. Complete Phases 1-3 (Setup, Task Model, Storage): Foundation
2. Complete Phases 4-5 (US1 & US2: Add & View): Minimum viable product
3. **STOP and VALIDATE**: Manual test creating and viewing tasks
4. Add Phases 6-8 (US3-5: Update, Delete, Mark): Complete feature set
5. Phase 9 (Integration): Wire everything
6. Phase 10 (QA): Final polish

### Commit Strategy

Suggested commits after each phase checkpoint:
- After T026: "feat: Implement Task model with TDD (tests + implementation)"
- After T049: "feat: Implement TaskStorage with full CRUD operations"
- After T090: "feat: Implement all 5 core user stories with UI"
- After T102: "docs: Complete documentation and verify Phase I ready"

---

## Notes

- **[P] Tasks**: Can run in parallel if they modify different files and have no dependencies
- **[Story] Label**: Maps task to specific user story for traceability (US1, US2, US3, US4, US5)
- **TDD Approach**: Tests written and failing BEFORE implementation code
- **Red-Green-Refactor**: Each phase follows Write Tests → Implement → Refactor → Test Coverage
- **Each User Story**: Should be independently completable and testable
- **Quality Checkpoints**: After each phase, run tests and verify coverage
- **Graceful Degradation**: Each phase builds on previous without breaking earlier functionality
- **Manual Testing**: Required for UI components (cannot fully automate console interaction in simple tests)

