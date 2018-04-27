# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.simple_image import SimpleImage  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMwsController(BaseTestCase):
    """MwsController integration test stubs"""

    def test_get_products(self):
        """Test case for get_products

        
        """
        query_string = [('offset', 56),
                        ('limit', 56)]
        response = self.client.open(
            '//mws',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
