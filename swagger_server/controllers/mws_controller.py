import connexion
import six

from swagger_server.models.get_mws_status_response import GetMwsStatusResponse  # noqa: E501
from swagger_server import util

from controller.mws import MWS

def get_mws_feeds_submissions(feedSubmissionIds=None, feedTypes=None, processingStatuses=None, maxCount=None, nextToken=None):  # noqa: E501
    """Get a list of feed submissions submitted

    Returns a list of all feed submissions submitted in the previous 90 days # noqa: E501

    :param feedSubmissionIds:
    :type feedSubmissionIds: List[str]
    :param feedTypes:
    :type feedTypes: List[str]
    :param processingStatuses:
    :type processingStatuses: List[str]
    :param maxCount:
    :type maxCount: int
    :param nextToken:
    :type nextToken: str

    :rtype: GetMwsFeedsSubmissionsResponse
    """
    return MWS.get_mws_feeds_submissions(feedSubmissionIds=feedSubmissionIds, feedTypes=feedTypes, processingStatuses=processingStatuses, maxCount=maxCount, nextToken=nextToken)


def get_mws_feeds_submissions_result(feedSubmissionId):  # noqa: E501
    """Get the feed processing report

    Returns the feed processing report and the Content-MD5 header # noqa: E501

    :param feedSubmissionId:
    :type feedSubmissionId: str

    :rtype: GetMwsFeedsSubmissionsResultResponse
    """
    return MWS.get_mws_feeds_submissions_result(feedSubmissionId=feedSubmissionId)

def get_mws_status():  # noqa: E501
    """

    Return Amazon MWS API status # noqa: E501


    :rtype: GetMwsStatusResponse
    """
    return MWS.get_mws_status()

def post_submit_feed(file):  # noqa: E501
    """Post a flat file feed

    Uploads a feed for processing by Amazon MWS # noqa: E501

    :param file: file: xxx.txt / content_type: text/tab-separated-values
    :type file: werkzeug.datastructures.FileStorage

    :rtype: PostSubmitFeedResponse
    """
    return MWS.post_submit_feed(file=file)
