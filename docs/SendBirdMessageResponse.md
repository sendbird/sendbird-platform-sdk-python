# SendbirdMessageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_auth** | **bool** |  | [optional] 
**message_survival_seconds** | **int** |  | [optional] 
**custom_type** | **str** |  | [optional] 
**mentioned_users** | [**[SendbirdBasicUserInfo]**](SendbirdBasicUserInfo.md) |  | [optional] 
**translations** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**is_op_msg** | **bool** |  | [optional] 
**reactions** | [**[SendbirdReaction]**](SendbirdReaction.md) |  | [optional] 
**is_removed** | **bool** |  | [optional] 
**user** | [**SendbirdBasicUserInfo**](SendbirdBasicUserInfo.md) |  | [optional] 
**file** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**files** | [**[SendbirdFile]**](SendbirdFile.md) |  | [optional] 
**message** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**message_retention_hour** | **int** |  | [optional] 
**silent** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**channel_type** | **str** |  | [optional] 
**req_id** | **str** |  | [optional] 
**mention_type** | **str** |  | [optional] 
**channel_url** | **str** |  | [optional] 
**message_id** | **int** |  | [optional] 
**sorted_metaarray** | [**SendbirdSortedMetaarray**](SendbirdSortedMetaarray.md) |  | [optional] 
**thread_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**parent_message_id** | **int** |  | [optional] 
**parent_message_info** | [**SendbirdParentMessageInfo**](SendbirdParentMessageInfo.md) |  | [optional] 
**is_reply_to_channel** | **bool** |  | [optional] 
**message_events** | [**SendbirdMessageResponseMessageEvents**](SendbirdMessageResponseMessageEvents.md) |  | [optional] 
**extended_message_payload** | [**SendbirdExtendedMessagePayload**](SendbirdExtendedMessagePayload.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


