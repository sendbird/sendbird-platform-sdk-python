"""
    Sendbird Platform SDK

    Sendbird Platform API SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@sendbird.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import sendbird_platform_sdk
from sendbird_platform_sdk.api.announcement_api import AnnouncementApi  # noqa: E501


class TestAnnouncementApi(unittest.TestCase):
    """AnnouncementApi unit test stubs"""

    def setUp(self):
        self.api = AnnouncementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_detailed_open_rate_of_announcement_group(self):
        """Test case for get_detailed_open_rate_of_announcement_group

        Get detailed open rate of an announcement group  # noqa: E501
        """
        pass

    def test_get_statistics(self):
        """Test case for get_statistics

        Get statistics - weekly  # noqa: E501
        """
        pass

    def test_get_statistics_daily(self):
        """Test case for get_statistics_daily

        Get statistics - daily  # noqa: E501
        """
        pass

    def test_get_statistics_monthly(self):
        """Test case for get_statistics_monthly

        Get statistics - monthly  # noqa: E501
        """
        pass

    def test_list_announcement_groups(self):
        """Test case for list_announcement_groups

        List announcement groups  # noqa: E501
        """
        pass

    def test_schedule_announcement(self):
        """Test case for schedule_announcement

        Schedule an announcement  # noqa: E501
        """
        pass

    def test_update_announcement_by_id(self):
        """Test case for update_announcement_by_id

        Update an announcement  # noqa: E501
        """
        pass

    def test_view_announcement_by_id(self):
        """Test case for view_announcement_by_id

        View an announcement  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
