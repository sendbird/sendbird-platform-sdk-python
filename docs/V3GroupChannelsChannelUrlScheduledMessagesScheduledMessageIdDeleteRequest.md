# V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** | Specifies the type of the message. The value of MESG represents a text message. | [optional] 
**user_id** | **str** | Specifies the user ID of the sender. | [optional] 
**message** | **str** | Specifies the content of the message. | [optional] 
**file** | **str** | Depending on the file upload method, this specifies the data of the file to upload to the Sendbird server either in raw binary format or by the file&#39;s location. When sending a request containing a file, you must change the value of the content-type header to multipart/form-data; boundary&#x3D;{your_unique_boundary_string} in the request. The code examples of HTTP multipart request and cURL are provided below the tables for your reference. If this file property is specified, the url property is not required. This doesn&#39;t allow a converted base64-encoded string from a file as its value. | [optional] 
**url** | **str** | Specifies the URL of the file hosted on the server of your own or other third-party companies. If this url property is specified, the file property is not required. | [optional] 
**scheduled_at** | **float** | The specified time that indicates when to send the message, in Unix milliseconds format. Since messages are scheduled in minutes, values less than seconds are discarded. The specified time can be between 5 minutes and 43,200 minutes (30 days) from the current time. | [optional] 
**custom_type** | **str** | Specifies a custom message type used for message grouping. The length is limited to 128 characters. * Custom types are also used to segment metrics within Sendbird&#39;s Advanced analytics, which enables the sub-classification of data views. | [optional] 
**data** | **str** | Specifies additional message information such as custom font size, font type, or JSON formatted string. | [optional] 
**send_push** | **bool** | Determines whether to send a push notification of the message to the channel members. This property only applies to group channels. (Default is true) | [optional] 
**mention_type** | **str** | Specifies the mentioning method that indicates which user receives a notification of the message. Acceptable values are users and channels. If set to users, only the users specified in the mentioned_user_ids property below are notified. If set to channels, all users in the channel are notified. (Default &#x3D; users) | [optional] 
**mentioned_user_ids** | **[str]** | Specifies an array of one or more IDs of the users who will receive a notification of the message. | [optional] 
**is_silent** | **bool** | Determines whether to send a message without updating some of the following channel properties. If set to true, the channel&#39;s last_message is updated only for the sender while its unread_message_count remains unchanged for all channel members. Also, a push notification isn&#39;t sent to the users receiving the message. If the message is sent to a hidden channel, the channel remains hidden. (Default is false) | [optional] 
**mark_as_read** | **bool** | Determines whether to mark the message as read for the sender. If set to false, then the sender&#39;s unread_count and read_receipt remain unchanged after the message is sent. (Default is true) | [optional] 
**sorted_metaarray** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | Specifies an array of one or more JSON objects consisting of key-values items that store additional message information. Items are saved and returned in the exact order they&#39;ve been specified. | [optional] 
**dedup_id** | **str** | Specifies a unique ID for the message created by another system. In general, this property is used to prevent the same message data from getting inserted when migrating messages from another system to the Sendbird server. If specified, the server performs a duplicate check using the property value. | [optional] 
**apns_bundle_id** | **str** | Specifies the bundle ID of the client app in order to send a push notification to iOS devices. You can find this in Settings &gt; Chat &gt; Notifications &gt; Push notification services on Sendbird Dashboard. | [optional] 
**apple_critical_alert_options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies options that support Apple&#39;s critical alerts and checks whether the message is a critical alert. | [optional] 
**sound** | **str** | Specifies the name of a sound file that is used for critical alerts. | [optional] 
**volume** | **float** | Specifies the volume of the critical alert sound. The volume ranges from 0.0to 1.0, which indicates silent and full volume, respectively. (Default &#x3D; 1.0) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


