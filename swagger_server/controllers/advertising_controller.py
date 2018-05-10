import connexion
import six

from swagger_server.models.get_advertising_browse_nodes_response import GetAdvertisingBrowseNodesResponse  # noqa: E501
from swagger_server.models.get_advertising_browse_nodes_top_sellers_response import GetAdvertisingBrowseNodesTopSellersResponse  # noqa: E501
from swagger_server import util

from controller.advertising import Advertising

def get_advertising_browse_node(nodeId):  # noqa: E501
    """Get browse node hierarchy from Amazon

    Return BrowseNodes Hierarchy # noqa: E501

    :param nodeId: 
    :type nodeId: str

    :rtype: GetAdvertisingBrowseNodesResponse
    """
    return Advertising.get_advertising_browse_node(nodeId=nodeId)

def get_advertising_browse_node_top_sellers(nodeId):  # noqa: E501
    """Get 10 top sellers within a specified browse node from Amazon

    Return 10 top sellers # noqa: E501

    :param nodeId: 
    :type nodeId: str

    :rtype: GetAdvertisingBrowseNodesTopSellersResponse
    """
    return Advertising.get_advertising_browse_node_top_sellers(nodeId=nodeId)

def get_advertising_status():  # noqa: E501
    """Get Amazon Product Advertising API status

    Returns Amazon Product Advertising API status (GREEN/YELLOW/RED) # noqa: E501


    :rtype: GetAdvertisingStatusResponse
    """
    return Advertising.get_advertising_status()
