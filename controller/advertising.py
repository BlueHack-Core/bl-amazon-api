import os
import bottlenose
from bs4 import BeautifulSoup

from swagger_server.models.get_advertising_browse_nodes_response import GetAdvertisingBrowseNodesResponse
from swagger_server.models.get_advertising_browse_nodes_response_data import GetAdvertisingBrowseNodesResponseData
from swagger_server.models.browse_node import BrowseNode

from swagger_server.models.get_advertising_browse_nodes_top_sellers_response import GetAdvertisingBrowseNodesTopSellersResponse
from swagger_server.models.get_advertising_browse_nodes_top_sellers_response_data import GetAdvertisingBrowseNodesTopSellersResponseData
from swagger_server.models.top_item import TopItem

from swagger_server.models.get_advertising_status_response import GetAdvertisingStatusResponse

amazon = bottlenose.Amazon(AWSAccessKeyId=os.environ['AWS_ACCESS_KEY_ID'],
                           AWSSecretAccessKey=os.environ['AWS_SECRET_ACCESS_KEY'],
                           AssociateTag=os.environ['AWS_ASSOCIATE_TAG'],
                           Parser=lambda text: BeautifulSoup(text, 'xml'))

class Advertising(object):
  def __init__(self):
    super().__init__()

  @staticmethod
  def get_advertising_browse_node(nodeId):
    res = GetAdvertisingBrowseNodesResponse()

    try:
      res_data = GetAdvertisingBrowseNodesResponseData()

      amazon_res = amazon.BrowseNodeLookup(BrowseNodeId=nodeId, ResponseGroup='BrowseNodeInfo')

      children_list = []
      ancestors_list = []

      browse_nodes = amazon_res.find('BrowseNodes')
      for browse_node in browse_nodes:
        if browse_node.Name:
          res_data.name = browse_node.Name.text
        if browse_node.BrowseNodeId:
          res_data.node_id = browse_node.BrowseNodeId.text

        if browse_node.Children:
          for browse_node in browse_node.Children:
            bn = BrowseNode()
            bn.node_id = browse_node.BrowseNodeId.text
            bn.name = browse_node.Name.text

            children_list.append(bn)

      res_data.children = children_list

      res.data = res_data
      res.message = 'Successful'
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_advertising_browse_node_top_sellers(nodeId):
    res = GetAdvertisingBrowseNodesTopSellersResponse()

    try:
      res_data = GetAdvertisingBrowseNodesTopSellersResponseData()

      amazon_res = amazon.BrowseNodeLookup(BrowseNodeId=nodeId, ResponseGroup='TopSellers')

      top_item_list = []

      browse_nodes = amazon_res.find('BrowseNodes')
      for browse_node in browse_nodes:
        if browse_node.Name:
          res_data.name = browse_node.Name.text
        if browse_node.BrowseNodeId:
          res_data.node_id = browse_node.BrowseNodeId.text

        if browse_node.TopItemSet:
          # print(browse_node.TopItemSet)
          for top_item in browse_node.TopItemSet:
            if top_item.ASIN:
              ti = TopItem()
              ti.asin = top_item.ASIN.text
              ti.title = top_item.Title.text
              ti.detail_page_url = top_item.DetailPageURL.text
              ti.product_group = top_item.ProductGroup.text

              top_item_list.append(ti)

      res_data.top_items = top_item_list

      res.data = res_data
      res.message = 'Successful'
      response_status = 200

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_advertising_status():
    res = GetAdvertisingStatusResponse()

    try:
      test_node_id = '13727922011'
      amazon_res = amazon.BrowseNodeLookup(BrowseNodeId=test_node_id, ResponseGroup='')

      browse_nodes = amazon_res.find('BrowseNodes')
      for browse_node in browse_nodes:
        if browse_node.BrowseNodeId:
          if test_node_id == browse_node.BrowseNodeId.text:
            res.message = 'GREEN'
          else:
            res.message = 'YELLOW'
          response_status = 200
        else:
          res.message = 'RED'
          response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status
