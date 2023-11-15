# coding: utf-8

"""
    SnapTrade

    Connect brokerage accounts to your app for live positions and trading

    The version of the OpenAPI document: 1.0.0
    Contact: api@snaptrade.com
    Created by: https://snaptrade.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from snaptrade_client.type.brokerage import Brokerage
from snaptrade_client.type.brokerage_authorization import BrokerageAuthorization
from snaptrade_client.type.brokerage_authorization_meta import BrokerageAuthorizationMeta
from snaptrade_client.type.brokerage_exchanges import BrokerageExchanges
from snaptrade_client.type.brokerage_type import BrokerageType
from snaptrade_client.type.currency import Currency
from snaptrade_client.type.exchange import Exchange
from snaptrade_client.type.options_symbol import OptionsSymbol
from snaptrade_client.type.security_type import SecurityType
from snaptrade_client.type.underlying_symbol import UnderlyingSymbol
from snaptrade_client.type.universal_symbol import UniversalSymbol
from snaptrade_client.type.us_exchange import USExchange

class RequiredBrokerageSymbol(TypedDict):
    pass

class OptionalBrokerageSymbol(TypedDict, total=False):
    id: str

    symbol: UniversalSymbol

    brokerage_authorization: BrokerageAuthorization

    description: str

    allows_fractional_units: typing.Optional[bool]

    option_symbol: OptionsSymbol

class BrokerageSymbol(RequiredBrokerageSymbol, OptionalBrokerageSymbol):
    pass
