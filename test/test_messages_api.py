"""
    Sendbird Platform SDK

    Sendbird Platform API Javascript SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import sendbird_platform_sdk
from sendbird_platform_sdk.api.messages_api import MessagesApi  # noqa: E501


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        self.api = MessagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_extra_data_to_message(self):
        """Test case for add_extra_data_to_message

        Add extra data to a message  # noqa: E501
        """
        pass

    def test_add_reaction_to_a_message(self):
        """Test case for add_reaction_to_a_message

        Add a reaction to a message  # noqa: E501
        """
        pass

    def test_delete_message_by_id(self):
        """Test case for delete_message_by_id

        Delete a message  # noqa: E501
        """
        pass

    def test_gc_mark_all_messages_as_delivered(self):
        """Test case for gc_mark_all_messages_as_delivered

        Mark all messages as delivered  # noqa: E501
        """
        pass

    def test_gc_mark_all_messages_as_read(self):
        """Test case for gc_mark_all_messages_as_read

        Mark all messages as read  # noqa: E501
        """
        pass

    def test_gc_view_number_of_each_members_unread_messages(self):
        """Test case for gc_view_number_of_each_members_unread_messages

        View number of each member's unread messages  # noqa: E501
        """
        pass

    def test_list_messages(self):
        """Test case for list_messages

        List messages  # noqa: E501
        """
        pass

    def test_list_reactions_of_message(self):
        """Test case for list_reactions_of_message

        List reactions of a message  # noqa: E501
        """
        pass

    def test_remove_extra_data_from_message(self):
        """Test case for remove_extra_data_from_message

        Remove extra data from a message  # noqa: E501
        """
        pass

    def test_remove_reaction_from_a_message(self):
        """Test case for remove_reaction_from_a_message

        Remove a reaction from a message  # noqa: E501
        """
        pass

    def test_send_message(self):
        """Test case for send_message

        Send a message  # noqa: E501
        """
        pass

    def test_translate_message_into_other_languages(self):
        """Test case for translate_message_into_other_languages

        Translate a message into other languages  # noqa: E501
        """
        pass

    def test_update_extra_data_in_message(self):
        """Test case for update_extra_data_in_message

        Update extra data in a message  # noqa: E501
        """
        pass

    def test_update_message_by_id(self):
        """Test case for update_message_by_id

        Update a message  # noqa: E501
        """
        pass

    def test_view_message_by_id(self):
        """Test case for view_message_by_id

        View a message  # noqa: E501
        """
        pass

    def test_view_total_number_of_messages_in_channel(self):
        """Test case for view_total_number_of_messages_in_channel

        View total number of messages in a channel  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
