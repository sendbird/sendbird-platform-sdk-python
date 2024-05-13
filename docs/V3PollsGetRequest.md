# V3PollsGetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Specifies the title of a poll. The length is limited to 2,048 characters. | [optional] 
**options** | **[str]** | Specifies an array of poll options that a user can vote for. At least one option should be provided, and the length of each option is limited to 2,000 characters. | [optional] 
**allow_user_suggestion** | **bool** | Determines whether to allow users other than the creator of the poll to add new options to the poll. (Default is false) | [optional] 
**allow_multiple_votes** | **bool** | Determines whether to allow users to vote for multiple options. (Default is false) | [optional] 
**close_at** | **int** | Specifies when the poll closes and no longer accepts votes in Unix seconds. If the value of this property is -1, the poll is open indefinitely. | [optional] 
**created_by** | **str** | Specifies the unique ID of the user who creates the poll. | [optional] 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies a JSON object of one or more key-value items to store additional poll information. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


