# CreateAGroupChannelRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**[SendbirdUser]**](SendbirdUser.md) |  | 
**access_code** | **str, none_type** |  | [optional] 
**block_sdk_user_channel_join** | **bool, none_type** |  | [optional] 
**channel_url** | **str** |  | [optional] 
**cover_file** | **file_type** | Uploads a file for the channel cover image. | [optional] 
**cover_url** | **str** |  | [optional] 
**custom_type** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**hidden_status** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies one or more key-value pair items which set the channel&#39;s hidden status for each user. The key should be a user_id and the value should be their hidden status. Acceptable values are limited to the following:&lt;br /&gt;- unhidden (default): the channel is included in when retrieving a list of group channels.&lt;br /&gt;- hidden_allow_auto_unhide: the channel automatically gets unhidden when receiving a new message.&lt;br /&gt;- hidden_prevent_auto_unhide: the channel keeps hidden though receiving a new message. | [optional] 
**invitation_status** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies one or more key-value pair items which set the invitation status of each user invited to the channel. The key should be a user_id and the value should be their joining status. Acceptable values are joined, invited_by_friend, and invited_by_non_friend. (Default: joined) | [optional] 
**inviter_id** | **str** |  | [optional] 
**is_distinct** | **bool** |  | [optional] 
**is_ephemeral** | **bool** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**is_super** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**operator_ids** | **[str]** |  | [optional] 
**strict** | **bool** |  | [optional] 
**user_ids** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


