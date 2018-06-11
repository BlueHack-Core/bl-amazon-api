# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_dictionary_browse_nodes_all_response import GetDictionaryBrowseNodesAllResponse  # noqa: E501
from swagger_server.models.get_dictionary_products_attrs_response import GetDictionaryProductsAttrsResponse  # noqa: E501
from swagger_server.models.get_dictionary_products_attrs_sub_attrs_response import GetDictionaryProductsAttrsSubAttrsResponse  # noqa: E501
from swagger_server.models.get_dictionary_products_attrs_sub_attrs_words_response import GetDictionaryProductsAttrsSubAttrsWordsResponse  # noqa: E501
from swagger_server.models.get_dictionary_sub_attrs_words_response import GetDictionarySubAttrsWordsResponse  # noqa: E501
from swagger_server.models.get_dictionary_words_filtered_response import GetDictionaryWordsFilteredResponse  # noqa: E501
from swagger_server.models.get_dictionary_words_response import GetDictionaryWordsResponse  # noqa: E501
from swagger_server.models.get_tool_titles_response import GetToolTitlesResponse  # noqa: E501
from swagger_server.models.post_dictionary_products_attrs_response import PostDictionaryProductsAttrsResponse  # noqa: E501
from swagger_server.models.post_dictionary_products_attrs_sub_attrs_response import PostDictionaryProductsAttrsSubAttrsResponse  # noqa: E501
from swagger_server.models.post_dictionary_products_attrs_sub_attrs_words_response import PostDictionaryProductsAttrsSubAttrsWordsResponse  # noqa: E501
from swagger_server.models.post_dictionary_sub_attrs_words_count_reset_response import PostDictionarySubAttrsWordsCountResetResponse  # noqa: E501
from swagger_server.models.post_dictionary_words_response import PostDictionaryWordsResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestToolController(BaseTestCase):
    """ToolController integration test stubs"""

    def test_get_dictionary_browse_nodes_all(self):
        """Test case for get_dictionary_browse_nodes_all

        Get all dictionary hierarchy within a specified browse node
        """
        response = self.client.open(
            '//tool/dictionary/browseNodes/{nodeId}/all'.format(nodeId='nodeId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dictionary_products_attrs(self):
        """Test case for get_dictionary_products_attrs

        Get an attribute within a specified browse node's
        """
        response = self.client.open(
            '//tool/dictionary/products/{nodeId}/attrs/{attrId}'.format(nodeId='nodeId_example', attrId='attrId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dictionary_products_attrs_sub_attrs(self):
        """Test case for get_dictionary_products_attrs_sub_attrs

        Get a sub attribute within a specified browse node's attribute
        """
        response = self.client.open(
            '//tool/dictionary/products/{nodeId}/attrs/{attrId}/subAttrs/{subAttrId}'.format(nodeId='nodeId_example', attrId='attrId_example', subAttrId='subAttrId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dictionary_products_attrs_sub_attrs_words(self):
        """Test case for get_dictionary_products_attrs_sub_attrs_words

        Check the dic_word contains within a specified browse node's attribute's sub attribute
        """
        query_string = [('word', 'word_example')]
        response = self.client.open(
            '//tool/dictionary/products/{nodeId}/attrs/{attrId}/subAttrs/{subAttrId}/words'.format(nodeId='nodeId_example', attrId='attrId_example', subAttrId='subAttrId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dictionary_sub_attrs_words(self):
        """Test case for get_dictionary_sub_attrs_words

        Get dictionary words with subAttrId list
        """
        query_string = [('subAttrIds', 'subAttrIds_example')]
        response = self.client.open(
            '//tool/dictionary/subAttrs/words',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dictionary_words(self):
        """Test case for get_dictionary_words

        [DEPRECATED] Get dictionary words for filtering within specified browse nodes
        """
        query_string = [('nodeIds', 'nodeIds_example')]
        response = self.client.open(
            '//tool/dictionary/words',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dictionary_words_filtered(self):
        """Test case for get_dictionary_words_filtered

        Get filtered words within a specified browse node with filtering words
        """
        query_string = [('filters', 'filters_example')]
        response = self.client.open(
            '//tool/dictionary/words/{nodeId}/filtered'.format(nodeId='nodeId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_tool_titles(self):
        """Test case for get_tool_titles

        Get 100 amazon best selling item titles within a specified browse node
        """
        response = self.client.open(
            '//tool/titles/{nodeId}'.format(nodeId='nodeId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_dictionary_products_attrs(self):
        """Test case for post_dictionary_products_attrs

        Add attribute within a specified browse node's
        """
        query_string = [('attrUsName', 'attrUsName_example'),
                        ('attrKrName', 'attrKrName_example')]
        response = self.client.open(
            '//tool/dictionary/products/{nodeId}/attrs/{attrId}'.format(nodeId='nodeId_example', attrId='attrId_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_dictionary_products_attrs_sub_attrs(self):
        """Test case for post_dictionary_products_attrs_sub_attrs

        Add sub attribute within a specified browse node's attribute
        """
        query_string = [('subAttrUsName', 'subAttrUsName_example'),
                        ('subAttrKrName', 'subAttrKrName_example')]
        response = self.client.open(
            '//tool/dictionary/products/{nodeId}/attrs/{attrId}/subAttrs/{subAttrId}'.format(nodeId='nodeId_example', attrId='attrId_example', subAttrId='subAttrId_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_dictionary_products_attrs_sub_attrs_words(self):
        """Test case for post_dictionary_products_attrs_sub_attrs_words

        Add a dic_word within a specified browse node's attribute's sub attribute
        """
        query_string = [('word', 'word_example')]
        response = self.client.open(
            '//tool/dictionary/products/{nodeId}/attrs/{attrId}/subAttrs/{subAttrId}/words'.format(nodeId='nodeId_example', attrId='attrId_example', subAttrId='subAttrId_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_dictionary_sub_attrs_words_count_reset(self):
        """Test case for post_dictionary_sub_attrs_words_count_reset

        Reset title_dic counts
        """
        query_string = [('subAttrIds', 'subAttrIds_example')]
        response = self.client.open(
            '//tool/dictionary/subAttrs/words/count/reset',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_dictionary_words(self):
        """Test case for post_dictionary_words

        [DEPRECATED] Add filtering word to dictionary
        """
        query_string = [('subAttrId', 'subAttrId_example'),
                        ('word', 'word_example')]
        response = self.client.open(
            '//tool/dictionary/words',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
