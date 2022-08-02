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


def lazy_import():
    from sendbird_platform_sdk.model.send_bird_group_channel import SendBirdGroupChannel
    from sendbird_platform_sdk.model.send_bird_group_channel_channel import SendBirdGroupChannelChannel
    from sendbird_platform_sdk.model.send_bird_group_channel_created_by import SendBirdGroupChannelCreatedBy
    from sendbird_platform_sdk.model.send_bird_group_channel_disappearing_message import SendBirdGroupChannelDisappearingMessage
    from sendbird_platform_sdk.model.send_bird_group_channel_sms_fallback import SendBirdGroupChannelSmsFallback
    from sendbird_platform_sdk.model.send_bird_member import SendBirdMember
    from sendbird_platform_sdk.model.send_bird_message_response import SendBirdMessageResponse
    from sendbird_platform_sdk.model.send_bird_open_channel import SendBirdOpenChannel
    from sendbird_platform_sdk.model.send_bird_user import SendBirdUser
    globals()['SendBirdGroupChannel'] = SendBirdGroupChannel
    globals()['SendBirdGroupChannelChannel'] = SendBirdGroupChannelChannel
    globals()['SendBirdGroupChannelCreatedBy'] = SendBirdGroupChannelCreatedBy
    globals()['SendBirdGroupChannelDisappearingMessage'] = SendBirdGroupChannelDisappearingMessage
    globals()['SendBirdGroupChannelSmsFallback'] = SendBirdGroupChannelSmsFallback
    globals()['SendBirdMember'] = SendBirdMember
    globals()['SendBirdMessageResponse'] = SendBirdMessageResponse
    globals()['SendBirdOpenChannel'] = SendBirdOpenChannel
    globals()['SendBirdUser'] = SendBirdUser


