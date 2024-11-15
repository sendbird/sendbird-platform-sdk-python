# sendbird_platform_sdk.UserApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_registration_or_device_token**](UserApi.md#add_registration_or_device_token) | **POST** /v3/users/{user_id}/push/{token_type} | Add a registration or device token
[**choose_push_notification_content_template**](UserApi.md#choose_push_notification_content_template) | **PUT** /v3/users/{user_id}/push/template | Choose a push notification content template
[**create_user**](UserApi.md#create_user) | **POST** /v3/users | Create a user
[**create_user_token**](UserApi.md#create_user_token) | **POST** /v3/users/{user_id}/token | Create user token
[**delete_user_by_id**](UserApi.md#delete_user_by_id) | **DELETE** /v3/users/{user_id} | Delete a user
[**leave_my_group_channels**](UserApi.md#leave_my_group_channels) | **PUT** /v3/users/{user_id}/my_group_channels/leave | Leave my group channels
[**list_my_group_channels**](UserApi.md#list_my_group_channels) | **GET** /v3/users/{user_id}/my_group_channels | List my group channels
[**list_registration_or_device_tokens**](UserApi.md#list_registration_or_device_tokens) | **GET** /v3/users/{user_id}/push/{token_type} | List registration or device tokens
[**list_users**](UserApi.md#list_users) | **GET** /v3/users | List users
[**mark_all_messages_as_read**](UserApi.md#mark_all_messages_as_read) | **PUT** /v3/users/{user_id}/mark_as_read_all | Mark all messages as read
[**register_as_operator_to_channels_with_custom_channel_types**](UserApi.md#register_as_operator_to_channels_with_custom_channel_types) | **POST** /v3/users/{user_id}/operating_channel_custom_types | Register as an operator to channels with custom channel types
[**remove_registration_or_device_token**](UserApi.md#remove_registration_or_device_token) | **DELETE** /v3/users/{user_id}/push | Remove a registration or device token - When unregistering all device tokens
[**remove_registration_or_device_token_by_token**](UserApi.md#remove_registration_or_device_token_by_token) | **DELETE** /v3/users/{user_id}/push/{token_type}/{token} | Remove a registration or device token - When unregistering a specific token
[**remove_registration_or_device_token_from_owner_by_token**](UserApi.md#remove_registration_or_device_token_from_owner_by_token) | **DELETE** /v3/push/device_tokens/{token_type}/{token} | Remove a registration or device token from an owner
[**reset_push_preferences**](UserApi.md#reset_push_preferences) | **DELETE** /v3/users/{user_id}/push_preference | Reset push preferences
[**update_channel_invitation_preference**](UserApi.md#update_channel_invitation_preference) | **PUT** /v3/users/{user_id}/channel_invitation_preference | Update channel invitation preference
[**update_count_preference_of_channel_by_url**](UserApi.md#update_count_preference_of_channel_by_url) | **PUT** /v3/users/{user_id}/count_preference/{channel_url} | Update count preference of a channel
[**update_push_preferences**](UserApi.md#update_push_preferences) | **PUT** /v3/users/{user_id}/push_preference | Update push preferences
[**update_push_preferences_for_channel_by_url**](UserApi.md#update_push_preferences_for_channel_by_url) | **PUT** /v3/users/{user_id}/push_preference/{channel_url} | Update push preferences for a channel
[**update_user_by_id**](UserApi.md#update_user_by_id) | **PUT** /v3/users/{user_id} | Update a user
[**view_channel_invitation_preference**](UserApi.md#view_channel_invitation_preference) | **GET** /v3/users/{user_id}/channel_invitation_preference | View channel invitation preference
[**view_count_preference_of_channel_by_url**](UserApi.md#view_count_preference_of_channel_by_url) | **GET** /v3/users/{user_id}/count_preference/{channel_url} | View count preference of a channel
[**view_number_of_channels_by_join_status**](UserApi.md#view_number_of_channels_by_join_status) | **GET** /v3/users/{user_id}/group_channel_count | View number of channels by join status
[**view_number_of_channels_with_unread_messages**](UserApi.md#view_number_of_channels_with_unread_messages) | **GET** /v3/users/{user_id}/unread_channel_count | View number of channels with unread messages
[**view_number_of_unread_items**](UserApi.md#view_number_of_unread_items) | **GET** /v3/users/{user_id}/unread_item_count | View number of unread items
[**view_number_of_unread_messages**](UserApi.md#view_number_of_unread_messages) | **GET** /v3/users/{user_id}/unread_message_count | View number of unread messages
[**view_push_preferences**](UserApi.md#view_push_preferences) | **GET** /v3/users/{user_id}/push_preference | View push preferences
[**view_push_preferences_for_channel_by_url**](UserApi.md#view_push_preferences_for_channel_by_url) | **GET** /v3/users/{user_id}/push_preference/{channel_url} | View push preferences for a channel
[**view_user_by_id**](UserApi.md#view_user_by_id) | **GET** /v3/users/{user_id} | View a user
[**view_who_owns_registration_or_device_token_by_token**](UserApi.md#view_who_owns_registration_or_device_token_by_token) | **GET** /v3/push/device_tokens/{token_type}/{token} | View who owns a registration or device token


# **add_registration_or_device_token**
> AddRegistrationOrDeviceTokenResponse add_registration_or_device_token(user_id, token_type)

Add a registration or device token

## Add a registration or device token  > __Note__: A user can have up to 20 FCM registration tokens, 20 HMS device tokens, and 20 APNs device tokens each. The oldest token will be deleted before a new token is added for a user who already has 20 registration or device tokens. Only the 20 newest tokens will be maintained for users who already have more than 20 of each token type.  To send notification requests to push notification services on behalf of your server, adds a specific user's FCM registration token, HMS device token, or APNs device token to Sendbird server. Depending on which push service you are using, you can pass one of two values in `token_type`: `gcm`, `huawei`, or `apns`.  A FCM registration token and an APNs device token allow identification of each client app instance on each device, and are generated and registered by Android and iOS apps through the corresponding SDKs. Use this method if you need to register a token via your own server.  > __Note__: For more information on the registration token and device token, visit the Google's [FCM](https://firebase.google.com/docs/auth/admin/verify-id-tokens) page, Huawei's [Push kit](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/service-introduction-0000001050040060) and Apple's [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html) page.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-add-a-registration-or-device-token ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.add_registration_or_device_token_data import AddRegistrationOrDeviceTokenData
from sendbird_platform_sdk.model.add_registration_or_device_token_response import AddRegistrationOrDeviceTokenResponse
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
    user_id = "user_id_example" # str | 
    token_type = "token_type_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_registration_or_device_token_data = AddRegistrationOrDeviceTokenData(
        gcm_reg_token="gcm_reg_token_example",
        huawei_device_token="huawei_device_token_example",
        apns_device_token="apns_device_token_example",
    ) # AddRegistrationOrDeviceTokenData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a registration or device token
        api_response = api_instance.add_registration_or_device_token(user_id, token_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->add_registration_or_device_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a registration or device token
        api_response = api_instance.add_registration_or_device_token(user_id, token_type, api_token=api_token, add_registration_or_device_token_data=add_registration_or_device_token_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->add_registration_or_device_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **token_type** | **str**|  |
 **api_token** | **str**|  | [optional]
 **add_registration_or_device_token_data** | [**AddRegistrationOrDeviceTokenData**](AddRegistrationOrDeviceTokenData.md)|  | [optional]

### Return type

[**AddRegistrationOrDeviceTokenResponse**](AddRegistrationOrDeviceTokenResponse.md)

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

# **choose_push_notification_content_template**
> ChoosePushNotificationContentTemplateResponse choose_push_notification_content_template(user_id)

Choose a push notification content template

## Choose a push notification content template  Chooses a push notification content template of a user's own. The push notifications feature is only available for group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-choose-a-push-notification-content-template ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.choose_push_notification_content_template_response import ChoosePushNotificationContentTemplateResponse
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Choose a push notification content template
        api_response = api_instance.choose_push_notification_content_template(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->choose_push_notification_content_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Choose a push notification content template
        api_response = api_instance.choose_push_notification_content_template(user_id, api_token=api_token, body=body)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->choose_push_notification_content_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**ChoosePushNotificationContentTemplateResponse**](ChoosePushNotificationContentTemplateResponse.md)

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

# **create_user**
> SendBirdUser create_user()

Create a user

## Create a user  Creates a new user in the application. A user is identified by its unique user ID, and additionally have a changeable nickname, profile image, and so on.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-create-a-user

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.send_bird_user import SendBirdUser
from sendbird_platform_sdk.model.create_user_data import CreateUserData
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
    create_user_data = CreateUserData(
        user_id="user_id_example",
        nickname="nickname_example",
        profile_url="profile_url_example",
        profile_file=open('/path/to/file', 'rb'),
        issue_access_token=True,
        discovery_keys=[
            "discovery_keys_example",
        ],
        metadata={},
    ) # CreateUserData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a user
        api_response = api_instance.create_user(api_token=api_token, create_user_data=create_user_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **create_user_data** | [**CreateUserData**](CreateUserData.md)|  | [optional]

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

# **create_user_token**
> CreateUserTokenResponse create_user_token(user_id)

Create user token

## Create user token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.create_user_token_data import CreateUserTokenData
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_user_token_data = CreateUserTokenData(
        expires_at=1,
    ) # CreateUserTokenData |  (optional)

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
        api_response = api_instance.create_user_token(user_id, api_token=api_token, create_user_token_data=create_user_token_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->create_user_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **create_user_token_data** | [**CreateUserTokenData**](CreateUserTokenData.md)|  | [optional]

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

# **delete_user_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_user_by_id(user_id)

Delete a user

## Delete a user  Deletes a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-delete-a-user ----------------------------

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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a user
        api_response = api_instance.delete_user_by_id(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->delete_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a user
        api_response = api_instance.delete_user_by_id(user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->delete_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
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

# **leave_my_group_channels**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} leave_my_group_channels(user_id)

Leave my group channels

## Leave my group channels  Makes a user leave all joined group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-leave-my-group-channels ----------------------------   `user_id`      Type: string      Description: Specifies the unique ID of the user to leave all joined group channels.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.leave_my_group_channels_data import LeaveMyGroupChannelsData
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    leave_my_group_channels_data = LeaveMyGroupChannelsData(
        custom_type="custom_type_example",
    ) # LeaveMyGroupChannelsData |  (optional)

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
        api_response = api_instance.leave_my_group_channels(user_id, api_token=api_token, leave_my_group_channels_data=leave_my_group_channels_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->leave_my_group_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **leave_my_group_channels_data** | [**LeaveMyGroupChannelsData**](LeaveMyGroupChannelsData.md)|  | [optional]

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
> ListMyGroupChannelsResponse list_my_group_channels(user_id)

List my group channels

## List my group channels  Retrieves all group channels that the user has joined. You can create a request based on various query parameters.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-list-my-group-channels ----------------------------   `user_id`      Type: string      Description: Specifies the unique ID of the target user.

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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    distinct_mode = "distinct_mode_example" # str |  (optional)
    public_mode = "public_mode_example" # str |  (optional)
    super_mode = "super_mode_example" # str |  (optional)
    hidden_mode = "hidden_mode_example" # str |  (optional)
    member_state_filter = "member_state_filter_example" # str |  (optional)
    unread_filter = "unread_filter_example" # str |  (optional)
    created_after = 1 # int |  (optional)
    created_before = 1 # int |  (optional)
    show_empty = True # bool |  (optional)
    show_frozen = True # bool |  (optional)
    show_member = True # bool |  (optional)
    show_delivery_receipt = True # bool |  (optional)
    show_read_receipt = True # bool |  (optional)
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
    search_query = "search_query_example" # str |  (optional)
    search_fields = "search_fields_example" # str |  (optional)
    metadata_key = "metadata_key_example" # str |  (optional)
    metadata_values = "metadata_values_example" # str |  (optional)
    metadata_value_startswith = "metadata_value_startswith_example" # str |  (optional)
    metacounter_key = "metacounter_key_example" # str |  (optional)
    metacounter_values = "metacounter_values_example" # str |  (optional)
    metacounter_value_gt = "metacounter_value_gt_example" # str |  (optional)
    metacounter_value_gte = "metacounter_value_gte_example" # str |  (optional)
    metacounter_value_lt = "metacounter_value_lt_example" # str |  (optional)
    metacounter_value_lte = "metacounter_value_lte_example" # str |  (optional)
    custom_type = "custom_type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List my group channels
        api_response = api_instance.list_my_group_channels(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_my_group_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List my group channels
        api_response = api_instance.list_my_group_channels(user_id, api_token=api_token, token=token, limit=limit, distinct_mode=distinct_mode, public_mode=public_mode, super_mode=super_mode, hidden_mode=hidden_mode, member_state_filter=member_state_filter, unread_filter=unread_filter, created_after=created_after, created_before=created_before, show_empty=show_empty, show_frozen=show_frozen, show_member=show_member, show_delivery_receipt=show_delivery_receipt, show_read_receipt=show_read_receipt, order=order, metadata_order_key=metadata_order_key, custom_types=custom_types, custom_type_startswith=custom_type_startswith, channel_urls=channel_urls, name=name, name_contains=name_contains, name_startswith=name_startswith, members_exactly_in=members_exactly_in, members_include_in=members_include_in, query_type=query_type, members_nickname=members_nickname, members_nickname_contains=members_nickname_contains, search_query=search_query, search_fields=search_fields, metadata_key=metadata_key, metadata_values=metadata_values, metadata_value_startswith=metadata_value_startswith, metacounter_key=metacounter_key, metacounter_values=metacounter_values, metacounter_value_gt=metacounter_value_gt, metacounter_value_gte=metacounter_value_gte, metacounter_value_lt=metacounter_value_lt, metacounter_value_lte=metacounter_value_lte, custom_type=custom_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_my_group_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **distinct_mode** | **str**|  | [optional]
 **public_mode** | **str**|  | [optional]
 **super_mode** | **str**|  | [optional]
 **hidden_mode** | **str**|  | [optional]
 **member_state_filter** | **str**|  | [optional]
 **unread_filter** | **str**|  | [optional]
 **created_after** | **int**|  | [optional]
 **created_before** | **int**|  | [optional]
 **show_empty** | **bool**|  | [optional]
 **show_frozen** | **bool**|  | [optional]
 **show_member** | **bool**|  | [optional]
 **show_delivery_receipt** | **bool**|  | [optional]
 **show_read_receipt** | **bool**|  | [optional]
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
 **search_query** | **str**|  | [optional]
 **search_fields** | **str**|  | [optional]
 **metadata_key** | **str**|  | [optional]
 **metadata_values** | **str**|  | [optional]
 **metadata_value_startswith** | **str**|  | [optional]
 **metacounter_key** | **str**|  | [optional]
 **metacounter_values** | **str**|  | [optional]
 **metacounter_value_gt** | **str**|  | [optional]
 **metacounter_value_gte** | **str**|  | [optional]
 **metacounter_value_lt** | **str**|  | [optional]
 **metacounter_value_lte** | **str**|  | [optional]
 **custom_type** | **str**|  | [optional]

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

## List registration or device tokens  Retrieves a list of a specific user's FCM registration tokens, HMS device tokens, or APNs device tokens. You can specify either `gcm`, `huawei`, or `apns` in the `token_type` parameter, depending on which push notification service you are using.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-list-registration-or-device-tokens ----------------------------

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
    user_id = "user_id_example" # str | 
    token_type = "token_type_example" # str | 
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
 **user_id** | **str**|  |
 **token_type** | **str**|  |
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

## List users  Retrieves a list of users in your application. You can query the list using various parameters.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-list-users ----------------------------

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
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    active_mode = "active_mode_example" # str |  (optional)
    show_bot = True # bool |  (optional)
    user_ids = "user_ids_example" # str |  (optional)
    nickname = "nickname_example" # str |  (optional)
    nickname_startswith = "nickname_startswith_example" # str |  (optional)
    metadatakey = "metadatakey_example" # str |  (optional)
    metadatavalues_in = "metadatavalues_in_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List users
        api_response = api_instance.list_users(api_token=api_token, token=token, limit=limit, active_mode=active_mode, show_bot=show_bot, user_ids=user_ids, nickname=nickname, nickname_startswith=nickname_startswith, metadatakey=metadatakey, metadatavalues_in=metadatavalues_in)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **active_mode** | **str**|  | [optional]
 **show_bot** | **bool**|  | [optional]
 **user_ids** | **str**|  | [optional]
 **nickname** | **str**|  | [optional]
 **nickname_startswith** | **str**|  | [optional]
 **metadatakey** | **str**|  | [optional]
 **metadatavalues_in** | **str**|  | [optional]

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

## Mark all messages as read  Marks all of a user's unread messages as read in the joined group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-mark-all-messages-as-read ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.mark_all_messages_as_read_data import MarkAllMessagesAsReadData
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    mark_all_messages_as_read_data = MarkAllMessagesAsReadData(
        channel_urls=[
            "channel_urls_example",
        ],
    ) # MarkAllMessagesAsReadData |  (optional)

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
        api_response = api_instance.mark_all_messages_as_read(user_id, api_token=api_token, mark_all_messages_as_read_data=mark_all_messages_as_read_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->mark_all_messages_as_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **mark_all_messages_as_read_data** | [**MarkAllMessagesAsReadData**](MarkAllMessagesAsReadData.md)|  | [optional]

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

# **register_as_operator_to_channels_with_custom_channel_types**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} register_as_operator_to_channels_with_custom_channel_types(user_id)

Register as an operator to channels with custom channel types

## Register as an operator to channels with custom channel types  Registers a user as an operator to channels with particular custom channel types.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-register-as-an-operator-to-channels-with-custom-channel-types ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.register_as_operator_to_channels_with_custom_channel_types_data import RegisterAsOperatorToChannelsWithCustomChannelTypesData
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    register_as_operator_to_channels_with_custom_channel_types_data = RegisterAsOperatorToChannelsWithCustomChannelTypesData(
        channel_custom_types=[
            "channel_custom_types_example",
        ],
    ) # RegisterAsOperatorToChannelsWithCustomChannelTypesData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register as an operator to channels with custom channel types
        api_response = api_instance.register_as_operator_to_channels_with_custom_channel_types(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->register_as_operator_to_channels_with_custom_channel_types: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register as an operator to channels with custom channel types
        api_response = api_instance.register_as_operator_to_channels_with_custom_channel_types(user_id, api_token=api_token, register_as_operator_to_channels_with_custom_channel_types_data=register_as_operator_to_channels_with_custom_channel_types_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->register_as_operator_to_channels_with_custom_channel_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **register_as_operator_to_channels_with_custom_channel_types_data** | [**RegisterAsOperatorToChannelsWithCustomChannelTypesData**](RegisterAsOperatorToChannelsWithCustomChannelTypesData.md)|  | [optional]

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

# **remove_registration_or_device_token**
> RemoveRegistrationOrDeviceTokenResponse remove_registration_or_device_token(user_id)

Remove a registration or device token - When unregistering all device tokens

## Remove a registration or device token  Removes a specific user's one or more FCM registration tokens, HMS device tokens, or APNs device tokens.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-remove-a-registration-or-device-token ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.remove_registration_or_device_token_response import RemoveRegistrationOrDeviceTokenResponse
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a registration or device token - When unregistering all device tokens
        api_response = api_instance.remove_registration_or_device_token(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_registration_or_device_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a registration or device token - When unregistering all device tokens
        api_response = api_instance.remove_registration_or_device_token(user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_registration_or_device_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**RemoveRegistrationOrDeviceTokenResponse**](RemoveRegistrationOrDeviceTokenResponse.md)

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

# **remove_registration_or_device_token_by_token**
> RemoveRegistrationOrDeviceTokenByTokenResponse remove_registration_or_device_token_by_token(user_id, token_type, token)

Remove a registration or device token - When unregistering a specific token

## Remove a registration or device token  Removes a specific user's one or more FCM registration tokens, HMS device tokens, or APNs device tokens.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-remove-a-registration-or-device-token ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.remove_registration_or_device_token_by_token_response import RemoveRegistrationOrDeviceTokenByTokenResponse
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
    user_id = "user_id_example" # str | 
    token_type = "token_type_example" # str | 
    token = "token_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a registration or device token - When unregistering a specific token
        api_response = api_instance.remove_registration_or_device_token_by_token(user_id, token_type, token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_registration_or_device_token_by_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a registration or device token - When unregistering a specific token
        api_response = api_instance.remove_registration_or_device_token_by_token(user_id, token_type, token, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_registration_or_device_token_by_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **token_type** | **str**|  |
 **token** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**RemoveRegistrationOrDeviceTokenByTokenResponse**](RemoveRegistrationOrDeviceTokenByTokenResponse.md)

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

# **remove_registration_or_device_token_from_owner_by_token**
> RemoveRegistrationOrDeviceTokenFromOwnerByTokenResponse remove_registration_or_device_token_from_owner_by_token(token_type, token)

Remove a registration or device token from an owner

## Remove a registration or device token from an owner  Removes a registration or device token from a user who owns it. You can pass one of two values in `token_type`: `gcm`, `huawei`, or `apns`, depending on which push service you are using.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-remove-a-registration-or-device-token-from-an-owner ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.remove_registration_or_device_token_from_owner_by_token_response import RemoveRegistrationOrDeviceTokenFromOwnerByTokenResponse
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
    token_type = "token_type_example" # str | 
    token = "token_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a registration or device token from an owner
        api_response = api_instance.remove_registration_or_device_token_from_owner_by_token(token_type, token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_registration_or_device_token_from_owner_by_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a registration or device token from an owner
        api_response = api_instance.remove_registration_or_device_token_from_owner_by_token(token_type, token, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->remove_registration_or_device_token_from_owner_by_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type** | **str**|  |
 **token** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**RemoveRegistrationOrDeviceTokenFromOwnerByTokenResponse**](RemoveRegistrationOrDeviceTokenFromOwnerByTokenResponse.md)

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
> ResetPushPreferencesResponse reset_push_preferences(user_id)

Reset push preferences

## Reset push preferences  Resets a user's push preferences. After performing this action,   `do_not_disturb` and `snooze_enabled` are set to false.  The values of the parameters associated with the time frame are all set to 0.  `timezone` is reset to `UTC`.  `push_sound` is reset to `default`.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-reset-push-preferences ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.reset_push_preferences_response import ResetPushPreferencesResponse
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
    user_id = "user_id_example" # str | 
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
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ResetPushPreferencesResponse**](ResetPushPreferencesResponse.md)

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

# **update_channel_invitation_preference**
> UpdateChannelInvitationPreferenceResponse update_channel_invitation_preference(user_id)

Update channel invitation preference

## Update channel invitation preference  Updates the channel invitation preference for a user's [private](https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#-3-private-vs-public) group channels.  > __Note__: Using the [update default channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference) action, you can update the value of channel invitation preference which is globally applied to all users within the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_channel_invitation_preference_response import UpdateChannelInvitationPreferenceResponse
from sendbird_platform_sdk.model.update_channel_invitation_preference_data import UpdateChannelInvitationPreferenceData
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_channel_invitation_preference_data = UpdateChannelInvitationPreferenceData(
        auto_accept=True,
    ) # UpdateChannelInvitationPreferenceData |  (optional)

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
        api_response = api_instance.update_channel_invitation_preference(user_id, api_token=api_token, update_channel_invitation_preference_data=update_channel_invitation_preference_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_channel_invitation_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_channel_invitation_preference_data** | [**UpdateChannelInvitationPreferenceData**](UpdateChannelInvitationPreferenceData.md)|  | [optional]

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

# **update_count_preference_of_channel_by_url**
> UpdateCountPreferenceOfChannelByUrlResponse update_count_preference_of_channel_by_url(user_id, channel_url)

Update count preference of a channel

## Update count preference of a channel  Updates count preference of a specific group channel of a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-count-preference-of-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_count_preference_of_channel_by_url_response import UpdateCountPreferenceOfChannelByUrlResponse
from sendbird_platform_sdk.model.update_count_preference_of_channel_by_url_data import UpdateCountPreferenceOfChannelByUrlData
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
    user_id = "user_id_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_count_preference_of_channel_by_url_data = UpdateCountPreferenceOfChannelByUrlData(
        count_preference="count_preference_example",
    ) # UpdateCountPreferenceOfChannelByUrlData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update count preference of a channel
        api_response = api_instance.update_count_preference_of_channel_by_url(user_id, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_count_preference_of_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update count preference of a channel
        api_response = api_instance.update_count_preference_of_channel_by_url(user_id, channel_url, api_token=api_token, update_count_preference_of_channel_by_url_data=update_count_preference_of_channel_by_url_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_count_preference_of_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_count_preference_of_channel_by_url_data** | [**UpdateCountPreferenceOfChannelByUrlData**](UpdateCountPreferenceOfChannelByUrlData.md)|  | [optional]

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

## Update push preferences  Updates a user's push preferences. Through this action, you can set `do_not_disturb` for a user, and update the time frame in which the setting applies.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-push-preferences ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_push_preferences_data import UpdatePushPreferencesData
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_push_preferences_data = UpdatePushPreferencesData(
        push_trigger_option="push_trigger_option_example",
        do_not_disturb=True,
        start_hour=1,
        start_min=1,
        end_hour=1,
        end_min=1,
        snooze_enabled=True,
        snooze_start_ts=1,
        snooze_end_ts=1,
        block_push_from_bots=True,
        push_blocked_bot_ids=[
            "push_blocked_bot_ids_example",
        ],
        timezone="timezone_example",
        push_sound="push_sound_example",
    ) # UpdatePushPreferencesData |  (optional)

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
        api_response = api_instance.update_push_preferences(user_id, api_token=api_token, update_push_preferences_data=update_push_preferences_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_push_preferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_push_preferences_data** | [**UpdatePushPreferencesData**](UpdatePushPreferencesData.md)|  | [optional]

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

# **update_push_preferences_for_channel_by_url**
> UpdatePushPreferencesForChannelByUrlResponse update_push_preferences_for_channel_by_url(user_id, channel_url)

Update push preferences for a channel

## Update push preferences for a channel  Updates push preferences for a user's specific group channel. The push notifications feature is only available for group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-push-preferences-for-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.update_push_preferences_for_channel_by_url_response import UpdatePushPreferencesForChannelByUrlResponse
from sendbird_platform_sdk.model.update_push_preferences_for_channel_by_url_data import UpdatePushPreferencesForChannelByUrlData
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
    user_id = "user_id_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_push_preferences_for_channel_by_url_data = UpdatePushPreferencesForChannelByUrlData(
        push_trigger_option="push_trigger_option_example",
        enable=True,
        push_sound="push_sound_example",
    ) # UpdatePushPreferencesForChannelByUrlData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update push preferences for a channel
        api_response = api_instance.update_push_preferences_for_channel_by_url(user_id, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_push_preferences_for_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update push preferences for a channel
        api_response = api_instance.update_push_preferences_for_channel_by_url(user_id, channel_url, api_token=api_token, update_push_preferences_for_channel_by_url_data=update_push_preferences_for_channel_by_url_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_push_preferences_for_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_push_preferences_for_channel_by_url_data** | [**UpdatePushPreferencesForChannelByUrlData**](UpdatePushPreferencesForChannelByUrlData.md)|  | [optional]

### Return type

[**UpdatePushPreferencesForChannelByUrlResponse**](UpdatePushPreferencesForChannelByUrlResponse.md)

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

# **update_user_by_id**
> SendBirdUser update_user_by_id(user_id)

Update a user

## Update a user  Updates information on a user. In addition to changing a user's nickname or profile image, you can issue a new access token for the user. The new access token replaces the previous one as the necessary token for authentication.  You can also deactivate or reactivate a user. If the `leave_all_when_deactivated` is true (which it is by default), a user leaves all joined group channels when deactivated.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.send_bird_user import SendBirdUser
from sendbird_platform_sdk.model.update_user_by_id_data import UpdateUserByIdData
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_user_by_id_data = UpdateUserByIdData(
        user_id="user_id_example",
        nickname="nickname_example",
        profile_url="profile_url_example",
        profile_file=open('/path/to/file', 'rb'),
        issue_access_token=True,
        issue_session_token=True,
        session_token_expires_at=1,
        is_active=True,
        last_seen_at=1,
        discovery_keys=[
            "discovery_keys_example",
        ],
        preferred_languages=[
            "preferred_languages_example",
        ],
        leave_all_when_deactivated=True,
    ) # UpdateUserByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a user
        api_response = api_instance.update_user_by_id(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a user
        api_response = api_instance.update_user_by_id(user_id, api_token=api_token, update_user_by_id_data=update_user_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->update_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_user_by_id_data** | [**UpdateUserByIdData**](UpdateUserByIdData.md)|  | [optional]

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

# **view_channel_invitation_preference**
> ViewChannelInvitationPreferenceResponse view_channel_invitation_preference(user_id)

View channel invitation preference

## View channel invitation preference  Retrieves channel invitation preference for a user's [private](https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#-3-private-vs-public) group channels.  > __Note__: Using the [view default channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-default-channel-invitation-preference) action, you can retrieve the value of channel invitation preference which is globally applied to all users within the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-channel-invitation-preference

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_channel_invitation_preference_response import ViewChannelInvitationPreferenceResponse
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View channel invitation preference
        api_response = api_instance.view_channel_invitation_preference(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_channel_invitation_preference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View channel invitation preference
        api_response = api_instance.view_channel_invitation_preference(user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_channel_invitation_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewChannelInvitationPreferenceResponse**](ViewChannelInvitationPreferenceResponse.md)

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

# **view_count_preference_of_channel_by_url**
> ViewCountPreferenceOfChannelByUrlResponse view_count_preference_of_channel_by_url(user_id, channel_url)

View count preference of a channel

## View count preference of a channel  Retrieves count preference of a specific group channel of a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-count-preference-of-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_count_preference_of_channel_by_url_response import ViewCountPreferenceOfChannelByUrlResponse
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
    user_id = "user_id_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View count preference of a channel
        api_response = api_instance.view_count_preference_of_channel_by_url(user_id, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_count_preference_of_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View count preference of a channel
        api_response = api_instance.view_count_preference_of_channel_by_url(user_id, channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_count_preference_of_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewCountPreferenceOfChannelByUrlResponse**](ViewCountPreferenceOfChannelByUrlResponse.md)

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

# **view_number_of_channels_by_join_status**
> ViewNumberOfChannelsByJoinStatusResponse view_number_of_channels_by_join_status(user_id)

View number of channels by join status

## View number of channels by join status  Retrieves the number of a user's group channels by their join status.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-number-of-channels-by-join-status ----------------------------   `user_id`      Type: string      Description: Specifies the unique ID of the user to retrieve the number.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_number_of_channels_by_join_status_response import ViewNumberOfChannelsByJoinStatusResponse
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    state = "state_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View number of channels by join status
        api_response = api_instance.view_number_of_channels_by_join_status(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_channels_by_join_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of channels by join status
        api_response = api_instance.view_number_of_channels_by_join_status(user_id, api_token=api_token, state=state)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_channels_by_join_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **state** | **str**|  | [optional]

### Return type

[**ViewNumberOfChannelsByJoinStatusResponse**](ViewNumberOfChannelsByJoinStatusResponse.md)

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

## View number of channels with unread messages  Retrieves the total number of a user's group channels with unread messages.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-number-of-channels-with-unread-messages ----------------------------

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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    custom_types = [
        "custom_types_example",
    ] # [str] |  (optional)
    super_mode = "super_mode_example" # str |  (optional)

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
        api_response = api_instance.view_number_of_channels_with_unread_messages(user_id, api_token=api_token, custom_types=custom_types, super_mode=super_mode)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_channels_with_unread_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **custom_types** | **[str]**|  | [optional]
 **super_mode** | **str**|  | [optional]

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

# **view_number_of_unread_items**
> ViewNumberOfUnreadItemsResponse view_number_of_unread_items(user_id)

View number of unread items

## View number of unread items  Retrieves a set of total numbers of a user's unread messages, unread mentioned messages, or received invitations in either super or non-super group channels. This action is only available for the group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-number-of-unread-items ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_number_of_unread_items_response import ViewNumberOfUnreadItemsResponse
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    custom_type = "custom_type_example" # str |  (optional)
    item_keys = "item_keys_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View number of unread items
        api_response = api_instance.view_number_of_unread_items(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_unread_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of unread items
        api_response = api_instance.view_number_of_unread_items(user_id, api_token=api_token, custom_type=custom_type, item_keys=item_keys)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_unread_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **custom_type** | **str**|  | [optional]
 **item_keys** | **str**|  | [optional]

### Return type

[**ViewNumberOfUnreadItemsResponse**](ViewNumberOfUnreadItemsResponse.md)

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

## View number of unread messages  Retrieves the total number of a user's currently unread messages in the group channels. The unread counts feature is only available for the group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-number-of-unread-messages ----------------------------   `user_id`      Type: string      Description: Specifies the unique ID of the user to retrieve the number.

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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    custom_types = "custom_types_example" # str |  (optional)
    super_mode = "super_mode_example" # str |  (optional)

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
        api_response = api_instance.view_number_of_unread_messages(user_id, api_token=api_token, custom_types=custom_types, super_mode=super_mode)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_number_of_unread_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **custom_types** | **str**|  | [optional]
 **super_mode** | **str**|  | [optional]

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

## View push preferences  Retrieves a user's push preferences about whether the user has set `do_not_disturb` to pause notifications for a certain period of time, and the time frame in which the user has applied the setting.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-push-preferences ----------------------------

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
    user_id = "user_id_example" # str | 
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
 **user_id** | **str**|  |
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

# **view_push_preferences_for_channel_by_url**
> ViewPushPreferencesForChannelByUrlResponse view_push_preferences_for_channel_by_url(user_id, channel_url)

View push preferences for a channel

## View push preferences for a channel  Retrieves whether a user has turned on notification messages for a specific channel. The push notifications feature is only available for group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-push-preferences-for-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_push_preferences_for_channel_by_url_response import ViewPushPreferencesForChannelByUrlResponse
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
    user_id = "user_id_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View push preferences for a channel
        api_response = api_instance.view_push_preferences_for_channel_by_url(user_id, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_push_preferences_for_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View push preferences for a channel
        api_response = api_instance.view_push_preferences_for_channel_by_url(user_id, channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_push_preferences_for_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewPushPreferencesForChannelByUrlResponse**](ViewPushPreferencesForChannelByUrlResponse.md)

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

# **view_user_by_id**
> SendBirdUser view_user_by_id(user_id)

View a user

## View a user  Retrieves information on a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-a-user ----------------------------   `user_id`      Type: string      Description: Specifies the unique ID of the user to retrieve.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.send_bird_user import SendBirdUser
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
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    include_unread_count = True # bool |  (optional)
    custom_types = "custom_types_example" # str |  (optional)
    super_mode = "super_mode_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a user
        api_response = api_instance.view_user_by_id(user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a user
        api_response = api_instance.view_user_by_id(user_id, api_token=api_token, include_unread_count=include_unread_count, custom_types=custom_types, super_mode=super_mode)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **include_unread_count** | **bool**|  | [optional]
 **custom_types** | **str**|  | [optional]
 **super_mode** | **str**|  | [optional]

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

# **view_who_owns_registration_or_device_token_by_token**
> ViewWhoOwnsRegistrationOrDeviceTokenByTokenResponse view_who_owns_registration_or_device_token_by_token(token_type, token)

View who owns a registration or device token

## View who owns a registration or device token  Retrieves a user who owns a FCM registration token, HMS device token, or APNs device token. You can pass one of two values in `token_type`: `gcm`, `huawei`, or `apns`, depending on which push service you are using.  https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-who-owns-a-registration-or-device-token ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.view_who_owns_registration_or_device_token_by_token_response import ViewWhoOwnsRegistrationOrDeviceTokenByTokenResponse
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
    token_type = "token_type_example" # str | 
    token = "token_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View who owns a registration or device token
        api_response = api_instance.view_who_owns_registration_or_device_token_by_token(token_type, token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_who_owns_registration_or_device_token_by_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View who owns a registration or device token
        api_response = api_instance.view_who_owns_registration_or_device_token_by_token(token_type, token, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->view_who_owns_registration_or_device_token_by_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type** | **str**|  |
 **token** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewWhoOwnsRegistrationOrDeviceTokenByTokenResponse**](ViewWhoOwnsRegistrationOrDeviceTokenByTokenResponse.md)

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

