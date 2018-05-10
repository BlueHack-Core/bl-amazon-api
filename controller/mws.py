from lib.mws import mws
import os

from swagger_server.models.get_mws_feeds_submissions_response import GetMwsFeedsSubmissionsResponse
from swagger_server.models.get_mws_feeds_submissions_response_data import GetMwsFeedsSubmissionsResponseData

from swagger_server.models.get_mws_feeds_submissions_result_response import GetMwsFeedsSubmissionsResultResponse
from swagger_server.models.get_mws_feeds_submissions_result_response_data import GetMwsFeedsSubmissionsResultResponseData

from swagger_server.models.get_mws_status_response import GetMwsStatusResponse

from swagger_server.models.post_submit_feed_response import PostSubmitFeedResponse
from swagger_server.models.post_submit_feed_response_data import PostSubmitFeedResponseData
from swagger_server.models.feed_submission_info import FeedSubmissionInfo

AWS_MWS_ACCESS_KEY = os.environ['AWS_MWS_ACCESS_KEY']
AWS_MWS_SECRET_KEY = os.environ['AWS_MWS_SECRET_KEY']
MERCHANT_ID = os.environ['MERCHANT_ID']

class MWS(object):
  def __init__(self):
    super().__init__()

  @staticmethod
  def get_mws_feeds_submissions(feedSubmissionIds=None, feedTypes=None, processingStatuses=None, maxCount=None,
                                nextToken=None):
    res = GetMwsFeedsSubmissionsResponse()
    res_data = GetMwsFeedsSubmissionsResponseData()

    try:
      feeds_api = mws.Feeds(AWS_MWS_ACCESS_KEY, AWS_MWS_SECRET_KEY,
                            MERCHANT_ID)
      feeds_res = feeds_api.get_feed_submission_list(feedids=feedSubmissionIds, feedtypes=feedTypes, processingstatuses=processingStatuses, max_count=maxCount, next_token=nextToken).parsed

      feed_submission_info_list = []
      try:
        feeds_res.value

        feed_info = feeds_res.FeedSubmissionInfo

        api_instance = FeedSubmissionInfo()
        api_instance.feed_submission_id = feed_info.FeedSubmissionId
        api_instance.feed_processing_status = feed_info.FeedProcessingStatus
        api_instance.feed_type = feed_info.FeedType

        feed_submission_info_list.append(api_instance)

      except:
        for feed_info in feeds_res.FeedSubmissionInfo:
          api_instance = FeedSubmissionInfo()
          api_instance.feed_submission_id = feed_info.FeedSubmissionId
          api_instance.feed_processing_status = feed_info.FeedProcessingStatus
          api_instance.feed_type = feed_info.FeedType

          feed_submission_info_list.append(api_instance)

      finally:
        res_data.feed_submission_info = feed_submission_info_list

        res_data.has_next = feeds_res.HasNext
        if feeds_res.HasNext == 'true':
          res_data.next_token = feeds_res.NextToken

      res.data = res_data
      res.message = 'Successful'
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_mws_feeds_submissions_result(feedSubmissionId):
    res = GetMwsFeedsSubmissionsResultResponse()
    res_data = GetMwsFeedsSubmissionsResultResponseData()

    try:
      feeds_api = mws.Feeds(AWS_MWS_ACCESS_KEY, AWS_MWS_SECRET_KEY,
                            MERCHANT_ID)
      feeds_res = feeds_api.get_feed_submission_result(feedid=feedSubmissionId).parsed
      res_data.result = feeds_res.decode('utf-8')

      res.data = res_data
      res.message = 'Successful'
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_mws_status():
    res = GetMwsStatusResponse()

    try:
      feeds_api = mws.Feeds(AWS_MWS_ACCESS_KEY, AWS_MWS_SECRET_KEY,
                            MERCHANT_ID)
      feeds_res = feeds_api.get_service_status().parsed

      res.message = feeds_res.Status
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def post_submit_feed(file):
    res = PostSubmitFeedResponse()

    try:
      res_data = PostSubmitFeedResponseData()

      data = file.read()
      file.close()

      feeds_api = mws.Feeds(AWS_MWS_ACCESS_KEY, AWS_MWS_SECRET_KEY,
                            MERCHANT_ID)
      feeds_res = feeds_api.submit_feed(data, feed_type="_POST_FLAT_FILE_LISTINGS_DATA_",
                                        content_type="text/tab-separated-values;charset=iso-8859-1").parsed

      api_instance = FeedSubmissionInfo()
      api_instance.feed_submission_id = feeds_res.FeedSubmissionInfo.FeedSubmissionId
      api_instance.feed_processing_status = feeds_res.FeedSubmissionInfo.FeedProcessingStatus
      api_instance.feed_type = feeds_res.FeedSubmissionInfo.FeedType

      res_data.feed_submission_info = api_instance

      res.data = res_data
      res.message = 'Successful'
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status
