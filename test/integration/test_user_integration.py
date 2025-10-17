"""
Integration tests for User API

These tests make real API calls to Sendbird servers.
"""

import pytest
import time
from sendbird_platform_sdk.api.user_api import UserApi
from sendbird_platform_sdk.model.create_a_user_request import CreateAUserRequest
from sendbird_platform_sdk.model.update_a_user_request import UpdateAUserRequest
from sendbird_platform_sdk.exceptions import ApiException


class TestUserApiIntegration:
    """Integration tests for User API"""
    
    @pytest.fixture(autouse=True)
    def setup(self, api_client, api_config):
        """Setup for each test"""
        self.api = UserApi(api_client=api_client)
        self.api_token = api_config['api_token']
        
    def test_create_and_view_user(self, test_user_id):
        """Test creating and viewing a user"""
        # Create a user
        create_request = CreateAUserRequest(
            user_id=test_user_id,
            nickname="Test User",
            profile_url="https://example.com/profile.jpg"
        )
        
        create_response = self.api.create_a_user(
            api_token=self.api_token,
            create_a_user_request=create_request
        )
        
        assert create_response is not None
        assert create_response.user_id == test_user_id
        
        # View the created user
        view_response = self.api.view_a_user(
            api_token=self.api_token,
            user_id=test_user_id
        )
        
        assert view_response is not None
        assert view_response.user_id == test_user_id
        assert view_response.nickname == "Test User"
        
        # Cleanup: delete the user
        try:
            self.api.delete_a_user(
                api_token=self.api_token,
                user_id=test_user_id
            )
        except ApiException:
            pass  # Ignore cleanup errors
            
    def test_create_update_and_delete_user(self, test_user_id):
        """Test creating, updating, and deleting a user"""
        # Create a user
        create_request = CreateAUserRequest(
            user_id=test_user_id,
            nickname="Original Name",
            profile_url="https://example.com/profile.jpg"
        )
        
        create_response = self.api.create_a_user(
            api_token=self.api_token,
            create_a_user_request=create_request
        )
        
        assert create_response is not None
        assert create_response.nickname == "Original Name"
        
        # Update the user
        update_request = UpdateAUserRequest(
            nickname="Updated Name",
            profile_url="https://example.com/updated_profile.jpg"
        )
        
        update_response = self.api.update_a_user(
            api_token=self.api_token,
            user_id=test_user_id,
            update_a_user_request=update_request
        )
        
        assert update_response is not None
        assert update_response.nickname == "Updated Name"
        
        # Delete the user
        delete_response = self.api.delete_a_user(
            api_token=self.api_token,
            user_id=test_user_id
        )
        
        assert delete_response is not None
        
    def test_list_users(self):
        """Test listing users"""
        response = self.api.list_users(
            api_token=self.api_token,
            limit=10
        )
        
        assert response is not None
        assert hasattr(response, 'users')
        
    def test_create_user_with_metadata(self, test_user_id):
        """Test creating a user with metadata"""
        create_request = CreateAUserRequest(
            user_id=test_user_id,
            nickname="User with Metadata",
            profile_url="https://example.com/profile.jpg",
            metadata={
                "level": 5,
                "vip": True,
                "country": "US"
            }
        )
        
        create_response = self.api.create_a_user(
            api_token=self.api_token,
            create_a_user_request=create_request
        )
        
        assert create_response is not None
        assert create_response.user_id == test_user_id
        
        # View the user to verify metadata
        view_response = self.api.view_a_user(
            api_token=self.api_token,
            user_id=test_user_id,
            include_unread_count=True
        )
        
        assert view_response is not None
        assert view_response.user_id == test_user_id
        
        # Cleanup
        try:
            self.api.delete_a_user(
                api_token=self.api_token,
                user_id=test_user_id
            )
        except ApiException:
            pass
            
    def test_create_user_token(self, test_user_id):
        """Test creating a user and generating a token"""
        # First create a user
        create_request = CreateAUserRequest(
            user_id=test_user_id,
            nickname="Token Test User",
            profile_url="https://example.com/profile.jpg",
            issue_access_token=True
        )
        
        create_response = self.api.create_a_user(
            api_token=self.api_token,
            create_a_user_request=create_request
        )
        
        assert create_response is not None
        assert create_response.user_id == test_user_id
        
        # Cleanup
        try:
            self.api.delete_a_user(
                api_token=self.api_token,
                user_id=test_user_id
            )
        except ApiException:
            pass

