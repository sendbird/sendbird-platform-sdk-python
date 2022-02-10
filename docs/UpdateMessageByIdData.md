# UpdateMessageByIdData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **int** | Specifies the unique ID of the message to update. | 
**channel_type** | **str** | Specifies the type of the channel. Either open_channels or group_channels. | [optional] 
**channel_url** | **str** | Specifies the URL of the target channel. | [optional] 
**message_type** | **str** | Specifies the type of the message as ADMM. | [optional] 
**message** | **str** | Specifies the content of the message. | [optional] 
**custom_type** | **str** | Specifies a custom message type which is used for message grouping. The length is limited to 128 characters.&lt;br /&gt;&lt;br /&gt; Custom types are also used within Sendbird&#39;s [Advanced analytics](/docs/chat/v3/platform-api/guides/advanced-analytics) to segment metrics, which enables the sub-classification of data views. | [optional] 
**data** | **str** | Specifies additional message information such as custom font size, font type or &#x60;JSON&#x60; formatted string. | [optional] 
**mention_type** | **str** | Specifies the mentioning method which indicates the user scope who will get a notification for the message. Acceptable values are users and channel. If set to users, only the specified users with the mentioned_users property below will get notified. If set to channel, all users in the channel will get notified. (Default: users) | [optional] 
**mentioned_user_ids** | **[int]** | Specifies an array of one or more IDs of the users who will get a notification for the message. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


