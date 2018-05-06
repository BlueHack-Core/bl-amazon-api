# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_mws_feeds_submissions_response import GetMwsFeedsSubmissionsResponse  # noqa: E501
from swagger_server.models.get_mws_feeds_submissions_result_response import GetMwsFeedsSubmissionsResultResponse  # noqa: E501
from swagger_server.models.get_mws_status_response import GetMwsStatusResponse  # noqa: E501
from swagger_server.models.post_submit_feed_response import PostSubmitFeedResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMwsController(BaseTestCase):
    """MwsController integration test stubs"""

    def test_get_mws_feeds_submissions(self):
        """Test case for get_mws_feeds_submissions

        Get a list of feed submissions submitted
        """
        query_string = [('feedSubmissionIds', 'feedSubmissionIds_example'),
                        ('feedTypes', 'feedTypes_example'),
                        ('processingStatuses', 'processingStatuses_example'),
                        ('maxCount', 56),
                        ('nextToken', 'nextToken_example')]
        response = self.client.open(
            '//mws/feeds/submissions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mws_feeds_submissions_result(self):
        """Test case for get_mws_feeds_submissions_result

        Get the feed processing report
        """
        response = self.client.open(
            '//mws/feeds/submissions/{feedSubmissionId}/result'.format(feedSubmissionId='feedSubmissionId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mws_status(self):
        """Test case for get_mws_status

        Get Amazon MWS API status
        """
        response = self.client.open(
            '//mws/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_submit_feed(self):
        """Test case for post_submit_feed

        Post feed with a flat file
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '//mws/feeds/submit',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
