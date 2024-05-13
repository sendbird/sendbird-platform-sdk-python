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



class V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest(ModelNormal):
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
            'message_type': (str,),  # noqa: E501
            'user_id': (str,),  # noqa: E501
            'message': (str,),  # noqa: E501
            'file': (str,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'scheduled_at': (float,),  # noqa: E501
            'custom_type': (str,),  # noqa: E501
            'data': (str,),  # noqa: E501
            'send_push': (bool,),  # noqa: E501
            'mention_type': (str,),  # noqa: E501
            'mentioned_user_ids': ([str],),  # noqa: E501
            'is_silent': (bool,),  # noqa: E501
            'mark_as_read': (bool,),  # noqa: E501
            'sorted_metaarray': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),  # noqa: E501
            'dedup_id': (str,),  # noqa: E501
            'apns_bundle_id': (str,),  # noqa: E501
            'apple_critical_alert_options': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'sound': (str,),  # noqa: E501
            'volume': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'message_type': 'message_type',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
        'message': 'message',  # noqa: E501
        'file': 'file',  # noqa: E501
        'url': 'url',  # noqa: E501
        'scheduled_at': 'scheduled_at',  # noqa: E501
        'custom_type': 'custom_type',  # noqa: E501
        'data': 'data',  # noqa: E501
        'send_push': 'send_push',  # noqa: E501
        'mention_type': 'mention_type',  # noqa: E501
        'mentioned_user_ids': 'mentioned_user_ids[]',  # noqa: E501
        'is_silent': 'is_silent',  # noqa: E501
        'mark_as_read': 'mark_as_read',  # noqa: E501
        'sorted_metaarray': 'sorted_metaarray',  # noqa: E501
        'dedup_id': 'dedup_id',  # noqa: E501
        'apns_bundle_id': 'apns_bundle_id',  # noqa: E501
        'apple_critical_alert_options': 'apple_critical_alert_options',  # noqa: E501
        'sound': 'sound',  # noqa: E501
        'volume': 'volume',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest - a model defined in OpenAPI

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
            message_type (str): Specifies the type of the message. The value of MESG represents a text message.. [optional]  # noqa: E501
            user_id (str): Specifies the user ID of the sender.. [optional]  # noqa: E501
            message (str): Specifies the content of the message.. [optional]  # noqa: E501
            file (str): Depending on the file upload method, this specifies the data of the file to upload to the Sendbird server either in raw binary format or by the file's location. When sending a request containing a file, you must change the value of the content-type header to multipart/form-data; boundary={your_unique_boundary_string} in the request. The code examples of HTTP multipart request and cURL are provided below the tables for your reference. If this file property is specified, the url property is not required. This doesn't allow a converted base64-encoded string from a file as its value.. [optional]  # noqa: E501
            url (str): Specifies the URL of the file hosted on the server of your own or other third-party companies. If this url property is specified, the file property is not required.. [optional]  # noqa: E501
            scheduled_at (float): The specified time that indicates when to send the message, in Unix milliseconds format. Since messages are scheduled in minutes, values less than seconds are discarded. The specified time can be between 5 minutes and 43,200 minutes (30 days) from the current time.. [optional]  # noqa: E501
            custom_type (str): Specifies a custom message type used for message grouping. The length is limited to 128 characters. * Custom types are also used to segment metrics within Sendbird's Advanced analytics, which enables the sub-classification of data views.. [optional]  # noqa: E501
            data (str): Specifies additional message information such as custom font size, font type, or JSON formatted string.. [optional]  # noqa: E501
            send_push (bool): Determines whether to send a push notification of the message to the channel members. This property only applies to group channels. (Default is true). [optional]  # noqa: E501
            mention_type (str): Specifies the mentioning method that indicates which user receives a notification of the message. Acceptable values are users and channels. If set to users, only the users specified in the mentioned_user_ids property below are notified. If set to channels, all users in the channel are notified. (Default = users). [optional]  # noqa: E501
            mentioned_user_ids ([str]): Specifies an array of one or more IDs of the users who will receive a notification of the message.. [optional]  # noqa: E501
            is_silent (bool): Determines whether to send a message without updating some of the following channel properties. If set to true, the channel's last_message is updated only for the sender while its unread_message_count remains unchanged for all channel members. Also, a push notification isn't sent to the users receiving the message. If the message is sent to a hidden channel, the channel remains hidden. (Default is false). [optional]  # noqa: E501
            mark_as_read (bool): Determines whether to mark the message as read for the sender. If set to false, then the sender's unread_count and read_receipt remain unchanged after the message is sent. (Default is true). [optional]  # noqa: E501
            sorted_metaarray ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Specifies an array of one or more JSON objects consisting of key-values items that store additional message information. Items are saved and returned in the exact order they've been specified.. [optional]  # noqa: E501
            dedup_id (str): Specifies a unique ID for the message created by another system. In general, this property is used to prevent the same message data from getting inserted when migrating messages from another system to the Sendbird server. If specified, the server performs a duplicate check using the property value.. [optional]  # noqa: E501
            apns_bundle_id (str): Specifies the bundle ID of the client app in order to send a push notification to iOS devices. You can find this in Settings > Chat > Notifications > Push notification services on Sendbird Dashboard.. [optional]  # noqa: E501
            apple_critical_alert_options ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies options that support Apple's critical alerts and checks whether the message is a critical alert.. [optional]  # noqa: E501
            sound (str): Specifies the name of a sound file that is used for critical alerts.. [optional]  # noqa: E501
            volume (float): Specifies the volume of the critical alert sound. The volume ranges from 0.0to 1.0, which indicates silent and full volume, respectively. (Default = 1.0). [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """V3GroupChannelsChannelUrlScheduledMessagesScheduledMessageIdDeleteRequest - a model defined in OpenAPI

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
            message_type (str): Specifies the type of the message. The value of MESG represents a text message.. [optional]  # noqa: E501
            user_id (str): Specifies the user ID of the sender.. [optional]  # noqa: E501
            message (str): Specifies the content of the message.. [optional]  # noqa: E501
            file (str): Depending on the file upload method, this specifies the data of the file to upload to the Sendbird server either in raw binary format or by the file's location. When sending a request containing a file, you must change the value of the content-type header to multipart/form-data; boundary={your_unique_boundary_string} in the request. The code examples of HTTP multipart request and cURL are provided below the tables for your reference. If this file property is specified, the url property is not required. This doesn't allow a converted base64-encoded string from a file as its value.. [optional]  # noqa: E501
            url (str): Specifies the URL of the file hosted on the server of your own or other third-party companies. If this url property is specified, the file property is not required.. [optional]  # noqa: E501
            scheduled_at (float): The specified time that indicates when to send the message, in Unix milliseconds format. Since messages are scheduled in minutes, values less than seconds are discarded. The specified time can be between 5 minutes and 43,200 minutes (30 days) from the current time.. [optional]  # noqa: E501
            custom_type (str): Specifies a custom message type used for message grouping. The length is limited to 128 characters. * Custom types are also used to segment metrics within Sendbird's Advanced analytics, which enables the sub-classification of data views.. [optional]  # noqa: E501
            data (str): Specifies additional message information such as custom font size, font type, or JSON formatted string.. [optional]  # noqa: E501
            send_push (bool): Determines whether to send a push notification of the message to the channel members. This property only applies to group channels. (Default is true). [optional]  # noqa: E501
            mention_type (str): Specifies the mentioning method that indicates which user receives a notification of the message. Acceptable values are users and channels. If set to users, only the users specified in the mentioned_user_ids property below are notified. If set to channels, all users in the channel are notified. (Default = users). [optional]  # noqa: E501
            mentioned_user_ids ([str]): Specifies an array of one or more IDs of the users who will receive a notification of the message.. [optional]  # noqa: E501
            is_silent (bool): Determines whether to send a message without updating some of the following channel properties. If set to true, the channel's last_message is updated only for the sender while its unread_message_count remains unchanged for all channel members. Also, a push notification isn't sent to the users receiving the message. If the message is sent to a hidden channel, the channel remains hidden. (Default is false). [optional]  # noqa: E501
            mark_as_read (bool): Determines whether to mark the message as read for the sender. If set to false, then the sender's unread_count and read_receipt remain unchanged after the message is sent. (Default is true). [optional]  # noqa: E501
            sorted_metaarray ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Specifies an array of one or more JSON objects consisting of key-values items that store additional message information. Items are saved and returned in the exact order they've been specified.. [optional]  # noqa: E501
            dedup_id (str): Specifies a unique ID for the message created by another system. In general, this property is used to prevent the same message data from getting inserted when migrating messages from another system to the Sendbird server. If specified, the server performs a duplicate check using the property value.. [optional]  # noqa: E501
            apns_bundle_id (str): Specifies the bundle ID of the client app in order to send a push notification to iOS devices. You can find this in Settings > Chat > Notifications > Push notification services on Sendbird Dashboard.. [optional]  # noqa: E501
            apple_critical_alert_options ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies options that support Apple's critical alerts and checks whether the message is a critical alert.. [optional]  # noqa: E501
            sound (str): Specifies the name of a sound file that is used for critical alerts.. [optional]  # noqa: E501
            volume (float): Specifies the volume of the critical alert sound. The volume ranges from 0.0to 1.0, which indicates silent and full volume, respectively. (Default = 1.0). [optional]  # noqa: E501
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