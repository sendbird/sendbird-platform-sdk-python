# SendBotSMessageDataExtendedMessagePayload

Specifies the extended message payload which is used to send a message with a custom message type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_replies** | **[str]** | Specifies an array of suggested replies to be sent with the message. | [optional] 
**custom_view** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON format you want to embed in message, eq : {\&quot;title\&quot;: \&quot;title\&quot;, \&quot;image\&quot;: \&quot;https://link.to/image.jpg\&quot;} | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


