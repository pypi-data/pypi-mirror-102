# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from bimdata_api_client.configuration import Configuration


class IfcAccessToken(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'token': 'str',
        'read_only': 'bool',
        'expires_at': 'datetime'
    }

    attribute_map = {
        'token': 'token',
        'read_only': 'read_only',
        'expires_at': 'expires_at'
    }

    def __init__(self, token=None, read_only=None, expires_at=None, local_vars_configuration=None):  # noqa: E501
        """IfcAccessToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._read_only = None
        self._expires_at = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if read_only is not None:
            self.read_only = read_only
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def token(self):
        """Gets the token of this IfcAccessToken.  # noqa: E501


        :return: The token of this IfcAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this IfcAccessToken.


        :param token: The token of this IfcAccessToken.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                token is not None and len(token) < 1):
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `1`")  # noqa: E501

        self._token = token

    @property
    def read_only(self):
        """Gets the read_only of this IfcAccessToken.  # noqa: E501


        :return: The read_only of this IfcAccessToken.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this IfcAccessToken.


        :param read_only: The read_only of this IfcAccessToken.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def expires_at(self):
        """Gets the expires_at of this IfcAccessToken.  # noqa: E501


        :return: The expires_at of this IfcAccessToken.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this IfcAccessToken.


        :param expires_at: The expires_at of this IfcAccessToken.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IfcAccessToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IfcAccessToken):
            return True

        return self.to_dict() != other.to_dict()
