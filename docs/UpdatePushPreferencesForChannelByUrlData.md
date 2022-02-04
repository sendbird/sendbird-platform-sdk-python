# UpdatePushPreferencesForChannelByUrlData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**push_trigger_option** | **str** | Determines the type of push notification trigger to apply to the speficied channel. Acceptable values are limited to the following:&lt;br /&gt;- default: the user&#39;s push notification trigger setting automatically applies to the channel. This is the default setting.&lt;br /&gt;- all: when disconnected from Sendbird server, the user receives notifications for all new messages in the channel including messages the user has been mentioned in.&lt;br /&gt;- mention_only: when disconnected from Sendbird server, the user only receives notifications for messages in the channel the user has been mentioned in.&lt;br /&gt;- off: the user doesn&#39;t receive any notifications in the channel. | 
**enable** | **bool** | (Deprecated) Determines whether notification messages for the user are delivered to the group channel. (default: true) | 
**push_sound** | **str** | Specifies the name of a sound file to be played when a push notification is delivered to the specified channel. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


