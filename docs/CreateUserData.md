# CreateUserData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Specifies a user&#39;s unique ID, which is used to sign into the Sendbird service. The length is limited to 80 characters.&lt;br /&gt;&lt;br /&gt; Do not use PII (Personally Identifiable Information) of your service, such as user email address, legal name or phone number. | 
**nickname** | **str** | Specifies a nickname for a new user. The length is limited to 80 characters. | 
**profile_url** | **str** | Specifies the URL of the user&#39;s profile image. If left empty, no profile image is set for the user. The length is limited to 2,048 characters.&lt;br /&gt;&lt;br /&gt; The [domain filter](/docs/chat/v3/platform-api/guides/filter-and-moderation#2-domain-filter) filters out the request if the value of this property matches the filter&#39;s domain set. | 
**profile_file** | **file_type** | Uploads the file of the user&#39;s profile image. An acceptable image is limited to &#x60;JPG&#x60; (.jpg), &#x60;JPEG&#x60; (.jpeg), or &#x60;PNG&#x60; (.png) file of up to 25 MB. | [optional] 
**issue_access_token** | **bool** | Determines whether to create an access token for the user. If true, an opaque string token is issued and provided upon creation, which should be passed whenever the user logs in. If false, an access token is not required when the user logs in. (Default: false) | [optional] 
**discovery_keys** | **[str]** | Specifies an array of unique keys of the user which is provided to Sendbird server for discovering friends. By using the keys, the server can identify and match the user with other users. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies a &#x60;JSON&#x60; object to store key-value items for additional user information such as phone number, email or a long description of the user. The key must not have a comma (,) and its length is limited to 128 characters. The value must be a string and its length is limited to 190 characters. This property can have up to 5 items. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


