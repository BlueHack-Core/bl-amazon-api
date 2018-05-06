# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_products_browse_node_attributes_response import GetProductsBrowseNodeAttributesResponse  # noqa: E501
from swagger_server.models.get_products_browse_node_valid_value_response import GetProductsBrowseNodeValidValueResponse  # noqa: E501
from swagger_server.models.get_products_status_response import GetProductsStatusResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductController(BaseTestCase):
    """ProductController integration test stubs"""

    def test_get_products_browse_node_attributes(self):
        """Test case for get_products_browse_node_attributes

        Get attributes within a specified browse node for the title generating
        """
        response = self.client.open(
            '//products/browseNodes/{nodeId}/attributes'.format(nodeId='nodeId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_products_browse_node_valid_value(self):
        """Test case for get_products_browse_node_valid_value

        Get the browse node's valid value for submiting a flat file
        """
        response = self.client.open(
            '//products/browseNodes/{nodeId}/validValue'.format(nodeId='nodeId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_products_status(self):
        """Test case for get_products_status

        Get Product API status
        """
        response = self.client.open(
            '//products/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
