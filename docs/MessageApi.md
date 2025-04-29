# sendbird_platform_sdk.MessageApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_extra_data_to_a_message**](MessageApi.md#add_extra_data_to_a_message) | **POST** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Add extra data to a message
[**delete_a_message**](MessageApi.md#delete_a_message) | **DELETE** /v3/{channel_type}/{channel_url}/messages/{message_id} | Delete a message
[**get_a_message**](MessageApi.md#get_a_message) | **GET** /v3/{channel_type}/{channel_url}/messages/{message_id} | Get a message
[**get_total_number_of_messages_in_a_channel**](MessageApi.md#get_total_number_of_messages_in_a_channel) | **GET** /v3/{channel_type}/{channel_url}/messages/total_count | Get total number of messages in a channel
[**list_messages**](MessageApi.md#list_messages) | **GET** /v3/{channel_type}/{channel_url}/messages | List messages
[**mark_channel_messages_as_read**](MessageApi.md#mark_channel_messages_as_read) | **PUT** /v3/group_channels/{channel_url}/messages/mark_as_read | Mark all messages as read
[**migrate_messages**](MessageApi.md#migrate_messages) | **POST** /v3/migration/{target_channel_url} | Migrate messages
[**remove_extra_data_from_a_message**](MessageApi.md#remove_extra_data_from_a_message) | **DELETE** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Remove extra data from a message
[**send_a_message**](MessageApi.md#send_a_message) | **POST** /v3/{channel_type}/{channel_url}/messages | Send a message
[**update_a_message**](MessageApi.md#update_a_message) | **PUT** /v3/{channel_type}/{channel_url}/messages/{message_id} | Update a message
[**update_extra_data_in_a_message**](MessageApi.md#update_extra_data_in_a_message) | **PUT** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Update extra data in a message


# **add_extra_data_to_a_message**
> AddExtraDataToAMessageResponse add_extra_data_to_a_message(channel_type, channel_url, message_id)

Add extra data to a message

## Add extra data to a message  Adds one or more key-values items which store additional information for a message.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/message-add-metadata#1-add-metadata ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.add_extra_data_to_a_message_request import AddExtraDataToAMessageRequest
from sendbird_platform_sdk.model.add_extra_data_to_a_message_response import AddExtraDataToAMessageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    message_id = "message_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_extra_data_to_a_message_request = AddExtraDataToAMessageRequest(
        sorted_metaarray=SendbirdSortedMetaarray([
            SendbirdSortedMetaarrayInner(
                key="key_example",
                value=[
                    "value_example",
                ],
            ),
        ]),
    ) # AddExtraDataToAMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add extra data to a message
        api_response = api_instance.add_extra_data_to_a_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_extra_data_to_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add extra data to a message
        api_response = api_instance.add_extra_data_to_a_message(channel_type, channel_url, message_id, api_token=api_token, add_extra_data_to_a_message_request=add_extra_data_to_a_message_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_extra_data_to_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **message_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **add_extra_data_to_a_message_request** | [**AddExtraDataToAMessageRequest**](AddExtraDataToAMessageRequest.md)|  | [optional]

### Return type

[**AddExtraDataToAMessageResponse**](AddExtraDataToAMessageResponse.md)

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

# **delete_a_message**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_a_message(channel_type, channel_url, message_id)

Delete a message

## Delete a message  Deletes a message from a channel.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/delete-a-message#1-delete-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    message_id = "message_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a message
        api_response = api_instance.delete_a_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->delete_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a message
        api_response = api_instance.delete_a_message(channel_type, channel_url, message_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->delete_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **message_id** | **str**| (Required)  |
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

# **get_a_message**
> SendbirdMessageResponse get_a_message(channel_type, channel_url, message_id)

Get a message

## Get a message  Retrieves information on a specific message.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/get-a-message#1-get-a-message ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.  `message_id`      Type: long      Description: Specifies the unique ID of the message to retrieve.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.sendbird_message_response import SendbirdMessageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    message_id = "message_id_example" # str | (Required) 
    include_reactions = True # bool |  (optional)
    include_thread_info = True # bool |  (optional)
    include_parent_message_info = True # bool |  (optional)
    include_poll_details = True # bool | Determines whether to include all properties of a poll resource with a full list of options in the results. If set to false, a selection of poll resource properties consisting of id, title, close_at, created_at, updated_at, status, and message_id are returned. (Default: false) * To use this property, the polls feature should be turned on in Settings > Chat > Features on Sendbird Dashboard. (optional)
    with_sorted_meta_array = True # bool |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a message
        api_response = api_instance.get_a_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->get_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a message
        api_response = api_instance.get_a_message(channel_type, channel_url, message_id, include_reactions=include_reactions, include_thread_info=include_thread_info, include_parent_message_info=include_parent_message_info, include_poll_details=include_poll_details, with_sorted_meta_array=with_sorted_meta_array, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->get_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **message_id** | **str**| (Required)  |
 **include_reactions** | **bool**|  | [optional]
 **include_thread_info** | **bool**|  | [optional]
 **include_parent_message_info** | **bool**|  | [optional]
 **include_poll_details** | **bool**| Determines whether to include all properties of a poll resource with a full list of options in the results. If set to false, a selection of poll resource properties consisting of id, title, close_at, created_at, updated_at, status, and message_id are returned. (Default: false) * To use this property, the polls feature should be turned on in Settings &gt; Chat &gt; Features on Sendbird Dashboard. | [optional]
 **with_sorted_meta_array** | **bool**|  | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**SendbirdMessageResponse**](SendbirdMessageResponse.md)

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

# **get_total_number_of_messages_in_a_channel**
> GetTotalNumberOfMessagesInAChannelResponse get_total_number_of_messages_in_a_channel(channel_type, channel_url)

Get total number of messages in a channel

## Get total number of messages in a channel  Retrieves the total number of messages in a specific channel.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/get-total-number-of-messages-in-a-channel#1-get-total-number-of-messages-in-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.get_total_number_of_messages_in_a_channel_response import GetTotalNumberOfMessagesInAChannelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get total number of messages in a channel
        api_response = api_instance.get_total_number_of_messages_in_a_channel(channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->get_total_number_of_messages_in_a_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get total number of messages in a channel
        api_response = api_instance.get_total_number_of_messages_in_a_channel(channel_type, channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->get_total_number_of_messages_in_a_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]

### Return type

[**GetTotalNumberOfMessagesInAChannelResponse**](GetTotalNumberOfMessagesInAChannelResponse.md)

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

# **list_messages**
> ListMessagesResponse list_messages(channel_type, channel_url, message_ts, message_id)

List messages

## List messages  You can retrieve a list of past messages of a specific channel with this API.  By default, this action returns a list of messages in the order they were created. Replies in threaded messages are also listed in the chronological order of their creation like other messages, not grouped with their parent messages.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/list-messages#1-list-messages  `channel_type`   Type: string   Description: Specifies the type of the channel. Either open_channels or group_channels.   `channel_url`   Type: string   Description: Specifies the URL of the channel to retrieve a list of past messages.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.list_messages_response import ListMessagesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    message_ts = 1 # int | Specifies the timestamp to be the reference point of the query in Unix milliseconds. Either this or the message_id parameter below should be specified in your query URL to retrieve a list. It fetches messages that were sent prior to and after the specified message_ts and the default value for both prev_limit and next_limit is 15.
    message_id = 1 # int | Specifies the unique ID of the message to be the reference point of the query. Either this or the message_ts parameter above should be specified in your query URL to retrieve a list. It fetches messages that were sent prior to and after the specified message_id and the default value for both prev_limit and next_limit is 15.
    prev_limit = 1 # int | Specifies the number of previously sent messages to retrieve before message_ts. For example, if message_ts=1484202848298, then prev_limit=50 returns 50 messages sent by 1484202848297 (message_ts - 1). Acceptable values range from 0 to 200. (Default: 15) (optional)
    next_limit = 1 # int | Specifies the number of sent messages to retrieve after message_ts. For example, if message_ts=1484202848298, then next_limit=50 returns 50 messages sent from 1484202848299 (message_ts + 1). Acceptable values range from 0 to 200. (Default: 15) (optional)
    include = True # bool | Determines whether to include messages sent exactly on the specified message_ts in the results. (Default: true) (optional)
    reverse = True # bool | Determines whether to sort the results in reverse chronological order. If set to true, messages appear in reverse chronological order where the newest comes first and the oldest last. (Default: false) (optional)
    sender_id = "sender_id_example" # str | Restricts the search scope to only retrieve messages sent by the user with the specified ID. (optional)
    sender_ids = "sender_ids_example" # str | Restricts the search scope to only retrieve messages sent by one or more users with the specified IDs listed in a comma-separated string. (optional)
    operator_filter = "all" # str |  (optional)
    custom_types = "custom_types_example" # str | Specifies a comma-separated string of one or more custom message types to retrieve. The value set to this parameter can serve as a filter as follows: - A string of specific custom types: Messages with the corresponding custom types are returned. - Empty like &custom_types=&...: Messages whose custom_type property is empty or has a value of null are returned. - An asterisk (\\*) (default): All messages are returned regardless of their custom_type. (optional)
    message_type = "MESG" # str |  (optional)
    including_removed = True # bool |  (optional)
    include_reactions = True # bool |  (optional)
    include_reply_type = "NONE" # str | One of following values: NONE, ALL, ONLY_REPLY_TO_CHANNEL (optional)
    include_parent_message_info = True # bool |  (optional)
    include_thread_info = True # bool |  (optional)
    include_poll_details = True # bool | Determines whether to include all properties of a poll resource with a full list of options in the results. If set to false, a selection of poll resource properties consisting of id, title, close_at, created_at, updated_at, status, and message_id are returned. (Default: false) * To use this property, the polls feature should be turned on in Settings > Chat > Features on Sendbird Dashboard. (optional)
    with_sorted_meta_array = True # bool | Determines whether to include the sorted_metaarray property in the response. (Default: false) (optional)
    show_subchannel_messages_only = True # bool |  (optional)
    user_id = "user_id_example" # str |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List messages
        api_response = api_instance.list_messages(channel_type, channel_url, message_ts, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List messages
        api_response = api_instance.list_messages(channel_type, channel_url, message_ts, message_id, prev_limit=prev_limit, next_limit=next_limit, include=include, reverse=reverse, sender_id=sender_id, sender_ids=sender_ids, operator_filter=operator_filter, custom_types=custom_types, message_type=message_type, including_removed=including_removed, include_reactions=include_reactions, include_reply_type=include_reply_type, include_parent_message_info=include_parent_message_info, include_thread_info=include_thread_info, include_poll_details=include_poll_details, with_sorted_meta_array=with_sorted_meta_array, show_subchannel_messages_only=show_subchannel_messages_only, user_id=user_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **message_ts** | **int**| Specifies the timestamp to be the reference point of the query in Unix milliseconds. Either this or the message_id parameter below should be specified in your query URL to retrieve a list. It fetches messages that were sent prior to and after the specified message_ts and the default value for both prev_limit and next_limit is 15. |
 **message_id** | **int**| Specifies the unique ID of the message to be the reference point of the query. Either this or the message_ts parameter above should be specified in your query URL to retrieve a list. It fetches messages that were sent prior to and after the specified message_id and the default value for both prev_limit and next_limit is 15. |
 **prev_limit** | **int**| Specifies the number of previously sent messages to retrieve before message_ts. For example, if message_ts&#x3D;1484202848298, then prev_limit&#x3D;50 returns 50 messages sent by 1484202848297 (message_ts - 1). Acceptable values range from 0 to 200. (Default: 15) | [optional]
 **next_limit** | **int**| Specifies the number of sent messages to retrieve after message_ts. For example, if message_ts&#x3D;1484202848298, then next_limit&#x3D;50 returns 50 messages sent from 1484202848299 (message_ts + 1). Acceptable values range from 0 to 200. (Default: 15) | [optional]
 **include** | **bool**| Determines whether to include messages sent exactly on the specified message_ts in the results. (Default: true) | [optional]
 **reverse** | **bool**| Determines whether to sort the results in reverse chronological order. If set to true, messages appear in reverse chronological order where the newest comes first and the oldest last. (Default: false) | [optional]
 **sender_id** | **str**| Restricts the search scope to only retrieve messages sent by the user with the specified ID. | [optional]
 **sender_ids** | **str**| Restricts the search scope to only retrieve messages sent by one or more users with the specified IDs listed in a comma-separated string. | [optional]
 **operator_filter** | **str**|  | [optional]
 **custom_types** | **str**| Specifies a comma-separated string of one or more custom message types to retrieve. The value set to this parameter can serve as a filter as follows: - A string of specific custom types: Messages with the corresponding custom types are returned. - Empty like &amp;custom_types&#x3D;&amp;...: Messages whose custom_type property is empty or has a value of null are returned. - An asterisk (\\*) (default): All messages are returned regardless of their custom_type. | [optional]
 **message_type** | **str**|  | [optional]
 **including_removed** | **bool**|  | [optional]
 **include_reactions** | **bool**|  | [optional]
 **include_reply_type** | **str**| One of following values: NONE, ALL, ONLY_REPLY_TO_CHANNEL | [optional]
 **include_parent_message_info** | **bool**|  | [optional]
 **include_thread_info** | **bool**|  | [optional]
 **include_poll_details** | **bool**| Determines whether to include all properties of a poll resource with a full list of options in the results. If set to false, a selection of poll resource properties consisting of id, title, close_at, created_at, updated_at, status, and message_id are returned. (Default: false) * To use this property, the polls feature should be turned on in Settings &gt; Chat &gt; Features on Sendbird Dashboard. | [optional]
 **with_sorted_meta_array** | **bool**| Determines whether to include the sorted_metaarray property in the response. (Default: false) | [optional]
 **show_subchannel_messages_only** | **bool**|  | [optional]
 **user_id** | **str**|  | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**ListMessagesResponse**](ListMessagesResponse.md)

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

# **mark_channel_messages_as_read**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} mark_channel_messages_as_read(channel_url)

Mark all messages as read

## Mark all messages as read  Marks all messages in a group channel as read for a specific user. This action is only applicable for users in a group channel.  https://sendbird.com/docs/chat/platform-api/v3/message/read-receipts/mark-all-messages-as-read-message#1-mark-all-messages-as-read

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.mark_channel_messages_as_read_request import MarkChannelMessagesAsReadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    mark_channel_messages_as_read_request = MarkChannelMessagesAsReadRequest(
        user_id="user_id_example",
    ) # MarkChannelMessagesAsReadRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mark all messages as read
        api_response = api_instance.mark_channel_messages_as_read(channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->mark_channel_messages_as_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark all messages as read
        api_response = api_instance.mark_channel_messages_as_read(channel_url, api_token=api_token, mark_channel_messages_as_read_request=mark_channel_messages_as_read_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->mark_channel_messages_as_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **mark_channel_messages_as_read_request** | [**MarkChannelMessagesAsReadRequest**](MarkChannelMessagesAsReadRequest.md)|  | [optional]

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

# **migrate_messages**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} migrate_messages(target_channel_url)

Migrate messages

## Migrate messages  Using our migration API, you can migrate the messages from another system into a Sendbird system's [channel](https://sendbird.com/docs/chat/v3/platform-api/guides/channel-types) which consists of users, messages, and other chat-related data.  > To turn on this feature, [contact our support team](https://dashboard.sendbird.com/settings/contact_us).      There are three things to do in advance before the migration. Follow the instructions below:  1. Register the users of your current chat solution to your Sendbird application. You can migrate the users into the Sendbird system using the [user creation API](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-create-a-user).      2. Create either an [open](https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-create-a-channel) or a [group](https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-create-a-channel) channel to migrate the messages of your chat solution. The Sendbird system doesn't create a channel for your migration automatically.      3. The maximum number of migrated messages per call is 100. To avoid the failure during your migration, you must adjust the number of messages to process at once via the API.       https://sendbird.com/docs/chat/platform-api/v3/message/migration/migrate-messages#1-migrate-messages

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    target_channel_url = "target_channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Migrate messages
        api_response = api_instance.migrate_messages(target_channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->migrate_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Migrate messages
        api_response = api_instance.migrate_messages(target_channel_url, api_token=api_token, body=body)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->migrate_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **remove_extra_data_from_a_message**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remove_extra_data_from_a_message(channel_type, channel_url, message_id)

Remove extra data from a message

## Remove extra data from a message  Removes specific items from a message by their keys.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/message-remove-metadata#1-remove-metadata ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    message_id = "message_id_example" # str | (Required) 
    keys = "keys_example" # str |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove extra data from a message
        api_response = api_instance.remove_extra_data_from_a_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->remove_extra_data_from_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove extra data from a message
        api_response = api_instance.remove_extra_data_from_a_message(channel_type, channel_url, message_id, keys=keys, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->remove_extra_data_from_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **message_id** | **str**| (Required)  |
 **keys** | **str**|  | [optional]
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

# **send_a_message**
> SendbirdMessageResponse send_a_message(channel_type, channel_url)

Send a message

## Send a message  You can use this action to send a text message, a file message, or an admin message to a specific channel. Sendbird Chat SDKs and the platform API allows you to upload any type of files in messages to the Sendbird server. See [Message Overview](https://sendbird.com/docs/chat/platform-api/v3/message/message-overview) for more information on each message type. Messages are sent between client devices running the Sendbird Chat SDK or UIKit as well as programmatically from businesses to their customers. For instance, a delivery app can automatically send a message like \"Arriving in one minute!\" on behalf of a delivery driver.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/send-a-message#1-send-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.sendbird_message_response import SendbirdMessageResponse
from sendbird_platform_sdk.model.send_a_message_request import SendAMessageRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    send_a_message_request = SendAMessageRequest(None) # SendAMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a message
        api_response = api_instance.send_a_message(channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->send_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a message
        api_response = api_instance.send_a_message(channel_type, channel_url, api_token=api_token, send_a_message_request=send_a_message_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->send_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **send_a_message_request** | [**SendAMessageRequest**](SendAMessageRequest.md)|  | [optional]

### Return type

[**SendbirdMessageResponse**](SendbirdMessageResponse.md)

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

# **update_a_message**
> SendbirdMessageResponse update_a_message(channel_type, channel_url, message_id)

Update a message

## Update a message  Updates specific information on a message.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/update-a-message#1-update-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.sendbird_message_response import SendbirdMessageResponse
from sendbird_platform_sdk.model.update_a_message_request import UpdateAMessageRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    message_id = "message_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_a_message_request = UpdateAMessageRequest(
        custom_type="custom_type_example",
        data="data_example",
        mention_type="mention_type_example",
        mentioned_user_ids=[
            "mentioned_user_ids_example",
        ],
        message="message_example",
        url="url_example",
        message_type="MESG",
    ) # UpdateAMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a message
        api_response = api_instance.update_a_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a message
        api_response = api_instance.update_a_message(channel_type, channel_url, message_id, api_token=api_token, update_a_message_request=update_a_message_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **message_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_a_message_request** | [**UpdateAMessageRequest**](UpdateAMessageRequest.md)|  | [optional]

### Return type

[**SendbirdMessageResponse**](SendbirdMessageResponse.md)

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

# **update_extra_data_in_a_message**
> UpdateExtraDataInAMessageResponse update_extra_data_in_a_message(channel_type, channel_url, message_id)

Update extra data in a message

## Update extra data in a message  Updates the values of specific items by their keys.  https://sendbird.com/docs/chat/platform-api/v3/message/messaging-basics/message-update-metadata#1-update-metadata ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.update_extra_data_in_a_message_response import UpdateExtraDataInAMessageResponse
from sendbird_platform_sdk.model.update_extra_data_in_a_message_request import UpdateExtraDataInAMessageRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    message_id = "message_id_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_extra_data_in_a_message_request = UpdateExtraDataInAMessageRequest(
        mode="mode_example",
        sorted_metaarray=SendbirdSortedMetaarray([
            SendbirdSortedMetaarrayInner(
                key="key_example",
                value=[
                    "value_example",
                ],
            ),
        ]),
        upsert=True,
    ) # UpdateExtraDataInAMessageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update extra data in a message
        api_response = api_instance.update_extra_data_in_a_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_extra_data_in_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update extra data in a message
        api_response = api_instance.update_extra_data_in_a_message(channel_type, channel_url, message_id, api_token=api_token, update_extra_data_in_a_message_request=update_extra_data_in_a_message_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_extra_data_in_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **message_id** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_extra_data_in_a_message_request** | [**UpdateExtraDataInAMessageRequest**](UpdateExtraDataInAMessageRequest.md)|  | [optional]

### Return type

[**UpdateExtraDataInAMessageResponse**](UpdateExtraDataInAMessageResponse.md)

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

