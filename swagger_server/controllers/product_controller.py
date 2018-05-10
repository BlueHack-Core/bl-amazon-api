import connexion
import six

from swagger_server.models.get_products_browse_node_attributes_response import GetProductsBrowseNodeAttributesResponse  # noqa: E501
from swagger_server.models.get_products_browse_node_valid_value_response import GetProductsBrowseNodeValidValueResponse  # noqa: E501
from swagger_server.models.get_products_status_response import GetProductsStatusResponse  # noqa: E501
from swagger_server import util

from controller.products import Products

def get_products_browse_node_attributes(nodeId):  # noqa: E501
    """Get attributes within a specified browse node for title generating

    Return Attributes # noqa: E501

    :param nodeId:
    :type nodeId: str

    :rtype: GetProductsBrowseNodeAttributesResponse
    """
    return Products.get_products_browse_node_attributes(nodeId=nodeId)

def get_products_browse_node_valid_value(nodeId):  # noqa: E501
    """Get the browse node&#39;s valid value for submiting a flat file

    Return Valid Value # noqa: E501

    :param nodeId:
    :type nodeId: str

    :rtype: GetProductsBrowseNodeValidValueResponse
    """
    return Products.get_products_browse_node_valid_value(nodeId=nodeId)

def get_products_status():  # noqa: E501
    """Get Product API status

    Returns Product API status # noqa: E501


    :rtype: GetProductsStatusResponse
    """
    return Products.get_products_status()
