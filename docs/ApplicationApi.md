# sendbird_platform_sdk.ApplicationApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_apns_push_configuration**](ApplicationApi.md#add_apns_push_configuration) | **POST** /v3/applications/push/apns | Add an APNs push configuration
[**add_fcm_push_configuration**](ApplicationApi.md#add_fcm_push_configuration) | **POST** /v3/applications/push/fcm | Add a FCM push configuration
[**add_hms_push_configuration**](ApplicationApi.md#add_hms_push_configuration) | **POST** /v3/applications/push/hms | Add an HMS push configuration
[**add_ip_to_whitelist**](ApplicationApi.md#add_ip_to_whitelist) | **PUT** /v3/applications/settings/ip_whitelist | Add an IP to a whitelist
[**ban_users_in_channels_with_custom_channel_type**](ApplicationApi.md#ban_users_in_channels_with_custom_channel_type) | **POST** /v3/applications/settings_by_channel_custom_type/{custom_type}/ban | Ban users in channels with a custom channel type
[**configure_auto_event_messages**](ApplicationApi.md#configure_auto_event_messages) | **PUT** /v3/applications/settings/auto_event_message | Configure auto event message settings
[**delete_allowed_ips_from_whitelist**](ApplicationApi.md#delete_allowed_ips_from_whitelist) | **DELETE** /v3/applications/settings/ip_whitelist | Delete allowed IPs from a whitelist
[**delete_apns_certificate_by_id**](ApplicationApi.md#delete_apns_certificate_by_id) | **DELETE** /v3/applications/push/apns/cert/{provider_id} | Delete an APNs certificate
[**generate_secondary_api_token**](ApplicationApi.md#generate_secondary_api_token) | **POST** /v3/applications/api_tokens | Generate a secondary API token
[**list_auto_event_messages**](ApplicationApi.md#list_auto_event_messages) | **GET** /v3/applications/settings/auto_event_message | List auto event messages
[**list_banned_users_in_channels_with_custom_channel_type**](ApplicationApi.md#list_banned_users_in_channels_with_custom_channel_type) | **GET** /v3/applications/settings_by_channel_custom_type/{custom_type}/ban | List banned users in channels with a custom channel type
[**list_muted_users_in_channels_with_custom_channel_type**](ApplicationApi.md#list_muted_users_in_channels_with_custom_channel_type) | **GET** /v3/applications/settings_by_channel_custom_type/{custom_type}/mute | List muted users in channels with a custom channel type
[**list_push_configurations**](ApplicationApi.md#list_push_configurations) | **GET** /v3/applications/push/{push_type} | List push configurations
[**list_push_notification_content_templates**](ApplicationApi.md#list_push_notification_content_templates) | **GET** /v3/applications/push/message_templates | List push notification content templates
[**list_secondary_api_tokens**](ApplicationApi.md#list_secondary_api_tokens) | **GET** /v3/applications/api_tokens | List secondary API tokens
[**mute_users_in_channels_with_custom_channel_type**](ApplicationApi.md#mute_users_in_channels_with_custom_channel_type) | **POST** /v3/applications/settings_by_channel_custom_type/{custom_type}/mute | Mute users in channels with a custom channel type
[**remove_push_configuration_by_id**](ApplicationApi.md#remove_push_configuration_by_id) | **DELETE** /v3/applications/push/{push_type}/{provider_id} | Remove a push configuration
[**retrieve_ip_whitelist**](ApplicationApi.md#retrieve_ip_whitelist) | **GET** /v3/applications/settings/ip_whitelist | Retrieve an IP whitelist
[**revoke_secondary_api_token_by_token**](ApplicationApi.md#revoke_secondary_api_token_by_token) | **DELETE** /v3/applications/api_tokens/{api_token} | Revoke a secondary API token
[**set_domain_filter**](ApplicationApi.md#set_domain_filter) | **PUT** /v3/applications/settings_global/{custom_type} | Message moderation
[**unban_users_in_channels_with_custom_channel_type**](ApplicationApi.md#unban_users_in_channels_with_custom_channel_type) | **DELETE** /v3/applications/settings_by_channel_custom_type/{custom_type}/ban | Unban users in channels with a custom channel type
[**unmute_users_in_channels_with_custom_channel_type**](ApplicationApi.md#unmute_users_in_channels_with_custom_channel_type) | **DELETE** /v3/applications/settings_by_channel_custom_type/{custom_type}/mute | Unmute users in channels with a custom channel type
[**update_apns_push_configuration_by_id**](ApplicationApi.md#update_apns_push_configuration_by_id) | **PUT** /v3/applications/push/apns/{provider_id} | Update an APNs push configuration
[**update_default_channel_invitation_preference**](ApplicationApi.md#update_default_channel_invitation_preference) | **PUT** /v3/applications/default_channel_invitation_preference | Update default channel invitation preference
[**update_fcm_push_configuration_by_id**](ApplicationApi.md#update_fcm_push_configuration_by_id) | **PUT** /v3/applications/push/fcm/{provider_id} | Update a FCM push configuration
[**update_hms_push_configuration_by_id**](ApplicationApi.md#update_hms_push_configuration_by_id) | **PUT** /v3/applications/push/hms/{provider_id} | Update an HMS push configuration
[**update_push_notification_content_template**](ApplicationApi.md#update_push_notification_content_template) | **PUT** /v3/applications/push/message_templates/{template_name} | Update a push notification content template
[**view_default_channel_invitation_preference**](ApplicationApi.md#view_default_channel_invitation_preference) | **GET** /v3/applications/default_channel_invitation_preference | View default channel invitation preference
[**view_push_configuration_by_id**](ApplicationApi.md#view_push_configuration_by_id) | **GET** /v3/applications/push/{push_type}/{provider_id} | View a push configuration
[**view_push_notification_content_template**](ApplicationApi.md#view_push_notification_content_template) | **GET** /v3/applications/push/message_templates/{template_name} | Get a push notification content template
[**view_secondary_api_token_by_token**](ApplicationApi.md#view_secondary_api_token_by_token) | **GET** /v3/applications/api_tokens/{api_token} | View a secondary API token


# **add_apns_push_configuration**
> AddApnsPushConfigurationResponse add_apns_push_configuration()

Add an APNs push configuration

## Add an APNs push configuration  Registers an APNs (Apple Push Notification service) push configuration for your client app. To send push notifications to iOS devices, your should first register the APNs push configuration. You can also register the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  > __Note__: To upload a [.p12](https://sendbird.com/docs/chat/v3/ios/guides/push-notifications#2-step-3-export-a-p12-file-and-upload-to-sendbird-dashboard) certificate file to Sendbird server, you should send a [Multipart request](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api#2-headers-3-multipart-requests).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-add-an-apns-push-configuration

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.add_apns_push_configuration_response import AddApnsPushConfigurationResponse
from sendbird_platform_sdk.model.add_apns_push_configuration_data import AddApnsPushConfigurationData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_apns_push_configuration_data = AddApnsPushConfigurationData(
        apns_cert=open('/path/to/file', 'rb'),
        apns_cert_env_type="apns_cert_env_type_example",
        apns_cert_password="apns_cert_password_example",
        has_unread_count_badge=True,
        content_available=True,
        mutable_content=True,
        push_sound="push_sound_example",
        apns_type="apns_type_example",
    ) # AddApnsPushConfigurationData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an APNs push configuration
        api_response = api_instance.add_apns_push_configuration(api_token=api_token, add_apns_push_configuration_data=add_apns_push_configuration_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->add_apns_push_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **add_apns_push_configuration_data** | [**AddApnsPushConfigurationData**](AddApnsPushConfigurationData.md)|  | [optional]

### Return type

[**AddApnsPushConfigurationResponse**](AddApnsPushConfigurationResponse.md)

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

# **add_fcm_push_configuration**
> AddFcmPushConfigurationResponse add_fcm_push_configuration()

Add a FCM push configuration

## Add a FCM push configuration  Registers a FCM (Firebase Cloud Messaging) push configuration for your client app. To send push notifications to Android devices, you should first register the FCM push configuration. You can also register the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-add-a-fcm-push-configuration

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.add_fcm_push_configuration_response import AddFcmPushConfigurationResponse
from sendbird_platform_sdk.model.add_fcm_push_configuration_data import AddFcmPushConfigurationData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_fcm_push_configuration_data = AddFcmPushConfigurationData(
        api_key="api_key_example",
        push_sound="push_sound_example",
    ) # AddFcmPushConfigurationData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a FCM push configuration
        api_response = api_instance.add_fcm_push_configuration(api_token=api_token, add_fcm_push_configuration_data=add_fcm_push_configuration_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->add_fcm_push_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **add_fcm_push_configuration_data** | [**AddFcmPushConfigurationData**](AddFcmPushConfigurationData.md)|  | [optional]

### Return type

[**AddFcmPushConfigurationResponse**](AddFcmPushConfigurationResponse.md)

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

# **add_hms_push_configuration**
> AddHmsPushConfigurationResponse add_hms_push_configuration()

Add an HMS push configuration

## Add an HMS push configuration  Registers an HMS (Huawei Mobile Services) push configuration for your client app. To send push notifications to Android devices for HMS, you should first register the HMS push configuration. You can also register the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-add-an-hms-push-configuration

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.add_hms_push_configuration_response import AddHmsPushConfigurationResponse
from sendbird_platform_sdk.model.add_hms_push_configuration_data import AddHmsPushConfigurationData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_hms_push_configuration_data = AddHmsPushConfigurationData(
        huawei_app_id="huawei_app_id_example",
        huawei_app_secret="huawei_app_secret_example",
        push_sound="push_sound_example",
    ) # AddHmsPushConfigurationData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an HMS push configuration
        api_response = api_instance.add_hms_push_configuration(api_token=api_token, add_hms_push_configuration_data=add_hms_push_configuration_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->add_hms_push_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **add_hms_push_configuration_data** | [**AddHmsPushConfigurationData**](AddHmsPushConfigurationData.md)|  | [optional]

### Return type

[**AddHmsPushConfigurationResponse**](AddHmsPushConfigurationResponse.md)

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

# **add_ip_to_whitelist**
> AddIpToWhitelistResponse add_ip_to_whitelist()

Add an IP to a whitelist

## Add an IP to a whitelist  Adds IP addresses and ranges to your Sendbird application settings. Both currently added and any previously added IPs are granted API access. You can configure the IP whitelist under Settings > Security > Allowed IPs in the [Sendbird Dashboard](https://dashboard.sendbird.com).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-add-an-ip-to-a-whitelist

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.add_ip_to_whitelist_response import AddIpToWhitelistResponse
from sendbird_platform_sdk.model.add_ip_to_whitelist_data import AddIpToWhitelistData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_ip_to_whitelist_data = AddIpToWhitelistData(
        ip_whitelist_addresses=[
            "ip_whitelist_addresses_example",
        ],
    ) # AddIpToWhitelistData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an IP to a whitelist
        api_response = api_instance.add_ip_to_whitelist(api_token=api_token, add_ip_to_whitelist_data=add_ip_to_whitelist_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->add_ip_to_whitelist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **add_ip_to_whitelist_data** | [**AddIpToWhitelistData**](AddIpToWhitelistData.md)|  | [optional]

### Return type

[**AddIpToWhitelistResponse**](AddIpToWhitelistResponse.md)

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

# **ban_users_in_channels_with_custom_channel_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} ban_users_in_channels_with_custom_channel_type(custom_type)

Ban users in channels with a custom channel type

## Ban specified users in channels with a custom channel type at once.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.ban_users_in_channels_with_custom_channel_type_data import BanUsersInChannelsWithCustomChannelTypeData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    custom_type = "custom_type_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    ban_users_in_channels_with_custom_channel_type_data = BanUsersInChannelsWithCustomChannelTypeData(
        banned_list=[
            BanUsersInChannelsWithCustomChannelTypeDataBannedListInner(
                user_id="user_id_example",
                seconds=3.14,
                description="description_example",
            ),
        ],
        on_demand_upsert=True,
    ) # BanUsersInChannelsWithCustomChannelTypeData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ban users in channels with a custom channel type
        api_response = api_instance.ban_users_in_channels_with_custom_channel_type(custom_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->ban_users_in_channels_with_custom_channel_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ban users in channels with a custom channel type
        api_response = api_instance.ban_users_in_channels_with_custom_channel_type(custom_type, api_token=api_token, ban_users_in_channels_with_custom_channel_type_data=ban_users_in_channels_with_custom_channel_type_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->ban_users_in_channels_with_custom_channel_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_type** | **str**|  |
 **api_token** | **str**|  | [optional]
 **ban_users_in_channels_with_custom_channel_type_data** | [**BanUsersInChannelsWithCustomChannelTypeData**](BanUsersInChannelsWithCustomChannelTypeData.md)|  | [optional]

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

# **configure_auto_event_messages**
> SendBirdAutoEventMessageSettings configure_auto_event_messages()

Configure auto event message settings

## Configure auto event message settings  Determines whether to automatically send event messages to group channels when events take place in an application. You can choose which auto event message to receive on the Sendbird Dashboard  https://sendbird.com/docs/chat/v3/platform-api/application/managing-auto-event-messages/configure-auto-event-message-settings ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.configure_auto_event_data import ConfigureAutoEventData
from sendbird_platform_sdk.model.send_bird_auto_event_message_settings import SendBirdAutoEventMessageSettings
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    configure_auto_event_data = ConfigureAutoEventData(
        auto_event_message=ConfigureAutoEventDataAutoEventMessage(
            user_leave={},
            user_join={},
            channel_create={},
            channel_change={},
        ),
    ) # ConfigureAutoEventData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Configure auto event message settings
        api_response = api_instance.configure_auto_event_messages(api_token=api_token, configure_auto_event_data=configure_auto_event_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->configure_auto_event_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **configure_auto_event_data** | [**ConfigureAutoEventData**](ConfigureAutoEventData.md)|  | [optional]

### Return type

[**SendBirdAutoEventMessageSettings**](SendBirdAutoEventMessageSettings.md)

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

# **delete_allowed_ips_from_whitelist**
> DeleteAllowedIpsFromWhitelistResponse delete_allowed_ips_from_whitelist(ip_whitelist_addresses)

Delete allowed IPs from a whitelist

## Delete allowed IPs from a whitelist  Deletes allowed IPs from the whitelist by specifying their IP addresses or ranges. You can configure the IP whitelist under Settings > Security > Allowed IPs in the [Sendbird Dashboard](https://dashboard.sendbird.com).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-delete-allowed-ips-from-a-whitelist

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.delete_allowed_ips_from_whitelist_response import DeleteAllowedIpsFromWhitelistResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    ip_whitelist_addresses = [
        "ip_whitelist_addresses_example",
    ] # [str] | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete allowed IPs from a whitelist
        api_response = api_instance.delete_allowed_ips_from_whitelist(ip_whitelist_addresses)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->delete_allowed_ips_from_whitelist: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete allowed IPs from a whitelist
        api_response = api_instance.delete_allowed_ips_from_whitelist(ip_whitelist_addresses, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->delete_allowed_ips_from_whitelist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_whitelist_addresses** | **[str]**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**DeleteAllowedIpsFromWhitelistResponse**](DeleteAllowedIpsFromWhitelistResponse.md)

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

# **delete_apns_certificate_by_id**
> DeleteApnsCertificateByIdResponse delete_apns_certificate_by_id(provider_id)

Delete an APNs certificate

## Delete an APNs certificate  Deletes a specific APNs certificate.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-delete-an-apns-certificate ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.delete_apns_certificate_by_id_response import DeleteApnsCertificateByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    provider_id = "provider_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete an APNs certificate
        api_response = api_instance.delete_apns_certificate_by_id(provider_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->delete_apns_certificate_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete an APNs certificate
        api_response = api_instance.delete_apns_certificate_by_id(provider_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->delete_apns_certificate_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**DeleteApnsCertificateByIdResponse**](DeleteApnsCertificateByIdResponse.md)

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

# **generate_secondary_api_token**
> GenerateSecondaryApiTokenResponse generate_secondary_api_token()

Generate a secondary API token

## Generate a secondary API token  Generates a new secondary API token.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-generate-a-secondary-api-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.generate_secondary_api_token_response import GenerateSecondaryApiTokenResponse
from sendbird_platform_sdk.model.generate_secondary_api_token_data import GenerateSecondaryApiTokenData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    generate_secondary_api_token_data = GenerateSecondaryApiTokenData(
        http_api_token="http_api_token_example",
    ) # GenerateSecondaryApiTokenData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate a secondary API token
        api_response = api_instance.generate_secondary_api_token(api_token=api_token, generate_secondary_api_token_data=generate_secondary_api_token_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->generate_secondary_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **generate_secondary_api_token_data** | [**GenerateSecondaryApiTokenData**](GenerateSecondaryApiTokenData.md)|  | [optional]

### Return type

[**GenerateSecondaryApiTokenResponse**](GenerateSecondaryApiTokenResponse.md)

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

# **list_auto_event_messages**
> SendBirdAutoEventMessageSettings list_auto_event_messages()

List auto event messages

## List auto event messages  Retrieves a list of auto event messages that are sent in a specified application and indicates which ones are in use. Auto event messages are Admin messages that are automatically generated when a specific event occurs.  https://sendbird.com/docs/chat/v3/platform-api/application/managing-auto-event-messages/list-auto-event-messages ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.send_bird_auto_event_message_settings import SendBirdAutoEventMessageSettings
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List auto event messages
        api_response = api_instance.list_auto_event_messages(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_auto_event_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**SendBirdAutoEventMessageSettings**](SendBirdAutoEventMessageSettings.md)

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

# **list_banned_users_in_channels_with_custom_channel_type**
> CustomTypeListBannedUsersResponse list_banned_users_in_channels_with_custom_channel_type(custom_type)

List banned users in channels with a custom channel type

## Retrieves a list of users banned from channels with the specified custom channel type.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.custom_type_list_banned_users_response import CustomTypeListBannedUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    custom_type = "custom_type_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List banned users in channels with a custom channel type
        api_response = api_instance.list_banned_users_in_channels_with_custom_channel_type(custom_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_banned_users_in_channels_with_custom_channel_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List banned users in channels with a custom channel type
        api_response = api_instance.list_banned_users_in_channels_with_custom_channel_type(custom_type, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_banned_users_in_channels_with_custom_channel_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_type** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**CustomTypeListBannedUsersResponse**](CustomTypeListBannedUsersResponse.md)

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

# **list_muted_users_in_channels_with_custom_channel_type**
> ListMutedUsersInChannelsWithCustomChannelType200Response list_muted_users_in_channels_with_custom_channel_type(custom_type)

List muted users in channels with a custom channel type

## Retrieves a list of the muted users in channels with a custom channel type.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.list_muted_users_in_channels_with_custom_channel_type200_response import ListMutedUsersInChannelsWithCustomChannelType200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    custom_type = "custom_type_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List muted users in channels with a custom channel type
        api_response = api_instance.list_muted_users_in_channels_with_custom_channel_type(custom_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_muted_users_in_channels_with_custom_channel_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List muted users in channels with a custom channel type
        api_response = api_instance.list_muted_users_in_channels_with_custom_channel_type(custom_type, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_muted_users_in_channels_with_custom_channel_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_type** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListMutedUsersInChannelsWithCustomChannelType200Response**](ListMutedUsersInChannelsWithCustomChannelType200Response.md)

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

# **list_push_configurations**
> ListPushConfigurationsResponse list_push_configurations(push_type)

List push configurations

## List push configurations  Retrieves a list of an application's registered push configurations.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-list-push-configurations ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.list_push_configurations_response import ListPushConfigurationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    push_type = "push_type_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List push configurations
        api_response = api_instance.list_push_configurations(push_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_push_configurations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List push configurations
        api_response = api_instance.list_push_configurations(push_type, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_push_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_type** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ListPushConfigurationsResponse**](ListPushConfigurationsResponse.md)

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

# **list_push_notification_content_templates**
> ListPushNotificationContentTemplatesResponse list_push_notification_content_templates()

List push notification content templates

## List push notification content templates  Retrieves a list of push notification content templates of an application.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-list-push-notification-content-templates

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.list_push_notification_content_templates_response import ListPushNotificationContentTemplatesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List push notification content templates
        api_response = api_instance.list_push_notification_content_templates(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_push_notification_content_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**ListPushNotificationContentTemplatesResponse**](ListPushNotificationContentTemplatesResponse.md)

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

# **list_secondary_api_tokens**
> ListSecondaryApiTokensResponse list_secondary_api_tokens()

List secondary API tokens

## List secondary API tokens  Retrieves a list of secondary API tokens.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-list-secondary-api-tokens

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.list_secondary_api_tokens_response import ListSecondaryApiTokensResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List secondary API tokens
        api_response = api_instance.list_secondary_api_tokens(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->list_secondary_api_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**ListSecondaryApiTokensResponse**](ListSecondaryApiTokensResponse.md)

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

# **mute_users_in_channels_with_custom_channel_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} mute_users_in_channels_with_custom_channel_type(custom_type)

Mute users in channels with a custom channel type

## Mutes specified users in channels with a custom channel type at once.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.mute_users_in_channels_with_custom_channel_type_data import MuteUsersInChannelsWithCustomChannelTypeData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    custom_type = "custom_type_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    mute_users_in_channels_with_custom_channel_type_data = MuteUsersInChannelsWithCustomChannelTypeData(
        user_ids=[
            "user_ids_example",
        ],
        seconds=3.14,
        description="description_example",
        on_demand_upsert=True,
    ) # MuteUsersInChannelsWithCustomChannelTypeData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mute users in channels with a custom channel type
        api_response = api_instance.mute_users_in_channels_with_custom_channel_type(custom_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->mute_users_in_channels_with_custom_channel_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mute users in channels with a custom channel type
        api_response = api_instance.mute_users_in_channels_with_custom_channel_type(custom_type, api_token=api_token, mute_users_in_channels_with_custom_channel_type_data=mute_users_in_channels_with_custom_channel_type_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->mute_users_in_channels_with_custom_channel_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_type** | **str**|  |
 **api_token** | **str**|  | [optional]
 **mute_users_in_channels_with_custom_channel_type_data** | [**MuteUsersInChannelsWithCustomChannelTypeData**](MuteUsersInChannelsWithCustomChannelTypeData.md)|  | [optional]

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

# **remove_push_configuration_by_id**
> RemovePushConfigurationByIdResponse remove_push_configuration_by_id(push_type, provider_id)

Remove a push configuration

## Remove a push configuration  Removes a specific push configuration from an application. The type of a push configuration is either `fcm`, `huawei`, or `apns`.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-remove-a-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.remove_push_configuration_by_id_response import RemovePushConfigurationByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    push_type = "push_type_example" # str | 
    provider_id = "provider_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a push configuration
        api_response = api_instance.remove_push_configuration_by_id(push_type, provider_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->remove_push_configuration_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a push configuration
        api_response = api_instance.remove_push_configuration_by_id(push_type, provider_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->remove_push_configuration_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_type** | **str**|  |
 **provider_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**RemovePushConfigurationByIdResponse**](RemovePushConfigurationByIdResponse.md)

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

# **retrieve_ip_whitelist**
> RetrieveIpWhitelistResponse retrieve_ip_whitelist()

Retrieve an IP whitelist

## Retrieve an IP whitelist  Retrieves a list of all the IP ranges and addresses that have access to your Sendbird application. This list is called an IP whitelist and its addresses are granted API access when the IP whitelist API enables [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notations.  If you specify which IP addresses or ranges to include in the whitelist, any unlisted foreign IP addresses will be denied access. If you don't specify any IP address or range to include in the whitelist, all IP addresses will be granted API access. You can configure the IP whitelist under Settings > Security > Allowed IPs in the [Sendbird Dashboard](https://dashboard.sendbird.com).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-retrieve-an-ip-whitelist

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.retrieve_ip_whitelist_response import RetrieveIpWhitelistResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an IP whitelist
        api_response = api_instance.retrieve_ip_whitelist(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->retrieve_ip_whitelist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**RetrieveIpWhitelistResponse**](RetrieveIpWhitelistResponse.md)

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

# **revoke_secondary_api_token_by_token**
> RevokeSecondaryApiTokenByTokenResponse revoke_secondary_api_token_by_token(api_token2)

Revoke a secondary API token

## Revoke a secondary API token  Revokes a secondary API token.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-revoke-a-secondary-api-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.revoke_secondary_api_token_by_token_response import RevokeSecondaryApiTokenByTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token2 = "api_token_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Revoke a secondary API token
        api_response = api_instance.revoke_secondary_api_token_by_token(api_token2)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->revoke_secondary_api_token_by_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Revoke a secondary API token
        api_response = api_instance.revoke_secondary_api_token_by_token(api_token2, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->revoke_secondary_api_token_by_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token2** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**RevokeSecondaryApiTokenByTokenResponse**](RevokeSecondaryApiTokenByTokenResponse.md)

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

# **set_domain_filter**
> SendBirdChannelResponse set_domain_filter(custom_type)

Message moderation

## 

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.set_domain_filter_data import SetDomainFilterData
from sendbird_platform_sdk.model.send_bird_channel_response import SendBirdChannelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    custom_type = "custom_type_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    set_domain_filter_data = SetDomainFilterData(
        domain_filter=SetDomainFilterDataDomainFilter(
            domains=[
                "domains_example",
            ],
            type=1,
            should_check_global=True,
        ),
        profanity_filter=SetDomainFilterDataProfanityFilter(
            keywords=[
                "keywords_example",
            ],
            regex_filters=[
                SetDomainFilterDataProfanityFilterRegexFiltersInner(
                    regex="regex_example",
                ),
            ],
            type=1,
            should_check_global=True,
        ),
        profanity_triggered_moderation=SetDomainFilterDataProfanityTriggeredModeration(
            count=1,
            duration=1,
            action=1,
        ),
        image_moderation=SetDomainFilterDataImageModeration(
            type=1,
            soft_block=True,
            limits=SetDomainFilterDataImageModerationLimits(
                adult=1,
                spoof=1,
                medical=1,
                violence=1,
                racy=1,
            ),
            check_urls=True,
        ),
    ) # SetDomainFilterData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Message moderation
        api_response = api_instance.set_domain_filter(custom_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->set_domain_filter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Message moderation
        api_response = api_instance.set_domain_filter(custom_type, api_token=api_token, set_domain_filter_data=set_domain_filter_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->set_domain_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_type** | **str**|  |
 **api_token** | **str**|  | [optional]
 **set_domain_filter_data** | [**SetDomainFilterData**](SetDomainFilterData.md)|  | [optional]

### Return type

[**SendBirdChannelResponse**](SendBirdChannelResponse.md)

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

# **unban_users_in_channels_with_custom_channel_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unban_users_in_channels_with_custom_channel_type(custom_type, user_ids)

Unban users in channels with a custom channel type

## Unban specified users in channels with a custom channel type at once.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    custom_type = "custom_type_example" # str | 
    user_ids = [
        "user_ids_example",
    ] # [str] | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unban users in channels with a custom channel type
        api_response = api_instance.unban_users_in_channels_with_custom_channel_type(custom_type, user_ids)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->unban_users_in_channels_with_custom_channel_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unban users in channels with a custom channel type
        api_response = api_instance.unban_users_in_channels_with_custom_channel_type(custom_type, user_ids, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->unban_users_in_channels_with_custom_channel_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_type** | **str**|  |
 **user_ids** | **[str]**|  |
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

# **unmute_users_in_channels_with_custom_channel_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unmute_users_in_channels_with_custom_channel_type(custom_type, user_ids)

Unmute users in channels with a custom channel type

## Unmute specified users in channels with a custom channel type at once.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    custom_type = "custom_type_example" # str | 
    user_ids = [
        "user_ids_example",
    ] # [str] | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unmute users in channels with a custom channel type
        api_response = api_instance.unmute_users_in_channels_with_custom_channel_type(custom_type, user_ids)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->unmute_users_in_channels_with_custom_channel_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unmute users in channels with a custom channel type
        api_response = api_instance.unmute_users_in_channels_with_custom_channel_type(custom_type, user_ids, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->unmute_users_in_channels_with_custom_channel_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_type** | **str**|  |
 **user_ids** | **[str]**|  |
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

# **update_apns_push_configuration_by_id**
> UpdateApnsPushConfigurationByIdResponse update_apns_push_configuration_by_id(provider_id)

Update an APNs push configuration

## Update an APNs push configuration  Updates a specific APNs (Apple Push Notification service) push configuration for your client app. You can also register the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  > __Note__: If your HTTP request body contains a [.p12](https://sendbird.com/docs/chat/v3/ios/guides/push-notifications#2-step-3-export-a-p12-file-and-upload-to-sendbird-dashboard) certificate file to upload to Sendbird server, you should send a [Multipart request](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api#2-headers-3-multipart-requests) .  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-an-apns-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.update_apns_push_configuration_by_id_data import UpdateApnsPushConfigurationByIdData
from sendbird_platform_sdk.model.update_apns_push_configuration_by_id_response import UpdateApnsPushConfigurationByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    provider_id = "provider_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_apns_push_configuration_by_id_data = UpdateApnsPushConfigurationByIdData(
        provider_id="provider_id_example",
        apns_cert=open('/path/to/file', 'rb'),
        apns_cert_env_type="apns_cert_env_type_example",
        apns_cert_password="apns_cert_password_example",
        has_unread_count_badge=True,
        content_available=True,
        mutable_content=True,
        push_sound="push_sound_example",
        apns_type="apns_type_example",
    ) # UpdateApnsPushConfigurationByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an APNs push configuration
        api_response = api_instance.update_apns_push_configuration_by_id(provider_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_apns_push_configuration_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an APNs push configuration
        api_response = api_instance.update_apns_push_configuration_by_id(provider_id, api_token=api_token, update_apns_push_configuration_by_id_data=update_apns_push_configuration_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_apns_push_configuration_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_apns_push_configuration_by_id_data** | [**UpdateApnsPushConfigurationByIdData**](UpdateApnsPushConfigurationByIdData.md)|  | [optional]

### Return type

[**UpdateApnsPushConfigurationByIdResponse**](UpdateApnsPushConfigurationByIdResponse.md)

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

# **update_default_channel_invitation_preference**
> UpdateDefaultChannelInvitationPreferenceResponse update_default_channel_invitation_preference()

Update default channel invitation preference

## Update default channel invitation preference  Updates the default channel invitation preference of an application.  > __Note__: Using the [update channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference) action, you can update the value of a specific user's channel invitation preference, which can be set individually by user.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.update_default_channel_invitation_preference_data import UpdateDefaultChannelInvitationPreferenceData
from sendbird_platform_sdk.model.update_default_channel_invitation_preference_response import UpdateDefaultChannelInvitationPreferenceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_default_channel_invitation_preference_data = UpdateDefaultChannelInvitationPreferenceData(
        auto_accept=True,
    ) # UpdateDefaultChannelInvitationPreferenceData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update default channel invitation preference
        api_response = api_instance.update_default_channel_invitation_preference(api_token=api_token, update_default_channel_invitation_preference_data=update_default_channel_invitation_preference_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_default_channel_invitation_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **update_default_channel_invitation_preference_data** | [**UpdateDefaultChannelInvitationPreferenceData**](UpdateDefaultChannelInvitationPreferenceData.md)|  | [optional]

### Return type

[**UpdateDefaultChannelInvitationPreferenceResponse**](UpdateDefaultChannelInvitationPreferenceResponse.md)

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

# **update_fcm_push_configuration_by_id**
> UpdateFcmPushConfigurationByIdResponse update_fcm_push_configuration_by_id(provider_id)

Update a FCM push configuration

## Update a FCM push configuration  Updates a specific FCM (Firebase Cloud Messaging) push configuration for your client app. You can also update the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-a-fcm-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.update_fcm_push_configuration_by_id_response import UpdateFcmPushConfigurationByIdResponse
from sendbird_platform_sdk.model.update_fcm_push_configuration_by_id_data import UpdateFcmPushConfigurationByIdData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    provider_id = "provider_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_fcm_push_configuration_by_id_data = UpdateFcmPushConfigurationByIdData(
        provider_id="provider_id_example",
        api_key="api_key_example",
        push_sound="push_sound_example",
    ) # UpdateFcmPushConfigurationByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a FCM push configuration
        api_response = api_instance.update_fcm_push_configuration_by_id(provider_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_fcm_push_configuration_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a FCM push configuration
        api_response = api_instance.update_fcm_push_configuration_by_id(provider_id, api_token=api_token, update_fcm_push_configuration_by_id_data=update_fcm_push_configuration_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_fcm_push_configuration_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_fcm_push_configuration_by_id_data** | [**UpdateFcmPushConfigurationByIdData**](UpdateFcmPushConfigurationByIdData.md)|  | [optional]

### Return type

[**UpdateFcmPushConfigurationByIdResponse**](UpdateFcmPushConfigurationByIdResponse.md)

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

# **update_hms_push_configuration_by_id**
> UpdateHmsPushConfigurationByIdResponse update_hms_push_configuration_by_id(provider_id)

Update an HMS push configuration

## Update an HMS push configuration  Updates a specific HMS (Huawei Mobile Services) push configuration for your client app. You can also update the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-an-hms-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.update_hms_push_configuration_by_id_response import UpdateHmsPushConfigurationByIdResponse
from sendbird_platform_sdk.model.update_hms_push_configuration_by_id_data import UpdateHmsPushConfigurationByIdData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    provider_id = "provider_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_hms_push_configuration_by_id_data = UpdateHmsPushConfigurationByIdData(
        provider_id="provider_id_example",
        huawei_app_id="huawei_app_id_example",
        huawei_app_secret="huawei_app_secret_example",
        push_sound="push_sound_example",
    ) # UpdateHmsPushConfigurationByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an HMS push configuration
        api_response = api_instance.update_hms_push_configuration_by_id(provider_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_hms_push_configuration_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an HMS push configuration
        api_response = api_instance.update_hms_push_configuration_by_id(provider_id, api_token=api_token, update_hms_push_configuration_by_id_data=update_hms_push_configuration_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_hms_push_configuration_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_hms_push_configuration_by_id_data** | [**UpdateHmsPushConfigurationByIdData**](UpdateHmsPushConfigurationByIdData.md)|  | [optional]

### Return type

[**UpdateHmsPushConfigurationByIdResponse**](UpdateHmsPushConfigurationByIdResponse.md)

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

# **update_push_notification_content_template**
> UpdatePushNotificationContentTemplateResponse update_push_notification_content_template(template_name)

Update a push notification content template

## Update a push notification content template  Updates a specific push notification content template of an application. The name of a content template is either `default` or `alternative`.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-a-push-notification-content-template ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.update_push_notification_content_template_response import UpdatePushNotificationContentTemplateResponse
from sendbird_platform_sdk.model.update_push_notification_content_template_data import UpdatePushNotificationContentTemplateData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    template_name = "template_name_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_push_notification_content_template_data = UpdatePushNotificationContentTemplateData(
        template_name="template_name_example",
        template="template_example",
        template_mesg="template_mesg_example",
        template_file="template_file_example",
        template_admn="template_admn_example",
    ) # UpdatePushNotificationContentTemplateData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a push notification content template
        api_response = api_instance.update_push_notification_content_template(template_name)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_push_notification_content_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a push notification content template
        api_response = api_instance.update_push_notification_content_template(template_name, api_token=api_token, update_push_notification_content_template_data=update_push_notification_content_template_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->update_push_notification_content_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_push_notification_content_template_data** | [**UpdatePushNotificationContentTemplateData**](UpdatePushNotificationContentTemplateData.md)|  | [optional]

### Return type

[**UpdatePushNotificationContentTemplateResponse**](UpdatePushNotificationContentTemplateResponse.md)

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

# **view_default_channel_invitation_preference**
> ViewDefaultChannelInvitationPreferenceResponse view_default_channel_invitation_preference()

View default channel invitation preference

## View default channel invitation preference  Retrieves the default channel invitation preference of an application.  > __Note__: Using the [view channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-channel-invitation-preference) action, you can retrieve the value of a specific user's channel invitation preference, which can be set individually by user.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-default-channel-invitation-preference

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.view_default_channel_invitation_preference_response import ViewDefaultChannelInvitationPreferenceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View default channel invitation preference
        api_response = api_instance.view_default_channel_invitation_preference(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_default_channel_invitation_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**ViewDefaultChannelInvitationPreferenceResponse**](ViewDefaultChannelInvitationPreferenceResponse.md)

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

# **view_push_configuration_by_id**
> ViewPushConfigurationByIdResponse view_push_configuration_by_id(push_type, provider_id)

View a push configuration

## View a push configuration  Retrieves a specific push configuration of an application. The type of a push configuration is either `fcm`, `huawei`, or `apns`.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-a-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.view_push_configuration_by_id_response import ViewPushConfigurationByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    push_type = "push_type_example" # str | 
    provider_id = "provider_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a push configuration
        api_response = api_instance.view_push_configuration_by_id(push_type, provider_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_push_configuration_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a push configuration
        api_response = api_instance.view_push_configuration_by_id(push_type, provider_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_push_configuration_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_type** | **str**|  |
 **provider_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewPushConfigurationByIdResponse**](ViewPushConfigurationByIdResponse.md)

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

# **view_push_notification_content_template**
> ViewPushNotificationContentTemplateResponse view_push_notification_content_template(template_name)

Get a push notification content template

## Get a push notification content template  Retrieves information on a specific push notification content templates of an application. The name of a content template is either `default` or `alternative`.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-a-push-notification-content-template ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.view_push_notification_content_template_response import ViewPushNotificationContentTemplateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    template_name = "template_name_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a push notification content template
        api_response = api_instance.view_push_notification_content_template(template_name)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_push_notification_content_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a push notification content template
        api_response = api_instance.view_push_notification_content_template(template_name, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_push_notification_content_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewPushNotificationContentTemplateResponse**](ViewPushNotificationContentTemplateResponse.md)

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

# **view_secondary_api_token_by_token**
> ViewSecondaryApiTokenByTokenResponse view_secondary_api_token_by_token(api_token2)

View a secondary API token

## View a secondary API token  Retrieves the information on a secondary API token.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-a-secondary-api-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.view_secondary_api_token_by_token_response import ViewSecondaryApiTokenByTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_api.ApplicationApi(api_client)
    api_token2 = "api_token_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a secondary API token
        api_response = api_instance.view_secondary_api_token_by_token(api_token2)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_secondary_api_token_by_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a secondary API token
        api_response = api_instance.view_secondary_api_token_by_token(api_token2, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_secondary_api_token_by_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token2** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewSecondaryApiTokenByTokenResponse**](ViewSecondaryApiTokenByTokenResponse.md)

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

