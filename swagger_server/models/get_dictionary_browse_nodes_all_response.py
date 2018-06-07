# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_dictionary_browse_nodes_all_response_data import GetDictionaryBrowseNodesAllResponseData  # noqa: F401,E501
from swagger_server import util


class GetDictionaryBrowseNodesAllResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, message: str=None, data: List[GetDictionaryBrowseNodesAllResponseData]=None):  # noqa: E501
        """GetDictionaryBrowseNodesAllResponse - a model defined in Swagger

        :param message: The message of this GetDictionaryBrowseNodesAllResponse.  # noqa: E501
        :type message: str
        :param data: The data of this GetDictionaryBrowseNodesAllResponse.  # noqa: E501
        :type data: List[GetDictionaryBrowseNodesAllResponseData]
        """
        self.swagger_types = {
            'message': str,
            'data': List[GetDictionaryBrowseNodesAllResponseData]
        }

        self.attribute_map = {
            'message': 'message',
            'data': 'data'
        }

        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'GetDictionaryBrowseNodesAllResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetDictionaryBrowseNodesAllResponse of this GetDictionaryBrowseNodesAllResponse.  # noqa: E501
        :rtype: GetDictionaryBrowseNodesAllResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this GetDictionaryBrowseNodesAllResponse.


        :return: The message of this GetDictionaryBrowseNodesAllResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this GetDictionaryBrowseNodesAllResponse.


        :param message: The message of this GetDictionaryBrowseNodesAllResponse.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> List[GetDictionaryBrowseNodesAllResponseData]:
        """Gets the data of this GetDictionaryBrowseNodesAllResponse.


        :return: The data of this GetDictionaryBrowseNodesAllResponse.
        :rtype: List[GetDictionaryBrowseNodesAllResponseData]
        """
        return self._data

    @data.setter
    def data(self, data: List[GetDictionaryBrowseNodesAllResponseData]):
        """Sets the data of this GetDictionaryBrowseNodesAllResponse.


        :param data: The data of this GetDictionaryBrowseNodesAllResponse.
        :type data: List[GetDictionaryBrowseNodesAllResponseData]
        """

        self._data = data