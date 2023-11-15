# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   ## Http Status Codes Following is a list of Http Status codes that could be returned by the platform      | Status Code            | Description                                                                          |     | -----------------------| -------------------------------------------------------------------------------------|     | 200 OK                 | The request was successfully processed and usually returns a json response           |     | 201 Created            | A resource was created and a Location header is returned linking to the new resource |     | 202 Accepted           | The request has been accepted for processing                                         |     | 204 No Content         | The request has been processed and there is no response (usually deletes and updates)|     | 400 Bad Request        | The request is invalid and should be fixed before retrying                           |     | 401 Unauthorized       | Authentication has failed, usually means the token has expired                       |     | 403 Forbidden          | The user does not have permissions for the request                                   |     | 404 Not Found          | The resource was not found                                                           |     | 409 Conflict           | The resource already exists and there is a conflict                                  |     | 429 Too Many Requests  | The user has submitted too many requests in a given amount of time                   |     | 5xx Server Error       | Platform internal error (should rarely happen)                                       |   # noqa: E501

    The version of the OpenAPI document: 2.37.148
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentChannelResponseV4(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'payee_id': 'str',
        'payment_channel_name': 'str',
        'account_name': 'str',
        'channel_type': 'str',
        'country_code': 'str',
        'routing_number': 'str',
        'account_number': 'str',
        'iban': 'str',
        'currency': 'str',
        'payor_ids': 'list[str]',
        'payee_name': 'str',
        'bank_name': 'str',
        'bank_swift_bic': 'str',
        'bank_address': 'AddressV4',
        'deleted': 'bool',
        'enabled': 'bool',
        'disabled_reason_code': 'str',
        'disabled_reason': 'str',
        'payable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'payee_id': 'payeeId',
        'payment_channel_name': 'paymentChannelName',
        'account_name': 'accountName',
        'channel_type': 'channelType',
        'country_code': 'countryCode',
        'routing_number': 'routingNumber',
        'account_number': 'accountNumber',
        'iban': 'iban',
        'currency': 'currency',
        'payor_ids': 'payorIds',
        'payee_name': 'payeeName',
        'bank_name': 'bankName',
        'bank_swift_bic': 'bankSwiftBic',
        'bank_address': 'bankAddress',
        'deleted': 'deleted',
        'enabled': 'enabled',
        'disabled_reason_code': 'disabledReasonCode',
        'disabled_reason': 'disabledReason',
        'payable': 'payable'
    }

    def __init__(self, id=None, payee_id=None, payment_channel_name=None, account_name=None, channel_type=None, country_code=None, routing_number=None, account_number=None, iban=None, currency=None, payor_ids=None, payee_name=None, bank_name=None, bank_swift_bic=None, bank_address=None, deleted=None, enabled=None, disabled_reason_code=None, disabled_reason=None, payable=None):  # noqa: E501
        """PaymentChannelResponseV4 - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._payee_id = None
        self._payment_channel_name = None
        self._account_name = None
        self._channel_type = None
        self._country_code = None
        self._routing_number = None
        self._account_number = None
        self._iban = None
        self._currency = None
        self._payor_ids = None
        self._payee_name = None
        self._bank_name = None
        self._bank_swift_bic = None
        self._bank_address = None
        self._deleted = None
        self._enabled = None
        self._disabled_reason_code = None
        self._disabled_reason = None
        self._payable = None
        self.discriminator = None

        self.id = id
        if payee_id is not None:
            self.payee_id = payee_id
        self.payment_channel_name = payment_channel_name
        self.account_name = account_name
        self.channel_type = channel_type
        self.country_code = country_code
        if routing_number is not None:
            self.routing_number = routing_number
        if account_number is not None:
            self.account_number = account_number
        if iban is not None:
            self.iban = iban
        self.currency = currency
        if payor_ids is not None:
            self.payor_ids = payor_ids
        if payee_name is not None:
            self.payee_name = payee_name
        if bank_name is not None:
            self.bank_name = bank_name
        if bank_swift_bic is not None:
            self.bank_swift_bic = bank_swift_bic
        if bank_address is not None:
            self.bank_address = bank_address
        if deleted is not None:
            self.deleted = deleted
        if enabled is not None:
            self.enabled = enabled
        if disabled_reason_code is not None:
            self.disabled_reason_code = disabled_reason_code
        if disabled_reason is not None:
            self.disabled_reason = disabled_reason
        if payable is not None:
            self.payable = payable

    @property
    def id(self):
        """Gets the id of this PaymentChannelResponseV4.  # noqa: E501


        :return: The id of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentChannelResponseV4.


        :param id: The id of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def payee_id(self):
        """Gets the payee_id of this PaymentChannelResponseV4.  # noqa: E501


        :return: The payee_id of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this PaymentChannelResponseV4.


        :param payee_id: The payee_id of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """

        self._payee_id = payee_id

    @property
    def payment_channel_name(self):
        """Gets the payment_channel_name of this PaymentChannelResponseV4.  # noqa: E501


        :return: The payment_channel_name of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_name

    @payment_channel_name.setter
    def payment_channel_name(self, payment_channel_name):
        """Sets the payment_channel_name of this PaymentChannelResponseV4.


        :param payment_channel_name: The payment_channel_name of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if payment_channel_name is None:
            raise ValueError("Invalid value for `payment_channel_name`, must not be `None`")  # noqa: E501

        self._payment_channel_name = payment_channel_name

    @property
    def account_name(self):
        """Gets the account_name of this PaymentChannelResponseV4.  # noqa: E501


        :return: The account_name of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this PaymentChannelResponseV4.


        :param account_name: The account_name of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def channel_type(self):
        """Gets the channel_type of this PaymentChannelResponseV4.  # noqa: E501

        Payment channel type. One of the following values: CHANNEL_BANK  # noqa: E501

        :return: The channel_type of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this PaymentChannelResponseV4.

        Payment channel type. One of the following values: CHANNEL_BANK  # noqa: E501

        :param channel_type: The channel_type of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if channel_type is None:
            raise ValueError("Invalid value for `channel_type`, must not be `None`")  # noqa: E501

        self._channel_type = channel_type

    @property
    def country_code(self):
        """Gets the country_code of this PaymentChannelResponseV4.  # noqa: E501

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The country_code of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PaymentChannelResponseV4.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param country_code: The country_code of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")  # noqa: E501
        if country_code is not None and len(country_code) < 2:
            raise ValueError("Invalid value for `country_code`, length must be greater than or equal to `2`")  # noqa: E501
        if country_code is not None and not re.search(r'^[A-Z]{2}$', country_code):  # noqa: E501
            raise ValueError(r"Invalid value for `country_code`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._country_code = country_code

    @property
    def routing_number(self):
        """Gets the routing_number of this PaymentChannelResponseV4.  # noqa: E501


        :return: The routing_number of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """Sets the routing_number of this PaymentChannelResponseV4.


        :param routing_number: The routing_number of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if routing_number is not None and len(routing_number) > 9:
            raise ValueError("Invalid value for `routing_number`, length must be less than or equal to `9`")  # noqa: E501
        if routing_number is not None and len(routing_number) < 9:
            raise ValueError("Invalid value for `routing_number`, length must be greater than or equal to `9`")  # noqa: E501

        self._routing_number = routing_number

    @property
    def account_number(self):
        """Gets the account_number of this PaymentChannelResponseV4.  # noqa: E501


        :return: The account_number of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this PaymentChannelResponseV4.


        :param account_number: The account_number of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if account_number is not None and len(account_number) > 17:
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `17`")  # noqa: E501
        if account_number is not None and len(account_number) < 6:
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `6`")  # noqa: E501

        self._account_number = account_number

    @property
    def iban(self):
        """Gets the iban of this PaymentChannelResponseV4.  # noqa: E501

        Must match the regular expression ```^[A-Za-z0-9]+$```.  # noqa: E501

        :return: The iban of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this PaymentChannelResponseV4.

        Must match the regular expression ```^[A-Za-z0-9]+$```.  # noqa: E501

        :param iban: The iban of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if iban is not None and len(iban) > 34:
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `34`")  # noqa: E501
        if iban is not None and len(iban) < 15:
            raise ValueError("Invalid value for `iban`, length must be greater than or equal to `15`")  # noqa: E501
        if iban is not None and not re.search(r'^[A-Za-z0-9]+$', iban):  # noqa: E501
            raise ValueError(r"Invalid value for `iban`, must be a follow pattern or equal to `/^[A-Za-z0-9]+$/`")  # noqa: E501

        self._iban = iban

    @property
    def currency(self):
        """Gets the currency of this PaymentChannelResponseV4.  # noqa: E501

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The currency of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentChannelResponseV4.

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param currency: The currency of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501
        if currency is not None and len(currency) < 3:
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")  # noqa: E501
        if currency is not None and not re.search(r'^[A-Z]{3}$', currency):  # noqa: E501
            raise ValueError(r"Invalid value for `currency`, must be a follow pattern or equal to `/^[A-Z]{3}$/`")  # noqa: E501

        self._currency = currency

    @property
    def payor_ids(self):
        """Gets the payor_ids of this PaymentChannelResponseV4.  # noqa: E501


        :return: The payor_ids of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: list[str]
        """
        return self._payor_ids

    @payor_ids.setter
    def payor_ids(self, payor_ids):
        """Sets the payor_ids of this PaymentChannelResponseV4.


        :param payor_ids: The payor_ids of this PaymentChannelResponseV4.  # noqa: E501
        :type: list[str]
        """

        self._payor_ids = payor_ids

    @property
    def payee_name(self):
        """Gets the payee_name of this PaymentChannelResponseV4.  # noqa: E501


        :return: The payee_name of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this PaymentChannelResponseV4.


        :param payee_name: The payee_name of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """

        self._payee_name = payee_name

    @property
    def bank_name(self):
        """Gets the bank_name of this PaymentChannelResponseV4.  # noqa: E501


        :return: The bank_name of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this PaymentChannelResponseV4.


        :param bank_name: The bank_name of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def bank_swift_bic(self):
        """Gets the bank_swift_bic of this PaymentChannelResponseV4.  # noqa: E501


        :return: The bank_swift_bic of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._bank_swift_bic

    @bank_swift_bic.setter
    def bank_swift_bic(self, bank_swift_bic):
        """Sets the bank_swift_bic of this PaymentChannelResponseV4.


        :param bank_swift_bic: The bank_swift_bic of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """

        self._bank_swift_bic = bank_swift_bic

    @property
    def bank_address(self):
        """Gets the bank_address of this PaymentChannelResponseV4.  # noqa: E501


        :return: The bank_address of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: AddressV4
        """
        return self._bank_address

    @bank_address.setter
    def bank_address(self, bank_address):
        """Sets the bank_address of this PaymentChannelResponseV4.


        :param bank_address: The bank_address of this PaymentChannelResponseV4.  # noqa: E501
        :type: AddressV4
        """

        self._bank_address = bank_address

    @property
    def deleted(self):
        """Gets the deleted of this PaymentChannelResponseV4.  # noqa: E501


        :return: The deleted of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this PaymentChannelResponseV4.


        :param deleted: The deleted of this PaymentChannelResponseV4.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def enabled(self):
        """Gets the enabled of this PaymentChannelResponseV4.  # noqa: E501


        :return: The enabled of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PaymentChannelResponseV4.


        :param enabled: The enabled of this PaymentChannelResponseV4.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def disabled_reason_code(self):
        """Gets the disabled_reason_code of this PaymentChannelResponseV4.  # noqa: E501


        :return: The disabled_reason_code of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._disabled_reason_code

    @disabled_reason_code.setter
    def disabled_reason_code(self, disabled_reason_code):
        """Sets the disabled_reason_code of this PaymentChannelResponseV4.


        :param disabled_reason_code: The disabled_reason_code of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """

        self._disabled_reason_code = disabled_reason_code

    @property
    def disabled_reason(self):
        """Gets the disabled_reason of this PaymentChannelResponseV4.  # noqa: E501


        :return: The disabled_reason of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._disabled_reason

    @disabled_reason.setter
    def disabled_reason(self, disabled_reason):
        """Sets the disabled_reason of this PaymentChannelResponseV4.


        :param disabled_reason: The disabled_reason of this PaymentChannelResponseV4.  # noqa: E501
        :type: str
        """

        self._disabled_reason = disabled_reason

    @property
    def payable(self):
        """Gets the payable of this PaymentChannelResponseV4.  # noqa: E501

        Whether this payment channel is payable  # noqa: E501

        :return: The payable of this PaymentChannelResponseV4.  # noqa: E501
        :rtype: bool
        """
        return self._payable

    @payable.setter
    def payable(self, payable):
        """Sets the payable of this PaymentChannelResponseV4.

        Whether this payment channel is payable  # noqa: E501

        :param payable: The payable of this PaymentChannelResponseV4.  # noqa: E501
        :type: bool
        """

        self._payable = payable

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentChannelResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
