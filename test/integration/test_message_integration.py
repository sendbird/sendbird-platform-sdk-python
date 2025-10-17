"""
Integration tests for Message API

These tests make real API calls to Sendbird servers.
"""

import pytest
import time
from sendbird_platform_sdk.api.message_api import MessageApi
from sendbird_platform_sdk.api.group_channel_api import GroupChannelApi
from sendbird_platform_sdk.api.user_api import UserApi
from sendbird_platform_sdk.model.create_a_user_request import CreateAUserRequest
from sendbird_platform_sdk.model.create_a_group_channel_request import CreateAGroupChannelRequest
from sendbird_platform_sdk.model.send_a_message_request import SendAMessageRequest
from sendbird_platform_sdk.exceptions import ApiException


class TestMessageApiIntegration:
    """Integration tests for Message API"""
    
    @pytest.fixture(autouse=True)
    def setup(self, api_client, api_config):
        """Setup for each test"""
        self.api = MessageApi(api_client=api_client)
        self.channel_api = GroupChannelApi(api_client=api_client)
        self.user_api = UserApi(api_client=api_client)
        self.api_token = api_config['api_token']
        self.created_users = []
        self.created_channels = []
        
    def teardown_method(self, method):
        """Cleanup after each test"""
        # Delete created channels
        for channel_url in self.created_channels:
            try:
                self.channel_api.delete_a_group_channel(
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
        
    def create_test_channel(self, channel_url, users):
        """Helper method to create a test channel"""
        create_request = CreateAGroupChannelRequest(
            users=users,
            name="Test Channel",
            channel_url=channel_url
        )
        
        response = self.channel_api.create_a_group_channel(
            api_token=self.api_token,
            create_a_group_channel_request=create_request
        )
        
        self.created_channels.append(channel_url)
        return response
        
    def test_send_and_view_message(self, test_user_id, test_channel_url):
        """Test sending and viewing a message"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        
        # Create channel
        channel = self.create_test_channel(
            test_channel_url,
            [user1, user2]
        )
        
        # Send a message
        send_request = SendAMessageRequest(
            message_type="MESG",
            user_id=user1.user_id,
            message="Hello, this is a test message!"
        )
        
        send_response = self.api.send_a_message(
            api_token=self.api_token,
            channel_type="group_channels",
            channel_url=test_channel_url,
            send_a_message_request=send_request
        )
        
        assert send_response is not None
        assert send_response.message == "Hello, this is a test message!"
        message_id = send_response.message_id
        
        # View the message
        view_response = self.api.get_a_message(
            api_token=self.api_token,
            channel_type="group_channels",
            channel_url=test_channel_url,
            message_id=message_id
        )
        
        assert view_response is not None
        assert view_response.message_id == message_id
        
    def test_list_messages(self, test_user_id, test_channel_url):
        """Test listing messages in a channel"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        
        # Create channel
        channel = self.create_test_channel(
            test_channel_url,
            [user1, user2]
        )
        
        # Send multiple messages
        for i in range(3):
            send_request = SendAMessageRequest(
                message_type="MESG",
                user_id=user1.user_id,
                message=f"Test message {i+1}"
            )
            
            self.api.send_a_message(
                api_token=self.api_token,
                channel_type="group_channels",
                channel_url=test_channel_url,
                send_a_message_request=send_request
            )
            
        # List messages
        list_response = self.api.list_messages(
            api_token=self.api_token,
            channel_type="group_channels",
            channel_url=test_channel_url,
            message_ts=0,
            message_id=0
        )
        
        assert list_response is not None
        assert hasattr(list_response, 'messages')
        assert len(list_response.messages) >= 3
        
    def test_update_message(self, test_user_id, test_channel_url):
        """Test updating a message"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        
        # Create channel
        channel = self.create_test_channel(
            test_channel_url,
            [user1, user2]
        )
        
        # Send a message
        send_request = SendAMessageRequest(
            message_type="MESG",
            user_id=user1.user_id,
            message="Original message"
        )
        
        send_response = self.api.send_a_message(
            api_token=self.api_token,
            channel_type="group_channels",
            channel_url=test_channel_url,
            send_a_message_request=send_request
        )
        
        message_id = send_response.message_id
        
        # Update the message
        from sendbird_platform_sdk.model.update_a_message_request import UpdateAMessageRequest
        update_request = UpdateAMessageRequest(
            message_type="MESG",
            message="Updated message"
        )
        
        update_response = self.api.update_a_message(
            api_token=self.api_token,
            channel_type="group_channels",
            channel_url=test_channel_url,
            message_id=message_id,
            update_a_message_request=update_request
        )
        
        assert update_response is not None
        assert update_response.message == "Updated message"
        
    def test_delete_message(self, test_user_id, test_channel_url):
        """Test deleting a message"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        
        # Create channel
        channel = self.create_test_channel(
            test_channel_url,
            [user1, user2]
        )
        
        # Send a message
        send_request = SendAMessageRequest(
            message_type="MESG",
            user_id=user1.user_id,
            message="Message to be deleted"
        )
        
        send_response = self.api.send_a_message(
            api_token=self.api_token,
            channel_type="group_channels",
            channel_url=test_channel_url,
            send_a_message_request=send_request
        )
        
        message_id = send_response.message_id
        
        # Delete the message
        delete_response = self.api.delete_a_message(
            api_token=self.api_token,
            channel_type="group_channels",
            channel_url=test_channel_url,
            message_id=message_id
        )
        
        assert delete_response is not None
        
    def test_send_admin_message(self, test_user_id, test_channel_url):
        """Test sending an admin message"""
        # Create test users
        user1 = self.create_test_user(test_user_id, "User 1")
        user2 = self.create_test_user(f"{test_user_id}_2", "User 2")
        
        # Create channel
        channel = self.create_test_channel(
            test_channel_url,
            [user1, user2]
        )
        
        # Send an admin message
        send_request = SendAMessageRequest(
            message_type="ADMM",
            user_id=user1.user_id,
            message="This is an admin message"
        )
        
        send_response = self.api.send_a_message(
            api_token=self.api_token,
            channel_type="group_channels",
            channel_url=test_channel_url,
            send_a_message_request=send_request
        )
        
        assert send_response is not None
        assert send_response.message == "This is an admin message"

