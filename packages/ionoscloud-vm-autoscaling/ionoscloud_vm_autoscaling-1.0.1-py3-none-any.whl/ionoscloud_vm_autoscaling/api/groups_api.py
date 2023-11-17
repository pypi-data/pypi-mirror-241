from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_vm_autoscaling.api_client import ApiClient
from ionoscloud_vm_autoscaling.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GroupsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def groups_actions_find_by_id(self, action_id, group_id, **kwargs):  # noqa: E501
        """Get Scaling Action Details by ID  # noqa: E501

        Retrieves the details of a scaling action specified by its ID. This operation returns metadata, properties, and the current status, for the specified scaling action  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_actions_find_by_id(action_id, group_id, async_req=True)
        >>> result = thread.get()

        :param action_id: (required)
        :type action_id: str
        :param group_id: (required)
        :type group_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Action
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_actions_find_by_id_with_http_info(action_id, group_id, **kwargs)  # noqa: E501

    def groups_actions_find_by_id_with_http_info(self, action_id, group_id, **kwargs):  # noqa: E501
        """Get Scaling Action Details by ID  # noqa: E501

        Retrieves the details of a scaling action specified by its ID. This operation returns metadata, properties, and the current status, for the specified scaling action  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_actions_find_by_id_with_http_info(action_id, group_id, async_req=True)
        >>> result = thread.get()

        :param action_id: (required)
        :type action_id: str
        :param group_id: (required)
        :type group_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Action, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'action_id',
            'group_id',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_actions_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'action_id' is set
        if self.api_client.client_side_validation and ('action_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['action_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `action_id` when calling `groups_actions_find_by_id`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_actions_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'action_id' in local_var_params:
            path_params['actionId'] = local_var_params['action_id']  # noqa: E501
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'Action'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups/{groupId}/actions/{actionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def groups_actions_get(self, group_id, **kwargs):  # noqa: E501
        """Get Scaling Actions  # noqa: E501

        Retrieves the list of the scaling actions for the Auto Scaling group specified by its ID.    >Note that currently, only the last ten actions are returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_actions_get(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param order_by: Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ActionCollection
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_actions_get_with_http_info(group_id, **kwargs)  # noqa: E501

    def groups_actions_get_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Get Scaling Actions  # noqa: E501

        Retrieves the list of the scaling actions for the Auto Scaling group specified by its ID.    >Note that currently, only the last ten actions are returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_actions_get_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param order_by: Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ActionCollection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'depth',
            'order_by'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_actions_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_actions_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ActionCollection'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups/{groupId}/actions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def groups_delete(self, group_id, **kwargs):  # noqa: E501
        """Delete an Auto Scaling Group by ID  # noqa: E501

        Deletes the Auto Scaling group specified by its ID.  >Deleting the associated servers and disks is currently not implemented.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_delete(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_delete_with_http_info(group_id, **kwargs)  # noqa: E501

    def groups_delete_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Delete an Auto Scaling Group by ID  # noqa: E501

        Deletes the Auto Scaling group specified by its ID.  >Deleting the associated servers and disks is currently not implemented.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_delete_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups/{groupId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def groups_find_by_id(self, group_id, **kwargs):  # noqa: E501
        """Get an Auto Scaling by ID  # noqa: E501

        Retrieves the Auto Scaling group specified by its ID including the details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_find_by_id(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Group
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_find_by_id_with_http_info(group_id, **kwargs)  # noqa: E501

    def groups_find_by_id_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Get an Auto Scaling by ID  # noqa: E501

        Retrieves the Auto Scaling group specified by its ID including the details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_find_by_id_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Group, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'Group'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups/{groupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def groups_get(self, **kwargs):  # noqa: E501
        """Get Auto Scaling Groups  # noqa: E501

        Lists all Auto Scaling groups of your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_get(async_req=True)
        >>> result = thread.get()

        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param order_by: Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GroupCollection
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_get_with_http_info(**kwargs)  # noqa: E501

    def groups_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Auto Scaling Groups  # noqa: E501

        Lists all Auto Scaling groups of your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param order_by: Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GroupCollection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'depth',
            'order_by'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'GroupCollection'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def groups_post(self, group_post, **kwargs):  # noqa: E501
        """Create an Auto Scaling Group  # noqa: E501

        Creates an Auto Scaling group.   > Note that creating a group triggers the creation of two monitoring alarms for 'Scale-In' and 'Scale-Out' operations according to the 'Policy' settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_post(group_post, async_req=True)
        >>> result = thread.get()

        :param group_post: (required)
        :type group_post: GroupPost
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GroupPostResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_post_with_http_info(group_post, **kwargs)  # noqa: E501

    def groups_post_with_http_info(self, group_post, **kwargs):  # noqa: E501
        """Create an Auto Scaling Group  # noqa: E501

        Creates an Auto Scaling group.   > Note that creating a group triggers the creation of two monitoring alarms for 'Scale-In' and 'Scale-Out' operations according to the 'Policy' settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_post_with_http_info(group_post, async_req=True)
        >>> result = thread.get()

        :param group_post: (required)
        :type group_post: GroupPost
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GroupPostResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_post'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_post' is set
        if self.api_client.client_side_validation and ('group_post' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_post'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_post` when calling `groups_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group_post' in local_var_params:
            body_params = local_var_params['group_post']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'GroupPostResponse'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def groups_put(self, group_id, group_put, **kwargs):  # noqa: E501
        """Update an Auto Scaling Group by ID  # noqa: E501

        Updates the Auto Scaling group specified by its ID. The IDs assigned by the system when the resource is created, such as 'properties.datacenter.id' and 'backupunitId', are immutable and cannot be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_put(group_id, group_put, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param group_put: (required)
        :type group_put: GroupPut
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Group
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_put_with_http_info(group_id, group_put, **kwargs)  # noqa: E501

    def groups_put_with_http_info(self, group_id, group_put, **kwargs):  # noqa: E501
        """Update an Auto Scaling Group by ID  # noqa: E501

        Updates the Auto Scaling group specified by its ID. The IDs assigned by the system when the resource is created, such as 'properties.datacenter.id' and 'backupunitId', are immutable and cannot be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_put_with_http_info(group_id, group_put, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param group_put: (required)
        :type group_put: GroupPut
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Group, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'group_put'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_put`")  # noqa: E501
        # verify the required parameter 'group_put' is set
        if self.api_client.client_side_validation and ('group_put' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_put'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_put` when calling `groups_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group_put' in local_var_params:
            body_params = local_var_params['group_put']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'Group'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups/{groupId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def groups_servers_find_by_id(self, group_id, server_id, **kwargs):  # noqa: E501
        """Get Auto Scaling Group Server by ID  # noqa: E501

        Retrieves the properties of the server specified by its ID.  >Note that the server IDs of the Auto Scaling groups are different from and do not match the VM server IDs in the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_servers_find_by_id(group_id, server_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param server_id: (required)
        :type server_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Server
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_servers_find_by_id_with_http_info(group_id, server_id, **kwargs)  # noqa: E501

    def groups_servers_find_by_id_with_http_info(self, group_id, server_id, **kwargs):  # noqa: E501
        """Get Auto Scaling Group Server by ID  # noqa: E501

        Retrieves the properties of the server specified by its ID.  >Note that the server IDs of the Auto Scaling groups are different from and do not match the VM server IDs in the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_servers_find_by_id_with_http_info(group_id, server_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param server_id: (required)
        :type server_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Server, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'server_id',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_servers_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_servers_find_by_id`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `groups_servers_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'Server'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups/{groupId}/servers/{serverId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def groups_servers_get(self, group_id, **kwargs):  # noqa: E501
        """Get Auto Scaling Group Servers  # noqa: E501

        Retrieves all servers associated with the Auto Scaling group specified by its ID.   >Note that the server IDs of the Auto Scaling groups are different from and do not match the VM server IDs in the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_servers_get(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param order_by: Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ServerCollection
        """
        kwargs['_return_http_data_only'] = True
        return self.groups_servers_get_with_http_info(group_id, **kwargs)  # noqa: E501

    def groups_servers_get_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Get Auto Scaling Group Servers  # noqa: E501

        Retrieves all servers associated with the Auto Scaling group specified by its ID.   >Note that the server IDs of the Auto Scaling groups are different from and do not match the VM server IDs in the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_servers_get_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: (required)
        :type group_id: str
        :param depth: With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.  
        :type depth: float
        :param order_by: Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``.
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ServerCollection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'depth',
            'order_by'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_servers_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `groups_servers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ServerCollection'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/groups/{groupId}/servers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
