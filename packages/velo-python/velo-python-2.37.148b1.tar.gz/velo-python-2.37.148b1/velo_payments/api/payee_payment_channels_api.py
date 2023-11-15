# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   ## Http Status Codes Following is a list of Http Status codes that could be returned by the platform      | Status Code            | Description                                                                          |     | -----------------------| -------------------------------------------------------------------------------------|     | 200 OK                 | The request was successfully processed and usually returns a json response           |     | 201 Created            | A resource was created and a Location header is returned linking to the new resource |     | 202 Accepted           | The request has been accepted for processing                                         |     | 204 No Content         | The request has been processed and there is no response (usually deletes and updates)|     | 400 Bad Request        | The request is invalid and should be fixed before retrying                           |     | 401 Unauthorized       | Authentication has failed, usually means the token has expired                       |     | 403 Forbidden          | The user does not have permissions for the request                                   |     | 404 Not Found          | The resource was not found                                                           |     | 409 Conflict           | The resource already exists and there is a conflict                                  |     | 429 Too Many Requests  | The user has submitted too many requests in a given amount of time                   |     | 5xx Server Error       | Platform internal error (should rarely happen)                                       |   # noqa: E501

    The version of the OpenAPI document: 2.37.148
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from velo_payments.api_client import ApiClient
from velo_payments.exceptions import (
    ApiTypeError,
    ApiValueError
)


class PayeePaymentChannelsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_payment_channel_v4(self, payee_id, create_payment_channel_request_v4, **kwargs):  # noqa: E501
        """Create Payment Channel  # noqa: E501

        <p>Create a payment channel</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_channel_v4(payee_id, create_payment_channel_request_v4, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param CreatePaymentChannelRequestV4 create_payment_channel_request_v4: Post payment channel to update (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_payment_channel_v4_with_http_info(payee_id, create_payment_channel_request_v4, **kwargs)  # noqa: E501

    def create_payment_channel_v4_with_http_info(self, payee_id, create_payment_channel_request_v4, **kwargs):  # noqa: E501
        """Create Payment Channel  # noqa: E501

        <p>Create a payment channel</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_channel_v4_with_http_info(payee_id, create_payment_channel_request_v4, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param CreatePaymentChannelRequestV4 create_payment_channel_request_v4: Post payment channel to update (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'create_payment_channel_request_v4']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment_channel_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `create_payment_channel_v4`")  # noqa: E501
        # verify the required parameter 'create_payment_channel_request_v4' is set
        if ('create_payment_channel_request_v4' not in local_var_params or
                local_var_params['create_payment_channel_request_v4'] is None):
            raise ApiValueError("Missing the required parameter `create_payment_channel_request_v4` when calling `create_payment_channel_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_payment_channel_request_v4' in local_var_params:
            body_params = local_var_params['create_payment_channel_request_v4']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/payees/{payeeId}/paymentChannels/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_payment_channel_v4(self, payee_id, payment_channel_id, **kwargs):  # noqa: E501
        """Delete Payment Channel  # noqa: E501

        <p>Delete a payees payment channel</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_payment_channel_v4(payee_id, payment_channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payment_channel_id: The UUID of the payment channel. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_payment_channel_v4_with_http_info(payee_id, payment_channel_id, **kwargs)  # noqa: E501

    def delete_payment_channel_v4_with_http_info(self, payee_id, payment_channel_id, **kwargs):  # noqa: E501
        """Delete Payment Channel  # noqa: E501

        <p>Delete a payees payment channel</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_payment_channel_v4_with_http_info(payee_id, payment_channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payment_channel_id: The UUID of the payment channel. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'payment_channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_payment_channel_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `delete_payment_channel_v4`")  # noqa: E501
        # verify the required parameter 'payment_channel_id' is set
        if ('payment_channel_id' not in local_var_params or
                local_var_params['payment_channel_id'] is None):
            raise ApiValueError("Missing the required parameter `payment_channel_id` when calling `delete_payment_channel_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501
        if 'payment_channel_id' in local_var_params:
            path_params['paymentChannelId'] = local_var_params['payment_channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/payees/{payeeId}/paymentChannels/{paymentChannelId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable_payment_channel_v4(self, payee_id, payment_channel_id, **kwargs):  # noqa: E501
        """Enable Payment Channel  # noqa: E501

        <p>Enable a payment channel for a payee</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_payment_channel_v4(payee_id, payment_channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payment_channel_id: The UUID of the payment channel. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.enable_payment_channel_v4_with_http_info(payee_id, payment_channel_id, **kwargs)  # noqa: E501

    def enable_payment_channel_v4_with_http_info(self, payee_id, payment_channel_id, **kwargs):  # noqa: E501
        """Enable Payment Channel  # noqa: E501

        <p>Enable a payment channel for a payee</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_payment_channel_v4_with_http_info(payee_id, payment_channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payment_channel_id: The UUID of the payment channel. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'payment_channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_payment_channel_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `enable_payment_channel_v4`")  # noqa: E501
        # verify the required parameter 'payment_channel_id' is set
        if ('payment_channel_id' not in local_var_params or
                local_var_params['payment_channel_id'] is None):
            raise ApiValueError("Missing the required parameter `payment_channel_id` when calling `enable_payment_channel_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501
        if 'payment_channel_id' in local_var_params:
            path_params['paymentChannelId'] = local_var_params['payment_channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/payees/{payeeId}/paymentChannels/{paymentChannelId}/enable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payment_channel_v4(self, payee_id, payment_channel_id, **kwargs):  # noqa: E501
        """Get Payment Channel Details  # noqa: E501

        <p>Get the payment channel details for the payee</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_channel_v4(payee_id, payment_channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payment_channel_id: The UUID of the payment channel. (required)
        :param bool payable: payable if true only return the payment channel if the payee is payable
        :param bool sensitive: <p>Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked.</p> <p>If set to true, and you have permission, the PII values will be returned as their original unmasked values.</p> 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaymentChannelResponseV4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payment_channel_v4_with_http_info(payee_id, payment_channel_id, **kwargs)  # noqa: E501

    def get_payment_channel_v4_with_http_info(self, payee_id, payment_channel_id, **kwargs):  # noqa: E501
        """Get Payment Channel Details  # noqa: E501

        <p>Get the payment channel details for the payee</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_channel_v4_with_http_info(payee_id, payment_channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payment_channel_id: The UUID of the payment channel. (required)
        :param bool payable: payable if true only return the payment channel if the payee is payable
        :param bool sensitive: <p>Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked.</p> <p>If set to true, and you have permission, the PII values will be returned as their original unmasked values.</p> 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaymentChannelResponseV4, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'payment_channel_id', 'payable', 'sensitive']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_channel_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `get_payment_channel_v4`")  # noqa: E501
        # verify the required parameter 'payment_channel_id' is set
        if ('payment_channel_id' not in local_var_params or
                local_var_params['payment_channel_id'] is None):
            raise ApiValueError("Missing the required parameter `payment_channel_id` when calling `get_payment_channel_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501
        if 'payment_channel_id' in local_var_params:
            path_params['paymentChannelId'] = local_var_params['payment_channel_id']  # noqa: E501

        query_params = []
        if 'payable' in local_var_params:
            query_params.append(('payable', local_var_params['payable']))  # noqa: E501
        if 'sensitive' in local_var_params:
            query_params.append(('sensitive', local_var_params['sensitive']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/payees/{payeeId}/paymentChannels/{paymentChannelId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentChannelResponseV4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payment_channels_v4(self, payee_id, **kwargs):  # noqa: E501
        """Get All Payment Channels Details  # noqa: E501

        <p>Get all payment channels details for a payee</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_channels_v4(payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payor_id: <p>(UUID) the id of the Payor.</p> <p>If specified the payment channels are filtered to those mapped to this payor.</p> 
        :param bool payable: payable if true only return the payment channel if the payee is payable
        :param bool sensitive: <p>Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked.</p> <p>If set to true, and you have permission, the PII values will be returned as their original unmasked values.</p> 
        :param bool ignore_payor_invite_status: payable if true only return the payment channel if the payee is payable
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaymentChannelsResponseV4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payment_channels_v4_with_http_info(payee_id, **kwargs)  # noqa: E501

    def get_payment_channels_v4_with_http_info(self, payee_id, **kwargs):  # noqa: E501
        """Get All Payment Channels Details  # noqa: E501

        <p>Get all payment channels details for a payee</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_channels_v4_with_http_info(payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payor_id: <p>(UUID) the id of the Payor.</p> <p>If specified the payment channels are filtered to those mapped to this payor.</p> 
        :param bool payable: payable if true only return the payment channel if the payee is payable
        :param bool sensitive: <p>Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked.</p> <p>If set to true, and you have permission, the PII values will be returned as their original unmasked values.</p> 
        :param bool ignore_payor_invite_status: payable if true only return the payment channel if the payee is payable
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaymentChannelsResponseV4, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'payor_id', 'payable', 'sensitive', 'ignore_payor_invite_status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_channels_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `get_payment_channels_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501

        query_params = []
        if 'payor_id' in local_var_params:
            query_params.append(('payorId', local_var_params['payor_id']))  # noqa: E501
        if 'payable' in local_var_params:
            query_params.append(('payable', local_var_params['payable']))  # noqa: E501
        if 'sensitive' in local_var_params:
            query_params.append(('sensitive', local_var_params['sensitive']))  # noqa: E501
        if 'ignore_payor_invite_status' in local_var_params:
            query_params.append(('ignorePayorInviteStatus', local_var_params['ignore_payor_invite_status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/payees/{payeeId}/paymentChannels/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentChannelsResponseV4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_payment_channel_order_v4(self, payee_id, payment_channel_order_request_v4, **kwargs):  # noqa: E501
        """Update Payees preferred Payment Channel order  # noqa: E501

        <p>Update the Payee's preferred order of payment channels by passing in just the payment channel ids. When payments are made to the payee then in the absence of any other rules (e.g. matching on currency) the first payment channel in this list will be chosen. </p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_payment_channel_order_v4(payee_id, payment_channel_order_request_v4, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param PaymentChannelOrderRequestV4 payment_channel_order_request_v4: Put the payment channel ids in the preferred order (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_payment_channel_order_v4_with_http_info(payee_id, payment_channel_order_request_v4, **kwargs)  # noqa: E501

    def update_payment_channel_order_v4_with_http_info(self, payee_id, payment_channel_order_request_v4, **kwargs):  # noqa: E501
        """Update Payees preferred Payment Channel order  # noqa: E501

        <p>Update the Payee's preferred order of payment channels by passing in just the payment channel ids. When payments are made to the payee then in the absence of any other rules (e.g. matching on currency) the first payment channel in this list will be chosen. </p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_payment_channel_order_v4_with_http_info(payee_id, payment_channel_order_request_v4, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param PaymentChannelOrderRequestV4 payment_channel_order_request_v4: Put the payment channel ids in the preferred order (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'payment_channel_order_request_v4']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment_channel_order_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `update_payment_channel_order_v4`")  # noqa: E501
        # verify the required parameter 'payment_channel_order_request_v4' is set
        if ('payment_channel_order_request_v4' not in local_var_params or
                local_var_params['payment_channel_order_request_v4'] is None):
            raise ApiValueError("Missing the required parameter `payment_channel_order_request_v4` when calling `update_payment_channel_order_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_channel_order_request_v4' in local_var_params:
            body_params = local_var_params['payment_channel_order_request_v4']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/payees/{payeeId}/paymentChannels/order', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_payment_channel_v4(self, payee_id, payment_channel_id, update_payment_channel_request_v4, **kwargs):  # noqa: E501
        """Update Payment Channel  # noqa: E501

        <p>Update the details of the payment channel. Note payment channels are immutable. The current payment channel will be logically deleted as part of this call and replaced with new one with the correct details; this endpoint will return a Location header with a link to the new payment channel upon success. Updating a currently disabled payment channel will result in a new, fully enabled, payment channel.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_payment_channel_v4(payee_id, payment_channel_id, update_payment_channel_request_v4, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payment_channel_id: The UUID of the payment channel. (required)
        :param UpdatePaymentChannelRequestV4 update_payment_channel_request_v4: Post payment channel to update (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_payment_channel_v4_with_http_info(payee_id, payment_channel_id, update_payment_channel_request_v4, **kwargs)  # noqa: E501

    def update_payment_channel_v4_with_http_info(self, payee_id, payment_channel_id, update_payment_channel_request_v4, **kwargs):  # noqa: E501
        """Update Payment Channel  # noqa: E501

        <p>Update the details of the payment channel. Note payment channels are immutable. The current payment channel will be logically deleted as part of this call and replaced with new one with the correct details; this endpoint will return a Location header with a link to the new payment channel upon success. Updating a currently disabled payment channel will result in a new, fully enabled, payment channel.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_payment_channel_v4_with_http_info(payee_id, payment_channel_id, update_payment_channel_request_v4, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param str payment_channel_id: The UUID of the payment channel. (required)
        :param UpdatePaymentChannelRequestV4 update_payment_channel_request_v4: Post payment channel to update (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'payment_channel_id', 'update_payment_channel_request_v4']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment_channel_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `update_payment_channel_v4`")  # noqa: E501
        # verify the required parameter 'payment_channel_id' is set
        if ('payment_channel_id' not in local_var_params or
                local_var_params['payment_channel_id'] is None):
            raise ApiValueError("Missing the required parameter `payment_channel_id` when calling `update_payment_channel_v4`")  # noqa: E501
        # verify the required parameter 'update_payment_channel_request_v4' is set
        if ('update_payment_channel_request_v4' not in local_var_params or
                local_var_params['update_payment_channel_request_v4'] is None):
            raise ApiValueError("Missing the required parameter `update_payment_channel_request_v4` when calling `update_payment_channel_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501
        if 'payment_channel_id' in local_var_params:
            path_params['paymentChannelId'] = local_var_params['payment_channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_payment_channel_request_v4' in local_var_params:
            body_params = local_var_params['update_payment_channel_request_v4']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/payees/{payeeId}/paymentChannels/{paymentChannelId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
