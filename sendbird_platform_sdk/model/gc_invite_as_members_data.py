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



class GcInviteAsMembersData(ModelNormal):
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
            'channel_url': (str,),  # noqa: E501
            'user_ids': ([str],),  # noqa: E501
            'users': ([str],),  # noqa: E501
            'invitation_status': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'hidden_status': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'channel_url': 'channel_url',  # noqa: E501
        'user_ids': 'user_ids',  # noqa: E501
        'users': 'users',  # noqa: E501
        'invitation_status': 'invitation_status',  # noqa: E501
        'hidden_status': 'hidden_status',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, channel_url, user_ids, users, invitation_status, hidden_status, *args, **kwargs):  # noqa: E501
        """GcInviteAsMembersData - a model defined in OpenAPI

        Args:
            channel_url (str): Specifies the URL of the channel to invite into.
            user_ids ([str]): Specifies an array of one or more user IDs to invite into the channel. The maximum number of users to be invited at once is 100. The users can be used instead of this property.
            users ([str]): Specifies a list of one or more `JSON` objects which contain the user_id property to invite into the channel. The maximum number of users to be invited at once is 100. The user_ids can be used instead of this property.
            invitation_status ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies one or more key-value pair items which set the invitation status of each user invited to the channel. The key should be a user_id and the value should be their joining status. Acceptable values are joined, invited_by_friend, and invited_by_non_friend. (Default: joined)
            hidden_status ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies one or more key-value pair items which set the channel's hidden status for each user. The key should be a user_id and the value should be their hidden status. Acceptable values are limited to the following:<br />- unhidden (default): the channel is included in when retrieving a list of group channels.<br />- hidden_allow_auto_unhide: the channel automatically gets unhidden when receiving a new message.<br />- hidden_prevent_auto_unhide: the channel keeps hidden though receiving a new message.

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

        self.channel_url = channel_url
        self.user_ids = user_ids
        self.users = users
        self.invitation_status = invitation_status
        self.hidden_status = hidden_status
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
    def __init__(self, channel_url, user_ids, users, invitation_status, hidden_status, *args, **kwargs):  # noqa: E501
        """GcInviteAsMembersData - a model defined in OpenAPI

        Args:
            channel_url (str): Specifies the URL of the channel to invite into.
            user_ids ([str]): Specifies an array of one or more user IDs to invite into the channel. The maximum number of users to be invited at once is 100. The users can be used instead of this property.
            users ([str]): Specifies a list of one or more `JSON` objects which contain the user_id property to invite into the channel. The maximum number of users to be invited at once is 100. The user_ids can be used instead of this property.
            invitation_status ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies one or more key-value pair items which set the invitation status of each user invited to the channel. The key should be a user_id and the value should be their joining status. Acceptable values are joined, invited_by_friend, and invited_by_non_friend. (Default: joined)
            hidden_status ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies one or more key-value pair items which set the channel's hidden status for each user. The key should be a user_id and the value should be their hidden status. Acceptable values are limited to the following:<br />- unhidden (default): the channel is included in when retrieving a list of group channels.<br />- hidden_allow_auto_unhide: the channel automatically gets unhidden when receiving a new message.<br />- hidden_prevent_auto_unhide: the channel keeps hidden though receiving a new message.

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

        self.channel_url = channel_url
        self.user_ids = user_ids
        self.users = users
        self.invitation_status = invitation_status
        self.hidden_status = hidden_status
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
