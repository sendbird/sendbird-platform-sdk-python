# sendbird_platform_sdk.UserApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_a_registration_or_device_token**](UserApi.md#add_a_registration_or_device_token) | **POST** /v3/users/{user_id}/push/{token_type} | Add a registration or device token
[**choose_a_push_notification_content_template**](UserApi.md#choose_a_push_notification_content_template) | **PUT** /v3/users/{user_id}/push/template | Choose a push notification content template
[**create_a_user**](UserApi.md#create_a_user) | **POST** /v3/users | Create a user
[**create_user_token**](UserApi.md#create_user_token) | **POST** /v3/users/{user_id}/token | Create user token
[**delete_a_user**](UserApi.md#delete_a_user) | **DELETE** /v3/users/{user_id} | Delete a user
[**get_channel_invitation_preference**](UserApi.md#get_channel_invitation_preference) | **GET** /v3/users/{user_id}/channel_invitation_preference | Get channel invitation preference
[**leave_my_group_channels**](UserApi.md#leave_my_group_channels) | **PUT** /v3/users/{user_id}/my_group_channels/leave | Leave my group channels
[**list_my_group_channels**](UserApi.md#list_my_group_channels) | **GET** /v3/users/{user_id}/my_group_channels | List my group channels
[**list_registration_or_device_tokens**](UserApi.md#list_registration_or_device_tokens) | **GET** /v3/users/{user_id}/push/{token_type} | List registration or device tokens
[**list_users**](UserApi.md#list_users) | **GET** /v3/users | List users
[**mark_all_messages_as_read**](UserApi.md#mark_all_messages_as_read) | **PUT** /v3/users/{user_id}/mark_as_read_all | Mark all messages as read
[**remove_a_registration_or_device_token**](UserApi.md#remove_a_registration_or_device_token) | **DELETE** /v3/users/{user_id}/push/{token_type}/{token} | Remove a registration or device token - When unregistering a specific token
[**remove_a_registration_or_device_token_from_an_owner**](UserApi.md#remove_a_registration_or_device_token_from_an_owner) | **DELETE** /v3/push/device_tokens/{token_type}/{token} | Remove a registration or device token from an owner
[**remove_all_registration_or_device_token**](UserApi.md#remove_all_registration_or_device_token) | **DELETE** /v3/users/{user_id}/push | Remove a registration or device token - When unregistering all device tokens
[**reset_push_preferences**](UserApi.md#reset_push_preferences) | **DELETE** /v3/users/{user_id}/push_preference | Reset push preferences
[**update_a_user**](UserApi.md#update_a_user) | **PUT** /v3/users/{user_id} | Update a user
[**update_channel_invitation_preference**](UserApi.md#update_channel_invitation_preference) | **PUT** /v3/users/{user_id}/channel_invitation_preference | Update channel invitation preference
[**update_count_preference_of_a_channel**](UserApi.md#update_count_preference_of_a_channel) | **PUT** /v3/users/{user_id}/count_preference/{channel_url} | Update count preference of a channel
[**update_push_preferences**](UserApi.md#update_push_preferences) | **PUT** /v3/users/{user_id}/push_preference | Update push preferences
[**update_push_preferences_for_a_channel**](UserApi.md#update_push_preferences_for_a_channel) | **PUT** /v3/users/{user_id}/push_preference/{channel_url} | Update push preferences for a channel
[**view_a_user**](UserApi.md#view_a_user) | **GET** /v3/users/{user_id} | View a user
[**view_count_preference_of_a_channel**](UserApi.md#view_count_preference_of_a_channel) | **GET** /v3/users/{user_id}/count_preference/{channel_url} | View count preference of a channel
[**view_number_of_channels_with_unread_messages**](UserApi.md#view_number_of_channels_with_unread_messages) | **GET** /v3/users/{user_id}/unread_channel_count | View number of channels with unread messages
[**view_number_of_unread_messages**](UserApi.md#view_number_of_unread_messages) | **GET** /v3/users/{user_id}/unread_message_count | View number of unread messages
[**view_push_preferences**](UserApi.md#view_push_preferences) | **GET** /v3/users/{user_id}/push_preference | View push preferences
[**view_push_preferences_for_a_channel**](UserApi.md#view_push_preferences_for_a_channel) | **GET** /v3/users/{user_id}/push_preference/{channel_url} | View push preferences for a channel
[**view_who_owns_a_registration_or_device_token**](UserApi.md#view_who_owns_a_registration_or_device_token) | **GET** /v3/push/device_tokens/{token_type}/{token} | View who owns a registration or device token


# **add_a_registration_or_device_token**
> AddARegistrationOrDeviceTokenResponse add_a_registration_or_device_token(user_id, token_type)

Add a registration or device token

## Add a registration or device token  > __Note__: A user can have up to 20 FCM registration tokens, 20 HMS device tokens, and 20 APNs device tokens each. The oldest token will be deleted before a new token is added for a user who already has 20 registration or device tokens. Only the 20 newest tokens will be maintained for users who already have more than 20 of each token type.  To send notification requests to push notification services on behalf of your server, adds a specific user's FCM registration token, HMS device token, or APNs device token to Sendbird server. Depending on which push service you are using, you can pass one of two values in `token_type`: `gcm`, `huawei`, or `apns`.  A FCM registration token and an APNs device token allow identification of each client app instance on each device, and are generated and registered by Android and iOS apps through the corresponding SDKs. Use this method if you need to register a token via your own server.  > __Note__: For more information on the registration token and device token, visit the Google's [FCM](https://firebase.google.com/docs/auth/admin/verify-id-tokens) page, Huawei's [Push kit](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/service-introduction-0000001050040060) and Apple's [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html) page.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-add-a-registration-or-device-token ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.add_a_registration_or_device_token_request import AddARegistrationOrDeviceTokenRequest
from sendbird_platform_sdk.model.add_a_registration_or_device_token_response import AddARegistrationOrDeviceTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    token_type = "gcm" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_a_registration_or_device_token_request = AddARegistrationOrDeviceTokenRequest(
        apns_device_token="apns_device_token_example",
        gcm_reg_token="gcm_reg_token_example",
        huawei_device_token="huawei_device_token_example",
    ) # AddARegistrationOrDeviceTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a registration or device token
        api_response = api_instance.add_a_registration_or_device_token(user_id, token_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->add_a_registration_or_device_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a registration or device token
        api_response = api_instance.add_a_registration_or_device_token(user_id, token_type, api_token=api_token, add_a_registration_or_device_token_request=add_a_registration_or_device_token_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->add_a_registration_or_device_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **token_type** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **add_a_registration_or_device_token_request** | [**AddARegistrationOrDeviceTokenRequest**](AddARegistrationOrDeviceTokenRequest.md)|  | [optional]

### Return type

[**AddARegistrationOrDeviceTokenResponse**](AddARegistrationOrDeviceTokenResponse.md)

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

# **choose_a_push_notification_content_template**
> ChooseAPushNotificationContentTemplateResponse choose_a_push_notification_content_template(user_id)

Choose a push notification content template

## Choose a push notification content template  Users can choose a template to determine how push notifications appear to them. Push notification content templates are pre-formatted forms that can be customized to display your own push notification messages on a user's device. Sendbird provides two types: `default` and `alternative`. Go to **Settings** > **Chat** > **Push notifications** > **Push notification content templates** on [Sendbird Dashboard](https://dashboard.sendbird.com/auth/signin) to customize the templates.  If the `push_message_template` property is specified when [sending a message](https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/send-a-message), the content template customized for the message takes precedence over the user's choice.  > **Note**: Push notifications are only available for group channels.      https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/choose-a-push-notification-content-template#1-choose-a-push-notification-content-template

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.choose_a_push_notification_content_template_response import ChooseAPushNotificationContentTemplateResponse
from sendbird_platform_sdk.model.choose_a_push_notification_content_template_request import ChooseAPushNotificationContentTemplateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    choose_a_push_notification_content_template_request = ChooseAPushNotificationContentTemplateRequest(
        name="default",
    ) # ChooseAPushNotificationContentTemplateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Choose a push notification content template
        api_response = api_instance.choose_a_push_notification_content_template(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->choose_a_push_notification_content_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Choose a push notification content template
        api_response = api_instance.choose_a_push_notification_content_template(user_id, api_token=api_token, choose_a_push_notification_content_template_request=choose_a_push_notification_content_template_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->choose_a_push_notification_content_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **choose_a_push_notification_content_template_request** | [**ChooseAPushNotificationContentTemplateRequest**](ChooseAPushNotificationContentTemplateRequest.md)|  | [optional]

### Return type

[**ChooseAPushNotificationContentTemplateResponse**](ChooseAPushNotificationContentTemplateResponse.md)

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

# **create_a_user**
> SendbirdUser create_a_user()

Create a user

## Create a user  You should create a user in your Sendbird application to initiate conversations in channels. A user is identified by its unique user ID, and additionally have a changeable nickname, profile image, and so on. Users are at the core of all conversations. Sendbird applications are made up of users who chat in either Open Channels or Group Channels. Using this API, it is possible to have fine grained control over your users and what those users can do. To learn more about users, see [User overview](https://sendbird.com/docs/chat/platform-api/v3/user/user-overview#2-resource-representation).  https://sendbird.com/docs/chat/platform-api/v3/user/creating-users/create-a-user#1-create-a-user

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.sendbird_user import SendbirdUser
from sendbird_platform_sdk.model.create_a_user_request import CreateAUserRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_a_user_request = CreateAUserRequest(
        discovery_keys=[
            "discovery_keys_example",
        ],
        issue_access_token=True,
        metadata={},
        nickname="nickname_example",
        profile_file=open('/path/to/file', 'rb'),
        profile_url="profile_url_example",
        user_id="user_id_example",
    ) # CreateAUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a user
        api_response = api_instance.create_a_user(api_token=api_token, create_a_user_request=create_a_user_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->create_a_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **create_a_user_request** | [**CreateAUserRequest**](CreateAUserRequest.md)|  | [optional]

### Return type

[**SendbirdUser**](SendbirdUser.md)

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

# **create_user_token**
> CreateUserTokenResponse create_user_token(user_id)

Create user token

## Create user token  This action issues a session token for user authentication. Session tokens provide an efficient stateless authentication method by not storing the tokens in the Sendbird database, and thus improving the server's performance. See [access token vs. session token](https://sendbird.com/docs/chat/platform-api/v3/user/creating-users/create-a-user#2-access-token-vs-session-token) to learn more about authenticating users.  > **Note**: The endpoint `/users/{user_id}` is deprecated. Use `/users/{user_id}/token` for greater efficiency.      https://sendbird.com/docs/chat/platform-api/v3/user/managing-session-tokens/issue-a-session-token#1-issue-a-session-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.create_user_token_request import CreateUserTokenRequest
from sendbird_platform_sdk.model.create_user_token_response import CreateUserTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_user_token_request = CreateUserTokenRequest(
        expires_at=1,
    ) # CreateUserTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create user token
        api_response = api_instance.create_user_token(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->create_user_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create user token
        api_response = api_instance.create_user_token(user_id, api_token=api_token, create_user_token_request=create_user_token_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->create_user_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **create_user_token_request** | [**CreateUserTokenRequest**](CreateUserTokenRequest.md)|  | [optional]

### Return type

[**CreateUserTokenResponse**](CreateUserTokenResponse.md)

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

# **delete_a_user**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_a_user(user_id)

Delete a user

## Delete a user  You can delete a user from your Sendbird application using this API.  > **Note**: This API deletes user data and metadata, except for their messages. If you wish to delete user data including their messages, use the [GDPR request](https://sendbird.com/docs/chat/platform-api/v3/privacy/privacy-overview).      [https://sendbird.com/docs/chat/platform-api/v3/user/managing-users/delete-a-user#1-delete-a-user](https://sendbird.com/docs/chat/platform-api/v3/user/managing-users/delete-a-user#1-delete-a-user)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a user
        api_response = api_instance.delete_a_user(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->delete_a_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a user
        api_response = api_instance.delete_a_user(user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->delete_a_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
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

# **get_channel_invitation_preference**
> GetChannelInvitationPreferenceResponse get_channel_invitation_preference(user_id)

Get channel invitation preference

## Get channel invitation preference  This action retrieves a user's [group channel](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-group-channel) invitation preference. Users are subject to both user-specific and application-wide invitation preferences. Of the two, the invitation preference set for a specific user takes precedence over [the default channel invitation preference](https://sendbird.com/docs/chat/platform-api/v3/channel/setting-up-channels/get-default-invitation-preference).  [https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/get-channel-invitation-preference#1-get-channel-invitation-preference](https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/get-channel-invitation-preference#1-get-channel-invitation-preference)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.get_channel_invitation_preference_response import GetChannelInvitationPreferenceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get channel invitation preference
        api_response = api_instance.get_channel_invitation_preference(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->get_channel_invitation_preference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get channel invitation preference
        api_response = api_instance.get_channel_invitation_preference(user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->get_channel_invitation_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**GetChannelInvitationPreferenceResponse**](GetChannelInvitationPreferenceResponse.md)

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

# **leave_my_group_channels**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} leave_my_group_channels(user_id)

Leave my group channels

## Leave my group channels  This action allows a user to leave all group channels or channels with a specific custom type. This API is useful if you want to let a user leave a set of channels at once. To let a user leave only one of their group channels, use the [leave a channel API](https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/leave-a-channel) instead.  Since this API can't be called for a deactivated user, ensure that the [<code>leave_all_when_deactivated</code>](https://sendbird.com/docs/chat/platform-api/v3/user/managing-users/update-a-user#2-request-body) property of the user is set to its default value of `true` to let the user leave all joined group channels upon deactivation.  https://sendbird.com/docs/chat/platform-api/v3/user/managing-joined-group-channels/leave-group-channels#1-leave-group-channels  `user_id`   Type: string   Description: Specifies the unique ID of the user to leave all joined group channels.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.leave_my_group_channels_request import LeaveMyGroupChannelsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    leave_my_group_channels_request = LeaveMyGroupChannelsRequest(
        custom_type="custom_type_example",
    ) # LeaveMyGroupChannelsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Leave my group channels
        api_response = api_instance.leave_my_group_channels(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->leave_my_group_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Leave my group channels
        api_response = api_instance.leave_my_group_channels(user_id, api_token=api_token, leave_my_group_channels_request=leave_my_group_channels_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->leave_my_group_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **leave_my_group_channels_request** | [**LeaveMyGroupChannelsRequest**](LeaveMyGroupChannelsRequest.md)|  | [optional]

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

# **list_my_group_channels**
> ListMyGroupChannelsResponse list_my_group_channels(user_id, api_token)

List my group channels

## List my group channels  This action retrieves a list of [group channels](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-group-channel) that a specific user has joined. You can use various query parameters to determine the search scope and select what kind of information you want to receive about the queried channels.  If you're looking to retrieve a list of group channels in a specific application, visit the [list group channels](https://sendbird.com/docs/chat/platform-api/v3/channel/listing-channels-in-an-application/list-group-channels) page under the Channel section.  https://sendbird.com/docs/chat/platform-api/v3/user/managing-joined-group-channels/list-group-channels-by-user#1-list-group-channels-by-user  `user_id`   Type: string   Description: Specifies the unique ID of the target user.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.list_my_group_channels_response import ListMyGroupChannelsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
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
    members_nickname_startswith = "members_nickname_startswith_example" # str | Searches for group channels with members whose nicknames begin with the specified value. This parameter isn't case-sensitive. URL encoding the value is recommended. (optional)
    search_query = "search_query_example" # str | Searches for group channels where the specified query string matches the channel name or the nickname of the member. This parameter isn't case-sensitive and should be specified in conjunction with the search_fields parameter below. URL encoding the value is recommended. (optional)
    search_fields = "search_fields_example" # str | Specifies a comma-separated string of one or more search fields to apply to the query, which restricts the results within the specified fields (OR search condition). Acceptable values are channel_name and member_nickname. This is effective only when the search_query parameter above is specified. (Default: channel_name, member_nickname together) (optional)
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
    hidden_mode = "unhidden_only" # str | Restricts the search scope to group channels that match a specific hidden_status and operating behavior (optional)
    unread_filter = "all" # str | Restricts the search scope to only retrieve group channels with one or more unread messages. This filter doesn't support Supergroup channels. Acceptable values are all and unread_message. (Default: all) (optional)
    member_state_filter = "all" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List my group channels
        api_response = api_instance.list_my_group_channels(user_id, api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_my_group_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List my group channels
        api_response = api_instance.list_my_group_channels(user_id, api_token, token=token, limit=limit, distinct_mode=distinct_mode, public_mode=public_mode, super_mode=super_mode, created_after=created_after, created_before=created_before, show_empty=show_empty, show_member=show_member, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, show_metadata=show_metadata, show_frozen=show_frozen, order=order, metadata_order_key=metadata_order_key, custom_types=custom_types, custom_type_startswith=custom_type_startswith, channel_urls=channel_urls, name=name, name_contains=name_contains, name_startswith=name_startswith, members_exactly_in=members_exactly_in, members_include_in=members_include_in, query_type=query_type, members_nickname=members_nickname, members_nickname_contains=members_nickname_contains, members_nickname_startswith=members_nickname_startswith, search_query=search_query, search_fields=search_fields, metadata_key=metadata_key, metadata_values=metadata_values, metadata_value_startswith=metadata_value_startswith, metacounter_key=metacounter_key, metacounter_values=metacounter_values, metacounter_value_gt=metacounter_value_gt, metacounter_value_gte=metacounter_value_gte, metacounter_value_lt=metacounter_value_lt, metacounter_value_lte=metacounter_value_lte, include_sorted_metaarray_in_last_message=include_sorted_metaarray_in_last_message, hidden_mode=hidden_mode, unread_filter=unread_filter, member_state_filter=member_state_filter)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_my_group_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
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
 **members_nickname_startswith** | **str**| Searches for group channels with members whose nicknames begin with the specified value. This parameter isn&#39;t case-sensitive. URL encoding the value is recommended. | [optional]
 **search_query** | **str**| Searches for group channels where the specified query string matches the channel name or the nickname of the member. This parameter isn&#39;t case-sensitive and should be specified in conjunction with the search_fields parameter below. URL encoding the value is recommended. | [optional]
 **search_fields** | **str**| Specifies a comma-separated string of one or more search fields to apply to the query, which restricts the results within the specified fields (OR search condition). Acceptable values are channel_name and member_nickname. This is effective only when the search_query parameter above is specified. (Default: channel_name, member_nickname together) | [optional]
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
 **hidden_mode** | **str**| Restricts the search scope to group channels that match a specific hidden_status and operating behavior | [optional]
 **unread_filter** | **str**| Restricts the search scope to only retrieve group channels with one or more unread messages. This filter doesn&#39;t support Supergroup channels. Acceptable values are all and unread_message. (Default: all) | [optional]
 **member_state_filter** | **str**|  | [optional]

### Return type

[**ListMyGroupChannelsResponse**](ListMyGroupChannelsResponse.md)

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

# **list_registration_or_device_tokens**
> ListRegistrationOrDeviceTokensResponse list_registration_or_device_tokens(user_id, token_type)

List registration or device tokens

## List registration or device tokens  Retrieves a list of a user's registration or device tokens. You can pass `gcm`, `huawei`, or `apns` for FCM registration token, HMS device token, or APNs device token, respectively, in the `token_type` parameter for the push notification service you are using.  https://sendbird.com/docs/chat/platform-api/v3/user/managing-device-tokens/list-registration-or-device-tokens#1-list-registration-or-device-tokens

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.list_registration_or_device_tokens_response import ListRegistrationOrDeviceTokensResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    token_type = "gcm" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List registration or device tokens
        api_response = api_instance.list_registration_or_device_tokens(user_id, token_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_registration_or_device_tokens: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List registration or device tokens
        api_response = api_instance.list_registration_or_device_tokens(user_id, token_type, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_registration_or_device_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **token_type** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**ListRegistrationOrDeviceTokensResponse**](ListRegistrationOrDeviceTokensResponse.md)

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

# **list_users**
> ListUsersResponse list_users()

List users

## List users  You can retrieve a list of users in your Sendbird application using this API. You can generate a customized list using various parameter combinations.  https://sendbird.com/docs/chat/platform-api/v3/user/listing-users/list-users#1-list-users

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.list_users_response import ListUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    active_mode = "activated" # str | Specifies the activation status of the users in the list. Acceptable values are `activated`, `deactivated`, and `all`. (Default: `activated`) (optional)
    show_bot = True # bool | Determines whether to include bots in the list. (Default: true) (optional)
    user_ids = "user_ids_example" # str | Specifies the user IDs. The value should be a comma-separated string that consists of multiple urlencoded user IDs. An example of a urlencoded string is ?user_ids=urlencoded_id_1,urlencoded_id_2. * The maximum number of user IDs in this parameter is 250. If you exceed the maximum number, your request may receive an HTTP 414 error indicating that the request URL is longer than what Sendbird server can interpret. (optional)
    nickname = "nickname_example" # str |  (optional)
    nickname_startswith = "nickname_startswith_example" # str |  (optional)
    metadatakey = "metadatakey_example" # str |  (optional)
    metadatavalues_in = "metadatavalues_in_example" # str | Searches for blocked users with metadata containing an item with the key specified by the metadatakey parameter above, and the value of that item matches one or more values specified by this parameter. The string should be specified with multiple urlencoded metadata values separated by commas (for example, `?metadatavalues_in=urlencoded_value_1, urlencoded_value_2`). This parameter should be specified in conjunction with the `metadatakey` above. (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List users
        api_response = api_instance.list_users(token=token, limit=limit, active_mode=active_mode, show_bot=show_bot, user_ids=user_ids, nickname=nickname, nickname_startswith=nickname_startswith, metadatakey=metadatakey, metadatavalues_in=metadatavalues_in, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **active_mode** | **str**| Specifies the activation status of the users in the list. Acceptable values are &#x60;activated&#x60;, &#x60;deactivated&#x60;, and &#x60;all&#x60;. (Default: &#x60;activated&#x60;) | [optional]
 **show_bot** | **bool**| Determines whether to include bots in the list. (Default: true) | [optional]
 **user_ids** | **str**| Specifies the user IDs. The value should be a comma-separated string that consists of multiple urlencoded user IDs. An example of a urlencoded string is ?user_ids&#x3D;urlencoded_id_1,urlencoded_id_2. * The maximum number of user IDs in this parameter is 250. If you exceed the maximum number, your request may receive an HTTP 414 error indicating that the request URL is longer than what Sendbird server can interpret. | [optional]
 **nickname** | **str**|  | [optional]
 **nickname_startswith** | **str**|  | [optional]
 **metadatakey** | **str**|  | [optional]
 **metadatavalues_in** | **str**| Searches for blocked users with metadata containing an item with the key specified by the metadatakey parameter above, and the value of that item matches one or more values specified by this parameter. The string should be specified with multiple urlencoded metadata values separated by commas (for example, &#x60;?metadatavalues_in&#x3D;urlencoded_value_1, urlencoded_value_2&#x60;). This parameter should be specified in conjunction with the &#x60;metadatakey&#x60; above. | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

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

# **mark_all_messages_as_read**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} mark_all_messages_as_read(user_id)

Mark all messages as read

## Mark all messages as read  This action marks all of a user's unread messages as read in certain group channels. If channels aren't specified, the user's unread messages in all group channels are marked as read.  https://sendbird.com/docs/chat/platform-api/v3/user/marking-messages-as-read/mark-all-of-a-users-messages-as-read#1-mark-all-of-a-user-s-messages-as-read

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.mark_all_messages_as_read_request import MarkAllMessagesAsReadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    mark_all_messages_as_read_request = MarkAllMessagesAsReadRequest(
        channel_urls=[
            "channel_urls_example",
        ],
    ) # MarkAllMessagesAsReadRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mark all messages as read
        api_response = api_instance.mark_all_messages_as_read(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->mark_all_messages_as_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark all messages as read
        api_response = api_instance.mark_all_messages_as_read(user_id, api_token=api_token, mark_all_messages_as_read_request=mark_all_messages_as_read_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->mark_all_messages_as_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **mark_all_messages_as_read_request** | [**MarkAllMessagesAsReadRequest**](MarkAllMessagesAsReadRequest.md)|  | [optional]

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

# **remove_a_registration_or_device_token**
> RemoveARegistrationOrDeviceTokenResponse remove_a_registration_or_device_token(user_id, token_type, token)

Remove a registration or device token - When unregistering a specific token

## Remove a registration or device token  Removes a user's specific registration or device token or all tokens. You can pass `gcm`, `huawei`, or `apns` for FCM registration token, HMS device token, or APNs device token, respectively, in the `token_type` parameter for the push notification service you are using.  https://sendbird.com/docs/chat/platform-api/v3/user/managing-device-tokens/remove-a-registration-or-device-token#1-remove-a-registration-or-device-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.remove_a_registration_or_device_token_response import RemoveARegistrationOrDeviceTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    token_type = "gcm" # str | (Required) 
    token = "token_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a registration or device token - When unregistering a specific token
        api_response = api_instance.remove_a_registration_or_device_token(user_id, token_type, token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_a_registration_or_device_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a registration or device token - When unregistering a specific token
        api_response = api_instance.remove_a_registration_or_device_token(user_id, token_type, token, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_a_registration_or_device_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **token_type** | **str**| (Required)  |
 **token** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**RemoveARegistrationOrDeviceTokenResponse**](RemoveARegistrationOrDeviceTokenResponse.md)

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

# **remove_a_registration_or_device_token_from_an_owner**
> RemoveARegistrationOrDeviceTokenFromAnOwnerResponse remove_a_registration_or_device_token_from_an_owner(token_type, token)

Remove a registration or device token from an owner

## Remove a registration or device token from an owner  Removes a registration or device token from a user who is the owner of the token. You can pass `gcm`, `huawei`, or `apns` for FCM registration token, HMS device token, or APNs device token, respectively, in the `token_type` parameter for the push notification service you are using.  https://sendbird.com/docs/chat/platform-api/v3/user/managing-device-tokens/remove-a-registration-or-device-token-from-an-owner#1-remove-a-registration-or-device-token-from-an-owner

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.remove_a_registration_or_device_token_from_an_owner_response import RemoveARegistrationOrDeviceTokenFromAnOwnerResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    token_type = "token_type_example" # str | (Required) 
    token = "token_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a registration or device token from an owner
        api_response = api_instance.remove_a_registration_or_device_token_from_an_owner(token_type, token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_a_registration_or_device_token_from_an_owner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a registration or device token from an owner
        api_response = api_instance.remove_a_registration_or_device_token_from_an_owner(token_type, token, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_a_registration_or_device_token_from_an_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type** | **str**| (Required)  |
 **token** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**RemoveARegistrationOrDeviceTokenFromAnOwnerResponse**](RemoveARegistrationOrDeviceTokenFromAnOwnerResponse.md)

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

# **remove_all_registration_or_device_token**
> RemoveAllRegistrationOrDeviceTokenResponse remove_all_registration_or_device_token(user_id)

Remove a registration or device token - When unregistering all device tokens

## Remove a registration or device token  Removes a user's specific registration or device token or all tokens. You can pass `gcm`, `huawei`, or `apns` for FCM registration token, HMS device token, or APNs device token, respectively, in the `token_type` parameter for the push notification service you are using.  https://sendbird.com/docs/chat/platform-api/v3/user/managing-device-tokens/remove-a-registration-or-device-token#1-remove-a-registration-or-device-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.remove_all_registration_or_device_token_response import RemoveAllRegistrationOrDeviceTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a registration or device token - When unregistering all device tokens
        api_response = api_instance.remove_all_registration_or_device_token(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_all_registration_or_device_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a registration or device token - When unregistering all device tokens
        api_response = api_instance.remove_all_registration_or_device_token(user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_all_registration_or_device_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**RemoveAllRegistrationOrDeviceTokenResponse**](RemoveAllRegistrationOrDeviceTokenResponse.md)

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

# **reset_push_preferences**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} reset_push_preferences(user_id)

Reset push preferences

## Reset push preferences  You can reset a user's notifications preferences. The values are reset to the default as the following.  - The values for the `do_not_disturb` and `snooze_enabled` properties are set to `false`.      - The values of the parameters associated with the time frame are all set to `0`.      - The value for the `timezone` property is set to `UTC`.      - The value for the `push_sound` property is set to `default`.       > **Note**: Push notifications are only available for group channels.      [https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/reset-push-notification-preferences#1-reset-push-notification-preferences](https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/reset-push-notification-preferences#1-reset-push-notification-preferences)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset push preferences
        api_response = api_instance.reset_push_preferences(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->reset_push_preferences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset push preferences
        api_response = api_instance.reset_push_preferences(user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->reset_push_preferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
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

# **update_a_user**
> SendbirdUser update_a_user(user_id)

Update a user

## Update a user  You can update information about a user using this API. In addition to changing a user's nickname or profile image, you can issue a new access token for the user. The new access token replaces the previous one as the necessary token for authentication.  You can also deactivate or reactivate a user using this API request. If the `leave_all_when_deactivated` is set to `true`, a user leaves all joined group channels and becomes deactivated.  > **Note**: Issuing session tokens through the `/users/{user_id}` endpoint is now deprecated and it&apos;s replaced with [&lt;code&gt;/users/{user_id}/token&lt;/code&gt;](https://sendbird.com/docs/chat/platform-api/v3/user/managing-session-tokens/issue-a-session-token) endpoint for greater efficiency. For those who are currently using the old endpoint, you can start issuing tokens using the new endpoint.      [https://sendbird.com/docs/chat/platform-api/v3/user/managing-users/update-a-user#1-update-a-user](https://sendbird.com/docs/chat/platform-api/v3/user/managing-users/update-a-user#1-update-a-user)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_a_user_request import UpdateAUserRequest
from sendbird_platform_sdk.model.sendbird_user import SendbirdUser
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_a_user_request = UpdateAUserRequest(
        discovery_keys=[
            "discovery_keys_example",
        ],
        is_active=True,
        issue_access_token=True,
        last_seen_at=1,
        leave_all_when_deactivated=True,
        nickname="nickname_example",
        preferred_languages=[
            "preferred_languages_example",
        ],
        profile_file=open('/path/to/file', 'rb'),
        profile_url="profile_url_example",
    ) # UpdateAUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a user
        api_response = api_instance.update_a_user(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_a_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a user
        api_response = api_instance.update_a_user(user_id, api_token=api_token, update_a_user_request=update_a_user_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_a_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_a_user_request** | [**UpdateAUserRequest**](UpdateAUserRequest.md)|  | [optional]

### Return type

[**SendbirdUser**](SendbirdUser.md)

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

# **update_channel_invitation_preference**
> UpdateChannelInvitationPreferenceResponse update_channel_invitation_preference(user_id)

Update channel invitation preference

## Update channel invitation preference  This action updates a user's [group channel](https://sendbird.com/docs/chat/platform-api/v3/channel/channel-overview#2-channel-types-3-group-channel) invitation preference. Updating the [application's default channel invitation preference](https://sendbird.com/docs/chat/platform-api/v3/channel/setting-up-channels/update-default-invitation-preference) won't override existing users' individual channel invitation preferences. The changed preference only affects the users created after the update.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-a-channel/update-channel-invitation-preference#1-update-channel-invitation-preference

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_channel_invitation_preference_response import UpdateChannelInvitationPreferenceResponse
from sendbird_platform_sdk.model.update_channel_invitation_preference_request import UpdateChannelInvitationPreferenceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_channel_invitation_preference_request = UpdateChannelInvitationPreferenceRequest(
        auto_accept=True,
    ) # UpdateChannelInvitationPreferenceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update channel invitation preference
        api_response = api_instance.update_channel_invitation_preference(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_channel_invitation_preference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update channel invitation preference
        api_response = api_instance.update_channel_invitation_preference(user_id, api_token=api_token, update_channel_invitation_preference_request=update_channel_invitation_preference_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_channel_invitation_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_channel_invitation_preference_request** | [**UpdateChannelInvitationPreferenceRequest**](UpdateChannelInvitationPreferenceRequest.md)|  | [optional]

### Return type

[**UpdateChannelInvitationPreferenceResponse**](UpdateChannelInvitationPreferenceResponse.md)

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

# **update_count_preference_of_a_channel**
> UpdateCountPreferenceOfChannelByUrlResponse update_count_preference_of_a_channel(user_id, channel_url)

Update count preference of a channel

## Update count preference of a channel  This action updates a user's count preference of a specific group channel. The count preference allows a user to either update the number of unread messages or the number of unread mentioned messages, or both in a specific group channel.  If you want to retrieve the total number count of a specific group channel, go to the [get count preference of a channel](https://sendbird.com/docs/chat/platform-api/v3/user/managing-unread-count/get-count-preference-of-a-channel) page.  https://sendbird.com/docs/chat/platform-api/v3/user/managing-unread-count/update-count-preference-of-a-channel#1-update-count-preference-of-a-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_count_preference_of_a_channel_request import UpdateCountPreferenceOfAChannelRequest
from sendbird_platform_sdk.model.update_count_preference_of_channel_by_url_response import UpdateCountPreferenceOfChannelByUrlResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_count_preference_of_a_channel_request = UpdateCountPreferenceOfAChannelRequest(
        count_preference="false",
    ) # UpdateCountPreferenceOfAChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update count preference of a channel
        api_response = api_instance.update_count_preference_of_a_channel(user_id, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_count_preference_of_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update count preference of a channel
        api_response = api_instance.update_count_preference_of_a_channel(user_id, channel_url, api_token=api_token, update_count_preference_of_a_channel_request=update_count_preference_of_a_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_count_preference_of_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_count_preference_of_a_channel_request** | [**UpdateCountPreferenceOfAChannelRequest**](UpdateCountPreferenceOfAChannelRequest.md)|  | [optional]

### Return type

[**UpdateCountPreferenceOfChannelByUrlResponse**](UpdateCountPreferenceOfChannelByUrlResponse.md)

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

# **update_push_preferences**
> UpdatePushPreferencesResponse update_push_preferences(user_id)

Update push preferences

## Update push preferences  You can update a user's notifications preferences. A push notification is a message that is immediately delivered to a user's device when the device is either idle or running the client app in the background.  > **Note**: Push notifications are only available for group channels.      [https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/update-push-notification-preferences#1-update-push-notification-preferences](https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/update-push-notification-preferences#1-update-push-notification-preferences)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_push_preferences_request import UpdatePushPreferencesRequest
from sendbird_platform_sdk.model.update_push_preferences_response import UpdatePushPreferencesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_push_preferences_request = UpdatePushPreferencesRequest(
        block_push_from_bots=True,
        do_not_disturb=True,
        enable_push_for_replies=True,
        end_hour=1,
        end_min=1,
        push_blocked_bot_ids=[
            "push_blocked_bot_ids_example",
        ],
        push_sound="push_sound_example",
        push_trigger_option=SendbirdPushTriggerOption("all"),
        snooze_enabled=True,
        snooze_end_ts=1,
        snooze_start_ts=1,
        start_hour=1,
        start_min=1,
        timezone="timezone_example",
    ) # UpdatePushPreferencesRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update push preferences
        api_response = api_instance.update_push_preferences(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_push_preferences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update push preferences
        api_response = api_instance.update_push_preferences(user_id, api_token=api_token, update_push_preferences_request=update_push_preferences_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_push_preferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_push_preferences_request** | [**UpdatePushPreferencesRequest**](UpdatePushPreferencesRequest.md)|  | [optional]

### Return type

[**UpdatePushPreferencesResponse**](UpdatePushPreferencesResponse.md)

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

# **update_push_preferences_for_a_channel**
> UpdatePushPreferencesForAChannelResponse update_push_preferences_for_a_channel(user_id, channel_url)

Update push preferences for a channel

## Update push preferences for a channel  You can update a user's notifications preferences for a specific channel. A push notification is a message that is immediately delivered to a user's device when the device is either idle or running the client app in the background.  > **Note**: Push notifications are only available for group channels.      [https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/update-push-notification-preferences-for-a-channel#1-update-push-notification-preferences-for-a-channel](https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/update-push-notification-preferences-for-a-channel#1-update-push-notification-preferences-for-a-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_push_preferences_for_a_channel_response import UpdatePushPreferencesForAChannelResponse
from sendbird_platform_sdk.model.update_push_preferences_for_a_channel_request import UpdatePushPreferencesForAChannelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_push_preferences_for_a_channel_request = UpdatePushPreferencesForAChannelRequest(
        push_trigger_option="default",
        push_sound="push_sound_example",
    ) # UpdatePushPreferencesForAChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update push preferences for a channel
        api_response = api_instance.update_push_preferences_for_a_channel(user_id, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_push_preferences_for_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update push preferences for a channel
        api_response = api_instance.update_push_preferences_for_a_channel(user_id, channel_url, api_token=api_token, update_push_preferences_for_a_channel_request=update_push_preferences_for_a_channel_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_push_preferences_for_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_push_preferences_for_a_channel_request** | [**UpdatePushPreferencesForAChannelRequest**](UpdatePushPreferencesForAChannelRequest.md)|  | [optional]

### Return type

[**UpdatePushPreferencesForAChannelResponse**](UpdatePushPreferencesForAChannelResponse.md)

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

# **view_a_user**
> SendbirdUser view_a_user(user_id)

View a user

## View a user  You can retrieve information about a user using this API.  https://sendbird.com/docs/chat/platform-api/v3/user/listing-users/get-a-user#1-get-a-user  `user_id`   Type: string   Description: Specifies the unique ID of the user to retrieve.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.sendbird_user import SendbirdUser
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    include_unread_count = True # bool |  (optional)
    custom_types = "custom_types_example" # str |  (optional)
    super_mode = "all" # str | Restricts the search scope to retrieve only Supergroup or non-Supergroup channels. Acceptable values are `all`, `super`, and `nonsuper`. This parameter should be specified in conjunction with `include_unread_count` above. (Default: `all`) (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a user
        api_response = api_instance.view_a_user(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_a_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a user
        api_response = api_instance.view_a_user(user_id, include_unread_count=include_unread_count, custom_types=custom_types, super_mode=super_mode, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_a_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **include_unread_count** | **bool**|  | [optional]
 **custom_types** | **str**|  | [optional]
 **super_mode** | **str**| Restricts the search scope to retrieve only Supergroup or non-Supergroup channels. Acceptable values are &#x60;all&#x60;, &#x60;super&#x60;, and &#x60;nonsuper&#x60;. This parameter should be specified in conjunction with &#x60;include_unread_count&#x60; above. (Default: &#x60;all&#x60;) | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**SendbirdUser**](SendbirdUser.md)

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

# **view_count_preference_of_a_channel**
> ViewCountPreferenceOfAChannelResponse view_count_preference_of_a_channel(user_id, channel_url)

View count preference of a channel

## View count preference of a channel  This action retrieves a user's count preference of a specific group channel. The count preference allows a user to either retrieve the number of unread messages or unread mentioned messages, or both in a specific group channel.  If you want to update the total number count of a specific group channel, visit the [update count preference of a channel](https://sendbird.com/docs/chat/platform-api/v3/user/managing-unread-count/update-count-preference-of-a-channel).  https://sendbird.com/docs/chat/platform-api/v3/user/managing-unread-count/get-count-preference-of-a-channel#1-get-count-preference-of-a-channel

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_count_preference_of_a_channel_response import ViewCountPreferenceOfAChannelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View count preference of a channel
        api_response = api_instance.view_count_preference_of_a_channel(user_id, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_count_preference_of_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View count preference of a channel
        api_response = api_instance.view_count_preference_of_a_channel(user_id, channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_count_preference_of_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewCountPreferenceOfAChannelResponse**](ViewCountPreferenceOfAChannelResponse.md)

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

# **view_number_of_channels_with_unread_messages**
> ViewNumberOfChannelsWithUnreadMessagesResponse view_number_of_channels_with_unread_messages(user_id)

View number of channels with unread messages

## View number of channels with unread messages  This action retrieves the total number of group channels in which a user has unread messages. You can use various query parameters to determine the search scope of group channels.  https://sendbird.com/docs/chat/platform-api/v3/user/managing-unread-count/get-number-of-channels-with-unread-messages#1-get-number-of-channels-with-unread-messages

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_number_of_channels_with_unread_messages_response import ViewNumberOfChannelsWithUnreadMessagesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    custom_types = "custom_types_example" # str |  (optional)
    super_mode = "all" # str | Restricts the search scope to either Supergroup channels or non-Supergroup channels or both. Acceptable values are all, super, and nonsuper. (Default: all) (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View number of channels with unread messages
        api_response = api_instance.view_number_of_channels_with_unread_messages(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_channels_with_unread_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of channels with unread messages
        api_response = api_instance.view_number_of_channels_with_unread_messages(user_id, custom_types=custom_types, super_mode=super_mode, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_channels_with_unread_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **custom_types** | **str**|  | [optional]
 **super_mode** | **str**| Restricts the search scope to either Supergroup channels or non-Supergroup channels or both. Acceptable values are all, super, and nonsuper. (Default: all) | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**ViewNumberOfChannelsWithUnreadMessagesResponse**](ViewNumberOfChannelsWithUnreadMessagesResponse.md)

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

# **view_number_of_unread_messages**
> ViewNumberOfUnreadMessagesResponse view_number_of_unread_messages(user_id)

View number of unread messages

## View number of unread messages  This action retrieves a user's total number of unread messages in group channels.  > **Note**: The unread count feature is only available for group channels.      [https://sendbird.com/docs/chat/platform-api/v3/user/managing-unread-count/get-number-of-unread-messages#1-get-number-of-unread-messages](https://sendbird.com/docs/chat/platform-api/v3/user/managing-unread-count/get-number-of-unread-messages#1-get-number-of-unread-messages)  `user_id`   Type: string   Description: Specifies the unique ID of a user.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_number_of_unread_messages_response import ViewNumberOfUnreadMessagesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    custom_types = "custom_types_example" # str | Specifies a comma-separated string of one or more custom types to filter group channels. URL encoding each type is recommended. If not specified, all channels are returned, regardless of their custom type. (optional)
    super_mode = "super_mode_example" # str | Restricts the search scope to either Supergroup channels or non-Supergroup channels or both. Acceptable values are `all`, `super`, and `nonsuper`. (Default: `all`) (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View number of unread messages
        api_response = api_instance.view_number_of_unread_messages(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_unread_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of unread messages
        api_response = api_instance.view_number_of_unread_messages(user_id, custom_types=custom_types, super_mode=super_mode, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_unread_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **custom_types** | **str**| Specifies a comma-separated string of one or more custom types to filter group channels. URL encoding each type is recommended. If not specified, all channels are returned, regardless of their custom type. | [optional]
 **super_mode** | **str**| Restricts the search scope to either Supergroup channels or non-Supergroup channels or both. Acceptable values are &#x60;all&#x60;, &#x60;super&#x60;, and &#x60;nonsuper&#x60;. (Default: &#x60;all&#x60;) | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**ViewNumberOfUnreadMessagesResponse**](ViewNumberOfUnreadMessagesResponse.md)

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

# **view_push_preferences**
> ViewPushPreferencesResponse view_push_preferences(user_id)

View push preferences

## View push preferences  You can retrieves a user's notifications preferences. A push notification is a message that is immediately delivered to a user's device when the device is either idle or running the client app in the background.  > **Note**: Push notifications are only available for group channels.      [https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/get-push-notification-preferences#1-get-push-notification-preferences](https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/get-push-notification-preferences#1-get-push-notification-preferences)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_push_preferences_response import ViewPushPreferencesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View push preferences
        api_response = api_instance.view_push_preferences(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_push_preferences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View push preferences
        api_response = api_instance.view_push_preferences(user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_push_preferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewPushPreferencesResponse**](ViewPushPreferencesResponse.md)

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

# **view_push_preferences_for_a_channel**
> ViewPushPreferencesForAChannelResponse view_push_preferences_for_a_channel(user_id, channel_url)

View push preferences for a channel

## View push preferences for a channel  You can retrieve a user's notifications preferences for a specific channel. A push notification is a message that is immediately delivered to a user's device when the device is either idle or running the client app in the background. These notifications preferences can be configured.  > **Note**: Push notifications are only available for group channels.      [https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/get-push-notification-preferences-for-a-channel#1-get-push-notification-preferences-for-a-channel](https://sendbird.com/docs/chat/platform-api/v3/user/configuring-notification-preferences/get-push-notification-preferences-for-a-channel#1-get-push-notification-preferences-for-a-channel)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_push_preferences_for_a_channel_response import ViewPushPreferencesForAChannelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View push preferences for a channel
        api_response = api_instance.view_push_preferences_for_a_channel(user_id, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_push_preferences_for_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View push preferences for a channel
        api_response = api_instance.view_push_preferences_for_a_channel(user_id, channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_push_preferences_for_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewPushPreferencesForAChannelResponse**](ViewPushPreferencesForAChannelResponse.md)

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

# **view_who_owns_a_registration_or_device_token**
> ViewWhoOwnsARegistrationOrDeviceTokenResponse view_who_owns_a_registration_or_device_token(token_type, token)

View who owns a registration or device token

## View who owns a registration or device token  Retrieves a user who owns a FCM registration token, HMS device token, or APNs device token. You can pass one of two values in `token_type`: `gcm`, `huawei`, or `apns`, depending on which push service you are using.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-who-owns-a-registration-or-device-token ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_who_owns_a_registration_or_device_token_response import ViewWhoOwnsARegistrationOrDeviceTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    token_type = "token_type_example" # str | (Required) 
    token = "token_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View who owns a registration or device token
        api_response = api_instance.view_who_owns_a_registration_or_device_token(token_type, token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_who_owns_a_registration_or_device_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View who owns a registration or device token
        api_response = api_instance.view_who_owns_a_registration_or_device_token(token_type, token, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_who_owns_a_registration_or_device_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type** | **str**| (Required)  |
 **token** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewWhoOwnsARegistrationOrDeviceTokenResponse**](ViewWhoOwnsARegistrationOrDeviceTokenResponse.md)

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

