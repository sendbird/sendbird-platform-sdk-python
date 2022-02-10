# RegisterAndScheduleDataExportData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_ts** | **int** | Specifies the starting timestamp of a period for target objects&#39; creation date, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. The creation time of messages, channels, and users will be in-between the start_ts and end_ts. | 
**end_ts** | **int** | Specifies the ending timestamp of a period for target objects&#39; creation date, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. The creation time of messages, channels, and users will be in-between the start_ts and end_ts. | 
**format** | **str** | Specifies the format of the file to export the messages to. Acceptable values are json and csv. (Default: json) | [optional] 
**csv_delimiter** | **str** | Sets a single character delimiter to separate the values in each row of the csv file which stores two-dimensional arrays of the exported message data. Either English alphabets or special characters can be used as a delimiter, including a horizontal tab (\\t), a line feed (\\n), a vertical bar (\\ | [optional] 
**timezone** | **str** | Specifies the timezone to be applied to the timestamp of the exported messages. For example, US/Pacific, Asia/Seoul, Europe/London, etc. (Default: UTC) | [optional] 
**sender_ids** | **[int]** | Specifies an array of the IDs of the users which are used to filter the messages by its sender for the export. This property is effective only when the data_type parameter is set to messages, and can be specified up to 10 IDs in the request. (Default: all messages sent by any user) | [optional] 
**exclude_sender_ids** | **[int]** | Specifies an array of the IDs of the users which are used to exclude their sent messages from the export. This property is effective only when the data_type parameter is set to messages, and can be specified up to 10 IDs. (Default: all messages sent by any user) | [optional] 
**channel_urls** | **[str]** | Specifies an array of one or more URLs of channels to export the messages from. This property is effective only when the data_type parameter is set to messages or channels. (Default: all channels) | [optional] 
**exclude_channel_urls** | **[str]** | Specifies an array of one or more URLs of channels to exclude when exporting the messages. This property is effective only when the data_type parameter is set to messages or channels. (Default: include all channels) | [optional] 
**user_ids** | **[int]** | Specifies an array of the IDs of the users to export their information. This property is effective only when the data_type parameter is set to users. (Default: all users) | [optional] 
**show_read_receipt** | **bool** | Determines whether to include information about the read receipts of each channel in the exported data. The read receipt indicates the timestamps of when each user has last read the messages in the channel, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps). (Default: true) | [optional] 
**show_channel_metadata** | **bool** | Determines whether to include [channel metadata](/docs/chat/v3/platform-api/guides/user-and-channel-metadata#2-view-a-channel-metadata) in the result files. | [optional] 
**neighboring_message_limit** | **int** | Specifies the maximum number of other users&#39; messages to be exported, which took place after the specified message of a user filtered by the sender_ids property. Even if there may be more messages that took place, if the quantity exceeds the number of the neighboring_message_limit, they are omitted. Only the messages that took place right after the specified message will be counted and exported. This can be used to better analyze the context. Acceptable values are 1 to 10, inclusive. (Default: 0) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


