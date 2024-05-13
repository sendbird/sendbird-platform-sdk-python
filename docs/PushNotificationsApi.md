# sendbird_platform_sdk.PushNotificationsApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_applications_push_settings_get**](PushNotificationsApi.md#v3_applications_push_settings_get) | **GET** /v3/applications/push/settings | Check push notifications
[**v3_applications_push_settings_put**](PushNotificationsApi.md#v3_applications_push_settings_put) | **PUT** /v3/applications/push/settings | Turn on push notifications


# **v3_applications_push_settings_get**
> V3ApplicationsPushSettingsGet200Response v3_applications_push_settings_get()

Check push notifications

## Check push notifications Shows whether the push notifications feature is turned on for an application. https://sendbird.com/docs/chat/v3/platform-api/application/managing-notifications/check-push-notifications -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import push_notifications_api
from sendbird_platform_sdk.model.v3_applications_push_settings_get200_response import V3ApplicationsPushSettingsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = push_notifications_api.PushNotificationsApi(api_client)
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check push notifications
        api_response = api_instance.v3_applications_push_settings_get(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PushNotificationsApi->v3_applications_push_settings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**V3ApplicationsPushSettingsGet200Response**](V3ApplicationsPushSettingsGet200Response.md)

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

# **v3_applications_push_settings_put**
> ListPushConfigurationsResponse v3_applications_push_settings_put()

Turn on push notifications

## Turn on push notifications Determines whether to turn on the push notifications feature for an application. https://sendbird.com/docs/chat/v3/platform-api/application/managing-notifications/turn-on-push-notifications -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import push_notifications_api
from sendbird_platform_sdk.model.list_push_configurations_response import ListPushConfigurationsResponse
from sendbird_platform_sdk.model.v3_applications_push_settings_get_request import V3ApplicationsPushSettingsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = push_notifications_api.PushNotificationsApi(api_client)
    api_token = "Api-Token_example" # str |  (optional)
    v3_applications_push_settings_get_request = V3ApplicationsPushSettingsGetRequest(
        push_enabled=True,
    ) # V3ApplicationsPushSettingsGetRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Turn on push notifications
        api_response = api_instance.v3_applications_push_settings_put(api_token=api_token, v3_applications_push_settings_get_request=v3_applications_push_settings_get_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PushNotificationsApi->v3_applications_push_settings_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **v3_applications_push_settings_get_request** | [**V3ApplicationsPushSettingsGetRequest**](V3ApplicationsPushSettingsGetRequest.md)|  | [optional]

### Return type

[**ListPushConfigurationsResponse**](ListPushConfigurationsResponse.md)

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

