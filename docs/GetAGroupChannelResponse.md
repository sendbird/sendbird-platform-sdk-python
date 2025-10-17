# GetAGroupChannelResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_url** | **str** |  | 
**channel** | [**SendbirdGroupChannelDetailChannel**](SendbirdGroupChannelDetailChannel.md) |  | [optional] 
**count_preference** | **str** |  | [optional] 
**cover_url** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**created_by** | [**SendbirdBasicUserInfo**](SendbirdBasicUserInfo.md) |  | [optional] 
**custom_type** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**delivery_receipt** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**disappearing_message** | [**SendbirdDisappearingMessage**](SendbirdDisappearingMessage.md) |  | [optional] 
**freeze** | **bool** |  | [optional] 
**has_ai_bot** | **bool** |  | [optional] 
**has_bot** | **bool** |  | [optional] 
**hidden_state** | **str** |  | [optional] 
**ignore_profanity_filter** | **bool** |  | [optional] 
**invited_at** | **int** |  | [optional] 
**inviter** | [**SendbirdBasicUserInfo**](SendbirdBasicUserInfo.md) |  | [optional] 
**is_access_code_required** | **bool, none_type** |  | [optional] 
**is_broadcast** | **bool** |  | [optional] 
**is_discoverable** | **bool** |  | [optional] 
**is_distinct** | **bool** |  | [optional] 
**is_ephemeral** | **bool** |  | [optional] 
**is_exclusive** | **bool** |  | [optional] 
**is_hidden** | **bool** |  | [optional] 
**is_muted** | **bool** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**is_push_enabled** | **bool** |  | [optional] 
**is_super** | **bool** |  | [optional] 
**joined_member_count** | **int** |  | [optional] 
**joined_ts** | **int, none_type** |  | [optional] 
**last_message** | [**SendbirdGroupChannelLastMessage**](SendbirdGroupChannelLastMessage.md) |  | [optional] 
**max_length_message** | **int** |  | [optional] 
**member_count** | **int** |  | [optional] 
**member_state** | **str** |  | [optional] 
**members** | [**[SendbirdMember]**](SendbirdMember.md) |  | [optional] 
**message_survival_seconds** | **int** |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**my_role** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**push_trigger_option** | [**SendbirdPushTriggerOption**](SendbirdPushTriggerOption.md) |  | [optional] 
**read_receipt** | **{str: (int,)}** |  | [optional] 
**sms_fallback** | [**SendbirdSmsFallback**](SendbirdSmsFallback.md) |  | [optional] 
**ts_message_offset** | **int** |  | [optional] 
**unread_mention_count** | **int** |  | [optional] 
**unread_message_count** | **int** |  | [optional] 
**user_last_read** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


