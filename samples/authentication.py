import time
import random
import string
from pprint import pprint
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api, open_channel_api, message_api, user_api, announcement_api
from sendbird_platform_sdk.model.gc_create_channel_data import GcCreateChannelData
from sendbird_platform_sdk.model.send_message_data import SendMessageData
from sendbird_platform_sdk.model.create_user_data import CreateUserData
from sendbird_platform_sdk.model.create_user_token_data import CreateUserTokenData
from sendbird_platform_sdk.model.send_bird_group_channel import SendBirdGroupChannel

configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-YOUR_APP_ID.sendbird.com"
)




with sendbird_platform_sdk.ApiClient(configuration=configuration) as api_client:
    # Create an instance of the API class
    
    api_token = "YOUR_API_KEY" # str | 


    class User():

        def __init__(self):
            self.api_instance = user_api.UserApi(api_client)

        def create_user(self):
            create_user_data = CreateUserData(
                user_id=random_string(),
                nickname="5678",
                profile_url="profile_url_example",
            )
            try:
                api_response = self.api_instance.create_user(api_token, create_user_data=create_user_data)
                return api_response
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling UserApi->create_user: %s\n" % e)

        def create_session_token(self, user_id):
            create_user_token_data = CreateUserTokenData()
            try:
                api_response = self.api_instance.create_user_token(api_token, user_id, create_user_token_data=create_user_token_data)
                return api_response
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling UserApi->create_user_token: %s\n" % e)

    class Authentication():
        def __init__(self):
            self.api_instance = announcement_api.AnnouncementApi(api_client)

        def run(self):
            print("running authentication sample: start")

            user = User()
            user_a = user.create_user()
            user.create_session_token(user_a["user_id"])
            print("running authentication sample: done")




    def random_string():
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return res

    authentication = Authentication()

    authentication.run()