# sendbird_platform_sdk.AdvancedAnalyticsApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_advanced_analytics_metrics**](AdvancedAnalyticsApi.md#retrieve_advanced_analytics_metrics) | **GET** /v3/statistics/metric | Retrieve Advanced analytics metrics


# **retrieve_advanced_analytics_metrics**
> RetrieveAdvancedAnalyticsMetricsResponse retrieve_advanced_analytics_metrics()

Retrieve Advanced analytics metrics

## Retrieve Advanced analytics metrics  Retrieves Advanced analytics metrics based on the specified parameters. You can retrieve either daily or monthly metrics using the time_dimension parameter.  >__Note__: Daily metrics are calculated and updated every three hours, starting at 1 a.m. in UTC. Meanwhile, monthly metrics are calculated after the last day of the month.  https://sendbird.com/docs/chat/v3/platform-api/guides/advanced-analytics#2-retrieve-advanced-analytics-metrics ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import advanced_analytics_api
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
    api_instance = advanced_analytics_api.AdvancedAnalyticsApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Advanced analytics metrics
        api_response = api_instance.retrieve_advanced_analytics_metrics(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AdvancedAnalyticsApi->retrieve_advanced_analytics_metrics: %s\n" % e)
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

