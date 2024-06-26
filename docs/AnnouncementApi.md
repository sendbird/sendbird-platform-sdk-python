# sendbird_platform_sdk.AnnouncementApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_detailed_open_rate_of_announcement_group**](AnnouncementApi.md#get_detailed_open_rate_of_announcement_group) | **GET** /v3/announcement_open_rate_by_group/{announcement_group} | Get detailed open rate of an announcement group
[**get_statistics**](AnnouncementApi.md#get_statistics) | **GET** /v3/announcement_stats/weekly | Get statistics - weekly
[**get_statistics_daily**](AnnouncementApi.md#get_statistics_daily) | **GET** /v3/announcement_stats/daily | Get statistics - daily
[**get_statistics_monthly**](AnnouncementApi.md#get_statistics_monthly) | **GET** /v3/announcement_stats/monthly | Get statistics - monthly
[**list_announcement_groups**](AnnouncementApi.md#list_announcement_groups) | **GET** /v3/announcement_group | List announcement groups
[**schedule_announcement**](AnnouncementApi.md#schedule_announcement) | **POST** /v3/announcements | Schedule an announcement
[**update_announcement_by_id**](AnnouncementApi.md#update_announcement_by_id) | **PUT** /v3/announcements/{unique_id} | Update an announcement
[**view_announcement_by_id**](AnnouncementApi.md#view_announcement_by_id) | **GET** /v3/announcements/{unique_id} | View an announcement


# **get_detailed_open_rate_of_announcement_group**
> GetDetailedOpenRateOfAnnouncementGroupResponse get_detailed_open_rate_of_announcement_group(announcement_group)

Get detailed open rate of an announcement group

## Get detailed open rate of an announcement group  Retrieves the detailed open rate information of an announcement group.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-detailed-open-rate-of-an-announcement-group ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.get_detailed_open_rate_of_announcement_group_response import GetDetailedOpenRateOfAnnouncementGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    announcement_group = "announcement_group_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get detailed open rate of an announcement group
        api_response = api_instance.get_detailed_open_rate_of_announcement_group(announcement_group)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_detailed_open_rate_of_announcement_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get detailed open rate of an announcement group
        api_response = api_instance.get_detailed_open_rate_of_announcement_group(announcement_group, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_detailed_open_rate_of_announcement_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_group** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**GetDetailedOpenRateOfAnnouncementGroupResponse**](GetDetailedOpenRateOfAnnouncementGroupResponse.md)

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

# **get_statistics**
> GetStatisticsResponse get_statistics()

Get statistics - weekly

## Get statistics  Retrieves the daily, weekly or monthly statistics of an announcement or an announcement group.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-statistics ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.get_statistics_response import GetStatisticsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get statistics - weekly
        api_response = api_instance.get_statistics(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**GetStatisticsResponse**](GetStatisticsResponse.md)

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

# **get_statistics_daily**
> GetStatisticsDailyResponse get_statistics_daily(start_date, end_date, start_week, end_week, start_month, end_month)

Get statistics - daily

## Get statistics  Retrieves the daily, weekly or monthly statistics of an announcement or an announcement group.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-statistics ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.get_statistics_daily_response import GetStatisticsDailyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    start_date = "start_date_example" # str | 
    end_date = "end_date_example" # str | 
    start_week = "start_week_example" # str | 
    end_week = "end_week_example" # str | 
    start_month = "start_month_example" # str | 
    end_month = "end_month_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    announcement_group = "announcement_group_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get statistics - daily
        api_response = api_instance.get_statistics_daily(start_date, end_date, start_week, end_week, start_month, end_month)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_statistics_daily: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get statistics - daily
        api_response = api_instance.get_statistics_daily(start_date, end_date, start_week, end_week, start_month, end_month, api_token=api_token, announcement_group=announcement_group)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_statistics_daily: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  |
 **end_date** | **str**|  |
 **start_week** | **str**|  |
 **end_week** | **str**|  |
 **start_month** | **str**|  |
 **end_month** | **str**|  |
 **api_token** | **str**|  | [optional]
 **announcement_group** | **str**|  | [optional]

### Return type

[**GetStatisticsDailyResponse**](GetStatisticsDailyResponse.md)

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

# **get_statistics_monthly**
> GetStatisticsMonthlyResponse get_statistics_monthly()

Get statistics - monthly

## Get statistics  Retrieves the daily, weekly or monthly statistics of an announcement or an announcement group.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-get-statistics ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.get_statistics_monthly_response import GetStatisticsMonthlyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get statistics - monthly
        api_response = api_instance.get_statistics_monthly(api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->get_statistics_monthly: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]

### Return type

[**GetStatisticsMonthlyResponse**](GetStatisticsMonthlyResponse.md)

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

# **list_announcement_groups**
> ListAnnouncementGroupsResponse list_announcement_groups()

List announcement groups

## List announcement groups  Retrieves a list of announcement groups.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-list-announcement-groups ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.list_announcement_groups_response import ListAnnouncementGroupsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List announcement groups
        api_response = api_instance.list_announcement_groups(api_token=api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->list_announcement_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ListAnnouncementGroupsResponse**](ListAnnouncementGroupsResponse.md)

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

# **schedule_announcement**
> ScheduleAnnouncementResponse schedule_announcement()

Schedule an announcement

## Schedule an announcement  Schedules a new announcement. You can also schedule an announcement in the [Sendbird Dashboard](https://dashboard.sendbird.com).  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-schedule-an-announcement

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.schedule_announcement_response import ScheduleAnnouncementResponse
from sendbird_platform_sdk.model.schedule_announcement_data import ScheduleAnnouncementData
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    schedule_announcement_data = ScheduleAnnouncementData(
        message=ScheduleAnnouncementDataMessage(
            type="type_example",
            user_id="user_id_example",
            content="content_example",
        ),
        message_type="message_type_example",
        user_id="user_id_example",
        content="content_example",
        target_at="target_at_example",
        target_list=[
            "target_list_example",
        ],
        target_channel_type="target_channel_type_example",
        unique_id="unique_id_example",
        message_custom_type="message_custom_type_example",
        message_data="message_data_example",
        create_channel=True,
        announcement_group="announcement_group_example",
        create_channel_options="create_channel_options_example",
        create_channel_options_name="create_channel_options_name_example",
        create_channel_options_cover_url="create_channel_options_cover_url_example",
        create_channel_options_custom_type="create_channel_options_custom_type_example",
        create_channel_options_data="create_channel_options_data_example",
        create_channel_options_distinct="create_channel_options_distinct_example",
        scheduled_at=1,
        cease_at="cease_at_example",
        resume_at="resume_at_example",
        end_at=1,
        enable_push=True,
        assign_sender_as_channel_inviter=True,
    ) # ScheduleAnnouncementData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedule an announcement
        api_response = api_instance.schedule_announcement(api_token=api_token, schedule_announcement_data=schedule_announcement_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->schedule_announcement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **schedule_announcement_data** | [**ScheduleAnnouncementData**](ScheduleAnnouncementData.md)|  | [optional]

### Return type

[**ScheduleAnnouncementResponse**](ScheduleAnnouncementResponse.md)

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

# **update_announcement_by_id**
> UpdateAnnouncementByIdResponse update_announcement_by_id(unique_id)

Update an announcement

## Update an announcement  Updates information of a specific announcement before it starts or changes the status of a specific announcement after it starts. For the 2 different applications, refer to the request body below.  >__Note__: Updating information of an announcement is possible only when the announcement status is scheduled, indicating it hasn't started yet.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-update-an-announcement ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.update_announcement_by_id_data import UpdateAnnouncementByIdData
from sendbird_platform_sdk.model.update_announcement_by_id_response import UpdateAnnouncementByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    unique_id = "unique_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    update_announcement_by_id_data = UpdateAnnouncementByIdData(
        unique_id="unique_id_example",
        action="action_example",
        announcement_group="announcement_group_example",
        create_channel=True,
        create_channel_options_name="create_channel_options_name_example",
        create_channel_options_cover_url="create_channel_options_cover_url_example",
        create_channel_options_custom_type="create_channel_options_custom_type_example",
        create_channel_options_data="create_channel_options_data_example",
        create_channel_options_distinct="create_channel_options_distinct_example",
        message_user_id="message_user_id_example",
        message_content="message_content_example",
        message_data="message_data_example",
        enable_push=True,
        scheduled_at=1,
        end_at=1,
        cease_at="cease_at_example",
        resume_at="resume_at_example",
    ) # UpdateAnnouncementByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an announcement
        api_response = api_instance.update_announcement_by_id(unique_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->update_announcement_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an announcement
        api_response = api_instance.update_announcement_by_id(unique_id, api_token=api_token, update_announcement_by_id_data=update_announcement_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->update_announcement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**|  |
 **api_token** | **str**|  | [optional]
 **update_announcement_by_id_data** | [**UpdateAnnouncementByIdData**](UpdateAnnouncementByIdData.md)|  | [optional]

### Return type

[**UpdateAnnouncementByIdResponse**](UpdateAnnouncementByIdResponse.md)

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

# **view_announcement_by_id**
> ViewAnnouncementByIdResponse view_announcement_by_id(unique_id)

View an announcement

## View an announcement  Retrieves information on a specific announcement.  https://sendbird.com/docs/chat/v3/platform-api/guides/announcements#2-view-an-announcement ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.view_announcement_by_id_response import ViewAnnouncementByIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = announcement_api.AnnouncementApi(api_client)
    unique_id = "unique_id_example" # str | 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View an announcement
        api_response = api_instance.view_announcement_by_id(unique_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->view_announcement_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View an announcement
        api_response = api_instance.view_announcement_by_id(unique_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->view_announcement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**ViewAnnouncementByIdResponse**](ViewAnnouncementByIdResponse.md)

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

