import connexion
import six

# from swagger_server.models.get_dictionary_words_filtered_response import GetDictionaryWordsFilteredResponse  # noqa: E501
# from swagger_server.models.get_dictionary_words_response import GetDictionaryWordsResponse  # noqa: E501
# from swagger_server.models.get_tool_titles_response import GetToolTitlesResponse  # noqa: E501
# from swagger_server.models.post_dictionary_products_attrs_sub_attrs_response import PostDictionaryProductsAttrsSubAttrsResponse  # noqa: E501
# from swagger_server.models.post_dictionary_words_response import PostDictionaryWordsResponse  # noqa: E501
# from swagger_server import util

from controller.tool import Tool

def get_dictionary_words(nodeIds):  # noqa: E501
    """Get dictionary words for filtering within a specified browse node

    Return Dictionary Words for filtering ingredients # noqa: E501

    :param nodeId: 
    :type nodeId: str

    :rtype: GetDictionaryWordsResponse
    """
    return Tool.get_dictionary_words(nodeIds=nodeIds)


def get_dictionary_words_filtered(nodeId, filters):  # noqa: E501
    """Get filtered words within a specified browse node with filtering words

    Return filtered words cloud # noqa: E501

    :param nodeId: 
    :type nodeId: str
    :param filters: 
    :type filters: List[str]

    :rtype: GetDictionaryWordsFilteredResponse
    """
    return Tool.get_dictionary_words_filtered(nodeId=nodeId, filters=filters)


def get_tool_titles(nodeId):  # noqa: E501
    """Get 100 amazon best selling item titles within a specified browse node

    Return Titles # noqa: E501

    :param nodeId: 
    :type nodeId: str

    :rtype: GetToolTitlesResponse
    """
    return Tool.get_tool_titles(nodeId=nodeId)


def post_dictionary_products_attrs_sub_attrs(nodeId, attrId, subAttrId, subAttrUsName, subAttrKrName, attrUsName=None, attrKrName=None):  # noqa: E501
    """Add sub attribute within a specified browse node&#39;s attribute

    Add sub attribute # noqa: E501

    :param nodeId: 
    :type nodeId: str
    :param attrId: 
    :type attrId: str
    :param subAttrId: 
    :type subAttrId: str
    :param subAttrUsName: 
    :type subAttrUsName: str
    :param subAttrKrName: 
    :type subAttrKrName: str
    :param attrUsName: Upserting if exists
    :type attrUsName: str
    :param attrKrName: Upserting if exists
    :type attrKrName: str

    :rtype: PostDictionaryProductsAttrsSubAttrsResponse
    """
    return Tool.post_dictionary_products_attrs_sub_attrs(nodeId=nodeId, attrId=attrId, attrUsName=attrUsName, attrKrName=attrKrName, subAttrId=subAttrId, subAttrUsName=subAttrUsName, subAttrKrName=subAttrKrName)


def post_dictionary_words(subAttrId, word):  # noqa: E501
    """Add filtering word to dictionary

    Add to dictionary # noqa: E501

    :param subAttrId: 
    :type subAttrId: str
    :param word: 
    :type word: str

    :rtype: PostDictionaryWordsResponse
    """
    return Tool.post_dictionary_words(subAttrId=subAttrId, word=word)
