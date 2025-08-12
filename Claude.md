# Python TDD Development Standards

## Testing Framework & Tools
- **Primary Testing**: pytest (NEVER unittest.TestCase)
- **Coverage**: pytest-cov with minimum 90% coverage target
- **Fixtures**: Use pytest fixtures in conftest.py files
- **Assertions**: Use pytest's enhanced assertions, avoid bare assert
- **Mocking**: Use pytest-mock (pytest fixture for unittest.mock)
- **Parametrization**: Use @pytest.mark.parametrize for multiple test cases

## Code Quality Stack
- **Linter & Formatter**: ruff (replaces black, flake8, isort)
- **Type Checker**: mypy in strict mode
- **Security**: bandit for security analysis
- **Pre-commit**: All quality checks must pass before commits

## Project Structure
```
src/
├── [project_name]/
│   ├── __init__.py
│   ├── models/
│   ├── services/
│   ├── api/
│   └── utils/
tests/
├── unit/                    # Fast, isolated unit tests
├── integration/             # Tests with external dependencies  
├── fixtures/                # Test data and factories
│   └── conftest.py         # Shared fixtures
└── conftest.py             # Root pytest configuration
pyproject.toml              # All tool configurations
```

## Essential Commands
```bash
# Code quality (run before every commit)
ruff check .                           # Lint code
ruff format .                         # Format code  
mypy src/                             # Type checking

# Testing workflows
pytest tests/unit/ -v                 # Unit tests only (fast)
pytest tests/integration/ -v          # Integration tests (slower)
pytest tests/ -v --cov=src --cov-report=html  # Full suite with coverage
pytest -x                            # Stop at first failure (TDD red phase)
pytest -k "test_specific_function"    # Run specific tests

# Complete quality gate (CI pipeline)
ruff check . && ruff format --check . && mypy src/ && pytest tests/ --cov=src --cov-fail-under=90
```

## Test Naming Conventions
- **Files**: `test_[module_name].py`
- **Classes**: `Test[ClassName]` (for grouping related behaviors)
- **Methods**: `test_[action]_[expected_result]_[when_condition]`

**Examples**:
- `test_user_creation_succeeds_when_valid_email_provided`
- `test_login_fails_when_password_incorrect`
- `test_api_returns_404_when_resource_not_found`
- `test_calculate_discount_returns_zero_when_no_items`

## Pytest Fixture Standards
- **Scope appropriately**: `session` > `module` > `class` > `function`
- **Descriptive names**: `admin_user`, `empty_database`, `mock_payment_service`
- **Factory pattern**: Use fixtures that return factory functions for multiple instances
- **Cleanup**: Use `yield` for setup/teardown, especially in integration tests
- **Location**: Shared fixtures in `conftest.py`, specific fixtures near their tests

## TDD Workflow (STRICT)
1. **🔴 RED PHASE**: 
   - Write failing tests first
   - Run `pytest -x` to confirm failure
   - Commit tests: `git commit -m "Add tests for [feature]"`

2. **🟢 GREEN PHASE**:
   - Write MINIMAL code to make tests pass
   - Run `pytest tests/unit/` frequently during development
   - NO refactoring until tests pass
   - Commit implementation: `git commit -m "Implement [feature]"`

3. **♻️ REFACTOR PHASE**:
   - Clean up code while keeping tests green
   - Run full test suite after each refactor
   - Commit refactors separately

## Code Standards
- **Type hints**: Required on all functions, methods, variables and tests
- **Line length**: 88 characters (ruff default)
- **Quotes**: Double quotes for strings
- **Imports**: Let ruff handle import sorting and formatting
- **Docstrings**: Use Google style for public APIs
- **No print()**: Use logging module or pytest -s for debug output

## Testing Best Practices

### ✅ DO:
- Test behavior, not implementation details
- Use arrange-act-assert pattern
- Mock external dependencies (databases, APIs, file systems)
- Write descriptive test names that explain the scenario
- Use parametrize for testing multiple inputs
- Keep tests focused and isolated
- Test edge cases and error conditions

### ❌ DON'T:
- Use unittest.TestCase (use plain functions or pytest classes)
- Test private methods directly
- Create dependencies between tests
- Use bare `assert` without descriptive messages
- Mock everything (test real collaborations when reasonable)
- Write tests that are longer than the code they test

## Unit vs Integration Test Guidelines

### Unit Tests (`tests/unit/`)
- Test single functions/classes in isolation
- Mock all external dependencies
- Fast execution (< 1ms per test typical)
- No database, filesystem, or network calls
- Focus on business logic and algorithms

### Integration Tests (`tests/integration/`)
- Test component interactions
- Use real databases (with transaction rollback)
- Test API endpoints end-to-end
- Verify external service integrations
- Test configuration loading and validation

## Mocking Strategy
- **Unit tests**: Mock at the boundary (database connections, HTTP clients)
- **Integration tests**: Use real services with proper cleanup
- **Use factories**: Create test data factories instead of hardcoded fixtures
- **Mock returns**: Mock return values, not internal behavior
- **Verify interactions**: Use `mock.assert_called_with()` when side effects matter

## Debugging Tests
- **Failing tests**: Run `pytest -vvv -s` for maximum verbosity
- **Specific test**: `pytest tests/unit/test_module.py::TestClass::test_method -s`
- **Drop into debugger**: Add `import pdb; pdb.set_trace()` in test
- **Coverage gaps**: `pytest --cov=src --cov-report=html` then open htmlcov/index.html

## Pre-commit Quality Gates
Before every commit, this command MUST pass:
```bash
ruff check . --fix && ruff format . && mypy src/ && pytest tests/unit/ -v
```

Before every push, this MUST pass:
```bash
pytest tests/ --cov=src --cov-fail-under=90
```

## Common Pytest Patterns

### Fixture Examples:
```python
@pytest.fixture
def user_data():
    return {"email": "test@example.com", "name": "Test User"}

@pytest.fixture  
def mock_database(mocker):
    return mocker.patch('myapp.database.get_connection')

@pytest.fixture(scope="session")
def test_database():
    # Setup test DB
    yield db_connection
    # Cleanup
```

### Parametrize Examples:
```python
@pytest.mark.parametrize("input,expected", [
    ("valid@email.com", True),
    ("invalid-email", False),
    ("", False),
])
def test_email_validation(input, expected):
    assert validate_email(input) == expected
```

## IMPORTANT TDD REMINDERS
- **RED FIRST**: Always write failing tests before any implementation code
- **MINIMAL CODE**: In green phase, write only enough code to pass the tests
- **ONE ASSERTION**: Generally one logical assertion per test method
- **FAST FEEDBACK**: Unit tests should run in milliseconds, not seconds
- **DESCRIPTIVE FAILURES**: Test names should make failures self-explanatory
- **NO SKIPPING**: Don't skip tests unless temporarily broken (use @pytest.mark.skip with reason)

## Integration with IDE
- Configure your IDE to run `ruff check` on save
- Set up pytest as the default test runner
- Enable mypy integration for real-time type checking
- Use pytest plugin for better test discovery and running
