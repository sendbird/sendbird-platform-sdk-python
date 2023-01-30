import time
import random
import string
from pprint import pprint
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api, open_channel_api, message_api, user_api
from sendbird_platform_sdk.model.gc_create_channel_data import GcCreateChannelData
from sendbird_platform_sdk.model.send_message_data import SendMessageData
from sendbird_platform_sdk.model.create_user_data import CreateUserData
from sendbird_platform_sdk.model.oc_create_channel_data import OcCreateChannelData
from sendbird_platform_sdk.model.send_bird_group_channel import SendBirdGroupChannel

configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-YOUR_APP_ID.sendbird.com"
)

with sendbird_platform_sdk.ApiClient(configuration=configuration) as api_client:
    # Create an instance of the API class
    
    api_token = "YOUR_API_KEY" # str | 
    class GroupChannel():

        def __init__(self):

            self.api_instance = group_channel_api.GroupChannelApi(api_client)


        def create_group_channel(self, user_ids):
            gc_create_channel_data = GcCreateChannelData(
                user_ids=user_ids,
                name="Name",
                channel_url=random_string(),
                is_distinct=False,
            )

            try:
                # Create a channel
                api_response = self.api_instance.gc_create_channel(api_token, gc_create_channel_data=gc_create_channel_data)
                return api_response
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling GroupChannelApi->gc_create_channel: %s\n" % e)


    class User():

        def __init__(self):
            self.api_instance = user_api.UserApi(api_client)

        def create_user(self):
            create_user_data = CreateUserData(
                user_id=random_string(),
                nickname="5678",
                profile_url="profile_url_example",
                metadata={},
            ) # CreateUserData |  (optional)

            # example passing only required values which don't have defaults set
            try:
                # Create a user
                api_response = self.api_instance.create_user(api_token, create_user_data=create_user_data)
                return api_response
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling UserApi->create_user: %s\n" % e)


    class Message():
        def __init__(self):
            self.api_instance = message_api.MessageApi(api_client)

        def send_user_message(self, user_id, channel_url):
            channel_type = "group_channels" # str | 
            channel_url = channel_url # str | 
            send_message_data = SendMessageData(
                message_type="MESG",
                user_id=user_id,
                message="hey",
            
            ) 

            try:
                api_response = self.api_instance.send_message(api_token, channel_type, channel_url, send_message_data=send_message_data)
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling MessageApi->send_message: %s\n" % e)

        def number_of_members_unread_messages(self, user_ids, channel_url):

            try:
                api_response = self.api_instance.gc_view_number_of_each_members_unread_messages(api_token, channel_url, user_ids=user_ids)
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling MessageApi->gc_view_number_of_each_members_unread_messages: %s\n" % e)


    class CountMessages():
        def run(self):
            print("running message count sample: start")
            user = User()
            groupChannel = GroupChannel()
            message = Message()

            user_a = user.create_user()
            user_b = user.create_user()
            channel = groupChannel.create_group_channel([user_b["user_id"], user_a["user_id"]])
            message.send_user_message(user_a["user_id"], channel["channel_url"])
            message.number_of_members_unread_messages(user_b["user_id"], channel["channel_url"])

            print("running message count sample: done")



    def random_string():
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return res

    countMessages = CountMessages()

    countMessages.run()