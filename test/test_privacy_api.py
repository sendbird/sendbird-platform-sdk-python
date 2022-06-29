"""
    Sendbird Platform SDK

    Sendbird Platform API Javascript SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import sendbird_platform_sdk
from sendbird_platform_sdk.api.privacy_api import PrivacyApi  # noqa: E501


class TestPrivacyApi(unittest.TestCase):
    """PrivacyApi unit test stubs"""

    def setUp(self):
        self.api = PrivacyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_the_registration_of_gdpr_request_by_id(self):
        """Test case for cancel_the_registration_of_gdpr_request_by_id

        Cancel the registration of a GDPR request  # noqa: E501
        """
        pass

    def test_list_gdpr_requests(self):
        """Test case for list_gdpr_requests

        List GDPR requests  # noqa: E501
        """
        pass

    def test_register_gdpr_request(self):
        """Test case for register_gdpr_request

        Register a GDPR request  # noqa: E501
        """
        pass

    def test_view_gdpr_request_by_id(self):
        """Test case for view_gdpr_request_by_id

        View a GDPR request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
