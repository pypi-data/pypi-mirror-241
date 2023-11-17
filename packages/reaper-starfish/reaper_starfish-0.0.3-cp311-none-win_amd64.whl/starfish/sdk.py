from typing import Optional
from .starfish import *

Backtest = RunMode.Backtest
Sandbox = RunMode.Sandbox
Real = RunMode.Real

Binance = Platform.Binance
Okx = Platform.Okx

Spot = Kind.Spot
Contract = Kind.Contract

Market = Type.Market
Limit = Type.Limit

Long = Side.Long
Short = Side.Short

OrderInitialize = OrderStatus.Initialize
OrderLive = OrderStatus.Live
OrderRejected = OrderStatus.Rejected
OrderFilled = OrderStatus.Filled
OrderCancled = OrderStatus.Cancled


def limit_buy(
    platform: Platform,
    kind: Kind,
    symbol: str,
    volume: float,
    price: float,
    side: Side = Long,
    id: Optional[str] = None,
):
    """
    限价买入
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [volume] : 数量
    * [price] : 价格
    * [side] : 交易方向
    * [id] : 订单ID
    """
    place_order(
        platform=platform,
        kind=kind,
        symbol=symbol,
        type=Limit,
        side=side,
        reduce=False,
        volume=volume,
        price=price,
        id=id,
    )


def limit_sell(
    platform: Platform,
    kind: Kind,
    symbol: str,
    volume: float,
    price: float,
    side: Side = Long,
    id: Optional[str] = None,
):
    """
    限价卖出
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [volume] : 数量
    * [price] : 价格
    * [side] : 交易方向
    * [id] : 订单ID
    """
    place_order(
        platform=platform,
        kind=kind,
        symbol=symbol,
        type=Limit,
        side=side,
        reduce=True,
        volume=volume,
        price=price,
        id=id,
    )


def market_buy(
    platform: Platform,
    kind: Kind,
    symbol: str,
    volume: float,
    side: Side = Long,
    id: Optional[str] = None,
):
    """
    市价买入
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [volume] : 数量
    * [side] : 交易方向
    * [id] : 订单ID
    """
    place_order(
        platform=platform,
        kind=kind,
        symbol=symbol,
        type=Market,
        side=side,
        reduce=False,
        volume=volume,
        price=None,
        id=id,
    )


def market_sell(
    platform: Platform,
    kind: Kind,
    symbol: str,
    volume: float,
    side: Side = Long,
    id: Optional[str] = None,
):
    """
    市价卖出
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [volume] : 数量
    * [side] : 交易方向
    * [id] : 订单ID
    """
    place_order(
        platform=platform,
        kind=kind,
        symbol=symbol,
        type=Limit,
        side=side,
        reduce=True,
        volume=volume,
        price=None,
        id=id,
    )
