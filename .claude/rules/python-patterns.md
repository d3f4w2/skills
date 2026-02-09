# Python Patterns

This file extends the common patterns with project-specific idioms.

## Data Validation with Pydantic

Use Pydantic for all data validation:

```python
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class Experience(BaseModel):
    skill_name: str = Field(..., min_length=1)
    success: bool
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: dict[str, Any] | None = None

    @field_validator('skill_name')
    @classmethod
    def validate_skill_name(cls, v: str) -> str:
        if not v.isalnum() and '-' not in v:
            raise ValueError('skill_name must be alphanumeric or contain hyphens')
        return v.lower()
```

## Repository Pattern

Encapsulate data access behind a consistent interface:

```python
from abc import ABC, abstractmethod

class ExperienceRepository(ABC):
    @abstractmethod
    def add(self, experience: Experience) -> Experience:
        ...

    @abstractmethod
    def get_by_id(self, experience_id: str) -> Experience | None:
        ...

    @abstractmethod
    def find_by_skill(self, skill_name: str) -> list[Experience]:
        ...

class SQLiteExperienceRepository(ExperienceRepository):
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

    def add(self, experience: Experience) -> Experience:
        # SQLite implementation
        ...
```

## Context Managers

Use context managers for resource management:

```python
from contextlib import contextmanager

@contextmanager
def database_connection(db_path: str):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()
```

## Dependency Injection

Use constructor functions to inject dependencies:

```python
def new_experience_store(
    repository: ExperienceRepository,
    logger: Logger,
) -> ExperienceStore:
    return Experience
Store(repository=repository, logger=logger)
```

## Configuration Pattern

Use python-dotenv for configuration:

```python
from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass(frozen=True)
class Config:
    database_path: str
    log_level: str
    max_context_tokens: int

    @classmethod
    def from_env(cls) -> 'Config':
        load_dotenv()
        return cls(
            database_path=os.getenv('DB_PATH', 'experience.db'),
            log_level=os.getenv('LOG_LEVEL', 'INFO'),
            max_context_tokens=int(os.getenv('MAX_TOKENS', '200000')),
        )
```

## Python 3.10+ Type Hints

Use modern type hint syntax:

```python
# Use | instead of Optional for union types
def process(value: int | None) -> str:
    ...

# Use dict and list instead of Dict, List
def get_items() -> list[dict[str, Any]]:
    ...

# Use match statement
match status:
    case "success":
        ...
    case "error" | "failed":
        ...
    case _:
        ...
```
