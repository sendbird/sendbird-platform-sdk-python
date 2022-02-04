# sendbird-platform-sdk.UserChannelMetadataApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel_metacounter**](UserChannelMetadataApi.md#create_channel_metacounter) | **POST** /v3/{channel_type}/{channel_url}/metacounter | Create a channel metacounter
[**create_channel_metadata**](UserChannelMetadataApi.md#create_channel_metadata) | **POST** /v3/{channel_type}/{channel_url}/metadata | Create a channel metadata
[**create_user_metadata**](UserChannelMetadataApi.md#create_user_metadata) | **POST** /v3/users/{user_id}/metadata | Create a user metadata
[**delete_channel_metacounter**](UserChannelMetadataApi.md#delete_channel_metacounter) | **DELETE** /v3/{channel_type}/{channel_url}/metacounter | Delete a channel metacounter - When deleting all items of a channel metacounter
[**delete_channel_metacounter_by_key**](UserChannelMetadataApi.md#delete_channel_metacounter_by_key) | **DELETE** /v3/{channel_type}/{channel_url}/metacounter/{key} | Delete a channel metacounter - When deleting a specific item of a channel metacounter by its key
[**delete_channel_metadata**](UserChannelMetadataApi.md#delete_channel_metadata) | **DELETE** /v3/{channel_type}/{channel_url}/metadata | Delete a channel metadata - When deleting all items of a channel metadata
[**delete_channel_metadata_by_key**](UserChannelMetadataApi.md#delete_channel_metadata_by_key) | **DELETE** /v3/{channel_type}/{channel_url}/metadata/{key} | Delete a channel metadata - When deleting a specific item of a channel metadata by its key
[**delete_user_metadata**](UserChannelMetadataApi.md#delete_user_metadata) | **DELETE** /v3/users/{user_id}/metadata | Delete a user metadata - When deleting all items of a user metadata
[**delete_user_metadata_by_key**](UserChannelMetadataApi.md#delete_user_metadata_by_key) | **DELETE** /v3/users/{user_id}/metadata/{key} | Delete a user metadata - When deleting a specific item of a user metadata by its key
[**update_channel_metacounter**](UserChannelMetadataApi.md#update_channel_metacounter) | **PUT** /v3/{channel_type}/{channel_url}/metacounter | Update a channel metacounter - When updating existing items of a channel metacounter by their keys or adding new items to the metacounter
[**update_channel_metacounter_by_key**](UserChannelMetadataApi.md#update_channel_metacounter_by_key) | **PUT** /v3/{channel_type}/{channel_url}/metacounter/{key} | Update a channel metacounter - When updating a specific item of a channel metacounter by its key
[**update_channel_metadata**](UserChannelMetadataApi.md#update_channel_metadata) | **PUT** /v3/{channel_type}/{channel_url}/metadata | Update a channel metadata - When updating existing items of a channel metadata by their keys or adding new items to the metadata
[**update_channel_metadata_by_key**](UserChannelMetadataApi.md#update_channel_metadata_by_key) | **PUT** /v3/{channel_type}/{channel_url}/metadata/{key} | Update a channel metadata - When updating a specific item of a channel metadata by its key
[**update_user_metadata**](UserChannelMetadataApi.md#update_user_metadata) | **PUT** /v3/users/{user_id}/metadata | Update a user metadata - When updating existing items of a user metadata by their keys or adding new items to the metadata
[**update_user_metadata_by_key**](UserChannelMetadataApi.md#update_user_metadata_by_key) | **PUT** /v3/users/{user_id}/metadata/{key} | Update a user metadata - When updating a specific item of a user metadata by its key
[**view_channel_metacounter**](UserChannelMetadataApi.md#view_channel_metacounter) | **GET** /v3/{channel_type}/{channel_url}/metacounter | View a channel metacounter - When retrieving all items of a channel metacounter
[**view_channel_metacounter_by_key**](UserChannelMetadataApi.md#view_channel_metacounter_by_key) | **GET** /v3/{channel_type}/{channel_url}/metacounter/{key} | View a channel metacounter - When retrieving a specific item of a channel metacounter by its key
[**view_channel_metadata**](UserChannelMetadataApi.md#view_channel_metadata) | **GET** /v3/{channel_type}/{channel_url}/metadata | View a channel metadata - When retrieving all items of a channel metadata
[**view_channel_metadata_by_key**](UserChannelMetadataApi.md#view_channel_metadata_by_key) | **GET** /v3/{channel_type}/{channel_url}/metadata/{key} | View a channel metadata - When retrieving a specific item of a channel metadata by its key
[**view_user_metadata**](UserChannelMetadataApi.md#view_user_metadata) | **GET** /v3/users/{user_id}/metadata | View a user metadata - When retrieving all items of a user metadata
[**view_user_metadata_by_key**](UserChannelMetadataApi.md#view_user_metadata_by_key) | **GET** /v3/users/{user_id}/metadata/{key} | View a user metadata - When retrieving a specific item of a user metadata by its key


# **create_channel_metacounter**
> {str: (SendBirdAdditionalProperties,)} create_channel_metacounter(channel_type, channel_url)

Create a channel metacounter

## Create a channel metacounter  Creates a channel metacounter's items to store in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-create-a-channel-metacounter ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.send_bird_additional_properties import SendBirdAdditionalProperties
from sendbird-platform-sdk.model.create_channel_metacounter_data import CreateChannelMetacounterData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_channel_metacounter_data = CreateChannelMetacounterData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        metacounter="metacounter_example",
    ) # CreateChannelMetacounterData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a channel metacounter
        api_response = api_instance.create_channel_metacounter(channel_type, channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->create_channel_metacounter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a channel metacounter
        api_response = api_instance.create_channel_metacounter(channel_type, channel_url, api_token=api_token, create_channel_metacounter_data=create_channel_metacounter_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->create_channel_metacounter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **create_channel_metacounter_data** | [**CreateChannelMetacounterData**](CreateChannelMetacounterData.md)|  | [optional]

### Return type

[**{str: (SendBirdAdditionalProperties,)}**](SendBirdAdditionalProperties.md)

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

# **create_channel_metadata**
> InlineResponse20061 create_channel_metadata(channel_type, channel_url)

Create a channel metadata

## Create a channel metadata  Creates a channel metadata's items to store in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-create-a-channel-metadata ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.inline_response20061 import InlineResponse20061
from sendbird-platform-sdk.model.create_channel_metadata_data import CreateChannelMetadataData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_channel_metadata_data = CreateChannelMetadataData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        metadata="metadata_example",
        include_ts=True,
    ) # CreateChannelMetadataData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a channel metadata
        api_response = api_instance.create_channel_metadata(channel_type, channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->create_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a channel metadata
        api_response = api_instance.create_channel_metadata(channel_type, channel_url, api_token=api_token, create_channel_metadata_data=create_channel_metadata_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->create_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **create_channel_metadata_data** | [**CreateChannelMetadataData**](CreateChannelMetadataData.md)|  | [optional]

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

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

# **create_user_metadata**
> InlineResponse20047UserMetadata create_user_metadata(user_id)

Create a user metadata

## Create a user metadata  Creates a user metadata's items to store in a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-create-a-user-metadata ----------------------------

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.create_user_metadata_data import CreateUserMetadataData
from sendbird-platform-sdk.model.inline_response20047_user_metadata import InlineResponse20047UserMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_user_metadata_data = CreateUserMetadataData(
        user_id="user_id_example",
        metadata="metadata_example",
    ) # CreateUserMetadataData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a user metadata
        api_response = api_instance.create_user_metadata(user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->create_user_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a user metadata
        api_response = api_instance.create_user_metadata(user_id, api_token=api_token, create_user_metadata_data=create_user_metadata_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->create_user_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **create_user_metadata_data** | [**CreateUserMetadataData**](CreateUserMetadataData.md)|  | [optional]

### Return type

[**InlineResponse20047UserMetadata**](InlineResponse20047UserMetadata.md)

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

# **delete_channel_metacounter**
> delete_channel_metacounter(channel_type, channel_url)

Delete a channel metacounter - When deleting all items of a channel metacounter

## Delete a channel metacounter  Deletes a channel metacounter's item that is stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-delete-a-channel-metacounter ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel which has the metacounter to delete.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel metacounter - When deleting all items of a channel metacounter
        api_instance.delete_channel_metacounter(channel_type, channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_channel_metacounter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a channel metacounter - When deleting all items of a channel metacounter
        api_instance.delete_channel_metacounter(channel_type, channel_url, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_channel_metacounter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
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

# **delete_channel_metacounter_by_key**
> delete_channel_metacounter_by_key(channel_type, channel_url, key)

Delete a channel metacounter - When deleting a specific item of a channel metacounter by its key

## Delete a channel metacounter  Deletes a channel metacounter's item that is stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-delete-a-channel-metacounter ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel which has the metacounter to delete.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel metacounter - When deleting a specific item of a channel metacounter by its key
        api_instance.delete_channel_metacounter_by_key(channel_type, channel_url, key)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_channel_metacounter_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a channel metacounter - When deleting a specific item of a channel metacounter by its key
        api_instance.delete_channel_metacounter_by_key(channel_type, channel_url, key, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_channel_metacounter_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  |
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

# **delete_channel_metadata**
> delete_channel_metadata(channel_type, channel_url)

Delete a channel metadata - When deleting all items of a channel metadata

## Delete a channel metadata  Deletes a channel metadata's one or all items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-delete-a-channel-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel which has the metadata to delete.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    key = "key_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel metadata - When deleting all items of a channel metadata
        api_instance.delete_channel_metadata(channel_type, channel_url)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a channel metadata - When deleting all items of a channel metadata
        api_instance.delete_channel_metadata(channel_type, channel_url, api_token=api_token, key=key)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **key** | **str**|  | [optional]

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

# **delete_channel_metadata_by_key**
> delete_channel_metadata_by_key(channel_type, channel_url, key)

Delete a channel metadata - When deleting a specific item of a channel metadata by its key

## Delete a channel metadata  Deletes a channel metadata's one or all items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-delete-a-channel-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel which has the metadata to delete.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel metadata - When deleting a specific item of a channel metadata by its key
        api_instance.delete_channel_metadata_by_key(channel_type, channel_url, key)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_channel_metadata_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a channel metadata - When deleting a specific item of a channel metadata by its key
        api_instance.delete_channel_metadata_by_key(channel_type, channel_url, key, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_channel_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  |
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

# **delete_user_metadata**
> delete_user_metadata(user_id)

Delete a user metadata - When deleting all items of a user metadata

## Delete a user metadata  Deletes a user metadata's one or all items that are stored in a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-delete-a-user-metadata ----------------------------   `user_id`      Type: string      Description: Specifies the ID of the user who has the metadata to delete.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    key = "key_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a user metadata - When deleting all items of a user metadata
        api_instance.delete_user_metadata(user_id)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_user_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a user metadata - When deleting all items of a user metadata
        api_instance.delete_user_metadata(user_id, api_token=api_token, key=key)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_user_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **key** | **str**|  | [optional]

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

# **delete_user_metadata_by_key**
> delete_user_metadata_by_key(user_id, key)

Delete a user metadata - When deleting a specific item of a user metadata by its key

## Delete a user metadata  Deletes a user metadata's one or all items that are stored in a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-delete-a-user-metadata ----------------------------   `user_id`      Type: string      Description: Specifies the ID of the user who has the metadata to delete.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    user_id = "user_id_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a user metadata - When deleting a specific item of a user metadata by its key
        api_instance.delete_user_metadata_by_key(user_id, key)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_user_metadata_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a user metadata - When deleting a specific item of a user metadata by its key
        api_instance.delete_user_metadata_by_key(user_id, key, api_token=api_token)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->delete_user_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **key** | **str**|  |
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

# **update_channel_metacounter**
> {str: (SendBirdAdditionalProperties,)} update_channel_metacounter(channel_type, channel_url)

Update a channel metacounter - When updating existing items of a channel metacounter by their keys or adding new items to the metacounter

## Update a channel metacounter  Updates existing items of a channel metacounter by their keys, or adds new items to the metacounter.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-update-a-channel-metacounter ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.send_bird_additional_properties import SendBirdAdditionalProperties
from sendbird-platform-sdk.model.update_channel_metacounter_data import UpdateChannelMetacounterData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_channel_metacounter_data = UpdateChannelMetacounterData(
        metacounter="metacounter_example",
        mode="mode_example",
        upsert=True,
    ) # UpdateChannelMetacounterData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel metacounter - When updating existing items of a channel metacounter by their keys or adding new items to the metacounter
        api_response = api_instance.update_channel_metacounter(channel_type, channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_channel_metacounter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel metacounter - When updating existing items of a channel metacounter by their keys or adding new items to the metacounter
        api_response = api_instance.update_channel_metacounter(channel_type, channel_url, api_token=api_token, update_channel_metacounter_data=update_channel_metacounter_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_channel_metacounter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_channel_metacounter_data** | [**UpdateChannelMetacounterData**](UpdateChannelMetacounterData.md)|  | [optional]

### Return type

[**{str: (SendBirdAdditionalProperties,)}**](SendBirdAdditionalProperties.md)

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

# **update_channel_metacounter_by_key**
> {str: (str,)} update_channel_metacounter_by_key(channel_type, channel_url, key)

Update a channel metacounter - When updating a specific item of a channel metacounter by its key

## Update a channel metacounter  Updates existing items of a channel metacounter by their keys, or adds new items to the metacounter.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-update-a-channel-metacounter ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel metacounter - When updating a specific item of a channel metacounter by its key
        api_response = api_instance.update_channel_metacounter_by_key(channel_type, channel_url, key)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_channel_metacounter_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel metacounter - When updating a specific item of a channel metacounter by its key
        api_response = api_instance.update_channel_metacounter_by_key(channel_type, channel_url, key, api_token=api_token, body=body)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_channel_metacounter_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  |
 **api_token** | **str**|  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (str,)}**

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

# **update_channel_metadata**
> {str: (str,)} update_channel_metadata(channel_type, channel_url)

Update a channel metadata - When updating existing items of a channel metadata by their keys or adding new items to the metadata

## Update a channel metadata  Updates existing items of a channel metadata by their keys, or adds new items to the metadata.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-update-a-channel-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.update_channel_metadata_data import UpdateChannelMetadataData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_channel_metadata_data = UpdateChannelMetadataData(
        metadata="metadata_example",
        upsert=True,
    ) # UpdateChannelMetadataData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel metadata - When updating existing items of a channel metadata by their keys or adding new items to the metadata
        api_response = api_instance.update_channel_metadata(channel_type, channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel metadata - When updating existing items of a channel metadata by their keys or adding new items to the metadata
        api_response = api_instance.update_channel_metadata(channel_type, channel_url, api_token=api_token, update_channel_metadata_data=update_channel_metadata_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_channel_metadata_data** | [**UpdateChannelMetadataData**](UpdateChannelMetadataData.md)|  | [optional]

### Return type

**{str: (str,)}**

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

# **update_channel_metadata_by_key**
> {str: (str,)} update_channel_metadata_by_key(channel_type, channel_url, key)

Update a channel metadata - When updating a specific item of a channel metadata by its key

## Update a channel metadata  Updates existing items of a channel metadata by their keys, or adds new items to the metadata.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-update-a-channel-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel metadata - When updating a specific item of a channel metadata by its key
        api_response = api_instance.update_channel_metadata_by_key(channel_type, channel_url, key)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_channel_metadata_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel metadata - When updating a specific item of a channel metadata by its key
        api_response = api_instance.update_channel_metadata_by_key(channel_type, channel_url, key, api_token=api_token, body=body)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_channel_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  |
 **api_token** | **str**|  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (str,)}**

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

# **update_user_metadata**
> InlineResponse20060 update_user_metadata(user_id)

Update a user metadata - When updating existing items of a user metadata by their keys or adding new items to the metadata

## Update a user metadata  Updates existing items of a user metadata by their keys, or adds new items to the metadata.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-update-a-user-metadata ----------------------------   `user_id`      Type: string      Description: Specifies the ID of the user to update the metadata in.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.inline_response20060 import InlineResponse20060
from sendbird-platform-sdk.model.update_user_metadata_data import UpdateUserMetadataData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_user_metadata_data = UpdateUserMetadataData(
        metadata="metadata_example",
        upsert=True,
    ) # UpdateUserMetadataData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a user metadata - When updating existing items of a user metadata by their keys or adding new items to the metadata
        api_response = api_instance.update_user_metadata(user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_user_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a user metadata - When updating existing items of a user metadata by their keys or adding new items to the metadata
        api_response = api_instance.update_user_metadata(user_id, api_token=api_token, update_user_metadata_data=update_user_metadata_data)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_user_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_user_metadata_data** | [**UpdateUserMetadataData**](UpdateUserMetadataData.md)|  | [optional]

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

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

# **update_user_metadata_by_key**
> {str: (str,)} update_user_metadata_by_key(user_id, key)

Update a user metadata - When updating a specific item of a user metadata by its key

## Update a user metadata  Updates existing items of a user metadata by their keys, or adds new items to the metadata.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-update-a-user-metadata ----------------------------   `user_id`      Type: string      Description: Specifies the ID of the user to update the metadata in.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    user_id = "user_id_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a user metadata - When updating a specific item of a user metadata by its key
        api_response = api_instance.update_user_metadata_by_key(user_id, key)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_user_metadata_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a user metadata - When updating a specific item of a user metadata by its key
        api_response = api_instance.update_user_metadata_by_key(user_id, key, api_token=api_token, body=body)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->update_user_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **key** | **str**|  |
 **api_token** | **str**|  | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (str,)}**

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

# **view_channel_metacounter**
> {str: (SendBirdAdditionalProperties,)} view_channel_metacounter(channel_type, channel_url)

View a channel metacounter - When retrieving all items of a channel metacounter

## View a channel metacounter  Retrieves channel metacounter's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metacounter ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.send_bird_additional_properties import SendBirdAdditionalProperties
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    key = "key_example" # str |  (optional)
    keys = [
        "keys_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel metacounter - When retrieving all items of a channel metacounter
        api_response = api_instance.view_channel_metacounter(channel_type, channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_channel_metacounter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel metacounter - When retrieving all items of a channel metacounter
        api_response = api_instance.view_channel_metacounter(channel_type, channel_url, api_token=api_token, key=key, keys=keys)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_channel_metacounter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **key** | **str**|  | [optional]
 **keys** | **[str]**|  | [optional]

### Return type

[**{str: (SendBirdAdditionalProperties,)}**](SendBirdAdditionalProperties.md)

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

# **view_channel_metacounter_by_key**
> {str: (SendBirdAdditionalProperties,)} view_channel_metacounter_by_key(channel_type, channel_url, key)

View a channel metacounter - When retrieving a specific item of a channel metacounter by its key

## View a channel metacounter  Retrieves channel metacounter's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metacounter ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.send_bird_additional_properties import SendBirdAdditionalProperties
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel metacounter - When retrieving a specific item of a channel metacounter by its key
        api_response = api_instance.view_channel_metacounter_by_key(channel_type, channel_url, key)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_channel_metacounter_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel metacounter - When retrieving a specific item of a channel metacounter by its key
        api_response = api_instance.view_channel_metacounter_by_key(channel_type, channel_url, key, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_channel_metacounter_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**{str: (SendBirdAdditionalProperties,)}**](SendBirdAdditionalProperties.md)

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

# **view_channel_metadata**
> {str: (str,)} view_channel_metadata(channel_type, channel_url)

View a channel metadata - When retrieving all items of a channel metadata

## View a channel metadata  Retrieves a channel metadata's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    key = "key_example" # str |  (optional)
    keys = [
        "keys_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel metadata - When retrieving all items of a channel metadata
        api_response = api_instance.view_channel_metadata(channel_type, channel_url)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel metadata - When retrieving all items of a channel metadata
        api_response = api_instance.view_channel_metadata(channel_type, channel_url, api_token=api_token, key=key, keys=keys)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **key** | **str**|  | [optional]
 **keys** | **[str]**|  | [optional]

### Return type

**{str: (str,)}**

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

# **view_channel_metadata_by_key**
> {str: (str,)} view_channel_metadata_by_key(channel_type, channel_url, key)

View a channel metadata - When retrieving a specific item of a channel metadata by its key

## View a channel metadata  Retrieves a channel metadata's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel metadata - When retrieving a specific item of a channel metadata by its key
        api_response = api_instance.view_channel_metadata_by_key(channel_type, channel_url, key)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_channel_metadata_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel metadata - When retrieving a specific item of a channel metadata by its key
        api_response = api_instance.view_channel_metadata_by_key(channel_type, channel_url, key, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_channel_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

**{str: (str,)}**

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

# **view_user_metadata**
> InlineResponse20047UserMetadata view_user_metadata(user_id)

View a user metadata - When retrieving all items of a user metadata

## View a user metadata  Retrieves a user metadata's one or more items that are stored in a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-user-metadata ----------------------------   `user_id`      Type: string      Description: Specifies the ID of the user to retrieve the metadata in.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from sendbird-platform-sdk.model.inline_response20047_user_metadata import InlineResponse20047UserMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    user_id = "user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    key = "key_example" # str |  (optional)
    keys = [
        "keys_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a user metadata - When retrieving all items of a user metadata
        api_response = api_instance.view_user_metadata(user_id)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_user_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a user metadata - When retrieving all items of a user metadata
        api_response = api_instance.view_user_metadata(user_id, api_token=api_token, key=key, keys=keys)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_user_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **key** | **str**|  | [optional]
 **keys** | **[str]**|  | [optional]

### Return type

[**InlineResponse20047UserMetadata**](InlineResponse20047UserMetadata.md)

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

# **view_user_metadata_by_key**
> {str: (str,)} view_user_metadata_by_key(user_id, key)

View a user metadata - When retrieving a specific item of a user metadata by its key

## View a user metadata  Retrieves a user metadata's one or more items that are stored in a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-user-metadata ----------------------------   `user_id`      Type: string      Description: Specifies the ID of the user to retrieve the metadata in.

### Example


```python
import time
import sendbird-platform-sdk
from sendbird-platform-sdk.api import user__channel_metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user__channel_metadata_api.UserChannelMetadataApi(api_client)
    user_id = "user_id_example" # str | 
    key = "key_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a user metadata - When retrieving a specific item of a user metadata by its key
        api_response = api_instance.view_user_metadata_by_key(user_id, key)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_user_metadata_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a user metadata - When retrieving a specific item of a user metadata by its key
        api_response = api_instance.view_user_metadata_by_key(user_id, key, api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling UserChannelMetadataApi->view_user_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **key** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

**{str: (str,)}**

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

