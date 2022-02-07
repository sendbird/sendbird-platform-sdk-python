# sendbird_platform_sdk.ApplicationApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_apns_push_configuration**](ApplicationApi.md#add_apns_push_configuration) | **POST** /v3/applications/push/apns | Add an APNs push configuration
[**add_fcm_push_configuration**](ApplicationApi.md#add_fcm_push_configuration) | **POST** /v3/applications/push/fcm | Add a FCM push configuration
[**add_hms_push_configuration**](ApplicationApi.md#add_hms_push_configuration) | **POST** /v3/applications/push/hms | Add an HMS push configuration
[**add_ip_to_whitelist**](ApplicationApi.md#add_ip_to_whitelist) | **PUT** /v3/applications/settings/ip_whitelist | Add an IP to a whitelist
[**delete_allowed_ips_from_whitelist**](ApplicationApi.md#delete_allowed_ips_from_whitelist) | **DELETE** /v3/applications/settings/ip_whitelist | Delete allowed IPs from a whitelist
[**delete_apns_certificate_by_id**](ApplicationApi.md#delete_apns_certificate_by_id) | **DELETE** /v3/applications/push/apns/cert/{provider_id} | Delete an APNs certificate
[**generate_secondary_api_token**](ApplicationApi.md#generate_secondary_api_token) | **POST** /v3/applications/api_tokens | Generate a secondary API token
[**list_push_configurations**](ApplicationApi.md#list_push_configurations) | **GET** /v3/applications/push/{push_type} | List push configurations
[**list_push_notification_content_templates**](ApplicationApi.md#list_push_notification_content_templates) | **GET** /v3/applications/push/message_templates | List push notification content templates
[**list_secondary_api_tokens**](ApplicationApi.md#list_secondary_api_tokens) | **GET** /v3/applications/api_tokens | List secondary API tokens
[**remove_push_configuration_by_id**](ApplicationApi.md#remove_push_configuration_by_id) | **DELETE** /v3/applications/push/{push_type}/{provider_id} | Remove a push configuration
[**retrieve_ip_whitelist**](ApplicationApi.md#retrieve_ip_whitelist) | **GET** /v3/applications/settings/ip_whitelist | Retrieve an IP whitelist
[**revoke_secondary_api_token_by_token**](ApplicationApi.md#revoke_secondary_api_token_by_token) | **DELETE** /v3/applications/api_tokens/{api_token} | Revoke a secondary API token
[**update_apns_push_configuration_by_id**](ApplicationApi.md#update_apns_push_configuration_by_id) | **PUT** /v3/applications/push/apns/{provider_id} | Update an APNs push configuration
[**update_default_channel_invitation_preference**](ApplicationApi.md#update_default_channel_invitation_preference) | **PUT** /v3/applications/default_channel_invitation_preference | Update default channel invitation preference
[**update_fcm_push_configuration_by_id**](ApplicationApi.md#update_fcm_push_configuration_by_id) | **PUT** /v3/applications/push/fcm/{provider_id} | Update a FCM push configuration
[**update_hms_push_configuration_by_id**](ApplicationApi.md#update_hms_push_configuration_by_id) | **PUT** /v3/applications/push/hms/{provider_id} | Update an HMS push configuration
[**update_push_notification_content_template**](ApplicationApi.md#update_push_notification_content_template) | **PUT** /v3/applications/push/message_templates/{template_name} | Update a push notification content template
[**view_default_channel_invitation_preference**](ApplicationApi.md#view_default_channel_invitation_preference) | **GET** /v3/applications/default_channel_invitation_preference | View default channel invitation preference
[**view_number_of_concurrent_connections**](ApplicationApi.md#view_number_of_concurrent_connections) | **GET** /v3/applications/ccu | View number of concurrent connections
[**view_number_of_daily_active_users**](ApplicationApi.md#view_number_of_daily_active_users) | **GET** /v3/applications/dau | View number of daily active users
[**view_number_of_monthly_active_users**](ApplicationApi.md#view_number_of_monthly_active_users) | **GET** /v3/applications/mau | View number of monthly active users
[**view_number_of_peak_connections**](ApplicationApi.md#view_number_of_peak_connections) | **GET** /v3/applications/peak_connections | View number of peak connections
[**view_push_configuration_by_id**](ApplicationApi.md#view_push_configuration_by_id) | **GET** /v3/applications/push/{push_type}/{provider_id} | View a push configuration
[**view_push_notification_content_template**](ApplicationApi.md#view_push_notification_content_template) | **GET** /v3/applications/push/message_templates/{template_name} | View a push notification content template
[**view_secondary_api_token_by_token**](ApplicationApi.md#view_secondary_api_token_by_token) | **GET** /v3/applications/api_tokens/{api_token} | View a secondary API token


# **add_apns_push_configuration**
> InlineResponse2003 add_apns_push_configuration()

Add an APNs push configuration

## Add an APNs push configuration  Registers an APNs (Apple Push Notification service) push configuration for your client app. To send push notifications to iOS devices, your should first register the APNs push configuration. You can also register the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  > __Note__: To upload a [.p12](https://sendbird.com/docs/chat/v3/ios/guides/push-notifications#2-step-3-export-a-p12-file-and-upload-to-sendbird-dashboard) certificate file to Sendbird server, you should send a [Multipart request](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api#2-headers-3-multipart-requests).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-add-an-apns-push-configuration

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2003 import InlineResponse2003
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

[**InlineResponse2003**](InlineResponse2003.md)

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
> InlineResponse2001 add_fcm_push_configuration()

Add a FCM push configuration

## Add a FCM push configuration  Registers a FCM (Firebase Cloud Messaging) push configuration for your client app. To send push notifications to Android devices, you should first register the FCM push configuration. You can also register the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-add-a-fcm-push-configuration

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2001 import InlineResponse2001
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

[**InlineResponse2001**](InlineResponse2001.md)

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
> InlineResponse2002 add_hms_push_configuration()

Add an HMS push configuration

## Add an HMS push configuration  Registers an HMS (Huawei Mobile Services) push configuration for your client app. To send push notifications to Android devices for HMS, you should first register the HMS push configuration. You can also register the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-add-an-hms-push-configuration

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.add_hms_push_configuration_data import AddHmsPushConfigurationData
from sendbird_platform_sdk.model.inline_response2002 import InlineResponse2002
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

[**InlineResponse2002**](InlineResponse2002.md)

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
> InlineResponse2006 add_ip_to_whitelist()

Add an IP to a whitelist

## Add an IP to a whitelist  Adds IP addresses and ranges to your Sendbird application settings. Both currently added and any previously added IPs are granted API access. You can configure the IP whitelist under Settings > Security > Allowed IPs in the [Sendbird Dashboard](https://dashboard.sendbird.com).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-add-an-ip-to-a-whitelist

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2006 import InlineResponse2006
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

[**InlineResponse2006**](InlineResponse2006.md)

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
> InlineResponse2006 delete_allowed_ips_from_whitelist(ip_whitelist_addresses)

Delete allowed IPs from a whitelist

## Delete allowed IPs from a whitelist  Deletes allowed IPs from the whitelist by specifying their IP addresses or ranges. You can configure the IP whitelist under Settings > Security > Allowed IPs in the [Sendbird Dashboard](https://dashboard.sendbird.com).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-delete-allowed-ips-from-a-whitelist

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2006 import InlineResponse2006
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

[**InlineResponse2006**](InlineResponse2006.md)

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
> InlineResponse20013 delete_apns_certificate_by_id(provider_id)

Delete an APNs certificate

## Delete an APNs certificate  Deletes a specific APNs certificate.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-delete-an-apns-certificate ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20013 import InlineResponse20013
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

[**InlineResponse20013**](InlineResponse20013.md)

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
> InlineResponse2007 generate_secondary_api_token()

Generate a secondary API token

## Generate a secondary API token  Generates a new secondary API token.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-generate-a-secondary-api-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.generate_secondary_api_token_data import GenerateSecondaryApiTokenData
from sendbird_platform_sdk.model.inline_response2007 import InlineResponse2007
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

[**InlineResponse2007**](InlineResponse2007.md)

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

# **list_push_configurations**
> InlineResponse20012 list_push_configurations(push_type)

List push configurations

## List push configurations  Retrieves a list of an application's registered push configurations.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-list-push-configurations ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20012 import InlineResponse20012
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

[**InlineResponse20012**](InlineResponse20012.md)

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
> InlineResponse2004 list_push_notification_content_templates()

List push notification content templates

## List push notification content templates  Retrieves a list of push notification content templates of an application.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-list-push-notification-content-templates

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2004 import InlineResponse2004
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

[**InlineResponse2004**](InlineResponse2004.md)

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
> InlineResponse2008 list_secondary_api_tokens()

List secondary API tokens

## List secondary API tokens  Retrieves a list of secondary API tokens.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-list-secondary-api-tokens

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2008 import InlineResponse2008
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

[**InlineResponse2008**](InlineResponse2008.md)

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

# **remove_push_configuration_by_id**
> InlineResponse20013 remove_push_configuration_by_id(push_type, provider_id)

Remove a push configuration

## Remove a push configuration  Removes a specific push configuration from an application. The type of a push configuration is either `fcm`, `huawei`, or `apns`.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-remove-a-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20013 import InlineResponse20013
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

[**InlineResponse20013**](InlineResponse20013.md)

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
> InlineResponse2006 retrieve_ip_whitelist()

Retrieve an IP whitelist

## Retrieve an IP whitelist  Retrieves a list of all the IP ranges and addresses that have access to your Sendbird application. This list is called an IP whitelist and its addresses are granted API access when the IP whitelist API enables [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notations.  If you specify which IP addresses or ranges to include in the whitelist, any unlisted foreign IP addresses will be denied access. If you don't specify any IP address or range to include in the whitelist, all IP addresses will be granted API access. You can configure the IP whitelist under Settings > Security > Allowed IPs in the [Sendbird Dashboard](https://dashboard.sendbird.com).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-retrieve-an-ip-whitelist

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2006 import InlineResponse2006
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

[**InlineResponse2006**](InlineResponse2006.md)

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
> InlineResponse2007 revoke_secondary_api_token_by_token(api_token2)

Revoke a secondary API token

## Revoke a secondary API token  Revokes a secondary API token.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-revoke-a-secondary-api-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2007 import InlineResponse2007
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

[**InlineResponse2007**](InlineResponse2007.md)

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
> InlineResponse20014 update_apns_push_configuration_by_id(provider_id)

Update an APNs push configuration

## Update an APNs push configuration  Updates a specific APNs (Apple Push Notification service) push configuration for your client app. You can also register the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  > __Note__: If your HTTP request body contains a [.p12](https://sendbird.com/docs/chat/v3/ios/guides/push-notifications#2-step-3-export-a-p12-file-and-upload-to-sendbird-dashboard) certificate file to upload to Sendbird server, you should send a [Multipart request](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api#2-headers-3-multipart-requests) .  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-an-apns-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.update_apns_push_configuration_by_id_data import UpdateApnsPushConfigurationByIdData
from sendbird_platform_sdk.model.inline_response20014 import InlineResponse20014
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

[**InlineResponse20014**](InlineResponse20014.md)

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
> InlineResponse2005 update_default_channel_invitation_preference()

Update default channel invitation preference

## Update default channel invitation preference  Updates the default channel invitation preference of an application.  > __Note__: Using the [update channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-update-channel-invitation-preference) action, you can update the value of a specific user's channel invitation preference, which can be set individually by user.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-default-channel-invitation-preference

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2005 import InlineResponse2005
from sendbird_platform_sdk.model.update_default_channel_invitation_preference_data import UpdateDefaultChannelInvitationPreferenceData
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

[**InlineResponse2005**](InlineResponse2005.md)

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
> InlineResponse20014 update_fcm_push_configuration_by_id(provider_id)

Update a FCM push configuration

## Update a FCM push configuration  Updates a specific FCM (Firebase Cloud Messaging) push configuration for your client app. You can also update the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-a-fcm-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.update_fcm_push_configuration_by_id_data import UpdateFcmPushConfigurationByIdData
from sendbird_platform_sdk.model.inline_response20014 import InlineResponse20014
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

[**InlineResponse20014**](InlineResponse20014.md)

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
> InlineResponse20014 update_hms_push_configuration_by_id(provider_id)

Update an HMS push configuration

## Update an HMS push configuration  Updates a specific HMS (Huawei Mobile Services) push configuration for your client app. You can also update the configurations in your [dashboard](https://dashboard.sendbird.com) under Settings > Application > Notifications.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-an-hms-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20014 import InlineResponse20014
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

[**InlineResponse20014**](InlineResponse20014.md)

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
> InlineResponse20015 update_push_notification_content_template(template_name)

Update a push notification content template

## Update a push notification content template  Updates a specific push notification content template of an application. The name of a content template is either `default` or `alternative`.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-update-a-push-notification-content-template ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20015 import InlineResponse20015
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

[**InlineResponse20015**](InlineResponse20015.md)

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
> InlineResponse2005 view_default_channel_invitation_preference()

View default channel invitation preference

## View default channel invitation preference  Retrieves the default channel invitation preference of an application.  > __Note__: Using the [view channel invitation preference](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-view-channel-invitation-preference) action, you can retrieve the value of a specific user's channel invitation preference, which can be set individually by user.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-default-channel-invitation-preference

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2005 import InlineResponse2005
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

[**InlineResponse2005**](InlineResponse2005.md)

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

# **view_number_of_concurrent_connections**
> InlineResponse200 view_number_of_concurrent_connections()

View number of concurrent connections

## View number of concurrent connections  Retrieves the number of devices and opened browser tabs which are currently connected to Sendbird server.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-concurrent-connections

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response200 import InlineResponse200
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
        # View number of concurrent connections
        api_response = api_instance.view_number_of_concurrent_connections(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_number_of_concurrent_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **view_number_of_daily_active_users**
> InlineResponse20011 view_number_of_daily_active_users()

View number of daily active users

## View number of daily active users  Retrieves the number of daily active users of the application (DAU).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-daily-active-users ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20011 import InlineResponse20011
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
    date = "date_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of daily active users
        api_response = api_instance.view_number_of_daily_active_users(api_token=api_token, date=date)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_number_of_daily_active_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **date** | **str**|  | [optional]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

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

# **view_number_of_monthly_active_users**
> InlineResponse20010 view_number_of_monthly_active_users()

View number of monthly active users

## View number of monthly active users  Retrieves the number of monthly active users of the application (MAU).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-monthly-active-users ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20010 import InlineResponse20010
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
    date = "date_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of monthly active users
        api_response = api_instance.view_number_of_monthly_active_users(api_token=api_token, date=date)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_number_of_monthly_active_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **date** | **str**|  | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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

# **view_number_of_peak_connections**
> InlineResponse2009 view_number_of_peak_connections(time_dimension, start_year, start_month, end_year, end_month)

View number of peak connections

## View number of peak connections  Retrieves the number of concurrently connected devices to Sendbird server during the requested time period.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-peak-connections ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2009 import InlineResponse2009
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
    time_dimension = "time_dimension_example" # str | 
    start_year = 1 # int | 
    start_month = 1 # int | 
    end_year = 1 # int | 
    end_month = 1 # int | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    start_day = 1 # int |  (optional)
    end_day = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View number of peak connections
        api_response = api_instance.view_number_of_peak_connections(time_dimension, start_year, start_month, end_year, end_month)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_number_of_peak_connections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of peak connections
        api_response = api_instance.view_number_of_peak_connections(time_dimension, start_year, start_month, end_year, end_month, api_token=api_token, start_day=start_day, end_day=end_day)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_number_of_peak_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_dimension** | **str**|  |
 **start_year** | **int**|  |
 **start_month** | **int**|  |
 **end_year** | **int**|  |
 **end_month** | **int**|  |
 **api_token** | **str**|  | [optional]
 **start_day** | **int**|  | [optional]
 **end_day** | **int**|  | [optional]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

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
> InlineResponse20012 view_push_configuration_by_id(push_type, provider_id)

View a push configuration

## View a push configuration  Retrieves a specific push configuration of an application. The type of a push configuration is either `fcm`, `huawei`, or `apns`.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-a-push-configuration ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20012 import InlineResponse20012
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

[**InlineResponse20012**](InlineResponse20012.md)

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
> InlineResponse20015 view_push_notification_content_template(template_name)

View a push notification content template

## View a push notification content template  Retrieves information on a specific push notification content templates of an application. The name of a content template is either `default` or `alternative`.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-a-push-notification-content-template ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response20015 import InlineResponse20015
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
        # View a push notification content template
        api_response = api_instance.view_push_notification_content_template(template_name)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->view_push_notification_content_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a push notification content template
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

[**InlineResponse20015**](InlineResponse20015.md)

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
> InlineResponse2007 view_secondary_api_token_by_token(api_token2)

View a secondary API token

## View a secondary API token  Retrieves the information on a secondary API token.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-a-secondary-api-token

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import application_api
from sendbird_platform_sdk.model.inline_response2007 import InlineResponse2007
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

[**InlineResponse2007**](InlineResponse2007.md)

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

