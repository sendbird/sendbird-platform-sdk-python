"""
    Sendbird Platform SDK

    Sendbird Platform API Javascript SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import sendbird_platform_sdk
from sendbird_platform_sdk.api.statistics_api import StatisticsApi  # noqa: E501


class TestStatisticsApi(unittest.TestCase):
    """StatisticsApi unit test stubs"""

    def setUp(self):
        self.api = StatisticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_advanced_analytics_metrics(self):
        """Test case for retrieve_advanced_analytics_metrics

        Retrieve Advanced analytics metrics  # noqa: E501
        """
        pass

    def test_view_number_of_concurrent_connections(self):
        """Test case for view_number_of_concurrent_connections

        View number of concurrent connections  # noqa: E501
        """
        pass

    def test_view_number_of_daily_active_users(self):
        """Test case for view_number_of_daily_active_users

        View number of daily active users  # noqa: E501
        """
        pass

    def test_view_number_of_monthly_active_users(self):
        """Test case for view_number_of_monthly_active_users

        View number of monthly active users  # noqa: E501
        """
        pass

    def test_view_number_of_peak_connections(self):
        """Test case for view_number_of_peak_connections

        View number of peak connections  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
