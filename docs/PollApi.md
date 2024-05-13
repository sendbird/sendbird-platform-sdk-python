# sendbird_platform_sdk.PollApi

All URIs are relative to *https://api-APP_ID.sendbird.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_polls_get**](PollApi.md#v3_polls_get) | **GET** /v3/polls | List polls
[**v3_polls_poll_id_close_put**](PollApi.md#v3_polls_poll_id_close_put) | **PUT** /v3/polls/{poll_id}/close | Close a poll
[**v3_polls_poll_id_delete**](PollApi.md#v3_polls_poll_id_delete) | **DELETE** /v3/polls/{poll_id} | Delete a poll
[**v3_polls_poll_id_get**](PollApi.md#v3_polls_poll_id_get) | **GET** /v3/polls/{poll_id} | Get a poll
[**v3_polls_poll_id_options_option_id_delete**](PollApi.md#v3_polls_poll_id_options_option_id_delete) | **DELETE** /v3/polls/{poll_id}/options/{option_id} | Delete a poll option
[**v3_polls_poll_id_options_option_id_get**](PollApi.md#v3_polls_poll_id_options_option_id_get) | **GET** /v3/polls/{poll_id}/options/{option_id} | Get a poll option
[**v3_polls_poll_id_options_option_id_put**](PollApi.md#v3_polls_poll_id_options_option_id_put) | **PUT** /v3/polls/{poll_id}/options/{option_id} | Update a poll option
[**v3_polls_poll_id_options_option_id_voters_get**](PollApi.md#v3_polls_poll_id_options_option_id_voters_get) | **GET** /v3/polls/{poll_id}/options/{option_id}/voters | List voters of a poll option
[**v3_polls_poll_id_options_post**](PollApi.md#v3_polls_poll_id_options_post) | **POST** /v3/polls/{poll_id}/options | Add a poll option
[**v3_polls_poll_id_put**](PollApi.md#v3_polls_poll_id_put) | **PUT** /v3/polls/{poll_id} | Update a poll
[**v3_polls_poll_id_vote_put**](PollApi.md#v3_polls_poll_id_vote_put) | **PUT** /v3/polls/{poll_id}/vote | Cast or cancel a vote
[**v3_polls_post**](PollApi.md#v3_polls_post) | **POST** /v3/polls | Create a poll


# **v3_polls_get**
> SendBirdPoll v3_polls_get()

List polls

## List polls This action retrieves a paginated list of both open and closed polls in an application or a specific channel. To retrieve polls in a specific channel, the channel_url must be specified. https://sendbird.com/docs/chat/v3/platform-api/message/polls/list-polls  -----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.send_bird_poll import SendBirdPoll
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    api_token = "Api-Token_example" # str |  (optional)
    channel_url = "channel_url_example" # str |  (optional)
    channel_type = "channel_type_example" # str |  (optional)
    token = "token_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List polls
        api_response = api_instance.v3_polls_get(api_token=api_token, channel_url=channel_url, channel_type=channel_type, token=token, limit=limit)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**|  | [optional]
 **channel_url** | **str**|  | [optional]
 **channel_type** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**SendBirdPoll**](SendBirdPoll.md)

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

# **v3_polls_poll_id_close_put**
> SendBirdPoll v3_polls_poll_id_close_put(poll_id)

Close a poll

## Close a poll This action closes a poll and prevents users from voting any further. https://sendbird.com/docs/chat/v3/platform-api/message/polls/close-a-poll -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.send_bird_poll import SendBirdPoll
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Close a poll
        api_response = api_instance.v3_polls_poll_id_close_put(poll_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_close_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Close a poll
        api_response = api_instance.v3_polls_poll_id_close_put(poll_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_close_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**SendBirdPoll**](SendBirdPoll.md)

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

# **v3_polls_poll_id_delete**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v3_polls_poll_id_delete(poll_id)

Delete a poll

## Delete a poll This action deletes a poll. Once a poll is deleted, you can't retrieve its data. https://sendbird.com/docs/chat/v3/platform-api/message/polls/delete-a-poll -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a poll
        api_response = api_instance.v3_polls_poll_id_delete(poll_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a poll
        api_response = api_instance.v3_polls_poll_id_delete(poll_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
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

# **v3_polls_poll_id_get**
> SendBirdPoll v3_polls_poll_id_get(poll_id)

Get a poll

## Get a poll This action retrieves information on a specific poll. https://sendbird.com/docs/chat/v3/platform-api/message/polls/get-a-poll -----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.v3_polls_poll_id_delete_request import V3PollsPollIdDeleteRequest
from sendbird_platform_sdk.model.send_bird_poll import SendBirdPoll
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_polls_poll_id_delete_request = V3PollsPollIdDeleteRequest(
        channel_url="channel_url_example",
        channel_type="channel_type_example",
        show_partial_voter_list=True,
    ) # V3PollsPollIdDeleteRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a poll
        api_response = api_instance.v3_polls_poll_id_get(poll_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a poll
        api_response = api_instance.v3_polls_poll_id_get(poll_id, api_token=api_token, v3_polls_poll_id_delete_request=v3_polls_poll_id_delete_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **api_token** | **str**|  | [optional]
 **v3_polls_poll_id_delete_request** | [**V3PollsPollIdDeleteRequest**](V3PollsPollIdDeleteRequest.md)|  | [optional]

### Return type

[**SendBirdPoll**](SendBirdPoll.md)

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

# **v3_polls_poll_id_options_option_id_delete**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v3_polls_poll_id_options_option_id_delete(poll_id, option_id)

Delete a poll option

## Delete a poll option This action deletes an option from a poll. https://sendbird.com/docs/chat/v3/platform-api/message/polls/delete-a-poll-option ----------------------------- 

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    option_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a poll option
        api_response = api_instance.v3_polls_poll_id_options_option_id_delete(poll_id, option_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_option_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a poll option
        api_response = api_instance.v3_polls_poll_id_options_option_id_delete(poll_id, option_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_option_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **option_id** | **int**|  |
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

# **v3_polls_poll_id_options_option_id_get**
> SendBirdPollOption v3_polls_poll_id_options_option_id_get(poll_id, option_id)

Get a poll option

## Get a poll option This action retrieves a poll option. https://sendbird.com/docs/chat/v3/platform-api/message/polls/get-a-poll-option -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.send_bird_poll_option import SendBirdPollOption
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    option_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a poll option
        api_response = api_instance.v3_polls_poll_id_options_option_id_get(poll_id, option_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_option_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a poll option
        api_response = api_instance.v3_polls_poll_id_options_option_id_get(poll_id, option_id, api_token=api_token)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_option_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **option_id** | **int**|  |
 **api_token** | **str**|  | [optional]

### Return type

[**SendBirdPollOption**](SendBirdPollOption.md)

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

# **v3_polls_poll_id_options_option_id_put**
> SendBirdPoll v3_polls_poll_id_options_option_id_put(poll_id, option_id)

Update a poll option

## Update a poll option This action updates the content of a poll option. Voting for an option doesn't update the option. https://sendbird.com/docs/chat/v3/platform-api/message/polls/update-a-poll-option -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.v3_polls_poll_id_options_option_id_delete_request import V3PollsPollIdOptionsOptionIdDeleteRequest
from sendbird_platform_sdk.model.send_bird_poll import SendBirdPoll
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    option_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_polls_poll_id_options_option_id_delete_request = V3PollsPollIdOptionsOptionIdDeleteRequest(
        text="text_example",
        created_by="created_by_example",
    ) # V3PollsPollIdOptionsOptionIdDeleteRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a poll option
        api_response = api_instance.v3_polls_poll_id_options_option_id_put(poll_id, option_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_option_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a poll option
        api_response = api_instance.v3_polls_poll_id_options_option_id_put(poll_id, option_id, api_token=api_token, v3_polls_poll_id_options_option_id_delete_request=v3_polls_poll_id_options_option_id_delete_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_option_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **option_id** | **int**|  |
 **api_token** | **str**|  | [optional]
 **v3_polls_poll_id_options_option_id_delete_request** | [**V3PollsPollIdOptionsOptionIdDeleteRequest**](V3PollsPollIdOptionsOptionIdDeleteRequest.md)|  | [optional]

### Return type

[**SendBirdPoll**](SendBirdPoll.md)

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

# **v3_polls_poll_id_options_option_id_voters_get**
> V3PollsPollIdOptionsOptionIdVotersGet200Response v3_polls_poll_id_options_option_id_voters_get(poll_id, option_id)

List voters of a poll option

## List voters of a poll option This action retrieves a list of users who voted for a poll option. https://sendbird.com/docs/chat/v3/platform-api/message/polls/list-voters-of-a-poll-option  -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.v3_polls_poll_id_options_option_id_voters_get_request import V3PollsPollIdOptionsOptionIdVotersGetRequest
from sendbird_platform_sdk.model.v3_polls_poll_id_options_option_id_voters_get200_response import V3PollsPollIdOptionsOptionIdVotersGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    option_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_polls_poll_id_options_option_id_voters_get_request = V3PollsPollIdOptionsOptionIdVotersGetRequest(
        token="token_example",
        limit=1,
    ) # V3PollsPollIdOptionsOptionIdVotersGetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List voters of a poll option
        api_response = api_instance.v3_polls_poll_id_options_option_id_voters_get(poll_id, option_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_option_id_voters_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List voters of a poll option
        api_response = api_instance.v3_polls_poll_id_options_option_id_voters_get(poll_id, option_id, api_token=api_token, v3_polls_poll_id_options_option_id_voters_get_request=v3_polls_poll_id_options_option_id_voters_get_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_option_id_voters_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **option_id** | **int**|  |
 **api_token** | **str**|  | [optional]
 **v3_polls_poll_id_options_option_id_voters_get_request** | [**V3PollsPollIdOptionsOptionIdVotersGetRequest**](V3PollsPollIdOptionsOptionIdVotersGetRequest.md)|  | [optional]

### Return type

[**V3PollsPollIdOptionsOptionIdVotersGet200Response**](V3PollsPollIdOptionsOptionIdVotersGet200Response.md)

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

# **v3_polls_poll_id_options_post**
> SendBirdPoll v3_polls_poll_id_options_post(poll_id)

Add a poll option

## Add a poll option This action adds a new option to a poll. https://sendbird.com/docs/chat/v3/platform-api/message/polls/add-a-poll-option -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.v3_polls_poll_id_options_option_id_delete_request import V3PollsPollIdOptionsOptionIdDeleteRequest
from sendbird_platform_sdk.model.send_bird_poll import SendBirdPoll
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_polls_poll_id_options_option_id_delete_request = V3PollsPollIdOptionsOptionIdDeleteRequest(
        text="text_example",
        created_by="created_by_example",
    ) # V3PollsPollIdOptionsOptionIdDeleteRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a poll option
        api_response = api_instance.v3_polls_poll_id_options_post(poll_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a poll option
        api_response = api_instance.v3_polls_poll_id_options_post(poll_id, api_token=api_token, v3_polls_poll_id_options_option_id_delete_request=v3_polls_poll_id_options_option_id_delete_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_options_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **api_token** | **str**|  | [optional]
 **v3_polls_poll_id_options_option_id_delete_request** | [**V3PollsPollIdOptionsOptionIdDeleteRequest**](V3PollsPollIdOptionsOptionIdDeleteRequest.md)|  | [optional]

### Return type

[**SendBirdPoll**](SendBirdPoll.md)

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

# **v3_polls_poll_id_put**
> SendBirdPoll v3_polls_poll_id_put(poll_id)

Update a poll

## Update a poll This action updates information of a poll. To change the content of a poll option, see the update a poll option page. https://sendbird.com/docs/chat/v3/platform-api/message/polls/update-a-poll -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.v3_polls_poll_id_delete_request1 import V3PollsPollIdDeleteRequest1
from sendbird_platform_sdk.model.send_bird_poll import SendBirdPoll
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_polls_poll_id_delete_request1 = V3PollsPollIdDeleteRequest1(
        title="title_example",
        allow_user_suggestion=True,
        allow_multiple_votes=True,
null,
        allocreated_byw_multiple_votes="allocreated_byw_multiple_votes_example",
        data={},
    ) # V3PollsPollIdDeleteRequest1 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a poll
        api_response = api_instance.v3_polls_poll_id_put(poll_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a poll
        api_response = api_instance.v3_polls_poll_id_put(poll_id, api_token=api_token, v3_polls_poll_id_delete_request1=v3_polls_poll_id_delete_request1)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **api_token** | **str**|  | [optional]
 **v3_polls_poll_id_delete_request1** | [**V3PollsPollIdDeleteRequest1**](V3PollsPollIdDeleteRequest1.md)|  | [optional]

### Return type

[**SendBirdPoll**](SendBirdPoll.md)

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

# **v3_polls_poll_id_vote_put**
> SendBirdPoll v3_polls_poll_id_vote_put(poll_id)

Cast or cancel a vote

## Cast or cancel a vote This action adds or removes a vote from a poll option, changing the number of votes given to each option. Use this action to override a previous vote and update the user's final choice of poll options. https://sendbird.com/docs/chat/v3/platform-api/message/polls/cast-or-cancel-a-vote -----------------------------  

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.v3_polls_poll_id_vote_put_request import V3PollsPollIdVotePutRequest
from sendbird_platform_sdk.model.send_bird_poll import SendBirdPoll
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    poll_id = 1 # int | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_polls_poll_id_vote_put_request = V3PollsPollIdVotePutRequest(
        user_id="user_id_example",
        option_ids=[
            1,
        ],
    ) # V3PollsPollIdVotePutRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cast or cancel a vote
        api_response = api_instance.v3_polls_poll_id_vote_put(poll_id)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_vote_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cast or cancel a vote
        api_response = api_instance.v3_polls_poll_id_vote_put(poll_id, api_token=api_token, v3_polls_poll_id_vote_put_request=v3_polls_poll_id_vote_put_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_poll_id_vote_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **int**|  |
 **api_token** | **str**|  | [optional]
 **v3_polls_poll_id_vote_put_request** | [**V3PollsPollIdVotePutRequest**](V3PollsPollIdVotePutRequest.md)|  | [optional]

### Return type

[**SendBirdPoll**](SendBirdPoll.md)

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

# **v3_polls_post**
> SendBirdPoll v3_polls_post(title, options)

Create a poll

## Create a poll This action creates a poll with at least one option.You can configure various settings for your poll, including when the poll will close and whether to allow voting for multiple options. After creating a poll, to share the poll with other users in a channel, the poll must be sent as a message. https://sendbird.com/docs/chat/v3/platform-api/message/polls/create-a-poll -----------------------------

### Example


```python
import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import poll_api
from sendbird_platform_sdk.model.send_bird_poll import SendBirdPoll
from sendbird_platform_sdk.model.v3_polls_get_request import V3PollsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = poll_api.PollApi(api_client)
    title = "title_example" # str | 
    options = [
        "options_example",
    ] # [str] | 
    api_token = "Api-Token_example" # str |  (optional)
    v3_polls_get_request = V3PollsGetRequest(
        title="title_example",
        options=[
            "options_example",
        ],
        allow_user_suggestion=True,
        allow_multiple_votes=True,
null,
        created_by="created_by_example",
        data={},
    ) # V3PollsGetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a poll
        api_response = api_instance.v3_polls_post(title, options)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a poll
        api_response = api_instance.v3_polls_post(title, options, api_token=api_token, v3_polls_get_request=v3_polls_get_request)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling PollApi->v3_polls_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  |
 **options** | **[str]**|  |
 **api_token** | **str**|  | [optional]
 **v3_polls_get_request** | [**V3PollsGetRequest**](V3PollsGetRequest.md)|  | [optional]

### Return type

[**SendBirdPoll**](SendBirdPoll.md)

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

