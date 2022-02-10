# ScheduleAnnouncementData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The [message](/docs/chat/v3/platform-api/guides/messages#-3-resource-representation) of a new announcement. | 
**message_type** | **str** | Specifies the type of the message, which can be either MESG for a text message and ADMM for an admin message. | 
**message_user_id** | **str** | Specifies the unique ID of the sender when the message.type is MESG. When the message.type value is ADMM, this property is not effective. | 
**message_content** | **str** | Specifies the content of the message. | 
**target_at** | **str** | Specifies the target channels to send the announcement to. Acceptable values are the following: &lt;br/&gt; - sender_all_channels (Default): sends the announcement to all of the sender&#39;s group channels.&lt;br /&gt;- target_channels: sends the announcement to all target group channels. When the &#x60;message.type&#x60; of the announcement is ADMM, this is the only valid option. &lt;br /&gt; - target_users_included_channels: sends the announcement to group channels consisting of the sender, target users, and other members. &lt;br/&gt; - target_users_only_channels: sends the announcement to group channels consisting of the sender and target users only. | 
**target_list** | **[str]** | Specifies an array of one or more target user IDs or target channel URLs to send the announcement to when the target_at is  target_channels, target_users_only_channels, or target_users_included_channels.&lt;br /&gt;&lt;br /&gt;  When the target_at value is sender_all_channels, this property is not effective. | 
**target_channel_type** | **str** | Determines which type of group channel to send the announcement to, based on the target_at and target_list. This property is effective only when the target_at is either target_users_only_channels or target_users_included_channels and the target_list is specified. Acceptable values are limited to the following:&lt;br/&gt;- all: send the announcement to all channels that have all target users and the sender in them, regardless of channel type.&lt;br/&gt;- distinct (default): sends this announcement to the distinct channels. Distinct channels continue to use the same existing channels whenever someone attempts to create a new channel with the same members.&lt;br/&gt;- non-distinct: sends this announcement to the non-distinct channels. Non-distinct channels always create a new channel even if there is an existing channel with the same members.&lt;br/&gt;&lt;br/&gt; The distinct and non-distinct channels are a subtype of group channels, determined by the [is_distinct](/docs/chat/v3/platform-api/guides/group-channel#2-types-of-a-channel-3-resource-representation) property. | 
**unique_id** | **str** | Specifies the unique ID of the new announcement. The unique_id will be automatically created unless specified. | [optional] 
**message_custom_type** | **str** | Specifies the custom message type of the message of the new announcement. | [optional] 
**message_data** | **str** | Specifies additional message information such as custom font size, font type or &#x60;JSON&#x60; formatted string. | [optional] 
**create_channel** | **bool** | Determines whether to create a new channel if there is no existing channel that matches with the target options including target_at and target_list. By specifying the create_channel_options, you can configure the properties of newly created channels. (Default: false) | [optional] 
**announcement_group** | **str** | Specifies the announcement group that the new announcement belongs to.&lt;br/&gt; &lt;br/&gt; This property is effective only when the target_at is either target_users_only_channels or target_users_included_channels. | [optional] 
**create_channel_options** | **str** | A newly created channel configuration. | [optional] 
**create_channel_options_name** | **str** | Specifies the name of channels to be created. (Default: Group Channel) | [optional] 
**create_channel_options_cover_url** | **str** | Specifies the URL of the cover image for the new channels. | [optional] 
**create_channel_options_custom_type** | **str** | Specifies the custom channel type of the new channels. | [optional] 
**create_channel_options_data** | **str** | Specifies additional channel information such as a long description of the channel or &#x60;JSON&#x60; formatted string. | [optional] 
**create_channel_options_distinct** | **str** | Determines whether to create a [distinct](/docs/chat/v3/platform-api/guides/channel-types#2-group-channel) channel. (Default: true) | [optional] 
**scheduled_at** | **int** | Specifies the time to start the announcement, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. If not specified, the default is the timestamp of when the request was delivered to Sendbird server. (Default: current timestamp) | [optional] 
**cease_at** | **str** | Specifies the time to temporarily put the announcement on hold in UTC. The string is represented in HHMM format. This should be specified in conjunction with the resume_at property.&lt;br/&gt;&lt;br/&gt; If both the cease_at and resume_at are not specified, Sendbird server starts to send the announcement at the time of the scheduled_at above. | [optional] 
**resume_at** | **str** | Specifies the time to automatically resume the on-hold announcement in UTC. The string is represented in HHMM format. This should be specified in conjunction with the cease_at property above.&lt;br/&gt;&lt;br/&gt; If both the cease_at and resume_at are not specified, Sendbird server starts to send the announcement at the time of the scheduled_at above. | [optional] 
**end_at** | **int** | Specifies the time to permanently end the announcement, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous##2-timestamps) format. If this property is specified, the announcement ends even when the announcement is not sent to all its targets. &lt;br/&gt;&lt;br/&gt; For the announcement to run safely, the end_at time should be set at least 10 minutes later than the scheduled_at time. | [optional] 
**enable_push** | **bool** | Determines whether to turn on push notification for the announcement. If set to true, push notifications will be sent for the announcement. (Default: true) | [optional] 
**assign_sender_as_channel_inviter** | **bool** | Determines whether to assign an announcement sender as an inviter of the newly created channels. (Default: false) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


