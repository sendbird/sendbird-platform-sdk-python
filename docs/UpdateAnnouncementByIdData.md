# UpdateAnnouncementByIdData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | Specifies the unique ID of the announcement to update. | 
**action** | **str** | Specifies an action to take on the announcement. If this property is updated, other specified properties in the request are not effective. Acceptable values are limited to remove, pause, resume, and cancel. The [Announcement actions](#2-update-an-announcement-3-how-to-change-announcement-status) table explains each action in detail. | [optional] 
**announcement_group** | **str** | Specifies the name of an announcement group to retrieve. If not specified, all announcements are returned, regardless of their group. | [optional] 
**create_channel** | **bool** | Determines whether to create a new channel if there is no existing channel that matches with the target options including target_at and target_list. | [optional] 
**create_channel_options_name** | **str** | Specifies the name of the channel. (Default: Group Channel) | [optional] 
**create_channel_options_cover_url** | **str** | Specifies the URL of the cover image. | [optional] 
**create_channel_options_custom_type** | **str** | Specifies the custom channel type. | [optional] 
**create_channel_options_data** | **str** | Specifies additional channel information such as a long description of the channel or &#x60;JSON&#x60; formatted string. | [optional] 
**create_channel_options_distinct** | **str** | Determines whether to create a [distinct](/docs/chat/v3/platform-api/guides/channel-types#2-group-channel) channel. (Default: true) | [optional] 
**message_user_id** | **str** | Specifies the unique ID of the announcement sender. | [optional] 
**message_content** | **str** | Specifies the content of the message. | [optional] 
**message_data** | **str** | Specifies additional message information such as custom font size, font type or &#x60;JSON&#x60; formatted string. | [optional] 
**enable_push** | **bool** | Determines whether to turn on push notification for the announcement. If set to true, push notifications will be sent for announcements. | [optional] 
**scheduled_at** | **int** | Specifies the time to start the announcement, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. (Default: current timestamp) | [optional] 
**end_at** | **int** | Specifies the time to permanently end the announcement, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format, even if the announcement is not sent to all its targets. | [optional] 
**cease_at** | **str** | Specifies the time to temporarily put the announcement on hold in UTC. The string is represented in HHMM format. This property should be specified in conjunction with the resume_at below. | [optional] 
**resume_at** | **str** | Specifies the time to automatically resume the on-hold announcement in UTC. The string is represented in HHMM format. This property should be specified in conjunction with the cease_at above. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


