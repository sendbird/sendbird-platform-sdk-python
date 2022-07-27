# sendbird_platform_sdk.BotApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bot**](BotApi.md#create_bot) | **POST** /v3/bots | Create a bot
[**delete_bot_by_id**](BotApi.md#delete_bot_by_id) | **DELETE** /v3/bots/{bot_userid} | Delete a bot
[**join_channels**](BotApi.md#join_channels) | **POST** /v3/bots/{bot_userid}/channels | Join channels
[**leave_channels**](BotApi.md#leave_channels) | **DELETE** /v3/bots/{bot_userid}/channels | Leave channels - When leaving all channels
[**leave_channels_by_url**](BotApi.md#leave_channels_by_url) | **DELETE** /v3/bots/{bot_userid}/channels/{channel_url} | Leave channels - When leaving a channel by its channel URL
[**list_bots**](BotApi.md#list_bots) | **GET** /v3/bots | List bots
[**send_bots_message**](BotApi.md#send_bots_message) | **POST** /v3/bots/{bot_userid}/send | Send a bot&#39;s message
[**update_bot_by_id**](BotApi.md#update_bot_by_id) | **PUT** /v3/bots/{bot_userid} | Update a bot
[**view_bot_by_id**](BotApi.md#view_bot_by_id) | **GET** /v3/bots/{bot_userid} | View a bot


# **create_bot**
> CreateBotResponse create_bot(api_token)

Create a bot

## Create a bot  Creates a new bot within the application. Creating a bot is similar to creating a normal user, except that a callback URL is specified in order for the bot to receive events.  > __Note__: The bot must [join](#2-join-channels) a group channel first to interact with users. In group channels, you can invite a bot through the [invite as members](https://sendbird.com/docs/chat/v3/platform-api/guides/group-channel#2-invite-as-members) action instead.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-create-a-bot

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.create_bot_response import CreateBotResponse
from sendbird_platform_sdk.model.create_bot_data import CreateBotData
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
    api_token = "{{API_TOKEN}}" # str | 
    create_bot_data = CreateBotData(
        bot_userid="bot_userid_example",
        bot_nickname="bot_nickname_example",
        bot_profile_url="bot_profile_url_example",
        bot_type="bot_type_example",
        bot_callback_url="bot_callback_url_example",
        is_privacy_mode=True,
        enable_mark_as_read=True,
        show_member=True,
        channel_invitation_preference=1,
    ) # CreateBotData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a bot
        api_response = api_instance.create_bot(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->create_bot: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a bot
        api_response = api_instance.create_bot(api_token, create_bot_data=create_bot_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->create_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **create_bot_data** | [**CreateBotData**](CreateBotData.md)|  | [optional]

### Return type

[**CreateBotResponse**](CreateBotResponse.md)

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

# **delete_bot_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_bot_by_id(api_token, bot_userid)

Delete a bot

## Delete a bot  Deletes a bot from an application.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-delete-a-bot ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    bot_userid = "bot_userid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a bot
        api_response = api_instance.delete_bot_by_id(api_token, bot_userid)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->delete_bot_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **bot_userid** | **str**|  |

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

# **join_channels**
> JoinChannelsResponse join_channels(api_token, bot_userid)

Join channels

## Join channels  Makes a bot join one or more channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-join-channels ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.join_channels_data import JoinChannelsData
from sendbird_platform_sdk.model.join_channels_response import JoinChannelsResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    bot_userid = "bot_userid_example" # str | 
    join_channels_data = JoinChannelsData(
        bot_userid="bot_userid_example",
        channel_urls=[
            "channel_urls_example",
        ],
    ) # JoinChannelsData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Join channels
        api_response = api_instance.join_channels(api_token, bot_userid)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->join_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Join channels
        api_response = api_instance.join_channels(api_token, bot_userid, join_channels_data=join_channels_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->join_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **bot_userid** | **str**|  |
 **join_channels_data** | [**JoinChannelsData**](JoinChannelsData.md)|  | [optional]

### Return type

[**JoinChannelsResponse**](JoinChannelsResponse.md)

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

# **leave_channels**
> leave_channels(api_token, bot_userid)

Leave channels - When leaving all channels

## Leave channels  Makes a bot leave one or more group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-leave-channels ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    bot_userid = "bot_userid_example" # str | 
    channel_url = "channel_url_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Leave channels - When leaving all channels
        api_instance.leave_channels(api_token, bot_userid)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->leave_channels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Leave channels - When leaving all channels
        api_instance.leave_channels(api_token, bot_userid, channel_url=channel_url)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->leave_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **bot_userid** | **str**|  |
 **channel_url** | **str**|  | [optional]

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

# **leave_channels_by_url**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} leave_channels_by_url(api_token, bot_userid, channel_url)

Leave channels - When leaving a channel by its channel URL

## Leave channels  Makes a bot leave one or more group channels.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-leave-channels ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    bot_userid = "bot_userid_example" # str | 
    channel_url = "channel_url_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Leave channels - When leaving a channel by its channel URL
        api_response = api_instance.leave_channels_by_url(api_token, bot_userid, channel_url)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->leave_channels_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **bot_userid** | **str**|  |
 **channel_url** | **str**|  |

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
> ListBotsResponse list_bots(api_token)

List bots

## List bots  Retrieves a list of all bots within an application.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-list-bots ----------------------------

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
    api_token = "{{API_TOKEN}}" # str | 
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List bots
        api_response = api_instance.list_bots(api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->list_bots: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List bots
        api_response = api_instance.list_bots(api_token, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->list_bots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

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

# **send_bots_message**
> SendBirdMessageResponse send_bots_message(api_token, bot_userid)

Send a bot's message

## Send a bot's message  Sends a bot's message to a channel.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-send-a-bot-s-message ----------------------------   `bot_userid`      Type: string      Description: Specifies the ID of the bot to send a message.

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.send_bird_message_response import SendBirdMessageResponse
from sendbird_platform_sdk.model.send_bot_s_message_data import SendBotSMessageData
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
    api_token = "{{API_TOKEN}}" # str | 
    bot_userid = "bot_userid_example" # str | 
    send_bot_s_message_data = SendBotSMessageData(
        message="message_example",
        channel_url="channel_url_example",
        custom_type="custom_type_example",
        data="data_example",
        send_push=True,
        mentioned=[
            "mentioned_example",
        ],
        mark_as_read=True,
        dedup_id="dedup_id_example",
        created_at=1,
    ) # SendBotSMessageData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a bot's message
        api_response = api_instance.send_bots_message(api_token, bot_userid)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->send_bots_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a bot's message
        api_response = api_instance.send_bots_message(api_token, bot_userid, send_bot_s_message_data=send_bot_s_message_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->send_bots_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **bot_userid** | **str**|  |
 **send_bot_s_message_data** | [**SendBotSMessageData**](SendBotSMessageData.md)|  | [optional]

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

# **update_bot_by_id**
> UpdateBotByIdResponse update_bot_by_id(api_token, bot_userid)

Update a bot

## Update a bot  Updates information on a bot.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-update-a-bot ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.update_bot_by_id_data import UpdateBotByIdData
from sendbird_platform_sdk.model.update_bot_by_id_response import UpdateBotByIdResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    bot_userid = "bot_userid_example" # str | 
    update_bot_by_id_data = UpdateBotByIdData(
        bot_userid="bot_userid_example",
        bot_nickname="bot_nickname_example",
        bot_profile_url="bot_profile_url_example",
        bot_callback_url="bot_callback_url_example",
        is_privacy_mode=True,
        enable_mark_as_read=True,
        show_member=True,
        channel_invitation_preference=1,
    ) # UpdateBotByIdData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a bot
        api_response = api_instance.update_bot_by_id(api_token, bot_userid)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->update_bot_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a bot
        api_response = api_instance.update_bot_by_id(api_token, bot_userid, update_bot_by_id_data=update_bot_by_id_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->update_bot_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **bot_userid** | **str**|  |
 **update_bot_by_id_data** | [**UpdateBotByIdData**](UpdateBotByIdData.md)|  | [optional]

### Return type

[**UpdateBotByIdResponse**](UpdateBotByIdResponse.md)

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

# **view_bot_by_id**
> ViewBotByIdResponse view_bot_by_id(api_token, bot_userid)

View a bot

## View a bot  Retrieves information on a bot.  https://sendbird.com/docs/chat/v3/platform-api/guides/bot-interface#2-view-a-bot ----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import bot_api
from sendbird_platform_sdk.model.view_bot_by_id_response import ViewBotByIdResponse
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
    api_token = "{{API_TOKEN}}" # str | 
    bot_userid = "bot_userid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # View a bot
        api_response = api_instance.view_bot_by_id(api_token, bot_userid)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling BotApi->view_bot_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  |
 **bot_userid** | **str**|  |

### Return type

[**ViewBotByIdResponse**](ViewBotByIdResponse.md)

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

