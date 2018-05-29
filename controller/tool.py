from swagger_server.models.get_tool_titles_response import GetToolTitlesResponse
from swagger_server.models.get_tool_titles_response_data import GetToolTitlesResponseData

from bl_db_product_amz_best.products import Products

class Tool(object):
  def __init__(self):
    super().__init__()

  @staticmethod
  def get_tool_titles(nodeId):
    api_instance = Products()
    res = GetToolTitlesResponse()

    try:
      res_data = GetToolTitlesResponseData()

      offset = 0
      limit = 100

      products_res = api_instance.get_products_by_node_id(node_id=nodeId, offset=offset, limit=limit)
      if products_res:
        if len(products_res) > 0:
          title_list = []
          for product in products_res:
            title_list.append(product.get('Title'))
          res_data.titles = title_list
        res.data = res_data
        res.message = 'Successful'
        response_status = 200
      else:
        res.message = 'No products'
        response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_dictionary_words(nodeId):
    return

  @staticmethod
  def get_dictionary_words_filtered(nodeId, filters):
    return

  @staticmethod
  def post_dictionary_products_attrs_sub_attrs(nodeId, attrId, subAttrId, subAttrUsName, subAttrKrName, attrUsName=None, attrKrName=None):
    return

  @staticmethod
  def post_dictionary_words(subAttrId, word):
    return
