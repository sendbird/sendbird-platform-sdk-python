# SendAMessageRequestPushMessageTemplateOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Specifies the title of the custom push notification template. You can customize the title using the variables sender_name and message, which can be later replaced with corresponding real values when the template is sent out as a notification request to FCM, HMS, or APNs. | [optional] 
**body** | **str** | Specifies the body of the custom push notification template. You can customize the body using the variables sender_name and message, which can be later replaced with corresponding real values when the template is sent out as a notification request to FCM, HMS, or APNs. If not specified, the body by default contains the message content inside the message property. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


