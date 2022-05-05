# sendbird_platform_sdk.DataExportApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_data_exports_by_message_channel_or_user**](DataExportApi.md#list_data_exports_by_message_channel_or_user) | **GET** /v3/export/{data_type} | List data exports by message, channel, or user
[**register_and_schedule_data_export**](DataExportApi.md#register_and_schedule_data_export) | **POST** /v3/export/{data_type} | Register and schedule a data export
[**view_data_export_by_id**](DataExportApi.md#view_data_export_by_id) | **GET** /v3/export/{data_type}/{request_id} | View a data export


# **list_data_exports_by_message_channel_or_user**
> ListDataExportsByMessageChannelOrUserResponse list_data_exports_by_message_channel_or_user(api_token, data_type)

List data exports by message, channel, or user

## List data exports by message, channel, or user  Retrieves a list of message, channel or user data exports  https://sendbird.com/docs/chat/v3/platform-api/guides/data-export#2-list-data-exports-by-message,-channel,-or-user ----------------------------   `data_type`      Type: string      Description: Specifies the type of a data export to retrieve. Acceptable values are messages, channels, users, and failed_webhooks.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import data_export_api
from sendbird_platform_sdk.model.list_data_exports_by_message_channel_or_user_response import ListDataExportsByMessageChannelOrUserResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_export_api.DataExportApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    data_type = "data_type_example" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List data exports by message, channel, or user
        api_response = api_instance.list_data_exports_by_message_channel_or_user(api_token, data_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling DataExportApi->list_data_exports_by_message_channel_or_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List data exports by message, channel, or user
        api_response = api_instance.list_data_exports_by_message_channel_or_user(api_token, data_type, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling DataExportApi->list_data_exports_by_message_channel_or_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **data_type** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListDataExportsByMessageChannelOrUserResponse**](ListDataExportsByMessageChannelOrUserResponse.md)

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

# **register_and_schedule_data_export**
> RegisterAndScheduleDataExportResponse register_and_schedule_data_export(api_token, data_type)

Register and schedule a data export

## Register and schedule a data export  Registers and schedules a message, channel, or user data export.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-export#2-register-and-schedule-a-data-export ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import data_export_api
from sendbird_platform_sdk.model.register_and_schedule_data_export_response import RegisterAndScheduleDataExportResponse
from sendbird_platform_sdk.model.register_and_schedule_data_export_data import RegisterAndScheduleDataExportData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_export_api.DataExportApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    data_type = "data_type_example" # str | 
    register_and_schedule_data_export_data = RegisterAndScheduleDataExportData(
        start_ts=1,
        end_ts=1,
        format="format_example",
        csv_delimiter="csv_delimiter_example",
        timezone="timezone_example",
        sender_ids=[
            1,
        ],
        exclude_sender_ids=[
            1,
        ],
        channel_urls=[
            "channel_urls_example",
        ],
        exclude_channel_urls=[
            "exclude_channel_urls_example",
        ],
        user_ids=[
            1,
        ],
        show_read_receipt=True,
        show_channel_metadata=True,
        neighboring_message_limit=1,
    ) # RegisterAndScheduleDataExportData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register and schedule a data export
        api_response = api_instance.register_and_schedule_data_export(api_token, data_type)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling DataExportApi->register_and_schedule_data_export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register and schedule a data export
        api_response = api_instance.register_and_schedule_data_export(api_token, data_type, register_and_schedule_data_export_data=register_and_schedule_data_export_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling DataExportApi->register_and_schedule_data_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **data_type** | **str**|  |
 **register_and_schedule_data_export_data** | [**RegisterAndScheduleDataExportData**](RegisterAndScheduleDataExportData.md)|  | [optional]

### Return type

[**RegisterAndScheduleDataExportResponse**](RegisterAndScheduleDataExportResponse.md)

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

# **view_data_export_by_id**
> ViewDataExportByIdResponse view_data_export_by_id(api_token, data_type, request_id)

View a data export

## View a data export  Retrieves information on a message, channel or user data export.  https://sendbird.com/docs/chat/v3/platform-api/guides/data-export#2-view-a-data-export ----------------------------   `data_type`      Type: string      Description: Specifies the type of a targeted data export. Acceptable values are messages, channels,  users, and failed_webhooks.  `request_id`      Type: string      Description: Specifies the unique ID of a data export to retrieve.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import data_export_api
from sendbird_platform_sdk.model.view_data_export_by_id_response import ViewDataExportByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_export_api.DataExportApi(api_client)
    api_token = "{{API_TOKEN}}" # str | 
    data_type = "data_type_example" # str | 
    request_id = "request_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a data export
        api_response = api_instance.view_data_export_by_id(api_token, data_type, request_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling DataExportApi->view_data_export_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **data_type** | **str**|  |
 **request_id** | **str**|  |

### Return type

[**ViewDataExportByIdResponse**](ViewDataExportByIdResponse.md)

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

