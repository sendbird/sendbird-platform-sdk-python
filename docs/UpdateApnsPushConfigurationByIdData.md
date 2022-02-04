# UpdateApnsPushConfigurationByIdData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Specifies the provider ID of the push configuration to update. | 
**apns_cert** | **file_type** | In a form of the &#x60;multipart/form-data&#x60; content type, specifies a [.p12](/docs/chat/v3/ios/guides/push-notifications#2-step-3-export-a-p12-file-and-upload-to-sendbird-dashboard) file of which type is either development or production. Sendbird server scans the content of the file, finds out the certificate type, and then registers the file as the corresponding type. If you upload a wrong file, you will receive an error. You should specify either this property or the apns_type below to inform the server of which certificate type to update. | 
**apns_cert_env_type** | **str** | Specifies the certificate type of the [.p12](/docs/chat/v3/ios/guides/push-notifications#2-step-3-export-a-p12-file-and-upload-to-sendbird-dashboard) file. Acceptable values are development and production. You should specify either this property or the apns_cert above to inform the server of which certificate type to update. | 
**apns_cert_password** | **str** | Specifies the password of the cerfificate file which has been set during the [.p12](/docs/chat/v3/ios/guides/push-notifications#2-step-3-export-a-p12-file-and-upload-to-sendbird-dashboard) export. | 
**has_unread_count_badge** | **bool** | Determines whether to badge your client app&#39;s icon with the number of a user&#39;s unread messages. (Default: true) | 
**content_available** | **bool** | Determines for your client app whether to perform a silent background update on a user&#39;s device. For more information, see the Apple Developer Documentation&#39;s [Pushing Updates to Your App Silently](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_updates_to_your_app_silently). (Default: false) | 
**mutable_content** | **bool** | Determines for your client app whether or not to modify the payload of a push notification before it is displayed on a user&#39;s device. For more information, see the Apple Developer Documentation&#39;s [Modifying Content in Newly Delivered Notifications](https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications). (Default: false) | 
**push_sound** | **str** | Specifies the name of a sound file to be played when a push notification is delivered to your client app. The file can be in the app&#39;s main bundle or in the &#x60;Library/Sounds&#x60; folder of the app&#39;s data container. | 
**apns_type** | **str** | (Deprecated)  Specifies the certificate type of the [.p12](/docs/chat/v3/ios/guides/push-notifications#2-step-3-export-a-p12-file-and-upload-to-sendbird-dashboard) file. Acceptable values are development and production. You should specify either this property or the apns_cert above to inform the server of which certificate type to update. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


