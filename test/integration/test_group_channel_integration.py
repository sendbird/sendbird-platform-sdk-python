"""
Integration tests for Group Channel API

These tests make real API calls to Sendbird servers.
"""

import pytest
import time
from sendbird_platform_sdk.api.group_channel_api import GroupChannelApi
from sendbird_platform_sdk.api.user_api import UserApi
from sendbird_platform_sdk.api.moderation_api import ModerationApi
from sendbird_platform_sdk.model.create_a_user_request import CreateAUserRequest
from sendbird_platform_sdk.model.create_a_group_channel_request import CreateAGroupChannelRequest
from sendbird_platform_sdk.model.update_a_group_channel_request import UpdateAGroupChannelRequest
from sendbird_platform_sdk.exceptions import ApiException


class TestGroupChannelApiIntegration:
    """Integration tests for Group Channel API"""
    
    @pytest.fixture(autouse=True)
    def setup(self, api_client, api_config):
        """Setup for each test"""
        self.api = GroupChannelApi(api_client=api_client)
        self.moderation_api = ModerationApi(api_client=api_client)
        self.user_api = UserApi(api_client=api_client)
        self.api_token = api_config['api_token']
        self.created_users = []
        self.created_channels = []
        
    def teardown_method(self, method):
        """Cleanup after each test"""
        # Delete created channels
        for channel_url in self.created_channels:
            try:
                self.api.delete_a_group_channel(
                    api_token=self.api_token,
                    channel_url=channel_url
                )
            except ApiException:
                pass
                
        # Delete created users
        for user_id in self.created_users:
            try:
                self.user_api.delete_a_user(
                    api_token=self.api_token,
                    user_id=user_id
                )
            except ApiException:
                pass
                
    def create_test_user(self, user_id, nickname):
        """Helper method to create a test user"""
        create_request = CreateAUserRequest(
            user_id=user_id,
            nickname=nickname,
            profile_url="https://example.com/profile.jpg"
        )
        
        response = self.user_api.create_a_user(
            api_token=self.api_token,
            create_a_user_request=create_request
        )
        
        self.created_users.append(user_id)
        return response
        
    def test_create_and_view_group_channel(self, test_user_id, test_channel_url):
        """Test creating and viewing a group channel"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        
        # Create group channel
        create_request = CreateAGroupChannelRequest(
            users=[user1, user2],
            name="Test Channel",
            channel_url=test_channel_url
        )
        
        create_response = self.api.create_a_group_channel(
            api_token=self.api_token,
            create_a_group_channel_request=create_request
        )
        
        assert create_response is not None
        assert create_response.channel_url == test_channel_url
        self.created_channels.append(test_channel_url)
        
        # View the created channel
        view_response = self.api.get_a_group_channel(
            api_token=self.api_token,
            channel_url=test_channel_url
        )
        
        assert view_response is not None
        assert view_response.channel_url == test_channel_url
        assert view_response.name == "Test Channel"
        
    def test_update_group_channel(self, test_user_id, test_channel_url):
        """Test updating a group channel"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        
        # Create group channel
        create_request = CreateAGroupChannelRequest(
            users=[user1, user2],
            name="Original Name",
            channel_url=test_channel_url
        )
        
        create_response = self.api.create_a_group_channel(
            api_token=self.api_token,
            create_a_group_channel_request=create_request
        )
        
        assert create_response is not None
        self.created_channels.append(test_channel_url)
        
        # Update the channel
        update_request = UpdateAGroupChannelRequest(
            name="Updated Name"
        )
        
        update_response = self.api.update_a_group_channel(
            api_token=self.api_token,
            channel_url=test_channel_url,
            update_a_group_channel_request=update_request
        )
        
        assert update_response is not None
        assert update_response.name == "Updated Name"
        
    def test_list_group_channels(self):
        """Test listing group channels"""
        response = self.api.list_channels(
            api_token=self.api_token,
            limit=10
        )
        
        assert response is not None
        assert hasattr(response, 'channels')
        
    def test_invite_members_to_channel(self, test_user_id, test_channel_url):
        """Test inviting members to a group channel"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        user3 = self.create_test_user(f"{test_user_id}_3", "User 3")
        
        # Create group channel with 2 users
        create_request = CreateAGroupChannelRequest(
            users=[user1, user2],
            name="Test Channel",
            channel_url=test_channel_url
        )
        
        create_response = self.api.create_a_group_channel(
            api_token=self.api_token,
            create_a_group_channel_request=create_request
        )
        
        assert create_response is not None
        self.created_channels.append(test_channel_url)
        
        # Invite third user
        from sendbird_platform_sdk.model.invite_as_members_request import InviteAsMembersRequest
        invite_request = InviteAsMembersRequest(
            user_ids=[user3.user_id]
        )
        
        invite_response = self.api.invite_as_members(
            api_token=self.api_token,
            channel_url=test_channel_url,
            invite_as_members_request=invite_request
        )
        
        assert invite_response is not None
        
    def test_freeze_and_unfreeze_channel(self, test_user_id, test_channel_url):
        """Test freezing and unfreezing a group channel"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        
        # Create group channel
        create_request = CreateAGroupChannelRequest(
            users=[user1, user2],
            name="Test Channel",
            channel_url=test_channel_url
        )
        
        create_response = self.api.create_a_group_channel(
            api_token=self.api_token,
            create_a_group_channel_request=create_request
        )
        
        assert create_response is not None
        self.created_channels.append(test_channel_url)
        
        # Freeze the channel
        from sendbird_platform_sdk.model.freeze_a_group_channel_request import FreezeAGroupChannelRequest
        freeze_request = FreezeAGroupChannelRequest(
            freeze=True
        )
        
        freeze_response = self.moderation_api.freeze_a_group_channel(
            api_token=self.api_token,
            channel_url=test_channel_url,
            freeze_a_group_channel_request=freeze_request
        )
        
        assert freeze_response is not None
        
        # Unfreeze the channel
        unfreeze_request = FreezeAGroupChannelRequest(
            freeze=False
        )
        
        unfreeze_response = self.moderation_api.freeze_a_group_channel(
            api_token=self.api_token,
            channel_url=test_channel_url,
            freeze_a_group_channel_request=unfreeze_request
        )
        
        assert unfreeze_response is not None

