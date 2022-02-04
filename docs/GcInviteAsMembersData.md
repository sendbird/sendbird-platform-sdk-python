# GcInviteAsMembersData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_url** | **str** | Specifies the URL of the channel to invite into. | 
**user_ids** | **[int]** | Specifies an array of one or more user IDs to invite into the channel. The maximum number of users to be invited at once is 100. The users can be used instead of this property. | 
**users** | **[int]** | Specifies a list of one or more &#x60;JSON&#x60; objects which contain the user_id property to invite into the channel. The maximum number of users to be invited at once is 100. The user_ids can be used instead of this property. | 
**invitation_status** | **[str]** | Specifies an array of one or more information about the join status of each invited user to the channel. Each item of the array should be specified with a combination of the unique ID of a user in the user_ids or users property, a colon (:), and the user&#39;s join status (for example, user_id_1: join status). Acceptable values are joined, invited_by_friend, and invited_by_non_friend. (Default: joined) | 
**hidden_status** | **[str]** | Specifies an array of one or more channel hidden statuses about whether to hide the channel from each invited user&#39;s list of group channels, and whether to automatically unhide the hidden channel when receiving a new message from other member of that channel. Each item of the array should be specified with a combination of the unique ID of a user in the user_ids or users property, a colon (:), and the channel hidden status (for example, user_id_1: channel hidden status). Acceptable values are limited to the following:&lt;br /&gt;- unhidden (default): the channel is included in when retrieving a list of group channels.&lt;br /&gt;- hidden_allow_auto_unhide: the channel automatically gets unhidden when receiving a new message.&lt;br /&gt;- hidden_prevent_auto_unhide: the channel keeps hidden though receiving a new message. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


