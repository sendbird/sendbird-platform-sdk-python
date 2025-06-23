# SendTextMessageRequestBodyPushMessageTemplate

Specifies the content of a push notification customized for the message. This property only applies to group channels. To choose from a push notification content template within your Sendbird application, specify a string value of default or alternative. To create a new push notification content tailored to the message being sent, use the properties listed below to specify its title and body in a nested object format. * This property overrides the application's default push notification content template or the preference chosen by the user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Specifies the title of the custom push notification template. You can customize the title using the variables sender_name and message, which can be later replaced with corresponding real values when the template is sent out as a notification request to FCM, HMS, or APNs. | [optional] 
**body** | **str** | Specifies the body of the custom push notification template. You can customize the body using the variables sender_name and message, which can be later replaced with corresponding real values when the template is sent out as a notification request to FCM, HMS, or APNs. If not specified, the body by default contains the message content inside the message property. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


