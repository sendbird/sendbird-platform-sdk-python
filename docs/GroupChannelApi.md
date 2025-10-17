# sendbird_platform_sdk.GroupChannelApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_an_invitation**](GroupChannelApi.md#accept_an_invitation) | **PUT** /v3/group_channels/{channel_url}/accept | Accept an invitation
[**cancel_the_registration_of_operators**](GroupChannelApi.md#cancel_the_registration_of_operators) | **DELETE** /v3/group_channels/{channel_url}/operators | Cancel the registration of operators
[**check_if_member**](GroupChannelApi.md#check_if_member) | **GET** /v3/group_channels/{channel_url}/members/{user_id} | Check if member
[**create_a_group_channel**](GroupChannelApi.md#create_a_group_channel) | **POST** /v3/group_channels | Create a group channel
[**delete_a_group_channel**](GroupChannelApi.md#delete_a_group_channel) | **DELETE** /v3/group_channels/{channel_url} | Delete a group channel
[**get_a_group_channel**](GroupChannelApi.md#get_a_group_channel) | **GET** /v3/group_channels/{channel_url} | Get a group channel
[**hide_a_channel**](GroupChannelApi.md#hide_a_channel) | **PUT** /v3/group_channels/{channel_url}/hide | Hide a channel
[**invite_as_members**](GroupChannelApi.md#invite_as_members) | **POST** /v3/group_channels/{channel_url}/invite | Invite as members
[**join_a_channel**](GroupChannelApi.md#join_a_channel) | **PUT** /v3/group_channels/{channel_url}/join | Join a channel
[**leave_a_channel**](GroupChannelApi.md#leave_a_channel) | **PUT** /v3/group_channels/{channel_url}/leave | Leave a channel
[**list_channels**](GroupChannelApi.md#list_channels) | **GET** /v3/group_channels | List channels
[**list_members**](GroupChannelApi.md#list_members) | **GET** /v3/group_channels/{channel_url}/members | List members
[**list_operators**](GroupChannelApi.md#list_operators) | **GET** /v3/group_channels/{channel_url}/operators | List operators
[**register_operators_to_a_group_channel**](GroupChannelApi.md#register_operators_to_a_group_channel) | **POST** /v3/group_channels/{channel_url}/operators | Register operators to a group channel
[**reset_chat_history**](GroupChannelApi.md#reset_chat_history) | **PUT** /v3/group_channels/{channel_url}/reset_user_history | Reset chat history
[**start_typing_indicators**](GroupChannelApi.md#start_typing_indicators) | **POST** /v3/group_channels/{channel_url}/typing | Start typing indicators
[**stop_typing_indicators**](GroupChannelApi.md#stop_typing_indicators) | **DELETE** /v3/group_channels/{channel_url}/typing | Stop typing indicators
[**unhide_a_channel**](GroupChannelApi.md#unhide_a_channel) | **DELETE** /v3/group_channels/{channel_url}/hide | Unhide a channel
[**update_a_group_channel**](GroupChannelApi.md#update_a_group_channel) | **PUT** /v3/group_channels/{channel_url} | Update a group channel


# **accept_an_invitation**
> SendbirdGroupChannelDetail accept_an_invitation(channel_url)

Accept an invitation

## Accept an invitation  Accepts an invitation from a group channel for a user to join. A single user may join up to 2,000 group channels, and any invitation to a user who is at capacity will be automatically canceled. See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.  > **Note**: This action is only available when the `auto_accept` property of an application is set to **false**. You can change the value of the property using the [update default channel invitation preference](https://sendbird.com/docs/chat/platform-api/v3/channel/setting-up-channels/update-default-invitation-preference) action, or the [update channel invitation preference](https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/update-channel-invitation-preference) action.      [https://sendbird.com/docs/chat/platform-api/v3/channel/inviting-a-user/accept-an-invitation-channel#1-accept-an-invitation](https://sendbird.com/docs/chat/platform-api/v3/channel/inviting-a-user/accept-an-invitation-channel#1-accept-an-invitation)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.sendbird_group_channel_detail import SendbirdGroupChannelDetail
from sendbird_platform_sdk.model.accept_an_invitation_request import AcceptAnInvitationRequest
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
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    accept_an_invitation_request = AcceptAnInvitationRequest(
        access_code="access_code_example",
        user_id="user_id_example",
    ) # AcceptAnInvitationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Accept an invitation
        api_response = api_instance.accept_an_invitation(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->accept_an_invitation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Accept an invitation
        api_response = api_instance.accept_an_invitation(channel_url, api_token=api_token, accept_an_invitation_request=accept_an_invitation_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->accept_an_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **accept_an_invitation_request** | [**AcceptAnInvitationRequest**](AcceptAnInvitationRequest.md)|  | [optional]

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

# **cancel_the_registration_of_operators**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} cancel_the_registration_of_operators(channel_url, operator_ids)

Cancel the registration of operators

## Unregister operators from a group channel  You can unregister operators in a group channel but keep them in the channel as members using this API.  https://sendbird.com/docs/chat/platform-api/v3/user/assigning-a-user-role/unregister-operators-from-a-group-channel#1-unregister-operators-from-a-group-channel  `channel_url`   Type: string   Description: Specifies the URL of the channel to cancel the registration of operators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
    channel_url = "channel_url_example" # str | (Required) 
    operator_ids = "operator_ids_example" # str | Specifies an array of one or more operator IDs to unregister from the channel. The operators in this array remain as participants of the channel after losing their operational roles. Urlencoding each operator ID is recommended. An example of a Urlencoded array would be ?operator_ids=urlencoded_id_1,urlencoded_id_2.
    delete_all = True # bool |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel the registration of operators
        api_response = api_instance.cancel_the_registration_of_operators(channel_url, operator_ids)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->cancel_the_registration_of_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel the registration of operators
        api_response = api_instance.cancel_the_registration_of_operators(channel_url, operator_ids, delete_all=delete_all, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->cancel_the_registration_of_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **operator_ids** | **str**| Specifies an array of one or more operator IDs to unregister from the channel. The operators in this array remain as participants of the channel after losing their operational roles. Urlencoding each operator ID is recommended. An example of a Urlencoded array would be ?operator_ids&#x3D;urlencoded_id_1,urlencoded_id_2. |
 **delete_all** | **bool**|  | [optional]
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

# **check_if_member**
> CheckIfMemberResponse check_if_member(channel_url, user_id)

Check if member

## Check if user is a member  Checks if a user is a member of a group channel.  > **Note**: See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.      [https://sendbird.com/docs/chat/platform-api/v3/channel/listing-users/check-if-user-is-a-member#1-check-if-user-is-a-member](https://sendbird.com/docs/chat/platform-api/v3/channel/listing-users/check-if-user-is-a-member#1-check-if-user-is-a-member)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.check_if_member_response import CheckIfMemberResponse
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
    channel_url = "channel_url_example" # str | (Required) 
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Check if member
        api_response = api_instance.check_if_member(channel_url, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->check_if_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check if member
        api_response = api_instance.check_if_member(channel_url, user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->check_if_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**CheckIfMemberResponse**](CheckIfMemberResponse.md)

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

# **create_a_group_channel**
> SendbirdGroupChannelDetail create_a_group_channel()

Create a group channel

## Create a group channel  You can create a group channel for 1-to-1 and 1-to-N conversations. By default, group channels are used for conversations between up to 100 members. This number can stretch up to tens of thousands in Supergroup channels. Group channels can either be private and invite only, or public. They support typing indicators, unread count and read receipts, allowing for an interactive chat experience. A user can join up to 2000 group channels, and higher numbers would negatively impact the performance for the end user. The Chat history is turned off by default and its settings can be changed on Sendbird Dashboard by going to Settings > Chat > Channels > Group channels > Chat history. To learn more about group channels, see Channel Overview.  > If you are seeing the error message Maximum \"channel join\" count reached., then consider deleting channels that are no longer used. For situations where an agent connects with many customers such as support, delivery logistics or sales, we recommend using Sendbird Desk.  https://sendbird.com/docs/chat/platform-api/v3/channel/creating-a-channel/create-a-group-channel#1-create-a-group-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.sendbird_group_channel_detail import SendbirdGroupChannelDetail
from sendbird_platform_sdk.model.create_a_group_channel_request import CreateAGroupChannelRequest
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
    create_a_group_channel_request = CreateAGroupChannelRequest(
        access_code="access_code_example",
        block_sdk_user_channel_join=True,
        channel_url="channel_url_example",
        cover_file=open('/path/to/file', 'rb'),
        cover_url="cover_url_example",
        custom_type="custom_type_example",
        data="data_example",
        hidden_status={},
        invitation_status={},
        inviter_id="inviter_id_example",
        is_distinct=True,
        is_ephemeral=True,
        is_public=True,
        is_super=True,
        name="name_example",
        operator_ids=[
            "operator_ids_example",
        ],
        strict=True,
        user_ids=[
            "user_ids_example",
        ],
        users=[
            SendbirdUser(
                access_token="access_token_example",
                created_at=1,
                discovery_keys=[
                    "discovery_keys_example",
                ],
                has_ever_logged_in=True,
                is_active=True,
                is_hide_me_from_friends=True,
                is_online=True,
                is_shadow_blocked=True,
                last_seen_at=1,
                locale="locale_example",
                metadata={},
                nickname="nickname_example",
                preferred_languages=[
                    "preferred_languages_example",
                ],
                profile_url="",
                require_auth_for_profile_image=True,
                user_id="user_id_example",
                state="",
                unread_channel_count=1,
                unread_message_count=1,
                phone_number="phone_number_example",
                is_created=True,
            ),
        ],
    ) # CreateAGroupChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a group channel
        api_response = api_instance.create_a_group_channel(api_token=api_token, create_a_group_channel_request=create_a_group_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->create_a_group_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **create_a_group_channel_request** | [**CreateAGroupChannelRequest**](CreateAGroupChannelRequest.md)|  | [optional]

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

# **delete_a_group_channel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_a_group_channel(channel_url)

Delete a group channel

## Delete a group channel  You can delete a group channel or a Supergroup channel using this API. See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.  [https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/delete-a-group-channel#1-delete-a-group-channel](https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/delete-a-group-channel#1-delete-a-group-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
        # Delete a group channel
        api_response = api_instance.delete_a_group_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->delete_a_group_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a group channel
        api_response = api_instance.delete_a_group_channel(channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->delete_a_group_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
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

# **get_a_group_channel**
> GetAGroupChannelResponse get_a_group_channel(channel_url)

Get a group channel

## Get a group channel  This action retrieves information about a specific [group channel](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-group-channel). You can use the optional query parameters to determine whether to include delivery receipt, read receipt, or member information in the response.  https://sendbird.com/docs/chat/platform-api/v3/channel/listing-channels-in-an-application/get-a-group-channel#1-get-a-group-channel  `channel_url`   Type: string   Description: Specifies the URL of the channel to retrieve.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.get_a_group_channel_response import GetAGroupChannelResponse
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
    show_delivery_receipt = True # bool |  (optional)
    show_read_receipt = True # bool |  (optional)
    show_member = True # bool |  (optional)
    member_active_mode = "all" # str | Restricts the member list to members who are activated or deactivated in the channel. This parameter is only effective if the parameter show_member is true. Acceptable values are all, activated, and deactivated. (default: all) (optional)
    user_id = "user_id_example" # str |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a group channel
        api_response = api_instance.get_a_group_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->get_a_group_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a group channel
        api_response = api_instance.get_a_group_channel(channel_url, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, show_member=show_member, member_active_mode=member_active_mode, user_id=user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->get_a_group_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **show_delivery_receipt** | **bool**|  | [optional]
 **show_read_receipt** | **bool**|  | [optional]
 **show_member** | **bool**|  | [optional]
 **member_active_mode** | **str**| Restricts the member list to members who are activated or deactivated in the channel. This parameter is only effective if the parameter show_member is true. Acceptable values are all, activated, and deactivated. (default: all) | [optional]
 **user_id** | **str**|  | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**GetAGroupChannelResponse**](GetAGroupChannelResponse.md)

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

# **hide_a_channel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} hide_a_channel(channel_url)

Hide a channel

## Hide a channel  This action allows you to hide a [group channel](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-group-channel) from a user's channel list. Hiding a channel gives users the ability to archive channels so that they can focus on channels that need the most attention.  With this API, you can allow users to hide a channel from themselves or from all channel members. You can also determine whether to have the channel remain hidden when a new message is sent to the channel. Note that only group channels can be hidden.  [https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/hide-a-channel#1-hide-a-channel](https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/hide-a-channel#1-hide-a-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.hide_a_channel_request import HideAChannelRequest
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
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    hide_a_channel_request = HideAChannelRequest(
        allow_auto_unhide=True,
        hide_previous_messages=True,
        should_hide_all=True,
        user_id="user_id_example",
    ) # HideAChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Hide a channel
        api_response = api_instance.hide_a_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->hide_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Hide a channel
        api_response = api_instance.hide_a_channel(channel_url, api_token=api_token, hide_a_channel_request=hide_a_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->hide_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **hide_a_channel_request** | [**HideAChannelRequest**](HideAChannelRequest.md)|  | [optional]

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

# **invite_as_members**
> InviteAsMembersResponse invite_as_members(channel_url)

Invite as members

## Invite as members  Invites one or more users as members to a group channel. Users can join a group channel immediately after receiving an invitation, without having to accept it. To give users an option to accept or decline an invitation, see [update default channel invitation preference](https://sendbird.com/docs/chat/platform-api/v3/channel/setting-up-channels/update-default-invitation-preference) or [update channel invitation preference](https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/update-channel-invitation-preference). See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.  > **Note**: By default, [blocked users](https://sendbird.com/docs/chat/platform-api/v3/moderation/blocking-users/block-users) are included when sending invitations. If you wish to exclude blocked users, [contact our sales team](https://get.sendbird.com/talk-to-sales.html).      [https://sendbird.com/docs/chat/platform-api/v3/channel/inviting-a-user/invite-as-members-channel#1-invite-as-members](https://sendbird.com/docs/chat/platform-api/v3/channel/inviting-a-user/invite-as-members-channel#1-invite-as-members)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.invite_as_members_response import InviteAsMembersResponse
from sendbird_platform_sdk.model.invite_as_members_request import InviteAsMembersRequest
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
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    invite_as_members_request = InviteAsMembersRequest(
        hidden_status={},
        invitation_status={},
        inviter_id="inviter_id_example",
        user_ids=[
            "user_ids_example",
        ],
    ) # InviteAsMembersRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Invite as members
        api_response = api_instance.invite_as_members(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->invite_as_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Invite as members
        api_response = api_instance.invite_as_members(channel_url, api_token=api_token, invite_as_members_request=invite_as_members_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->invite_as_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **invite_as_members_request** | [**InviteAsMembersRequest**](InviteAsMembersRequest.md)|  | [optional]

### Return type

[**InviteAsMembersResponse**](InviteAsMembersResponse.md)

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

# **join_a_channel**
> SendbirdGroupChannelDetail join_a_channel(channel_url)

Join a channel

## Join a channel  This API allows a user to join a [public](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#4-group-channel-types) group channel. Users can only join public group channels where the `is_public` property is set to `true` using this API. A single user can join up to 2,000 group channels, and a user who reaches the capacity can’t join a new channel. See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.  [https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/join-a-channel#1-join-a-channel](https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/join-a-channel#1-join-a-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.sendbird_group_channel_detail import SendbirdGroupChannelDetail
from sendbird_platform_sdk.model.join_a_channel_request import JoinAChannelRequest
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
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    join_a_channel_request = JoinAChannelRequest(
        user_id="user_id_example",
        access_code="access_code_example",
    ) # JoinAChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Join a channel
        api_response = api_instance.join_a_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->join_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Join a channel
        api_response = api_instance.join_a_channel(channel_url, api_token=api_token, join_a_channel_request=join_a_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->join_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **join_a_channel_request** | [**JoinAChannelRequest**](JoinAChannelRequest.md)|  | [optional]

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
**200** | Join a channel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_a_channel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} leave_a_channel(channel_url)

Leave a channel

## Leave a channel  Makes one or more members leave a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-leave-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.leave_a_channel_request import LeaveAChannelRequest
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
    leave_a_channel_request = LeaveAChannelRequest(
        user_ids=[
            "user_ids_example",
        ],
        should_leave_all=True,
        should_remove_operator_status=True,
        reason="LEFT_BY_OWN_CHOICE",
    ) # LeaveAChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Leave a channel
        api_response = api_instance.leave_a_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->leave_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Leave a channel
        api_response = api_instance.leave_a_channel(channel_url, api_token=api_token, leave_a_channel_request=leave_a_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->leave_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **leave_a_channel_request** | [**LeaveAChannelRequest**](LeaveAChannelRequest.md)|  | [optional]

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

# **list_channels**
> GroupChatListChannelsResponse list_channels(api_token)

List channels

## List group channels  This action retrieves a list of [group channels](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-group-channel). You can use various query parameters to determine the search scope and select what kind of information you want to receive about the queried channels.  If you want to retrieve a list of group channels that a specific user has joined, use the [list group channels by user](https://sendbird.com/docs/chat/platform-api/v3/user/managing-joined-group-channels/list-group-channels-by-user) action under the User section.  https://sendbird.com/docs/chat/platform-api/v3/channel/listing-channels-in-an-application/list-group-channels#1-list-group-channels

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.group_chat_list_channels_response import GroupChatListChannelsResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    token = "token_example" # str | Specifies a page token that indicates the starting index of a chunk of results. If not specified, the index is set as 0. (optional)
    limit = 10 # int | Specifies the number of results to return per page. Acceptable values are 1 to 100, inclusive. (Default: 10) (optional)
    distinct_mode = "all" # str |  (optional)
    public_mode = "all" # str |  (optional)
    super_mode = "all" # str |  (optional)
    created_after = 1234567890123 # int | Restricts the search scope to only retrieve group channels which have been created after the specified time, in Unix milliseconds format. (optional)
    created_before = 1234567890123 # int | Restricts the search scope to only retrieve group channels which have been created before the specified time, in Unix milliseconds format. (optional)
    show_empty = False # bool |  (optional)
    show_member = False # bool |  (optional)
    show_delivery_receipt = False # bool |  (optional)
    show_read_receipt = False # bool |  (optional)
    show_metadata = False # bool |  (optional)
    show_frozen = False # bool |  (optional)
    order = "chronological" # str |  (optional)
    metadata_order_key = "metadata_order_key_example" # str | Specifies the key of an item in metadata. When a value of the order parameter is set to metadata_value_alphabetical, the results are alphabetically sorted by the value of the item specified by the key. (optional)
    custom_types = "custom_types_example" # str | Specifies a comma-separated string of one or more custom types to filter group channels. URL encoding each type is recommended. If not specified, all channels are returned, regardless of their custom type. (optional)
    custom_type_startswith = "custom_type_startswith_example" # str | Searches for group channels with the custom type which starts with the specified value. URL encoding the value is recommended. (optional)
    channel_urls = "channel_urls_example" # str | Specifies a comma-separated string of one or more group channel URLs to restrict the search scope. URL encoding each channel URL is recommended. (optional)
    name = "name_example" # str | Specifies one or more group channel names. (optional)
    name_contains = "name_contains_example" # str | Searches for group channels whose names contain the specified value. Note that this parameter is case-insensitive. URL encoding the value is recommended. (optional)
    name_startswith = "name_startswith_example" # str | Searches for group channels whose names start with the specified value. Note that this parameter is case-insensitive. URL encoding the value is recommended. (optional)
    members_exactly_in = "members_exactly_in_example" # str | Searches for group channels with all the specified users as members. The parameter value should consist of user IDs separated by commas.  Only user IDs that match those of existing users are used for channel search. URL encoding each ID is recommended. (optional)
    members_include_in = "members_include_in_example" # str | Searches for group channels that include one or more users as members among the specified users. The value should consist of user IDs separated by commas or %2C. You can specify up to 60 user IDs.  Only user IDs that match those of existing users are used for channel search. URL encoding each ID is recommended. (optional)
    query_type = "query_type_example" # str | Specifies a logical condition applied to the members_include_in parameter. Acceptable values are either AND or OR. For example, if you specify three members, A, B, and C, in members_include_in, the value of AND returns all channels that include every one of {A. B, C} as members. The value of OR returns channels that include {A}, plus those that include {B}, plus those that include {C}. (Default: AND) (optional)
    members_nickname = "members_nickname_example" # str | Searches for group channels with members whose nicknames match the specified value. URL encoding the value is recommended. (optional)
    members_nickname_contains = "members_nickname_contains_example" # str | Searches for group channels with members whose nicknames contain the specified value. Note that this parameter is case-insensitive. URL encoding the value is recommended.  * We recommend using at least three characters for the parameter value for better search efficiency when you design and implement related features. If you would like to allow one or two characters for searching, use members_nickname instead to prevent performance issues. (optional)
    metadata_key = "metadata_key_example" # str | Searches for group channels with metadata containing an item with the specified value as its key. To use this parameter, either the metadata_values parameter or the metadata_value_startswith parameter should be specified. (optional)
    metadata_values = "metadata_values_example" # str | Searches for group channels with metadata containing an item with the key specified by the metadata_key parameter, and the value of that item matches one or more values specified by this parameter. The string should be specified with multiple values separated by commas. URL encoding each value is recommended. To use this parameter, the metadata_key parameter should be specified. (optional)
    metadata_value_startswith = "metadata_value_startswith_example" # str | Searches for group channels with metadata containing an item with the key specified by the metadata_key parameter, and the values of that item that start with the specified value of this parameter. URL encoding the value is recommended. To use this parameter, the metadata_key parameter should be specified. (optional)
    metacounter_key = "metacounter_key_example" # str | Searches for group channels with metacounter containing an item with the specified value as its key. To use this parameter, either the metacounter_values parameter or one of the metacounter_value_gt, metacounter_value_gte, metacounter_value_lt, and metacounter_value_lte parameters should be specified. (optional)
    metacounter_values = "metacounter_values_example" # str | Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is equal to one or more values specified by this parameter. The string should be specified with multiple values separated by commas. To use this parameter, the metacounter_key parameter should be specified. (optional)
    metacounter_value_gt = "metacounter_value_gt_example" # str | Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is greater than the value specified by this parameter. To use this parameter, the metacounter_key parameter should be specified. (optional)
    metacounter_value_gte = "metacounter_value_gte_example" # str | Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is greater than or equal to the value specified by this parameter. To use this parameter, the metacounter_key parameter should be specified. (optional)
    metacounter_value_lt = "metacounter_value_lt_example" # str | Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is lower than the value specified by this parameter. To use this parameter, the metacounter_key parameter should be specified. (optional)
    metacounter_value_lte = "metacounter_value_lte_example" # str | Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is lower than or equal to the value specified by this parameter. To use this parameter, the metacounter_key parameter should be specified. (optional)
    include_sorted_metaarray_in_last_message = False # bool | Determines whether to include the sorted_metaarray as one of the last_message’s properties in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List channels
        api_response = api_instance.list_channels(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->list_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List channels
        api_response = api_instance.list_channels(api_token, token=token, limit=limit, distinct_mode=distinct_mode, public_mode=public_mode, super_mode=super_mode, created_after=created_after, created_before=created_before, show_empty=show_empty, show_member=show_member, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, show_metadata=show_metadata, show_frozen=show_frozen, order=order, metadata_order_key=metadata_order_key, custom_types=custom_types, custom_type_startswith=custom_type_startswith, channel_urls=channel_urls, name=name, name_contains=name_contains, name_startswith=name_startswith, members_exactly_in=members_exactly_in, members_include_in=members_include_in, query_type=query_type, members_nickname=members_nickname, members_nickname_contains=members_nickname_contains, metadata_key=metadata_key, metadata_values=metadata_values, metadata_value_startswith=metadata_value_startswith, metacounter_key=metacounter_key, metacounter_values=metacounter_values, metacounter_value_gt=metacounter_value_gt, metacounter_value_gte=metacounter_value_gte, metacounter_value_lt=metacounter_value_lt, metacounter_value_lte=metacounter_value_lte, include_sorted_metaarray_in_last_message=include_sorted_metaarray_in_last_message)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->list_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **token** | **str**| Specifies a page token that indicates the starting index of a chunk of results. If not specified, the index is set as 0. | [optional]
 **limit** | **int**| Specifies the number of results to return per page. Acceptable values are 1 to 100, inclusive. (Default: 10) | [optional]
 **distinct_mode** | **str**|  | [optional]
 **public_mode** | **str**|  | [optional]
 **super_mode** | **str**|  | [optional]
 **created_after** | **int**| Restricts the search scope to only retrieve group channels which have been created after the specified time, in Unix milliseconds format. | [optional]
 **created_before** | **int**| Restricts the search scope to only retrieve group channels which have been created before the specified time, in Unix milliseconds format. | [optional]
 **show_empty** | **bool**|  | [optional]
 **show_member** | **bool**|  | [optional]
 **show_delivery_receipt** | **bool**|  | [optional]
 **show_read_receipt** | **bool**|  | [optional]
 **show_metadata** | **bool**|  | [optional]
 **show_frozen** | **bool**|  | [optional]
 **order** | **str**|  | [optional]
 **metadata_order_key** | **str**| Specifies the key of an item in metadata. When a value of the order parameter is set to metadata_value_alphabetical, the results are alphabetically sorted by the value of the item specified by the key. | [optional]
 **custom_types** | **str**| Specifies a comma-separated string of one or more custom types to filter group channels. URL encoding each type is recommended. If not specified, all channels are returned, regardless of their custom type. | [optional]
 **custom_type_startswith** | **str**| Searches for group channels with the custom type which starts with the specified value. URL encoding the value is recommended. | [optional]
 **channel_urls** | **str**| Specifies a comma-separated string of one or more group channel URLs to restrict the search scope. URL encoding each channel URL is recommended. | [optional]
 **name** | **str**| Specifies one or more group channel names. | [optional]
 **name_contains** | **str**| Searches for group channels whose names contain the specified value. Note that this parameter is case-insensitive. URL encoding the value is recommended. | [optional]
 **name_startswith** | **str**| Searches for group channels whose names start with the specified value. Note that this parameter is case-insensitive. URL encoding the value is recommended. | [optional]
 **members_exactly_in** | **str**| Searches for group channels with all the specified users as members. The parameter value should consist of user IDs separated by commas.  Only user IDs that match those of existing users are used for channel search. URL encoding each ID is recommended. | [optional]
 **members_include_in** | **str**| Searches for group channels that include one or more users as members among the specified users. The value should consist of user IDs separated by commas or %2C. You can specify up to 60 user IDs.  Only user IDs that match those of existing users are used for channel search. URL encoding each ID is recommended. | [optional]
 **query_type** | **str**| Specifies a logical condition applied to the members_include_in parameter. Acceptable values are either AND or OR. For example, if you specify three members, A, B, and C, in members_include_in, the value of AND returns all channels that include every one of {A. B, C} as members. The value of OR returns channels that include {A}, plus those that include {B}, plus those that include {C}. (Default: AND) | [optional]
 **members_nickname** | **str**| Searches for group channels with members whose nicknames match the specified value. URL encoding the value is recommended. | [optional]
 **members_nickname_contains** | **str**| Searches for group channels with members whose nicknames contain the specified value. Note that this parameter is case-insensitive. URL encoding the value is recommended.  * We recommend using at least three characters for the parameter value for better search efficiency when you design and implement related features. If you would like to allow one or two characters for searching, use members_nickname instead to prevent performance issues. | [optional]
 **metadata_key** | **str**| Searches for group channels with metadata containing an item with the specified value as its key. To use this parameter, either the metadata_values parameter or the metadata_value_startswith parameter should be specified. | [optional]
 **metadata_values** | **str**| Searches for group channels with metadata containing an item with the key specified by the metadata_key parameter, and the value of that item matches one or more values specified by this parameter. The string should be specified with multiple values separated by commas. URL encoding each value is recommended. To use this parameter, the metadata_key parameter should be specified. | [optional]
 **metadata_value_startswith** | **str**| Searches for group channels with metadata containing an item with the key specified by the metadata_key parameter, and the values of that item that start with the specified value of this parameter. URL encoding the value is recommended. To use this parameter, the metadata_key parameter should be specified. | [optional]
 **metacounter_key** | **str**| Searches for group channels with metacounter containing an item with the specified value as its key. To use this parameter, either the metacounter_values parameter or one of the metacounter_value_gt, metacounter_value_gte, metacounter_value_lt, and metacounter_value_lte parameters should be specified. | [optional]
 **metacounter_values** | **str**| Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is equal to one or more values specified by this parameter. The string should be specified with multiple values separated by commas. To use this parameter, the metacounter_key parameter should be specified. | [optional]
 **metacounter_value_gt** | **str**| Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is greater than the value specified by this parameter. To use this parameter, the metacounter_key parameter should be specified. | [optional]
 **metacounter_value_gte** | **str**| Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is greater than or equal to the value specified by this parameter. To use this parameter, the metacounter_key parameter should be specified. | [optional]
 **metacounter_value_lt** | **str**| Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is lower than the value specified by this parameter. To use this parameter, the metacounter_key parameter should be specified. | [optional]
 **metacounter_value_lte** | **str**| Searches for group channels with metacounter containing an item with the key specified by the metadata_key parameter, where the value of that item is lower than or equal to the value specified by this parameter. To use this parameter, the metacounter_key parameter should be specified. | [optional]
 **include_sorted_metaarray_in_last_message** | **bool**| Determines whether to include the sorted_metaarray as one of the last_message’s properties in the response. | [optional]

### Return type

[**GroupChatListChannelsResponse**](GroupChatListChannelsResponse.md)

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

# **list_members**
> GroupChannelListMembersResponse list_members(channel_url)

List members

## List members  Retrieves a list of members of a group channel.  > **Note**: See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.      [https://sendbird.com/docs/chat/platform-api/v3/channel/listing-users/list-members-of-a-group-channel#1-list-members-of-a-group-channel](https://sendbird.com/docs/chat/platform-api/v3/channel/listing-users/list-members-of-a-group-channel#1-list-members-of-a-group-channel)  `channel_url`   Type: string   Description: Specifies the URL of the channel to retrieve a list of members of.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.group_channel_list_members_response import GroupChannelListMembersResponse
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
    channel_url = "channel_url_example" # str | (Required) 
    token = "token_example" # str |  (optional)
    limit = 1 # int | Specifies the number of results to return per page. Acceptable values are 1 to 100, inclusive. (Default: 10) (optional)
    user_id = "user_id_example" # str | Specifies the unique ID of a user. If `user_id` is provided, the response will include two additional boolean properties about each user in the members list. - `is_blocking_me`: Indicates whether the listed user is blocking the user specified in the user_id parameter. - `is_blocked_by_me`: Indicates whether the listed user is blocked by the user specified in the user_id parameter. (optional)
    show_delivery_receipt = True # bool |  (optional)
    show_read_receipt = True # bool |  (optional)
    show_member_is_muted = True # bool |  (optional)
    order = "member_nickname_alphabetical" # str | Specifies the method to sort a list of results. Acceptable values are the following: - `member_nickname_alphabetical` (default): sorts by the member nicknames in alphabetical order. - `operator_then_member_alphabetical`: sorts by the operational role and member nickname in alphabetical order where channel operators are listed before channel members. (optional)
    operator_filter = "all" # str | Restricts the search scope to only retrieve operators or non-operator members of the channel. Acceptable values are the following: - `all` (default): no filter is applied to the list. - `operator`: only channel operators are retrieved. - `nonoperator`: all channel members, except channel operators, are retrieved. (optional)
    member_state_filter = "all" # str | Restricts the search scope to retrieve members based on if they have accepted an invitation or if they were invited by a friend. Acceptable values are `invited_only`, `joined_only`, `invited_by_friend`, `invited_by_non_friend`, and `all`. (Default: `all`) (optional)
    muted_member_filter = "all" # str | Restricts the search scope to retrieve members who are muted or unmuted in the channel. Acceptable values are `all`, `muted`, and `unmuted`. (Default: `all`) (optional)
    member_active_mode_filter = "activated" # str | Restricts the search scope to retrieve members who are activated or deactivated in the channel. Acceptable values are `all`, `activated`, and `deactivated`. (default: `activated`) (optional)
    nickname_startswith = "nickname_startswith_example" # str | Searches for members whose nicknames start with the specified value. Urlencoding the value is recommended. (optional)
    include_push_preference = True # bool | Determines whether to include information about the push preference of each member, such as `push_enabled`, `push_trigger_option`, and `do_not_disturb`. (Default: `false`) (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List members
        api_response = api_instance.list_members(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->list_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List members
        api_response = api_instance.list_members(channel_url, token=token, limit=limit, user_id=user_id, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, show_member_is_muted=show_member_is_muted, order=order, operator_filter=operator_filter, member_state_filter=member_state_filter, muted_member_filter=muted_member_filter, member_active_mode_filter=member_active_mode_filter, nickname_startswith=nickname_startswith, include_push_preference=include_push_preference, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->list_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **token** | **str**|  | [optional]
 **limit** | **int**| Specifies the number of results to return per page. Acceptable values are 1 to 100, inclusive. (Default: 10) | [optional]
 **user_id** | **str**| Specifies the unique ID of a user. If &#x60;user_id&#x60; is provided, the response will include two additional boolean properties about each user in the members list. - &#x60;is_blocking_me&#x60;: Indicates whether the listed user is blocking the user specified in the user_id parameter. - &#x60;is_blocked_by_me&#x60;: Indicates whether the listed user is blocked by the user specified in the user_id parameter. | [optional]
 **show_delivery_receipt** | **bool**|  | [optional]
 **show_read_receipt** | **bool**|  | [optional]
 **show_member_is_muted** | **bool**|  | [optional]
 **order** | **str**| Specifies the method to sort a list of results. Acceptable values are the following: - &#x60;member_nickname_alphabetical&#x60; (default): sorts by the member nicknames in alphabetical order. - &#x60;operator_then_member_alphabetical&#x60;: sorts by the operational role and member nickname in alphabetical order where channel operators are listed before channel members. | [optional]
 **operator_filter** | **str**| Restricts the search scope to only retrieve operators or non-operator members of the channel. Acceptable values are the following: - &#x60;all&#x60; (default): no filter is applied to the list. - &#x60;operator&#x60;: only channel operators are retrieved. - &#x60;nonoperator&#x60;: all channel members, except channel operators, are retrieved. | [optional]
 **member_state_filter** | **str**| Restricts the search scope to retrieve members based on if they have accepted an invitation or if they were invited by a friend. Acceptable values are &#x60;invited_only&#x60;, &#x60;joined_only&#x60;, &#x60;invited_by_friend&#x60;, &#x60;invited_by_non_friend&#x60;, and &#x60;all&#x60;. (Default: &#x60;all&#x60;) | [optional]
 **muted_member_filter** | **str**| Restricts the search scope to retrieve members who are muted or unmuted in the channel. Acceptable values are &#x60;all&#x60;, &#x60;muted&#x60;, and &#x60;unmuted&#x60;. (Default: &#x60;all&#x60;) | [optional]
 **member_active_mode_filter** | **str**| Restricts the search scope to retrieve members who are activated or deactivated in the channel. Acceptable values are &#x60;all&#x60;, &#x60;activated&#x60;, and &#x60;deactivated&#x60;. (default: &#x60;activated&#x60;) | [optional]
 **nickname_startswith** | **str**| Searches for members whose nicknames start with the specified value. Urlencoding the value is recommended. | [optional]
 **include_push_preference** | **bool**| Determines whether to include information about the push preference of each member, such as &#x60;push_enabled&#x60;, &#x60;push_trigger_option&#x60;, and &#x60;do_not_disturb&#x60;. (Default: &#x60;false&#x60;) | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**GroupChannelListMembersResponse**](GroupChannelListMembersResponse.md)

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

# **list_operators**
> ListOperatorsResponse list_operators(channel_url)

List operators

## List operators  You can retrieve a list of operators of a group channel using this API.  https://sendbird.com/docs/chat/platform-api/v3/user/assigning-a-user-role/list-operators-of-a-group-channel#1-list-operators-of-a-group-channel  `channel_url`   Type: string   Description: Specifies the URL of the channel to retrieve a list of operators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    token = "token_example" # str |  (optional)
    limit = 1 # int | Specifies the number of results to return per page. Acceptable values are 1 to 100, inclusive. (Default: 10) (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List operators
        api_response = api_instance.list_operators(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->list_operators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List operators
        api_response = api_instance.list_operators(channel_url, token=token, limit=limit, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->list_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **token** | **str**|  | [optional]
 **limit** | **int**| Specifies the number of results to return per page. Acceptable values are 1 to 100, inclusive. (Default: 10) | [optional]
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

# **register_operators_to_a_group_channel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} register_operators_to_a_group_channel(channel_url)

Register operators to a group channel

## Register operators to a group channel  You can register one or more operators to a group channel using this API.  https://sendbird.com/docs/chat/platform-api/v3/user/assigning-a-user-role/register-operators-to-a-group-channel#1-register-operators-to-a-group-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
    api_instance = group_channel_api.GroupChannelApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    register_operators_to_a_group_channel_request = RegisterOperatorsToAGroupChannelRequest(
        operator_ids=[
            "operator_ids_example",
        ],
    ) # RegisterOperatorsToAGroupChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register operators to a group channel
        api_response = api_instance.register_operators_to_a_group_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->register_operators_to_a_group_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register operators to a group channel
        api_response = api_instance.register_operators_to_a_group_channel(channel_url, api_token=api_token, register_operators_to_a_group_channel_request=register_operators_to_a_group_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->register_operators_to_a_group_channel: %s\n" % e)
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

# **reset_chat_history**
> ResetChatHistoryResponse reset_chat_history(channel_url)

Reset chat history

## Reset chat history  This action resets the properties related to a specific user's chat history in a [group channel](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-group-channel), clearing existing messages in a channel from only the specified user's end. Because this action doesn't delete messages from the Sendbird database, other members in the channel can still retrieve and see the messages.  This action clears the messages for the specified user by updating the `last_message` and `read_receipt` properties of the [group channel resource](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#4-list-of-properties-for-group-channels) in addition to other internally managed data such as the count of a user's unread messages.  Using the `reset_all` property, you can also reset the properties related to the chat history of all members in a group channel.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/reset-chat-history#1-reset-chat-history

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.reset_chat_history_request import ResetChatHistoryRequest
from sendbird_platform_sdk.model.reset_chat_history_response import ResetChatHistoryResponse
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
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    reset_chat_history_request = ResetChatHistoryRequest(
        reset_all=True,
        user_id="user_id_example",
    ) # ResetChatHistoryRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset chat history
        api_response = api_instance.reset_chat_history(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->reset_chat_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset chat history
        api_response = api_instance.reset_chat_history(channel_url, api_token=api_token, reset_chat_history_request=reset_chat_history_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->reset_chat_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **reset_chat_history_request** | [**ResetChatHistoryRequest**](ResetChatHistoryRequest.md)|  | [optional]

### Return type

[**ResetChatHistoryResponse**](ResetChatHistoryResponse.md)

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

# **start_typing_indicators**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} start_typing_indicators(channel_url)

Start typing indicators

## Start typing indicators  You can start showing a typing indicator using this API. Seeing whether other users are typing can help a more interactive conversation environment by showing real-time engagement of other users.  If you're looking for an easy way to show typing indicators on your app, check out Sendbird UIKit for a ready-to-use UI feature that can be customized to fit your needs.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-typing-indicators/start-typing-indicators#1-start-typing-indicators  `channel_url`   Type: string   Description: Specifies the URL of the channel to set typing indicators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.start_typing_indicators_request import StartTypingIndicatorsRequest
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
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    start_typing_indicators_request = StartTypingIndicatorsRequest(
        user_ids=[
            "user_ids_example",
        ],
    ) # StartTypingIndicatorsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start typing indicators
        api_response = api_instance.start_typing_indicators(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->start_typing_indicators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start typing indicators
        api_response = api_instance.start_typing_indicators(channel_url, api_token=api_token, start_typing_indicators_request=start_typing_indicators_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->start_typing_indicators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **start_typing_indicators_request** | [**StartTypingIndicatorsRequest**](StartTypingIndicatorsRequest.md)|  | [optional]

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

# **stop_typing_indicators**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} stop_typing_indicators(channel_url)

Stop typing indicators

## Stop typing indicators  You can stop showing a typing indicator using this API. To signal that a user is no longer typing, you can let the indicator disappear when the user sends a message or completely deletes the message text.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-typing-indicators/stop-typing-indicators#1-stop-typing-indicators  `channel_url`   Type: string   Description: Specifies the URL of the channel to set typing indicators.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.start_typing_indicators_request import StartTypingIndicatorsRequest
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
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    start_typing_indicators_request = StartTypingIndicatorsRequest(
        user_ids=[
            "user_ids_example",
        ],
    ) # StartTypingIndicatorsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop typing indicators
        api_response = api_instance.stop_typing_indicators(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->stop_typing_indicators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop typing indicators
        api_response = api_instance.stop_typing_indicators(channel_url, api_token=api_token, start_typing_indicators_request=start_typing_indicators_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->stop_typing_indicators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **start_typing_indicators_request** | [**StartTypingIndicatorsRequest**](StartTypingIndicatorsRequest.md)|  | [optional]

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

# **unhide_a_channel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unhide_a_channel(channel_url, user_id)

Unhide a channel

## Unhide a channel  This action lets a hidden [group channel](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-group-channel) reappear on the channel list of a specific user or every member in the group channel. Hiding or unhiding a channel lets users organize their channel list based on those that require the most attention. Note that only group channels can be hidden or unhidden.  [https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/unhide-a-channel#1-unhide-a-channel](https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/unhide-a-channel#1-unhide-a-channel)  `channel_url`   Type: string   Description: Specifies the URL of the channel to unhide or unarchive.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
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
    channel_url = "channel_url_example" # str | (Required) 
    user_id = "user_id_example" # str | (Required) 
    should_unhide_all = True # bool |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unhide a channel
        api_response = api_instance.unhide_a_channel(channel_url, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->unhide_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unhide a channel
        api_response = api_instance.unhide_a_channel(channel_url, user_id, should_unhide_all=should_unhide_all, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->unhide_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **user_id** | **str**| (Required)  |
 **should_unhide_all** | **bool**|  | [optional]
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

# **update_a_group_channel**
> SendbirdGroupChannelDetail update_a_group_channel(channel_url)

Update a group channel

## Update a group channel  You can update information about a group channel or a Supergroup channel using this API. You can't make any changes to the members of a channel with this API. To change members, see [invite as members](https://sendbird.com/docs/chat/platform-api/v3/channel/inviting-a-user/invite-as-members-channel) instead. See [this page](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-open-channel-vs-group-channel-vs-supergroup-channel) to learn more about channel types.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/update-a-group-channel#1-update-a-group-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api
from sendbird_platform_sdk.model.sendbird_group_channel_detail import SendbirdGroupChannelDetail
from sendbird_platform_sdk.model.update_a_group_channel_request import UpdateAGroupChannelRequest
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
    update_a_group_channel_request = UpdateAGroupChannelRequest(
        access_code="access_code_example",
        cover_file=open('/path/to/file', 'rb'),
        cover_url="cover_url_example",
        custom_type="custom_type_example",
        data="data_example",
        is_distinct=True,
        is_public=True,
        is_super=True,
        name="name_example",
        operator_ids=[
            "operator_ids_example",
        ],
    ) # UpdateAGroupChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a group channel
        api_response = api_instance.update_a_group_channel(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->update_a_group_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a group channel
        api_response = api_instance.update_a_group_channel(channel_url, api_token=api_token, update_a_group_channel_request=update_a_group_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling GroupChannelApi->update_a_group_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_a_group_channel_request** | [**UpdateAGroupChannelRequest**](UpdateAGroupChannelRequest.md)|  | [optional]

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

