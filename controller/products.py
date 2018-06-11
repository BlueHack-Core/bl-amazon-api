from bl_product_amaz.us_btgs import US_btgs
from bl_product_amaz.amz_attrs import AMZ_attrs
from bl_product_amaz.amz_sub_attrs import AMZ_sub_attrs
from bl_product_amaz.amz_title_dic import AMZ_title_dic

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
      sub_attrs_api = AMZ_sub_attrs()

      us_btgs_res = us_btgs_api.get_attrs_by_node_id(nodeId)
      if us_btgs_res:
        for anAttr in us_btgs_res:
          for key in anAttr.keys():
            attrs_res = attrs_api.get_attr_by_attr_id(key)
            if attrs_res:
              res_data = GetProductsBrowseNodeAttributesResponseData()

              attr_instance = Attr()
              attr_instance.attr_id = attrs_res.get('attr_id')
              attr_instance.attr_us_name = attrs_res.get('attr_us_name')
              attr_instance.attr_kr_name = attrs_res.get('attr_kr_name')
              sub_attr_ids = attrs_res.get('sub_attr_ids')

              if sub_attr_ids:
                sub_attr_list = []
                for sub_attr_id in sub_attr_ids:
                  sub_attrs_res = sub_attrs_api.get_sub_attr_by_sub_attr_id(sub_attr_id)
                  if sub_attrs_res:
                    sub_attr_instance = SubAttr()
                    sub_attr_instance.sub_attr_id = sub_attrs_res.get('sub_attr_id')
                    sub_attr_instance.sub_attr_us_name = sub_attrs_res.get('sub_attr_us_name')
                    sub_attr_instance.sub_attr_kr_name = sub_attrs_res.get('sub_attr_kr_name')

                    sub_attr_list.append(sub_attr_instance)

              res_data.attr = attr_instance
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
