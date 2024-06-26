# GcInviteAsMembersData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_url** | **str** | Specifies the URL of the channel to invite into. | 
**user_ids** | **[str]** | Specifies an array of one or more user IDs to invite into the channel. The maximum number of users to be invited at once is 100. The users can be used instead of this property. | 
**users** | **[str]** | Specifies a list of one or more &#x60;JSON&#x60; objects which contain the user_id property to invite into the channel. The maximum number of users to be invited at once is 100. The user_ids can be used instead of this property. | [optional] 
**invitation_status** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies one or more key-value pair items which set the invitation status of each user invited to the channel. The key should be a user_id and the value should be their joining status. Acceptable values are joined, invited_by_friend, and invited_by_non_friend. (Default: joined) | [optional] 
**hidden_status** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies one or more key-value pair items which set the channel&#39;s hidden status for each user. The key should be a user_id and the value should be their hidden status. Acceptable values are limited to the following:&lt;br /&gt;- unhidden (default): the channel is included in when retrieving a list of group channels.&lt;br /&gt;- hidden_allow_auto_unhide: the channel automatically gets unhidden when receiving a new message.&lt;br /&gt;- hidden_prevent_auto_unhide: the channel keeps hidden though receiving a new message. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


