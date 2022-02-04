![Sendbird banner image](http://ww1.prweb.com/prfiles/2021/09/14/18371217/Sendbird_Logo_RGB_lg.png)

# [Sendbird Python Platform SDK](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api)


[![link to docs](https://img.shields.io/badge/SDK-docs-green)](/docs)

This is a python library that makes talking to the [Sendbird Platform API](https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api) easier. With this library you can extend your Sendbird integration to include advanced features like channel automation and user management.

# 🔥 Quick start

```python

import time
import sendbird-platform-sdk
from pprint import pprint
from sendbird-platform-sdk.api import advanced_analytics_api
from sendbird-platform-sdk.model.inline_response20062 import InlineResponse20062
# Defining the host is optional and defaults to https://api-APP_ID.sendbird.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sendbird-platform-sdk.Configuration(
    host = "https://api-APP_ID.sendbird.com"
)



# Enter a context with an instance of the API client
with sendbird-platform-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advanced_analytics_api.AdvancedAnalyticsApi(api_client)
    api_token = "{{API_TOKEN}}" # str |  (optional)

    try:
        # Retrieve Advanced analytics metrics
        api_response = api_instance.retrieve_advanced_analytics_metrics(api_token=api_token)
        pprint(api_response)
    except sendbird-platform-sdk.ApiException as e:
        print("Exception when calling AdvancedAnalyticsApi->retrieve_advanced_analytics_metrics: %s\n" % e)
```

# ⚒️ Prerequisite
In order to make requests with this SDK you will need you master API token. This can be found through the [Sendbird dashboard](https://dashboard.sendbird.com/).  Each app you create in Sendbird has its own master api token. These tokens can be found in Settings > Application > General.

![how to find you api token](https://i.imgur.com/0YMKtpX.png)

# 💻 Requirements 


# ⚙️ Installation 


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
