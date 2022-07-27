"""
    Sendbird Platform SDK

    Sendbird Platform API Javascript SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from sendbird_platform_sdk.api_client import ApiClient, Endpoint as _Endpoint
from sendbird_platform_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from sendbird_platform_sdk.model.retrieve_advanced_analytics_metrics_response import RetrieveAdvancedAnalyticsMetricsResponse
from sendbird_platform_sdk.model.view_number_of_concurrent_connections_response import ViewNumberOfConcurrentConnectionsResponse
from sendbird_platform_sdk.model.view_number_of_daily_active_users_response import ViewNumberOfDailyActiveUsersResponse
from sendbird_platform_sdk.model.view_number_of_monthly_active_users_response import ViewNumberOfMonthlyActiveUsersResponse
from sendbird_platform_sdk.model.view_number_of_peak_connections_response import ViewNumberOfPeakConnectionsResponse


class StatisticsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.retrieve_advanced_analytics_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (RetrieveAdvancedAnalyticsMetricsResponse,),
                'auth': [],
                'endpoint_path': '/v3/statistics/metric',
                'operation_id': 'retrieve_advanced_analytics_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                ],
                'required': [
                    'api_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'api_token':
                        (str,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                },
                'location_map': {
                    'api_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.view_number_of_concurrent_connections_endpoint = _Endpoint(
            settings={
                'response_type': (ViewNumberOfConcurrentConnectionsResponse,),
                'auth': [],
                'endpoint_path': '/v3/applications/ccu',
                'operation_id': 'view_number_of_concurrent_connections',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                ],
                'required': [
                    'api_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'api_token':
                        (str,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                },
                'location_map': {
                    'api_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.view_number_of_daily_active_users_endpoint = _Endpoint(
            settings={
                'response_type': (ViewNumberOfDailyActiveUsersResponse,),
                'auth': [],
                'endpoint_path': '/v3/applications/dau',
                'operation_id': 'view_number_of_daily_active_users',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'date',
                ],
                'required': [
                    'api_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'api_token':
                        (str,),
                    'date':
                        (str,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                    'date': 'date',
                },
                'location_map': {
                    'api_token': 'header',
                    'date': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.view_number_of_monthly_active_users_endpoint = _Endpoint(
            settings={
                'response_type': (ViewNumberOfMonthlyActiveUsersResponse,),
                'auth': [],
                'endpoint_path': '/v3/applications/mau',
                'operation_id': 'view_number_of_monthly_active_users',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'date',
                ],
                'required': [
                    'api_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'api_token':
                        (str,),
                    'date':
                        (str,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                    'date': 'date',
                },
                'location_map': {
                    'api_token': 'header',
                    'date': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.view_number_of_peak_connections_endpoint = _Endpoint(
            settings={
                'response_type': (ViewNumberOfPeakConnectionsResponse,),
                'auth': [],
                'endpoint_path': '/v3/applications/peak_connections',
                'operation_id': 'view_number_of_peak_connections',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'time_dimension',
                    'start_year',
                    'start_month',
                    'end_year',
                    'end_month',
                    'start_day',
                    'end_day',
                ],
                'required': [
                    'api_token',
                    'time_dimension',
                    'start_year',
                    'start_month',
                    'end_year',
                    'end_month',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'api_token':
                        (str,),
                    'time_dimension':
                        (str,),
                    'start_year':
                        (int,),
                    'start_month':
                        (int,),
                    'end_year':
                        (int,),
                    'end_month':
                        (int,),
                    'start_day':
                        (int,),
                    'end_day':
                        (int,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                    'time_dimension': 'time_dimension',
                    'start_year': 'start_year',
                    'start_month': 'start_month',
                    'end_year': 'end_year',
                    'end_month': 'end_month',
                    'start_day': 'start_day',
                    'end_day': 'end_day',
                },
                'location_map': {
                    'api_token': 'header',
                    'time_dimension': 'query',
                    'start_year': 'query',
                    'start_month': 'query',
                    'end_year': 'query',
                    'end_month': 'query',
                    'start_day': 'query',
                    'end_day': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def retrieve_advanced_analytics_metrics(
        self,
        api_token,
        **kwargs
    ):
        """Retrieve Advanced analytics metrics  # noqa: E501

        ## Retrieve Advanced analytics metrics  Retrieves Advanced analytics metrics based on the specified parameters. You can retrieve either daily or monthly metrics using the time_dimension parameter.  >__Note__: Daily metrics are calculated and updated every three hours, starting at 1 a.m. in UTC. Meanwhile, monthly metrics are calculated after the last day of the month.  https://sendbird.com/docs/chat/v3/platform-api/guides/advanced-analytics#2-retrieve-advanced-analytics-metrics ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.retrieve_advanced_analytics_metrics(api_token, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            RetrieveAdvancedAnalyticsMetricsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['api_token'] = \
            api_token
        return self.retrieve_advanced_analytics_metrics_endpoint.call_with_http_info(**kwargs)

    def view_number_of_concurrent_connections(
        self,
        api_token,
        **kwargs
    ):
        """View number of concurrent connections  # noqa: E501

        ## View number of concurrent connections  Retrieves the number of devices and opened browser tabs which are currently connected to Sendbird server.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-concurrent-connections  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.view_number_of_concurrent_connections(api_token, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ViewNumberOfConcurrentConnectionsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['api_token'] = \
            api_token
        return self.view_number_of_concurrent_connections_endpoint.call_with_http_info(**kwargs)

    def view_number_of_daily_active_users(
        self,
        api_token,
        **kwargs
    ):
        """View number of daily active users  # noqa: E501

        ## View number of daily active users  Retrieves the number of daily active users of the application (DAU).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-daily-active-users ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.view_number_of_daily_active_users(api_token, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):

        Keyword Args:
            date (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ViewNumberOfDailyActiveUsersResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['api_token'] = \
            api_token
        return self.view_number_of_daily_active_users_endpoint.call_with_http_info(**kwargs)

    def view_number_of_monthly_active_users(
        self,
        api_token,
        **kwargs
    ):
        """View number of monthly active users  # noqa: E501

        ## View number of monthly active users  Retrieves the number of monthly active users of the application (MAU).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-monthly-active-users ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.view_number_of_monthly_active_users(api_token, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):

        Keyword Args:
            date (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ViewNumberOfMonthlyActiveUsersResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['api_token'] = \
            api_token
        return self.view_number_of_monthly_active_users_endpoint.call_with_http_info(**kwargs)

    def view_number_of_peak_connections(
        self,
        api_token,
        time_dimension,
        start_year,
        start_month,
        end_year,
        end_month,
        **kwargs
    ):
        """View number of peak connections  # noqa: E501

        ## View number of peak connections  Retrieves the number of concurrently connected devices to Sendbird server during the requested time period.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-peak-connections ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.view_number_of_peak_connections(api_token, time_dimension, start_year, start_month, end_year, end_month, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):
            time_dimension (str):
            start_year (int):
            start_month (int):
            end_year (int):
            end_month (int):

        Keyword Args:
            start_day (int): [optional]
            end_day (int): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ViewNumberOfPeakConnectionsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['api_token'] = \
            api_token
        kwargs['time_dimension'] = \
            time_dimension
        kwargs['start_year'] = \
            start_year
        kwargs['start_month'] = \
            start_month
        kwargs['end_year'] = \
            end_year
        kwargs['end_month'] = \
            end_month
        return self.view_number_of_peak_connections_endpoint.call_with_http_info(**kwargs)

