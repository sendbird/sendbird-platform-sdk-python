# SendBotSMessageData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the content of the message sent by the bot. | 
**channel_url** | **str** | Specifies the URL of the channel where the message is sent to. | 
**custom_type** | **str** | Specifies a custom message type which is used for message grouping. The length is limited to 128 characters. | [optional] 
**data** | **str** | Specifies additional message information such as custom font size, font type or &#x60;JSON&#x60; formatted string. | [optional] 
**send_push** | **bool** | Determines whether to send a push notification for the message to the members of the channel (Default: true) | [optional] 
**mentioned** | **[str]** | Specifies an array of one or more IDs of the users who get a notification for the message. | [optional] 
**mark_as_read** | **bool** | Determines whether to mark the message as read for the bot. If set to false, the bot&#39;s unread_count and read_receipt remain unchanged after the message is sent. (Default: true) | [optional] 
**dedup_id** | **str** | Specifies the unique ID for the message to prevent the same message data from getting sent to the channel. | [optional] 
**created_at** | **int** | Specifies the time that the message was sent, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


