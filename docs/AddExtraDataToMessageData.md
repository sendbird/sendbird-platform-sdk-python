# AddExtraDataToMessageData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** | Specifies the type of the channel. Either open_channels or group_channels. | 
**channel_url** | **str** | Specifies the URL of the target channel. | 
**message_id** | **int** | Specifies the unique ID of the message to add key-values items for additional information. | 
**sorted_metaarray** | **str** | Specifies a &#x60;JSON&#x60; object of one or more key-values items which store additional message information. Each item consists of a key and the values in an array. Items are saved and will be returned in the exact order they&#39;ve been specified. | 
**metaarray** | **str** | (Deprecated) Specifies a &#x60;JSON&#x60; object of one or more key-values items which store additional message information. The item consists of a key and the values in an array. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


