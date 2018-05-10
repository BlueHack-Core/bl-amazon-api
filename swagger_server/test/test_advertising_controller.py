# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_advertising_browse_nodes_response import GetAdvertisingBrowseNodesResponse  # noqa: E501
from swagger_server.models.get_advertising_browse_nodes_top_sellers_response import GetAdvertisingBrowseNodesTopSellersResponse  # noqa: E501
from swagger_server.models.get_advertising_status_response import GetAdvertisingStatusResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdvertisingController(BaseTestCase):
    """AdvertisingController integration test stubs"""

    def test_get_advertising_browse_node(self):
        """Test case for get_advertising_browse_node

        Get browse node hierarchy from Amazon
        """
        response = self.client.open(
            '//advertising/browseNodes/{nodeId}'.format(nodeId='nodeId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_advertising_browse_node_top_sellers(self):
        """Test case for get_advertising_browse_node_top_sellers

        Get 10 top sellers within a specified browse node from Amazon
        """
        response = self.client.open(
            '//advertising/browseNodes/{nodeId}/topSellers'.format(nodeId='nodeId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_advertising_status(self):
        """Test case for get_advertising_status

        Get Amazon Product Advertising API status
        """
        response = self.client.open(
            '//advertising/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
