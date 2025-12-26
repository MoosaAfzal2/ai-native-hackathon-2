# Example: API Project (FastAPI, Standard Quality, src/ Layout)

**Configuration chosen:**
- Type: API/Microservice
- Folder structure: src/
- Python version: 3.12
- Quality level: Standard
- GitHub Actions: Yes (Full)
- Dependencies: Opinionated (FastAPI defaults)

## Generated Folder Structure

```
user-service/
├── src/
│   └── user_service/
│       ├── __init__.py
│       ├── main.py (FastAPI app entry point)
│       ├── config.py (Configuration management)
│       ├── models/
│       │   ├── __init__.py
│       │   └── user.py (Pydantic models)
│       ├── core/
│       │   ├── __init__.py
│       │   └── utils.py (Core business logic)
│       ├── agents/
│       │   └── __init__.py
│       ├── tools/
│       │   ├── __init__.py
│       │   └── validators.py
│       └── routes/
│           ├── __init__.py
│           └── users.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_routes.py
├── .github/workflows/
│   ├── lint.yml
│   └── test.yml
├── pyproject.toml
├── ruff.toml
├── mypy.ini
├── pytest.ini
├── README.md
└── .gitignore
```

## Key Files

### pyproject.toml
```toml
[project]
name = "user-service"
version = "0.1.0"
description = "A FastAPI microservice for user management"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115",
    "uvicorn>=0.30",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=5.0",
    "ruff>=0.6",
    "mypy>=1.12",
]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "RUF"]

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--cov=src/user_service --cov-fail-under=80"
```

### src/user_service/main.py
```python
from fastapi import FastAPI
from user_service.routes import users

app = FastAPI(title="User Service", version="0.1.0")

app.include_router(users.router)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
```

### src/user_service/models/user.py
```python
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """User creation model."""
    name: str
    email: EmailStr


class User(UserCreate):
    """User response model."""
    id: int

    class Config:
        from_attributes = True
```

### src/user_service/core/utils.py
```python
"""Core utility functions."""


def validate_email_domain(email: str, allowed_domains: list[str] | None = None) -> bool:
    """Validate email domain."""
    if not allowed_domains:
        return True
    domain = email.split("@")[1]
    return domain in allowed_domains
```

### src/user_service/routes/users.py
```python
from fastapi import APIRouter
from user_service.models.user import UserCreate, User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def list_users() -> dict:
    """List all users."""
    return {"users": []}


@router.post("/")
async def create_user(user: UserCreate) -> User:
    """Create a new user."""
    return User(id=1, **user.model_dump())
```

## Getting Started

```bash
cd user-service
uv sync                          # Install dependencies
uv run ruff check src/ tests/    # Lint
uv run mypy src/ tests/          # Type check
uv run pytest                    # Run tests (expect failures, you'll add tests)
uv run uvicorn user_service.main:app --reload   # Run server
```

Server available at: http://localhost:8000
API docs at: http://localhost:8000/docs
