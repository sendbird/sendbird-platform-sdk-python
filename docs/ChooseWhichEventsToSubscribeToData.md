# ChooseWhichEventsToSubscribeToData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Determines whether webhooks are turned on in your Sendbird application or not. (Default: false) | 
**url** | **str** | Specifies the URL of your webhook server to receive payloads for events. | 
**include_members** | **bool** | Determines whether to include the information on the members of group channels in payloads. (Default: false) | [optional] 
**enabled_events** | **[str]** | Specifies an array of one or more [events](#2-webhook-events) for your webhook server to subscribe to. If set to an asterisk () only, the server will subscribe to all supported events. If set to an empty array, the server will unsubscribe from all (which indicates turning off webhooks). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


