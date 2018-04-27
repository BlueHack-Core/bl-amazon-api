import connexion
import six

from swagger_server.models.simple_image import SimpleImage  # noqa: E501
from swagger_server import util

from controller.mwss import MWSs

def get_products(offset=None, limit=None):  # noqa: E501
    """

    Returns Main Feeds # noqa: E501

    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    :rtype: SimpleImage
    """
    return MWSs.get_products(offset=offset, limit=limit)
