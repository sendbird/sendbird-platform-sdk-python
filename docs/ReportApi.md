# sendbird_platform_sdk.ReportApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_reports**](ReportApi.md#list_reports) | **GET** /v3/report | List reports
[**list_reports_on_channel_by_url**](ReportApi.md#list_reports_on_channel_by_url) | **GET** /v3/report/{channel_type}/{channel_url} | List reports on a channel
[**list_reports_on_message_by_id**](ReportApi.md#list_reports_on_message_by_id) | **GET** /v3/report/{channel_type}/{channel_url}/messages/{message_id} | List reports on a message
[**list_reports_on_user_by_id**](ReportApi.md#list_reports_on_user_by_id) | **GET** /v3/report/users/{offending_user_id} | List reports on a user
[**report_channel_by_url**](ReportApi.md#report_channel_by_url) | **POST** /v3/report/{channel_type}/{channel_url} | Report a channel
[**report_message_by_id**](ReportApi.md#report_message_by_id) | **POST** /v3/report/{channel_type}/{channel_url}/messages/{message_id} | Report a message
[**report_user_by_id**](ReportApi.md#report_user_by_id) | **POST** /v3/report/users/{offending_user_id} | Report a user
[**view_moderated_message_by_id**](ReportApi.md#view_moderated_message_by_id) | **GET** /v3/report/{channel_type}/{channel_url}/profanity_messages/{message_id} | View a moderated message


# **list_reports**
> ListReportsResponse list_reports()

List reports

## List reports  Retrieves a list of reports within an application regardless of object types.  https://sendbird.com/docs/chat/v3/platform-api/guides/report-content-and-subject#2-list-reports ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import report_api
from sendbird_platform_sdk.model.list_reports_response import ListReportsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_api.ReportApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    start_ts = 1 # int |  (optional)
    end_ts = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List reports
        api_response = api_instance.list_reports(api_token=api_token, token=token, limit=limit, start_ts=start_ts, end_ts=end_ts)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->list_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **start_ts** | **int**|  | [optional]
 **end_ts** | **int**|  | [optional]

### Return type

[**ListReportsResponse**](ListReportsResponse.md)

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

# **list_reports_on_channel_by_url**
> ListReportsOnChannelByUrlResponse list_reports_on_channel_by_url(channel_type, channel_url)

List reports on a channel

## List reports on a channel  Retrieves a list of reports on a channel that has offensive messages or abusive activities.  https://sendbird.com/docs/chat/v3/platform-api/guides/report-content-and-subject#2-list-reports-on-a-channel ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel which is reported for offensive messages or inappropriate activities.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import report_api
from sendbird_platform_sdk.model.list_reports_on_channel_by_url_response import ListReportsOnChannelByUrlResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_api.ReportApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List reports on a channel
        api_response = api_instance.list_reports_on_channel_by_url(channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->list_reports_on_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List reports on a channel
        api_response = api_instance.list_reports_on_channel_by_url(channel_type, channel_url, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->list_reports_on_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListReportsOnChannelByUrlResponse**](ListReportsOnChannelByUrlResponse.md)

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

# **list_reports_on_message_by_id**
> ListReportsOnMessageByIdResponse list_reports_on_message_by_id(channel_type, channel_url, message_id)

List reports on a message

## List reports on a message  Retrieves a list of reports on a message which contains suspicious, harassing, or inappropriate content.  https://sendbird.com/docs/chat/v3/platform-api/guides/report-content-and-subject#2-list-reports-on-a-message ----------------------------   `channel_type`      Type: string      Description: Specifies the type of the channel. Either open_channels or group_channels.  `channel_url`      Type: string      Description: Specifies the URL of the channel where the reported message is in.  `message_id`      Type: string      Description: Specifies the unique ID of the reported message.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import report_api
from sendbird_platform_sdk.model.list_reports_on_message_by_id_response import ListReportsOnMessageByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_api.ReportApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List reports on a message
        api_response = api_instance.list_reports_on_message_by_id(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->list_reports_on_message_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List reports on a message
        api_response = api_instance.list_reports_on_message_by_id(channel_type, channel_url, message_id, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->list_reports_on_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListReportsOnMessageByIdResponse**](ListReportsOnMessageByIdResponse.md)

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

# **list_reports_on_user_by_id**
> ListReportsOnUserByIdResponse list_reports_on_user_by_id(offending_user_id)

List reports on a user

## List reports on a user  Retrieves a list of reports on a user who sends an offensive message.  https://sendbird.com/docs/chat/v3/platform-api/guides/report-content-and-subject#2-list-reports-on-a-user ----------------------------   `offending_user_id`      Type: string      Description: Specifies the unique ID of the user who has sent the message to report.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import report_api
from sendbird_platform_sdk.model.list_reports_on_user_by_id_response import ListReportsOnUserByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_api.ReportApi(api_client)
    offending_user_id = "offending_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List reports on a user
        api_response = api_instance.list_reports_on_user_by_id(offending_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->list_reports_on_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List reports on a user
        api_response = api_instance.list_reports_on_user_by_id(offending_user_id, api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->list_reports_on_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offending_user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListReportsOnUserByIdResponse**](ListReportsOnUserByIdResponse.md)

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

# **report_channel_by_url**
> ReportChannelByUrlResponse report_channel_by_url(channel_type, channel_url)

Report a channel

## Report a channel  Reports a channel that has offensive messages or abusive activities.  https://sendbird.com/docs/chat/v3/platform-api/guides/report-content-and-subject#2-report-a-channel ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import report_api
from sendbird_platform_sdk.model.report_channel_by_url_data import ReportChannelByUrlData
from sendbird_platform_sdk.model.report_channel_by_url_response import ReportChannelByUrlResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_api.ReportApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    report_channel_by_url_data = ReportChannelByUrlData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        report_category="report_category_example",
        reporting_user_id="reporting_user_id_example",
        report_description="report_description_example",
    ) # ReportChannelByUrlData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Report a channel
        api_response = api_instance.report_channel_by_url(channel_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->report_channel_by_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Report a channel
        api_response = api_instance.report_channel_by_url(channel_type, channel_url, api_token=api_token, report_channel_by_url_data=report_channel_by_url_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->report_channel_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **api_token** | **str**|  | [optional]
 **report_channel_by_url_data** | [**ReportChannelByUrlData**](ReportChannelByUrlData.md)|  | [optional]

### Return type

[**ReportChannelByUrlResponse**](ReportChannelByUrlResponse.md)

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

# **report_message_by_id**
> ReportMessageByIdResponse report_message_by_id(channel_type, channel_url, message_id)

Report a message

## Report a message  Reports a message which contains suspicious, harassing, or inappropriate content.  https://sendbird.com/docs/chat/v3/platform-api/guides/report-content-and-subject#2-report-a-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import report_api
from sendbird_platform_sdk.model.report_message_by_id_data import ReportMessageByIdData
from sendbird_platform_sdk.model.report_message_by_id_response import ReportMessageByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_api.ReportApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    report_message_by_id_data = ReportMessageByIdData(
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        message_id="message_id_example",
        report_category="report_category_example",
        offending_user_id="offending_user_id_example",
        reporting_user_id="reporting_user_id_example",
        report_description="report_description_example",
    ) # ReportMessageByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Report a message
        api_response = api_instance.report_message_by_id(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->report_message_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Report a message
        api_response = api_instance.report_message_by_id(channel_type, channel_url, message_id, api_token=api_token, report_message_by_id_data=report_message_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->report_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **report_message_by_id_data** | [**ReportMessageByIdData**](ReportMessageByIdData.md)|  | [optional]

### Return type

[**ReportMessageByIdResponse**](ReportMessageByIdResponse.md)

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

# **report_user_by_id**
> ReportUserByIdResponse report_user_by_id(offending_user_id)

Report a user

## Report a user  Reports a user who sends an offensive message in a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/report-content-and-subject#2-report-a-user ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import report_api
from sendbird_platform_sdk.model.report_user_by_id_response import ReportUserByIdResponse
from sendbird_platform_sdk.model.report_user_by_id_data import ReportUserByIdData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_api.ReportApi(api_client)
    offending_user_id = "offending_user_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    report_user_by_id_data = ReportUserByIdData(
        offending_user_id="offending_user_id_example",
        channel_type="channel_type_example",
        channel_url="channel_url_example",
        report_category="report_category_example",
        reporting_user_id="reporting_user_id_example",
        report_description="report_description_example",
    ) # ReportUserByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Report a user
        api_response = api_instance.report_user_by_id(offending_user_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->report_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Report a user
        api_response = api_instance.report_user_by_id(offending_user_id, api_token=api_token, report_user_by_id_data=report_user_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->report_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offending_user_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **report_user_by_id_data** | [**ReportUserByIdData**](ReportUserByIdData.md)|  | [optional]

### Return type

[**ReportUserByIdResponse**](ReportUserByIdResponse.md)

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

# **view_moderated_message_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} view_moderated_message_by_id(channel_type, channel_url, message_id)

View a moderated message

## View a moderated message  Retrieves information on a message that has been moderated by the [profanity filter](https://sendbird.com/docs/chat/v3/platform-api/guides/filter-and-moderation#2-profanity-filter).  https://sendbird.com/docs/chat/v3/platform-api/guides/report-content-and-subject#2-view-a-moderated-message ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import report_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_api.ReportApi(api_client)
    channel_type = "channel_type_example" # str | 
    channel_url = "channel_url_example" # str | 
    message_id = "message_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View a moderated message
        api_response = api_instance.view_moderated_message_by_id(channel_type, channel_url, message_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->view_moderated_message_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View a moderated message
        api_response = api_instance.view_moderated_message_by_id(channel_type, channel_url, message_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling ReportApi->view_moderated_message_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_type** | **str**|  |
 **channel_url** | **str**|  |
 **message_id** | **str**|  |
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

