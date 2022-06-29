# sendbird_platform_sdk.MetadataApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**view_channel_metacounter**](MetadataApi.md#view_channel_metacounter) | **GET** /v3/{channel_type}/{channel_url}/metacounter | View a channel metacounter - When retrieving all items of a channel metacounter
[**view_channel_metacounter_by_key**](MetadataApi.md#view_channel_metacounter_by_key) | **GET** /v3/{channel_type}/{channel_url}/metacounter/{key} | View a channel metacounter - When retrieving a specific item of a channel metacounter by its key
[**view_channel_metadata**](MetadataApi.md#view_channel_metadata) | **GET** /v3/{channel_type}/{channel_url}/metadata | View a channel metadata - When retrieving all items of a channel metadata
[**view_channel_metadata_by_key**](MetadataApi.md#view_channel_metadata_by_key) | **GET** /v3/{channel_type}/{channel_url}/metadata/{key} | View a channel metadata - When retrieving a specific item of a channel metadata by its key
[**view_user_metadata**](MetadataApi.md#view_user_metadata) | **GET** /v3/users/{user_id}/metadata | View a user metadata - When retrieving all items of a user metadata
[**view_user_metadata_by_key**](MetadataApi.md#view_user_metadata_by_key) | **GET** /v3/users/{user_id}/metadata/{key} | View a user metadata - When retrieving a specific item of a user metadata by its key


# **view_channel_metacounter**
> ViewChannelMetacounterResponse view_channel_metacounter(api_token, channel_type, channel_url)

View a channel metacounter - When retrieving all items of a channel metacounter

## View a channel metacounter  Retrieves channel metacounter's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metacounter ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import metadata_api
from sendbird_platform_sdk.model.send_bird_additional_properties import SendBirdAdditionalProperties
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str |  (optional)
    keys = [
        "keys_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel metacounter - When retrieving all items of a channel metacounter
        api_response = api_instance.view_channel_metacounter(api_token, channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_channel_metacounter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel metacounter - When retrieving all items of a channel metacounter
        api_response = api_instance.view_channel_metacounter(api_token, channel_type, channel_url, key=key, keys=keys)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_channel_metacounter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  | [optional]
 **keys** | **[str]**|  | [optional]

### Return type

[**ViewChannelMetacounterResponse**](SendBirdAdditionalProperties.md)

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
> ViewChannelMetacounterByKeyResponse view_channel_metacounter_by_key(api_token, channel_type, channel_url, key)

View a channel metacounter - When retrieving a specific item of a channel metacounter by its key

## View a channel metacounter  Retrieves channel metacounter's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metacounter ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import metadata_api
from sendbird_platform_sdk.model.send_bird_additional_properties import SendBirdAdditionalProperties
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a channel metacounter - When retrieving a specific item of a channel metacounter by its key
        api_response = api_instance.view_channel_metacounter_by_key(api_token, channel_type, channel_url, key)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_channel_metacounter_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  |

### Return type

[**ViewChannelMetacounterByKeyResponse**](SendBirdAdditionalProperties.md)

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
> ViewChannelMetadataResponse view_channel_metadata(api_token, channel_type, channel_url)

View a channel metadata - When retrieving all items of a channel metadata

## View a channel metadata  Retrieves a channel metadata's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str |  (optional)
    keys = [
        "keys_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel metadata - When retrieving all items of a channel metadata
        api_response = api_instance.view_channel_metadata(api_token, channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel metadata - When retrieving all items of a channel metadata
        api_response = api_instance.view_channel_metadata(api_token, channel_type, channel_url, key=key, keys=keys)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  | [optional]
 **keys** | **[str]**|  | [optional]

### Return type

**ViewChannelMetadataResponse**

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
> ViewChannelMetadataByKeyResponse view_channel_metadata_by_key(api_token, channel_type, channel_url, key)

View a channel metadata - When retrieving a specific item of a channel metadata by its key

## View a channel metadata  Retrieves a channel metadata's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a channel metadata - When retrieving a specific item of a channel metadata by its key
        api_response = api_instance.view_channel_metadata_by_key(api_token, channel_type, channel_url, key)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_channel_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **key** | **str**|  |

### Return type

**ViewChannelMetadataByKeyResponse**

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
> ViewUserMetadataResponse view_user_metadata(api_token, user_id)

View a user metadata - When retrieving all items of a user metadata

## View a user metadata  Retrieves a user metadata's one or more items that are stored in a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-user-metadata ----------------------------   `user_id`      Type: string      Description: Specifies the ID of the user to retrieve the metadata in.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import metadata_api
from sendbird_platform_sdk.model.view_user_metadata_response import ViewUserMetadataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    key = "key_example" # str |  (optional)
    keys = [
        "keys_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a user metadata - When retrieving all items of a user metadata
        api_response = api_instance.view_user_metadata(api_token, user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_user_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a user metadata - When retrieving all items of a user metadata
        api_response = api_instance.view_user_metadata(api_token, user_id, key=key, keys=keys)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_user_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **key** | **str**|  | [optional]
 **keys** | **[str]**|  | [optional]

### Return type

[**ViewUserMetadataResponse**](ViewUserMetadataResponse.md)

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
> ViewUserMetadataByKeyResponse view_user_metadata_by_key(api_token, user_id, key)

View a user metadata - When retrieving a specific item of a user metadata by its key

## View a user metadata  Retrieves a user metadata's one or more items that are stored in a user.  https://sendbird.com/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-user-metadata ----------------------------   `user_id`      Type: string      Description: Specifies the ID of the user to retrieve the metadata in.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import metadata_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    user_id = "user_id_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a user metadata - When retrieving a specific item of a user metadata by its key
        api_response = api_instance.view_user_metadata_by_key(api_token, user_id, key)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_user_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **user_id** | **str**|  |
 **key** | **str**|  |

### Return type

**ViewUserMetadataByKeyResponse**

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

