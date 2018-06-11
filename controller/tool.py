from bl_product_amaz.us_btgs import US_btgs
from bl_product_amaz.amz_attrs import AMZ_attrs
from bl_product_amaz.amz_sub_attrs import AMZ_sub_attrs
from bl_product_amaz.amz_title_dic import AMZ_title_dic

from bl_db_product_amz_best.products import Products
from bl_title_amaz.title_filter import Title_filter


from swagger_server.models.get_tool_titles_response import GetToolTitlesResponse
from swagger_server.models.get_tool_titles_response_data import GetToolTitlesResponseData

from swagger_server.models.get_dictionary_products_attrs_response import GetDictionaryProductsAttrsResponse
from swagger_server.models.get_dictionary_products_attrs_sub_attrs_response import GetDictionaryProductsAttrsSubAttrsResponse
from swagger_server.models.get_dictionary_products_attrs_sub_attrs_words_response import GetDictionaryProductsAttrsSubAttrsWordsResponse

from swagger_server.models.get_dictionary_words_response import GetDictionaryWordsResponse
from swagger_server.models.get_dictionary_words_response_data import GetDictionaryWordsResponseData

from swagger_server.models.get_dictionary_browse_nodes_all_response import GetDictionaryBrowseNodesAllResponse
from swagger_server.models.get_dictionary_browse_nodes_all_response_data import GetDictionaryBrowseNodesAllResponseData
from swagger_server.models.get_dictionary_browse_nodes_all_response_sub_attrs import GetDictionaryBrowseNodesAllResponseSubAttrs

from swagger_server.models.get_dictionary_sub_attrs_words_response import GetDictionarySubAttrsWordsResponse

from swagger_server.models.get_dictionary_words_filtered_response import GetDictionaryWordsFilteredResponse
from swagger_server.models.get_dictionary_words_filtered_response_data import GetDictionaryWordsFilteredResponseData
from swagger_server.models.get_dictionary_words_filtered_response_data_words import GetDictionaryWordsFilteredResponseDataWords

from swagger_server.models.post_dictionary_words_response import PostDictionaryWordsResponse

from swagger_server.models.post_dictionary_products_attrs_response import PostDictionaryProductsAttrsResponse

from swagger_server.models.post_dictionary_products_attrs_sub_attrs_response import PostDictionaryProductsAttrsSubAttrsResponse

from swagger_server.models.post_dictionary_products_attrs_sub_attrs_words_response import PostDictionaryProductsAttrsSubAttrsWordsResponse

from swagger_server.models.post_dictionary_sub_attrs_words_count_reset_response import PostDictionarySubAttrsWordsCountResetResponse


