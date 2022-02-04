"""
    Sendbird Platform SDK

    Sendbird Platform API Javascript SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from sendbird-platform-sdk.model_utils import (  # noqa: F401
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
from sendbird-platform-sdk.exceptions import ApiAttributeError



class CreateBotData(ModelNormal):
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
            'bot_userid': (str,),  # noqa: E501
            'bot_nickname': (str,),  # noqa: E501
            'bot_profile_url': (str,),  # noqa: E501
            'bot_type': (str,),  # noqa: E501
            'bot_callback_url': (str,),  # noqa: E501
            'is_privacy_mode': (bool,),  # noqa: E501
            'enable_mark_as_read': (bool,),  # noqa: E501
            'show_member': (bool,),  # noqa: E501
            'channel_invitation_preference': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'bot_userid': 'bot_userid',  # noqa: E501
        'bot_nickname': 'bot_nickname',  # noqa: E501
        'bot_profile_url': 'bot_profile_url',  # noqa: E501
        'bot_type': 'bot_type',  # noqa: E501
        'bot_callback_url': 'bot_callback_url',  # noqa: E501
        'is_privacy_mode': 'is_privacy_mode',  # noqa: E501
        'enable_mark_as_read': 'enable_mark_as_read',  # noqa: E501
        'show_member': 'show_member',  # noqa: E501
        'channel_invitation_preference': 'channel_invitation_preference',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, bot_userid, bot_nickname, bot_profile_url, bot_type, bot_callback_url, is_privacy_mode, enable_mark_as_read, show_member, channel_invitation_preference, *args, **kwargs):  # noqa: E501
        """CreateBotData - a model defined in OpenAPI

        Args:
            bot_userid (str): Specifies the unique ID of the bot. The length is limited to 80 characters.
            bot_nickname (str): Specifies the bot's nickname. The length is limited to 80 characters.
            bot_profile_url (str): Specifies the URL of the bot's profile image. The size is limited to 2,048 characters.
            bot_type (str): Specifies the type of the bot that you can specify for categorization. The length is limited to 128 characters.
            bot_callback_url (str): Specifies the server URL where bot is located to receive all events, requests, and data forwarded from an application. For security reasons, it is highly recommended that you use an SSL server. The length is limited to 1,024 characters.
            is_privacy_mode (bool): In the channels of where the bot is a member, determines whether to only forward the messages with the specific conditions to the bot or forword all messages to the bot, for privacy concerns. If set to true, only messages that start with a '/' or mention the bot_userid are forwarded to the bot. If set to false, all messages are forwarded.
            enable_mark_as_read (bool): Determines whether to mark the bot's message as read upon sending it. (Default: true)
            show_member (bool): Determines whether to include information about the members of each channel in a callback response. (Default: false)
            channel_invitation_preference (int):

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

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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

        self.bot_userid = bot_userid
        self.bot_nickname = bot_nickname
        self.bot_profile_url = bot_profile_url
        self.bot_type = bot_type
        self.bot_callback_url = bot_callback_url
        self.is_privacy_mode = is_privacy_mode
        self.enable_mark_as_read = enable_mark_as_read
        self.show_member = show_member
        self.channel_invitation_preference = channel_invitation_preference
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
    def __init__(self, bot_userid, bot_nickname, bot_profile_url, bot_type, bot_callback_url, is_privacy_mode, enable_mark_as_read, show_member, channel_invitation_preference, *args, **kwargs):  # noqa: E501
        """CreateBotData - a model defined in OpenAPI

        Args:
            bot_userid (str): Specifies the unique ID of the bot. The length is limited to 80 characters.
            bot_nickname (str): Specifies the bot's nickname. The length is limited to 80 characters.
            bot_profile_url (str): Specifies the URL of the bot's profile image. The size is limited to 2,048 characters.
            bot_type (str): Specifies the type of the bot that you can specify for categorization. The length is limited to 128 characters.
            bot_callback_url (str): Specifies the server URL where bot is located to receive all events, requests, and data forwarded from an application. For security reasons, it is highly recommended that you use an SSL server. The length is limited to 1,024 characters.
            is_privacy_mode (bool): In the channels of where the bot is a member, determines whether to only forward the messages with the specific conditions to the bot or forword all messages to the bot, for privacy concerns. If set to true, only messages that start with a '/' or mention the bot_userid are forwarded to the bot. If set to false, all messages are forwarded.
            enable_mark_as_read (bool): Determines whether to mark the bot's message as read upon sending it. (Default: true)
            show_member (bool): Determines whether to include information about the members of each channel in a callback response. (Default: false)
            channel_invitation_preference (int):

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

        self.bot_userid = bot_userid
        self.bot_nickname = bot_nickname
        self.bot_profile_url = bot_profile_url
        self.bot_type = bot_type
        self.bot_callback_url = bot_callback_url
        self.is_privacy_mode = is_privacy_mode
        self.enable_mark_as_read = enable_mark_as_read
        self.show_member = show_member
        self.channel_invitation_preference = channel_invitation_preference
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
