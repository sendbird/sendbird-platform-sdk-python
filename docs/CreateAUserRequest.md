# CreateAUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** |  | 
**profile_url** | **str** |  | 
**user_id** | **str** |  | 
**discovery_keys** | **[str]** |  | [optional] 
**issue_access_token** | **bool** |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**profile_file** | **file_type** | Specifies the file of the user&#39;s profile image. An acceptable image is limited to a JPG, JPEG, or PNG file of up to 5 MB. When passing a file, you should send a multipart request. If the profile_file property is specified, the profile_url property is not required. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


