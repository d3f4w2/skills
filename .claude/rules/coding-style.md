# Python Coding Style

This project follows PEP 8 conventions with additional strict guidelines.

## Core Principles

1. **Immutability**: Use frozen dataclasses, NamedTuple, or similar immutable patterns
2. **Type Safety**: All functions must have type hints
3. **Error Handling**: Explicit error handling with context using `fmt.Errorf` pattern
4. **Modular Design**: Use many small files, avoid single large files

## Modular Design (CRITICAL)

- **Many small files > Few large files**
- Keep files under 800 lines (200-400 lines typical)
- Extract utilities from large modules
- Organize by feature/domain, not by type
- High cohesion, low coupling

Examples:
- Prefer `models/user.py`, `models/post.py` over `models.py`
- Prefer `services/auth/login.py`, `services/auth/register.py` over `services/auth.py`
- Extract shared utilities to `utils/helpers.py`, `utils/validators.py`

## Formatting

- **ruff**: Primary formatter (replaces flake8, isort, black)
- Run `ruff check .` and `ruff format .`
- Line length: 88 characters

## Type Hints

All functions must have complete type annotations:

```python
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

def process_data(
    input_data: List[Dict[str, Any]],
    config: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Process input data with optional configuration."""
    ...
```

## Immutability

Use frozen dataclasses for immutable data structures:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Experience:
    skill_name: str
    success: bool
    metrics: PerformanceMetrics
    timestamp: datetime.datetime
```

## Error Handling

Never silently swallow errors. Always wrap with context:

```python
try:
    result = risky_operation()
data except ValueError as e:
    raise ValueError(f"Failed to process data: {e}") from e
except Exception as e:
    raise RuntimeError(f"Unexpected error: {e}") from e
```

## Validation

Validate at system boundaries (user input, external APIs):

```python
from pydantic import BaseModel, validator

class CreateSkillRequest(BaseModel):
    name: str
    description: str

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('name cannot be empty')
        return v.strip()
```
