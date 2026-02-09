# Testing Requirements

## Framework

- **pytest**: Primary testing framework
- **pytest-cov**: Coverage reporting (minimum 80% coverage)
- **pytest-asyncio**: Async test support

## Test Organization

Use table-driven tests for parameterized testing:

```python
import pytest

@pytest.mark.unit
class TestExperienceStore:
    @pytest.mark.parametrize("skill_name,expected_count", [
        ("test-skill", 1),
        ("nonexistent", 0),
    ])
    def test_get_experiences_by_skill(
        self,
        store: SQLiteExperienceStore,
        skill_name: str,
        expected_count: int,
    ) -> None:
        result = store.get_experiences_by_skill(skill_name)
        assert len(result) == expected_count
```

## Coverage Requirements

- **Minimum coverage**: 80%
- Run `pytest --cov=meta_skills --cov-report=term-missing`
- Failing tests block completion

## Test Categories

- **Unit tests**: Test individual functions/classes (mark with `@pytest.mark.unit`)
- **Integration tests**: Test component integration (mark with `@pytest.mark.integration`)
- **E2E tests**: Test complete flows (mark with `@pytest.mark.e2e`)

## Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=meta-skills --cov-report=term-missing

# Specific test file
pytest tests/test_experience_store.py

# Specific category
pytest -m unit
pytest -m integration

# Parallel execution
pytest -n auto
```
