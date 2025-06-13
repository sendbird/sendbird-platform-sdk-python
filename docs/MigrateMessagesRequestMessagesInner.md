# MigrateMessagesRequestMessagesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_type** | **str** |  | [optional] 
**mentioned_user_ids** | **[str]** |  | [optional] 
**data** | **str** |  | [optional] 
**dedup_id** | **str** |  | [optional] 
**sorted_metaarray** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**file_name** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**file_type** | **str** |  | [optional] 
**thumbnails** | [**[MigrateMessagesFileMessageRequestThumbnailsInner]**](MigrateMessagesFileMessageRequestThumbnailsInner.md) |  | [optional] 
**require_auth** | **bool** |  | [optional] 
**custom_field** | **str** |  | [optional] 
**is_silent** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional]  if omitted the server will use the default value of "ADMM"
**message** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


