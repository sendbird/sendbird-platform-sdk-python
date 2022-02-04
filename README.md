![Sendbird banner image](http://ww1.prweb.com/prfiles/2021/09/14/18371217/Sendbird_Logo_RGB_lg.png)

# [Sendbird Python Platform SDK](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api)


[![link to docs](https://img.shields.io/badge/SDK-docs-green)](/docs)

This is a python library that makes talking to the [Sendbird Platform API](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api) easier. With this library you can extend your Sendbird integration to include advanced features like channel automation and user management.

# 🔥 Quick start

```python

import time
import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from sendbird_platform_sdk.model.send_bird_user import SendBirdUser
from sendbird_platform_sdk.model.create_user_data import CreateUserData
from pprint import pprint


configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-YOUR_APP_ID_FROM_DASHBOARD.sendbird.com"
)


with sendbird_platform_sdk.ApiClient() as api_client:
    user_id = "bob_smith"
    nickname = "bob"
    profileUrl = "https://cataas.com/c"
    api_instance = user_api.UserApi(api_client)
    api_token = "YOUR_MASTER_API_TOKEN_FROM_DASHBOARD"
    create_user_data = CreateUserData(
        user_id=user_id,
        nickname=nickname,
        profile_url=profileUrl
       
    )

    try:
        api_response = api_instance.create_user(api_token=api_token, create_user_data=create_user_data)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```

# ⚒️ Prerequisite
In order to make requests with this SDK you will need you master API token. This can be found through the [Sendbird dashboard](https://dashboard.sendbird.com/).  Each app you create in Sendbird has its own master api token. These tokens can be found in Settings > Application > General.

![how to find you api token](https://i.imgur.com/0YMKtpX.png)

# 💻 Requirements 
This package has been tested with python version 3.9.10


# ⚙️ Installation 
see Local Development

# 🤓 Local Development
Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)


# 🗃️ Documentation 
All the documentation for this project lives in the /docs directory of this repo. 

##### Helpful links

|       | Documentation |
| ----------- | ----------- |
| Announcements   | [docs/AnnouncementsApi.md](docs/AnnouncementsApi.md)|
| Application | [docs/ApplicationApi.md](docs/ApplicationApi.md)  |
| BotInterface | [docs/BotInterfaceApi.md](docs/BotInterfaceApi.md)  |
| GroupChannel | [docs/GroupChannelApi.md](docs/GroupChannelApi.md)  |
| Messages | [docs/MessagesApi.md](docs/MessagesApi.md)  |
| OpenChannel | [docs/OpenChannelApi.md ](docs/OpenChannelApi.md)  |
| User | [docs/UserApi.md](docs/UserApi.md)  |
| Webhooks | [docs/UserApi.md](docs/WebhooksApi.md)  |


# 👀 Examples
### User Management 
TODO
### Authentication
TODO
### Authentication
TODO
### Unread counts
TODO
### Scheduling Announcements
TODO
### Channel Automation
TODO
### Automatic Message
TODO
 
# 🙄 Gotchas
