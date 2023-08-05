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


class ContainerImagesResponse(object):
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
        'container_images': 'list[ContainerImagesResponseContainerImages]',
        'parameters': 'ContainerImagesResponseParameters'
    }

    attribute_map = {
        'container_images': 'container_images',
        'parameters': 'parameters'
    }

    def __init__(self, container_images=None, parameters=None):  # noqa: E501
        """ContainerImagesResponse - a model defined in Swagger"""  # noqa: E501
        self._container_images = None
        self._parameters = None
        self.discriminator = None
        self.container_images = container_images
        self.parameters = parameters

    @property
    def container_images(self):
        """Gets the container_images of this ContainerImagesResponse.  # noqa: E501


        :return: The container_images of this ContainerImagesResponse.  # noqa: E501
        :rtype: list[ContainerImagesResponseContainerImages]
        """
        return self._container_images

    @container_images.setter
    def container_images(self, container_images):
        """Sets the container_images of this ContainerImagesResponse.


        :param container_images: The container_images of this ContainerImagesResponse.  # noqa: E501
        :type: list[ContainerImagesResponseContainerImages]
        """
        if container_images is None:
            raise ValueError("Invalid value for `container_images`, must not be `None`")  # noqa: E501

        self._container_images = container_images

    @property
    def parameters(self):
        """Gets the parameters of this ContainerImagesResponse.  # noqa: E501


        :return: The parameters of this ContainerImagesResponse.  # noqa: E501
        :rtype: ContainerImagesResponseParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ContainerImagesResponse.


        :param parameters: The parameters of this ContainerImagesResponse.  # noqa: E501
        :type: ContainerImagesResponseParameters
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if issubclass(ContainerImagesResponse, dict):
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
        if not isinstance(other, ContainerImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
