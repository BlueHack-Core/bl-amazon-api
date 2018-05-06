from bson.objectid import ObjectId
from bl_product_amaz.us_btgs import US_btgs

from swagger_server.models.get_products_browse_node_attributes_response import GetProductsBrowseNodeAttributesResponse
from swagger_server.models.get_products_browse_node_valid_value_response import GetProductsBrowseNodeValidValueResponse
from swagger_server.models.get_products_browse_node_valid_value_response_data import GetProductsBrowseNodeValidValueResponseData
from swagger_server.models.get_products_status_response import GetProductsStatusResponse

from pprint import pprint

class Products(object):
  def __init__(self):
    super().__init__()

  @staticmethod
  def get_products_browse_node_attributes(nodeId):
    res = GetProductsBrowseNodeAttributesResponse()

    try:
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_products_browse_node_valid_value(nodeId):
    res = GetProductsBrowseNodeValidValueResponse()

    try:
      res_data = GetProductsBrowseNodeValidValueResponseData()

      api_instance = US_btgs()
      api_res = api_instance.get_valid_value_by_node_id(node_id=nodeId)

      if res:
        res_data.valid_value = api_res
        res.message = 'Successful'
        response_status = 200
      else:
        res_data.valid_value = None
        res.message = 'No valid_value'
        response_status = 400

      res.data = res_data

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_products_status():
    res = GetProductsStatusResponse()

    res.message = "Successful"
    response_status = 200

    return res, response_status
