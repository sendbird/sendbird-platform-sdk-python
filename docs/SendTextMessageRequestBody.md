# SendTextMessageRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**message_type** | **str** | Specifies the type of the message. The value of MESG represents a text message. | defaults to "MESG"
**apns_bundle_id** | **str** |  | [optional] 
**apple_critical_alert_options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**created_at** | **int** |  | [optional] 
**custom_type** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**dedup_id** | **str** |  | [optional] 
**include_poll_details** | **bool** |  | [optional] 
**is_silent** | **bool** |  | [optional] 
**mark_as_read** | **bool** |  | [optional] 
**mention_type** | **str** |  | [optional] 
**mentioned_user_ids** | **[str]** |  | [optional] 
**poll_id** | **int** |  | [optional] 
**push_message_template** | [**SendTextMessageRequestBodyPushMessageTemplate**](SendTextMessageRequestBodyPushMessageTemplate.md) |  | [optional] 
**send_push** | **bool** |  | [optional] 
**sorted_metaarray** | [**SendbirdSortedMetaarray**](SendbirdSortedMetaarray.md) |  | [optional] 
**sound** | **str** |  | [optional] 
**volume** | **float** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


