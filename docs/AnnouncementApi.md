# sendbird_platform_sdk.AnnouncementApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_detailed_open_rate_of_announcement_by_id**](AnnouncementApi.md#get_detailed_open_rate_of_announcement_by_id) | **GET** /v3/announcement_open_rate/{unique_id} | Get detailed open rate of an announcement
[**get_detailed_open_rate_of_announcement_group**](AnnouncementApi.md#get_detailed_open_rate_of_announcement_group) | **GET** /v3/announcement_open_rate_by_group/{announcement_group} | Get detailed open rate of an announcement group
[**get_detailed_open_status_of_announcement_by_id**](AnnouncementApi.md#get_detailed_open_status_of_announcement_by_id) | **GET** /v3/announcement_open_status/{unique_id} | Get detailed open status of an announcement
[**view_announcement_by_id**](AnnouncementApi.md#view_announcement_by_id) | **GET** /v3/announcements/{unique_id} | View an announcement


# **get_detailed_open_rate_of_announcement_by_id**
> GetDetailedOpenRateOfAnnouncementByIdResponse get_detailed_open_rate_of_announcement_by_id(api_token, unique_id)

Get detailed open rate of an announcement

## Get detailed open rate of an announcement  Retrieves the detailed open rate information of an announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-rate-of-an-announcement ----------------------------   `unique_id`      Type: string      Description: Specifies the unique ID of the announcement to get its open rate.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.get_detailed_open_rate_of_announcement_by_id_response import GetDetailedOpenRateOfAnnouncementByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    unique_id = "unique_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get detailed open rate of an announcement
        api_response = api_instance.get_detailed_open_rate_of_announcement_by_id(api_token, unique_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_detailed_open_rate_of_announcement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **unique_id** | **str**|  |

### Return type

[**GetDetailedOpenRateOfAnnouncementByIdResponse**](GetDetailedOpenRateOfAnnouncementByIdResponse.md)

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

# **get_detailed_open_rate_of_announcement_group**
> GetDetailedOpenRateOfAnnouncementGroupResponse get_detailed_open_rate_of_announcement_group(api_token, announcement_group)

Get detailed open rate of an announcement group

## Get detailed open rate of an announcement group  Retrieves the detailed open rate information of an announcement group.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-rate-of-an-announcement-group ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.get_detailed_open_rate_of_announcement_group_response import GetDetailedOpenRateOfAnnouncementGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    announcement_group = "announcement_group_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get detailed open rate of an announcement group
        api_response = api_instance.get_detailed_open_rate_of_announcement_group(api_token, announcement_group)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_detailed_open_rate_of_announcement_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **announcement_group** | **str**|  |

### Return type

[**GetDetailedOpenRateOfAnnouncementGroupResponse**](GetDetailedOpenRateOfAnnouncementGroupResponse.md)

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

# **get_detailed_open_status_of_announcement_by_id**
> GetDetailedOpenStatusOfAnnouncementByIdResponse get_detailed_open_status_of_announcement_by_id(api_token, unique_id)

Get detailed open status of an announcement

## Get detailed open status of an announcement  Retrieves the detailed open status information of a specific announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-status-of-an-announcement ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.get_detailed_open_status_of_announcement_by_id_response import GetDetailedOpenStatusOfAnnouncementByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    unique_id = "unique_id_example" # str | 
    limit = 1 # int |  (optional)
    next = "next_example" # str |  (optional)
    unique_ids = [
        "unique_ids_example",
    ] # [str] |  (optional)
    channel_urls = [
        "channel_urls_example",
    ] # [str] |  (optional)
    has_opened = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get detailed open status of an announcement
        api_response = api_instance.get_detailed_open_status_of_announcement_by_id(api_token, unique_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_detailed_open_status_of_announcement_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get detailed open status of an announcement
        api_response = api_instance.get_detailed_open_status_of_announcement_by_id(api_token, unique_id, limit=limit, next=next, unique_ids=unique_ids, channel_urls=channel_urls, has_opened=has_opened)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_detailed_open_status_of_announcement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **unique_id** | **str**|  |
 **limit** | **int**|  | [optional]
 **next** | **str**|  | [optional]
 **unique_ids** | **[str]**|  | [optional]
 **channel_urls** | **[str]**|  | [optional]
 **has_opened** | **bool**|  | [optional]

### Return type

[**GetDetailedOpenStatusOfAnnouncementByIdResponse**](GetDetailedOpenStatusOfAnnouncementByIdResponse.md)

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

# **view_announcement_by_id**
> ViewAnnouncementByIdResponse view_announcement_by_id(api_token, unique_id)

View an announcement

## View an announcement  Retrieves information on a specific announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-view-an-announcement ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.view_announcement_by_id_response import ViewAnnouncementByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    unique_id = "unique_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View an announcement
        api_response = api_instance.view_announcement_by_id(api_token, unique_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->view_announcement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **unique_id** | **str**|  |

### Return type

[**ViewAnnouncementByIdResponse**](ViewAnnouncementByIdResponse.md)

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

