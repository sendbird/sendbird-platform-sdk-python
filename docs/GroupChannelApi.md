# sendbird-platform-sdk.GroupChannelApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gc_accept_invitation**](GroupChannelApi.md#gc_accept_invitation) | **PUT** /v3/group_channels/{channel_url}/accept | Accept an invitation
[**gc_ban_user**](GroupChannelApi.md#gc_ban_user) | **POST** /v3/group_channels/{channel_url}/ban | Ban a user
[**gc_cancel_the_registration_of_operators**](GroupChannelApi.md#gc_cancel_the_registration_of_operators) | **DELETE** /v3/group_channels/{channel_url}/operators | Cancel the registration of operators
[**gc_check_if_member_by_id**](GroupChannelApi.md#gc_check_if_member_by_id) | **GET** /v3/group_channels/{channel_url}/members/{user_id} | Check if member
[**gc_create_channel**](GroupChannelApi.md#gc_create_channel) | **POST** /v3/group_channels | Create a channel
[**gc_decline_invitation**](GroupChannelApi.md#gc_decline_invitation) | **PUT** /v3/group_channels/{channel_url}/decline | Decline an invitation
[**gc_delete_channel_by_url**](GroupChannelApi.md#gc_delete_channel_by_url) | **DELETE** /v3/group_channels/{channel_url} | Delete a channel
[**gc_freeze_channel**](GroupChannelApi.md#gc_freeze_channel) | **PUT** /v3/group_channels/{channel_url}/freeze | Freeze a channel
[**gc_hide_or_archive_channel**](GroupChannelApi.md#gc_hide_or_archive_channel) | **PUT** /v3/group_channels/{channel_url}/hide | Hide or archive a channel
[**gc_invite_as_members**](GroupChannelApi.md#gc_invite_as_members) | **POST** /v3/group_channels/{channel_url}/invite | Invite as members
[**gc_join_channel**](GroupChannelApi.md#gc_join_channel) | **PUT** /v3/group_channels/{channel_url}/join | Join a channel
[**gc_leave_channel**](GroupChannelApi.md#gc_leave_channel) | **PUT** /v3/group_channels/{channel_url}/leave | Leave a channel
[**gc_list_banned_users**](GroupChannelApi.md#gc_list_banned_users) | **GET** /v3/group_channels/{channel_url}/ban | List banned users
[**gc_list_channels**](GroupChannelApi.md#gc_list_channels) | **GET** /v3/group_channels | List channels
[**gc_list_members**](GroupChannelApi.md#gc_list_members) | **GET** /v3/group_channels/{channel_url}/members | List members
[**gc_list_muted_users**](GroupChannelApi.md#gc_list_muted_users) | **GET** /v3/group_channels/{channel_url}/mute | List muted users
[**gc_list_operators**](GroupChannelApi.md#gc_list_operators) | **GET** /v3/group_channels/{channel_url}/operators | List operators
[**gc_mute_user**](GroupChannelApi.md#gc_mute_user) | **POST** /v3/group_channels/{channel_url}/mute | Mute a user
[**gc_register_operators**](GroupChannelApi.md#gc_register_operators) | **POST** /v3/group_channels/{channel_url}/operators | Register operators
[**gc_reset_chat_history**](GroupChannelApi.md#gc_reset_chat_history) | **PUT** /v3/group_channels/{channel_url}/reset_user_history | Reset chat history
[**gc_unban_user_by_id**](GroupChannelApi.md#gc_unban_user_by_id) | **DELETE** /v3/group_channels/{channel_url}/ban/{banned_user_id} | Unban a user
[**gc_unhide_or_unarchive_channel**](GroupChannelApi.md#gc_unhide_or_unarchive_channel) | **DELETE** /v3/group_channels/{channel_url}/hide | Unhide or unarchive a channel
[**gc_unmute_user_by_id**](GroupChannelApi.md#gc_unmute_user_by_id) | **DELETE** /v3/group_channels/{channel_url}/mute/{muted_user_id} | Unmute a user
[**gc_update_ban_by_id**](GroupChannelApi.md#gc_update_ban_by_id) | **PUT** /v3/group_channels/{channel_url}/ban/{banned_user_id} | Update a ban
[**gc_update_channel_by_url**](GroupChannelApi.md#gc_update_channel_by_url) | **PUT** /v3/group_channels/{channel_url} | Update a channel
[**gc_view_ban_by_id**](GroupChannelApi.md#gc_view_ban_by_id) | **GET** /v3/group_channels/{channel_url}/ban/{banned_user_id} | View a ban
[**gc_view_channel_by_url**](GroupChannelApi.md#gc_view_channel_by_url) | **GET** /v3/group_channels/{channel_url} | View a channel
[**gc_view_mute_by_id**](GroupChannelApi.md#gc_view_mute_by_id) | **GET** /v3/group_channels/{channel_url}/mute/{muted_user_id} | View a mute


# **gc_accept_invitation**
> SendBirdGroupChannel gc_accept_invitation(channel_url)

Accept an invitation

## Accept an invitation  Accepts an invitation from a [private](#4-private-vs-public) group channel for a user to join. Since a user is allowed to join up to 2,000 group channels, the invitation to a user who already belongs to a maximum number of group channels will be canceled automatically.  > __Note__: This action is effective only when the `auto_accept` property of an application is set to false. You can change the value of the property using the [update default channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference) action, or [update a user's channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference) action.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-accept-an-invitation ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.send_bird_group_channel import SendBirdGroupChannel
from sendbird-platform-sdk.model.gc_accept_invitation_data import GcAcceptInvitationData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_accept_invitation_data = GcAcceptInvitationData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        access_code="access_code_example",
    ) # GcAcceptInvitationData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept an invitation
        api_response = api_instance.gc_accept_invitation(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_accept_invitation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept an invitation
        api_response = api_instance.gc_accept_invitation(channel_url, api_token=api_token, gc_accept_invitation_data=gc_accept_invitation_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_accept_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_accept_invitation_data** | [**GcAcceptInvitationData**](GcAcceptInvitationData.md)|  | [optional]

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

# **gc_ban_user**
> InlineResponse20033BannedList gc_ban_user(channel_url)

Ban a user

## Ban a user  Bans a user from a group channel. A banned user is immediately expelled from a channel and allowed to join the channel again after a set time period.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-ban-a-user ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.gc_ban_user_data import GcBanUserData
from sendbird-platform-sdk.model.inline_response20033_banned_list import InlineResponse20033BannedList
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
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
        api_response = api_instance.gc_ban_user(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_ban_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ban a user
        api_response = api_instance.gc_ban_user(channel_url, api_token=api_token, gc_ban_user_data=gc_ban_user_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_ban_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_ban_user_data** | [**GcBanUserData**](GcBanUserData.md)|  | [optional]

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

# **gc_cancel_the_registration_of_operators**
> gc_cancel_the_registration_of_operators(channel_url, operator_ids)

Cancel the registration of operators

## Cancel the registration of operators  Cancels the registration of operators from a group channel but leave them as members.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-cancel-the-registration-of-operators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to cancel the registration of operators.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    operator_ids = [
        "operator_ids_example",
    ] # [str] | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    delete_all = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel the registration of operators
        api_instance.gc_cancel_the_registration_of_operators(channel_url, operator_ids)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_cancel_the_registration_of_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel the registration of operators
        api_instance.gc_cancel_the_registration_of_operators(channel_url, operator_ids, api_token=api_token, delete_all=delete_all)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_cancel_the_registration_of_operators: %s\n" % e)
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

# **gc_check_if_member_by_id**
> InlineResponse20037 gc_check_if_member_by_id(channel_url, user_id)

Check if member

## Check if member  Checks whether the user is a member of the group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-check-if-member ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.inline_response20037 import InlineResponse20037
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Check if member
        api_response = api_instance.gc_check_if_member_by_id(channel_url, user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_check_if_member_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check if member
        api_response = api_instance.gc_check_if_member_by_id(channel_url, user_id, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_check_if_member_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

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

# **gc_create_channel**
> SendBirdGroupChannel gc_create_channel()

Create a channel

## Create a channel  Creates a new group channel.  > If you are creating a 1-on-1 direct messaging channel for a user, it is recommended that you turn on the `distinct` property. If the property is turned off, a user can create a new channel even if they have had the previous chat between them, and therefore can't see previously sent messages or data in the new channel. On the other hand, if the `distinct` property is turned on, every 1-on-1 conversation between the same two users occurs within the same channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-create-a-channel

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.gc_create_channel_data import GcCreateChannelData
from sendbird-platform-sdk.model.send_bird_group_channel import SendBirdGroupChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_create_channel_data = GcCreateChannelData(
        user_ids=[
            1,
        ],
        users=[
            1,
        ],
        name="name_example",
        channel_url="channel_url_example",
        cover_url="cover_url_example",
        cover_file=open('/path/to/file', 'rb'),
        custom_type="custom_type_example",
        data="data_example",
        is_distinct=True,
        is_public=True,
        is_super=True,
        is_ephemeral=True,
        access_code="access_code_example",
        inviter_id="inviter_id_example",
        strict=True,
        invitation_status=[
            "invitation_status_example",
        ],
        hidden_status=[
            "hidden_status_example",
        ],
        operator_ids=[
            1,
        ],
        block_sdk_user_channel_join=True,
    ) # GcCreateChannelData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a channel
        api_response = api_instance.gc_create_channel(api_token=api_token, gc_create_channel_data=gc_create_channel_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_create_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **gc_create_channel_data** | [**GcCreateChannelData**](GcCreateChannelData.md)|  | [optional]

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

# **gc_decline_invitation**
> gc_decline_invitation(channel_url)

Decline an invitation

## Decline an invitation  Declines an invitation for a user to not join a [private](#4-private-vs-public) group channel.  > __Note__: This action is effective only when the `auto_accept` property of an application is set to false. You can change the value of the property using the [update default channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference) action, or [update a user's channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference) action.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-decline-an-invitation ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.gc_decline_invitation_data import GcDeclineInvitationData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_decline_invitation_data = GcDeclineInvitationData(
        channel_url="channel_url_example",
        user_id="user_id_example",
    ) # GcDeclineInvitationData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Decline an invitation
        api_instance.gc_decline_invitation(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_decline_invitation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Decline an invitation
        api_instance.gc_decline_invitation(channel_url, api_token=api_token, gc_decline_invitation_data=gc_decline_invitation_data)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_decline_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_decline_invitation_data** | [**GcDeclineInvitationData**](GcDeclineInvitationData.md)|  | [optional]

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

# **gc_delete_channel_by_url**
> gc_delete_channel_by_url(channel_url)

Delete a channel

## Delete a channel  Deletes a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-delete-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel
        api_instance.gc_delete_channel_by_url(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_delete_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a channel
        api_instance.gc_delete_channel_by_url(channel_url, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_delete_channel_by_url: %s\n" % e)
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

# **gc_freeze_channel**
> SendBirdGroupChannel gc_freeze_channel(channel_url)

Freeze a channel

## Freeze a channel  Freezes or unfreezes a group channel.  > __Note__: Only users designated as channel operators are allowed to talk when a channel is frozen.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-freeze-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.send_bird_group_channel import SendBirdGroupChannel
from sendbird-platform-sdk.model.gc_freeze_channel_data import GcFreezeChannelData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_freeze_channel_data = GcFreezeChannelData(
        channel_url="channel_url_example",
        freeze=True,
    ) # GcFreezeChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Freeze a channel
        api_response = api_instance.gc_freeze_channel(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_freeze_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Freeze a channel
        api_response = api_instance.gc_freeze_channel(channel_url, api_token=api_token, gc_freeze_channel_data=gc_freeze_channel_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_freeze_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
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

# **gc_hide_or_archive_channel**
> gc_hide_or_archive_channel(channel_url)

Hide or archive a channel

## Hide or archive a channel  Hides or archives a channel from the channel list of either a specific user or entire channel members. Normally, a hidden channel comes back and shows up in the channel list when a member in the channel sends a new message. This automatically-triggered behavior is intended for users who want to temporarily remove a channel from their list because [leaving the channel](#2-leave-the-channel) would delete all the past messages and stored data.  You can also leave out a channel from the list and archive the channel. The channel doesn't appear even when receiving a new message from other member.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-hide-or-archive-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.gc_hide_or_archive_channel_data import GcHideOrArchiveChannelData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_hide_or_archive_channel_data = GcHideOrArchiveChannelData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        allow_auto_unhide=True,
        should_hide_all=True,
        hide_previous_messages=True,
    ) # GcHideOrArchiveChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Hide or archive a channel
        api_instance.gc_hide_or_archive_channel(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_hide_or_archive_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Hide or archive a channel
        api_instance.gc_hide_or_archive_channel(channel_url, api_token=api_token, gc_hide_or_archive_channel_data=gc_hide_or_archive_channel_data)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_hide_or_archive_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_hide_or_archive_channel_data** | [**GcHideOrArchiveChannelData**](GcHideOrArchiveChannelData.md)|  | [optional]

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

# **gc_invite_as_members**
> SendBirdGroupChannel gc_invite_as_members(channel_url)

Invite as members

## Invite as members  Invites one or more users as members into the group channel.  > __Note__: By default, users in your application automatically join a [private](#4-private-vs-public) group channel promptly from an invitation without having to accept it. If you want to give them the option to decide whether to accept or decline an invitation, you should set the value of channel invitation preference to false through the [update default channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference) action. Or using the [update a user's channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference) action, you can also allow the option individually by user.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-invite-as-members ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.send_bird_group_channel import SendBirdGroupChannel
from sendbird-platform-sdk.model.gc_invite_as_members_data import GcInviteAsMembersData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_invite_as_members_data = GcInviteAsMembersData(
        channel_url="channel_url_example",
        user_ids=[
            1,
        ],
        users=[
            1,
        ],
        invitation_status=[
            "invitation_status_example",
        ],
        hidden_status=[
            "hidden_status_example",
        ],
    ) # GcInviteAsMembersData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Invite as members
        api_response = api_instance.gc_invite_as_members(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_invite_as_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Invite as members
        api_response = api_instance.gc_invite_as_members(channel_url, api_token=api_token, gc_invite_as_members_data=gc_invite_as_members_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_invite_as_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_invite_as_members_data** | [**GcInviteAsMembersData**](GcInviteAsMembersData.md)|  | [optional]

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

# **gc_join_channel**
> gc_join_channel(channel_url)

Join a channel

## Join a channel  Allows a user to join a [public](#4-private-vs-public) group channel. Since a user is allowed to join up to 2,000 group channels, a user who already belongs to a maximum number of group channels can't join a new channel.  > __Note__: This action is only permitted for public group channels where the `is_public` property is true.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-join-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.gc_join_channel_data import GcJoinChannelData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_join_channel_data = GcJoinChannelData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        access_code="access_code_example",
    ) # GcJoinChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Join a channel
        api_instance.gc_join_channel(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_join_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Join a channel
        api_instance.gc_join_channel(channel_url, api_token=api_token, gc_join_channel_data=gc_join_channel_data)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_join_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_join_channel_data** | [**GcJoinChannelData**](GcJoinChannelData.md)|  | [optional]

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

# **gc_leave_channel**
> gc_leave_channel(channel_url)

Leave a channel

## Leave a channel  Makes one or more members leave a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-leave-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.gc_leave_channel_data import GcLeaveChannelData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_leave_channel_data = GcLeaveChannelData(
        channel_url="channel_url_example",
        user_ids=[
            1,
        ],
        should_leave_all=True,
    ) # GcLeaveChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Leave a channel
        api_instance.gc_leave_channel(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_leave_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Leave a channel
        api_instance.gc_leave_channel(channel_url, api_token=api_token, gc_leave_channel_data=gc_leave_channel_data)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_leave_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_leave_channel_data** | [**GcLeaveChannelData**](GcLeaveChannelData.md)|  | [optional]

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

# **gc_list_banned_users**
> InlineResponse20033 gc_list_banned_users(channel_url)

List banned users

## List banned users  Retrieves a list of the banned users from a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-banned-users ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel where to retrieve a list of banned users.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List banned users
        api_response = api_instance.gc_list_banned_users(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_banned_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List banned users
        api_response = api_instance.gc_list_banned_users(channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_banned_users: %s\n" % e)
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

# **gc_list_channels**
> InlineResponse20017 gc_list_channels()

List channels

## List channels  Retrieves a list of group channels in the application.  > __Note__: If you want to get a list of a specific user's group channels, use the [list my group channels](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-list-my-group-channels) action instead.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-channels ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.inline_response20017 import InlineResponse20017
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    distinct_mode = "distinct_mode_example" # str |  (optional)
    public_mode = "public_mode_example" # str |  (optional)
    super_mode = "super_mode_example" # str |  (optional)
    created_after = 1 # int |  (optional)
    created_before = 1 # int |  (optional)
    show_empty = True # bool |  (optional)
    show_member = True # bool |  (optional)
    show_delivery_receipt = True # bool |  (optional)
    show_read_receipt = True # bool |  (optional)
    show_metadata = True # bool |  (optional)
    show_frozen = True # bool |  (optional)
    order = "order_example" # str |  (optional)
    metadata_order_key = "metadata_order_key_example" # str |  (optional)
    custom_types = "custom_types_example" # str |  (optional)
    custom_type_startswith = "custom_type_startswith_example" # str |  (optional)
    channel_urls = "channel_urls_example" # str |  (optional)
    name = "name_example" # str |  (optional)
    name_contains = "name_contains_example" # str |  (optional)
    name_startswith = "name_startswith_example" # str |  (optional)
    members_exactly_in = "members_exactly_in_example" # str |  (optional)
    members_include_in = "members_include_in_example" # str |  (optional)
    query_type = "query_type_example" # str |  (optional)
    members_nickname = "members_nickname_example" # str |  (optional)
    members_nickname_contains = "members_nickname_contains_example" # str |  (optional)
    metadata_key = "metadata_key_example" # str |  (optional)
    metadata_values = "metadata_values_example" # str |  (optional)
    metadata_value_startswith = "metadata_value_startswith_example" # str |  (optional)
    metacounter_key = "metacounter_key_example" # str |  (optional)
    metacounter_values = "metacounter_values_example" # str |  (optional)
    metacounter_value_gt = "metacounter_value_gt_example" # str |  (optional)
    metacounter_value_gte = "metacounter_value_gte_example" # str |  (optional)
    metacounter_value_lt = "metacounter_value_lt_example" # str |  (optional)
    metacounter_value_lte = "metacounter_value_lte_example" # str |  (optional)
    include_sorted_metaarray_in_last_message = True # bool |  (optional)
    custom_type = "custom_type_example" # str |  (optional)
    read_receipt = True # bool |  (optional)
    member = True # bool |  (optional)
    is_distinct = True # bool |  (optional)
    members_in = "members_in_example" # str |  (optional)
    user_id = "user_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List channels
        api_response = api_instance.gc_list_channels(api_token=api_token, token=token, limit=limit, distinct_mode=distinct_mode, public_mode=public_mode, super_mode=super_mode, created_after=created_after, created_before=created_before, show_empty=show_empty, show_member=show_member, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, show_metadata=show_metadata, show_frozen=show_frozen, order=order, metadata_order_key=metadata_order_key, custom_types=custom_types, custom_type_startswith=custom_type_startswith, channel_urls=channel_urls, name=name, name_contains=name_contains, name_startswith=name_startswith, members_exactly_in=members_exactly_in, members_include_in=members_include_in, query_type=query_type, members_nickname=members_nickname, members_nickname_contains=members_nickname_contains, metadata_key=metadata_key, metadata_values=metadata_values, metadata_value_startswith=metadata_value_startswith, metacounter_key=metacounter_key, metacounter_values=metacounter_values, metacounter_value_gt=metacounter_value_gt, metacounter_value_gte=metacounter_value_gte, metacounter_value_lt=metacounter_value_lt, metacounter_value_lte=metacounter_value_lte, include_sorted_metaarray_in_last_message=include_sorted_metaarray_in_last_message, custom_type=custom_type, read_receipt=read_receipt, member=member, is_distinct=is_distinct, members_in=members_in, user_id=user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **distinct_mode** | **str**|  | [optional]
 **public_mode** | **str**|  | [optional]
 **super_mode** | **str**|  | [optional]
 **created_after** | **int**|  | [optional]
 **created_before** | **int**|  | [optional]
 **show_empty** | **bool**|  | [optional]
 **show_member** | **bool**|  | [optional]
 **show_delivery_receipt** | **bool**|  | [optional]
 **show_read_receipt** | **bool**|  | [optional]
 **show_metadata** | **bool**|  | [optional]
 **show_frozen** | **bool**|  | [optional]
 **order** | **str**|  | [optional]
 **metadata_order_key** | **str**|  | [optional]
 **custom_types** | **str**|  | [optional]
 **custom_type_startswith** | **str**|  | [optional]
 **channel_urls** | **str**|  | [optional]
 **name** | **str**|  | [optional]
 **name_contains** | **str**|  | [optional]
 **name_startswith** | **str**|  | [optional]
 **members_exactly_in** | **str**|  | [optional]
 **members_include_in** | **str**|  | [optional]
 **query_type** | **str**|  | [optional]
 **members_nickname** | **str**|  | [optional]
 **members_nickname_contains** | **str**|  | [optional]
 **metadata_key** | **str**|  | [optional]
 **metadata_values** | **str**|  | [optional]
 **metadata_value_startswith** | **str**|  | [optional]
 **metacounter_key** | **str**|  | [optional]
 **metacounter_values** | **str**|  | [optional]
 **metacounter_value_gt** | **str**|  | [optional]
 **metacounter_value_gte** | **str**|  | [optional]
 **metacounter_value_lt** | **str**|  | [optional]
 **metacounter_value_lte** | **str**|  | [optional]
 **include_sorted_metaarray_in_last_message** | **bool**|  | [optional]
 **custom_type** | **str**|  | [optional]
 **read_receipt** | **bool**|  | [optional]
 **member** | **bool**|  | [optional]
 **is_distinct** | **bool**|  | [optional]
 **members_in** | **str**|  | [optional]
 **user_id** | **str**|  | [optional]

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

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

# **gc_list_members**
> InlineResponse20036 gc_list_members(channel_url)

List members

## List members  Retrieves a list of members of a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-members ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of members of.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.inline_response20036 import InlineResponse20036
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    show_delivery_receipt = True # bool |  (optional)
    show_read_receipt = True # bool |  (optional)
    order = "order_example" # str |  (optional)
    operator_filter = "operator_filter_example" # str |  (optional)
    member_state_filter = "member_state_filter_example" # str |  (optional)
    muted_member_filter = "muted_member_filter_example" # str |  (optional)
    nickname_startswith = "nickname_startswith_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List members
        api_response = api_instance.gc_list_members(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List members
        api_response = api_instance.gc_list_members(channel_url, api_token=api_token, token=token, limit=limit, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, order=order, operator_filter=operator_filter, member_state_filter=member_state_filter, muted_member_filter=muted_member_filter, nickname_startswith=nickname_startswith)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **show_delivery_receipt** | **bool**|  | [optional]
 **show_read_receipt** | **bool**|  | [optional]
 **order** | **str**|  | [optional]
 **operator_filter** | **str**|  | [optional]
 **member_state_filter** | **str**|  | [optional]
 **muted_member_filter** | **str**|  | [optional]
 **nickname_startswith** | **str**|  | [optional]

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

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
> InlineResponse20031 gc_list_muted_users(channel_url)

List muted users

## List muted users  Retrieves a list of the muted users in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-muted-users ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of muted users.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List muted users
        api_response = api_instance.gc_list_muted_users(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_muted_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List muted users
        api_response = api_instance.gc_list_muted_users(channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_muted_users: %s\n" % e)
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

# **gc_list_operators**
> InlineResponse20034 gc_list_operators(channel_url)

List operators

## List operators  Retrieves a list of operators of a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-operators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of operators.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List operators
        api_response = api_instance.gc_list_operators(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List operators
        api_response = api_instance.gc_list_operators(channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_operators: %s\n" % e)
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

# **gc_mute_user**
> SendBirdGroupChannel gc_mute_user(channel_url)

Mute a user

## Mute a user  Mutes a user in a group channel. A muted user remains in the channel and is allowed to view the messages, but can't send any messages until unmuted.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-mute-a-user ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.send_bird_group_channel import SendBirdGroupChannel
from sendbird-platform-sdk.model.gc_mute_user_data import GcMuteUserData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_mute_user_data = GcMuteUserData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        seconds=1,
        description="description_example",
    ) # GcMuteUserData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mute a user
        api_response = api_instance.gc_mute_user(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_mute_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mute a user
        api_response = api_instance.gc_mute_user(channel_url, api_token=api_token, gc_mute_user_data=gc_mute_user_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_mute_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
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

# **gc_register_operators**
> InlineResponse20038 gc_register_operators(channel_url)

Register operators

## Register operators  Registers one or more operators to a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-register-operators ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.gc_register_operators_data import GcRegisterOperatorsData
from sendbird-platform-sdk.model.inline_response20038 import InlineResponse20038
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_register_operators_data = GcRegisterOperatorsData(
        channel_url="channel_url_example",
        operator_ids=[
            1,
        ],
    ) # GcRegisterOperatorsData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register operators
        api_response = api_instance.gc_register_operators(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_register_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register operators
        api_response = api_instance.gc_register_operators(channel_url, api_token=api_token, gc_register_operators_data=gc_register_operators_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_register_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_register_operators_data** | [**GcRegisterOperatorsData**](GcRegisterOperatorsData.md)|  | [optional]

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

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

# **gc_reset_chat_history**
> gc_reset_chat_history(channel_url)

Reset chat history

## Reset chat history  Resets the properties related to a user's chat history in a group channel, then clears the existing messages in the channel on the user's side only. A user can no longer see the messages in a group channel once this action is called, but those messages are not deleted from the database of the Sendbird system. All other members in the channel can retrieve and see the messages.  This action simply clears the messages for the user by updating the `last_message` and `read_receipt` properties of the [channel](#2-types-of-a-channel-3-resource-representation) resource in addition to other internally managed data such as the number of the user's unread message.  Using the `reset_all` property, you can also reset the properties related to all users' chat history in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-reset-chat-history ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.gc_reset_chat_history_data import GcResetChatHistoryData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_reset_chat_history_data = GcResetChatHistoryData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        reset_all=True,
    ) # GcResetChatHistoryData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset chat history
        api_instance.gc_reset_chat_history(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_reset_chat_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset chat history
        api_instance.gc_reset_chat_history(channel_url, api_token=api_token, gc_reset_chat_history_data=gc_reset_chat_history_data)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_reset_chat_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_reset_chat_history_data** | [**GcResetChatHistoryData**](GcResetChatHistoryData.md)|  | [optional]

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

# **gc_unban_user_by_id**
> gc_unban_user_by_id(channel_url, banned_user_id)

Unban a user

## Unban a user  Unbans a user from a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-unban-a-user ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unban a user
        api_instance.gc_unban_user_by_id(channel_url, banned_user_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_unban_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unban a user
        api_instance.gc_unban_user_by_id(channel_url, banned_user_id, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_unban_user_by_id: %s\n" % e)
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

# **gc_unhide_or_unarchive_channel**
> gc_unhide_or_unarchive_channel(channel_url, user_id)

Unhide or unarchive a channel

## Unhide or unarchive a channel  Makes a hidden or archived channel reappear in the channel list of either a specific user or entire channel members.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-unhide-or-unarchive-a-channel ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to unhide or unarchive.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    should_unhide_all = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unhide or unarchive a channel
        api_instance.gc_unhide_or_unarchive_channel(channel_url, user_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_unhide_or_unarchive_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unhide or unarchive a channel
        api_instance.gc_unhide_or_unarchive_channel(channel_url, user_id, api_token=api_token, should_unhide_all=should_unhide_all)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_unhide_or_unarchive_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **should_unhide_all** | **bool**|  | [optional]

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

# **gc_unmute_user_by_id**
> gc_unmute_user_by_id(channel_url, muted_user_id)

Unmute a user

## Unmute a user  Unmutes a user within a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-unmute-a-user ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    muted_user_id = "muted_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unmute a user
        api_instance.gc_unmute_user_by_id(channel_url, muted_user_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_unmute_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unmute a user
        api_instance.gc_unmute_user_by_id(channel_url, muted_user_id, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_unmute_user_by_id: %s\n" % e)
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

# **gc_update_ban_by_id**
> SendBirdUser gc_update_ban_by_id(channel_url, banned_user_id)

Update a ban

## Update a ban  Updates details of a ban imposed on a user. You can change the length of the ban with this action, and also provide an updated description.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-update-a-ban ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.send_bird_user import SendBirdUser
from sendbird-platform-sdk.model.gc_update_ban_by_id_data import GcUpdateBanByIdData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_update_ban_by_id_data = GcUpdateBanByIdData(
        channel_url="channel_url_example",
        banned_user_id="banned_user_id_example",
        seconds=1,
        description="description_example",
    ) # GcUpdateBanByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a ban
        api_response = api_instance.gc_update_ban_by_id(channel_url, banned_user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_update_ban_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a ban
        api_response = api_instance.gc_update_ban_by_id(channel_url, banned_user_id, api_token=api_token, gc_update_ban_by_id_data=gc_update_ban_by_id_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_update_ban_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **banned_user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_update_ban_by_id_data** | [**GcUpdateBanByIdData**](GcUpdateBanByIdData.md)|  | [optional]

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

# **gc_update_channel_by_url**
> SendBirdGroupChannel gc_update_channel_by_url(channel_url)

Update a channel

## Update a channel  Updates information on a group channel.  > __Note__: You can't change the members of the channel here. To do so, see [invite as members](#2-invite-as-members) action below.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-update-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.send_bird_group_channel import SendBirdGroupChannel
from sendbird-platform-sdk.model.gc_update_channel_by_url_data import GcUpdateChannelByUrlData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_update_channel_by_url_data = GcUpdateChannelByUrlData(
        channel_url="channel_url_example",
        name="name_example",
        cover_url="cover_url_example",
        cover_file=open('/path/to/file', 'rb'),
        custom_type="custom_type_example",
        data="data_example",
        is_distinct=True,
        is_public=True,
        access_code="access_code_example",
        operator_ids=[
            1,
        ],
    ) # GcUpdateChannelByUrlData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel
        api_response = api_instance.gc_update_channel_by_url(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_update_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel
        api_response = api_instance.gc_update_channel_by_url(channel_url, api_token=api_token, gc_update_channel_by_url_data=gc_update_channel_by_url_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_update_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_update_channel_by_url_data** | [**GcUpdateChannelByUrlData**](GcUpdateChannelByUrlData.md)|  | [optional]

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

# **gc_view_ban_by_id**
> SendBirdUser gc_view_ban_by_id(channel_url, banned_user_id)

View a ban

## View a ban  Retrieves details of a ban imposed on a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-view-a-ban ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    banned_user_id = "banned_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a ban
        api_response = api_instance.gc_view_ban_by_id(channel_url, banned_user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_view_ban_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a ban
        api_response = api_instance.gc_view_ban_by_id(channel_url, banned_user_id, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_view_ban_by_id: %s\n" % e)
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

# **gc_view_channel_by_url**
> SendBirdGroupChannel gc_view_channel_by_url(channel_url)

View a channel

## View a channel  Retrieves information on a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-view-a-channel ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
from sendbird-platform-sdk.model.send_bird_group_channel import SendBirdGroupChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    show_delivery_receipt = True # bool |  (optional)
    show_read_receipt = True # bool |  (optional)
    show_member = True # bool |  (optional)
    read_receipt = True # bool |  (optional)
    member = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel
        api_response = api_instance.gc_view_channel_by_url(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_view_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel
        api_response = api_instance.gc_view_channel_by_url(channel_url, api_token=api_token, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, show_member=show_member, read_receipt=read_receipt, member=member)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_view_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **show_delivery_receipt** | **bool**|  | [optional]
 **show_read_receipt** | **bool**|  | [optional]
 **show_member** | **bool**|  | [optional]
 **read_receipt** | **bool**|  | [optional]
 **member** | **bool**|  | [optional]

### Return type

[**SendBirdGroupChannel**](SendBirdGroupChannel.md)

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
> InlineResponse20035 gc_view_mute_by_id(channel_url, muted_user_id)

View a mute

## View a mute  Checks if a user is muted in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-view-a-mute ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    muted_user_id = "muted_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a mute
        api_response = api_instance.gc_view_mute_by_id(channel_url, muted_user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_view_mute_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a mute
        api_response = api_instance.gc_view_mute_by_id(channel_url, muted_user_id, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_view_mute_by_id: %s\n" % e)
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

