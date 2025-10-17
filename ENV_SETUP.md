# Environment Setup for Integration Tests

This guide explains how to configure credentials for integration tests.

## Quick Start

1. Create a `.env` file in the project root directory
2. Add your Sendbird credentials
3. Run integration tests

## Step-by-Step Setup

### 1. Create .env File

Create a file named `.env` in the project root directory (same directory as `README.md`):

```bash
# Navigate to project root
cd /path/to/sendbird-platform-sdk-python

# Create .env file
touch .env
```

### 2. Add Your Credentials

Edit the `.env` file and add your Sendbird credentials:

```bash
# Sendbird Platform SDK - Integration Test Configuration

# Your Sendbird Application ID
# Find this in Sendbird Dashboard > Settings > Application > App ID
SENDBIRD_APP_ID=your_app_id_here

# Your Sendbird API Token (Master API Token)
# Find this in Sendbird Dashboard > Settings > Application > API tokens
SENDBIRD_API_TOKEN=your_api_token_here
```

### 3. Get Your Credentials

To find your Sendbird credentials:

1. Log in to [Sendbird Dashboard](https://dashboard.sendbird.com/)
2. Select your application
3. Go to **Settings** > **Application**
4. **App ID**: Copy the Application ID
5. **API Token**: Go to **API tokens** tab and copy the Master API token

### 4. Verify Setup

Run a simple test to verify your setup:

```bash
# Test with a single integration test
python -m pytest test/integration/test_user_integration.py::TestUserApiIntegration::test_list_users -v
```

If configured correctly, the test will run (not skip).

## Alternative: Environment Variables

Instead of using a `.env` file, you can set environment variables directly:

```bash
# Set environment variables
export SENDBIRD_APP_ID=your_app_id_here
export SENDBIRD_API_TOKEN=your_api_token_here

# Run tests
python -m pytest test/integration/ -v
```

## Security Notes

⚠️ **Important Security Considerations:**

1. **Never commit `.env` file**: The `.env` file is automatically ignored by git
2. **Keep credentials secret**: Do not share your API token
3. **Use test applications**: Consider using a separate Sendbird application for testing
4. **Rotate tokens regularly**: Regenerate API tokens periodically
5. **Limit token permissions**: Use tokens with minimal required permissions if possible

## Troubleshooting

### Tests are being skipped

If you see "Integration tests require SENDBIRD_APP_ID and SENDBIRD_API_TOKEN", check:

1. `.env` file exists in the project root (not in `test/` directory)
2. Variable names are correct (case-sensitive)
3. Values don't have quotes or extra spaces
4. File is saved

### Invalid credentials

If tests run but fail with authentication errors:

1. Verify credentials in Sendbird Dashboard
2. Check for typos in `.env` file
3. Ensure API token has required permissions
4. Try regenerating the API token

### .env file not loading

1. Ensure file is named exactly `.env` (not `.env.txt` or similar)
2. File should be in project root directory
3. Check file permissions (should be readable)

## Example .env File

Here's a complete example:

```bash
# Sendbird Platform SDK - Integration Test Configuration
# Created: 2024-10-15

# Application ID from Sendbird Dashboard
SENDBIRD_APP_ID=A1B2C3D4-E5F6-7890-ABCD-EF1234567890

# Master API Token from Sendbird Dashboard  
SENDBIRD_API_TOKEN=1234567890abcdef1234567890abcdef1234567890
```

## Additional Resources

- [Sendbird Platform API Documentation](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api)
- [Sendbird Dashboard](https://dashboard.sendbird.com/)
- [Integration Test Guide](test/README.md)

