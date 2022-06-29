# sendbird_platform_sdk.ModerationApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ban_from_channels_with_custom_channel_types**](ModerationApi.md#ban_from_channels_with_custom_channel_types) | **POST** /v3/users/{user_id}/banned_channel_custom_types | Ban from channels with custom channel types
[**block_user**](ModerationApi.md#block_user) | **POST** /v3/users/{user_id}/block | Block a user
[**gc_ban_user**](ModerationApi.md#gc_ban_user) | **POST** /v3/group_channels/{channel_url}/ban | Ban a user
[**gc_freeze_channel**](ModerationApi.md#gc_freeze_channel) | **PUT** /v3/group_channels/{channel_url}/freeze | Freeze a channel
[**gc_list_banned_users**](ModerationApi.md#gc_list_banned_users) | **GET** /v3/group_channels/{channel_url}/ban | List banned users
[**gc_list_muted_users**](ModerationApi.md#gc_list_muted_users) | **GET** /v3/group_channels/{channel_url}/mute | List muted users
[**gc_mute_user**](ModerationApi.md#gc_mute_user) | **POST** /v3/group_channels/{channel_url}/mute | Mute a user
[**gc_unban_user_by_id**](ModerationApi.md#gc_unban_user_by_id) | **DELETE** /v3/group_channels/{channel_url}/ban/{banned_user_id} | Unban a user
[**gc_unmute_user_by_id**](ModerationApi.md#gc_unmute_user_by_id) | **DELETE** /v3/group_channels/{channel_url}/mute/{muted_user_id} | Unmute a user
[**gc_update_ban_by_id**](ModerationApi.md#gc_update_ban_by_id) | **PUT** /v3/group_channels/{channel_url}/ban/{banned_user_id} | Update a ban
[**gc_view_ban_by_id**](ModerationApi.md#gc_view_ban_by_id) | **GET** /v3/group_channels/{channel_url}/ban/{banned_user_id} | View a ban
[**gc_view_mute_by_id**](ModerationApi.md#gc_view_mute_by_id) | **GET** /v3/group_channels/{channel_url}/mute/{muted_user_id} | View a mute
[**list_banned_channels**](ModerationApi.md#list_banned_channels) | **GET** /v3/users/{user_id}/ban | List banned channels
[**list_blocked_users**](ModerationApi.md#list_blocked_users) | **GET** /v3/users/{user_id}/block | List blocked users
[**list_muted_channels**](ModerationApi.md#list_muted_channels) | **GET** /v3/users/{user_id}/mute | List muted channels
[**mute_in_channels_with_custom_channel_types**](ModerationApi.md#mute_in_channels_with_custom_channel_types) | **POST** /v3/users/{user_id}/muted_channel_custom_types | Mute in channels with custom channel types
[**oc_ban_user**](ModerationApi.md#oc_ban_user) | **POST** /v3/open_channels/{channel_url}/ban | Ban a user
[**oc_freeze_channel**](ModerationApi.md#oc_freeze_channel) | **PUT** /v3/open_channels/{channel_url}/freeze | Freeze a channel
[**oc_list_banned_users**](ModerationApi.md#oc_list_banned_users) | **GET** /v3/open_channels/{channel_url}/ban | List banned users
[**oc_list_muted_users**](ModerationApi.md#oc_list_muted_users) | **GET** /v3/open_channels/{channel_url}/mute | List muted users
[**oc_mute_user**](ModerationApi.md#oc_mute_user) | **POST** /v3/open_channels/{channel_url}/mute | Mute a user
[**oc_unban_user_by_id**](ModerationApi.md#oc_unban_user_by_id) | **DELETE** /v3/open_channels/{channel_url}/ban/{banned_user_id} | Unban a user
[**oc_unmute_user_by_id**](ModerationApi.md#oc_unmute_user_by_id) | **DELETE** /v3/open_channels/{channel_url}/mute/{muted_user_id} | Unmute a user
[**oc_update_ban_by_id**](ModerationApi.md#oc_update_ban_by_id) | **PUT** /v3/open_channels/{channel_url}/ban/{banned_user_id} | Update a ban
[**oc_view_ban_by_id**](ModerationApi.md#oc_view_ban_by_id) | **GET** /v3/open_channels/{channel_url}/ban/{banned_user_id} | View a ban
[**oc_view_mute_by_id**](ModerationApi.md#oc_view_mute_by_id) | **GET** /v3/open_channels/{channel_url}/mute/{muted_user_id} | View a mute
[**unblock_user_by_id**](ModerationApi.md#unblock_user_by_id) | **DELETE** /v3/users/{user_id}/block/{target_id} | Unblock a user


# **ban_from_channels_with_custom_channel_types**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} ban_from_channels_with_custom_channel_types(api_token, user_id)

Ban from channels with custom channel types

## Ban from channels with custom channel types  Bans a user from channels with particular custom channel types.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-ban-from-channels-with-custom-channel-types ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.ban_from_channels_with_custom_channel_types_data import BanFromChannelsWithCustomChannelTypesData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    ban_from_channels_with_custom_channel_types_data = BanFromChannelsWithCustomChannelTypesData(
        channel_custom_types=[
            "channel_custom_types_example",
        ],
    ) # BanFromChannelsWithCustomChannelTypesData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ban from channels with custom channel types
        api_response = api_instance.ban_from_channels_with_custom_channel_types(api_token, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->ban_from_channels_with_custom_channel_types: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ban from channels with custom channel types
        api_response = api_instance.ban_from_channels_with_custom_channel_types(api_token, user_id, ban_from_channels_with_custom_channel_types_data=ban_from_channels_with_custom_channel_types_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->ban_from_channels_with_custom_channel_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **ban_from_channels_with_custom_channel_types_data** | [**BanFromChannelsWithCustomChannelTypesData**](BanFromChannelsWithCustomChannelTypesData.md)|  | [optional]

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

# **block_user**
> BlockUserResponse block_user(api_token, user_id)

Block a user

## Block a user  Allows a user to block another user. A user doesn't receive messages from someone they have blocked anymore. Also, blocking someone doesn't alert them that they have been blocked. Blocked users still can send messages as normal in the channel: however, they can't receive any messages from the users who have blocked them.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-block-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.block_user_response import BlockUserResponse
from sendbird_platform_sdk.model.block_user_data import BlockUserData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    block_user_data = BlockUserData(
        user_id="user_id_example",
        target_id="target_id_example",
        user_ids=[
            1,
        ],
        users=[
            1,
        ],
    ) # BlockUserData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Block a user
        api_response = api_instance.block_user(api_token, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->block_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Block a user
        api_response = api_instance.block_user(api_token, user_id, block_user_data=block_user_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->block_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **block_user_data** | [**BlockUserData**](BlockUserData.md)|  | [optional]

### Return type

[**BlockUserResponse**](BlockUserResponse.md)

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

# **gc_ban_user**
> GcBanUserResponse gc_ban_user(api_token, channel_url)

Ban a user

## Ban a user  Bans a user from a group channel. A banned user is immediately expelled from a channel and allowed to join the channel again after a set time period.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-ban-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.gc_ban_user_data import GcBanUserData
from sendbird_platform_sdk.model.gc_ban_user_response import GcBanUserResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    gc_ban_user_data = GcBanUserData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        agent_id="agent_id_example",
        seconds=1,
        description="description_example",
    ) # GcBanUserData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ban a user
        api_response = api_instance.gc_ban_user(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_ban_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ban a user
        api_response = api_instance.gc_ban_user(api_token, channel_url, gc_ban_user_data=gc_ban_user_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_ban_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **gc_ban_user_data** | [**GcBanUserData**](GcBanUserData.md)|  | [optional]

### Return type

[**GcBanUserResponse**](GcBanUserResponse.md)

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

# **gc_freeze_channel**
> SendBirdGroupChannel gc_freeze_channel(api_token, channel_url)

Freeze a channel

## Freeze a channel  Freezes or unfreezes a group channel.  > __Note__: Only users designated as channel operators are allowed to talk when a channel is frozen.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-freeze-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.gc_freeze_channel_data import GcFreezeChannelData
from sendbird_platform_sdk.model.send_bird_group_channel import SendBirdGroupChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    gc_freeze_channel_data = GcFreezeChannelData(
        channel_url="channel_url_example",
        freeze=True,
    ) # GcFreezeChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Freeze a channel
        api_response = api_instance.gc_freeze_channel(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_freeze_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Freeze a channel
        api_response = api_instance.gc_freeze_channel(api_token, channel_url, gc_freeze_channel_data=gc_freeze_channel_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_freeze_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **gc_freeze_channel_data** | [**GcFreezeChannelData**](GcFreezeChannelData.md)|  | [optional]

### Return type

[**SendBirdGroupChannel**](SendBirdGroupChannel.md)

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

# **gc_list_banned_users**
> GcListBannedUsersResponse gc_list_banned_users(api_token, channel_url)

List banned users

## List banned users  Retrieves a list of the banned users from a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-banned-users ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel where to retrieve a list of banned users.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.gc_list_banned_users_response import GcListBannedUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List banned users
        api_response = api_instance.gc_list_banned_users(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_list_banned_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List banned users
        api_response = api_instance.gc_list_banned_users(api_token, channel_url, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_list_banned_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**GcListBannedUsersResponse**](GcListBannedUsersResponse.md)

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

# **gc_list_muted_users**
> GcListMutedUsersResponse gc_list_muted_users(api_token, channel_url)

List muted users

## List muted users  Retrieves a list of the muted users in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-muted-users ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of muted users.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.gc_list_muted_users_response import GcListMutedUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List muted users
        api_response = api_instance.gc_list_muted_users(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_list_muted_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List muted users
        api_response = api_instance.gc_list_muted_users(api_token, channel_url, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_list_muted_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**GcListMutedUsersResponse**](GcListMutedUsersResponse.md)

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

# **gc_mute_user**
> SendBirdGroupChannel gc_mute_user(api_token, channel_url)

Mute a user

## Mute a user  Mutes a user in a group channel. A muted user remains in the channel and is allowed to view the messages, but can't send any messages until unmuted.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-mute-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.gc_mute_user_data import GcMuteUserData
from sendbird_platform_sdk.model.send_bird_group_channel import SendBirdGroupChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    gc_mute_user_data = GcMuteUserData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        seconds=1,
        description="description_example",
    ) # GcMuteUserData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mute a user
        api_response = api_instance.gc_mute_user(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_mute_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mute a user
        api_response = api_instance.gc_mute_user(api_token, channel_url, gc_mute_user_data=gc_mute_user_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_mute_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **gc_mute_user_data** | [**GcMuteUserData**](GcMuteUserData.md)|  | [optional]

### Return type

[**SendBirdGroupChannel**](SendBirdGroupChannel.md)

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

# **gc_unban_user_by_id**
> InlineResponse2001 gc_unban_user_by_id(api_token, channel_url, banned_user_id)

Unban a user

## Unban a user  Unbans a user from a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-unban-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unban a user
        api_response = api_instance.gc_unban_user_by_id(api_token, channel_url, banned_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_unban_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **gc_unmute_user_by_id**
> InlineResponse2001 gc_unmute_user_by_id(api_token, channel_url, muted_user_id)

Unmute a user

## Unmute a user  Unmutes a user within a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-unmute-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    muted_user_id = "muted_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unmute a user
        api_response = api_instance.gc_unmute_user_by_id(api_token, channel_url, muted_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_unmute_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **muted_user_id** | **str**|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **gc_update_ban_by_id**
> GcUpdateBanByIdResponse gc_update_ban_by_id(api_token, channel_url, banned_user_id)

Update a ban

## Update a ban  Updates details of a ban imposed on a user. You can change the length of the ban with this action, and also provide an updated description.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-update-a-ban ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.gc_update_ban_by_id_data import GcUpdateBanByIdData
from sendbird_platform_sdk.model.gc_update_ban_by_id_response import GcUpdateBanByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 
    gc_update_ban_by_id_data = GcUpdateBanByIdData(
        channel_url="channel_url_example",
        banned_user_id="banned_user_id_example",
        seconds=1,
        description="description_example",
    ) # GcUpdateBanByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a ban
        api_response = api_instance.gc_update_ban_by_id(api_token, channel_url, banned_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_update_ban_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a ban
        api_response = api_instance.gc_update_ban_by_id(api_token, channel_url, banned_user_id, gc_update_ban_by_id_data=gc_update_ban_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_update_ban_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |
 **gc_update_ban_by_id_data** | [**GcUpdateBanByIdData**](GcUpdateBanByIdData.md)|  | [optional]

### Return type

[**GcUpdateBanByIdResponse**](GcUpdateBanByIdResponse.md)

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

# **gc_view_ban_by_id**
> GcViewBanByIdResponse gc_view_ban_by_id(api_token, channel_url, banned_user_id)

View a ban

## View a ban  Retrieves details of a ban imposed on a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-view-a-ban ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.gc_view_ban_by_id_response import GcViewBanByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a ban
        api_response = api_instance.gc_view_ban_by_id(api_token, channel_url, banned_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_view_ban_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |

### Return type

[**GcViewBanByIdResponse**](GcViewBanByIdResponse.md)

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

# **gc_view_mute_by_id**
> GcViewMuteByIdResponse gc_view_mute_by_id(api_token, channel_url, muted_user_id)

View a mute

## View a mute  Checks if a user is muted in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-view-a-mute ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.gc_view_mute_by_id_response import GcViewMuteByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    muted_user_id = "muted_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a mute
        api_response = api_instance.gc_view_mute_by_id(api_token, channel_url, muted_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->gc_view_mute_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **muted_user_id** | **str**|  |

### Return type

[**GcViewMuteByIdResponse**](GcViewMuteByIdResponse.md)

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

# **list_banned_channels**
> ListBannedChannelsResponse list_banned_channels(api_token, user_id)

List banned channels

## List banned channels  Retrieves a list of open and group channels with additional information where a user is banned.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-list-banned-channels ----------------------------   `user_id`      Type: string      Description: Specifies the unique ID of the target user.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.list_banned_channels_response import ListBannedChannelsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List banned channels
        api_response = api_instance.list_banned_channels(api_token, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->list_banned_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List banned channels
        api_response = api_instance.list_banned_channels(api_token, user_id, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->list_banned_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListBannedChannelsResponse**](ListBannedChannelsResponse.md)

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

# **list_blocked_users**
> ListBlockedUsersResponse list_blocked_users(api_token, user_id)

List blocked users

## List blocked users  Retrieves a list of other users that a user has blocked.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-list-blocked-users ----------------------------   `user_id`      Type: string      Description: Specifies the unique ID of the target user.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.list_blocked_users_response import ListBlockedUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    user_ids = "user_ids_example" # str |  (optional)
    metadatakey = "metadatakey_example" # str |  (optional)
    metadatavalues_in = "metadatavalues_in_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List blocked users
        api_response = api_instance.list_blocked_users(api_token, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->list_blocked_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List blocked users
        api_response = api_instance.list_blocked_users(api_token, user_id, token=token, limit=limit, user_ids=user_ids, metadatakey=metadatakey, metadatavalues_in=metadatavalues_in)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->list_blocked_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **user_ids** | **str**|  | [optional]
 **metadatakey** | **str**|  | [optional]
 **metadatavalues_in** | **str**|  | [optional]

### Return type

[**ListBlockedUsersResponse**](ListBlockedUsersResponse.md)

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

# **list_muted_channels**
> ListMutedChannelsResponse list_muted_channels(api_token, user_id)

List muted channels

## List muted channels  Retrieves a list of open and group channels with additional information where a user is muted.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-list-muted-channels ----------------------------   `user_id`      Type: string      Description: Specifies the unique ID of the target user.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.list_muted_channels_response import ListMutedChannelsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List muted channels
        api_response = api_instance.list_muted_channels(api_token, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->list_muted_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List muted channels
        api_response = api_instance.list_muted_channels(api_token, user_id, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->list_muted_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListMutedChannelsResponse**](ListMutedChannelsResponse.md)

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

# **mute_in_channels_with_custom_channel_types**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} mute_in_channels_with_custom_channel_types(api_token, user_id)

Mute in channels with custom channel types

## Mute in channels with custom channel types  Mutes a user in channels with particular custom channel types.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-mute-in-channels-with-custom-channel-types ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.mute_in_channels_with_custom_channel_types_data import MuteInChannelsWithCustomChannelTypesData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    mute_in_channels_with_custom_channel_types_data = MuteInChannelsWithCustomChannelTypesData(
        channel_custom_types=[
            "channel_custom_types_example",
        ],
    ) # MuteInChannelsWithCustomChannelTypesData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mute in channels with custom channel types
        api_response = api_instance.mute_in_channels_with_custom_channel_types(api_token, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->mute_in_channels_with_custom_channel_types: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mute in channels with custom channel types
        api_response = api_instance.mute_in_channels_with_custom_channel_types(api_token, user_id, mute_in_channels_with_custom_channel_types_data=mute_in_channels_with_custom_channel_types_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->mute_in_channels_with_custom_channel_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **mute_in_channels_with_custom_channel_types_data** | [**MuteInChannelsWithCustomChannelTypesData**](MuteInChannelsWithCustomChannelTypesData.md)|  | [optional]

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

# **oc_ban_user**
> OcBanUserResponse oc_ban_user(api_token, channel_url)

Ban a user

## Ban a user  Bans a user from an open channel. A banned user is immediately expelled from a channel and allowed to participate in the channel again after a set time period.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-ban-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.oc_ban_user_response import OcBanUserResponse
from sendbird_platform_sdk.model.oc_ban_user_data import OcBanUserData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
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
        api_response = api_instance.oc_ban_user(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_ban_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ban a user
        api_response = api_instance.oc_ban_user(api_token, channel_url, oc_ban_user_data=oc_ban_user_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_ban_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **oc_ban_user_data** | [**OcBanUserData**](OcBanUserData.md)|  | [optional]

### Return type

[**OcBanUserResponse**](OcBanUserResponse.md)

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

# **oc_freeze_channel**
> SendBirdOpenChannel oc_freeze_channel(api_token, channel_url)

Freeze a channel

## Freeze a channel  Freezes or unfreezes an open channel.  > __Note__: Only users designated as channel operators are allowed to talk when a channel is frozen.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-freeze-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.oc_freeze_channel_data import OcFreezeChannelData
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
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    oc_freeze_channel_data = OcFreezeChannelData(
        channel_url="channel_url_example",
        freeze=True,
    ) # OcFreezeChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Freeze a channel
        api_response = api_instance.oc_freeze_channel(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_freeze_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Freeze a channel
        api_response = api_instance.oc_freeze_channel(api_token, channel_url, oc_freeze_channel_data=oc_freeze_channel_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_freeze_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
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
> OcListBannedUsersResponse oc_list_banned_users(api_token, channel_url)

List banned users

## List banned users  Retrieves a list of banned users from a specific open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-banned-users ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel where to retrieve a list of banned users.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.oc_list_banned_users_response import OcListBannedUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List banned users
        api_response = api_instance.oc_list_banned_users(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_list_banned_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List banned users
        api_response = api_instance.oc_list_banned_users(api_token, channel_url, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_list_banned_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**OcListBannedUsersResponse**](OcListBannedUsersResponse.md)

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
> OcListMutedUsersResponse oc_list_muted_users(api_token, channel_url)

List muted users

## List muted users  Retrieves a list of muted users in the channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-list-muted-users ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of muted users.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.oc_list_muted_users_response import OcListMutedUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List muted users
        api_response = api_instance.oc_list_muted_users(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_list_muted_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List muted users
        api_response = api_instance.oc_list_muted_users(api_token, channel_url, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_list_muted_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**OcListMutedUsersResponse**](OcListMutedUsersResponse.md)

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
> SendBirdOpenChannel oc_mute_user(api_token, channel_url)

Mute a user

## Mute a user  Mutes a user in the channel. A muted user remains in the channel and is allowed to view the messages, but can't send any messages until unmuted.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-mute-a-user

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.send_bird_open_channel import SendBirdOpenChannel
from sendbird_platform_sdk.model.oc_mute_user_data import OcMuteUserData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    oc_mute_user_data = OcMuteUserData(
        user_id="user_id_example",
        seconds=1,
        description="description_example",
    ) # OcMuteUserData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mute a user
        api_response = api_instance.oc_mute_user(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_mute_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mute a user
        api_response = api_instance.oc_mute_user(api_token, channel_url, oc_mute_user_data=oc_mute_user_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_mute_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
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

# **oc_unban_user_by_id**
> InlineResponse2001 oc_unban_user_by_id(api_token, channel_url, banned_user_id)

Unban a user

## Unban a user  Unbans a user from an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-unban-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unban a user
        api_response = api_instance.oc_unban_user_by_id(api_token, channel_url, banned_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_unban_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **oc_unmute_user_by_id**
> InlineResponse2001 oc_unmute_user_by_id(api_token, channel_url, muted_user_id)

Unmute a user

## Unmute a user  Unmutes a user from an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-unmute-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    muted_user_id = "muted_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unmute a user
        api_response = api_instance.oc_unmute_user_by_id(api_token, channel_url, muted_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_unmute_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **muted_user_id** | **str**|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **oc_update_ban_by_id**
> OcUpdateBanByIdResponse oc_update_ban_by_id(api_token, channel_url, banned_user_id)

Update a ban

## Update a ban  Updates details of a ban imposed on a user. You can change the length of a ban with this action, and also provide an updated description.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-update-a-ban ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.oc_update_ban_by_id_response import OcUpdateBanByIdResponse
from sendbird_platform_sdk.model.oc_update_ban_by_id_data import OcUpdateBanByIdData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 
    oc_update_ban_by_id_data = OcUpdateBanByIdData(
        channel_url="channel_url_example",
        banned_user_id="banned_user_id_example",
        seconds=1,
        description="description_example",
    ) # OcUpdateBanByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a ban
        api_response = api_instance.oc_update_ban_by_id(api_token, channel_url, banned_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_update_ban_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a ban
        api_response = api_instance.oc_update_ban_by_id(api_token, channel_url, banned_user_id, oc_update_ban_by_id_data=oc_update_ban_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_update_ban_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |
 **oc_update_ban_by_id_data** | [**OcUpdateBanByIdData**](OcUpdateBanByIdData.md)|  | [optional]

### Return type

[**OcUpdateBanByIdResponse**](OcUpdateBanByIdResponse.md)

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
> OcViewBanByIdResponse oc_view_ban_by_id(api_token, channel_url, banned_user_id)

View a ban

## View a ban  Retrieves details of a ban imposed on a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-view-a-ban ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.oc_view_ban_by_id_response import OcViewBanByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a ban
        api_response = api_instance.oc_view_ban_by_id(api_token, channel_url, banned_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_view_ban_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |

### Return type

[**OcViewBanByIdResponse**](OcViewBanByIdResponse.md)

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
> OcViewMuteByIdResponse oc_view_mute_by_id(api_token, channel_url, muted_user_id)

View a mute

## View a mute  Checks if a user is muted in an open channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-view-a-mute ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.oc_view_mute_by_id_response import OcViewMuteByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    muted_user_id = "muted_user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a mute
        api_response = api_instance.oc_view_mute_by_id(api_token, channel_url, muted_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->oc_view_mute_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **muted_user_id** | **str**|  |

### Return type

[**OcViewMuteByIdResponse**](OcViewMuteByIdResponse.md)

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

# **unblock_user_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unblock_user_by_id(api_token, user_id, target_id)

Unblock a user

## Unblock a user  Unblocks the user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-unblock-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moderation_api.ModerationApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    target_id = "target_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unblock a user
        api_response = api_instance.unblock_user_by_id(api_token, user_id, target_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->unblock_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **target_id** | **str**|  |

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

