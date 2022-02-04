# sendbird-platform-sdk.OpenChannelApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oc_ban_user**](OpenChannelApi.md#oc_ban_user) | **POST** /v3/open_channels/{channel_url}/ban | Ban a user
[**oc_cancel_the_registration_of_operators**](OpenChannelApi.md#oc_cancel_the_registration_of_operators) | **DELETE** /v3/open_channels/{channel_url}/operators | Cancel the registration of operators
[**oc_create_channel**](OpenChannelApi.md#oc_create_channel) | **POST** /v3/open_channels | Create a channel
[**oc_delete_channel_by_url**](OpenChannelApi.md#oc_delete_channel_by_url) | **DELETE** /v3/open_channels/{channel_url} | Delete a channel
[**oc_freeze_channel**](OpenChannelApi.md#oc_freeze_channel) | **PUT** /v3/open_channels/{channel_url}/freeze | Freeze a channel
[**oc_list_banned_users**](OpenChannelApi.md#oc_list_banned_users) | **GET** /v3/open_channels/{channel_url}/ban | List banned users
[**oc_list_channels**](OpenChannelApi.md#oc_list_channels) | **GET** /v3/open_channels | List channels
[**oc_list_muted_users**](OpenChannelApi.md#oc_list_muted_users) | **GET** /v3/open_channels/{channel_url}/mute | List muted users
[**oc_list_operators**](OpenChannelApi.md#oc_list_operators) | **GET** /v3/open_channels/{channel_url}/operators | List operators
[**oc_list_participants**](OpenChannelApi.md#oc_list_participants) | **GET** /v3/open_channels/{channel_url}/participants | List participants
[**oc_mute_user**](OpenChannelApi.md#oc_mute_user) | **POST** /v3/open_channels/{channel_url}/mute | Mute a user
[**oc_register_operators**](OpenChannelApi.md#oc_register_operators) | **POST** /v3/open_channels/{channel_url}/operators | Register operators
[**oc_unban_user_by_id**](OpenChannelApi.md#oc_unban_user_by_id) | **DELETE** /v3/open_channels/{channel_url}/ban/{banned_user_id} | Unban a user
[**oc_unmute_user_by_id**](OpenChannelApi.md#oc_unmute_user_by_id) | **DELETE** /v3/open_channels/{channel_url}/mute/{muted_user_id} | Unmute a user
[**oc_update_ban_by_id**](OpenChannelApi.md#oc_update_ban_by_id) | **PUT** /v3/open_channels/{channel_url}/ban/{banned_user_id} | Update a ban
[**oc_update_channel_by_url**](OpenChannelApi.md#oc_update_channel_by_url) | **PUT** /v3/open_channels/{channel_url} | Update a channel
[**oc_view_ban_by_id**](OpenChannelApi.md#oc_view_ban_by_id) | **GET** /v3/open_channels/{channel_url}/ban/{banned_user_id} | View a ban
[**oc_view_channel_by_url**](OpenChannelApi.md#oc_view_channel_by_url) | **GET** /v3/open_channels/{channel_url} | View a channel
[**oc_view_mute_by_id**](OpenChannelApi.md#oc_view_mute_by_id) | **GET** /v3/open_channels/{channel_url}/mute/{muted_user_id} | View a mute


# **oc_ban_user**
> InlineResponse20033BannedList oc_ban_user(channel_url)

Ban a user

## Ban a user  Bans a user from an open channel. A banned user is immediately expelled from a channel and allowed to participate in the channel again after a set time period.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-ban-a-user ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.inline_response20033_banned_list import InlineResponse20033BannedList
from sendbird-platform-sdk.model.oc_ban_user_data import OcBanUserData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    oc_ban_user_data = OcBanUserData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        agent_id="agent_id_example",
        seconds=1,
        description="description_example",
    ) # OcBanUserData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ban a user
        api_response = api_instance.oc_ban_user(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_ban_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ban a user
        api_response = api_instance.oc_ban_user(channel_url, api_token=api_token, oc_ban_user_data=oc_ban_user_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_ban_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **oc_ban_user_data** | [**OcBanUserData**](OcBanUserData.md)|  | [optional]

### Return type

[**InlineResponse20033BannedList**](InlineResponse20033BannedList.md)

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

# **oc_cancel_the_registration_of_operators**
> oc_cancel_the_registration_of_operators(channel_url, operator_ids)

Cancel the registration of operators

## Cancel the registration of operators  Cancels the registration of operators from an open channel but leave them as participants.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-cancel-the-registration-of-operators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to cancel the registration of operators.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    operator_ids = [
        "operator_ids_example",
    ] # [str] | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    delete_all = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel the registration of operators
        api_instance.oc_cancel_the_registration_of_operators(channel_url, operator_ids)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_cancel_the_registration_of_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel the registration of operators
        api_instance.oc_cancel_the_registration_of_operators(channel_url, operator_ids, api_token=api_token, delete_all=delete_all)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_cancel_the_registration_of_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **operator_ids** | **[str]**|  |
 **api_token** | **str**|  | [optional]
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
> SendBirdOpenChannel oc_create_channel()

Create a channel

## Create a channel  Creates an open channel.  >__Note__: Classic open channels created before the deprecation date of March 2021 will maintain their original form and functions. However, new applications created after December 15, 2020, will be able to create dynamic partitioning open channels only.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-create-a-channel

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.oc_create_channel_data import OcCreateChannelData
from sendbird-platform-sdk.model.send_bird_open_channel import SendBirdOpenChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
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
            1,
        ],
        operators=[
            "operators_example",
        ],
    ) # OcCreateChannelData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a channel
        api_response = api_instance.oc_create_channel(api_token=api_token, oc_create_channel_data=oc_create_channel_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_create_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
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
> oc_delete_channel_by_url(channel_url)

Delete a channel

## Delete a channel  Deletes an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-delete-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel
        api_instance.oc_delete_channel_by_url(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_delete_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a channel
        api_instance.oc_delete_channel_by_url(channel_url, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_delete_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]

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

# **oc_freeze_channel**
> SendBirdOpenChannel oc_freeze_channel(channel_url)

Freeze a channel

## Freeze a channel  Freezes or unfreezes an open channel.  > __Note__: Only users designated as channel operators are allowed to talk when a channel is frozen.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-freeze-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.send_bird_open_channel import SendBirdOpenChannel
from sendbird-platform-sdk.model.oc_freeze_channel_data import OcFreezeChannelData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    oc_freeze_channel_data = OcFreezeChannelData(
        channel_url="channel_url_example",
        freeze=True,
    ) # OcFreezeChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Freeze a channel
        api_response = api_instance.oc_freeze_channel(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_freeze_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Freeze a channel
        api_response = api_instance.oc_freeze_channel(channel_url, api_token=api_token, oc_freeze_channel_data=oc_freeze_channel_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_freeze_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **oc_freeze_channel_data** | [**OcFreezeChannelData**](OcFreezeChannelData.md)|  | [optional]

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

# **oc_list_banned_users**
> InlineResponse20033 oc_list_banned_users(channel_url)

List banned users

## List banned users  Retrieves a list of banned users from a specific open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-banned-users ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel where to retrieve a list of banned users.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.inline_response20033 import InlineResponse20033
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List banned users
        api_response = api_instance.oc_list_banned_users(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_banned_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List banned users
        api_response = api_instance.oc_list_banned_users(channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_banned_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

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
> InlineResponse20030 oc_list_channels()

List channels

## List channels  Retrieves a list of open channels. You can query the list using various parameters.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-channels ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.inline_response20030 import InlineResponse20030
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    custom_types = "custom_types_example" # str |  (optional)
    name_contains = "name_contains_example" # str |  (optional)
    url_contains = "url_contains_example" # str |  (optional)
    show_frozen = True # bool |  (optional)
    show_metadata = True # bool |  (optional)
    custom_type = "custom_type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List channels
        api_response = api_instance.oc_list_channels(api_token=api_token, token=token, limit=limit, custom_types=custom_types, name_contains=name_contains, url_contains=url_contains, show_frozen=show_frozen, show_metadata=show_metadata, custom_type=custom_type)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **custom_types** | **str**|  | [optional]
 **name_contains** | **str**|  | [optional]
 **url_contains** | **str**|  | [optional]
 **show_frozen** | **bool**|  | [optional]
 **show_metadata** | **bool**|  | [optional]
 **custom_type** | **str**|  | [optional]

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

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

# **oc_list_muted_users**
> InlineResponse20031 oc_list_muted_users(channel_url)

List muted users

## List muted users  Retrieves a list of muted users in the channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-muted-users ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of muted users.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.inline_response20031 import InlineResponse20031
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List muted users
        api_response = api_instance.oc_list_muted_users(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_muted_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List muted users
        api_response = api_instance.oc_list_muted_users(channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_muted_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

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
> InlineResponse20034 oc_list_operators(channel_url)

List operators

## List operators  Retrieves a list of operators of an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-operators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of operators.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.inline_response20034 import InlineResponse20034
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List operators
        api_response = api_instance.oc_list_operators(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List operators
        api_response = api_instance.oc_list_operators(channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

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
> InlineResponse20032 oc_list_participants(channel_url)

List participants

## List participants  Retrieves a list of the participants of an open channel. A participant refers to a user who has entered the open channel and is currently online.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-participants ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of participants in.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.inline_response20032 import InlineResponse20032
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List participants
        api_response = api_instance.oc_list_participants(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_participants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List participants
        api_response = api_instance.oc_list_participants(channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_list_participants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

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

# **oc_mute_user**
> SendBirdOpenChannel oc_mute_user(channel_url)

Mute a user

## Mute a user  Mutes a user in the channel. A muted user remains in the channel and is allowed to view the messages, but can't send any messages until unmuted.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-mute-a-user

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.oc_mute_user_data import OcMuteUserData
from sendbird-platform-sdk.model.send_bird_open_channel import SendBirdOpenChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    oc_mute_user_data = OcMuteUserData(
        user_id="user_id_example",
        seconds=1,
        description="description_example",
    ) # OcMuteUserData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mute a user
        api_response = api_instance.oc_mute_user(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_mute_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mute a user
        api_response = api_instance.oc_mute_user(channel_url, api_token=api_token, oc_mute_user_data=oc_mute_user_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_mute_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **oc_mute_user_data** | [**OcMuteUserData**](OcMuteUserData.md)|  | [optional]

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

# **oc_register_operators**
> oc_register_operators(channel_url)

Register operators

## Register operators  Registers one or more operators to an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-register-operators ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.oc_register_operators_data import OcRegisterOperatorsData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    oc_register_operators_data = OcRegisterOperatorsData(
        channel_url="channel_url_example",
        operator_ids=[
            1,
        ],
    ) # OcRegisterOperatorsData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register operators
        api_instance.oc_register_operators(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_register_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register operators
        api_instance.oc_register_operators(channel_url, api_token=api_token, oc_register_operators_data=oc_register_operators_data)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_register_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **oc_register_operators_data** | [**OcRegisterOperatorsData**](OcRegisterOperatorsData.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oc_unban_user_by_id**
> oc_unban_user_by_id(channel_url, banned_user_id)

Unban a user

## Unban a user  Unbans a user from an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-unban-a-user ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unban a user
        api_instance.oc_unban_user_by_id(channel_url, banned_user_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_unban_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unban a user
        api_instance.oc_unban_user_by_id(channel_url, banned_user_id, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_unban_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

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

# **oc_unmute_user_by_id**
> oc_unmute_user_by_id(channel_url, muted_user_id)

Unmute a user

## Unmute a user  Unmutes a user from an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-unmute-a-user ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    muted_user_id = "muted_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unmute a user
        api_instance.oc_unmute_user_by_id(channel_url, muted_user_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_unmute_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unmute a user
        api_instance.oc_unmute_user_by_id(channel_url, muted_user_id, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_unmute_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **muted_user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

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

# **oc_update_ban_by_id**
> SendBirdUser oc_update_ban_by_id(channel_url, banned_user_id)

Update a ban

## Update a ban  Updates details of a ban imposed on a user. You can change the length of a ban with this action, and also provide an updated description.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-update-a-ban ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.oc_update_ban_by_id_data import OcUpdateBanByIdData
from sendbird-platform-sdk.model.send_bird_user import SendBirdUser
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    oc_update_ban_by_id_data = OcUpdateBanByIdData(
        channel_url="channel_url_example",
        banned_user_id="banned_user_id_example",
        seconds=1,
        description="description_example",
    ) # OcUpdateBanByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a ban
        api_response = api_instance.oc_update_ban_by_id(channel_url, banned_user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_update_ban_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a ban
        api_response = api_instance.oc_update_ban_by_id(channel_url, banned_user_id, api_token=api_token, oc_update_ban_by_id_data=oc_update_ban_by_id_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_update_ban_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **oc_update_ban_by_id_data** | [**OcUpdateBanByIdData**](OcUpdateBanByIdData.md)|  | [optional]

### Return type

[**SendBirdUser**](SendBirdUser.md)

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
> SendBirdOpenChannel oc_update_channel_by_url(channel_url)

Update a channel

## Update a channel  Updates information on an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-update-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.oc_update_channel_by_url_data import OcUpdateChannelByUrlData
from sendbird-platform-sdk.model.send_bird_open_channel import SendBirdOpenChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    oc_update_channel_by_url_data = OcUpdateChannelByUrlData(
        channel_url="channel_url_example",
        name="name_example",
        cover_url="cover_url_example",
        cover_file=open('/path/to/file', 'rb'),
        custom_type="custom_type_example",
        data="data_example",
        operator_ids=[
            1,
        ],
        operators=[
            "operators_example",
        ],
    ) # OcUpdateChannelByUrlData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel
        api_response = api_instance.oc_update_channel_by_url(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_update_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel
        api_response = api_instance.oc_update_channel_by_url(channel_url, api_token=api_token, oc_update_channel_by_url_data=oc_update_channel_by_url_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_update_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
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

# **oc_view_ban_by_id**
> SendBirdUser oc_view_ban_by_id(channel_url, banned_user_id)

View a ban

## View a ban  Retrieves details of a ban imposed on a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-view-a-ban ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.send_bird_user import SendBirdUser
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a ban
        api_response = api_instance.oc_view_ban_by_id(channel_url, banned_user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_view_ban_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a ban
        api_response = api_instance.oc_view_ban_by_id(channel_url, banned_user_id, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_view_ban_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**SendBirdUser**](SendBirdUser.md)

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

# **oc_view_channel_by_url**
> SendBirdOpenChannel oc_view_channel_by_url(channel_url)

View a channel

## View a channel  Retrieves information on a specific open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-view-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.send_bird_open_channel import SendBirdOpenChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel
        api_response = api_instance.oc_view_channel_by_url(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_view_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel
        api_response = api_instance.oc_view_channel_by_url(channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_view_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]

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

# **oc_view_mute_by_id**
> InlineResponse20035 oc_view_mute_by_id(channel_url, muted_user_id)

View a mute

## View a mute  Checks if a user is muted in an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-view-a-mute ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import open_channel_api
from sendbird-platform-sdk.model.inline_response20035 import InlineResponse20035
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = open_channel_api.OpenChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    muted_user_id = "muted_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a mute
        api_response = api_instance.oc_view_mute_by_id(channel_url, muted_user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_view_mute_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a mute
        api_response = api_instance.oc_view_mute_by_id(channel_url, muted_user_id, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling OpenChannelApi->oc_view_mute_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **muted_user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

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

