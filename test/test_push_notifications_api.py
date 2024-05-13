"""
    Sendbird Platform SDK

    Sendbird Platform API SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@sendbird.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import sendbird_platform_sdk
from sendbird_platform_sdk.api.push_notifications_api import PushNotificationsApi  # noqa: E501


class TestPushNotificationsApi(unittest.TestCase):
    """PushNotificationsApi unit test stubs"""

    def setUp(self):
        self.api = PushNotificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v3_applications_push_settings_get(self):
        """Test case for v3_applications_push_settings_get

        Check push notifications  # noqa: E501
        """
        pass

    def test_v3_applications_push_settings_put(self):
        """Test case for v3_applications_push_settings_put

        Turn on push notifications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
