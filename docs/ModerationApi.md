# sendbird_platform_sdk.ModerationApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_a_user**](ModerationApi.md#block_a_user) | **POST** /v3/users/{user_id}/block | Block a user
[**freeze_a_group_channel**](ModerationApi.md#freeze_a_group_channel) | **PUT** /v3/group_channels/{channel_url}/freeze | Freeze a group channel
[**freeze_an_open_channel**](ModerationApi.md#freeze_an_open_channel) | **PUT** /v3/open_channels/{channel_url}/freeze | Freeze an open channel
[**list_blocked_users**](ModerationApi.md#list_blocked_users) | **GET** /v3/users/{user_id}/block | List blocked users
[**unblock_a_user**](ModerationApi.md#unblock_a_user) | **DELETE** /v3/users/{user_id}/block/{target_id} | Unblock a user


# **block_a_user**
> BlockAUserResponse block_a_user(user_id)

Block a user

## Block a user  A user can block another user if the user doesn't wish to receive any messages or notifications from the blocked user in a 1-to-1 group channel. In a 1-to-N group channel, the user can still receive messages from the blocked user, but this depends on the UI settings of the chat view. In any case, notifications from the blocked user won't be delivered to the 1-to-N group channel. You can choose whether or not the user can view [which users are blocked](https://sendbird.com/docs/chat/platform-api/v3/moderation/listing-blocked-and-blocking-users/list-blocked-and-blocking-users) in the channel UI.  Sendbird application provides two blocking options: include or exclude blocked users when sending invitations, and turn on or off notifications from blocked users. [Explicit and classic block modes](https://sendbird.com/docs/chat/platform-api/v3/deprecated#2-explicit-and-classic-block-modes) have been deprecated and are only supported for customers who started using them before they were deprecated.  - **Include or exclude blocked users when sending invitations**: Determines whether or not to automatically filter out blocked users when a user invites a group of users to a new group channel. By default, blocked users are included when sending invitations. The value of this option can be changed by Sendbird if your Sendbird application isn't integrated with the client app. If you want to change the value, [contact our sales team](https://get.sendbird.com/talk-to-sales.html).      - **Turn on or off notifications from blocked users**: Determines whether or not to receive message notifications from the blocked user in a specific 1-to-N group channel where they are both members. By default, a user doesn't receive notifications from blocked users. The value of this option can be set individually per channel. If you want to use this option, [contact our sales team](https://get.sendbird.com/talk-to-sales.html).  > **Note**: To learn more about other available moderation tools, see [Moderation Overview](https://sendbird.com/docs/chat/platform-api/v3/moderation/moderation-overview#2-actions).  The following tables explain what happens to a user's chat experience when the user blocks another user in a 1-to-1 or 1-to-N group channel. In the case of a 1-to-1 group channel, the block mode is only maintained with the original members. If other than the original members are added, the rules for 1-to-N group channel begin to apply.  [https://sendbird.com/docs/chat/platform-api/v3/moderation/blocking-users/block-users#1-block-users](https://sendbird.com/docs/chat/platform-api/v3/moderation/blocking-users/block-users#1-block-users)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.block_a_user_request import BlockAUserRequest
from sendbird_platform_sdk.model.block_a_user_response import BlockAUserResponse
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
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    block_a_user_request = BlockAUserRequest(
        target_id="target_id_example",
        user_ids=[
            "user_ids_example",
        ],
    ) # BlockAUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Block a user
        api_response = api_instance.block_a_user(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->block_a_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Block a user
        api_response = api_instance.block_a_user(user_id, api_token=api_token, block_a_user_request=block_a_user_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->block_a_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **block_a_user_request** | [**BlockAUserRequest**](BlockAUserRequest.md)|  | [optional]

### Return type

[**BlockAUserResponse**](BlockAUserResponse.md)

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

# **freeze_a_group_channel**
> SendbirdGroupChannelDetail freeze_a_group_channel(channel_url)

Freeze a group channel

## Freeze a group channel  Freezes or unfreezes a group channel.  > **Note**: To learn more about other available moderation tools, see [Moderation Overview](https://sendbird.com/docs/chat/platform-api/v3/moderation/moderation-overview#2-actions).      [https://sendbird.com/docs/chat/platform-api/v3/moderation/freezing-a-channel/freeze-a-group-channel#1-freeze-a-group-channel](https://sendbird.com/docs/chat/platform-api/v3/moderation/freezing-a-channel/freeze-a-group-channel#1-freeze-a-group-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.sendbird_group_channel_detail import SendbirdGroupChannelDetail
from sendbird_platform_sdk.model.freeze_a_group_channel_request import FreezeAGroupChannelRequest
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
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    freeze_a_group_channel_request = FreezeAGroupChannelRequest(
        freeze=True,
    ) # FreezeAGroupChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Freeze a group channel
        api_response = api_instance.freeze_a_group_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->freeze_a_group_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Freeze a group channel
        api_response = api_instance.freeze_a_group_channel(channel_url, api_token=api_token, freeze_a_group_channel_request=freeze_a_group_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->freeze_a_group_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **freeze_a_group_channel_request** | [**FreezeAGroupChannelRequest**](FreezeAGroupChannelRequest.md)|  | [optional]

### Return type

[**SendbirdGroupChannelDetail**](SendbirdGroupChannelDetail.md)

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

# **freeze_an_open_channel**
> SendbirdOpenChannel freeze_an_open_channel(channel_url)

Freeze an open channel

## Freeze an open channel  Freezes or unfreezes an open channel.  > **Note**: To learn more about other available moderation tools, see [Moderation Overview](https://sendbird.com/docs/chat/platform-api/v3/moderation/moderation-overview#2-actions).      [https://sendbird.com/docs/chat/platform-api/v3/moderation/freezing-a-channel/freeze-an-open-channel#1-freeze-an-open-channel](https://sendbird.com/docs/chat/platform-api/v3/moderation/freezing-a-channel/freeze-an-open-channel#1-freeze-an-open-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import moderation_api
from sendbird_platform_sdk.model.freeze_an_open_channel_request import FreezeAnOpenChannelRequest
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
    api_instance = moderation_api.ModerationApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    freeze_an_open_channel_request = FreezeAnOpenChannelRequest(
        freeze=True,
    ) # FreezeAnOpenChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Freeze an open channel
        api_response = api_instance.freeze_an_open_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->freeze_an_open_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Freeze an open channel
        api_response = api_instance.freeze_an_open_channel(channel_url, api_token=api_token, freeze_an_open_channel_request=freeze_an_open_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->freeze_an_open_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **freeze_an_open_channel_request** | [**FreezeAnOpenChannelRequest**](FreezeAnOpenChannelRequest.md)|  | [optional]

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

# **list_blocked_users**
> ListBlockedUsersResponse list_blocked_users(user_id)

List blocked users

## List blocked by and blocking users  This action retrieves a list of users who are either blocked by a specific user or a list of users who are blocking a specific user.  [https://sendbird.com/docs/chat/platform-api/v3/moderation/listing-blocked-and-blocking-users/list-blocked-and-blocking-users#1-list-blocked-by-and-blocking-users](https://sendbird.com/docs/chat/platform-api/v3/moderation/listing-blocked-and-blocking-users/list-blocked-and-blocking-users#1-list-blocked-by-and-blocking-users)  `user_id`   Type: string   Description: Specifies the unique ID of the target user.

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
    user_id = "user_id_example" # str | (Required) 
    list = "blocked_by_me" # str | Specifies whether to retrieve a list of users who are blocked by the specified user or a list of users who are blocking the specified user. Acceptable values are blocked_by_me and blocking_me. The `me` in the values refers to the user specified in the parameter. (Default: blocked_by_me) (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    user_ids = "user_ids_example" # str | Specifies the user IDs of the blocked or blocking users to search for. The value should be a comma-separated string that consists of multiple URL encoded user IDs. (optional)
    metadatakey = "metadatakey_example" # str |  (optional)
    metadatavalues_in = "metadatavalues_in_example" # str |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List blocked users
        api_response = api_instance.list_blocked_users(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->list_blocked_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List blocked users
        api_response = api_instance.list_blocked_users(user_id, list=list, token=token, limit=limit, user_ids=user_ids, metadatakey=metadatakey, metadatavalues_in=metadatavalues_in, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->list_blocked_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **list** | **str**| Specifies whether to retrieve a list of users who are blocked by the specified user or a list of users who are blocking the specified user. Acceptable values are blocked_by_me and blocking_me. The &#x60;me&#x60; in the values refers to the user specified in the parameter. (Default: blocked_by_me) | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **user_ids** | **str**| Specifies the user IDs of the blocked or blocking users to search for. The value should be a comma-separated string that consists of multiple URL encoded user IDs. | [optional]
 **metadatakey** | **str**|  | [optional]
 **metadatavalues_in** | **str**|  | [optional]
 **api_token** | **str**|  | [optional]

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

# **unblock_a_user**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unblock_a_user(user_id, target_id)

Unblock a user

## Unblock a user  Unblocks the user.  https://sendbird.com/docs/chat/platform-api/v3/moderation/blocking-users/unblock-a-user#1-unblock-a-user

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
    user_id = "user_id_example" # str | (Required) 
    target_id = "target_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unblock a user
        api_response = api_instance.unblock_a_user(user_id, target_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->unblock_a_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unblock a user
        api_response = api_instance.unblock_a_user(user_id, target_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ModerationApi->unblock_a_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **target_id** | **str**| (Required)  |
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

