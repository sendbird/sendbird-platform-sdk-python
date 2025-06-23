# sendbird_platform_sdk.OpenChannelApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_an_open_channel**](OpenChannelApi.md#create_an_open_channel) | **POST** /v3/open_channels | Create an open channel
[**delete_an_open_channel**](OpenChannelApi.md#delete_an_open_channel) | **DELETE** /v3/open_channels/{channel_url} | Delete an open channel
[**get_an_open_channel**](OpenChannelApi.md#get_an_open_channel) | **GET** /v3/open_channels/{channel_url} | Get an open channel
[**list_channel_operators**](OpenChannelApi.md#list_channel_operators) | **GET** /v3/open_channels/{channel_url}/operators | List operators of an open channel
[**list_open_channels**](OpenChannelApi.md#list_open_channels) | **GET** /v3/open_channels | List open channels
[**register_operators**](OpenChannelApi.md#register_operators) | **POST** /v3/open_channels/{channel_url}/operators | Register operators to an open channel
[**unregister_operators**](OpenChannelApi.md#unregister_operators) | **DELETE** /v3/open_channels/{channel_url}/operators | Unregister operators from an open channel
[**update_an_open_channel**](OpenChannelApi.md#update_an_open_channel) | **PUT** /v3/open_channels/{channel_url} | Update an open channel


# **create_an_open_channel**
> SendbirdOpenChannel create_an_open_channel()

Create an open channel

## Create an open channel  You can create an [open channel](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel) that facilitates conversations for millions of users. Open channels allow a seamless chat experience possible for all participants by using [dynamic partitioning](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#4-how-dynamic-partitioning-works) which creates subchannels that each handle up to tens of thousands of participants.  Because users don't need invitations to join open channels, short-lived live events like concerts or live streams that don't require a sustained membership are good use cases for open channels.  [https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-create-a-channel](https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-create-a-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.sendbird_open_channel import SendbirdOpenChannel
from sendbird_platform_sdk.model.create_an_open_channel_request import CreateAnOpenChannelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_an_open_channel_request = CreateAnOpenChannelRequest(
        is_dynamic_partitioned=True,
        channel_url="channel_url_example",
        cover_file=open('/path/to/file', 'rb'),
        cover_url="cover_url_example",
        custom_type="custom_type_example",
        data="data_example",
        is_ephemeral=True,
        name="name_example",
        operator_ids=[
            "operator_ids_example",
        ],
    ) # CreateAnOpenChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an open channel
        api_response = api_instance.create_an_open_channel(api_token=api_token, create_an_open_channel_request=create_an_open_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->create_an_open_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **create_an_open_channel_request** | [**CreateAnOpenChannelRequest**](CreateAnOpenChannelRequest.md)|  | [optional]

### Return type

[**SendbirdOpenChannel**](SendbirdOpenChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_open_channel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_an_open_channel(channel_url)

Delete an open channel

## Delete an open channel  You can delete an open channel using this API. See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/delete-an-open-channel#1-delete-an-open-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete an open channel
        api_response = api_instance.delete_an_open_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->delete_an_open_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete an open channel
        api_response = api_instance.delete_an_open_channel(channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->delete_an_open_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_open_channel**
> SendbirdOpenChannel get_an_open_channel(channel_url)

Get an open channel

## Get an open channel  This action retrieves information about a specific [open channel](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel).  [https://sendbird.com/docs/chat/platform-api/v3/channel/listing-channels-in-an-application/get-an-open-channel#1-get-an-open-channel](https://sendbird.com/docs/chat/platform-api/v3/channel/listing-channels-in-an-application/get-an-open-channel#1-get-an-open-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.sendbird_open_channel import SendbirdOpenChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    include_operators = True # bool | Determines whether to include a list of operators in the response. (Default: false) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an open channel
        api_response = api_instance.get_an_open_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->get_an_open_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an open channel
        api_response = api_instance.get_an_open_channel(channel_url, api_token=api_token, include_operators=include_operators)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->get_an_open_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **include_operators** | **bool**| Determines whether to include a list of operators in the response. (Default: false) | [optional]

### Return type

[**SendbirdOpenChannel**](SendbirdOpenChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_channel_operators**
> ListOperatorsResponse list_channel_operators(channel_url)

List operators of an open channel

## List operators of an open channel  You can retrieve a list of operators of an open channel using this API.  https://sendbird.com/docs/chat/platform-api/v3/user/assigning-a-user-role/list-operators-of-an-open-channel#1-list-operators-of-an-open-channel  `channel_url`   Type: string   Description: Specifies the URL of the channel to retrieve a list of operators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.list_operators_response import ListOperatorsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List operators of an open channel
        api_response = api_instance.list_channel_operators(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->list_channel_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List operators of an open channel
        api_response = api_instance.list_channel_operators(channel_url, token=token, limit=limit, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->list_channel_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**ListOperatorsResponse**](ListOperatorsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_open_channels**
> ListOpenChannelsResponse list_open_channels()

List open channels

## List open channels  This action retrieves a list of [open channels](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel). You can use various query parameters to determine the search scope and select what kind of information you want to receive about the queried channels.  [https://sendbird.com/docs/chat/platform-api/v3/channel/listing-channels-in-an-application/list-open-channels#1-list-open-channels](https://sendbird.com/docs/chat/platform-api/v3/channel/listing-channels-in-an-application/list-open-channels#1-list-open-channels)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.list_open_channels_response import ListOpenChannelsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    token = "token_example" # str |  (optional)
    channel_urls = "channel_urls_example" # str | Specifies a comma-separated string of one or more open channel URLs to restrict the search scope. URL encoding each channel URL is recommended. (optional)
    limit = 1 # int |  (optional)
    custom_types = "custom_types_example" # str | Specifies a comma-separated string of one or more custom types to filter open channels. Urlencoding each type is recommended (for example, ?custom_types=urlencoded_type_1,urlencoded_type_2). If not specified, all channels are returned, regardless of their custom type. (optional)
    name_contains = "name_contains_example" # str |  (optional)
    url_contains = "url_contains_example" # str |  (optional)
    show_frozen = True # bool | Determines whether to include frozen channels in the response. Frozen channels are channels where only channel operators are allowed to send messages. (Default: true) (optional)
    show_metadata = True # bool | Determines whether to include channel metadata in the response. (Default: false) (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List open channels
        api_response = api_instance.list_open_channels(token=token, channel_urls=channel_urls, limit=limit, custom_types=custom_types, name_contains=name_contains, url_contains=url_contains, show_frozen=show_frozen, show_metadata=show_metadata, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->list_open_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional]
 **channel_urls** | **str**| Specifies a comma-separated string of one or more open channel URLs to restrict the search scope. URL encoding each channel URL is recommended. | [optional]
 **limit** | **int**|  | [optional]
 **custom_types** | **str**| Specifies a comma-separated string of one or more custom types to filter open channels. Urlencoding each type is recommended (for example, ?custom_types&#x3D;urlencoded_type_1,urlencoded_type_2). If not specified, all channels are returned, regardless of their custom type. | [optional]
 **name_contains** | **str**|  | [optional]
 **url_contains** | **str**|  | [optional]
 **show_frozen** | **bool**| Determines whether to include frozen channels in the response. Frozen channels are channels where only channel operators are allowed to send messages. (Default: true) | [optional]
 **show_metadata** | **bool**| Determines whether to include channel metadata in the response. (Default: false) | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**ListOpenChannelsResponse**](ListOpenChannelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_operators**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} register_operators(channel_url)

Register operators to an open channel

## Register operators to an open channel  You can register one or more operators to an open channel using this API.  https://sendbird.com/docs/chat/platform-api/v3/user/assigning-a-user-role/register-operators-to-an-open-channel#1-register-operators-to-an-open-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.register_operators_to_a_group_channel_request import RegisterOperatorsToAGroupChannelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    register_operators_to_a_group_channel_request = RegisterOperatorsToAGroupChannelRequest(
        operator_ids=[
            "operator_ids_example",
        ],
    ) # RegisterOperatorsToAGroupChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register operators to an open channel
        api_response = api_instance.register_operators(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->register_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register operators to an open channel
        api_response = api_instance.register_operators(channel_url, api_token=api_token, register_operators_to_a_group_channel_request=register_operators_to_a_group_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->register_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **register_operators_to_a_group_channel_request** | [**RegisterOperatorsToAGroupChannelRequest**](RegisterOperatorsToAGroupChannelRequest.md)|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_operators**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unregister_operators(channel_url, operator_ids)

Unregister operators from an open channel

## Unregister operators from an open channel  You can unregister operators in an open channel but keep them in the channel as participants using this API.  https://sendbird.com/docs/chat/platform-api/v3/user/assigning-a-user-role/unregister-operators-from-an-open-channel#1-unregister-operators-from-an-open-channel  `channel_url`   Type: string   Description: Specifies the URL of the channel to cancel the registration of operators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    operator_ids = "operator_ids_example" # str | Specifies an array of one or more operator IDs to unregister from the channel. The operators in this array remain as participants of the channel after losing their operational roles. Urlencoding each operator ID is recommended. An example of a Urlencoded array would be ?operator_ids=urlencoded_id_1,urlencoded_id_2.
    delete_all = True # bool | Determines whether to unregister all operators and leave them as the participants of the channel. When this is set to true, the operator_ids property isn't effective and doesn't need to be specified in the request. (Default: false) (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unregister operators from an open channel
        api_response = api_instance.unregister_operators(channel_url, operator_ids)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->unregister_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unregister operators from an open channel
        api_response = api_instance.unregister_operators(channel_url, operator_ids, delete_all=delete_all, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->unregister_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **operator_ids** | **str**| Specifies an array of one or more operator IDs to unregister from the channel. The operators in this array remain as participants of the channel after losing their operational roles. Urlencoding each operator ID is recommended. An example of a Urlencoded array would be ?operator_ids&#x3D;urlencoded_id_1,urlencoded_id_2. |
 **delete_all** | **bool**| Determines whether to unregister all operators and leave them as the participants of the channel. When this is set to true, the operator_ids property isn&#39;t effective and doesn&#39;t need to be specified in the request. (Default: false) | [optional]
 **api_token** | **str**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_open_channel**
> SendbirdOpenChannel update_an_open_channel(channel_url)

Update an open channel

## Update an open channel  You can update information about an open channel using this API. You can add a cover image to a channel to better identify the channel or specify a custom channel type for grouping channels by custom type. See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/update-an-open-channel#1-update-an-open-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.sendbird_open_channel import SendbirdOpenChannel
from sendbird_platform_sdk.model.update_an_open_channel_request import UpdateAnOpenChannelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_an_open_channel_request = UpdateAnOpenChannelRequest(
        cover_file=open('/path/to/file', 'rb'),
        cover_url="cover_url_example",
        custom_type="custom_type_example",
        data="data_example",
        name="name_example",
        operator_ids=[
            "operator_ids_example",
        ],
    ) # UpdateAnOpenChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an open channel
        api_response = api_instance.update_an_open_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->update_an_open_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an open channel
        api_response = api_instance.update_an_open_channel(channel_url, api_token=api_token, update_an_open_channel_request=update_an_open_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->update_an_open_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_an_open_channel_request** | [**UpdateAnOpenChannelRequest**](UpdateAnOpenChannelRequest.md)|  | [optional]

### Return type

[**SendbirdOpenChannel**](SendbirdOpenChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

