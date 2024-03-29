"""
    Sendbird Platform SDK

    Sendbird Platform API SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@sendbird.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import sendbird_platform_sdk
from sendbird_platform_sdk.model.send_bird_channel_response import SendBirdChannelResponse
from sendbird_platform_sdk.model.send_bird_message_response import SendBirdMessageResponse
from sendbird_platform_sdk.model.send_bird_user import SendBirdUser
globals()['SendBirdChannelResponse'] = SendBirdChannelResponse
globals()['SendBirdMessageResponse'] = SendBirdMessageResponse
globals()['SendBirdUser'] = SendBirdUser
from sendbird_platform_sdk.model.report_user_by_id_response import ReportUserByIdResponse


class TestReportUserByIdResponse(unittest.TestCase):
    """ReportUserByIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReportUserByIdResponse(self):
        """Test ReportUserByIdResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ReportUserByIdResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