class SendBirdChannelResponse(ModelComposed):
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
        ('hidden_state',): {
            'HIDDEN_ALLOW_AUTO_UNHIDE': "hidden_allow_auto_unhide",
            'HIDDEN_PREVENT_AUTO_UNHIDE': "hidden_prevent_auto_unhide",
            'UNHIDDEN': "unhidden",
        },
        ('my_member_state',): {
            'INVITED': "invited",
            'JOINED': "joined",
            'NONE': "none",
        },
        ('my_muted_state',): {
            'MUTED': "muted",
            'UNMUTED': "unmuted",
        },
        ('my_push_trigger_option',): {
            'ALL': "all",
            'DEFAULT': "default",
            'MENTION_ONLY': "mention_only",
            'FALSE': "false",
        },
        ('my_role',): {
            'NONE': "none",
            'OPERATOR': "operator",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
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
        lazy_import()
        return {
            'channel_url': (str,),  # noqa: E501
            'cover_url': (str,),  # noqa: E501
            'created_at': (float,),  # noqa: E501
            'created_by': (SendBirdGroupChannelCreatedBy,),  # noqa: E501
            'creator': (SendBirdUser,),  # noqa: E501
            'custom_type': (str,),  # noqa: E501
            'data': (str,),  # noqa: E501
            'disappearing_message': (SendBirdGroupChannelDisappearingMessage,),  # noqa: E501
            'freeze': (bool,),  # noqa: E501
            'ignore_profanity_filter': (bool,),  # noqa: E501
            'hidden_state': (str,),  # noqa: E501
            'invited_at': (float,),  # noqa: E501
            'inviter': (SendBirdUser,),  # noqa: E501
            'is_access_code_required': (bool,),  # noqa: E501
            'is_broadcast': (bool,),  # noqa: E501
            'is_created': (bool,),  # noqa: E501
            'is_discoverable': (bool,),  # noqa: E501
            'is_distinct': (bool,),  # noqa: E501
            'is_ephemeral': (bool,),  # noqa: E501
            'is_frozen': (bool,),  # noqa: E501
            'is_hidden': (bool,),  # noqa: E501
            'is_public': (bool,),  # noqa: E501
            'is_push_enabled': (bool,),  # noqa: E501
            'is_super': (bool,),  # noqa: E501
            'joined_at': (float,),  # noqa: E501
            'joined_member_count': (float,),  # noqa: E501
            'last_message': (SendBirdMessageResponse,),  # noqa: E501
            'max_length_message': (float,),  # noqa: E501
            'member_count': (float,),  # noqa: E501
            'members': ([SendBirdMember],),  # noqa: E501
            'message_offset_timestamp': (float,),  # noqa: E501
            'message_survival_seconds': (float,),  # noqa: E501
            'my_count_preference': (str,),  # noqa: E501
            'my_last_read': (float,),  # noqa: E501
            'my_member_state': (str,),  # noqa: E501
            'my_muted_state': (str,),  # noqa: E501
            'my_push_trigger_option': (str,),  # noqa: E501
            'my_role': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'operators': ([SendBirdUser],),  # noqa: E501
            'sms_fallback': (SendBirdGroupChannelSmsFallback,),  # noqa: E501
            'unread_mention_count': (float,),  # noqa: E501
            'unread_message_count': (float,),  # noqa: E501
            'channel': (SendBirdGroupChannelChannel,),  # noqa: E501
            'is_dynamic_partitioned': (bool,),  # noqa: E501
            'participant_count': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'channel_url': 'channel_url',  # noqa: E501
        'cover_url': 'cover_url',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'creator': 'creator',  # noqa: E501
        'custom_type': 'custom_type',  # noqa: E501
        'data': 'data',  # noqa: E501
        'disappearing_message': 'disappearing_message',  # noqa: E501
        'freeze': 'freeze',  # noqa: E501
        'ignore_profanity_filter': 'ignore_profanity_filter',  # noqa: E501
        'hidden_state': 'hidden_state',  # noqa: E501
        'invited_at': 'invited_at',  # noqa: E501
        'inviter': 'inviter',  # noqa: E501
        'is_access_code_required': 'is_access_code_required',  # noqa: E501
        'is_broadcast': 'is_broadcast',  # noqa: E501
        'is_created': 'is_created',  # noqa: E501
        'is_discoverable': 'is_discoverable',  # noqa: E501
        'is_distinct': 'is_distinct',  # noqa: E501
        'is_ephemeral': 'is_ephemeral',  # noqa: E501
        'is_frozen': 'is_frozen',  # noqa: E501
        'is_hidden': 'is_hidden',  # noqa: E501
        'is_public': 'is_public',  # noqa: E501
        'is_push_enabled': 'is_push_enabled',  # noqa: E501
        'is_super': 'is_super',  # noqa: E501
        'joined_at': 'joined_at',  # noqa: E501
        'joined_member_count': 'joined_member_count',  # noqa: E501
        'last_message': 'last_message',  # noqa: E501
        'max_length_message': 'max_length_message',  # noqa: E501
        'member_count': 'member_count',  # noqa: E501
        'members': 'members',  # noqa: E501
        'message_offset_timestamp': 'message_offset_timestamp',  # noqa: E501
        'message_survival_seconds': 'message_survival_seconds',  # noqa: E501
        'my_count_preference': 'my_count_preference',  # noqa: E501
        'my_last_read': 'my_last_read',  # noqa: E501
        'my_member_state': 'my_member_state',  # noqa: E501
        'my_muted_state': 'my_muted_state',  # noqa: E501
        'my_push_trigger_option': 'my_push_trigger_option',  # noqa: E501
        'my_role': 'my_role',  # noqa: E501
        'name': 'name',  # noqa: E501
        'operators': 'operators',  # noqa: E501
        'sms_fallback': 'sms_fallback',  # noqa: E501
        'unread_mention_count': 'unread_mention_count',  # noqa: E501
        'unread_message_count': 'unread_message_count',  # noqa: E501
        'channel': 'channel',  # noqa: E501
        'is_dynamic_partitioned': 'is_dynamic_partitioned',  # noqa: E501
        'participant_count': 'participant_count',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SendBirdChannelResponse - a model defined in OpenAPI

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
            channel_url (str): [optional]  # noqa: E501
            cover_url (str): [optional]  # noqa: E501
            created_at (float): [optional]  # noqa: E501
            created_by (SendBirdGroupChannelCreatedBy): [optional]  # noqa: E501
            creator (SendBirdUser): [optional]  # noqa: E501
            custom_type (str): [optional]  # noqa: E501
            data (str): [optional]  # noqa: E501
            disappearing_message (SendBirdGroupChannelDisappearingMessage): [optional]  # noqa: E501
            freeze (bool): [optional]  # noqa: E501
            ignore_profanity_filter (bool): [optional]  # noqa: E501
            hidden_state (str): [optional]  # noqa: E501
            invited_at (float): [optional]  # noqa: E501
            inviter (SendBirdUser): [optional]  # noqa: E501
            is_access_code_required (bool): [optional]  # noqa: E501
            is_broadcast (bool): [optional]  # noqa: E501
            is_created (bool): [optional]  # noqa: E501
            is_discoverable (bool): [optional]  # noqa: E501
            is_distinct (bool): [optional]  # noqa: E501
            is_ephemeral (bool): [optional]  # noqa: E501
            is_frozen (bool): [optional]  # noqa: E501
            is_hidden (bool): [optional]  # noqa: E501
            is_public (bool): [optional]  # noqa: E501
            is_push_enabled (bool): [optional]  # noqa: E501
            is_super (bool): [optional]  # noqa: E501
            joined_at (float): [optional]  # noqa: E501
            joined_member_count (float): [optional]  # noqa: E501
            last_message (SendBirdMessageResponse): [optional]  # noqa: E501
            max_length_message (float): [optional]  # noqa: E501
            member_count (float): [optional]  # noqa: E501
            members ([SendBirdMember]): [optional]  # noqa: E501
            message_offset_timestamp (float): [optional]  # noqa: E501
            message_survival_seconds (float): [optional]  # noqa: E501
            my_count_preference (str): [optional]  # noqa: E501
            my_last_read (float): [optional]  # noqa: E501
            my_member_state (str): [optional]  # noqa: E501
            my_muted_state (str): [optional]  # noqa: E501
            my_push_trigger_option (str): [optional]  # noqa: E501
            my_role (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            operators ([SendBirdUser]): [optional]  # noqa: E501
            sms_fallback (SendBirdGroupChannelSmsFallback): [optional]  # noqa: E501
            unread_mention_count (float): [optional]  # noqa: E501
            unread_message_count (float): [optional]  # noqa: E501
            channel (SendBirdGroupChannelChannel): [optional]  # noqa: E501
            is_dynamic_partitioned (bool): [optional]  # noqa: E501
            participant_count (float): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SendBirdChannelResponse - a model defined in OpenAPI

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
            channel_url (str): [optional]  # noqa: E501
            cover_url (str): [optional]  # noqa: E501
            created_at (float): [optional]  # noqa: E501
            created_by (SendBirdGroupChannelCreatedBy): [optional]  # noqa: E501
            creator (SendBirdUser): [optional]  # noqa: E501
            custom_type (str): [optional]  # noqa: E501
            data (str): [optional]  # noqa: E501
            disappearing_message (SendBirdGroupChannelDisappearingMessage): [optional]  # noqa: E501
            freeze (bool): [optional]  # noqa: E501
            ignore_profanity_filter (bool): [optional]  # noqa: E501
            hidden_state (str): [optional]  # noqa: E501
            invited_at (float): [optional]  # noqa: E501
            inviter (SendBirdUser): [optional]  # noqa: E501
            is_access_code_required (bool): [optional]  # noqa: E501
            is_broadcast (bool): [optional]  # noqa: E501
            is_created (bool): [optional]  # noqa: E501
            is_discoverable (bool): [optional]  # noqa: E501
            is_distinct (bool): [optional]  # noqa: E501
            is_ephemeral (bool): [optional]  # noqa: E501
            is_frozen (bool): [optional]  # noqa: E501
            is_hidden (bool): [optional]  # noqa: E501
            is_public (bool): [optional]  # noqa: E501
            is_push_enabled (bool): [optional]  # noqa: E501
            is_super (bool): [optional]  # noqa: E501
            joined_at (float): [optional]  # noqa: E501
            joined_member_count (float): [optional]  # noqa: E501
            last_message (SendBirdMessageResponse): [optional]  # noqa: E501
            max_length_message (float): [optional]  # noqa: E501
            member_count (float): [optional]  # noqa: E501
            members ([SendBirdMember]): [optional]  # noqa: E501
            message_offset_timestamp (float): [optional]  # noqa: E501
            message_survival_seconds (float): [optional]  # noqa: E501
            my_count_preference (str): [optional]  # noqa: E501
            my_last_read (float): [optional]  # noqa: E501
            my_member_state (str): [optional]  # noqa: E501
            my_muted_state (str): [optional]  # noqa: E501
            my_push_trigger_option (str): [optional]  # noqa: E501
            my_role (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            operators ([SendBirdUser]): [optional]  # noqa: E501
            sms_fallback (SendBirdGroupChannelSmsFallback): [optional]  # noqa: E501
            unread_mention_count (float): [optional]  # noqa: E501
            unread_message_count (float): [optional]  # noqa: E501
            channel (SendBirdGroupChannelChannel): [optional]  # noqa: E501
            is_dynamic_partitioned (bool): [optional]  # noqa: E501
            participant_count (float): [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
              SendBirdGroupChannel,
              SendBirdOpenChannel,
          ],
          'allOf': [
          ],
          'oneOf': [
          ],
        }
