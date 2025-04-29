# CreateABotRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_callback_url** | **str** |  | 
**bot_nickname** | **str** | Specifies the bot&#39;s nickname. The length is limited to 80 characters. | 
**bot_profile_url** | **str** |  | 
**bot_type** | **str** |  | 
**bot_userid** | **str** | Specifies the unique ID of a bot. The length is limited to 80 characters. | 
**is_privacy_mode** | **bool** | Determines whether to forward all or specific messages to the bot in channels where the bot is a member. If set to true, only messages starting with a \&quot;/\&quot; or mentioning the bot_userid are forwarded to the bot. If set to false, all messages are forwarded. This property can help protect the privacy of users&#39; chat logs by configuring the bot to only receive messages addressed to the bot. | 
**channel_invitation_preference** | **int** |  | [optional] 
**enable_mark_as_read** | **bool** |  | [optional] 
**show_member** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


