"""
Pytest configuration for integration tests

This file contains fixtures and configuration shared across integration tests.
"""

import os
import pytest
from pathlib import Path
from sendbird_platform_sdk.api_client import ApiClient
from sendbird_platform_sdk.configuration import Configuration


def load_env_file():
    """
    Load environment variables from .env file
    
    Looks for .env file in the project root and loads variables from it.
    """
    # Find project root (where .env file should be)
    current_dir = Path(__file__).resolve()
    project_root = current_dir.parent.parent.parent
    env_file = project_root / '.env'
    
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                # Parse KEY=VALUE format
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    # Remove quotes if present
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    # Set environment variable only if not already set
                    if key not in os.environ:
                        os.environ[key] = value


@pytest.fixture(scope="session")
def api_config():
    """
    Create API configuration from environment variables or .env file
    
    Required variables (from .env file or environment):
    - SENDBIRD_APP_ID: Your Sendbird application ID
    - SENDBIRD_API_TOKEN: Your Sendbird API token
    """
    # Load .env file if it exists
    load_env_file()
    
    app_id = os.environ.get('SENDBIRD_APP_ID')
    api_token = os.environ.get('SENDBIRD_API_TOKEN')
    
    if not app_id or not api_token:
        pytest.skip(
            "Integration tests require SENDBIRD_APP_ID and SENDBIRD_API_TOKEN. "
            "Create a .env file in the project root with these variables or set them as environment variables."
        )
    
    config = Configuration(
        host=f"https://api-{app_id}.sendbird.com"
    )
    
    return {
        'config': config,
        'api_token': api_token,
        'app_id': app_id
    }


@pytest.fixture(scope="session")
def api_client(api_config):
    """Create an API client for integration tests"""
    return ApiClient(configuration=api_config['config'])


@pytest.fixture
def test_user_id():
    """Generate a unique test user ID"""
    import uuid
    return f"test_user_{uuid.uuid4().hex[:8]}"


@pytest.fixture
def test_channel_url():
    """Generate a unique test channel URL"""
    import uuid
    return f"test_channel_{uuid.uuid4().hex[:8]}"

