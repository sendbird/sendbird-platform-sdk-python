# sendbird_platform_sdk.WebhooksApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**choose_which_events_to_subscribe_to**](WebhooksApi.md#choose_which_events_to_subscribe_to) | **PUT** /v3/applications/settings/webhook | Choose which events to subscribe to
[**retrieve_list_of_subscribed_events**](WebhooksApi.md#retrieve_list_of_subscribed_events) | **GET** /v3/applications/settings/webhook | Retrieve a list of subscribed events


# **choose_which_events_to_subscribe_to**
> ChooseWhichEventsToSubscribeToResponse choose_which_events_to_subscribe_to()

Choose which events to subscribe to

## Choose which events to subscribe to  Chooses which events for your webhook server to receive payloads for. By subscribing to specific events based on your own needs, you can control the number of HTTP requests to your webhook server.  https://sendbird.com/docs/chat/v3/platform-api/guides/webhooks#2-choose-which-events-to-subscribe-to

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import webhooks_api
from sendbird_platform_sdk.model.choose_which_events_to_subscribe_to_data import ChooseWhichEventsToSubscribeToData
from sendbird_platform_sdk.model.choose_which_events_to_subscribe_to_response import ChooseWhichEventsToSubscribeToResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    choose_which_events_to_subscribe_to_data = ChooseWhichEventsToSubscribeToData(
        enabled=True,
        url="url_example",
        include_members=True,
        enabled_events=[
            "enabled_events_example",
        ],
    ) # ChooseWhichEventsToSubscribeToData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Choose which events to subscribe to
        api_response = api_instance.choose_which_events_to_subscribe_to(api_token=api_token, choose_which_events_to_subscribe_to_data=choose_which_events_to_subscribe_to_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling WebhooksApi->choose_which_events_to_subscribe_to: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **choose_which_events_to_subscribe_to_data** | [**ChooseWhichEventsToSubscribeToData**](ChooseWhichEventsToSubscribeToData.md)|  | [optional]

### Return type

[**ChooseWhichEventsToSubscribeToResponse**](ChooseWhichEventsToSubscribeToResponse.md)

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

# **retrieve_list_of_subscribed_events**
> RetrieveListOfSubscribedEventsResponse retrieve_list_of_subscribed_events()

Retrieve a list of subscribed events

## Retrieve a list of subscribed events  Retrieves a list of events for your webhook server to receive payloads for.  https://sendbird.com/docs/chat/v3/platform-api/guides/webhooks#2-retrieve-a-list-of-subscribed-events ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import webhooks_api
from sendbird_platform_sdk.model.retrieve_list_of_subscribed_events_response import RetrieveListOfSubscribedEventsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    display_all_webhook_categories = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of subscribed events
        api_response = api_instance.retrieve_list_of_subscribed_events(api_token=api_token, display_all_webhook_categories=display_all_webhook_categories)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling WebhooksApi->retrieve_list_of_subscribed_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **display_all_webhook_categories** | **bool**|  | [optional]

### Return type

[**RetrieveListOfSubscribedEventsResponse**](RetrieveListOfSubscribedEventsResponse.md)

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

