# sendbird_platform_sdk.ScheduledMessageApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_channel_type_channel_url_scheduled_messages_scheduled_message_id_send_now_post**](ScheduledMessageApi.md#v3_channel_type_channel_url_scheduled_messages_scheduled_message_id_send_now_post) | **POST** /v3/{channel_type}/{channel_url}/scheduled_messages/{scheduled_message_id}/send_now | Send a scheduled message immediately
[**v3_group_channels_channel_url_scheduled_messages_post**](ScheduledMessageApi.md#v3_group_channels_channel_url_scheduled_messages_post) | **POST** /v3/group_channels/{channel_url}/scheduled_messages | Create a scheduled message
[**v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete**](ScheduledMessageApi.md#v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete) | **DELETE** /v3/group_channels/{channel_url}/scheduled_messages/{scheduled_message_id} | Cancel a scheduled message
[**v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_get**](ScheduledMessageApi.md#v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_get) | **GET** /v3/group_channels/{channel_url}/scheduled_messages/{scheduled_message_id} | View a scheduled message
[**v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_post**](ScheduledMessageApi.md#v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_post) | **POST** /v3/group_channels/{channel_url}/scheduled_messages/{scheduled_message_id} | Update a scheduled message
[**v3_scheduled_messages_count_get**](ScheduledMessageApi.md#v3_scheduled_messages_count_get) | **GET** /v3/scheduled_messages/count | View number of scheduled messages
[**v3_scheduled_messages_get**](ScheduledMessageApi.md#v3_scheduled_messages_get) | **GET** /v3/scheduled_messages | List scheduled messages


# **v3_channel_type_channel_url_scheduled_messages_scheduled_message_id_send_now_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v3_channel_type_channel_url_scheduled_messages_scheduled_message_id_send_now_post(channel_type, channel_url, scheduled_message_id)

Send a scheduled message immediately

## Send a scheduled message immediately This action sends a scheduled message immediately. A user can only send their own scheduled messages immediately. https://sendbird.com/docs/chat/v3/platform-api/message/scheduled-messages/send-a-scheduled-message-immediately -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import scheduled_message_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_message_api.ScheduledMessageApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    scheduled_message_id =  # int | 
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a scheduled message immediately
        api_response = api_instance.v3_channel_type_channel_url_scheduled_messages_scheduled_message_id_send_now_post(channel_type, channel_url, scheduled_message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_channel_type_channel_url_scheduled_messages_scheduled_message_id_send_now_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a scheduled message immediately
        api_response = api_instance.v3_channel_type_channel_url_scheduled_messages_scheduled_message_id_send_now_post(channel_type, channel_url, scheduled_message_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_channel_type_channel_url_scheduled_messages_scheduled_message_id_send_now_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **scheduled_message_id** | **int**|  |
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

# **v3_group_channels_channel_url_scheduled_messages_post**
> V3ScheduledMessagesGet200Response v3_group_channels_channel_url_scheduled_messages_post(channel_url)

Create a scheduled message

## Create a scheduled message This action creates a new scheduled message. If a user leaves the channel before the scheduled time for the message to be sent, the scheduled message will be removed. https://sendbird.com/docs/chat/v3/platform-api/message/scheduled-messages/create-a-scheduled-message -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import scheduled_message_api
from sendbird_platform_sdk.model.v3_scheduled_messages_get200_response import V3ScheduledMessagesGet200Response
from sendbird_platform_sdk.model.v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request import V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_message_api.ScheduledMessageApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request = V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest(
        message_type="message_type_example",
        user_id="user_id_example",
        message="message_example",
        file="file_example",
        url="url_example",
        scheduled_at=3.14,
        custom_type="custom_type_example",
        data="data_example",
        send_push=True,
        mention_type="mention_type_example",
        mentioned_user_ids=[
            "mentioned_user_ids_example",
        ],
        is_silent=True,
        mark_as_read=True,
        sorted_metaarray=[
            {},
        ],
        dedup_id="dedup_id_example",
        apns_bundle_id="apns_bundle_id_example",
        apple_critical_alert_options={},
        sound="sound_example",
null,
    ) # V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a scheduled message
        api_response = api_instance.v3_group_channels_channel_url_scheduled_messages_post(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_group_channels_channel_url_scheduled_messages_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a scheduled message
        api_response = api_instance.v3_group_channels_channel_url_scheduled_messages_post(channel_url, api_token=api_token, v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request=v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_group_channels_channel_url_scheduled_messages_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request** | [**V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest**](V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest.md)|  | [optional]

### Return type

[**V3ScheduledMessagesGet200Response**](V3ScheduledMessagesGet200Response.md)

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

# **v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete**
> V3ScheduledMessagesGet200Response v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete(channel_url, scheduled_message_id)

Cancel a scheduled message

## Cancel a scheduled message This action cancels a message that a user has scheduled to send at a later time. https://sendbird.com/docs/chat/v3/platform-api/message/scheduled-messages/cancel-a-scheduled-message -----------------------------                      

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import scheduled_message_api
from sendbird_platform_sdk.model.v3_scheduled_messages_get200_response import V3ScheduledMessagesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_message_api.ScheduledMessageApi(api_client)
    channel_url = "channel_url_example" # str | 
    scheduled_message_id =  # int | 
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel a scheduled message
        api_response = api_instance.v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete(channel_url, scheduled_message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel a scheduled message
        api_response = api_instance.v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete(channel_url, scheduled_message_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **scheduled_message_id** | **int**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**V3ScheduledMessagesGet200Response**](V3ScheduledMessagesGet200Response.md)

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

# **v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_get**
> V3ScheduledMessagesGet200Response v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_get(channel_url, scheduled_message_id)

View a scheduled message

## View a scheduled message This action retrieves information on a specific scheduled message. https://sendbird.com/docs/chat/v3/platform-api/message/scheduled-messages/view-a-scheduled-message -----------------------------                      

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import scheduled_message_api
from sendbird_platform_sdk.model.v3_scheduled_messages_get200_response import V3ScheduledMessagesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_message_api.ScheduledMessageApi(api_client)
    channel_url = "channel_url_example" # str | 
    scheduled_message_id =  # int | 
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a scheduled message
        api_response = api_instance.v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_get(channel_url, scheduled_message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a scheduled message
        api_response = api_instance.v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_get(channel_url, scheduled_message_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **scheduled_message_id** | **int**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**V3ScheduledMessagesGet200Response**](V3ScheduledMessagesGet200Response.md)

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

# **v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_post**
> V3ScheduledMessagesGet200Response v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_post(channel_url, scheduled_message_id)

Update a scheduled message

## Update a scheduled message This action updates information on a specific scheduled message. You can’t change the message type. Update operation should be done at least 5 minutes prior to the original scheduled time. https://sendbird.com/docs/chat/v3/platform-api/message/scheduled-messages/update-a-scheduled-message -----------------------------      

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import scheduled_message_api
from sendbird_platform_sdk.model.v3_scheduled_messages_get200_response import V3ScheduledMessagesGet200Response
from sendbird_platform_sdk.model.v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request import V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_message_api.ScheduledMessageApi(api_client)
    channel_url = "channel_url_example" # str | 
    scheduled_message_id =  # int | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request = V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest(
        message_type="message_type_example",
        user_id="user_id_example",
        message="message_example",
        file="file_example",
        url="url_example",
        scheduled_at=3.14,
        custom_type="custom_type_example",
        data="data_example",
        send_push=True,
        mention_type="mention_type_example",
        mentioned_user_ids=[
            "mentioned_user_ids_example",
        ],
        is_silent=True,
        mark_as_read=True,
        sorted_metaarray=[
            {},
        ],
        dedup_id="dedup_id_example",
        apns_bundle_id="apns_bundle_id_example",
        apple_critical_alert_options={},
        sound="sound_example",
null,
    ) # V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a scheduled message
        api_response = api_instance.v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_post(channel_url, scheduled_message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a scheduled message
        api_response = api_instance.v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_post(channel_url, scheduled_message_id, api_token=api_token, v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request=v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **scheduled_message_id** | **int**|  |
 **api_token** | **str**|  | [optional]
 **v3_group_channels_channel_url_scheduled_messages_scheduled_message_id_delete_request** | [**V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest**](V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest.md)|  | [optional]

### Return type

[**V3ScheduledMessagesGet200Response**](V3ScheduledMessagesGet200Response.md)

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

# **v3_scheduled_messages_count_get**
> V3ScheduledMessagesCountGet200Response v3_scheduled_messages_count_get()

View number of scheduled messages

## View number of scheduled messages This action retrieves the total number of scheduled messages that a user has. https://sendbird.com/docs/chat/v3/platform-api/message/scheduled-messages/view-number-of-scheduled-messages -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import scheduled_message_api
from sendbird_platform_sdk.model.v3_scheduled_messages_count_get200_response import V3ScheduledMessagesCountGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_message_api.ScheduledMessageApi(api_client)
    api_token = "Api-Token_example" # str |  (optional)
    channel_type = "channel_type_example" # str |  (optional)
    channel_url = "channel_url_example" # str |  (optional)
    sender_id = "sender_id_example" # str |  (optional)
    status = [
        {},
    ] # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] |  (optional)
    message_type = "message_type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of scheduled messages
        api_response = api_instance.v3_scheduled_messages_count_get(api_token=api_token, channel_type=channel_type, channel_url=channel_url, sender_id=sender_id, status=status, message_type=message_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_scheduled_messages_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **channel_type** | **str**|  | [optional]
 **channel_url** | **str**|  | [optional]
 **sender_id** | **str**|  | [optional]
 **status** | [**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**]({str: (bool, date, datetime, dict, float, int, list, str, none_type)}.md)|  | [optional]
 **message_type** | **str**|  | [optional]

### Return type

[**V3ScheduledMessagesCountGet200Response**](V3ScheduledMessagesCountGet200Response.md)

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

# **v3_scheduled_messages_get**
> V3ScheduledMessagesGet200Response v3_scheduled_messages_get()

List scheduled messages

## List scheduled messages This action retrieves a list of scheduled messages. A user can only see the list of their own scheduled messages. https://sendbird.com/docs/chat/v3/platform-api/message/scheduled-messages/list-scheduled-messages -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import scheduled_message_api
from sendbird_platform_sdk.model.int import Int
from sendbird_platform_sdk.model.v3_scheduled_messages_get200_response import V3ScheduledMessagesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scheduled_message_api.ScheduledMessageApi(api_client)
    api_token = "Api-Token_example" # str |  (optional)
    channel_type = "channel_type_example" # str |  (optional)
    channel_url = "channel_url_example" # str |  (optional)
    sender_id = "sender_id_example" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit =  # Int |  (optional)
    order = "order_example" # str |  (optional)
    reverse = True # bool |  (optional)
    status = [
        {},
    ] # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] |  (optional)
    message_type = "message_type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List scheduled messages
        api_response = api_instance.v3_scheduled_messages_get(api_token=api_token, channel_type=channel_type, channel_url=channel_url, sender_id=sender_id, token=token, limit=limit, order=order, reverse=reverse, status=status, message_type=message_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ScheduledMessageApi->v3_scheduled_messages_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **channel_type** | **str**|  | [optional]
 **channel_url** | **str**|  | [optional]
 **sender_id** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **Int**|  | [optional]
 **order** | **str**|  | [optional]
 **reverse** | **bool**|  | [optional]
 **status** | [**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**]({str: (bool, date, datetime, dict, float, int, list, str, none_type)}.md)|  | [optional]
 **message_type** | **str**|  | [optional]

### Return type

[**V3ScheduledMessagesGet200Response**](V3ScheduledMessagesGet200Response.md)

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

