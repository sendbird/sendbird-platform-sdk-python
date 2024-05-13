# sendbird_platform_sdk.PinAMessageApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_channel_type_channel_url_messages_message_id_pin_post**](PinAMessageApi.md#v3_channel_type_channel_url_messages_message_id_pin_post) | **POST** /v3/{channel_type}/{channel_url}/messages/{message_id}/pin | Add a new pin


# **v3_channel_type_channel_url_messages_message_id_pin_post**
> SendBirdChannelResponse v3_channel_type_channel_url_messages_message_id_pin_post(channel_type, channel_url, message_id)

Add a new pin

## Add a new pin Pin a message to its channel. -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import pin_a_message_api
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
    api_instance = pin_a_message_api.PinAMessageApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a new pin
        api_response = api_instance.v3_channel_type_channel_url_messages_message_id_pin_post(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PinAMessageApi->v3_channel_type_channel_url_messages_message_id_pin_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a new pin
        api_response = api_instance.v3_channel_type_channel_url_messages_message_id_pin_post(channel_type, channel_url, message_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PinAMessageApi->v3_channel_type_channel_url_messages_message_id_pin_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **int**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**SendBirdChannelResponse**](SendBirdChannelResponse.md)

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

