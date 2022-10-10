"""
    Sendbird Platform SDK

    Sendbird Platform API SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@sendbird.com
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
from sendbird_platform_sdk.model.get_detailed_open_rate_of_announcement_by_id_response import GetDetailedOpenRateOfAnnouncementByIdResponse
from sendbird_platform_sdk.model.get_detailed_open_rate_of_announcement_group_response import GetDetailedOpenRateOfAnnouncementGroupResponse
from sendbird_platform_sdk.model.get_detailed_open_status_of_announcement_by_id_response import GetDetailedOpenStatusOfAnnouncementByIdResponse
from sendbird_platform_sdk.model.view_announcement_by_id_response import ViewAnnouncementByIdResponse


class AnnouncementApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_detailed_open_rate_of_announcement_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (GetDetailedOpenRateOfAnnouncementByIdResponse,),
                'auth': [],
                'endpoint_path': '/v3/announcement_open_rate/{unique_id}',
                'operation_id': 'get_detailed_open_rate_of_announcement_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'unique_id',
                ],
                'required': [
                    'api_token',
                    'unique_id',
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
                    'unique_id':
                        (str,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                    'unique_id': 'unique_id',
                },
                'location_map': {
                    'api_token': 'header',
                    'unique_id': 'path',
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
        self.get_detailed_open_rate_of_announcement_group_endpoint = _Endpoint(
            settings={
                'response_type': (GetDetailedOpenRateOfAnnouncementGroupResponse,),
                'auth': [],
                'endpoint_path': '/v3/announcement_open_rate_by_group/{announcement_group}',
                'operation_id': 'get_detailed_open_rate_of_announcement_group',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'announcement_group',
                ],
                'required': [
                    'api_token',
                    'announcement_group',
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
                    'announcement_group':
                        (str,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                    'announcement_group': 'announcement_group',
                },
                'location_map': {
                    'api_token': 'header',
                    'announcement_group': 'path',
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
        self.get_detailed_open_status_of_announcement_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (GetDetailedOpenStatusOfAnnouncementByIdResponse,),
                'auth': [],
                'endpoint_path': '/v3/announcement_open_status/{unique_id}',
                'operation_id': 'get_detailed_open_status_of_announcement_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'unique_id',
                    'limit',
                    'next',
                    'unique_ids',
                    'channel_urls',
                    'has_opened',
                ],
                'required': [
                    'api_token',
                    'unique_id',
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
                    'unique_id':
                        (str,),
                    'limit':
                        (int,),
                    'next':
                        (str,),
                    'unique_ids':
                        ([str],),
                    'channel_urls':
                        ([str],),
                    'has_opened':
                        (bool,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                    'unique_id': 'unique_id',
                    'limit': 'limit',
                    'next': 'next',
                    'unique_ids': 'unique_ids',
                    'channel_urls': 'channel_urls',
                    'has_opened': 'has_opened',
                },
                'location_map': {
                    'api_token': 'header',
                    'unique_id': 'path',
                    'limit': 'query',
                    'next': 'query',
                    'unique_ids': 'query',
                    'channel_urls': 'query',
                    'has_opened': 'query',
                },
                'collection_format_map': {
                    'unique_ids': 'multi',
                    'channel_urls': 'multi',
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
        self.view_announcement_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (ViewAnnouncementByIdResponse,),
                'auth': [],
                'endpoint_path': '/v3/announcements/{unique_id}',
                'operation_id': 'view_announcement_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'unique_id',
                ],
                'required': [
                    'api_token',
                    'unique_id',
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
                    'unique_id':
                        (str,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                    'unique_id': 'unique_id',
                },
                'location_map': {
                    'api_token': 'header',
                    'unique_id': 'path',
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

    def get_detailed_open_rate_of_announcement_by_id(
        self,
        api_token,
        unique_id,
        **kwargs
    ):
        """Get detailed open rate of an announcement  # noqa: E501

        ## Get detailed open rate of an announcement  Retrieves the detailed open rate information of an announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-rate-of-an-announcement ----------------------------   `unique_id`      Type: string      Description: Specifies the unique ID of the announcement to get its open rate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_detailed_open_rate_of_announcement_by_id(api_token, unique_id, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):
            unique_id (str):

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
            GetDetailedOpenRateOfAnnouncementByIdResponse
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
        kwargs['unique_id'] = \
            unique_id
        return self.get_detailed_open_rate_of_announcement_by_id_endpoint.call_with_http_info(**kwargs)

    def get_detailed_open_rate_of_announcement_group(
        self,
        api_token,
        announcement_group,
        **kwargs
    ):
        """Get detailed open rate of an announcement group  # noqa: E501

        ## Get detailed open rate of an announcement group  Retrieves the detailed open rate information of an announcement group.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-rate-of-an-announcement-group ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_detailed_open_rate_of_announcement_group(api_token, announcement_group, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):
            announcement_group (str):

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
            GetDetailedOpenRateOfAnnouncementGroupResponse
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
        kwargs['announcement_group'] = \
            announcement_group
        return self.get_detailed_open_rate_of_announcement_group_endpoint.call_with_http_info(**kwargs)

    def get_detailed_open_status_of_announcement_by_id(
        self,
        api_token,
        unique_id,
        **kwargs
    ):
        """Get detailed open status of an announcement  # noqa: E501

        ## Get detailed open status of an announcement  Retrieves the detailed open status information of a specific announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-status-of-an-announcement ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_detailed_open_status_of_announcement_by_id(api_token, unique_id, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):
            unique_id (str):

        Keyword Args:
            limit (int): [optional]
            next (str): [optional]
            unique_ids ([str]): [optional]
            channel_urls ([str]): [optional]
            has_opened (bool): [optional]
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
            GetDetailedOpenStatusOfAnnouncementByIdResponse
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
        kwargs['unique_id'] = \
            unique_id
        return self.get_detailed_open_status_of_announcement_by_id_endpoint.call_with_http_info(**kwargs)

    def view_announcement_by_id(
        self,
        api_token,
        unique_id,
        **kwargs
    ):
        """View an announcement  # noqa: E501

        ## View an announcement  Retrieves information on a specific announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-view-an-announcement ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.view_announcement_by_id(api_token, unique_id, async_req=True)
        >>> result = thread.get()

        Args:
            api_token (str):
            unique_id (str):

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
            ViewAnnouncementByIdResponse
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
        kwargs['unique_id'] = \
            unique_id
        return self.view_announcement_by_id_endpoint.call_with_http_info(**kwargs)