from swagger_server.models.attr import Attr
from swagger_server.models.sub_attr import SubAttr
from swagger_server.models.title_dic import TitleDic



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
  def get_dictionary_products_attrs(nodeId, attrId):
    res = GetDictionaryProductsAttrsResponse()

    print(attrId)

    try:
      attrs_api = AMZ_attrs()
      attrs_api_res = attrs_api.get_attr_by_attr_id(attr_id=attrId)

      if attrs_api_res:
        attr_instance = Attr()
        attr_instance.attr_id = attrs_api_res.get('attr_id')
        attr_instance.attr_us_name = attrs_api_res.get('attr_us_name')
        attr_instance.attr_kr_name = attrs_api_res.get('attr_kr_name')

        res.data = attr_instance
      else:
        res.data = None

      res.message = 'Successful'
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_dictionary_products_attrs_sub_attrs(nodeId, attrId, subAttrId):
    res = GetDictionaryProductsAttrsSubAttrsResponse()

    try:
      sub_attrs_api = AMZ_sub_attrs()
      sub_attrs_api_res = sub_attrs_api.get_sub_attr_by_sub_attr_id(sub_attr_id=subAttrId)

      if sub_attrs_api_res:
        sub_attr_instance = SubAttr()
        sub_attr_instance.sub_attr_id = sub_attrs_api_res.get('sub_attr_id')
        sub_attr_instance.sub_attr_us_name = sub_attrs_api_res.get('sub_attr_us_name')
        sub_attr_instance.sub_attr_kr_name = sub_attrs_api_res.get('sub_attr_kr_name')

        res.data = sub_attr_instance
      else:
        res.data = None

      res.message = 'Successful'
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_dictionary_products_attrs_sub_attrs_words(nodeId, attrId, subAttrId, word):
    res = GetDictionaryProductsAttrsSubAttrsWordsResponse()

    try:
      title_dic_api = AMZ_title_dic()
      title_dic_api_res = title_dic_api.get_dic_by_sub_attr_id(sub_attr_id=subAttrId, offset=0, limit=1000)

      if title_dic_api_res:
        title_dic_instance = TitleDic()
        is_exist = False
        for a_titls_dic in title_dic_api_res:
          if a_titls_dic.get('sub_attr_dic_word') == word:
            title_dic_instance.sub_attr_id = a_titls_dic.get('sub_attr_id')
            title_dic_instance.dic_word = a_titls_dic.get('sub_attr_dic_word')
            title_dic_instance.count = a_titls_dic.get('count')

            is_exist = True
        if is_exist:
          res.data = title_dic_instance
          res.message = 'Word already enrolled'
        else:
          res.message = 'Available'

      else:
        res.message = 'SubAttrId not exists'

      response_status = 200

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
  def get_dictionary_browse_nodes_all(nodeId):
    res = GetDictionaryBrowseNodesAllResponse()

    try:
      attr_data_list = []

      us_btgs_api = US_btgs()
      attrs_api = AMZ_attrs()
      sub_attrs_api = AMZ_sub_attrs()
      title_dic_api = AMZ_title_dic()

      us_btgs_res = us_btgs_api.get_attrs_by_node_id(nodeId)
      if us_btgs_res:
        for anAttr in us_btgs_res:
          for key in anAttr.keys():
            attrs_res = attrs_api.get_attr_by_attr_id(key)
            if attrs_res:
              res_data = GetDictionaryBrowseNodesAllResponseData()

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
                    sub_attr = GetDictionaryBrowseNodesAllResponseSubAttrs()

                    sub_attr_instance = SubAttr()
                    sub_attr_instance.sub_attr_id = sub_attrs_res.get('sub_attr_id')
                    sub_attr_instance.sub_attr_us_name = sub_attrs_res.get('sub_attr_us_name')
                    sub_attr_instance.sub_attr_kr_name = sub_attrs_res.get('sub_attr_kr_name')

                    sub_attr.sub_attr = sub_attr_instance

                    title_dic_res = title_dic_api.get_dic_by_sub_attr_id(sub_attr_instance.sub_attr_id, offset=0, limit=1000)
                    if title_dic_res:
                      sub_attr.title_dics = []
                      for a_title_dic in title_dic_res:
                        title_dic_instance = TitleDic()
                        title_dic_instance.sub_attr_id = a_title_dic.get('sub_attr_id')
                        title_dic_instance.dic_word = a_title_dic.get('sub_attr_dic_word')
                        title_dic_instance.count = a_title_dic.get('count')

                        sub_attr.title_dics.append(title_dic_instance)

                    sub_attr_list.append(sub_attr)

              res_data.attr = attr_instance
              res_data.sub_attrs = sub_attr_list

          attr_data_list.append(res_data)

        res.message = 'Successful'
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
  def get_dictionary_sub_attrs_words(subAttrIds):
    res = GetDictionarySubAttrsWordsResponse()

    try:
      title_dic_api = AMZ_title_dic()

      sub_attr_list = []
      for subAttrId in subAttrIds:
        title_dic_res = title_dic_api.get_dic_by_sub_attr_id(subAttrId, offset=0, limit=1000)
        if title_dic_res:
          for a_title_dic in title_dic_res:
            title_dic_instance = TitleDic()
            title_dic_instance.sub_attr_id = a_title_dic.get('sub_attr_id')
            title_dic_instance.dic_word = a_title_dic.get('sub_attr_dic_word')
            title_dic_instance.count = a_title_dic.get('count')

            sub_attr_list.append(title_dic_instance)

      res.data = sub_attr_list
      res.message = 'Successful'
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_dictionary_words_filtered(nodeId, filters):
    res = GetDictionaryWordsFilteredResponse()

    try:
      api_instance = Title_filter()
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
    res = PostDictionaryProductsAttrsResponse()

    try:
      api_instance = Title_filter()
      attrs_res = api_instance.add_sub_attr_in_amz_sub_attrs(node_id=nodeId,
                                                             attr_id=attrId, attr_kr_name=attrKrName, attr_us_name=attrUsName,
                                                             sub_attr_id=None,
                                                             sub_attr_kr_name=None,
                                                             sub_attr_us_name=None)
      # print(attrs_res)
      res.message = 'Successful'
      response_status = 200

      # if attrs_res:
      #   res.message = 'Successful'
      #   response_status = 200
      # else:
      #   res.message = 'Add attr Failed'
      #   response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def post_dictionary_products_attrs_sub_attrs(nodeId, attrId, subAttrId, subAttrUsName, subAttrKrName):
    res = PostDictionaryProductsAttrsSubAttrsResponse()

    try:
      api_instance = Title_filter()
      sub_attrs_res = api_instance.add_sub_attr_in_amz_sub_attrs(node_id=nodeId,
                                                                 attr_id=attrId,
                                                                 sub_attr_id=subAttrId, sub_attr_kr_name=subAttrKrName, sub_attr_us_name=subAttrUsName,
                                                                 attr_kr_name=None,
                                                                 attr_us_name=None)

      # print(sub_attrs_res)
      res.message = 'Successful'
      response_status = 200

      # if sub_attrs_res:
      #   res.message = 'Successful'
      #   response_status = 200
      # else:
      #   res.message = 'Add sub attr Failed'
      #   response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def post_dictionary_products_attrs_sub_attrs_words(nodeId, attrId, subAttrId, word):
    res = PostDictionaryProductsAttrsSubAttrsWordsResponse()

    try:
      api_instance = Title_filter()
      title_dic_res = api_instance.add_sub_attr_word_in_amz_title_dic(sub_attr_id=subAttrId, sub_attr_word=word)

      # print(title_dic_res)
      res.message = 'Successful'
      response_status = 200

          # if title_dic_res:
          #     res.message = 'Successful'
          #     response_status = 200
          # else:
          #     res.message = 'Add title_dic attr Failed'
          #     response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def post_dictionary_sub_attrs_words_count_reset(subAttrIds):
    res = PostDictionarySubAttrsWordsCountResetResponse()

    try:
      title_dic_api = AMZ_title_dic()

      num = 0
      for sub_attr_id in subAttrIds:
        title_dic_api_res = title_dic_api.reset_count_to_zero_by_sub_attr_id(sub_attr_id=sub_attr_id)
        num += 1

      if len(subAttrIds) == num:
        res.message = 'Successful'
        response_status = 200
      else:
        res.message = 'Success partially'
        response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

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
