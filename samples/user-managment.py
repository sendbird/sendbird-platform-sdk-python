import time
import random
import string
from pprint import pprint
import sendbird_platform_sdk
from sendbird_platform_sdk.api import group_channel_api, open_channel_api, message_api, user_api
from sendbird_platform_sdk.model.gc_create_channel_data import GcCreateChannelData
from sendbird_platform_sdk.model.send_message_data import SendMessageData
from sendbird_platform_sdk.model.create_user_data import CreateUserData
from sendbird_platform_sdk.model.send_bird_group_channel import SendBirdGroupChannel
from sendbird_platform_sdk.model.update_user_by_id_data import UpdateUserByIdData

configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-YOUR_APP_ID.sendbird.com"
)




with sendbird_platform_sdk.ApiClient(configuration=configuration) as api_client:
    
    api_token = "YOUR_API_KEY" 


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
                
        def update_user(self, user_id):
            update_user_by_id_data = UpdateUserByIdData(
                user_id=user_id,
                nickname="updated-nickname",
                profile_url="new-profile-url"
            )
            try:
                api_response = self.api_instance.update_user_by_id(api_token, user_id, update_user_by_id_data=update_user_by_id_data)
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling UserApi->update_user_by_id: %s\n" % e)

        def delete_user(self, user_id):
            try:
                api_response = self.api_instance.delete_user_by_id(api_token, user_id)
            except sendbird_platform_sdk.ApiException as e:
                print("Exception when calling UserApi->delete_user_by_id: %s\n" % e)

    class UserManagment():

        def run(self):
            print("running user managment sample: start")

            user = User()
            user_a = user.create_user()
            user.update_user(user_a["user_id"])
            user.delete_user(user_a["user_id"])

            print("running user managment sample: done")




    def random_string():
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return res

    userManagment = UserManagment()

    userManagment.run()