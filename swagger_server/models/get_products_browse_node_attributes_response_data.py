# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.attr import Attr  # noqa: F401,E501
from swagger_server.models.sub_attr import SubAttr  # noqa: F401,E501
from swagger_server import util


class GetProductsBrowseNodeAttributesResponseData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, attr: Attr=None, sub_attrs: List[SubAttr]=None):  # noqa: E501
        """GetProductsBrowseNodeAttributesResponseData - a model defined in Swagger

        :param attr: The attr of this GetProductsBrowseNodeAttributesResponseData.  # noqa: E501
        :type attr: Attr
        :param sub_attrs: The sub_attrs of this GetProductsBrowseNodeAttributesResponseData.  # noqa: E501
        :type sub_attrs: List[SubAttr]
        """
        self.swagger_types = {
            'attr': Attr,
            'sub_attrs': List[SubAttr]
        }

        self.attribute_map = {
            'attr': 'attr',
            'sub_attrs': 'sub_attrs'
        }

        self._attr = attr
        self._sub_attrs = sub_attrs

    @classmethod
    def from_dict(cls, dikt) -> 'GetProductsBrowseNodeAttributesResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetProductsBrowseNodeAttributesResponse_data of this GetProductsBrowseNodeAttributesResponseData.  # noqa: E501
        :rtype: GetProductsBrowseNodeAttributesResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attr(self) -> Attr:
        """Gets the attr of this GetProductsBrowseNodeAttributesResponseData.


        :return: The attr of this GetProductsBrowseNodeAttributesResponseData.
        :rtype: Attr
        """
        return self._attr

    @attr.setter
    def attr(self, attr: Attr):
        """Sets the attr of this GetProductsBrowseNodeAttributesResponseData.


        :param attr: The attr of this GetProductsBrowseNodeAttributesResponseData.
        :type attr: Attr
        """

        self._attr = attr

    @property
    def sub_attrs(self) -> List[SubAttr]:
        """Gets the sub_attrs of this GetProductsBrowseNodeAttributesResponseData.


        :return: The sub_attrs of this GetProductsBrowseNodeAttributesResponseData.
        :rtype: List[SubAttr]
        """
        return self._sub_attrs

    @sub_attrs.setter
    def sub_attrs(self, sub_attrs: List[SubAttr]):
        """Sets the sub_attrs of this GetProductsBrowseNodeAttributesResponseData.


        :param sub_attrs: The sub_attrs of this GetProductsBrowseNodeAttributesResponseData.
        :type sub_attrs: List[SubAttr]
        """

        self._sub_attrs = sub_attrs
