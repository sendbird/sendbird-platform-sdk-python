# sendbird-platform-sdk.EmojisApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_emoji_categories**](EmojisApi.md#add_emoji_categories) | **POST** /v3/emoji_categories | Add emoji categories
[**add_emojis**](EmojisApi.md#add_emojis) | **POST** /v3/emojis | Add emojis
[**delete_emoji_by_key**](EmojisApi.md#delete_emoji_by_key) | **DELETE** /v3/emojis/{emoji_key} | Delete an emoji
[**delete_emoji_category_by_id**](EmojisApi.md#delete_emoji_category_by_id) | **DELETE** /v3/emoji_categories/{emoji_category_id} | Delete an emoji category
[**enable_reactions**](EmojisApi.md#enable_reactions) | **PUT** /v3/applications/settings/reactions | Enable reactions
[**get_emoji_by_key**](EmojisApi.md#get_emoji_by_key) | **GET** /v3/emojis/{emoji_key} | Get an emoji
[**get_emoji_category_by_id**](EmojisApi.md#get_emoji_category_by_id) | **GET** /v3/emoji_categories/{emoji_category_id} | Get an emoji category
[**list_all_emojis_and_emoji_categories**](EmojisApi.md#list_all_emojis_and_emoji_categories) | **GET** /v3/emoji_categories | List all emojis and emoji categories
[**list_emojis**](EmojisApi.md#list_emojis) | **GET** /v3/emojis | List emojis
[**update_emoji_category_url_by_id**](EmojisApi.md#update_emoji_category_url_by_id) | **PUT** /v3/emoji_categories/{emoji_category_id} | Update an emoji category URL
[**update_emoji_url_by_key**](EmojisApi.md#update_emoji_url_by_key) | **PUT** /v3/emojis/{emoji_key} | Update an emoji URL
[**use_default_emojis**](EmojisApi.md#use_default_emojis) | **PUT** /v3/applications/settings/use_default_emoji | Use default emojis


# **add_emoji_categories**
> InlineResponse20057 add_emoji_categories()

Add emoji categories

## Add emoji categories  Adds a list of one or more new emoji categories to the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-add-emoji-categories

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.inline_response20057 import InlineResponse20057
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add emoji categories
        api_response = api_instance.add_emoji_categories(api_token=api_token, body=body)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->add_emoji_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

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
> InlineResponse20059 add_emojis()

Add emojis

## Add emojis  Adds a list of one or more new emojis to the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-add-emojis

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.inline_response20059 import InlineResponse20059
from sendbird-platform-sdk.model.add_emojis_data import AddEmojisData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    add_emojis_data = AddEmojisData(
        emoji_category_id=1,
        emojis=[
            "emojis_example",
        ],
        emoji_key="emoji_key_example",
        emoji_url="emoji_url_example",
    ) # AddEmojisData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add emojis
        api_response = api_instance.add_emojis(api_token=api_token, add_emojis_data=add_emojis_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->add_emojis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **add_emojis_data** | [**AddEmojisData**](AddEmojisData.md)|  | [optional]

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

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
> delete_emoji_by_key(emoji_key)

Delete an emoji

## Delete an emoji  Deletes an emoji from the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-delete-an-emoji ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    emoji_key = "emoji_key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete an emoji
        api_instance.delete_emoji_by_key(emoji_key)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->delete_emoji_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete an emoji
        api_instance.delete_emoji_by_key(emoji_key, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->delete_emoji_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emoji_key** | **str**|  |
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

# **delete_emoji_category_by_id**
> delete_emoji_category_by_id(emoji_category_id)

Delete an emoji category

## Delete an emoji category  Deletes an emoji category with the specified ID.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-delete-an-emoji-category ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    emoji_category_id = "emoji_category_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete an emoji category
        api_instance.delete_emoji_category_by_id(emoji_category_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->delete_emoji_category_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete an emoji category
        api_instance.delete_emoji_category_by_id(emoji_category_id, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->delete_emoji_category_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emoji_category_id** | **str**|  |
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

# **enable_reactions**
> InlineResponse20051 enable_reactions()

Enable reactions

## Enable reactions  Turn on or off reactions in a Sendbird application.  > __Note__: This action also allows reactions in UIKit.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-enable-reactions

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.inline_response20051 import InlineResponse20051
from sendbird-platform-sdk.model.enable_reactions_data import EnableReactionsData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    enable_reactions_data = EnableReactionsData(
        enabled=True,
    ) # EnableReactionsData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable reactions
        api_response = api_instance.enable_reactions(api_token=api_token, enable_reactions_data=enable_reactions_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->enable_reactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **enable_reactions_data** | [**EnableReactionsData**](EnableReactionsData.md)|  | [optional]

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

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

# **get_emoji_by_key**
> SendBirdEmoji get_emoji_by_key(emoji_key)

Get an emoji

## Get an emoji  Retrieves an emoji with the specified key.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-get-an-emoji ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.send_bird_emoji import SendBirdEmoji
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    emoji_key = "emoji_key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an emoji
        api_response = api_instance.get_emoji_by_key(emoji_key)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->get_emoji_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an emoji
        api_response = api_instance.get_emoji_by_key(emoji_key, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->get_emoji_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emoji_key** | **str**|  |
 **api_token** | **str**|  | [optional]

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
> SendBirdEmojiCategory get_emoji_category_by_id(emoji_category_id)

Get an emoji category

## Get an emoji category  Retrieves an emoji category with the specified ID, including its emojis.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-get-an-emoji-category ----------------------------   `emoji_category_id`      Type: int      Description: Specifies the unique ID of the emoji category to retrieve.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.send_bird_emoji_category import SendBirdEmojiCategory
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    emoji_category_id = "emoji_category_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an emoji category
        api_response = api_instance.get_emoji_category_by_id(emoji_category_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->get_emoji_category_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an emoji category
        api_response = api_instance.get_emoji_category_by_id(emoji_category_id, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->get_emoji_category_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emoji_category_id** | **str**|  |
 **api_token** | **str**|  | [optional]

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
> InlineResponse20056 list_all_emojis_and_emoji_categories()

List all emojis and emoji categories

## List all emojis and emoji categories  Retrieves a list of all emoji categories registered to the application, including their emojis.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-list-all-emojis-and-emoji-categories

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.inline_response20056 import InlineResponse20056
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all emojis and emoji categories
        api_response = api_instance.list_all_emojis_and_emoji_categories(api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->list_all_emojis_and_emoji_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

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
> InlineResponse20058 list_emojis()

List emojis

## List emojis  Retrieves a list of all emojis registered to the application.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-list-emojis

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.inline_response20058 import InlineResponse20058
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List emojis
        api_response = api_instance.list_emojis(api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->list_emojis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

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

# **update_emoji_category_url_by_id**
> SendBirdEmojiCategory update_emoji_category_url_by_id(emoji_category_id)

Update an emoji category URL

## Update an emoji category URL  Updates the URL of an emoji category with the specified ID.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-update-an-emoji-category-url ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.update_emoji_category_url_by_id_data import UpdateEmojiCategoryUrlByIdData
from sendbird-platform-sdk.model.send_bird_emoji_category import SendBirdEmojiCategory
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    emoji_category_id = "emoji_category_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_emoji_category_url_by_id_data = UpdateEmojiCategoryUrlByIdData(
        emoji_category_id=1,
        url="url_example",
    ) # UpdateEmojiCategoryUrlByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an emoji category URL
        api_response = api_instance.update_emoji_category_url_by_id(emoji_category_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->update_emoji_category_url_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an emoji category URL
        api_response = api_instance.update_emoji_category_url_by_id(emoji_category_id, api_token=api_token, update_emoji_category_url_by_id_data=update_emoji_category_url_by_id_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->update_emoji_category_url_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emoji_category_id** | **str**|  |
 **api_token** | **str**|  | [optional]
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
> SendBirdEmoji update_emoji_url_by_key(emoji_key)

Update an emoji URL

## Update an emoji URL  Updates the image URL of an emoji with the specified key.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-update-an-emoji-url ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.send_bird_emoji import SendBirdEmoji
from sendbird-platform-sdk.model.update_emoji_url_by_key_data import UpdateEmojiUrlByKeyData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    emoji_key = "emoji_key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_emoji_url_by_key_data = UpdateEmojiUrlByKeyData(
        emoji_key="emoji_key_example",
        url="url_example",
    ) # UpdateEmojiUrlByKeyData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an emoji URL
        api_response = api_instance.update_emoji_url_by_key(emoji_key)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->update_emoji_url_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an emoji URL
        api_response = api_instance.update_emoji_url_by_key(emoji_key, api_token=api_token, update_emoji_url_by_key_data=update_emoji_url_by_key_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->update_emoji_url_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emoji_key** | **str**|  |
 **api_token** | **str**|  | [optional]
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

# **use_default_emojis**
> InlineResponse20055 use_default_emojis()

Use default emojis

## Use default emojis  Determines whether to use the 7 default emojis initially provided.  https://sendbird.com/docs/chat/v3/platform-api/guides/emojis#2-use-default-emojis

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import emojis_api
from sendbird-platform-sdk.model.use_default_emojis_data import UseDefaultEmojisData
from sendbird-platform-sdk.model.inline_response20055 import InlineResponse20055
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = emojis_api.EmojisApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    use_default_emojis_data = UseDefaultEmojisData(
        use_default_emoji=True,
    ) # UseDefaultEmojisData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Use default emojis
        api_response = api_instance.use_default_emojis(api_token=api_token, use_default_emojis_data=use_default_emojis_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling EmojisApi->use_default_emojis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **use_default_emojis_data** | [**UseDefaultEmojisData**](UseDefaultEmojisData.md)|  | [optional]

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

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

