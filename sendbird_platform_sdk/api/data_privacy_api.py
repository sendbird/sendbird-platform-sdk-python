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
from sendbird_platform_sdk.model.list_gdpr_requests_response import ListGdprRequestsResponse
from sendbird_platform_sdk.model.register_gdpr_request_data import RegisterGdprRequestData
from sendbird_platform_sdk.model.register_gdpr_request_response import RegisterGdprRequestResponse
from sendbird_platform_sdk.model.view_gdpr_request_by_id_response import ViewGdprRequestByIdResponse


class DataPrivacyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.cancel_the_registration_of_gdpr_request_by_id_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/v3/privacy/gdpr/{request_id}',
                'operation_id': 'cancel_the_registration_of_gdpr_request_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'request_id',
                    'api_token',
                ],
                'required': [
                    'request_id',
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
                    'request_id':
                        (str,),
                    'api_token':
                        (str,),
                },
                'attribute_map': {
                    'request_id': 'request_id',
                    'api_token': 'Api-Token',
                },
                'location_map': {
                    'request_id': 'path',
                    'api_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_gdpr_requests_endpoint = _Endpoint(
            settings={
                'response_type': (ListGdprRequestsResponse,),
                'auth': [],
                'endpoint_path': '/v3/privacy/gdpr',
                'operation_id': 'list_gdpr_requests',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'token',
                    'limit',
                ],
                'required': [],
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
                    'token':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                    'token': 'token',
                    'limit': 'limit',
                },
                'location_map': {
                    'api_token': 'header',
                    'token': 'query',
                    'limit': 'query',
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
        self.register_gdpr_request_endpoint = _Endpoint(
            settings={
                'response_type': (RegisterGdprRequestResponse,),
                'auth': [],
                'endpoint_path': '/v3/privacy/gdpr',
                'operation_id': 'register_gdpr_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_token',
                    'register_gdpr_request_data',
                ],
                'required': [],
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
                    'register_gdpr_request_data':
                        (RegisterGdprRequestData,),
                },
                'attribute_map': {
                    'api_token': 'Api-Token',
                },
                'location_map': {
                    'api_token': 'header',
                    'register_gdpr_request_data': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.view_gdpr_request_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (ViewGdprRequestByIdResponse,),
                'auth': [],
                'endpoint_path': '/v3/privacy/gdpr/{request_id}',
                'operation_id': 'view_gdpr_request_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'request_id',
                    'api_token',
                ],
                'required': [
                    'request_id',
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
                    'request_id':
                        (str,),
                    'api_token':
                        (str,),
                },
                'attribute_map': {
                    'request_id': 'request_id',
                    'api_token': 'Api-Token',
                },
                'location_map': {
                    'request_id': 'path',
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

    def cancel_the_registration_of_gdpr_request_by_id(
        self,
        request_id,
        **kwargs
    ):
        """Cancel the registration of a GDPR request  # noqa: E501

        ## Cancel the registration of a GDPR request  Cancels the registration of a specific GDPR request.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-privacy#2-cancel-the-registration-of-a-gdpr-request ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_the_registration_of_gdpr_request_by_id(request_id, async_req=True)
        >>> result = thread.get()

        Args:
            request_id (str):

        Keyword Args:
            api_token (str): [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['request_id'] = \
            request_id
        return self.cancel_the_registration_of_gdpr_request_by_id_endpoint.call_with_http_info(**kwargs)

    def list_gdpr_requests(
        self,
        **kwargs
    ):
        """List GDPR requests  # noqa: E501

        ## List GDPR requests  Retrieves a list of GDPR requests of all types.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-privacy#2-list-gdpr-requests ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_gdpr_requests(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            api_token (str): [optional]
            token (str): [optional]
            limit (int): [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListGdprRequestsResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_gdpr_requests_endpoint.call_with_http_info(**kwargs)

    def register_gdpr_request(
        self,
        **kwargs
    ):
        """Register a GDPR request  # noqa: E501

        ## Register a GDPR request  Registers a specific type of GDPR request to meet the GDPR's requirements.  > __Note__: Currently, only delete and access of the user data are supported. The features for the [right to restriction of processing](https://gdpr-info.eu/art-18-gdpr/) and [right to object](https://gdpr-info.eu/art-21-gdpr/) will be available soon.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-privacy#2-register-a-gdpr-request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.register_gdpr_request(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            api_token (str): [optional]
            register_gdpr_request_data (RegisterGdprRequestData): [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            RegisterGdprRequestResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.register_gdpr_request_endpoint.call_with_http_info(**kwargs)

    def view_gdpr_request_by_id(
        self,
        request_id,
        **kwargs
    ):
        """View a GDPR request  # noqa: E501

        ## View a GDPR request  Retrieves a specific GDPR request.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-privacy#2-view-a-gdpr-request ----------------------------  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.view_gdpr_request_by_id(request_id, async_req=True)
        >>> result = thread.get()

        Args:
            request_id (str):

        Keyword Args:
            api_token (str): [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ViewGdprRequestByIdResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['request_id'] = \
            request_id
        return self.view_gdpr_request_by_id_endpoint.call_with_http_info(**kwargs)

