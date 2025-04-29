# sendbird_platform_sdk.MetadataApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_channel_metadata**](MetadataApi.md#create_a_channel_metadata) | **POST** /v3/{channel_type}/{channel_url}/metadata | Create a channel metadata
[**delete_a_channel_metadata_when_deleting_all_items_of_a_channel_metadata**](MetadataApi.md#delete_a_channel_metadata_when_deleting_all_items_of_a_channel_metadata) | **DELETE** /v3/{channel_type}/{channel_url}/metadata | Delete a channel metadata - When deleting all items of a channel metadata
[**update_a_channel_metadata**](MetadataApi.md#update_a_channel_metadata) | **PUT** /v3/{channel_type}/{channel_url}/metadata | Update a channel metadata - When updating existing items of a channel metadata by their keys or adding new items to the metadata
[**view_a_channel_metadata_when_retrieving_all_items_of_a_channel_metadata**](MetadataApi.md#view_a_channel_metadata_when_retrieving_all_items_of_a_channel_metadata) | **GET** /v3/{channel_type}/{channel_url}/metadata | View a channel metadata - When retrieving all items of a channel metadata


# **create_a_channel_metadata**
> CreateAChannelMetadataResponse create_a_channel_metadata(channel_type, channel_url)

Create a channel metadata

## Create a channel metadata  Creates a channel metadata's items to store in a channel.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-metadata/channel-create-metadata#1-create-metadata ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import metadata_api
from sendbird_platform_sdk.model.create_a_channel_metadata_request import CreateAChannelMetadataRequest
from sendbird_platform_sdk.model.create_a_channel_metadata_response import CreateAChannelMetadataResponse
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
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_a_channel_metadata_request = CreateAChannelMetadataRequest(
        include_ts=True,
        metadata={},
    ) # CreateAChannelMetadataRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a channel metadata
        api_response = api_instance.create_a_channel_metadata(channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->create_a_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a channel metadata
        api_response = api_instance.create_a_channel_metadata(channel_type, channel_url, api_token=api_token, create_a_channel_metadata_request=create_a_channel_metadata_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->create_a_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **create_a_channel_metadata_request** | [**CreateAChannelMetadataRequest**](CreateAChannelMetadataRequest.md)|  | [optional]

### Return type

[**CreateAChannelMetadataResponse**](CreateAChannelMetadataResponse.md)

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

# **delete_a_channel_metadata_when_deleting_all_items_of_a_channel_metadata**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_a_channel_metadata_when_deleting_all_items_of_a_channel_metadata(channel_type, channel_url)

Delete a channel metadata - When deleting all items of a channel metadata

## Delete a channel metadata  Deletes a channel metadata's one or all items that are stored in a channel.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-metadata/channel-delete-metadata#1-delete-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel which has the metadata to delete.

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
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    key = "key_example" # str |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a channel metadata - When deleting all items of a channel metadata
        api_response = api_instance.delete_a_channel_metadata_when_deleting_all_items_of_a_channel_metadata(channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->delete_a_channel_metadata_when_deleting_all_items_of_a_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a channel metadata - When deleting all items of a channel metadata
        api_response = api_instance.delete_a_channel_metadata_when_deleting_all_items_of_a_channel_metadata(channel_type, channel_url, key=key, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->delete_a_channel_metadata_when_deleting_all_items_of_a_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **key** | **str**|  | [optional]
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

# **update_a_channel_metadata**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_a_channel_metadata(channel_type, channel_url)

Update a channel metadata - When updating existing items of a channel metadata by their keys or adding new items to the metadata

## Update a channel metadata  Updates existing items of a channel metadata by their keys, or adds new items to the metadata.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-metadata/channel-update-metadata#1-update-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import metadata_api
from sendbird_platform_sdk.model.update_a_channel_metadata_request import UpdateAChannelMetadataRequest
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
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_a_channel_metadata_request = UpdateAChannelMetadataRequest(
        metadata={},
        upsert=True,
    ) # UpdateAChannelMetadataRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a channel metadata - When updating existing items of a channel metadata by their keys or adding new items to the metadata
        api_response = api_instance.update_a_channel_metadata(channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->update_a_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a channel metadata - When updating existing items of a channel metadata by their keys or adding new items to the metadata
        api_response = api_instance.update_a_channel_metadata(channel_type, channel_url, api_token=api_token, update_a_channel_metadata_request=update_a_channel_metadata_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->update_a_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **update_a_channel_metadata_request** | [**UpdateAChannelMetadataRequest**](UpdateAChannelMetadataRequest.md)|  | [optional]

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

# **view_a_channel_metadata_when_retrieving_all_items_of_a_channel_metadata**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} view_a_channel_metadata_when_retrieving_all_items_of_a_channel_metadata(channel_type, channel_url)

View a channel metadata - When retrieving all items of a channel metadata

## View a channel metadata  Retrieves a channel metadata's one or more items that are stored in a channel.  https://sendbird.com/docs/chat/platform-api/v3/channel/managing-metadata/channel-get-metadata#1-get-metadata ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the target channel.

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
    channel_type = "open_channels" # str | (Required) 
    channel_url = "channel_url_example" # str | (Required) 
    key = "key_example" # str |  (optional)
    keys = "keys_example" # str | In a query string, specifies an array of one or more keys of the metadata items. If not specified, all items of the metadata are returned. If specified, only the items that match the parameter values are returned. URL encoding each key is recommended. (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a channel metadata - When retrieving all items of a channel metadata
        api_response = api_instance.view_a_channel_metadata_when_retrieving_all_items_of_a_channel_metadata(channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_a_channel_metadata_when_retrieving_all_items_of_a_channel_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a channel metadata - When retrieving all items of a channel metadata
        api_response = api_instance.view_a_channel_metadata_when_retrieving_all_items_of_a_channel_metadata(channel_type, channel_url, key=key, keys=keys, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling MetadataApi->view_a_channel_metadata_when_retrieving_all_items_of_a_channel_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**| (Required)  |
 **channel_url** | **str**| (Required)  |
 **key** | **str**|  | [optional]
 **keys** | **str**| In a query string, specifies an array of one or more keys of the metadata items. If not specified, all items of the metadata are returned. If specified, only the items that match the parameter values are returned. URL encoding each key is recommended. | [optional]
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

