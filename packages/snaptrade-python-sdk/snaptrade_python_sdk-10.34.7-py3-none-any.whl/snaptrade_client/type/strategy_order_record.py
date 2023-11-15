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

from snaptrade_client.type.currency import Currency
from snaptrade_client.type.exchange import Exchange
from snaptrade_client.type.option_strategy import OptionStrategy
from snaptrade_client.type.option_strategy_legs import OptionStrategyLegs
from snaptrade_client.type.order_type import OrderType
from snaptrade_client.type.price import Price
from snaptrade_client.type.security_type import SecurityType
from snaptrade_client.type.time_in_force import TimeInForce
from snaptrade_client.type.universal_symbol import UniversalSymbol

class RequiredStrategyOrderRecord(TypedDict):
    pass

class OptionalStrategyOrderRecord(TypedDict, total=False):
    strategy: OptionStrategy

    status: str

    filled_quantity: typing.Union[int, float]

    open_quantity: typing.Union[int, float]

    closed_quantity: typing.Union[int, float]

    order_type: OrderType

    time_in_force: TimeInForce

    limit_price: Price

    execution_price: Price

    # Time
    time_placed: str

    # Time
    time_updated: str

class StrategyOrderRecord(RequiredStrategyOrderRecord, OptionalStrategyOrderRecord):
    pass
