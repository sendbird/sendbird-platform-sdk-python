# sendbird_platform_sdk.PrivacyApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_the_registration_of_gdpr_request_by_id**](PrivacyApi.md#cancel_the_registration_of_gdpr_request_by_id) | **DELETE** /v3/privacy/gdpr/{request_id} | Cancel the registration of a GDPR request
[**list_gdpr_requests**](PrivacyApi.md#list_gdpr_requests) | **GET** /v3/privacy/gdpr | List GDPR requests
[**register_gdpr_request**](PrivacyApi.md#register_gdpr_request) | **POST** /v3/privacy/gdpr | Register a GDPR request
[**view_gdpr_request_by_id**](PrivacyApi.md#view_gdpr_request_by_id) | **GET** /v3/privacy/gdpr/{request_id} | View a GDPR request


# **cancel_the_registration_of_gdpr_request_by_id**
> cancel_the_registration_of_gdpr_request_by_id(request_id)

Cancel the registration of a GDPR request

## Cancel the registration of a GDPR request  Cancels the registration of a specific GDPR request.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-privacy#2-cancel-the-registration-of-a-gdpr-request ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import privacy_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = privacy_api.PrivacyApi(api_client)
    request_id = "request_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel the registration of a GDPR request
        api_instance.cancel_the_registration_of_gdpr_request_by_id(request_id)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PrivacyApi->cancel_the_registration_of_gdpr_request_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel the registration of a GDPR request
        api_instance.cancel_the_registration_of_gdpr_request_by_id(request_id, api_token=api_token)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PrivacyApi->cancel_the_registration_of_gdpr_request_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |
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

# **list_gdpr_requests**
> ListGdprRequestsResponse list_gdpr_requests()

List GDPR requests

## List GDPR requests  Retrieves a list of GDPR requests of all types.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-privacy#2-list-gdpr-requests ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import privacy_api
from sendbird_platform_sdk.model.list_gdpr_requests_response import ListGdprRequestsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = privacy_api.PrivacyApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List GDPR requests
        api_response = api_instance.list_gdpr_requests(api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PrivacyApi->list_gdpr_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListGdprRequestsResponse**](ListGdprRequestsResponse.md)

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

# **register_gdpr_request**
> RegisterGdprRequestResponse register_gdpr_request()

Register a GDPR request

## Register a GDPR request  Registers a specific type of GDPR request to meet the GDPR's requirements.  > __Note__: Currently, only delete and access of the user data are supported. The features for the [right to restriction of processing](https://gdpr-info.eu/art-18-gdpr/) and [right to object](https://gdpr-info.eu/art-21-gdpr/) will be available soon.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-privacy#2-register-a-gdpr-request

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import privacy_api
from sendbird_platform_sdk.model.register_gdpr_request_response import RegisterGdprRequestResponse
from sendbird_platform_sdk.model.register_gdpr_request_data import RegisterGdprRequestData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = privacy_api.PrivacyApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    register_gdpr_request_data = RegisterGdprRequestData(
        action="action_example",
        user_ids=[
            "user_ids_example",
        ],
        channel_delete_option="channel_delete_option_example",
        user_id="user_id_example",
    ) # RegisterGdprRequestData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register a GDPR request
        api_response = api_instance.register_gdpr_request(api_token=api_token, register_gdpr_request_data=register_gdpr_request_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PrivacyApi->register_gdpr_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **register_gdpr_request_data** | [**RegisterGdprRequestData**](RegisterGdprRequestData.md)|  | [optional]

### Return type

[**RegisterGdprRequestResponse**](RegisterGdprRequestResponse.md)

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

# **view_gdpr_request_by_id**
> ViewGdprRequestByIdResponse view_gdpr_request_by_id(request_id)

View a GDPR request

## View a GDPR request  Retrieves a specific GDPR request.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-privacy#2-view-a-gdpr-request ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import privacy_api
from sendbird_platform_sdk.model.view_gdpr_request_by_id_response import ViewGdprRequestByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = privacy_api.PrivacyApi(api_client)
    request_id = "request_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a GDPR request
        api_response = api_instance.view_gdpr_request_by_id(request_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PrivacyApi->view_gdpr_request_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a GDPR request
        api_response = api_instance.view_gdpr_request_by_id(request_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PrivacyApi->view_gdpr_request_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewGdprRequestByIdResponse**](ViewGdprRequestByIdResponse.md)

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

