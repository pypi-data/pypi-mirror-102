# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.6.0-dev
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AnalysisResultResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'metadata': 'AnalysisResultResponseMetadata',
        'result': 'object'
    }

    attribute_map = {
        'metadata': 'metadata',
        'result': 'result'
    }

    def __init__(self, metadata=None, result=None):  # noqa: E501
        """AnalysisResultResponse - a model defined in Swagger"""  # noqa: E501
        self._metadata = None
        self._result = None
        self.discriminator = None
        self.metadata = metadata
        self.result = result

    @property
    def metadata(self):
        """Gets the metadata of this AnalysisResultResponse.  # noqa: E501


        :return: The metadata of this AnalysisResultResponse.  # noqa: E501
        :rtype: AnalysisResultResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AnalysisResultResponse.


        :param metadata: The metadata of this AnalysisResultResponse.  # noqa: E501
        :type: AnalysisResultResponseMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def result(self):
        """Gets the result of this AnalysisResultResponse.  # noqa: E501

        Actual result of an analysis run.  # noqa: E501

        :return: The result of this AnalysisResultResponse.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AnalysisResultResponse.

        Actual result of an analysis run.  # noqa: E501

        :param result: The result of this AnalysisResultResponse.  # noqa: E501
        :type: object
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AnalysisResultResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalysisResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
