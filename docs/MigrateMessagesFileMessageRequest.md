# MigrateMessagesFileMessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**url** | **str** |  | 
**timestamp** | **int** |  | 
**message_type** | **str** |  | defaults to "FILE"
**file_name** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**file_type** | **str** |  | [optional] 
**thumbnails** | [**[MigrateMessagesFileMessageRequestThumbnailsInner]**](MigrateMessagesFileMessageRequestThumbnailsInner.md) |  | [optional] 
**require_auth** | **bool** |  | [optional] 
**custom_type** | **str** |  | [optional] 
**custom_field** | **str** |  | [optional] 
**mentioned_user_ids** | **[str]** |  | [optional] 
**dedup_id** | **str** |  | [optional] 
**sorted_metaarray** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


