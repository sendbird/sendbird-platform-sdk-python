
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from sendbird_platform_sdk.api.announcement_api import AnnouncementApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from sendbird_platform_sdk.api.announcement_api import AnnouncementApi
from sendbird_platform_sdk.api.bot_api import BotApi
from sendbird_platform_sdk.api.group_channel_api import GroupChannelApi
from sendbird_platform_sdk.api.message_api import MessageApi
from sendbird_platform_sdk.api.metadata_api import MetadataApi
from sendbird_platform_sdk.api.moderation_api import ModerationApi
from sendbird_platform_sdk.api.open_channel_api import OpenChannelApi
from sendbird_platform_sdk.api.statistics_api import StatisticsApi
from sendbird_platform_sdk.api.user_api import UserApi
