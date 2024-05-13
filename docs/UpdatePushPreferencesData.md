# UpdatePushPreferencesData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**push_trigger_option** | **str** | Determines the type of push notification trigger to apply to the user&#39;s joined group channels. Valid values are the following:&lt;br /&gt;- all (default): when disconnected from Sendbird server, the user receives notifications for all new messages including mentioned messages the user has been mentioned in.&lt;br /&gt;- mention_only: when disconnected from Sendbird server, the user only receives notifications for messages the user has been mentioned in.&lt;br /&gt;- off: the user doesn&#39;t receive any notifications. | 
**do_not_disturb** | **bool** | Determines whether to pause notification messages for the user during a specific time of day. (Default: false) | 
**start_hour** | **int** | Specifies the hour to start pausing the notifications for Do Not Disturb of the user. | 
**start_min** | **int** | Specifies the minute of the hour to start pausing the notifications for Do Not Disturb of the user. | 
**end_hour** | **int** | Specifies the hour to stop pausing the notifications for Do Not Disturb of the user. | 
**end_min** | **int** | Specifies the minute of the hour to stop pausing the notifications for Do Not Disturb of the user. | 
**snooze_enabled** | **bool** | Determines whether to snooze notification messages for the user during a specific period of time. (Default: false) | 
**snooze_start_ts** | **int** | Specifies the timestamp of when to start snoozing the notifications, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps). | 
**snooze_end_ts** | **int** | Specifies the timestamp of when to end snoozing the notifications, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps). | 
**timezone** | **str** | Specifies the timezone to be applied to push preferences with a value such as UTC, Asia/Seoul, Europe/London, etc. | 
**push_sound** | **str** | Specifies the name of a sound file to be played when a push notification is delivered to your client app. | 
**block_push_from_bots** | **bool** | Determines whether to block push notifications from [all bots](/docs/chat/v3/platform-api/guides/bot-interface#2-list-bots) within the application. If the push_blocked_bot_ids is specified, notifications only from the bots in the property are blocked. (Default: false) | [optional] 
**push_blocked_bot_ids** | **[str]** | Specifies an array of one or more IDs of bots whose push notifications are blocked. This property is effective only when the block_push_from_bots is set to true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


