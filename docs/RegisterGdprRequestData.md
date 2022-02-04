# RegisterGdprRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Determines the type of a GDPR request. Acceptable values are limited to access and delete. If set to access, Sendbird server generates a downloadable zip file containing the data of the specified user with the user_id property to comply with GDPR&#39;s [right to access](https://gdpr-info.eu/art-15-gdpr/) of the data subject. If set to delete, the specified users with the user_ids property will be permanently deleted from your Sendbird application to comply with GDPR&#39;s [right to erasure](https://gdpr-info.eu/art-17-gdpr/) of the data subject. (Default: delete) | 
**user_ids** | **[int]** | Specifies an array of the IDs of the users to delete in order to meet the GDPR&#39;s requirements. The maximum number of users to be processed at once is 100. This should be specified when the value of the action property is delete. | 
**channel_delete_option** | **str** | Determines the scope of group channels to delete in addition to deleting the specified users with the user_ids property. Acceptable values are limited to the following:&lt;br /&gt;- do_not_delete (default): the users will be deleted but their joined group channels will remain.&lt;br /&gt;- 1_on_1: only 1-on-1 group channels of the users will be deleted. (This option can be useful when eliminating spam users) &lt;br /&gt;- all: all joined group channels of the users will be deleted.&lt;br /&gt;&lt;br /&gt; This only works when the value of the action property is delete. | 
**user_id** | **str** | Specifies the ID of the user to meet the GDPR&#39;s requirements. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


