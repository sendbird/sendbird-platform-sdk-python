import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api, open_channel_api, message_api, user_api
from sendbird_platform_sdk.model.gc_create_channel_data import GcCreateChannelData
from sendbird_platform_sdk.model.send_message_data import SendMessageData

from sendbird_platform_sdk.model.oc_create_channel_data import OcCreateChannelData

from sendbird_platform_sdk.model.send_bird_group_channel import SendBirdGroupChannel
from pprint import pprint
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-76AE2940-073F-41F6-8C14-0B3C60BABB83.sendbird.com"
)


# Enter a context with an instance of the API client
with sendbird_platform_sdk.ApiClient(configuration=configuration) as api_client:
    # Create an instance of the API class
    api_token = "cd4f6b80741fc4fb833754cb4147337a67a6b679" # str | 
    class GroupChannel():

        def __init__(self):
            self.api_instance = group_channel_api.GroupChannelApi(api_client)


        def createGroupChannel(self):
            gc_create_channel_data = GcCreateChannelData(
                user_ids=[
                    "james1"
                ],
                name="Otter Support Team",
                channel_url="sendbird_ops_support_channel_{}".format("8123773"),
                custom_type="support",
                is_distinct=True,
                is_public=False,
                is_super=False,
                is_ephemeral=False,
                inviter_id="bob",
                operator_ids=["bob"]
                # created_by="bob",
                # invitation_status={
                #     "OtterOps1": "joined",
                #     "bob": "joined",
                # },
            )
            print(gc_create_channel_data)
            # gc_create_channel_data = {
            #     "user_ids": ["1"]
            # }
            # example passing only required values which don't have defaults set
            try:
                # Create a channel
                api_response = self.api_instance.gc_create_channel(api_token, gc_create_channel_data=gc_create_channel_data)
                pprint(api_response)
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling GroupChannelApi->gc_create_channel: %s\n" % e)


    class User():

        def __init__(self):
            self.api_instance = user_api.UserApi(api_client)


        def listUserChannels(self):
            user_id = "james1"
            try:
                # List my group channels
                api_response = self.api_instance.list_my_group_channels(api_token, user_id, show_empty=True)
                pprint(api_response)
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling UserApi->list_my_group_channels: %s\n" % e)

    class OpenChannel():
        def __init__(self):
            self.api_instance = open_channel_api.OpenChannelApi(api_client)

        def createOpenChannel(self):
            oc_create_channel_data = OcCreateChannelData(
                user_ids = ["james1"]
            ) # GcCreateChannelData |  (optional)

            try:
                # Create a channel
                api_response = self.api_instance.oc_create_channel(api_token, oc_create_channel_data=oc_create_channel_data)
                pprint(api_response)
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling GroupChannelApi->oc_create_channel: %s\n" % e)

    class Message():
        def __init__(self):
            self.api_instance = message_api.MessageApi(api_client)

        def sendUserMessage(self):
            channel_type = "group_channels" # str | 
            channel_url = "sendbird_ops_support_channel_8123773" # str | 
            send_message_data = SendMessageData(
                message_type="MESG",
                user_id="james1",
                message="hey",
            
            ) # SendMessageData |  (optional)
            print(send_message_data)

            try:
                # Send a message
                api_response = self.api_instance.send_message(api_token, channel_type, channel_url, send_message_data=send_message_data)
                pprint(api_response)
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling MessageApi->send_message: %s\n" % e)

    groupChannel = GroupChannel()
    groupChannel.createGroupChannel()

    # openChannel = OpenChannel()
    # openChannel.createOpenChannel()

    # message = Message()
    # message.sendUserMessage()
    
    # user = User()
    # user.listUserChannels()
