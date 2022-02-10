# UpdateExtraDataInMessageData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** | Specifies the type of the channel. Either open_channels or group_channels. | 
**channel_url** | **str** | Specifies the URL of the target channel. | 
**message_id** | **int** | Specifies the unique ID of the message to update key-values items. | 
**sorted_metaarray** | **str** | Specifies a &#x60;JSON&#x60; object of one or more key-values items which store additional message information. Each item consists of a key and the values in an array. Items are saved and will be returned in the exact order they&#39;ve been specified. | 
**mode** | **str** | Determines whether to add the specified values in the items or remove the specified values from the existing items. Acceptable values are limited to add and remove. If set to add, the specified values are added only when they are different from the existing values. If set to remove, the specified values are removed only when they have the corresponding ones in the existing values. | 
**upsert** | **bool** | Determines whether to add new items in addition to updating existing items. If true, new key-values items are added when there are no items with the keys. The existing items are updated with new values when there are already items with the keys. If false, only the items of which keys match the ones you specify are updated with new values. (Default: false) | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


