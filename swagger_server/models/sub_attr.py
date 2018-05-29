# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SubAttr(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sub_attr_code: str=None, value: str=None, text: str=None):  # noqa: E501
        """SubAttr - a model defined in Swagger

        :param sub_attr_code: The sub_attr_code of this SubAttr.  # noqa: E501
        :type sub_attr_code: str
        :param value: The value of this SubAttr.  # noqa: E501
        :type value: str
        :param text: The text of this SubAttr.  # noqa: E501
        :type text: str
        """
        self.swagger_types = {
            'sub_attr_code': str,
            'value': str,
            'text': str
        }

        self.attribute_map = {
            'sub_attr_code': 'sub_attr_code',
            'value': 'value',
            'text': 'text'
        }

        self._sub_attr_code = sub_attr_code
        self._value = value
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'SubAttr':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubAttr of this SubAttr.  # noqa: E501
        :rtype: SubAttr
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_attr_code(self) -> str:
        """Gets the sub_attr_code of this SubAttr.


        :return: The sub_attr_code of this SubAttr.
        :rtype: str
        """
        return self._sub_attr_code

    @sub_attr_code.setter
    def sub_attr_code(self, sub_attr_code: str):
        """Sets the sub_attr_code of this SubAttr.


        :param sub_attr_code: The sub_attr_code of this SubAttr.
        :type sub_attr_code: str
        """

        self._sub_attr_code = sub_attr_code

    @property
    def value(self) -> str:
        """Gets the value of this SubAttr.


        :return: The value of this SubAttr.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this SubAttr.


        :param value: The value of this SubAttr.
        :type value: str
        """

        self._value = value

    @property
    def text(self) -> str:
        """Gets the text of this SubAttr.


        :return: The text of this SubAttr.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this SubAttr.


        :param text: The text of this SubAttr.
        :type text: str
        """

        self._text = text