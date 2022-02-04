# sendbird-platform-sdk.MessagesApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_extra_data_to_message**](MessagesApi.md#add_extra_data_to_message) | **POST** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Add extra data to a message
[**add_reaction_to_a_message**](MessagesApi.md#add_reaction_to_a_message) | **POST** /v3/{channel_type}/{channel_url}/messages/{message_id}/reactions | Add a reaction to a message
[**delete_message_by_id**](MessagesApi.md#delete_message_by_id) | **DELETE** /v3/{channel_type}/{channel_url}/messages/{message_id} | Delete a message
[**gc_mark_all_messages_as_delivered**](MessagesApi.md#gc_mark_all_messages_as_delivered) | **PUT** /v3/group_channels/{channel_url}/messages/mark_as_delivered | Mark all messages as delivered
[**gc_mark_all_messages_as_read**](MessagesApi.md#gc_mark_all_messages_as_read) | **PUT** /v3/group_channels/{channel_url}/messages/mark_as_read | Mark all messages as read
[**gc_view_number_of_each_members_unread_messages**](MessagesApi.md#gc_view_number_of_each_members_unread_messages) | **GET** /v3/group_channels/{channel_url}/messages/unread_count | View number of each member&#39;s unread messages
[**list_messages**](MessagesApi.md#list_messages) | **GET** /v3/{channel_type}/{channel_url}/messages | List messages
[**list_reactions_of_message**](MessagesApi.md#list_reactions_of_message) | **GET** /v3/{channel_type}/{channel_url}/messages/{message_id}/reactions | List reactions of a message
[**remove_extra_data_from_message**](MessagesApi.md#remove_extra_data_from_message) | **DELETE** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Remove extra data from a message
[**remove_reaction_from_a_message**](MessagesApi.md#remove_reaction_from_a_message) | **DELETE** /v3/{channel_type}/{channel_url}/messages/{message_id}/reactions | Remove a reaction from a message
[**send_message**](MessagesApi.md#send_message) | **POST** /v3/{channel_type}/{channel_url}/messages | Send a message
[**translate_message_into_other_languages**](MessagesApi.md#translate_message_into_other_languages) | **POST** /v3/{channel_type}/{channel_url}/messages/{message_id}/translation | Translate a message into other languages
[**update_extra_data_in_message**](MessagesApi.md#update_extra_data_in_message) | **PUT** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Update extra data in a message
[**update_message_by_id**](MessagesApi.md#update_message_by_id) | **PUT** /v3/{channel_type}/{channel_url}/messages/{message_id} | Update a message
[**view_message_by_id**](MessagesApi.md#view_message_by_id) | **GET** /v3/{channel_type}/{channel_url}/messages/{message_id} | View a message
[**view_total_number_of_messages_in_channel**](MessagesApi.md#view_total_number_of_messages_in_channel) | **GET** /v3/{channel_type}/{channel_url}/messages/total_count | View total number of messages in a channel


# **add_extra_data_to_message**
> InlineResponse20054 add_extra_data_to_message(channel_type, channel_url, message_id)

Add extra data to a message

## Add extra data to a message  Adds one or more key-values items which store additional information for a message.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-add-extra-data-to-a-message ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.add_extra_data_to_message_data import AddExtraDataToMessageData
from sendbird-platform-sdk.model.inline_response20054 import InlineResponse20054
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_extra_data_to_message_data = AddExtraDataToMessageData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        message_id=1,
        sorted_metaarray="sorted_metaarray_example",
        metaarray="metaarray_example",
    ) # AddExtraDataToMessageData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add extra data to a message
        api_response = api_instance.add_extra_data_to_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->add_extra_data_to_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add extra data to a message
        api_response = api_instance.add_extra_data_to_message(channel_type, channel_url, message_id, api_token=api_token, add_extra_data_to_message_data=add_extra_data_to_message_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->add_extra_data_to_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **add_extra_data_to_message_data** | [**AddExtraDataToMessageData**](AddExtraDataToMessageData.md)|  | [optional]

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

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

# **add_reaction_to_a_message**
> InlineResponse20053 add_reaction_to_a_message(channel_type, channel_url, message_id)

Add a reaction to a message

## Add a reaction to a message  Adds a specific reaction to a message.  > __Note__: Currently, this action is only available in group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-add-a-reaction-to-a-message ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.inline_response20053 import InlineResponse20053
from sendbird-platform-sdk.model.add_reaction_to_a_message_data import AddReactionToAMessageData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_reaction_to_a_message_data = AddReactionToAMessageData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        message_id=1,
        user_id="user_id_example",
        reaction="reaction_example",
    ) # AddReactionToAMessageData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a reaction to a message
        api_response = api_instance.add_reaction_to_a_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->add_reaction_to_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a reaction to a message
        api_response = api_instance.add_reaction_to_a_message(channel_type, channel_url, message_id, api_token=api_token, add_reaction_to_a_message_data=add_reaction_to_a_message_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->add_reaction_to_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **add_reaction_to_a_message_data** | [**AddReactionToAMessageData**](AddReactionToAMessageData.md)|  | [optional]

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

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

# **delete_message_by_id**
> delete_message_by_id(channel_type, channel_url, message_id)

Delete a message

## Delete a message  Deletes a message from a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-delete-a-message ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a message
        api_instance.delete_message_by_id(channel_type, channel_url, message_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->delete_message_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a message
        api_instance.delete_message_by_id(channel_type, channel_url, message_id, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->delete_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
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

# **gc_mark_all_messages_as_delivered**
> InlineResponse20050 gc_mark_all_messages_as_delivered(channel_url)

Mark all messages as delivered

## Mark all messages as delivered  Marks all messages in a group channel as delivered for a given user. This action is only applicable for users in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-mark-all-messages-as-delivered ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.gc_mark_all_messages_as_delivered_data import GcMarkAllMessagesAsDeliveredData
from sendbird-platform-sdk.model.inline_response20050 import InlineResponse20050
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_mark_all_messages_as_delivered_data = GcMarkAllMessagesAsDeliveredData(
        application_id="application_id_example",
        channel_url="channel_url_example",
        user_id="user_id_example",
    ) # GcMarkAllMessagesAsDeliveredData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mark all messages as delivered
        api_response = api_instance.gc_mark_all_messages_as_delivered(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->gc_mark_all_messages_as_delivered: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark all messages as delivered
        api_response = api_instance.gc_mark_all_messages_as_delivered(channel_url, api_token=api_token, gc_mark_all_messages_as_delivered_data=gc_mark_all_messages_as_delivered_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->gc_mark_all_messages_as_delivered: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_mark_all_messages_as_delivered_data** | [**GcMarkAllMessagesAsDeliveredData**](GcMarkAllMessagesAsDeliveredData.md)|  | [optional]

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

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

# **gc_mark_all_messages_as_read**
> gc_mark_all_messages_as_read(channel_url)

Mark all messages as read

## Mark all messages as read  Marks all messages in a group channel as read for a given user. This action is only applicable for users in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-mark-all-messages-as-read ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.gc_mark_all_messages_as_read_data import GcMarkAllMessagesAsReadData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    gc_mark_all_messages_as_read_data = GcMarkAllMessagesAsReadData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        timestamp=1,
    ) # GcMarkAllMessagesAsReadData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mark all messages as read
        api_instance.gc_mark_all_messages_as_read(channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->gc_mark_all_messages_as_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark all messages as read
        api_instance.gc_mark_all_messages_as_read(channel_url, api_token=api_token, gc_mark_all_messages_as_read_data=gc_mark_all_messages_as_read_data)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->gc_mark_all_messages_as_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **gc_mark_all_messages_as_read_data** | [**GcMarkAllMessagesAsReadData**](GcMarkAllMessagesAsReadData.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gc_view_number_of_each_members_unread_messages**
> InlineResponse20049 gc_view_number_of_each_members_unread_messages(channel_url)

View number of each member's unread messages

## View number of each member's unread messages  Retrieves the total number of each member's unread messages in a group channel. This action is only applicable for users in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-view-number-of-each-member-s-unread-messages ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.inline_response20049 import InlineResponse20049
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    user_ids = "user_ids_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View number of each member's unread messages
        api_response = api_instance.gc_view_number_of_each_members_unread_messages(channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->gc_view_number_of_each_members_unread_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of each member's unread messages
        api_response = api_instance.gc_view_number_of_each_members_unread_messages(channel_url, api_token=api_token, user_ids=user_ids)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->gc_view_number_of_each_members_unread_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **user_ids** | **str**|  | [optional]

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

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
> InlineResponse20047 list_messages(channel_type, channel_url, message_ts, message_id)

List messages

## List messages  Retrieves a list of past messages of a channel.  > This message retrieval is one of Sendbird's [premium features](https://sendbird.com/docs/chat/v3/platform-api/guides/application#-3-sendbird-s-premium-features). Contact our [sales team](https://get.sendbird.com/talk-to-sales.html) for further assistance.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-list-messages ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of past messages.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.inline_response20047 import InlineResponse20047
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_ts = 1 # int | 
    message_id = 1 # int | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    prev_limit = 1 # int |  (optional)
    next_limit = 1 # int |  (optional)
    include = True # bool |  (optional)
    reverse = True # bool |  (optional)
    sender_id = "sender_id_example" # str |  (optional)
    sender_ids = "sender_ids_example" # str |  (optional)
    operator_filter = "operator_filter_example" # str |  (optional)
    custom_types = "custom_types_example" # str |  (optional)
    message_type = "message_type_example" # str |  (optional)
    including_removed = True # bool |  (optional)
    include_reactions = True # bool |  (optional)
    with_sorted_meta_array = True # bool |  (optional)
    show_subchannel_messages_only = True # bool |  (optional)
    user_id = "user_id_example" # str |  (optional)
    custom_type = "custom_type_example" # str |  (optional)
    with_meta_array = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List messages
        api_response = api_instance.list_messages(channel_type, channel_url, message_ts, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List messages
        api_response = api_instance.list_messages(channel_type, channel_url, message_ts, message_id, api_token=api_token, prev_limit=prev_limit, next_limit=next_limit, include=include, reverse=reverse, sender_id=sender_id, sender_ids=sender_ids, operator_filter=operator_filter, custom_types=custom_types, message_type=message_type, including_removed=including_removed, include_reactions=include_reactions, with_sorted_meta_array=with_sorted_meta_array, show_subchannel_messages_only=show_subchannel_messages_only, user_id=user_id, custom_type=custom_type, with_meta_array=with_meta_array)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_ts** | **int**|  |
 **message_id** | **int**|  |
 **api_token** | **str**|  | [optional]
 **prev_limit** | **int**|  | [optional]
 **next_limit** | **int**|  | [optional]
 **include** | **bool**|  | [optional]
 **reverse** | **bool**|  | [optional]
 **sender_id** | **str**|  | [optional]
 **sender_ids** | **str**|  | [optional]
 **operator_filter** | **str**|  | [optional]
 **custom_types** | **str**|  | [optional]
 **message_type** | **str**|  | [optional]
 **including_removed** | **bool**|  | [optional]
 **include_reactions** | **bool**|  | [optional]
 **with_sorted_meta_array** | **bool**|  | [optional]
 **show_subchannel_messages_only** | **bool**|  | [optional]
 **user_id** | **str**|  | [optional]
 **custom_type** | **str**|  | [optional]
 **with_meta_array** | **bool**|  | [optional]

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

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

# **list_reactions_of_message**
> InlineResponse20052 list_reactions_of_message(channel_type, channel_url, message_id)

List reactions of a message

## List reactions of a message  Retrieves a list of reactions made to a message.  > __Note__: Currently, this action is only available in group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-list-reactions-of-a-message ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.  `message_id`      Type: long      Description: Specifies the unique ID of the message to add a reaction to.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.inline_response20052 import InlineResponse20052
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    list_users = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List reactions of a message
        api_response = api_instance.list_reactions_of_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->list_reactions_of_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List reactions of a message
        api_response = api_instance.list_reactions_of_message(channel_type, channel_url, message_id, api_token=api_token, list_users=list_users)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->list_reactions_of_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **list_users** | **bool**|  | [optional]

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

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

# **remove_extra_data_from_message**
> remove_extra_data_from_message(channel_type, channel_url, message_id)

Remove extra data from a message

## Remove extra data from a message  Removes specific items from a message by their keys.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-remove-extra-data-from-a-message ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    keys = [
        "keys_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove extra data from a message
        api_instance.remove_extra_data_from_message(channel_type, channel_url, message_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->remove_extra_data_from_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove extra data from a message
        api_instance.remove_extra_data_from_message(channel_type, channel_url, message_id, api_token=api_token, keys=keys)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->remove_extra_data_from_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **keys** | **[str]**|  | [optional]

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

# **remove_reaction_from_a_message**
> InlineResponse20053 remove_reaction_from_a_message(channel_type, channel_url, message_id)

Remove a reaction from a message

## Remove a reaction from a message  Removes a specific reaction from a message.  > __Note__: Currently, this action is only available in group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-remove-a-reaction-from-a-message ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.inline_response20053 import InlineResponse20053
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    user_id = "user_id_example" # str |  (optional)
    reaction = "reaction_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a reaction from a message
        api_response = api_instance.remove_reaction_from_a_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->remove_reaction_from_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a reaction from a message
        api_response = api_instance.remove_reaction_from_a_message(channel_type, channel_url, message_id, api_token=api_token, user_id=user_id, reaction=reaction)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->remove_reaction_from_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **user_id** | **str**|  | [optional]
 **reaction** | **str**|  | [optional]

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

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

# **send_message**
> SendBirdMessageResponse send_message(channel_type, channel_url)

Send a message

## Send a message  Sends a message to a channel. You can send a text message, a file message, and an admin message.  >__Note__: With Sendbird Chat SDKs and the platform API, any type of files in messages can be uploaded to Sendbird server.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-send-a-message ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.send_bird_message_response import SendBirdMessageResponse
from sendbird-platform-sdk.model.send_message_data import SendMessageData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    send_message_data = SendMessageData(
        user_id="user_id_example",
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        message_type="message_type_example",
        message="message_example",
        custom_type="custom_type_example",
        data="data_example",
        send_push=True,
        mention_type="mention_type_example",
        mentioned_user_ids=[
            "mentioned_user_ids_example",
        ],
        is_silent=True,
        sorted_metaarray="sorted_metaarray_example",
        created_at=1,
        dedup_id="dedup_id_example",
        apns_bundle_id="apns_bundle_id_example",
        sound="sound_example",
        volume=3.14,
    ) # SendMessageData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a message
        api_response = api_instance.send_message(channel_type, channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->send_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a message
        api_response = api_instance.send_message(channel_type, channel_url, api_token=api_token, send_message_data=send_message_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->send_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **send_message_data** | [**SendMessageData**](SendMessageData.md)|  | [optional]

### Return type

[**SendBirdMessageResponse**](SendBirdMessageResponse.md)

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

# **translate_message_into_other_languages**
> SendBirdMessageResponse translate_message_into_other_languages(channel_type, channel_url, message_id)

Translate a message into other languages

## Translate a message into other languages  Translates a message into specific languages. Only text messages of which type is MESG can be translated into other languages.  > __Note__: Message translation is powered by [Google Cloud Translation API recognition engine](https://cloud.google.com/translate/). Find language codes supported by the engine in the [Miscellaneous](https://sendbird.com/docs/chat/v3/platform-api/guides/Miscellaneous) page or visit the [Language Support](https://cloud.google.com/translate/docs/languages) for Google Cloud Translation.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-translate-a-message-into-other-languages ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.send_bird_message_response import SendBirdMessageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Translate a message into other languages
        api_response = api_instance.translate_message_into_other_languages(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->translate_message_into_other_languages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Translate a message into other languages
        api_response = api_instance.translate_message_into_other_languages(channel_type, channel_url, message_id, api_token=api_token, body=body)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->translate_message_into_other_languages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**SendBirdMessageResponse**](SendBirdMessageResponse.md)

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

# **update_extra_data_in_message**
> InlineResponse20054 update_extra_data_in_message(channel_type, channel_url, message_id)

Update extra data in a message

## Update extra data in a message  Updates the values of specific items by their keys.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-update-extra-data-in-a-message ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.inline_response20054 import InlineResponse20054
from sendbird-platform-sdk.model.update_extra_data_in_message_data import UpdateExtraDataInMessageData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_extra_data_in_message_data = UpdateExtraDataInMessageData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        message_id=1,
        sorted_metaarray="sorted_metaarray_example",
        mode="mode_example",
        upsert=True,
        metaarray="metaarray_example",
    ) # UpdateExtraDataInMessageData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update extra data in a message
        api_response = api_instance.update_extra_data_in_message(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->update_extra_data_in_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update extra data in a message
        api_response = api_instance.update_extra_data_in_message(channel_type, channel_url, message_id, api_token=api_token, update_extra_data_in_message_data=update_extra_data_in_message_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->update_extra_data_in_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_extra_data_in_message_data** | [**UpdateExtraDataInMessageData**](UpdateExtraDataInMessageData.md)|  | [optional]

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

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

# **update_message_by_id**
> SendBirdMessageResponse update_message_by_id(channel_type, channel_url, message_id)

Update a message

## Update a message  Updates information on a message in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-update-a-message ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.send_bird_message_response import SendBirdMessageResponse
from sendbird-platform-sdk.model.update_message_by_id_data import UpdateMessageByIdData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_message_by_id_data = UpdateMessageByIdData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        message_id=1,
        message_type="message_type_example",
        message="message_example",
        custom_type="custom_type_example",
        data="data_example",
        mention_type="mention_type_example",
        mentioned_user_ids=[
            1,
        ],
    ) # UpdateMessageByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a message
        api_response = api_instance.update_message_by_id(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->update_message_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a message
        api_response = api_instance.update_message_by_id(channel_type, channel_url, message_id, api_token=api_token, update_message_by_id_data=update_message_by_id_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->update_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_message_by_id_data** | [**UpdateMessageByIdData**](UpdateMessageByIdData.md)|  | [optional]

### Return type

[**SendBirdMessageResponse**](SendBirdMessageResponse.md)

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

# **view_message_by_id**
> SendBirdMessageResponse view_message_by_id(channel_type, channel_url, message_id)

View a message

## View a message  Retrieves information on a message.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-view-a-message ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.  `message_id`      Type: long      Description: Specifies the unique ID of the message to retrieve.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.send_bird_message_response import SendBirdMessageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    with_sorted_meta_array = True # bool |  (optional)
    with_meta_array = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a message
        api_response = api_instance.view_message_by_id(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->view_message_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a message
        api_response = api_instance.view_message_by_id(channel_type, channel_url, message_id, api_token=api_token, with_sorted_meta_array=with_sorted_meta_array, with_meta_array=with_meta_array)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->view_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **with_sorted_meta_array** | **bool**|  | [optional]
 **with_meta_array** | **bool**|  | [optional]

### Return type

[**SendBirdMessageResponse**](SendBirdMessageResponse.md)

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

# **view_total_number_of_messages_in_channel**
> InlineResponse20048 view_total_number_of_messages_in_channel(channel_type, channel_url)

View total number of messages in a channel

## View total number of messages in a channel  Retrieves the total number of messages in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-view-total-number-of-messages-in-a-channel ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import messages_api
from sendbird-platform-sdk.model.inline_response20048 import InlineResponse20048
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View total number of messages in a channel
        api_response = api_instance.view_total_number_of_messages_in_channel(channel_type, channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->view_total_number_of_messages_in_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View total number of messages in a channel
        api_response = api_instance.view_total_number_of_messages_in_channel(channel_type, channel_url, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling MessagesApi->view_total_number_of_messages_in_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

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

