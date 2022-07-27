"""
    Sendbird Platform SDK

    Sendbird Platform API Javascript SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from sendbird_platform_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from sendbird_platform_sdk.exceptions import ApiAttributeError



class UpdatePushPreferencesData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'push_trigger_option': (str,),  # noqa: E501
            'do_not_disturb': (bool,),  # noqa: E501
            'start_hour': (int,),  # noqa: E501
            'start_min': (int,),  # noqa: E501
            'end_hour': (int,),  # noqa: E501
            'end_min': (int,),  # noqa: E501
            'snooze_enabled': (bool,),  # noqa: E501
            'snooze_start_ts': (int,),  # noqa: E501
            'snooze_end_ts': (int,),  # noqa: E501
            'block_push_from_bots': (bool,),  # noqa: E501
            'push_blocked_bot_ids': ([int],),  # noqa: E501
            'timezone': (str,),  # noqa: E501
            'push_sound': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'push_trigger_option': 'push_trigger_option',  # noqa: E501
        'do_not_disturb': 'do_not_disturb',  # noqa: E501
        'start_hour': 'start_hour',  # noqa: E501
        'start_min': 'start_min',  # noqa: E501
        'end_hour': 'end_hour',  # noqa: E501
        'end_min': 'end_min',  # noqa: E501
        'snooze_enabled': 'snooze_enabled',  # noqa: E501
        'snooze_start_ts': 'snooze_start_ts',  # noqa: E501
        'snooze_end_ts': 'snooze_end_ts',  # noqa: E501
        'block_push_from_bots': 'block_push_from_bots',  # noqa: E501
        'push_blocked_bot_ids': 'push_blocked_bot_ids',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'push_sound': 'push_sound',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, push_trigger_option, do_not_disturb, start_hour, start_min, end_hour, end_min, snooze_enabled, snooze_start_ts, snooze_end_ts, block_push_from_bots, push_blocked_bot_ids, timezone, push_sound, *args, **kwargs):  # noqa: E501
        """UpdatePushPreferencesData - a model defined in OpenAPI

        Args:
            push_trigger_option (str): Determines the type of push notification trigger to apply to the user's joined group channels. Valid values are the following:<br />- all (default): when disconnected from Sendbird server, the user receives notifications for all new messages including mentioned messages the user has been mentioned in.<br />- mention_only: when disconnected from Sendbird server, the user only receives notifications for messages the user has been mentioned in.<br />- off: the user doesn't receive any notifications.
            do_not_disturb (bool): Determines whether to pause notification messages for the user during a specific time of day. (Default: false)
            start_hour (int): Specifies the hour to start pausing the notifications for Do Not Disturb of the user.
            start_min (int): Specifies the minute of the hour to start pausing the notifications for Do Not Disturb of the user.
            end_hour (int): Specifies the hour to stop pausing the notifications for Do Not Disturb of the user.
            end_min (int): Specifies the minute of the hour to stop pausing the notifications for Do Not Disturb of the user.
            snooze_enabled (bool): Determines whether to snooze notification messages for the user during a specific period of time. (Default: false)
            snooze_start_ts (int): Specifies the timestamp of when to start snoozing the notifications, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps).
            snooze_end_ts (int): Specifies the timestamp of when to end snoozing the notifications, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps).
            block_push_from_bots (bool): Determines whether to block push notifications from [all bots](/docs/chat/v3/platform-api/guides/bot-interface#2-list-bots) within the application. If the push_blocked_bot_ids is specified, notifications only from the bots in the property are blocked. (Default: false)
            push_blocked_bot_ids ([int]): Specifies an array of one or more IDs of bots whose push notifications are blocked. This property is effective only when the block_push_from_bots is set to true.
            timezone (str): Specifies the timezone to be applied to push preferences with a value such as UTC, Asia/Seoul, Europe/London, etc.
            push_sound (str): Specifies the name of a sound file to be played when a push notification is delivered to your client app.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.push_trigger_option = push_trigger_option
        self.do_not_disturb = do_not_disturb
        self.start_hour = start_hour
        self.start_min = start_min
        self.end_hour = end_hour
        self.end_min = end_min
        self.snooze_enabled = snooze_enabled
        self.snooze_start_ts = snooze_start_ts
        self.snooze_end_ts = snooze_end_ts
        self.block_push_from_bots = block_push_from_bots
        self.push_blocked_bot_ids = push_blocked_bot_ids
        self.timezone = timezone
        self.push_sound = push_sound
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, push_trigger_option, do_not_disturb, start_hour, start_min, end_hour, end_min, snooze_enabled, snooze_start_ts, snooze_end_ts, block_push_from_bots, push_blocked_bot_ids, timezone, push_sound, *args, **kwargs):  # noqa: E501
        """UpdatePushPreferencesData - a model defined in OpenAPI

        Args:
            push_trigger_option (str): Determines the type of push notification trigger to apply to the user's joined group channels. Valid values are the following:<br />- all (default): when disconnected from Sendbird server, the user receives notifications for all new messages including mentioned messages the user has been mentioned in.<br />- mention_only: when disconnected from Sendbird server, the user only receives notifications for messages the user has been mentioned in.<br />- off: the user doesn't receive any notifications.
            do_not_disturb (bool): Determines whether to pause notification messages for the user during a specific time of day. (Default: false)
            start_hour (int): Specifies the hour to start pausing the notifications for Do Not Disturb of the user.
            start_min (int): Specifies the minute of the hour to start pausing the notifications for Do Not Disturb of the user.
            end_hour (int): Specifies the hour to stop pausing the notifications for Do Not Disturb of the user.
            end_min (int): Specifies the minute of the hour to stop pausing the notifications for Do Not Disturb of the user.
            snooze_enabled (bool): Determines whether to snooze notification messages for the user during a specific period of time. (Default: false)
            snooze_start_ts (int): Specifies the timestamp of when to start snoozing the notifications, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps).
            snooze_end_ts (int): Specifies the timestamp of when to end snoozing the notifications, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps).
            block_push_from_bots (bool): Determines whether to block push notifications from [all bots](/docs/chat/v3/platform-api/guides/bot-interface#2-list-bots) within the application. If the push_blocked_bot_ids is specified, notifications only from the bots in the property are blocked. (Default: false)
            push_blocked_bot_ids ([int]): Specifies an array of one or more IDs of bots whose push notifications are blocked. This property is effective only when the block_push_from_bots is set to true.
            timezone (str): Specifies the timezone to be applied to push preferences with a value such as UTC, Asia/Seoul, Europe/London, etc.
            push_sound (str): Specifies the name of a sound file to be played when a push notification is delivered to your client app.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.push_trigger_option = push_trigger_option
        self.do_not_disturb = do_not_disturb
        self.start_hour = start_hour
        self.start_min = start_min
        self.end_hour = end_hour
        self.end_min = end_min
        self.snooze_enabled = snooze_enabled
        self.snooze_start_ts = snooze_start_ts
        self.snooze_end_ts = snooze_end_ts
        self.block_push_from_bots = block_push_from_bots
        self.push_blocked_bot_ids = push_blocked_bot_ids
        self.timezone = timezone
        self.push_sound = push_sound
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
