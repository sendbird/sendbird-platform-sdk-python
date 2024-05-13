# sendbird_platform_sdk.StatisticsApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_detailed_open_rate_of_announcement_by_id**](StatisticsApi.md#get_detailed_open_rate_of_announcement_by_id) | **GET** /v3/announcement_open_rate/{unique_id} | Get detailed open rate of an announcement
[**get_detailed_open_status_of_announcement_by_id**](StatisticsApi.md#get_detailed_open_status_of_announcement_by_id) | **GET** /v3/announcement_open_status/{unique_id} | Get detailed open status of an announcement
[**retrieve_advanced_analytics_metrics**](StatisticsApi.md#retrieve_advanced_analytics_metrics) | **GET** /v3/statistics/metric | Retrieve Advanced analytics metrics
[**view_number_of_concurrent_connections**](StatisticsApi.md#view_number_of_concurrent_connections) | **GET** /v3/applications/ccu | View number of concurrent connections
[**view_number_of_daily_active_users**](StatisticsApi.md#view_number_of_daily_active_users) | **GET** /v3/applications/dau | View number of daily active users
[**view_number_of_monthly_active_users**](StatisticsApi.md#view_number_of_monthly_active_users) | **GET** /v3/applications/mau | View number of monthly active users
[**view_number_of_peak_connections**](StatisticsApi.md#view_number_of_peak_connections) | **GET** /v3/applications/peak_connections | View number of peak connections


# **get_detailed_open_rate_of_announcement_by_id**
> GetDetailedOpenRateOfAnnouncementByIdResponse get_detailed_open_rate_of_announcement_by_id(unique_id)

Get detailed open rate of an announcement

## Get detailed open rate of an announcement  Retrieves the detailed open rate information of an announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-rate-of-an-announcement ----------------------------   `unique_id`      Type: string      Description: Specifies the unique ID of the announcement to get its open rate.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import statistics_api
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
    api_instance = statistics_api.StatisticsApi(api_client)
    unique_id = "unique_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get detailed open rate of an announcement
        api_response = api_instance.get_detailed_open_rate_of_announcement_by_id(unique_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->get_detailed_open_rate_of_announcement_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get detailed open rate of an announcement
        api_response = api_instance.get_detailed_open_rate_of_announcement_by_id(unique_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->get_detailed_open_rate_of_announcement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**|  |
 **api_token** | **str**|  | [optional]

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

# **get_detailed_open_status_of_announcement_by_id**
> GetDetailedOpenStatusOfAnnouncementByIdResponse get_detailed_open_status_of_announcement_by_id(unique_id)

Get detailed open status of an announcement

## Get detailed open status of an announcement  Retrieves the detailed open status information of a specific announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-status-of-an-announcement ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import statistics_api
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
    api_instance = statistics_api.StatisticsApi(api_client)
    unique_id = "unique_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
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
        api_response = api_instance.get_detailed_open_status_of_announcement_by_id(unique_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->get_detailed_open_status_of_announcement_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get detailed open status of an announcement
        api_response = api_instance.get_detailed_open_status_of_announcement_by_id(unique_id, api_token=api_token, limit=limit, next=next, unique_ids=unique_ids, channel_urls=channel_urls, has_opened=has_opened)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->get_detailed_open_status_of_announcement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**|  |
 **api_token** | **str**|  | [optional]
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

# **retrieve_advanced_analytics_metrics**
> RetrieveAdvancedAnalyticsMetricsResponse retrieve_advanced_analytics_metrics()

Retrieve Advanced analytics metrics

## Retrieve Advanced analytics metrics  Retrieves Advanced analytics metrics based on the specified parameters. You can retrieve either daily or monthly metrics using the time_dimension parameter.  >__Note__: Daily metrics are calculated and updated every three hours, starting at 1 a.m. in UTC. Meanwhile, monthly metrics are calculated after the last day of the month.  https://sendbird.com/docs/chat/v3/platform-api/guides/advanced-analytics#2-retrieve-advanced-analytics-metrics ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import statistics_api
from sendbird_platform_sdk.model.retrieve_advanced_analytics_metrics_response import RetrieveAdvancedAnalyticsMetricsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = statistics_api.StatisticsApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Advanced analytics metrics
        api_response = api_instance.retrieve_advanced_analytics_metrics(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->retrieve_advanced_analytics_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**RetrieveAdvancedAnalyticsMetricsResponse**](RetrieveAdvancedAnalyticsMetricsResponse.md)

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
> ViewNumberOfConcurrentConnectionsResponse view_number_of_concurrent_connections()

View number of concurrent connections

## View number of concurrent connections  Retrieves the number of devices and opened browser tabs which are currently connected to Sendbird server.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-concurrent-connections

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import statistics_api
from sendbird_platform_sdk.model.view_number_of_concurrent_connections_response import ViewNumberOfConcurrentConnectionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = statistics_api.StatisticsApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of concurrent connections
        api_response = api_instance.view_number_of_concurrent_connections(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->view_number_of_concurrent_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**ViewNumberOfConcurrentConnectionsResponse**](ViewNumberOfConcurrentConnectionsResponse.md)

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
> ViewNumberOfDailyActiveUsersResponse view_number_of_daily_active_users()

View number of daily active users

## View number of daily active users  Retrieves the number of daily active users of the application (DAU).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-daily-active-users ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import statistics_api
from sendbird_platform_sdk.model.view_number_of_daily_active_users_response import ViewNumberOfDailyActiveUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = statistics_api.StatisticsApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    date = "date_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of daily active users
        api_response = api_instance.view_number_of_daily_active_users(api_token=api_token, date=date)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->view_number_of_daily_active_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **date** | **str**|  | [optional]

### Return type

[**ViewNumberOfDailyActiveUsersResponse**](ViewNumberOfDailyActiveUsersResponse.md)

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
> ViewNumberOfMonthlyActiveUsersResponse view_number_of_monthly_active_users()

View number of monthly active users

## View number of monthly active users  Retrieves the number of monthly active users of the application (MAU).  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-monthly-active-users ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import statistics_api
from sendbird_platform_sdk.model.view_number_of_monthly_active_users_response import ViewNumberOfMonthlyActiveUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = statistics_api.StatisticsApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    date = "date_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of monthly active users
        api_response = api_instance.view_number_of_monthly_active_users(api_token=api_token, date=date)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->view_number_of_monthly_active_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **date** | **str**|  | [optional]

### Return type

[**ViewNumberOfMonthlyActiveUsersResponse**](ViewNumberOfMonthlyActiveUsersResponse.md)

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
> ViewNumberOfPeakConnectionsResponse view_number_of_peak_connections(time_dimension, start_year, start_month, end_year, end_month)

View number of peak connections

## View number of peak connections  Retrieves the number of concurrently connected devices to Sendbird server during the requested time period.  https://sendbird.com/docs/chat/v3/platform-api/guides/application#2-view-number-of-peak-connections ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import statistics_api
from sendbird_platform_sdk.model.view_number_of_peak_connections_response import ViewNumberOfPeakConnectionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = statistics_api.StatisticsApi(api_client)
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
        print("Exception when calling StatisticsApi->view_number_of_peak_connections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of peak connections
        api_response = api_instance.view_number_of_peak_connections(time_dimension, start_year, start_month, end_year, end_month, api_token=api_token, start_day=start_day, end_day=end_day)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling StatisticsApi->view_number_of_peak_connections: %s\n" % e)
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

[**ViewNumberOfPeakConnectionsResponse**](ViewNumberOfPeakConnectionsResponse.md)

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

