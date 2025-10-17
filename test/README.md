# Sendbird Platform SDK Python - Testing Guide

This document explains the test structure and execution methods for the Sendbird Platform SDK Python.

## Test Structure

Tests are organized into two types:

### 1. Unit Tests

Unit tests independently test individual components of the SDK. They run quickly without actual API calls by using mocks.

**Location**: `/test/test_*.py`

**Test Coverage**:
- Model classes (creation, attribute validation, serialization/deserialization)
- API classes (method calls using mocks)

**Example**:
```python
# Model test
def testCreateAUserRequest(self):
    model = CreateAUserRequest(
        user_id="user123",
        nickname="John Doe",
        profile_url="https://example.com/profile.jpg"
    )
    self.assertEqual(model.user_id, "user123")

# API test (using mock)
@patch.object(ApiClient, 'call_api')
def test_create_a_user(self, mock_call_api):
    mock_response = MagicMock()
    mock_response.data = {...}
    mock_call_api.return_value = mock_response
    
    response = self.api.create_a_user(...)
    mock_call_api.assert_called_once()
```

### 2. Integration Tests

Integration tests verify the complete flow against actual Sendbird API. Real API credentials are required.

**Location**: `/test/integration/test_*_integration.py`

**Test Coverage**:
- User API (create, view, update, delete users)
- Group Channel API (create, manage channels, invite members)
- Message API (send, view, update, delete messages)

## Running Tests

### Running Unit Tests

```bash
# Run all unit tests
python -m pytest test/ --ignore=test/integration/

# Run specific test file
python -m pytest test/test_user_api.py

# Run specific test case
python -m pytest test/test_user_api.py::TestUserApi::test_create_a_user

# With coverage
python -m pytest test/ --ignore=test/integration/ --cov=sendbird_platform_sdk --cov-report=html
```

### Running Integration Tests

Integration tests can be configured using a `.env` file or environment variables.

#### Option 1: Using .env File (Recommended)

Create a `.env` file in the project root:

```bash
# .env
SENDBIRD_APP_ID=your_app_id
SENDBIRD_API_TOKEN=your_api_token
```

Then run integration tests:

```bash
# Run integration tests (automatically loads .env)
python -m pytest test/integration/

# Run specific integration test
python -m pytest test/integration/test_user_integration.py

# Verbose output
python -m pytest test/integration/ -v
```

#### Option 2: Using Environment Variables

Alternatively, set environment variables directly:

```bash
# Set environment variables
export SENDBIRD_APP_ID=your_app_id
export SENDBIRD_API_TOKEN=your_api_token

# Run integration tests
python -m pytest test/integration/ -v
```

#### .env File Template

Create a `.env` file in the project root with the following content:

```bash
# Sendbird Platform SDK - Integration Test Configuration
# Your Sendbird Application ID
SENDBIRD_APP_ID=your_app_id_here

# Your Sendbird API Token (Master API Token)
SENDBIRD_API_TOKEN=your_api_token_here
```

**Important**: 
- Integration tests make actual API calls
- Valid Sendbird credentials are required
- Real data will be created/deleted during test execution
- API usage will be counted towards your quota
- Never commit `.env` file to version control (it's gitignored by default)

## Installing Test Dependencies

```bash
# Install test dependencies
pip install -r test-requirements.txt
```

Required packages:
- `pytest>=6.2.5` - Test framework
- `pytest-cov>=2.8.1` - Code coverage
- `pytest-mock>=3.6.1` - Mock helpers
- `responses>=0.13.3` - HTTP request mocking

## Known Test Failures

Some tests intentionally fail to document SDK bugs and limitations. These failing tests serve as:
- Documentation of expected vs actual behavior
- Regression detection when bugs are fixed
- Clear specifications for future improvements

**Current failing tests**: ~7 tests related to optional fields rejecting None values

See [KNOWN_ISSUES.md](../KNOWN_ISSUES.md) for detailed information about these issues and workarounds.

## Adding New Tests

### Adding Unit Tests

1. Create a `test_*.py` file with the same name as the module to test
2. Create a class inheriting from `unittest.TestCase`
3. Write test cases as `test_*` methods
4. Use mocks to isolate external dependencies

Example:
```python
import unittest
from unittest.mock import Mock, patch
from sendbird_platform_sdk.api.user_api import UserApi

class TestUserApi(unittest.TestCase):
    def setUp(self):
        self.api = UserApi()
    
    @patch.object(ApiClient, 'call_api')
    def test_new_feature(self, mock_call_api):
        # Test implementation
        pass
```

### Adding Integration Tests

1. Create a `test_*_integration.py` file in `/test/integration/`
2. Use fixtures from `conftest.py`
3. Write tests with actual API calls
4. Clean up created resources in `teardown_method`

Example:
```python
import pytest
from sendbird_platform_sdk.api.user_api import UserApi

class TestUserApiIntegration:
    @pytest.fixture(autouse=True)
    def setup(self, api_client, api_config):
        self.api = UserApi(api_client=api_client)
        self.api_token = api_config['api_token']
        
    def test_new_feature(self, test_user_id):
        # Test with actual API calls
        pass
```

## Troubleshooting

### Unit Test Failures

1. Check mock configuration
2. Verify import paths
3. Ensure test isolation (each test should be independent)

### Integration Test Failures

1. Verify environment variables are set correctly
2. Check API credentials are valid
3. Verify network connection
4. Check API rate limits
5. Ensure resources from previous tests were cleaned up properly

## Best Practices

1. **Unit Tests First**: Cover as much as possible with unit tests; use integration tests only for end-to-end flow verification
2. **Test Isolation**: Each test should be runnable independently
3. **Resource Cleanup**: Integration tests must clean up all created resources
4. **Clear Names**: Test method names should clearly describe what is being tested
5. **Proper Assertions**: Clearly validate test results
6. **Documentation**: Add comments for complex tests

## References

- [Pytest Official Documentation](https://docs.pytest.org/)
- [unittest.mock Guide](https://docs.python.org/3/library/unittest.mock.html)
- [Sendbird Platform API Documentation](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api)
