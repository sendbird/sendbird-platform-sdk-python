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



class GcCreateChannelData(ModelNormal):
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
            'user_ids': ([str],),  # noqa: E501
            'users': ([str],),  # noqa: E501
            'name': (str,),  # noqa: E501
            'channel_url': (str,),  # noqa: E501
            'cover_url': (str,),  # noqa: E501
            'cover_file': (file_type,),  # noqa: E501
            'custom_type': (str,),  # noqa: E501
            'data': (str,),  # noqa: E501
            'is_distinct': (bool,),  # noqa: E501
            'is_public': (bool,),  # noqa: E501
            'is_super': (bool,),  # noqa: E501
            'is_ephemeral': (bool,),  # noqa: E501
            'access_code': (str,),  # noqa: E501
            'inviter_id': (str,),  # noqa: E501
            'strict': (bool,),  # noqa: E501
            'invitation_status': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'hidden_status': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'operator_ids': ([str],),  # noqa: E501
            'block_sdk_user_channel_join': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'user_ids': 'user_ids',  # noqa: E501
        'users': 'users',  # noqa: E501
        'name': 'name',  # noqa: E501
        'channel_url': 'channel_url',  # noqa: E501
        'cover_url': 'cover_url',  # noqa: E501
        'cover_file': 'cover_file',  # noqa: E501
        'custom_type': 'custom_type',  # noqa: E501
        'data': 'data',  # noqa: E501
        'is_distinct': 'is_distinct',  # noqa: E501
        'is_public': 'is_public',  # noqa: E501
        'is_super': 'is_super',  # noqa: E501
        'is_ephemeral': 'is_ephemeral',  # noqa: E501
        'access_code': 'access_code',  # noqa: E501
        'inviter_id': 'inviter_id',  # noqa: E501
        'strict': 'strict',  # noqa: E501
        'invitation_status': 'invitation_status',  # noqa: E501
        'hidden_status': 'hidden_status',  # noqa: E501
        'operator_ids': 'operator_ids',  # noqa: E501
        'block_sdk_user_channel_join': 'block_sdk_user_channel_join',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, user_ids, *args, **kwargs):  # noqa: E501
        """GcCreateChannelData - a model defined in OpenAPI

        Args:
            user_ids ([str]): Specifies an array of one or more IDs of users to invite to the channel. The maximum number of users to be invited at once is 100. The users below and this property can be used interchangeably.

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
            users ([str]): Specifies an array of one or more IDs of users to invite to the channel. The maximum number of users to be invited at once is 100. The user_ids above and this property can be used interchangeably.. [optional]  # noqa: E501
            name (str): Specifies the name of the channel, or the channel topic. The length is limited to 191 characters. (Default: group channel). [optional]  # noqa: E501
            channel_url (str): Specifies the URL of the channel. Only numbers, characters, and underscores are allowed. The length is 4 to 100 characters, inclusive. If not specified, a URL is automatically generated.. [optional]  # noqa: E501
            cover_url (str): Specifies the URL of the cover image for the channel. The length is limited to 2,048 characters.. [optional]  # noqa: E501
            cover_file (file_type): Uploads the cover image file for the channel.. [optional]  # noqa: E501
            custom_type (str): Specifies the custom channel type which is used for channel grouping. The length is limited to 128 characters.<br /><br /> Custom types are also used within Sendbird's [Advanced analytics](/docs/chat/v3/platform-api/guides/advanced-analytics) to segment metrics, which enables the sub-classification of data views.. [optional]  # noqa: E501
            data (str): Specifies additional channel information such as a long description of the channel or `JSON` formatted string.. [optional]  # noqa: E501
            is_distinct (bool): Determines whether to reuse an existing channel or create a new channel. If set to true, returns a channel with the same users in the user_ids or users property or creates a new channel if no match is found. Sendbird server can also use the custom channel type in the custom_type property if specified along with the users to return the corresponding channel. If set to false, Sendbird server always creates a new channel with a combination of the users as well as the channel custom type if specified. (Default: false)<br /><br /> Under this property, Sendbird server does not distinguish channels based on other properties such as channel URL or channel name.. [optional]  # noqa: E501
            is_public (bool): Determines whether to allow a user to join the channel without an invitation. (Default: false). [optional]  # noqa: E501
            is_super (bool): Determines whether to allow the channel to accommodate more than 2,000 members. (Default: false) <br/><br/> Supergroup channels are not supported with the is_distinct property and the property is false by default.. [optional]  # noqa: E501
            is_ephemeral (bool): Determines whether to preserve the messages in the channel for the purpose of retrieving chat history. (Default: false). [optional]  # noqa: E501
            access_code (str): This parameter can only be used when the channel operator creates a public group channel. They can set an access code for the corresponding type of channel. The channel then requires the specified access code to a user who attempts to join. If specified, the is_access_code_required property of the channel resource is set to true.. [optional]  # noqa: E501
            inviter_id (str): Specifies the ID of the user who has invited other users as members of the channel. The inviter is not automatically registered to the channel as a member, so you should specify the ID of the inviter in the user_ids property below if needed.. [optional]  # noqa: E501
            strict (bool): Determines whether to receive a `400111` error and cease channel creation when there is at least one non-existing user in the specified user_ids or users property above. If set to false, the channel will be created excluding the non-existing users without receiving the mentioned error. (Default: false). [optional]  # noqa: E501
            invitation_status ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies one or more key-value pair items which set the invitation status of each user invited to the channel. The key should be a user_id and the value should be their joining status. Acceptable values are joined, invited_by_friend, and invited_by_non_friend. (Default: joined). [optional]  # noqa: E501
            hidden_status ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies one or more key-value pair items which set the channel's hidden status for each user. The key should be a user_id and the value should be their hidden status. Acceptable values are limited to the following:<br />- unhidden (default): the channel is included in when retrieving a list of group channels.<br />- hidden_allow_auto_unhide: the channel automatically gets unhidden when receiving a new message.<br />- hidden_prevent_auto_unhide: the channel keeps hidden though receiving a new message.. [optional]  # noqa: E501
            operator_ids ([str]): Specifies an array of one or more IDs of users to register as operators of the channel. You should also include these IDs in the user_ids property to invite them to the channel as members. They can delete any messages in the channel, and also view all messages without any filtering or throttling. The maximum allowed number of operators per channel is 100.. [optional]  # noqa: E501
            block_sdk_user_channel_join (bool): Determines whether to block users from joining the channel through the Chat SDK. This parameter can be used in order to restrict the ways for users to join the channel, and only using the [join a channel](#2-join-a-channel) action can add a user to the channel. (Default: false). [optional]  # noqa: E501
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

        self.user_ids = user_ids
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
    def __init__(self, user_ids, *args, **kwargs):  # noqa: E501
        """GcCreateChannelData - a model defined in OpenAPI

        Args:
            user_ids ([str]): Specifies an array of one or more IDs of users to invite to the channel. The maximum number of users to be invited at once is 100. The users below and this property can be used interchangeably.

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
            users ([str]): Specifies an array of one or more IDs of users to invite to the channel. The maximum number of users to be invited at once is 100. The user_ids above and this property can be used interchangeably.. [optional]  # noqa: E501
            name (str): Specifies the name of the channel, or the channel topic. The length is limited to 191 characters. (Default: group channel). [optional]  # noqa: E501
            channel_url (str): Specifies the URL of the channel. Only numbers, characters, and underscores are allowed. The length is 4 to 100 characters, inclusive. If not specified, a URL is automatically generated.. [optional]  # noqa: E501
            cover_url (str): Specifies the URL of the cover image for the channel. The length is limited to 2,048 characters.. [optional]  # noqa: E501
            cover_file (file_type): Uploads the cover image file for the channel.. [optional]  # noqa: E501
            custom_type (str): Specifies the custom channel type which is used for channel grouping. The length is limited to 128 characters.<br /><br /> Custom types are also used within Sendbird's [Advanced analytics](/docs/chat/v3/platform-api/guides/advanced-analytics) to segment metrics, which enables the sub-classification of data views.. [optional]  # noqa: E501
            data (str): Specifies additional channel information such as a long description of the channel or `JSON` formatted string.. [optional]  # noqa: E501
            is_distinct (bool): Determines whether to reuse an existing channel or create a new channel. If set to true, returns a channel with the same users in the user_ids or users property or creates a new channel if no match is found. Sendbird server can also use the custom channel type in the custom_type property if specified along with the users to return the corresponding channel. If set to false, Sendbird server always creates a new channel with a combination of the users as well as the channel custom type if specified. (Default: false)<br /><br /> Under this property, Sendbird server does not distinguish channels based on other properties such as channel URL or channel name.. [optional]  # noqa: E501
            is_public (bool): Determines whether to allow a user to join the channel without an invitation. (Default: false). [optional]  # noqa: E501
            is_super (bool): Determines whether to allow the channel to accommodate more than 2,000 members. (Default: false) <br/><br/> Supergroup channels are not supported with the is_distinct property and the property is false by default.. [optional]  # noqa: E501
            is_ephemeral (bool): Determines whether to preserve the messages in the channel for the purpose of retrieving chat history. (Default: false). [optional]  # noqa: E501
            access_code (str): This parameter can only be used when the channel operator creates a public group channel. They can set an access code for the corresponding type of channel. The channel then requires the specified access code to a user who attempts to join. If specified, the is_access_code_required property of the channel resource is set to true.. [optional]  # noqa: E501
            inviter_id (str): Specifies the ID of the user who has invited other users as members of the channel. The inviter is not automatically registered to the channel as a member, so you should specify the ID of the inviter in the user_ids property below if needed.. [optional]  # noqa: E501
            strict (bool): Determines whether to receive a `400111` error and cease channel creation when there is at least one non-existing user in the specified user_ids or users property above. If set to false, the channel will be created excluding the non-existing users without receiving the mentioned error. (Default: false). [optional]  # noqa: E501
            invitation_status ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies one or more key-value pair items which set the invitation status of each user invited to the channel. The key should be a user_id and the value should be their joining status. Acceptable values are joined, invited_by_friend, and invited_by_non_friend. (Default: joined). [optional]  # noqa: E501
            hidden_status ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies one or more key-value pair items which set the channel's hidden status for each user. The key should be a user_id and the value should be their hidden status. Acceptable values are limited to the following:<br />- unhidden (default): the channel is included in when retrieving a list of group channels.<br />- hidden_allow_auto_unhide: the channel automatically gets unhidden when receiving a new message.<br />- hidden_prevent_auto_unhide: the channel keeps hidden though receiving a new message.. [optional]  # noqa: E501
            operator_ids ([str]): Specifies an array of one or more IDs of users to register as operators of the channel. You should also include these IDs in the user_ids property to invite them to the channel as members. They can delete any messages in the channel, and also view all messages without any filtering or throttling. The maximum allowed number of operators per channel is 100.. [optional]  # noqa: E501
            block_sdk_user_channel_join (bool): Determines whether to block users from joining the channel through the Chat SDK. This parameter can be used in order to restrict the ways for users to join the channel, and only using the [join a channel](#2-join-a-channel) action can add a user to the channel. (Default: false). [optional]  # noqa: E501
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

        self.user_ids = user_ids
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
