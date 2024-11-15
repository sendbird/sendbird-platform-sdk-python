# sendbird_platform_sdk.GroupChannelApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gc_accept_invitation**](GroupChannelApi.md#gc_accept_invitation) | **PUT** /v3/group_channels/{channel_url}/accept | Accept an invitation
[**gc_cancel_the_registration_of_operators**](GroupChannelApi.md#gc_cancel_the_registration_of_operators) | **DELETE** /v3/group_channels/{channel_url}/operators | Cancel the registration of operators
[**gc_check_if_member_by_id**](GroupChannelApi.md#gc_check_if_member_by_id) | **GET** /v3/group_channels/{channel_url}/members/{user_id} | Check if member
[**gc_create_channel**](GroupChannelApi.md#gc_create_channel) | **POST** /v3/group_channels | Create a channel
[**gc_decline_invitation**](GroupChannelApi.md#gc_decline_invitation) | **PUT** /v3/group_channels/{channel_url}/decline | Decline an invitation
[**gc_delete_channel_by_url**](GroupChannelApi.md#gc_delete_channel_by_url) | **DELETE** /v3/group_channels/{channel_url} | Delete a channel
[**gc_hide_or_archive_channel**](GroupChannelApi.md#gc_hide_or_archive_channel) | **PUT** /v3/group_channels/{channel_url}/hide | Hide or archive a channel
[**gc_invite_as_members**](GroupChannelApi.md#gc_invite_as_members) | **POST** /v3/group_channels/{channel_url}/invite | Invite as members
[**gc_join_channel**](GroupChannelApi.md#gc_join_channel) | **PUT** /v3/group_channels/{channel_url}/join | Join a channel
[**gc_leave_channel**](GroupChannelApi.md#gc_leave_channel) | **PUT** /v3/group_channels/{channel_url}/leave | Leave a channel
[**gc_list_channels**](GroupChannelApi.md#gc_list_channels) | **GET** /v3/group_channels | List channels
[**gc_list_members**](GroupChannelApi.md#gc_list_members) | **GET** /v3/group_channels/{channel_url}/members | List members
[**gc_list_operators**](GroupChannelApi.md#gc_list_operators) | **GET** /v3/group_channels/{channel_url}/operators | List operators
[**gc_register_operators**](GroupChannelApi.md#gc_register_operators) | **POST** /v3/group_channels/{channel_url}/operators | Register operators
[**gc_reset_chat_history**](GroupChannelApi.md#gc_reset_chat_history) | **PUT** /v3/group_channels/{channel_url}/reset_user_history | Reset chat history
[**gc_start_typing_indicators**](GroupChannelApi.md#gc_start_typing_indicators) | **POST** /v3/group_channels/{channel_url}/typing | Start typing indicators
[**gc_stop_typing_indicators**](GroupChannelApi.md#gc_stop_typing_indicators) | **DELETE** /v3/group_channels/{channel_url}/typing | Stop typing indicators
[**gc_unhide_or_unarchive_channel**](GroupChannelApi.md#gc_unhide_or_unarchive_channel) | **DELETE** /v3/group_channels/{channel_url}/hide | Unhide or unarchive a channel
[**gc_update_channel_by_url**](GroupChannelApi.md#gc_update_channel_by_url) | **PUT** /v3/group_channels/{channel_url} | Update a channel
[**gc_view_channel_by_url**](GroupChannelApi.md#gc_view_channel_by_url) | **GET** /v3/group_channels/{channel_url} | View a channel


# **gc_accept_invitation**
> SendBirdGroupChannel gc_accept_invitation(channel_url)

Accept an invitation

## Accept an invitation  Accepts an invitation from a [private](#4-private-vs-public) group channel for a user to join. Since a user is allowed to join up to 2,000 group channels, the invitation to a user who already belongs to a maximum number of group channels will be canceled automatically.  > __Note__: This action is effective only when the `auto_accept` property of an application is set to false. You can change the value of the property using the [update default channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference) action, or [update a user's channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference) action.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-accept-an-invitation ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_accept_invitation_data import GcAcceptInvitationData
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
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_accept_invitation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept an invitation
        api_response = api_instance.gc_accept_invitation(channel_url, api_token=api_token, gc_accept_invitation_data=gc_accept_invitation_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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

# **gc_cancel_the_registration_of_operators**
> OcDeleteChannelByUrl200Response gc_cancel_the_registration_of_operators(channel_url, operator_ids)

Cancel the registration of operators

## Cancel the registration of operators  Cancels the registration of operators from a group channel but leave them as members.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-cancel-the-registration-of-operators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to cancel the registration of operators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
        api_response = api_instance.gc_cancel_the_registration_of_operators(channel_url, operator_ids)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_cancel_the_registration_of_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel the registration of operators
        api_response = api_instance.gc_cancel_the_registration_of_operators(channel_url, operator_ids, api_token=api_token, delete_all=delete_all)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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

# **gc_check_if_member_by_id**
> GcCheckIfMemberByIdResponse gc_check_if_member_by_id(channel_url, user_id)

Check if member

## Check if member  Checks whether the user is a member of the group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-check-if-member ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_check_if_member_by_id_response import GcCheckIfMemberByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
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
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_check_if_member_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check if member
        api_response = api_instance.gc_check_if_member_by_id(channel_url, user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_check_if_member_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**GcCheckIfMemberByIdResponse**](GcCheckIfMemberByIdResponse.md)

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
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_create_channel_data import GcCreateChannelData
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_create_channel_data = GcCreateChannelData(
        user_ids=[
            "user_ids_example",
        ],
        users=[
            SendBirdUser(
                require_auth_for_profile_image=True,
                is_online=True,
                user_id="user_id_example",
                access_token="access_token_example",
                has_ever_logged_in=True,
                is_active=True,
                last_seen_at=1,
                nickname="nickname_example",
                discovery_keys=[
                    "discovery_keys_example",
                ],
                session_tokens=[
                    {},
                ],
                preferred_languages=[
                    "preferred_languages_example",
                ],
                profile_url="profile_url_example",
                created_at=1,
                phone_number="phone_number_example",
                local="local_example",
                locale="locale_example",
                is_hide_me_from_friends=True,
                is_shadow_blocked=True,
                is_created=True,
                metadata={},
                description="description_example",
                end_at=1,
                start_at=1,
            ),
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
        invitation_status={},
        hidden_status={},
        operator_ids=[
            "operator_ids_example",
        ],
        block_sdk_user_channel_join=True,
    ) # GcCreateChannelData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a channel
        api_response = api_instance.gc_create_channel(api_token=api_token, gc_create_channel_data=gc_create_channel_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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
> OcDeleteChannelByUrl200Response gc_decline_invitation(channel_url)

Decline an invitation

## Decline an invitation  Declines an invitation for a user to not join a [private](#4-private-vs-public) group channel.  > __Note__: This action is effective only when the `auto_accept` property of an application is set to false. You can change the value of the property using the [update default channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference) action, or [update a user's channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference) action.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-decline-an-invitation ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_decline_invitation_data import GcDeclineInvitationData
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
        api_response = api_instance.gc_decline_invitation(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_decline_invitation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Decline an invitation
        api_response = api_instance.gc_decline_invitation(channel_url, api_token=api_token, gc_decline_invitation_data=gc_decline_invitation_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_decline_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_decline_invitation_data** | [**GcDeclineInvitationData**](GcDeclineInvitationData.md)|  | [optional]

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

# **gc_delete_channel_by_url**
> OcDeleteChannelByUrl200Response gc_delete_channel_by_url(channel_url)

Delete a channel

## Delete a channel  Deletes a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-delete-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel
        api_response = api_instance.gc_delete_channel_by_url(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_delete_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a channel
        api_response = api_instance.gc_delete_channel_by_url(channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_delete_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]

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

# **gc_hide_or_archive_channel**
> OcDeleteChannelByUrl200Response gc_hide_or_archive_channel(channel_url)

Hide or archive a channel

## Hide or archive a channel  Hides or archives a channel from the channel list of either a specific user or entire channel members. Normally, a hidden channel comes back and shows up in the channel list when a member in the channel sends a new message. This automatically-triggered behavior is intended for users who want to temporarily remove a channel from their list because [leaving the channel](#2-leave-the-channel) would delete all the past messages and stored data.  You can also leave out a channel from the list and archive the channel. The channel doesn't appear even when receiving a new message from other member.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-hide-or-archive-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_hide_or_archive_channel_data import GcHideOrArchiveChannelData
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
        api_response = api_instance.gc_hide_or_archive_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_hide_or_archive_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Hide or archive a channel
        api_response = api_instance.gc_hide_or_archive_channel(channel_url, api_token=api_token, gc_hide_or_archive_channel_data=gc_hide_or_archive_channel_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_hide_or_archive_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_hide_or_archive_channel_data** | [**GcHideOrArchiveChannelData**](GcHideOrArchiveChannelData.md)|  | [optional]

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

# **gc_invite_as_members**
> SendBirdGroupChannel gc_invite_as_members(channel_url)

Invite as members

## Invite as members  Invites one or more users as members into the group channel.  > __Note__: By default, users in your application automatically join a [private](#4-private-vs-public) group channel promptly from an invitation without having to accept it. If you want to give them the option to decide whether to accept or decline an invitation, you should set the value of channel invitation preference to false through the [update default channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference) action. Or using the [update a user's channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference) action, you can also allow the option individually by user.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-invite-as-members ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_invite_as_members_data import GcInviteAsMembersData
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_invite_as_members_data = GcInviteAsMembersData(
        channel_url="channel_url_example",
        user_ids=[
            "user_ids_example",
        ],
        users=[
            "users_example",
        ],
        invitation_status={},
        hidden_status={},
    ) # GcInviteAsMembersData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Invite as members
        api_response = api_instance.gc_invite_as_members(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_invite_as_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Invite as members
        api_response = api_instance.gc_invite_as_members(channel_url, api_token=api_token, gc_invite_as_members_data=gc_invite_as_members_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_join_channel_data import GcJoinChannelData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
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
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_join_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Join a channel
        api_instance.gc_join_channel(channel_url, api_token=api_token, gc_join_channel_data=gc_join_channel_data)
    except sendbird_platform_sdk.ApiException as e:
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
> OcDeleteChannelByUrl200Response gc_leave_channel(channel_url)

Leave a channel

## Leave a channel  Makes one or more members leave a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-leave-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_leave_channel_data import GcLeaveChannelData
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_leave_channel_data = GcLeaveChannelData(
        channel_url="channel_url_example",
        user_ids=[
            "user_ids_example",
        ],
        should_leave_all=True,
    ) # GcLeaveChannelData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Leave a channel
        api_response = api_instance.gc_leave_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_leave_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Leave a channel
        api_response = api_instance.gc_leave_channel(channel_url, api_token=api_token, gc_leave_channel_data=gc_leave_channel_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_leave_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_leave_channel_data** | [**GcLeaveChannelData**](GcLeaveChannelData.md)|  | [optional]

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

# **gc_list_channels**
> GcListChannelsResponse gc_list_channels()

List channels

## List channels  Retrieves a list of group channels in the application.  > __Note__: If you want to get a list of a specific user's group channels, use the [list my group channels](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-list-my-group-channels) action instead.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-channels ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_list_channels_response import GcListChannelsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
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
    except sendbird_platform_sdk.ApiException as e:
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

[**GcListChannelsResponse**](GcListChannelsResponse.md)

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
> GcListMembersResponse gc_list_members(channel_url)

List members

## List members  Retrieves a list of members of a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-members ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of members of.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_list_members_response import GcListMembersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
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
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List members
        api_response = api_instance.gc_list_members(channel_url, api_token=api_token, token=token, limit=limit, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, order=order, operator_filter=operator_filter, member_state_filter=member_state_filter, muted_member_filter=muted_member_filter, nickname_startswith=nickname_startswith)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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

[**GcListMembersResponse**](GcListMembersResponse.md)

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
> GcListOperatorsResponse gc_list_operators(channel_url)

List operators

## List operators  Retrieves a list of operators of a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-list-operators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of operators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_list_operators_response import GcListOperatorsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
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
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_list_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List operators
        api_response = api_instance.gc_list_operators(channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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

[**GcListOperatorsResponse**](GcListOperatorsResponse.md)

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

# **gc_register_operators**
> GcRegisterOperatorsResponse gc_register_operators(channel_url)

Register operators

## Register operators  Registers one or more operators to a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-register-operators ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_register_operators_data import GcRegisterOperatorsData
from sendbird_platform_sdk.model.gc_register_operators_response import GcRegisterOperatorsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_register_operators_data = GcRegisterOperatorsData(
        channel_url="channel_url_example",
        operator_ids=[
            "operator_ids_example",
        ],
    ) # GcRegisterOperatorsData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register operators
        api_response = api_instance.gc_register_operators(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_register_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register operators
        api_response = api_instance.gc_register_operators(channel_url, api_token=api_token, gc_register_operators_data=gc_register_operators_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_register_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_register_operators_data** | [**GcRegisterOperatorsData**](GcRegisterOperatorsData.md)|  | [optional]

### Return type

[**GcRegisterOperatorsResponse**](GcRegisterOperatorsResponse.md)

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
> GcResetChatHistoryResponse gc_reset_chat_history(channel_url)

Reset chat history

## Reset chat history  Resets the properties related to a user's chat history in a group channel, then clears the existing messages in the channel on the user's side only. A user can no longer see the messages in a group channel once this action is called, but those messages are not deleted from the database of the Sendbird system. All other members in the channel can retrieve and see the messages.  This action simply clears the messages for the user by updating the `last_message` and `read_receipt` properties of the [channel](#2-types-of-a-channel-3-resource-representation) resource in addition to other internally managed data such as the number of the user's unread message.  Using the `reset_all` property, you can also reset the properties related to all users' chat history in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-reset-chat-history ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_reset_chat_history_response import GcResetChatHistoryResponse
from sendbird_platform_sdk.model.gc_reset_chat_history_data import GcResetChatHistoryData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
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
        api_response = api_instance.gc_reset_chat_history(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_reset_chat_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset chat history
        api_response = api_instance.gc_reset_chat_history(channel_url, api_token=api_token, gc_reset_chat_history_data=gc_reset_chat_history_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_reset_chat_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_reset_chat_history_data** | [**GcResetChatHistoryData**](GcResetChatHistoryData.md)|  | [optional]

### Return type

[**GcResetChatHistoryResponse**](GcResetChatHistoryResponse.md)

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

# **gc_start_typing_indicators**
> OcDeleteChannelByUrl200Response gc_start_typing_indicators(channel_url)

Start typing indicators

## Start typing indicators  You can start showing a typing indicator using this API. Seeing whether other users are typing can help a more interactive conversation environment by showing real-time engagement of other users.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-typing-indicators/start-typing-indicators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to set typing indicators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_typing_indicators_data import GcTypingIndicatorsData
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_typing_indicators_data = GcTypingIndicatorsData(
        user_ids=[
            "user_ids_example",
        ],
    ) # GcTypingIndicatorsData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start typing indicators
        api_response = api_instance.gc_start_typing_indicators(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_start_typing_indicators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start typing indicators
        api_response = api_instance.gc_start_typing_indicators(channel_url, api_token=api_token, gc_typing_indicators_data=gc_typing_indicators_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_start_typing_indicators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_typing_indicators_data** | [**GcTypingIndicatorsData**](GcTypingIndicatorsData.md)|  | [optional]

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

# **gc_stop_typing_indicators**
> OcDeleteChannelByUrl200Response gc_stop_typing_indicators(channel_url)

Stop typing indicators

## Stop typing indicators  You can stop showing a typing indicator using this API. To signal that a user is no longer typing, you can let the indicator disappear when the user sends a message or completely deletes the message text.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-typing-indicators/stop-typing-indicators ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to set typing indicators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_typing_indicators_data import GcTypingIndicatorsData
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_typing_indicators_data = GcTypingIndicatorsData(
        user_ids=[
            "user_ids_example",
        ],
    ) # GcTypingIndicatorsData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop typing indicators
        api_response = api_instance.gc_stop_typing_indicators(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_stop_typing_indicators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop typing indicators
        api_response = api_instance.gc_stop_typing_indicators(channel_url, api_token=api_token, gc_typing_indicators_data=gc_typing_indicators_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_stop_typing_indicators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_typing_indicators_data** | [**GcTypingIndicatorsData**](GcTypingIndicatorsData.md)|  | [optional]

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

# **gc_unhide_or_unarchive_channel**
> OcDeleteChannelByUrl200Response gc_unhide_or_unarchive_channel(channel_url, user_id)

Unhide or unarchive a channel

## Unhide or unarchive a channel  Makes a hidden or archived channel reappear in the channel list of either a specific user or entire channel members.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-unhide-or-unarchive-a-channel ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to unhide or unarchive.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | 
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    should_unhide_all = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unhide or unarchive a channel
        api_response = api_instance.gc_unhide_or_unarchive_channel(channel_url, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_unhide_or_unarchive_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unhide or unarchive a channel
        api_response = api_instance.gc_unhide_or_unarchive_channel(channel_url, user_id, api_token=api_token, should_unhide_all=should_unhide_all)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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

# **gc_update_channel_by_url**
> SendBirdGroupChannel gc_update_channel_by_url(channel_url)

Update a channel

## Update a channel  Updates information on a group channel.  > __Note__: You can't change the members of the channel here. To do so, see [invite as members](#2-invite-as-members) action below.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-update-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.gc_update_channel_by_url_data import GcUpdateChannelByUrlData
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
            "operator_ids_example",
        ],
    ) # GcUpdateChannelByUrlData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel
        api_response = api_instance.gc_update_channel_by_url(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_update_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel
        api_response = api_instance.gc_update_channel_by_url(channel_url, api_token=api_token, gc_update_channel_by_url_data=gc_update_channel_by_url_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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

# **gc_view_channel_by_url**
> SendBirdGroupChannel gc_view_channel_by_url(channel_url)

View a channel

## View a channel  Retrieves information on a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-view-a-channel ----------------------------   `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->gc_view_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel
        api_response = api_instance.gc_view_channel_by_url(channel_url, api_token=api_token, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, show_member=show_member, read_receipt=read_receipt, member=member)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
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

