# SendAMessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** |  | 
**user_id** | **str** |  | 
**message** | **str** | Specifies the content of the message. * This property is required when message_type is MESG or ADMM. | [optional] 
**push_message_template** | [**SendAMessageRequestPushMessageTemplate**](SendAMessageRequestPushMessageTemplate.md) |  | [optional] 
**poll_id** | **int** | Specifies the ID of the poll to be associated with the message. * This property is only available for group channels and message_type is MESG. | [optional] 
**files** | [**SendbirdFile**](SendbirdFile.md) |  | [optional] 
**require_auth** | **bool** | Determines whether to require an authentication key to verify if the file is being properly accessed. Only the user who uploaded the file or users who are in the channel where the file was uploaded should have access. The authentication key managed internally by the Sendbird system is generated every time a user logs in to the Sendbird server and is valid for three days starting from the last login. If set to false, Sendbird tries to access a file without any key. To access encrypted files, such as the files in the Sendbird server which are by default encrypted, the property must be set to true. (Default: false) The require_auth parameter only works if the file or URL is managed by Sendbird, which means that when you upload files using multipart format or provide URLs that point to the files hosted on the Sendbird server. However, if the file is hosted on a server or service that is not managed by Sendbird, access control and authentication for the file should be handled by the respective server or service hosting the file. | [optional] 
**thumbnail1** | **str** | Specifies the URL of the thumbnail of the file. * This property is available when message_type is FILE. | [optional] 
**thumbnail2** | **str** | Specifies the URL of the thumbnail of the file. * This property is available when message_type is FILE. | [optional] 
**thumbnail3** | **str** | Specifies the URL of the thumbnail of the file. * This property is available when message_type is FILE. | [optional] 
**thumbnails** | **[str]** | Specifies the URL of the thumbnail of the file. * This property is available when message_type is FILE. | [optional] 
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
**send_push** | **bool** |  | [optional] 
**sorted_metaarray** | [**SendbirdSortedMetaarray**](SendbirdSortedMetaarray.md) |  | [optional] 
**sound** | **str** |  | [optional] 
**volume** | **float** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


