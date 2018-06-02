from bl_product_amaz.us_btgs import US_btgs
from bl_product_amaz.amz_attrs import AMZ_attrs

from swagger_server.models.get_products_browse_node_attributes_response import GetProductsBrowseNodeAttributesResponse
from swagger_server.models.get_products_browse_node_attributes_response_data import GetProductsBrowseNodeAttributesResponseData
from swagger_server.models.attr import Attr
from swagger_server.models.sub_attr import SubAttr

from swagger_server.models.get_products_browse_node_valid_value_response import GetProductsBrowseNodeValidValueResponse
from swagger_server.models.get_products_browse_node_valid_value_response_data import GetProductsBrowseNodeValidValueResponseData

from swagger_server.models.get_products_status_response import GetProductsStatusResponse

class Products(object):
  def __init__(self):
    super().__init__()

  @staticmethod
  def get_products_browse_node_attributes(nodeId):
    res = GetProductsBrowseNodeAttributesResponse()

    try:
      attr_data_list = []

      us_btgs_api = US_btgs()
      attrs_api = AMZ_attrs()

      us_btgs_res = us_btgs_api.get_attrs_by_node_id(nodeId)
      if us_btgs_res:
        for attr in us_btgs_res:
          for key, value in attr.items():
            res_data = GetProductsBrowseNodeAttributesResponseData()

            attr_instance = Attr()
            attr_instance.attr_code = key
            attr_instance.value = value
            res_data.attr = attr_instance

            if key:
              attrs_res = attrs_api.get_sub_attr_by_attr_code(key)
              sub_attr_list = []
              for sub_attr in attrs_res:
                sub_attr_instance = SubAttr()
                sub_attr_instance.sub_attr_code = sub_attr.get('sub_attr_code')
                sub_attr_instance.value = sub_attr.get('value')
                sub_attr_instance.text = sub_attr.get('text')

                sub_attr_list.append(sub_attr_instance)

              res_data.sub_attrs = sub_attr_list

            attr_data_list.append(res_data)

        response_status = 200

        res_data = attr_data_list
        res.data = res_data
      else:
        res.message = 'No attributes for node_id: ' + nodeId
        response_status = 400

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
        res.message = 'No valid_value for node_id: ' + nodeId
        response_status = 400

      res.data = res_data

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_products_status():
    res = GetProductsStatusResponse()

    res.message = "Stable"
    response_status = 200

    return res, response_status
