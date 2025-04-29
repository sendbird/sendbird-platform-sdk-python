# LeaveAChannelRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **[str]** | Specifies an array of one or more IDs of the users to leave the channel. | 
**should_leave_all** | **bool** | Determines whether to make all members leave the channel. (Default: false) | [optional] 
**should_remove_operator_status** | **bool** | Determines whether to remove a user from the channel&#39;s operator list if the user who is leaving the channel is an operator. (Default: false) | [optional] 
**reason** | **str** | Specifies the reason for leaving a channel. Acceptable values are admin_removed, admin_deleted, admin_deactivated, left_by_own_choice, and channel_operator_removed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


