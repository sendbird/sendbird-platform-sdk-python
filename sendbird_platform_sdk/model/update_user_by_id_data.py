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



class UpdateUserByIdData(ModelNormal):
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
            'user_id': (str,),  # noqa: E501
            'nickname': (str,),  # noqa: E501
            'profile_url': (str,),  # noqa: E501
            'profile_file': (file_type,),  # noqa: E501
            'issue_access_token': (bool,),  # noqa: E501
            'issue_session_token': (bool,),  # noqa: E501
            'session_token_expires_at': (int,),  # noqa: E501
            'is_active': (bool,),  # noqa: E501
            'last_seen_at': (int,),  # noqa: E501
            'discovery_keys': ([str],),  # noqa: E501
            'preferred_languages': ([str],),  # noqa: E501
            'leave_all_when_deactivated': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'user_id': 'user_id',  # noqa: E501
        'nickname': 'nickname',  # noqa: E501
        'profile_url': 'profile_url',  # noqa: E501
        'profile_file': 'profile_file',  # noqa: E501
        'issue_access_token': 'issue_access_token',  # noqa: E501
        'issue_session_token': 'issue_session_token',  # noqa: E501
        'session_token_expires_at': 'session_token_expires_at',  # noqa: E501
        'is_active': 'is_active',  # noqa: E501
        'last_seen_at': 'last_seen_at',  # noqa: E501
        'discovery_keys': 'discovery_keys',  # noqa: E501
        'preferred_languages': 'preferred_languages',  # noqa: E501
        'leave_all_when_deactivated': 'leave_all_when_deactivated',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, user_id, nickname, profile_url, *args, **kwargs):  # noqa: E501
        """UpdateUserByIdData - a model defined in OpenAPI

        Args:
            user_id (str): Specifies the unique ID of the user to update.
            nickname (str): Specifies the user's nickname. The length is limited to 80 characters.
            profile_url (str): Specifies the URL of the user's profile image. The length is limited to 2,048 characters.<br /><br /> The [domain filter](/docs/chat/v3/platform-api/guides/filter-and-moderation#2-domain-filter) filters out the request if the value of this property matches the filter's domain set.

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
            profile_file (file_type): Uploads the file of the user's profile image. An acceptable image is limited to `JPG` (.jpg), `JPEG` (.jpeg), or `PNG` (.png) file of up to 25 MB.. [optional]  # noqa: E501
            issue_access_token (bool): Determines whether to revoke the existing access token and create a new one for the user. If true, an opaque string token is issued and provided upon creation, which should be passed whenever the user logs in. If false, an access token is not required when the user logs in. (Default: false). [optional]  # noqa: E501
            issue_session_token (bool): Determines whether to add a new session token for the user. If true, an opaque string token is issued and provided upon creation, which should be passed whenever the user logs in. If false, a session token is not required when the user logs in. (Default: false). [optional]  # noqa: E501
            session_token_expires_at (int): Specifies the time for the issued session token to expire in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. The length should be 13. If not specified and the issue_session_token property above is true, the value of this property is set to the sum of the current timestamp and 604800000 by default, which indicates that the token will be valid for the next 7 days starting from the current timestamp.. [optional]  # noqa: E501
            is_active (bool): Determines whether to activate or deactivate the user within the application.. [optional]  # noqa: E501
            last_seen_at (int): Specifies the time when the user goes offline, to indicate when they were last online, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format.. [optional]  # noqa: E501
            discovery_keys ([str]): Specifies an array of unique keys of the user which is provided to Sendbird server for discovering friends. By using the keys, the server can identify and match the user with other users.. [optional]  # noqa: E501
            preferred_languages ([str]): Specifies an array of one or more [language codes](/docs/chat/v3/platform-api/guides/miscellaneous#2-language-codes-for-auto-translation) to translate notification messages to preferred languages. Up to 4 languages can be set for the user. If messages are sent in one of the preferred languages, notification messages won't be translated. If messages are sent in a language other than the preferred languages, notification messages will be translated into the first language in the array. In addition, the messages translated into other preferred languages will be provided in the `sendbird` property of a notification message payload.. [optional]  # noqa: E501
            leave_all_when_deactivated (bool): Determines whether the user leaves all joined group channels upon deactivation. Note that this value is true by default. Use in conjunction with the is_active property above.. [optional]  # noqa: E501
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

        self.user_id = user_id
        self.nickname = nickname
        self.profile_url = profile_url
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
    def __init__(self, user_id, nickname, profile_url, *args, **kwargs):  # noqa: E501
        """UpdateUserByIdData - a model defined in OpenAPI

        Args:
            user_id (str): Specifies the unique ID of the user to update.
            nickname (str): Specifies the user's nickname. The length is limited to 80 characters.
            profile_url (str): Specifies the URL of the user's profile image. The length is limited to 2,048 characters.<br /><br /> The [domain filter](/docs/chat/v3/platform-api/guides/filter-and-moderation#2-domain-filter) filters out the request if the value of this property matches the filter's domain set.

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
            profile_file (file_type): Uploads the file of the user's profile image. An acceptable image is limited to `JPG` (.jpg), `JPEG` (.jpeg), or `PNG` (.png) file of up to 25 MB.. [optional]  # noqa: E501
            issue_access_token (bool): Determines whether to revoke the existing access token and create a new one for the user. If true, an opaque string token is issued and provided upon creation, which should be passed whenever the user logs in. If false, an access token is not required when the user logs in. (Default: false). [optional]  # noqa: E501
            issue_session_token (bool): Determines whether to add a new session token for the user. If true, an opaque string token is issued and provided upon creation, which should be passed whenever the user logs in. If false, a session token is not required when the user logs in. (Default: false). [optional]  # noqa: E501
            session_token_expires_at (int): Specifies the time for the issued session token to expire in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format. The length should be 13. If not specified and the issue_session_token property above is true, the value of this property is set to the sum of the current timestamp and 604800000 by default, which indicates that the token will be valid for the next 7 days starting from the current timestamp.. [optional]  # noqa: E501
            is_active (bool): Determines whether to activate or deactivate the user within the application.. [optional]  # noqa: E501
            last_seen_at (int): Specifies the time when the user goes offline, to indicate when they were last online, in [Unix milliseconds](/docs/chat/v3/platform-api/guides/miscellaneous#2-timestamps) format.. [optional]  # noqa: E501
            discovery_keys ([str]): Specifies an array of unique keys of the user which is provided to Sendbird server for discovering friends. By using the keys, the server can identify and match the user with other users.. [optional]  # noqa: E501
            preferred_languages ([str]): Specifies an array of one or more [language codes](/docs/chat/v3/platform-api/guides/miscellaneous#2-language-codes-for-auto-translation) to translate notification messages to preferred languages. Up to 4 languages can be set for the user. If messages are sent in one of the preferred languages, notification messages won't be translated. If messages are sent in a language other than the preferred languages, notification messages will be translated into the first language in the array. In addition, the messages translated into other preferred languages will be provided in the `sendbird` property of a notification message payload.. [optional]  # noqa: E501
            leave_all_when_deactivated (bool): Determines whether the user leaves all joined group channels upon deactivation. Note that this value is true by default. Use in conjunction with the is_active property above.. [optional]  # noqa: E501
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

        self.user_id = user_id
        self.nickname = nickname
        self.profile_url = profile_url
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
