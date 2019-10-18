# coding: utf-8

"""
    IdCheck.IO API

    Check identity documents

    OpenAPI spec version: 0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""



import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SandboxApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_image(self, image_uid, **kwargs):
        """
        HTTP GET image
        GET image

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_image(image_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str image_uid: EnumDemoDocsImage (required)
        :param str raw_type: Image raw type
        :param str face: Image face
        :param str light: Image light
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_image_with_http_info(image_uid, **kwargs)
        else:
            (data) = self.get_image_with_http_info(image_uid, **kwargs)
            return data

    def get_image_with_http_info(self, image_uid, **kwargs):
        """
        HTTP GET image
        GET image

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_image_with_http_info(image_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str image_uid: EnumDemoDocsImage (required)
        :param str raw_type: Image raw type
        :param str face: Image face
        :param str light: Image light
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['image_uid', 'raw_type', 'face', 'light']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_uid' is set
        if ('image_uid' not in params) or (params['image_uid'] is None):
            raise ValueError("Missing the required parameter `image_uid` when calling `get_image`")

        resource_path = '/v0/sandbox/image/{imageUid}'.replace('{format}', 'json')
        path_params = {}
        if 'image_uid' in params:
            path_params['imageUid'] = params['image_uid']

        query_params = {}
        if 'raw_type' in params:
            query_params['rawType'] = params['raw_type']
        if 'face' in params:
            query_params['face'] = params['face']
        if 'light' in params:
            query_params['light'] = params['light']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[str]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_image_list(self, **kwargs):
        """
        HTTP GET images list
        GET images list

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_image_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ImageListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_image_list_with_http_info(**kwargs)
        else:
            (data) = self.get_image_list_with_http_info(**kwargs)
            return data

    def get_image_list_with_http_info(self, **kwargs):
        """
        HTTP GET images list
        GET images list

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_image_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ImageListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_list" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v0/sandbox/imagelist'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ImageListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_mrz(self, mrz_uid, **kwargs):
        """
        HTTP GET mrz
        GET mrz

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_mrz(mrz_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str mrz_uid: EnumDemoDocsMrz (required)
        :return: MrzResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_mrz_with_http_info(mrz_uid, **kwargs)
        else:
            (data) = self.get_mrz_with_http_info(mrz_uid, **kwargs)
            return data

    def get_mrz_with_http_info(self, mrz_uid, **kwargs):
        """
        HTTP GET mrz
        GET mrz

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_mrz_with_http_info(mrz_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str mrz_uid: EnumDemoDocsMrz (required)
        :return: MrzResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mrz_uid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mrz" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mrz_uid' is set
        if ('mrz_uid' not in params) or (params['mrz_uid'] is None):
            raise ValueError("Missing the required parameter `mrz_uid` when calling `get_mrz`")

        resource_path = '/v0/sandbox/mrz/{mrzUid}'.replace('{format}', 'json')
        path_params = {}
        if 'mrz_uid' in params:
            path_params['mrzUid'] = params['mrz_uid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MrzResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_mrz_list(self, **kwargs):
        """
        HTTP GET mrz list
        GET mrz list

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_mrz_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: MrzListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_mrz_list_with_http_info(**kwargs)
        else:
            (data) = self.get_mrz_list_with_http_info(**kwargs)
            return data

    def get_mrz_list_with_http_info(self, **kwargs):
        """
        HTTP GET mrz list
        GET mrz list

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_mrz_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: MrzListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mrz_list" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v0/sandbox/mrzlist'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MrzListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
