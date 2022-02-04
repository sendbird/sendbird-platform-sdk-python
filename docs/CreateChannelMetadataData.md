# CreateChannelMetadataData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** | Specifies the type of the channel. Either open_channels or group_channels. | 
**channel_url** | **str** | Specifies the URL of the channel to store the metadata in. | 
**metadata** | **str** | Specifies a &#x60;JSON&#x60; object that stores key-value items. The key must not have a comma (,) and its length is limited to 128 characters. The value must be a string and its length is limited to 190 characters. This property can have up to 5 items. | 
**include_ts** | **bool** | Determines whether to include the timestamp of when a metadata has been created in the response. (Default: false) | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


