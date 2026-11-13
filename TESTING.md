"""
Backend FastAPI Tests Documentation

This directory contains comprehensive tests for the Mergington High School API.
Tests are structured using the AAA (Arrange-Act-Assert) pattern for clarity and maintainability.

## Test Structure

### tests/conftest.py
Pytest configuration file that provides shared fixtures used across all test files.

**Fixtures:**
- `client`: TestClient for making HTTP requests with isolated activity state per test
- `sample_activity`: Sample activity data for testing

### tests/test_app.py
Tests for the root endpoint (GET /).

**Test Cases:**
- test_root_redirects_to_static_index: Verifies redirect to /static/index.html
- test_root_redirect_status_code: Validates HTTP 307 status code

### tests/test_activities.py
Tests for the activities endpoint (GET /activities).

**Test Cases:**
- test_get_activities_returns_all_activities: Verifies all 9 activities are returned
- test_get_activities_returns_valid_json: Validates JSON response format
- test_activity_contains_required_fields: Checks for required fields in each activity
- test_activity_fields_have_correct_types: Validates data types of activity fields
- test_get_activities_success_status_code: Verifies HTTP 200 status
- test_chess_club_has_initial_participants: Validates initial participant data

### tests/test_signup.py
Tests for the signup endpoint (POST /activities/{activity_name}/signup).

**Test Cases:**
- test_successful_signup_for_valid_activity: Verifies successful signup workflow
- test_signup_returns_confirmation_message: Validates response message format
- test_signup_for_nonexistent_activity_returns_404: Tests error handling for invalid activity
- test_signup_adds_participant_to_activity: Verifies participant is added to activity
- test_multiple_signups_increase_participant_count: Tests multiple signups
- test_signup_response_status_is_success: Validates HTTP 200 status
- test_signup_error_response_format: Tests error response format

## Running Tests

### Run all tests
```bash
pytest tests/
```

### Run with verbose output
```bash
pytest tests/ -v
```

### Run specific test file
```bash
pytest tests/test_app.py -v
```

### Run specific test class
```bash
pytest tests/test_signup.py::TestSignupEndpoint -v
```

### Run specific test case
```bash
pytest tests/test_signup.py::TestSignupEndpoint::test_successful_signup_for_valid_activity -v
```

### Run with coverage report
```bash
pytest tests/ --cov=src --cov-report=term-missing
```

### Run with HTML coverage report
```bash
pytest tests/ --cov=src --cov-report=html
# Open htmlcov/index.html in a browser
```

## AAA (Arrange-Act-Assert) Pattern

All tests follow the AAA pattern for maximum clarity:

1. **Arrange**: Set up test data and preconditions
2. **Act**: Execute the code being tested
3. **Assert**: Verify the results

Example:
```python
def test_successful_signup_for_valid_activity(self, client, sample_activity):
    # Arrange
    activity_name = sample_activity["name"]
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
```

## Test Coverage

The existing suite covers:
- ✅ GET / - Root endpoint redirect
- ✅ GET /activities - All activities retrieval
- ✅ POST /activities/{activity_name}/signup - Student signup

The unregistration endpoint and duplicate-signup validation are not yet covered.

## Dependencies

Tests require the following packages (see requirements.txt):
- `pytest`: Test framework
- `pytest-cov`: Coverage reporting plugin
- `fastapi`: Web framework (app under test)
- `httpx`: HTTP client (used by TestClient)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Test Best Practices

1. **Clear naming**: Test names clearly describe what is being tested
2. **Single responsibility**: Each test verifies one specific behavior
3. **No side effects**: The client fixture isolates the in-memory activity state for each test
4. **Descriptive docstrings**: Each test includes a docstring explaining the test
5. **Fixtures over setup**: Use pytest fixtures for test data and client initialization
6. **AAA pattern**: All tests follow Arrange-Act-Assert structure

## Continuous Integration

These tests can be run in CI/CD pipelines. Example GitHub Actions command:
```bash
pytest tests/ --cov=src --cov-report=xml
```

## Future Enhancements

- Add tests for edge cases (e.g., max participant capacity)
- Add parametrized tests for testing multiple activities
- Add integration tests with real database
- Add performance tests
- Add test fixtures for database state management
"""
