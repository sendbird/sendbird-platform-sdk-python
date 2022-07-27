# GcUpdateChannelByUrlData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_url** | **str** | Specifies the URL of the channel to update. | 
**name** | **str** | Specifies the name of the channel, or the channel topic. The length is limited to 191 characters. | 
**cover_url** | **str** | Specifies the unique URL of the cover image. The length is limited to 2,048 characters. | 
**cover_file** | **file_type** | Uploads the cover image file for the channel. | 
**custom_type** | **str** | Specifies the custom channel type which is used for channel grouping. The length is limited to 128 characters.&lt;br /&gt;&lt;br /&gt; Custom types are also used within Sendbird&#39;s [Advanced analytics](/docs/chat/v3/platform-api/guides/advanced-analytics) to segment metrics, which enables the sub-classification of data views. | 
**data** | **str** | Specifies additional channel information such as a long description of the channel or &#x60;JSON&#x60; formatted string. | 
**is_distinct** | **bool** | Determines whether to reuse an existing channel or create a new channel. If set to true, returns a channel with the current channel members users or creates a new channel if no match is found. Sendbird server can also use the custom channel type in the custom_type property if specified along with the users to return the corresponding channel. If set to false, Sendbird server always creates a new channel with a combination of the users as well as the channel custom type if specified. (Default: false)&lt;br /&gt;&lt;br /&gt; Under this property, Sendbird server does not distinguish channels based on other properties such as channel URL or channel name. | 
**is_public** | **bool** | Determines whether to allow a user to join the channel without an invitation. (Default: false) | 
**access_code** | **str** | This property can be used only when the channel operator wants to set an access code for a public group channel. If specified, the is_access_code_required property of the channel resource is then set to true, and the channel begins to require the specified access code to a user who attempts to join. | 
**operator_ids** | **[str]** | Specifies an array of one or more IDs of users to register as operators of the channel. If the operators are not members of the channel yet, they need an [invitation](#2-invite-as-members) to [join](#2-join-a-channel) a privte group channel while they don&#39;t need any to join a [public](#-3-private-vs-public) group channel. The maximum allowed number of operators per channel is 100. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


