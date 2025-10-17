![Sendbird banner image](http://ww1.prweb.com/prfiles/2021/09/14/18371217/Sendbird_Logo_RGB_lg.png)

# [Sendbird Python Platform SDK](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api)


[![link to docs](https://img.shields.io/badge/SDK-docs-green)](/docs)
[![PYPI](https://img.shields.io/pypi/v/sendbird-platform-sdk.svg)](https://pypi.org/project/sendbird-platform-sdk)


This is a python library that makes talking to the [Sendbird Platform API](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api) easier. With this library you can extend your Sendbird integration to include advanced features like channel automation and user management.

# 🔥 Quick start

```python

import sendbird_platform_sdk
from sendbird_platform_sdk.api import user_api
from pprint import pprint


configuration = sendbird_platform_sdk.Configuration(
    host = "https://api-YOUR_APP_ID_FROM_DASHBOARD.sendbird.com"
)

with sendbird_platform_sdk.ApiClient(configuration=configuration) as api_client:
    api_instance = user_api.UserApi(api_client)
    api_token = "YOUR_MASTER_API_TOKEN_FROM_DASHBOARD"

    try:
        api_response = api_instance.list_users(api_token=api_token, limit=1)
        pprint(api_response)
    except sendbird_platform_sdk.ApiException as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```

# ⚒️ Prerequisite
In order to make requests with this SDK you will need you master API token. This can be found through the [Sendbird dashboard](https://dashboard.sendbird.com/).  Each app you create in Sendbird has its own master api token. These tokens can be found in Settings > Application > General.

![how to find you api token](https://i.imgur.com/0YMKtpX.png)

# 💻 Requirements 
This package has been tested with python version 3.9.10


# ⚙️ Installation 

Using pip

```bash
pip install sendbird-platform-sdk
```

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
| Announcement   | [docs/AnnouncementApi.md](docs/AnnouncementApi.md)|
| Bot | [docs/BotApi.md](docs/BotApi.md)  |
| GroupChannel | [docs/GroupChannelApi.md](docs/GroupChannelApi.md)  |
| Message | [docs/MessageApi.md](docs/MessageApi.md)  |
| OpenChannel | [docs/OpenChannelApi.md ](docs/OpenChannelApi.md)  |
| User | [docs/UserApi.md](docs/UserApi.md)  |
| Moderation | [docs/ModerationApi.md](docs/ModerationApi.md)  |
