from swagger_server.models.get_tool_titles_response import GetToolTitlesResponse
from swagger_server.models.get_tool_titles_response_data import GetToolTitlesResponseData

from swagger_server.models.get_dictionary_words_response import GetDictionaryWordsResponse
from swagger_server.models.get_dictionary_words_response_data import GetDictionaryWordsResponseData

from swagger_server.models.get_dictionary_words_filtered_response import GetDictionaryWordsFilteredResponse
from swagger_server.models.get_dictionary_words_filtered_response_data import GetDictionaryWordsFilteredResponseData
from swagger_server.models.get_dictionary_words_filtered_response_data_words import GetDictionaryWordsFilteredResponseDataWords

from swagger_server.models.post_dictionary_words_response import PostDictionaryWordsResponse

from swagger_server.models.post_dictionary_products_attrs_response import PostDictionaryProductsAttrsResponse

from swagger_server.models.post_dictionary_products_attrs_sub_attrs_response import PostDictionaryProductsAttrsSubAttrsResponse

from bl_db_product_amz_best.products import Products
from bl_title_amaz.title_filter import Title_filter

from collections import Counter

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
  def get_dictionary_words(nodeIds):
    api_instance = Title_filter()
    res = GetDictionaryWordsResponse()

    try:
      res_data = GetDictionaryWordsResponseData()

      word_res = api_instance.get_title_word_dic_by_node_id(node_ids=nodeIds)
      if word_res:
        if len(word_res) > 0:
          word_list = []
          for word in word_res:
            word_list.append(word)
          res_data.words = word_list
          res.data = res_data
          res.message = 'Successful'
          response_status = 200
        else:
          res.message = 'No words'
          response_status = 400
      else:
        res.message = 'No words'
        response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_dictionary_words_filtered(nodeId, filters):
    api_instance = Title_filter()
    res = GetDictionaryWordsFilteredResponse()

    try:
      res_data = GetDictionaryWordsFilteredResponseData()

      filtered_titles, result_word = api_instance.filtering_titles(node_ids=[nodeId], filter_list=filters)
      if result_word:
        if len(result_word) > 0:
          word_list = []
          for k, v in result_word.most_common():
            word = GetDictionaryWordsFilteredResponseDataWords()
            word.text = k
            word.count = v
            word_list.append(word)
          res_data.words = word_list
          res.data = res_data
          res.message = 'Successful'
          response_status = 200
        else:
          res.message = 'No words'
          response_status = 400
      else:
        res.message = 'No words'
        response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def post_dictionary_products_attrs(nodeId, attrId, attrUsName, attrKrName):
    api_instance = Title_filter()
    res = PostDictionaryProductsAttrsResponse()

    try:
      attrs_res = api_instance.add_sub_attr_in_amz_sub_attrs(node_id=nodeId,
                                                             attr_id=attrId, attr_kr_name=attrKrName, attr_us_name=attrUsName,
                                                             sub_attr_id=None,
                                                             sub_attr_kr_name=None,
                                                             sub_attr_us_name=None)

      if attrs_res:
        res.message = 'Successful'
        response_status = 200
      else:
        res.message = 'Add attr Failed'
        response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def post_dictionary_products_attrs_sub_attrs(nodeId, attrId, subAttrId, subAttrUsName, subAttrKrName):
    return

  @staticmethod
  def post_dictionary_words(subAttrId, word):
    api_instance = Title_filter()
    res = PostDictionaryWordsResponse()

    try:
      word_res = api_instance.add_sub_attr_word_in_amz_title_dic(sub_attr_id=subAttrId, sub_attr_word=word)

      if word_res:
        res.message = 'Successful'
        response_status = 200
      else:
        res.message = 'Add words Failed'
        response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status
