# OcBanUserData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_url** | **str** | Specifies the URL of the channel where to ban the specified user. | 
**user_id** | **str** | Specifies the ID of the user to ban. | 
**agent_id** | **str** | Specifies the ID of the operator (agent) who bans the user. | 
**seconds** | **int** | Specifies the ban duration. If set to -1, the user will be banned permanently (10 years, technically). (Default: -1) | 
**description** | **str** | Specifies a reason for the banning. The length is limited to 250 characters. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


