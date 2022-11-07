# sendbird_platform_sdk.MessageApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_emoji_categories**](MessageApi.md#add_emoji_categories) | **POST** /v3/emoji_categories | Add emoji categories
[**add_emojis**](MessageApi.md#add_emojis) | **POST** /v3/emojis | Add emojis
[**add_extra_data_to_message**](MessageApi.md#add_extra_data_to_message) | **POST** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Add extra data to a message
[**add_reaction_to_a_message**](MessageApi.md#add_reaction_to_a_message) | **POST** /v3/{channel_type}/{channel_url}/messages/{message_id}/reactions | Add a reaction to a message
[**delete_emoji_by_key**](MessageApi.md#delete_emoji_by_key) | **DELETE** /v3/emojis/{emoji_key} | Delete an emoji
[**delete_emoji_category_by_id**](MessageApi.md#delete_emoji_category_by_id) | **DELETE** /v3/emoji_categories/{emoji_category_id} | Delete an emoji category
[**delete_message_by_id**](MessageApi.md#delete_message_by_id) | **DELETE** /v3/{channel_type}/{channel_url}/messages/{message_id} | Delete a message
[**enable_reactions**](MessageApi.md#enable_reactions) | **PUT** /v3/applications/settings/reactions | Enable reactions
[**gc_mark_all_messages_as_delivered**](MessageApi.md#gc_mark_all_messages_as_delivered) | **PUT** /v3/group_channels/{channel_url}/messages/mark_as_delivered | Mark all messages as delivered
[**gc_mark_all_messages_as_read**](MessageApi.md#gc_mark_all_messages_as_read) | **PUT** /v3/group_channels/{channel_url}/messages/mark_as_read | Mark all messages as read
[**gc_view_number_of_each_members_unread_messages**](MessageApi.md#gc_view_number_of_each_members_unread_messages) | **GET** /v3/group_channels/{channel_url}/messages/unread_count | View number of each member&#39;s unread messages
[**get_emoji_by_key**](MessageApi.md#get_emoji_by_key) | **GET** /v3/emojis/{emoji_key} | Get an emoji
[**get_emoji_category_by_id**](MessageApi.md#get_emoji_category_by_id) | **GET** /v3/emoji_categories/{emoji_category_id} | Get an emoji category
[**list_all_emojis_and_emoji_categories**](MessageApi.md#list_all_emojis_and_emoji_categories) | **GET** /v3/emoji_categories | List all emojis and emoji categories
[**list_announcements**](MessageApi.md#list_announcements) | **GET** /v3/announcements | List announcements
[**list_emojis**](MessageApi.md#list_emojis) | **GET** /v3/emojis | List emojis
[**list_messages**](MessageApi.md#list_messages) | **GET** /v3/{channel_type}/{channel_url}/messages | List messages
[**list_reactions_of_message**](MessageApi.md#list_reactions_of_message) | **GET** /v3/{channel_type}/{channel_url}/messages/{message_id}/reactions | List reactions of a message
[**migrate_messages_by_url**](MessageApi.md#migrate_messages_by_url) | **POST** /v3/migration/{target_channel_url} | Migrate messages
[**remove_extra_data_from_message**](MessageApi.md#remove_extra_data_from_message) | **DELETE** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Remove extra data from a message
[**remove_reaction_from_a_message**](MessageApi.md#remove_reaction_from_a_message) | **DELETE** /v3/{channel_type}/{channel_url}/messages/{message_id}/reactions | Remove a reaction from a message
[**send_message**](MessageApi.md#send_message) | **POST** /v3/{channel_type}/{channel_url}/messages | Send a message
[**translate_message_into_other_languages**](MessageApi.md#translate_message_into_other_languages) | **POST** /v3/{channel_type}/{channel_url}/messages/{message_id}/translation | Translate a message into other languages
[**update_emoji_category_url_by_id**](MessageApi.md#update_emoji_category_url_by_id) | **PUT** /v3/emoji_categories/{emoji_category_id} | Update an emoji category URL
[**update_emoji_url_by_key**](MessageApi.md#update_emoji_url_by_key) | **PUT** /v3/emojis/{emoji_key} | Update an emoji URL
[**update_extra_data_in_message**](MessageApi.md#update_extra_data_in_message) | **PUT** /v3/{channel_type}/{channel_url}/messages/{message_id}/sorted_metaarray | Update extra data in a message
[**update_message_by_id**](MessageApi.md#update_message_by_id) | **PUT** /v3/{channel_type}/{channel_url}/messages/{message_id} | Update a message
[**use_default_emojis**](MessageApi.md#use_default_emojis) | **PUT** /v3/applications/settings/use_default_emoji | Use default emojis
[**view_message_by_id**](MessageApi.md#view_message_by_id) | **GET** /v3/{channel_type}/{channel_url}/messages/{message_id} | View a message
[**view_total_number_of_messages_in_channel**](MessageApi.md#view_total_number_of_messages_in_channel) | **GET** /v3/{channel_type}/{channel_url}/messages/total_count | View total number of messages in a channel


# **add_emoji_categories**
> AddEmojiCategoriesResponse add_emoji_categories(api_token)

Add emoji categories

## Add emoji categories  Adds a list of one or more new emoji categories to the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-add-emoji-categories

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.add_emoji_categories_response import AddEmojiCategoriesResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add emoji categories
        api_response = api_instance.add_emoji_categories(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_emoji_categories: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add emoji categories
        api_response = api_instance.add_emoji_categories(api_token, body=body)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_emoji_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**AddEmojiCategoriesResponse**](AddEmojiCategoriesResponse.md)

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

# **add_emojis**
> AddEmojisResponse add_emojis(api_token)

Add emojis

## Add emojis  Adds a list of one or more new emojis to the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-add-emojis

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.add_emojis_response import AddEmojisResponse
from sendbird_platform_sdk.model.add_emojis_data import AddEmojisData
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
    api_token = "{{API_TOKEN}}" # str | 
    add_emojis_data = AddEmojisData(
        emoji_category_id=1,
        emojis=[
            {},
        ],
    ) # AddEmojisData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add emojis
        api_response = api_instance.add_emojis(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_emojis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add emojis
        api_response = api_instance.add_emojis(api_token, add_emojis_data=add_emojis_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_emojis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **add_emojis_data** | [**AddEmojisData**](AddEmojisData.md)|  | [optional]

### Return type

[**AddEmojisResponse**](AddEmojisResponse.md)

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

# **add_extra_data_to_message**
> AddExtraDataToMessageResponse add_extra_data_to_message(api_token, channel_type, channel_url, message_id)

Add extra data to a message

## Add extra data to a message  Adds one or more key-values items which store additional information for a message.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-add-extra-data-to-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.add_extra_data_to_message_response import AddExtraDataToMessageResponse
from sendbird_platform_sdk.model.add_extra_data_to_message_data import AddExtraDataToMessageData
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    add_extra_data_to_message_data = AddExtraDataToMessageData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        message_id=1,
        sorted_metaarray="sorted_metaarray_example",
    ) # AddExtraDataToMessageData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add extra data to a message
        api_response = api_instance.add_extra_data_to_message(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_extra_data_to_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add extra data to a message
        api_response = api_instance.add_extra_data_to_message(api_token, channel_type, channel_url, message_id, add_extra_data_to_message_data=add_extra_data_to_message_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_extra_data_to_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **add_extra_data_to_message_data** | [**AddExtraDataToMessageData**](AddExtraDataToMessageData.md)|  | [optional]

### Return type

[**AddExtraDataToMessageResponse**](AddExtraDataToMessageResponse.md)

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
> AddReactionToAMessageResponse add_reaction_to_a_message(api_token, channel_type, channel_url, message_id)

Add a reaction to a message

## Add a reaction to a message  Adds a specific reaction to a message.  > __Note__: Currently, this action is only available in group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-add-a-reaction-to-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.add_reaction_to_a_message_data import AddReactionToAMessageData
from sendbird_platform_sdk.model.add_reaction_to_a_message_response import AddReactionToAMessageResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
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
        api_response = api_instance.add_reaction_to_a_message(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_reaction_to_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a reaction to a message
        api_response = api_instance.add_reaction_to_a_message(api_token, channel_type, channel_url, message_id, add_reaction_to_a_message_data=add_reaction_to_a_message_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->add_reaction_to_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **add_reaction_to_a_message_data** | [**AddReactionToAMessageData**](AddReactionToAMessageData.md)|  | [optional]

### Return type

[**AddReactionToAMessageResponse**](AddReactionToAMessageResponse.md)

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

# **delete_emoji_by_key**
> delete_emoji_by_key(api_token, emoji_key)

Delete an emoji

## Delete an emoji  Deletes an emoji from the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-delete-an-emoji ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    emoji_key = "emoji_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an emoji
        api_instance.delete_emoji_by_key(api_token, emoji_key)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->delete_emoji_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **emoji_key** | **str**|  |

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

# **delete_emoji_category_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_emoji_category_by_id(api_token, emoji_category_id)

Delete an emoji category

## Delete an emoji category  Deletes an emoji category with the specified ID.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-delete-an-emoji-category ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    emoji_category_id = "emoji_category_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an emoji category
        api_response = api_instance.delete_emoji_category_by_id(api_token, emoji_category_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->delete_emoji_category_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **emoji_category_id** | **str**|  |

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

# **delete_message_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_message_by_id(api_token, channel_type, channel_url, message_id)

Delete a message

## Delete a message  Deletes a message from a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-delete-a-message ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a message
        api_response = api_instance.delete_message_by_id(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->delete_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |

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

# **enable_reactions**
> EnableReactionsResponse enable_reactions(api_token)

Enable reactions

## Enable reactions  Turn on or off reactions in a Sendbird application.  > __Note__: This action also allows reactions in UIKit.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-enable-reactions

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.enable_reactions_response import EnableReactionsResponse
from sendbird_platform_sdk.model.enable_reactions_data import EnableReactionsData
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
    api_token = "{{API_TOKEN}}" # str | 
    enable_reactions_data = EnableReactionsData(
        enabled=True,
    ) # EnableReactionsData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Enable reactions
        api_response = api_instance.enable_reactions(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->enable_reactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable reactions
        api_response = api_instance.enable_reactions(api_token, enable_reactions_data=enable_reactions_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->enable_reactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **enable_reactions_data** | [**EnableReactionsData**](EnableReactionsData.md)|  | [optional]

### Return type

[**EnableReactionsResponse**](EnableReactionsResponse.md)

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

# **gc_mark_all_messages_as_delivered**
> GcMarkAllMessagesAsDeliveredResponse gc_mark_all_messages_as_delivered(api_token, channel_url)

Mark all messages as delivered

## Mark all messages as delivered  Marks all messages in a group channel as delivered for a given user. This action is only applicable for users in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-mark-all-messages-as-delivered ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.gc_mark_all_messages_as_delivered_data import GcMarkAllMessagesAsDeliveredData
from sendbird_platform_sdk.model.gc_mark_all_messages_as_delivered_response import GcMarkAllMessagesAsDeliveredResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    gc_mark_all_messages_as_delivered_data = GcMarkAllMessagesAsDeliveredData(
        application_id="application_id_example",
        channel_url="channel_url_example",
        user_id="user_id_example",
    ) # GcMarkAllMessagesAsDeliveredData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mark all messages as delivered
        api_response = api_instance.gc_mark_all_messages_as_delivered(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->gc_mark_all_messages_as_delivered: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark all messages as delivered
        api_response = api_instance.gc_mark_all_messages_as_delivered(api_token, channel_url, gc_mark_all_messages_as_delivered_data=gc_mark_all_messages_as_delivered_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->gc_mark_all_messages_as_delivered: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **gc_mark_all_messages_as_delivered_data** | [**GcMarkAllMessagesAsDeliveredData**](GcMarkAllMessagesAsDeliveredData.md)|  | [optional]

### Return type

[**GcMarkAllMessagesAsDeliveredResponse**](GcMarkAllMessagesAsDeliveredResponse.md)

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
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} gc_mark_all_messages_as_read(api_token, channel_url)

Mark all messages as read

## Mark all messages as read  Marks all messages in a group channel as read for a given user. This action is only applicable for users in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-mark-all-messages-as-read ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.gc_mark_all_messages_as_read_data import GcMarkAllMessagesAsReadData
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    gc_mark_all_messages_as_read_data = GcMarkAllMessagesAsReadData(
        channel_url="channel_url_example",
        user_id="user_id_example",
        timestamp=1,
    ) # GcMarkAllMessagesAsReadData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Mark all messages as read
        api_response = api_instance.gc_mark_all_messages_as_read(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->gc_mark_all_messages_as_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark all messages as read
        api_response = api_instance.gc_mark_all_messages_as_read(api_token, channel_url, gc_mark_all_messages_as_read_data=gc_mark_all_messages_as_read_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->gc_mark_all_messages_as_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **gc_mark_all_messages_as_read_data** | [**GcMarkAllMessagesAsReadData**](GcMarkAllMessagesAsReadData.md)|  | [optional]

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

# **gc_view_number_of_each_members_unread_messages**
> GcViewNumberOfEachMembersUnreadMessagesResponse gc_view_number_of_each_members_unread_messages(api_token, channel_url)

View number of each member's unread messages

## View number of each member's unread messages  Retrieves the total number of each member's unread messages in a group channel. This action is only applicable for users in a group channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-view-number-of-each-member-s-unread-messages ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.gc_view_number_of_each_members_unread_messages_response import GcViewNumberOfEachMembersUnreadMessagesResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_url = "channel_url_example" # str | 
    user_ids = "user_ids_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View number of each member's unread messages
        api_response = api_instance.gc_view_number_of_each_members_unread_messages(api_token, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->gc_view_number_of_each_members_unread_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View number of each member's unread messages
        api_response = api_instance.gc_view_number_of_each_members_unread_messages(api_token, channel_url, user_ids=user_ids)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->gc_view_number_of_each_members_unread_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_url** | **str**|  |
 **user_ids** | **str**|  | [optional]

### Return type

[**GcViewNumberOfEachMembersUnreadMessagesResponse**](GcViewNumberOfEachMembersUnreadMessagesResponse.md)

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

# **get_emoji_by_key**
> SendBirdEmoji get_emoji_by_key(api_token, emoji_key)

Get an emoji

## Get an emoji  Retrieves an emoji with the specified key.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-get-an-emoji ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.send_bird_emoji import SendBirdEmoji
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
    api_token = "{{API_TOKEN}}" # str | 
    emoji_key = "emoji_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an emoji
        api_response = api_instance.get_emoji_by_key(api_token, emoji_key)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->get_emoji_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **emoji_key** | **str**|  |

### Return type

[**SendBirdEmoji**](SendBirdEmoji.md)

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

# **get_emoji_category_by_id**
> SendBirdEmojiCategory get_emoji_category_by_id(api_token, emoji_category_id)

Get an emoji category

## Get an emoji category  Retrieves an emoji category with the specified ID, including its emojis.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-get-an-emoji-category ----------------------------   `emoji_category_id`      Type: int      Description: Specifies the unique ID of the emoji category to retrieve.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.send_bird_emoji_category import SendBirdEmojiCategory
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
    api_token = "{{API_TOKEN}}" # str | 
    emoji_category_id = "emoji_category_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an emoji category
        api_response = api_instance.get_emoji_category_by_id(api_token, emoji_category_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->get_emoji_category_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **emoji_category_id** | **str**|  |

### Return type

[**SendBirdEmojiCategory**](SendBirdEmojiCategory.md)

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

# **list_all_emojis_and_emoji_categories**
> ListAllEmojisAndEmojiCategoriesResponse list_all_emojis_and_emoji_categories(api_token)

List all emojis and emoji categories

## List all emojis and emoji categories  Retrieves a list of all emoji categories registered to the application, including their emojis.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-list-all-emojis-and-emoji-categories

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.list_all_emojis_and_emoji_categories_response import ListAllEmojisAndEmojiCategoriesResponse
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
    api_token = "{{API_TOKEN}}" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List all emojis and emoji categories
        api_response = api_instance.list_all_emojis_and_emoji_categories(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_all_emojis_and_emoji_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |

### Return type

[**ListAllEmojisAndEmojiCategoriesResponse**](ListAllEmojisAndEmojiCategoriesResponse.md)

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

# **list_announcements**
> ListAnnouncementsResponse list_announcements(api_token)

List announcements

## List announcements  Retrieves a list of announcements.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-list-announcements ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.list_announcements_response import ListAnnouncementsResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    order = "order_example" # str |  (optional)
    status = "status_example" # str |  (optional)
    announcement_group = "announcement_group_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List announcements
        api_response = api_instance.list_announcements(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_announcements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List announcements
        api_response = api_instance.list_announcements(api_token, token=token, limit=limit, order=order, status=status, announcement_group=announcement_group)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_announcements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **order** | **str**|  | [optional]
 **status** | **str**|  | [optional]
 **announcement_group** | **str**|  | [optional]

### Return type

[**ListAnnouncementsResponse**](ListAnnouncementsResponse.md)

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

# **list_emojis**
> ListEmojisResponse list_emojis(api_token)

List emojis

## List emojis  Retrieves a list of all emojis registered to the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-list-emojis

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.list_emojis_response import ListEmojisResponse
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
    api_token = "{{API_TOKEN}}" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List emojis
        api_response = api_instance.list_emojis(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_emojis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |

### Return type

[**ListEmojisResponse**](ListEmojisResponse.md)

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
> ListMessagesResponse list_messages(api_token, channel_type, channel_url)

List messages

## List messages  Retrieves a list of past messages of a channel.  > This message retrieval is one of Sendbird's [premium features](https://sendbird.com/docs/chat/v3/platform-api/guides/application#-3-sendbird-s-premium-features). Contact our [sales team](https://get.sendbird.com/talk-to-sales.html) for further assistance.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-list-messages ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel to retrieve a list of past messages.

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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_ts = "message_ts_example" # str |  (optional)
    message_id = 1 # int |  (optional)
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
        api_response = api_instance.list_messages(api_token, channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List messages
        api_response = api_instance.list_messages(api_token, channel_type, channel_url, message_ts=message_ts, message_id=message_id, prev_limit=prev_limit, next_limit=next_limit, include=include, reverse=reverse, sender_id=sender_id, sender_ids=sender_ids, operator_filter=operator_filter, custom_types=custom_types, message_type=message_type, including_removed=including_removed, include_reactions=include_reactions, with_sorted_meta_array=with_sorted_meta_array, show_subchannel_messages_only=show_subchannel_messages_only, user_id=user_id, custom_type=custom_type, with_meta_array=with_meta_array)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_ts** | **str**|  | [optional]
 **message_id** | **int**|  | [optional]
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

# **list_reactions_of_message**
> ListReactionsOfMessageResponse list_reactions_of_message(api_token, channel_type, channel_url, message_id)

List reactions of a message

## List reactions of a message  Retrieves a list of reactions made to a message.  > __Note__: Currently, this action is only available in group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-list-reactions-of-a-message ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.  `message_id`      Type: long      Description: Specifies the unique ID of the message to add a reaction to.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.list_reactions_of_message_response import ListReactionsOfMessageResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    list_users = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List reactions of a message
        api_response = api_instance.list_reactions_of_message(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_reactions_of_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List reactions of a message
        api_response = api_instance.list_reactions_of_message(api_token, channel_type, channel_url, message_id, list_users=list_users)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->list_reactions_of_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **list_users** | **bool**|  | [optional]

### Return type

[**ListReactionsOfMessageResponse**](ListReactionsOfMessageResponse.md)

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

# **migrate_messages_by_url**
> migrate_messages_by_url(api_token, target_channel_url)

Migrate messages

## Migrate messages  Using our migration API, you can migrate the messages from another system into a Sendbird system's [channel](https://sendbird.com/docs/chat/v3/platform-api/guides/channel-types) which consists of users, messages, and other chat-related data.  > To turn on this feature, [contact our support team](https://dashboard.sendbird.com/settings/contact_us).  There are three things to do in advance before the migration. Follow the instructions below:  1. Register the users of your current chat solution to your Sendbird application. You can migrate the users into the Sendbird system using the [user creation API](https://sendbird.com/docs/chat/v3/platform-api/guides/user#2-create-a-user). 2. Create either an [open](https://sendbird.com/docs/chat/v3/platform-api/guides/open-channel#2-create-a-channel) or a [group](https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-create-a-channel) channel to migrate the messages of your chat solution. The Sendbird system doesn't create a channel for your migration automatically. 3. The maximum number of migrated messages per call is 100. To avoid the failure during your migration, you must adjust the number of messages to process at once via the API.  https://sendbird.com/docs/chat/v3/platform-api/guides/migration#2-migrate-messages ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    target_channel_url = "target_channel_url_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Migrate messages
        api_instance.migrate_messages_by_url(api_token, target_channel_url)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->migrate_messages_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Migrate messages
        api_instance.migrate_messages_by_url(api_token, target_channel_url, body=body)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->migrate_messages_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **target_channel_url** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **remove_extra_data_from_message**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remove_extra_data_from_message(api_token, channel_type, channel_url, message_id)

Remove extra data from a message

## Remove extra data from a message  Removes specific items from a message by their keys.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-remove-extra-data-from-a-message ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    keys = [
        "keys_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove extra data from a message
        api_response = api_instance.remove_extra_data_from_message(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->remove_extra_data_from_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove extra data from a message
        api_response = api_instance.remove_extra_data_from_message(api_token, channel_type, channel_url, message_id, keys=keys)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->remove_extra_data_from_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **keys** | **[str]**|  | [optional]

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

# **remove_reaction_from_a_message**
> RemoveReactionFromAMessageResponse remove_reaction_from_a_message(api_token, channel_type, channel_url, message_id)

Remove a reaction from a message

## Remove a reaction from a message  Removes a specific reaction from a message.  > __Note__: Currently, this action is only available in group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-remove-a-reaction-from-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.remove_reaction_from_a_message_response import RemoveReactionFromAMessageResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    user_id = "user_id_example" # str |  (optional)
    reaction = "reaction_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a reaction from a message
        api_response = api_instance.remove_reaction_from_a_message(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->remove_reaction_from_a_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a reaction from a message
        api_response = api_instance.remove_reaction_from_a_message(api_token, channel_type, channel_url, message_id, user_id=user_id, reaction=reaction)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->remove_reaction_from_a_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **user_id** | **str**|  | [optional]
 **reaction** | **str**|  | [optional]

### Return type

[**RemoveReactionFromAMessageResponse**](RemoveReactionFromAMessageResponse.md)

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
> SendBirdMessageResponse send_message(api_token, channel_type, channel_url)

Send a message

## Send a message  Sends a message to a channel. You can send a text message, a file message, and an admin message.  >__Note__: With Sendbird Chat SDKs and the platform API, any type of files in messages can be uploaded to Sendbird server.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-send-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.send_bird_message_response import SendBirdMessageResponse
from sendbird_platform_sdk.model.send_message_data import SendMessageData
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
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
        url="url_example",
        file="file_example",
        file_name="file_name_example",
        file_size=3.14,
        file_type="file_type_example",
        thumbnails=[
            "thumbnails_example",
        ],
        thumbnail1="thumbnail1_example",
        thumbnail2="thumbnail2_example",
        thumbnail3="thumbnail3_example",
    ) # SendMessageData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a message
        api_response = api_instance.send_message(api_token, channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->send_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a message
        api_response = api_instance.send_message(api_token, channel_type, channel_url, send_message_data=send_message_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->send_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
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
> SendBirdMessageResponse translate_message_into_other_languages(api_token, channel_type, channel_url, message_id)

Translate a message into other languages

## Translate a message into other languages  Translates a message into specific languages. Only text messages of which type is MESG can be translated into other languages.  > __Note__: Message translation is powered by [Google Cloud Translation API recognition engine](https://cloud.google.com/translate/). Find language codes supported by the engine in the [Miscellaneous](https://sendbird.com/docs/chat/v3/platform-api/guides/Miscellaneous) page or visit the [Language Support](https://cloud.google.com/translate/docs/languages) for Google Cloud Translation.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-translate-a-message-into-other-languages ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.send_bird_message_response import SendBirdMessageResponse
from sendbird_platform_sdk.model.translate_message_into_other_languages_data import TranslateMessageIntoOtherLanguagesData
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    translate_message_into_other_languages_data = TranslateMessageIntoOtherLanguagesData(
        target_langs=[
            "target_langs_example",
        ],
    ) # TranslateMessageIntoOtherLanguagesData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Translate a message into other languages
        api_response = api_instance.translate_message_into_other_languages(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->translate_message_into_other_languages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Translate a message into other languages
        api_response = api_instance.translate_message_into_other_languages(api_token, channel_type, channel_url, message_id, translate_message_into_other_languages_data=translate_message_into_other_languages_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->translate_message_into_other_languages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **translate_message_into_other_languages_data** | [**TranslateMessageIntoOtherLanguagesData**](TranslateMessageIntoOtherLanguagesData.md)|  | [optional]

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

# **update_emoji_category_url_by_id**
> SendBirdEmojiCategory update_emoji_category_url_by_id(api_token, emoji_category_id)

Update an emoji category URL

## Update an emoji category URL  Updates the URL of an emoji category with the specified ID.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-update-an-emoji-category-url ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.update_emoji_category_url_by_id_data import UpdateEmojiCategoryUrlByIdData
from sendbird_platform_sdk.model.send_bird_emoji_category import SendBirdEmojiCategory
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
    api_token = "{{API_TOKEN}}" # str | 
    emoji_category_id = "emoji_category_id_example" # str | 
    update_emoji_category_url_by_id_data = UpdateEmojiCategoryUrlByIdData(
        emoji_category_id=1,
        url="url_example",
    ) # UpdateEmojiCategoryUrlByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an emoji category URL
        api_response = api_instance.update_emoji_category_url_by_id(api_token, emoji_category_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_emoji_category_url_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an emoji category URL
        api_response = api_instance.update_emoji_category_url_by_id(api_token, emoji_category_id, update_emoji_category_url_by_id_data=update_emoji_category_url_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_emoji_category_url_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **emoji_category_id** | **str**|  |
 **update_emoji_category_url_by_id_data** | [**UpdateEmojiCategoryUrlByIdData**](UpdateEmojiCategoryUrlByIdData.md)|  | [optional]

### Return type

[**SendBirdEmojiCategory**](SendBirdEmojiCategory.md)

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

# **update_emoji_url_by_key**
> SendBirdEmoji update_emoji_url_by_key(api_token, emoji_key)

Update an emoji URL

## Update an emoji URL  Updates the image URL of an emoji with the specified key.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-update-an-emoji-url ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.send_bird_emoji import SendBirdEmoji
from sendbird_platform_sdk.model.update_emoji_url_by_key_data import UpdateEmojiUrlByKeyData
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
    api_token = "{{API_TOKEN}}" # str | 
    emoji_key = "emoji_key_example" # str | 
    update_emoji_url_by_key_data = UpdateEmojiUrlByKeyData(
        emoji_key="emoji_key_example",
        url="url_example",
    ) # UpdateEmojiUrlByKeyData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an emoji URL
        api_response = api_instance.update_emoji_url_by_key(api_token, emoji_key)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_emoji_url_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an emoji URL
        api_response = api_instance.update_emoji_url_by_key(api_token, emoji_key, update_emoji_url_by_key_data=update_emoji_url_by_key_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_emoji_url_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **emoji_key** | **str**|  |
 **update_emoji_url_by_key_data** | [**UpdateEmojiUrlByKeyData**](UpdateEmojiUrlByKeyData.md)|  | [optional]

### Return type

[**SendBirdEmoji**](SendBirdEmoji.md)

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
> UpdateExtraDataInMessageResponse update_extra_data_in_message(api_token, channel_type, channel_url, message_id)

Update extra data in a message

## Update extra data in a message  Updates the values of specific items by their keys.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-update-extra-data-in-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.update_extra_data_in_message_response import UpdateExtraDataInMessageResponse
from sendbird_platform_sdk.model.update_extra_data_in_message_data import UpdateExtraDataInMessageData
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    update_extra_data_in_message_data = UpdateExtraDataInMessageData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        message_id=1,
        sorted_metaarray="sorted_metaarray_example",
        mode="mode_example",
        upsert=True,
    ) # UpdateExtraDataInMessageData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update extra data in a message
        api_response = api_instance.update_extra_data_in_message(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_extra_data_in_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update extra data in a message
        api_response = api_instance.update_extra_data_in_message(api_token, channel_type, channel_url, message_id, update_extra_data_in_message_data=update_extra_data_in_message_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_extra_data_in_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **update_extra_data_in_message_data** | [**UpdateExtraDataInMessageData**](UpdateExtraDataInMessageData.md)|  | [optional]

### Return type

[**UpdateExtraDataInMessageResponse**](UpdateExtraDataInMessageResponse.md)

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
> SendBirdMessageResponse update_message_by_id(api_token, channel_type, channel_url, message_id)

Update a message

## Update a message  Updates information on a message in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-update-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.update_message_by_id_data import UpdateMessageByIdData
from sendbird_platform_sdk.model.send_bird_message_response import SendBirdMessageResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
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
            "mentioned_user_ids_example",
        ],
    ) # UpdateMessageByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a message
        api_response = api_instance.update_message_by_id(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_message_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a message
        api_response = api_instance.update_message_by_id(api_token, channel_type, channel_url, message_id, update_message_by_id_data=update_message_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->update_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
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

# **use_default_emojis**
> UseDefaultEmojisResponse use_default_emojis(api_token)

Use default emojis

## Use default emojis  Determines whether to use the 7 default emojis initially provided.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-use-default-emojis

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.use_default_emojis_data import UseDefaultEmojisData
from sendbird_platform_sdk.model.use_default_emojis_response import UseDefaultEmojisResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    use_default_emojis_data = UseDefaultEmojisData(
        use_default_emoji=True,
    ) # UseDefaultEmojisData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Use default emojis
        api_response = api_instance.use_default_emojis(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->use_default_emojis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Use default emojis
        api_response = api_instance.use_default_emojis(api_token, use_default_emojis_data=use_default_emojis_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->use_default_emojis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **use_default_emojis_data** | [**UseDefaultEmojisData**](UseDefaultEmojisData.md)|  | [optional]

### Return type

[**UseDefaultEmojisResponse**](UseDefaultEmojisResponse.md)

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
> SendBirdMessageResponse view_message_by_id(api_token, channel_type, channel_url, message_id)

View a message

## View a message  Retrieves information on a message.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-view-a-message ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.  `message_id`      Type: long      Description: Specifies the unique ID of the message to retrieve.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.send_bird_message_response import SendBirdMessageResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    with_sorted_meta_array = True # bool |  (optional)
    with_meta_array = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a message
        api_response = api_instance.view_message_by_id(api_token, channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->view_message_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a message
        api_response = api_instance.view_message_by_id(api_token, channel_type, channel_url, message_id, with_sorted_meta_array=with_sorted_meta_array, with_meta_array=with_meta_array)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->view_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
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
> ViewTotalNumberOfMessagesInChannelResponse view_total_number_of_messages_in_channel(api_token, channel_type, channel_url)

View total number of messages in a channel

## View total number of messages in a channel  Retrieves the total number of messages in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/messages#2-view-total-number-of-messages-in-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import message_api
from sendbird_platform_sdk.model.view_total_number_of_messages_in_channel_response import ViewTotalNumberOfMessagesInChannelResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View total number of messages in a channel
        api_response = api_instance.view_total_number_of_messages_in_channel(api_token, channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MessageApi->view_total_number_of_messages_in_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |

### Return type

[**ViewTotalNumberOfMessagesInChannelResponse**](ViewTotalNumberOfMessagesInChannelResponse.md)

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

