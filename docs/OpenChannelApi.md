# sendbird_platform_sdk.OpenChannelApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oc_cancel_the_registration_of_operators**](OpenChannelApi.md#oc_cancel_the_registration_of_operators) | **DELETE** /v3/open_channels/{channel_url}/operators | Cancel the registration of operators
[**oc_create_channel**](OpenChannelApi.md#oc_create_channel) | **POST** /v3/open_channels | Create a channel
[**oc_delete_channel_by_url**](OpenChannelApi.md#oc_delete_channel_by_url) | **DELETE** /v3/open_channels/{channel_url} | Delete a channel
[**oc_list_channels**](OpenChannelApi.md#oc_list_channels) | **GET** /v3/open_channels | List channels
[**oc_list_operators**](OpenChannelApi.md#oc_list_operators) | **GET** /v3/open_channels/{channel_url}/operators | List operators
[**oc_list_participants**](OpenChannelApi.md#oc_list_participants) | **GET** /v3/open_channels/{channel_url}/participants | List participants
[**oc_register_operators**](OpenChannelApi.md#oc_register_operators) | **POST** /v3/open_channels/{channel_url}/operators | Register operators
[**oc_update_channel_by_url**](OpenChannelApi.md#oc_update_channel_by_url) | **PUT** /v3/open_channels/{channel_url} | Update a channel
[**oc_view_channel_by_url**](OpenChannelApi.md#oc_view_channel_by_url) | **GET** /v3/open_channels/{channel_url} | View a channel


# **oc_cancel_the_registration_of_operators**
> oc_cancel_the_registration_of_operators(api_token, channel_url, operator_ids)

Cancel the registration of operators

## Cancel the registration of operators  Cancels the registration of operators from an open channel but leave them as participants.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-cancel-the-registration-of-operators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to cancel the registration of operators.

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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    operator_ids = [
        "operator_ids_example",
    ] # [str] | 
    delete_all = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel the registration of operators
        api_instance.oc_cancel_the_registration_of_operators(api_token, channel_url, operator_ids)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_cancel_the_registration_of_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel the registration of operators
        api_instance.oc_cancel_the_registration_of_operators(api_token, channel_url, operator_ids, delete_all=delete_all)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_cancel_the_registration_of_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **operator_ids** | **[str]**|  |
 **delete_all** | **bool**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oc_create_channel**
> SendBirdOpenChannel oc_create_channel(api_token)

Create a channel

## Create a channel  Creates an open channel.  >__Note__: Classic open channels created before the deprecation date of March 2021 will maintain their original form and functions. However, new applications created after December 15, 2020, will be able to create dynamic partitioning open channels only.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-create-a-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.send_bird_open_channel import SendBirdOpenChannel
from sendbird_platform_sdk.model.oc_create_channel_data import OcCreateChannelData
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
    api_token = "{{API_TOKEN}}" # str | 
    oc_create_channel_data = OcCreateChannelData(
        name="name_example",
        channel_url="channel_url_example",
        cover_url="cover_url_example",
        cover_file=open('/path/to/file', 'rb'),
        custom_type="custom_type_example",
        data="data_example",
        is_ephemeral=True,
        is_dynamic_partitioned_2_how_dynamic_partitioning_works=True,
        operator_ids=[
            "operator_ids_example",
        ],
        operators=[
            "operators_example",
        ],
    ) # OcCreateChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a channel
        api_response = api_instance.oc_create_channel(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_create_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a channel
        api_response = api_instance.oc_create_channel(api_token, oc_create_channel_data=oc_create_channel_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_create_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **oc_create_channel_data** | [**OcCreateChannelData**](OcCreateChannelData.md)|  | [optional]

### Return type

[**SendBirdOpenChannel**](SendBirdOpenChannel.md)

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

# **oc_delete_channel_by_url**
> OcDeleteChannelByUrl200Response oc_delete_channel_by_url(api_token, channel_url)

Delete a channel

## Delete a channel  Deletes an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-delete-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.oc_delete_channel_by_url200_response import OcDeleteChannelByUrl200Response
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel
        api_response = api_instance.oc_delete_channel_by_url(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_delete_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |

### Return type

[**OcDeleteChannelByUrl200Response**](OcDeleteChannelByUrl200Response.md)

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

# **oc_list_channels**
> OcListChannelsResponse oc_list_channels(api_token)

List channels

## List channels  Retrieves a list of open channels. You can query the list using various parameters.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-channels ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.oc_list_channels_response import OcListChannelsResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    custom_types = "custom_types_example" # str |  (optional)
    name_contains = "name_contains_example" # str |  (optional)
    url_contains = "url_contains_example" # str |  (optional)
    show_frozen = True # bool |  (optional)
    show_metadata = True # bool |  (optional)
    custom_type = "custom_type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List channels
        api_response = api_instance.oc_list_channels(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List channels
        api_response = api_instance.oc_list_channels(api_token, token=token, limit=limit, custom_types=custom_types, name_contains=name_contains, url_contains=url_contains, show_frozen=show_frozen, show_metadata=show_metadata, custom_type=custom_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **custom_types** | **str**|  | [optional]
 **name_contains** | **str**|  | [optional]
 **url_contains** | **str**|  | [optional]
 **show_frozen** | **bool**|  | [optional]
 **show_metadata** | **bool**|  | [optional]
 **custom_type** | **str**|  | [optional]

### Return type

[**OcListChannelsResponse**](OcListChannelsResponse.md)

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

# **oc_list_operators**
> OcListOperatorsResponse oc_list_operators(api_token, channel_url)

List operators

## List operators  Retrieves a list of operators of an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-operators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of operators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.oc_list_operators_response import OcListOperatorsResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List operators
        api_response = api_instance.oc_list_operators(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List operators
        api_response = api_instance.oc_list_operators(api_token, channel_url, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**OcListOperatorsResponse**](OcListOperatorsResponse.md)

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

# **oc_list_participants**
> OcListParticipantsResponse oc_list_participants(api_token, channel_url)

List participants

## List participants  Retrieves a list of the participants of an open channel. A participant refers to a user who has entered the open channel and is currently online.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-participants ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of participants in.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.oc_list_participants_response import OcListParticipantsResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List participants
        api_response = api_instance.oc_list_participants(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_participants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List participants
        api_response = api_instance.oc_list_participants(api_token, channel_url, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_participants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**OcListParticipantsResponse**](OcListParticipantsResponse.md)

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

# **oc_register_operators**
> OcDeleteChannelByUrl200Response oc_register_operators(api_token, channel_url)

Register operators

## Register operators  Registers one or more operators to an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-register-operators ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.oc_register_operators_data import OcRegisterOperatorsData
from sendbird_platform_sdk.model.oc_delete_channel_by_url200_response import OcDeleteChannelByUrl200Response
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    oc_register_operators_data = OcRegisterOperatorsData(
        channel_url="channel_url_example",
        operator_ids=[
            "operator_ids_example",
        ],
    ) # OcRegisterOperatorsData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register operators
        api_response = api_instance.oc_register_operators(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_register_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register operators
        api_response = api_instance.oc_register_operators(api_token, channel_url, oc_register_operators_data=oc_register_operators_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_register_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **oc_register_operators_data** | [**OcRegisterOperatorsData**](OcRegisterOperatorsData.md)|  | [optional]

### Return type

[**OcDeleteChannelByUrl200Response**](OcDeleteChannelByUrl200Response.md)

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

# **oc_update_channel_by_url**
> SendBirdOpenChannel oc_update_channel_by_url(api_token, channel_url)

Update a channel

## Update a channel  Updates information on an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-update-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.send_bird_open_channel import SendBirdOpenChannel
from sendbird_platform_sdk.model.oc_update_channel_by_url_data import OcUpdateChannelByUrlData
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    oc_update_channel_by_url_data = OcUpdateChannelByUrlData(
        channel_url="channel_url_example",
        name="name_example",
        cover_url="cover_url_example",
        cover_file=open('/path/to/file', 'rb'),
        custom_type="custom_type_example",
        data="data_example",
        operator_ids=[
            "operator_ids_example",
        ],
        operators=[
            "operators_example",
        ],
    ) # OcUpdateChannelByUrlData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel
        api_response = api_instance.oc_update_channel_by_url(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_update_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel
        api_response = api_instance.oc_update_channel_by_url(api_token, channel_url, oc_update_channel_by_url_data=oc_update_channel_by_url_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_update_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **oc_update_channel_by_url_data** | [**OcUpdateChannelByUrlData**](OcUpdateChannelByUrlData.md)|  | [optional]

### Return type

[**SendBirdOpenChannel**](SendBirdOpenChannel.md)

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

# **oc_view_channel_by_url**
> SendBirdOpenChannel oc_view_channel_by_url(api_token, channel_url)

View a channel

## View a channel  Retrieves information on a specific open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-view-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import open_channel_api
from sendbird_platform_sdk.model.send_bird_open_channel import SendBirdOpenChannel
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a channel
        api_response = api_instance.oc_view_channel_by_url(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_view_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |

### Return type

[**SendBirdOpenChannel**](SendBirdOpenChannel.md)

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

