# sendbird_platform_sdk.AnnouncementApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedule_an_announcement**](AnnouncementApi.md#schedule_an_announcement) | **POST** /v3/announcements | Schedule an announcement


# **schedule_an_announcement**
> ScheduleAnAnnouncementResponse schedule_an_announcement()

Schedule an announcement

## Schedule an announcement  Creates an announcement. You can also schedule an announcement in the [Sendbird Dashboard](https://dashboard.sendbird.com).  [https://sendbird.com/docs/chat/platform-api/v3/message/announcements/create-an-announcement#1-create-an-announcement](https://sendbird.com/docs/chat/platform-api/v3/message/announcements/create-an-announcement#1-create-an-announcement)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import announcement_api
from sendbird_platform_sdk.model.schedule_an_announcement_response import ScheduleAnAnnouncementResponse
from sendbird_platform_sdk.model.schedule_an_announcement_request import ScheduleAnAnnouncementRequest
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
    schedule_an_announcement_request = ScheduleAnAnnouncementRequest(
        announcement_group="announcement_group_example",
        assign_sender_as_channel_inviter=True,
        cease_at="cease_at_example",
        create_channel=True,
        create_channel_options=ScheduleAnAnnouncementRequestCreateChannelOptions(
            cover_url="cover_url_example",
            custom_type="custom_type_example",
            data="data_example",
            distinct=True,
            name="name_example",
        ),
        enable_push=True,
        end_at=1,
        keep_channel_hidden_for_sender=True,
        mark_as_read=True,
        message=ScheduleAnAnnouncementRequestMessage(
            content="content_example",
            custom_type="custom_type_example",
            data="data_example",
            type="type_example",
            user_id="user_id_example",
        ),
        resume_at="resume_at_example",
        scheduled_at=1,
        send_to_frozen_channels=True,
        target_at="target_at_example",
        target_channel_type="target_channel_type_example",
        target_custom_type="target_custom_type_example",
        target_list=[
            "target_list_example",
        ],
        unique_id="unique_id_example",
    ) # ScheduleAnAnnouncementRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedule an announcement
        api_response = api_instance.schedule_an_announcement(api_token=api_token, schedule_an_announcement_request=schedule_an_announcement_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling AnnouncementApi->schedule_an_announcement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **schedule_an_announcement_request** | [**ScheduleAnAnnouncementRequest**](ScheduleAnAnnouncementRequest.md)|  | [optional]

### Return type

[**ScheduleAnAnnouncementResponse**](ScheduleAnAnnouncementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

