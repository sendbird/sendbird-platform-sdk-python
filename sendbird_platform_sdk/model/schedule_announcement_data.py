"""
    Sendbird Platform SDK

    Sendbird Platform API SDK  https://sendbird.com/docs/chat/v3/platform-api/getting-started/prepare-to-use-api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@sendbird.com
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
    from sendbird_platform_sdk.model.schedule_announcement_data_message import ScheduleAnnouncementDataMessage
    globals()['ScheduleAnnouncementDataMessage'] = ScheduleAnnouncementDataMessage


class ScheduleAnnouncementData(ModelNormal):
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
            'message': (ScheduleAnnouncementDataMessage,),  # noqa: E501
            'target_at': (str,),  # noqa: E501
            'target_list': ([str],),  # noqa: E501
            'target_channel_type': (str,),  # noqa: E501
            'message_type': (str,),  # noqa: E501
            'user_id': (str,),  # noqa: E501
            'content': (str,),  # noqa: E501
            'unique_id': (str,),  # noqa: E501
            'message_custom_type': (str,),  # noqa: E501
            'message_data': (str,),  # noqa: E501
            'create_channel': (bool,),  # noqa: E501
            'announcement_group': (str,),  # noqa: E501
            'create_channel_options': (str,),  # noqa: E501
            'create_channel_options_name': (str,),  # noqa: E501
            'create_channel_options_cover_url': (str,),  # noqa: E501
            'create_channel_options_custom_type': (str,),  # noqa: E501
            'create_channel_options_data': (str,),  # noqa: E501
            'create_channel_options_distinct': (str,),  # noqa: E501
            'scheduled_at': (int,),  # noqa: E501
            'cease_at': (str,),  # noqa: E501
            'resume_at': (str,),  # noqa: E501
            'end_at': (int,),  # noqa: E501
            'enable_push': (bool,),  # noqa: E501
            'assign_sender_as_channel_inviter': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'message': 'message',  # noqa: E501
        'target_at': 'target_at',  # noqa: E501
        'target_list': 'target_list',  # noqa: E501
        'target_channel_type': 'target_channel_type',  # noqa: E501
        'message_type': 'message_type',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
        'content': 'content',  # noqa: E501
        'unique_id': 'unique_id',  # noqa: E501
        'message_custom_type': 'message.custom_type',  # noqa: E501
        'message_data': 'message.data',  # noqa: E501
        'create_channel': 'create_channel',  # noqa: E501
        'announcement_group': 'announcement_group',  # noqa: E501
        'create_channel_options': 'create_channel_options',  # noqa: E501
        'create_channel_options_name': 'create_channel_options.name',  # noqa: E501
        'create_channel_options_cover_url': 'create_channel_options.cover_url',  # noqa: E501
        'create_channel_options_custom_type': 'create_channel_options.custom_type',  # noqa: E501
        'create_channel_options_data': 'create_channel_options.data',  # noqa: E501
        'create_channel_options_distinct': 'create_channel_options.distinct',  # noqa: E501
        'scheduled_at': 'scheduled_at',  # noqa: E501
        'cease_at': 'cease_at',  # noqa: E501
        'resume_at': 'resume_at',  # noqa: E501
        'end_at': 'end_at',  # noqa: E501
        'enable_push': 'enable_push',  # noqa: E501
        'assign_sender_as_channel_inviter': 'assign_sender_as_channel_inviter',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, message, target_at, target_list, target_channel_type, *args, **kwargs):  # noqa: E501
        """ScheduleAnnouncementData - a model defined in OpenAPI

        Args:
            message (ScheduleAnnouncementDataMessage):
            target_at (str): Specifies the target channels to send the announcement to. Acceptable values are the following: <br/> - sender_all_channels (Default): sends the announcement to all of the sender's group channels.<br />- target_channels: sends the announcement to all target group channels. When the `message.type` of the announcement is ADMM, this is the only valid option. <br /> - target_users_included_channels: sends the announcement to group channels consisting of the sender, target users, and other members. <br/> - target_users_only_channels: sends the announcement to group channels consisting of the sender and target users only.
            target_list ([str]): Specifies an array of one or more target user IDs or target channel URLs to send the announcement to when the target_at is  target_channels, target_users_only_channels, or target_users_included_channels.<br /><br />  When the target_at value is sender_all_channels, this property is not effective.
            target_channel_type (str): Determines which type of group channel to send the announcement to, based on the target_at and target_list. This property is effective only when the target_at is either target_users_only_channels or target_users_included_channels and the target_list is specified. Acceptable values are limited to the following:<br/>- all: send the announcement to all channels that have all target users and the sender in them, regardless of channel type.<br/>- distinct (default): sends this announcement to the distinct channels. Distinct channels continue to use the same existing channels whenever someone attempts to create a new channel with the same members.<br/>- non-distinct: sends this announcement to the non-distinct channels. Non-distinct channels always create a new channel even if there is an existing channel with the same members.<br/><br/> The distinct and non-distinct channels are a subtype of group channels, determined by the [is_distinct](/docs/chat/v3/platform-api/guides/group-channel#2-types-of-a-channel-3-resource-representation) property.

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
            message_type (str): Specifies the type of the message, which can be either MESG for a text message and ADMM for an admin message.. [optional]  # noqa: E501
            user_id (str): Specifies the unique ID of the sender when the message.type is MESG. When the message.type value is ADMM, this property is not effective.. [optional]  # noqa: E501
            content (str): Specifies the content of the message.. [optional]  # noqa: E501
            unique_id (str): Specifies the unique ID of the new announcement. The unique_id will be automatically created unless specified.. [optional]  # noqa: E501
            message_custom_type (str): Specifies the custom message type of the message of the new announcement.. [optional]  # noqa: E501
            message_data (str): Specifies additional message information such as custom font size, font type or `JSON` formatted string.. [optional]  # noqa: E501
            create_channel (bool): Determines whether to create a new channel if there is no existing channel that matches with the target options including target_at and target_list. By specifying the create_channel_options, you can configure the properties of newly created channels. (Default: false). [optional]  # noqa: E501
            announcement_group (str): Specifies the announcement group that the new announcement belongs to.<br/> <br/> This property is effective only when the target_at is either target_users_only_channels or target_users_included_channels.. [optional]  # noqa: E501
            create_channel_options (str): A newly created channel configuration.. [optional]  # noqa: E501
            create_channel_options_name (str): Specifies the name of channels to be created. (Default: Group Channel). [optional]  # noqa: E501
            create_channel_options_cover_url (str): Specifies the URL of the cover image for the new channels.. [optional]  # noqa: E501
            create_channel_options_custom_type (str): Specifies the custom channel type of the new channels.. [optional]  # noqa: E501
            create_channel_options_data (str): Specifies additional channel information such as a long description of the channel or `JSON` formatted string.. [optional]  # noqa: E501
            create_channel_options_distinct (str): Determines whether to create a [distinct](/docs/chat/v3/platform-api/guides/channel-types#2-group-channel) channel. (Default: true). [optional]  # noqa: E501
            scheduled_at (int): Specifies the time to start the announcement, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. If not specified, the default is the timestamp of when the request was delivered to Sendbird server. (Default: current timestamp). [optional]  # noqa: E501
            cease_at (str): Specifies the time to temporarily put the announcement on hold in UTC. The string is represented in HHMM format. This should be specified in conjunction with the resume_at property.<br/><br/> If both the cease_at and resume_at are not specified, Sendbird server starts to send the announcement at the time of the scheduled_at above.. [optional]  # noqa: E501
            resume_at (str): Specifies the time to automatically resume the on-hold announcement in UTC. The string is represented in HHMM format. This should be specified in conjunction with the cease_at property above.<br/><br/> If both the cease_at and resume_at are not specified, Sendbird server starts to send the announcement at the time of the scheduled_at above.. [optional]  # noqa: E501
            end_at (int): Specifies the time to permanently end the announcement, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous##2-timestamps) format. If this property is specified, the announcement ends even when the announcement is not sent to all its targets. <br/><br/> For the announcement to run safely, the end_at time should be set at least 10 minutes later than the scheduled_at time.. [optional]  # noqa: E501
            enable_push (bool): Determines whether to turn on push notification for the announcement. If set to true, push notifications will be sent for the announcement. (Default: true). [optional]  # noqa: E501
            assign_sender_as_channel_inviter (bool): Determines whether to assign an announcement sender as an inviter of the newly created channels. (Default: false). [optional]  # noqa: E501
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

        self.message = message
        self.target_at = target_at
        self.target_list = target_list
        self.target_channel_type = target_channel_type
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
    def __init__(self, message, target_at, target_list, target_channel_type, *args, **kwargs):  # noqa: E501
        """ScheduleAnnouncementData - a model defined in OpenAPI

        Args:
            message (ScheduleAnnouncementDataMessage):
            target_at (str): Specifies the target channels to send the announcement to. Acceptable values are the following: <br/> - sender_all_channels (Default): sends the announcement to all of the sender's group channels.<br />- target_channels: sends the announcement to all target group channels. When the `message.type` of the announcement is ADMM, this is the only valid option. <br /> - target_users_included_channels: sends the announcement to group channels consisting of the sender, target users, and other members. <br/> - target_users_only_channels: sends the announcement to group channels consisting of the sender and target users only.
            target_list ([str]): Specifies an array of one or more target user IDs or target channel URLs to send the announcement to when the target_at is  target_channels, target_users_only_channels, or target_users_included_channels.<br /><br />  When the target_at value is sender_all_channels, this property is not effective.
            target_channel_type (str): Determines which type of group channel to send the announcement to, based on the target_at and target_list. This property is effective only when the target_at is either target_users_only_channels or target_users_included_channels and the target_list is specified. Acceptable values are limited to the following:<br/>- all: send the announcement to all channels that have all target users and the sender in them, regardless of channel type.<br/>- distinct (default): sends this announcement to the distinct channels. Distinct channels continue to use the same existing channels whenever someone attempts to create a new channel with the same members.<br/>- non-distinct: sends this announcement to the non-distinct channels. Non-distinct channels always create a new channel even if there is an existing channel with the same members.<br/><br/> The distinct and non-distinct channels are a subtype of group channels, determined by the [is_distinct](/docs/chat/v3/platform-api/guides/group-channel#2-types-of-a-channel-3-resource-representation) property.

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
            message_type (str): Specifies the type of the message, which can be either MESG for a text message and ADMM for an admin message.. [optional]  # noqa: E501
            user_id (str): Specifies the unique ID of the sender when the message.type is MESG. When the message.type value is ADMM, this property is not effective.. [optional]  # noqa: E501
            content (str): Specifies the content of the message.. [optional]  # noqa: E501
            unique_id (str): Specifies the unique ID of the new announcement. The unique_id will be automatically created unless specified.. [optional]  # noqa: E501
            message_custom_type (str): Specifies the custom message type of the message of the new announcement.. [optional]  # noqa: E501
            message_data (str): Specifies additional message information such as custom font size, font type or `JSON` formatted string.. [optional]  # noqa: E501
            create_channel (bool): Determines whether to create a new channel if there is no existing channel that matches with the target options including target_at and target_list. By specifying the create_channel_options, you can configure the properties of newly created channels. (Default: false). [optional]  # noqa: E501
            announcement_group (str): Specifies the announcement group that the new announcement belongs to.<br/> <br/> This property is effective only when the target_at is either target_users_only_channels or target_users_included_channels.. [optional]  # noqa: E501
            create_channel_options (str): A newly created channel configuration.. [optional]  # noqa: E501
            create_channel_options_name (str): Specifies the name of channels to be created. (Default: Group Channel). [optional]  # noqa: E501
            create_channel_options_cover_url (str): Specifies the URL of the cover image for the new channels.. [optional]  # noqa: E501
            create_channel_options_custom_type (str): Specifies the custom channel type of the new channels.. [optional]  # noqa: E501
            create_channel_options_data (str): Specifies additional channel information such as a long description of the channel or `JSON` formatted string.. [optional]  # noqa: E501
            create_channel_options_distinct (str): Determines whether to create a [distinct](/docs/chat/v3/platform-api/guides/channel-types#2-group-channel) channel. (Default: true). [optional]  # noqa: E501
            scheduled_at (int): Specifies the time to start the announcement, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. If not specified, the default is the timestamp of when the request was delivered to Sendbird server. (Default: current timestamp). [optional]  # noqa: E501
            cease_at (str): Specifies the time to temporarily put the announcement on hold in UTC. The string is represented in HHMM format. This should be specified in conjunction with the resume_at property.<br/><br/> If both the cease_at and resume_at are not specified, Sendbird server starts to send the announcement at the time of the scheduled_at above.. [optional]  # noqa: E501
            resume_at (str): Specifies the time to automatically resume the on-hold announcement in UTC. The string is represented in HHMM format. This should be specified in conjunction with the cease_at property above.<br/><br/> If both the cease_at and resume_at are not specified, Sendbird server starts to send the announcement at the time of the scheduled_at above.. [optional]  # noqa: E501
            end_at (int): Specifies the time to permanently end the announcement, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous##2-timestamps) format. If this property is specified, the announcement ends even when the announcement is not sent to all its targets. <br/><br/> For the announcement to run safely, the end_at time should be set at least 10 minutes later than the scheduled_at time.. [optional]  # noqa: E501
            enable_push (bool): Determines whether to turn on push notification for the announcement. If set to true, push notifications will be sent for the announcement. (Default: true). [optional]  # noqa: E501
            assign_sender_as_channel_inviter (bool): Determines whether to assign an announcement sender as an inviter of the newly created channels. (Default: false). [optional]  # noqa: E501
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

        self.message = message
        self.target_at = target_at
        self.target_list = target_list
        self.target_channel_type = target_channel_type
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
