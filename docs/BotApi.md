# sendbird_platform_sdk.BotApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_bot**](BotApi.md#create_a_bot) | **POST** /v3/bots | Create a bot
[**join_channels**](BotApi.md#join_channels) | **POST** /v3/bots/{bot_userid}/channels | Join channels
[**leave_a_group_channel**](BotApi.md#leave_a_group_channel) | **DELETE** /v3/bots/{bot_userid}/channels/{channel_url} | Leave channels - When leaving a specific channel
[**leave_group_channels**](BotApi.md#leave_group_channels) | **DELETE** /v3/bots/{bot_userid}/channels | Leave channels - When leaving all channels
[**list_bots**](BotApi.md#list_bots) | **GET** /v3/bots | List bots
[**send_a_bot_message**](BotApi.md#send_a_bot_message) | **POST** /v3/bots/{bot_userid}/send | Send a bot&#39;s message


# **create_a_bot**
> CreateABotResponse create_a_bot()

Create a bot

## Create a bot  Creates a new bot within an application. Creating a bot is similar to creating a normal user, except a callback URL should be specified for a bot to receive events.  > **Note**: The bot must first [join a group channel](https://sendbird.com/docs/chat/platform-api/v3/bot/managing-a-bot/join-channels) to interact with users. In group channels, you can also invite a bot through the [invite as members](https://sendbird.com/docs/chat/platform-api/v3/channel/inviting-a-user/invite-as-members-channel) action.      [https://sendbird.com/docs/chat/platform-api/v3/bot/creating-a-bot/create-a-bot#1-create-a-bot](https://sendbird.com/docs/chat/platform-api/v3/bot/creating-a-bot/create-a-bot#1-create-a-bot)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.create_a_bot_response import CreateABotResponse
from sendbird_platform_sdk.model.create_a_bot_request import CreateABotRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bot_api.BotApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)
    create_a_bot_request = CreateABotRequest(
        bot_callback_url="bot_callback_url_example",
        bot_nickname="bot_nickname_example",
        bot_profile_url="bot_profile_url_example",
        bot_type="bot_type_example",
        bot_userid="bot_userid_example",
        is_privacy_mode=True,
        channel_invitation_preference=1,
        enable_mark_as_read=True,
        show_member=True,
    ) # CreateABotRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a bot
        api_response = api_instance.create_a_bot(api_token=api_token, create_a_bot_request=create_a_bot_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->create_a_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **create_a_bot_request** | [**CreateABotRequest**](CreateABotRequest.md)|  | [optional]

### Return type

[**CreateABotResponse**](CreateABotResponse.md)

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

# **join_channels**
> SendbirdGroupChannelDetail join_channels(bot_userid)

Join channels

## Join channels  Makes a bot join one or more group channels.  [https://sendbird.com/docs/chat/platform-api/v3/bot/managing-a-bot/join-channels#1-join-channels](https://sendbird.com/docs/chat/platform-api/v3/bot/managing-a-bot/join-channels#1-join-channels)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.sendbird_group_channel_detail import SendbirdGroupChannelDetail
from sendbird_platform_sdk.model.join_channels_request import JoinChannelsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bot_api.BotApi(api_client)
    bot_userid = "bot_userid_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)
    join_channels_request = JoinChannelsRequest(
        channel_urls=[
            "channel_urls_example",
        ],
    ) # JoinChannelsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Join channels
        api_response = api_instance.join_channels(bot_userid)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->join_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Join channels
        api_response = api_instance.join_channels(bot_userid, api_token=api_token, join_channels_request=join_channels_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->join_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_userid** | **str**| (Required)  |
 **api_token** | **str**|  | [optional]
 **join_channels_request** | [**JoinChannelsRequest**](JoinChannelsRequest.md)|  | [optional]

### Return type

[**SendbirdGroupChannelDetail**](SendbirdGroupChannelDetail.md)

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

# **leave_a_group_channel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} leave_a_group_channel(channel_url, bot_userid)

Leave channels - When leaving a specific channel

## Leave channels  Makes a bot leave a specific channel  [https://sendbird.com/docs/chat/platform-api/v3/bot/managing-a-bot/leave-channels#1-leave-channels](https://sendbird.com/docs/chat/platform-api/v3/bot/managing-a-bot/leave-channels#1-leave-channels)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bot_api.BotApi(api_client)
    channel_url = "channel_url_example" # str | 
    bot_userid = "bot_userid_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Leave channels - When leaving a specific channel
        api_response = api_instance.leave_a_group_channel(channel_url, bot_userid)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->leave_a_group_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Leave channels - When leaving a specific channel
        api_response = api_instance.leave_a_group_channel(channel_url, bot_userid, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->leave_a_group_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | **str**|  |
 **bot_userid** | **str**| (Required)  |
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

# **leave_group_channels**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} leave_group_channels(bot_userid)

Leave channels - When leaving all channels

## Leave channels  Makes a bot leave all group channels.  [https://sendbird.com/docs/chat/platform-api/v3/bot/managing-a-bot/leave-channels#1-leave-channels](https://sendbird.com/docs/chat/platform-api/v3/bot/managing-a-bot/leave-channels#1-leave-channels)

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bot_api.BotApi(api_client)
    bot_userid = "bot_userid_example" # str | (Required) 
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Leave channels - When leaving all channels
        api_response = api_instance.leave_group_channels(bot_userid)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->leave_group_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Leave channels - When leaving all channels
        api_response = api_instance.leave_group_channels(bot_userid, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->leave_group_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_userid** | **str**| (Required)  |
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

# **list_bots**
> ListBotsResponse list_bots()

List bots

## List bots  Retrieves a list of all bots within an application.  https://sendbird.com/docs/chat/platform-api/v3/bot/listing-bots/list-bots#1-list-bots

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.list_bots_response import ListBotsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bot_api.BotApi(api_client)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List bots
        api_response = api_instance.list_bots(token=token, limit=limit, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->list_bots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **api_token** | **str**|  | [optional]

### Return type

[**ListBotsResponse**](ListBotsResponse.md)

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

# **send_a_bot_message**
> SendABotMessageResponse send_a_bot_message(bot_userid, message_type, channel_url)

Send a bot's message

## Send a bot message  Sends a bot message to a group channel.  [https://sendbird.com/docs/chat/platform-api/v3/bot/sending-a-bot-message/send-a-bot-message#1-send-a-bot-message](https://sendbird.com/docs/chat/platform-api/v3/bot/sending-a-bot-message/send-a-bot-message#1-send-a-bot-message)  `bot_userid`   Type: string   Description: Specifies the ID of the bot to send a message.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.send_a_bot_message_response import SendABotMessageResponse
from sendbird_platform_sdk.model.sendbird_sorted_metaarray import SendbirdSortedMetaarray
from sendbird_platform_sdk.model.sendbird_extended_message_payload import SendbirdExtendedMessagePayload
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bot_api.BotApi(api_client)
    bot_userid = "bot_userid_example" # str | (Required) 
    message_type = "MESG" # str | Specifies the type of message to send. MESG for text message, FILE for file message.
    channel_url = "channel_url_example" # str | Specifies the URL of the channel to send the message to.
    api_token = "{{API_TOKEN}}" # str |  (optional)
    message = "message_example" # str | Specifies the content of the message. * This property is required when message_type is MESG. (optional)
    mentioned = [
        "mentioned_example",
    ] # [str] | * This property is available when message_type is MESG. (optional)
    extended_message_payload = SendbirdExtendedMessagePayload(
        custom_view={},
        suggested_replies=[
            "suggested_replies_example",
        ],
    ) # SendbirdExtendedMessagePayload |  (optional)
    file = open('/path/to/file', 'rb') # file_type | When sending a single file with a message, specifies the data of the file to upload to the Sendbird server in raw binary format. When sending a request containing a file, change the value of the content-type header to multipart/form-data;boundary={your_unique_boundary_string} in the request. * This property is required when message_type is FILE. * This doesn't allow a converted base64-encoded string from a file as its value. (optional)
    require_auth = True # bool | Determines whether to require an authentication key to verify if the file is being properly accessed. Only the user who uploaded the file or users who are in the channel where the file was uploaded should have access. The authentication key managed internally by the Sendbird system is generated every time a user logs in to the Sendbird server and is valid for three days starting from the last login. If set to false, Sendbird tries to access a file without any key. To access encrypted files, such as the files in the Sendbird server which are by default encrypted, the property must be set to true. (Default: false) The require_auth parameter only works if the file or URL is managed by Sendbird, which means that when you upload files using multipart format or provide URLs that point to the files hosted on the Sendbird server. However, if the file is hosted on a server or service that is not managed by Sendbird, access control and authentication for the file should be handled by the respective server or service hosting the file. * This property is available when message_type is FILE. (optional)
    mention_type = "users" # str | * This property is available when message_type is FILE. (optional)
    mentioned_user_ids = [
        "mentioned_user_ids_example",
    ] # [str] | * This property is available when message_type is FILE. (optional)
    is_silent = True # bool | * This property is available when message_type is FILE. (optional)
    sorted_metaarray = SendbirdSortedMetaarray([
        SendbirdSortedMetaarrayInner(
            key="key_example",
            value=[
                "value_example",
            ],
        ),
    ]) # SendbirdSortedMetaarray |  (optional)
    apns_bundle_id = "apns_bundle_id_example" # str | * This property is available when message_type is FILE. (optional)
    apple_critical_alert_options = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | * This property is available when message_type is FILE. (optional)
    sound = "sound_example" # str | * This property is available when message_type is FILE. (optional)
    volume = 3.14 # float | * This property is available when message_type is FILE. (optional)
    created_at = 1 # int |  (optional)
    custom_type = "custom_type_example" # str |  (optional)
    data = "data_example" # str |  (optional)
    dedup_id = "dedup_id_example" # str |  (optional)
    mark_as_read = True # bool |  (optional)
    send_push = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a bot's message
        api_response = api_instance.send_a_bot_message(bot_userid, message_type, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->send_a_bot_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a bot's message
        api_response = api_instance.send_a_bot_message(bot_userid, message_type, channel_url, api_token=api_token, message=message, mentioned=mentioned, extended_message_payload=extended_message_payload, file=file, require_auth=require_auth, mention_type=mention_type, mentioned_user_ids=mentioned_user_ids, is_silent=is_silent, sorted_metaarray=sorted_metaarray, apns_bundle_id=apns_bundle_id, apple_critical_alert_options=apple_critical_alert_options, sound=sound, volume=volume, created_at=created_at, custom_type=custom_type, data=data, dedup_id=dedup_id, mark_as_read=mark_as_read, send_push=send_push)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->send_a_bot_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_userid** | **str**| (Required)  |
 **message_type** | **str**| Specifies the type of message to send. MESG for text message, FILE for file message. |
 **channel_url** | **str**| Specifies the URL of the channel to send the message to. |
 **api_token** | **str**|  | [optional]
 **message** | **str**| Specifies the content of the message. * This property is required when message_type is MESG. | [optional]
 **mentioned** | **[str]**| * This property is available when message_type is MESG. | [optional]
 **extended_message_payload** | [**SendbirdExtendedMessagePayload**](SendbirdExtendedMessagePayload.md)|  | [optional]
 **file** | **file_type**| When sending a single file with a message, specifies the data of the file to upload to the Sendbird server in raw binary format. When sending a request containing a file, change the value of the content-type header to multipart/form-data;boundary&#x3D;{your_unique_boundary_string} in the request. * This property is required when message_type is FILE. * This doesn&#39;t allow a converted base64-encoded string from a file as its value. | [optional]
 **require_auth** | **bool**| Determines whether to require an authentication key to verify if the file is being properly accessed. Only the user who uploaded the file or users who are in the channel where the file was uploaded should have access. The authentication key managed internally by the Sendbird system is generated every time a user logs in to the Sendbird server and is valid for three days starting from the last login. If set to false, Sendbird tries to access a file without any key. To access encrypted files, such as the files in the Sendbird server which are by default encrypted, the property must be set to true. (Default: false) The require_auth parameter only works if the file or URL is managed by Sendbird, which means that when you upload files using multipart format or provide URLs that point to the files hosted on the Sendbird server. However, if the file is hosted on a server or service that is not managed by Sendbird, access control and authentication for the file should be handled by the respective server or service hosting the file. * This property is available when message_type is FILE. | [optional]
 **mention_type** | **str**| * This property is available when message_type is FILE. | [optional]
 **mentioned_user_ids** | **[str]**| * This property is available when message_type is FILE. | [optional]
 **is_silent** | **bool**| * This property is available when message_type is FILE. | [optional]
 **sorted_metaarray** | [**SendbirdSortedMetaarray**](SendbirdSortedMetaarray.md)|  | [optional]
 **apns_bundle_id** | **str**| * This property is available when message_type is FILE. | [optional]
 **apple_critical_alert_options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| * This property is available when message_type is FILE. | [optional]
 **sound** | **str**| * This property is available when message_type is FILE. | [optional]
 **volume** | **float**| * This property is available when message_type is FILE. | [optional]
 **created_at** | **int**|  | [optional]
 **custom_type** | **str**|  | [optional]
 **data** | **str**|  | [optional]
 **dedup_id** | **str**|  | [optional]
 **mark_as_read** | **bool**|  | [optional]
 **send_push** | **bool**|  | [optional]

### Return type

[**SendABotMessageResponse**](SendABotMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

