from enum import Enum
from datetime import datetime
from typing import List, Optional, Tuple

class RunMode(Enum):
    """运行模式"""

    Backtest = RunMode
    """回测"""
    Sandbox = RunMode
    """模拟盘"""
    Real = RunMode
    """实盘"""

class Platform(Enum):
    """平台"""

    Binance = Platform
    """币安"""
    Okx = Platform
    """欧易"""

class Kind(Enum):
    """交易品种"""

    Spot = Kind
    """币币"""
    Contract = Kind
    """合约"""

class Type(Enum):
    """交易类型"""

    Market = Type
    """市价"""
    Limit = Type
    """限价"""

class Side(Enum):
    """交易方向"""

    Long = Side
    """做多"""
    Short = Side
    """做空"""

class OrderStatus(Enum):
    """订单状态"""

    Initialize = OrderStatus
    """初始化"""
    Live = OrderStatus
    """挂单中"""
    Rejected = OrderStatus
    """订单被拒"""
    Filled = OrderStatus
    """完全成交"""
    Cancled = OrderStatus
    """撤单"""

class Order:
    """订单"""

    id: str
    """ID"""
    pid: str
    """平台ID"""
    platform: Platform
    """平台"""
    kind: Kind
    """交易品种"""
    symbol: str
    """标的"""
    type: Type
    """交易类型"""
    side: Side
    """交易方向"""
    reduce: bool
    """减仓"""
    risk: bool
    """风控单"""
    status: OrderStatus
    """状态"""
    time: datetime
    """下单时间"""
    volume: float
    """数量"""
    price: float
    """价格"""
    deal_base: float
    """基础币成交数量"""
    deal_quote: float
    """计价币成交数量"""
    deal_average_price: float
    """成交均价"""
    cost_base: float
    """基础币手续费"""
    cost_quote: float
    """计价币手续费"""

class FundingFee:
    """资金费"""

    id: str
    """ID"""
    platform: Platform
    """平台"""
    kind: Kind
    """交易品种"""
    symbol: str
    """标的"""
    time: datetime
    """时间"""
    fee: float
    """资金费"""

class BookLevel:
    """订单簿深度"""

    price: float
    """价格"""
    volume: float
    """数量"""

class Books:
    """订单簿"""

    buys: List[BookLevel]
    """买盘"""
    sells: List[BookLevel]
    """卖盘"""
    time: datetime
    """刷新时间"""

class KLine:
    """K线"""

    open: float
    """开盘价"""
    high: float
    """最高价"""
    low: float
    """最低价"""
    close: float
    """收盘价"""
    volume: float
    """成交量"""
    time: datetime
    """开盘时间"""
    finish: bool
    """是否已完结"""

class Pair:
    """交易对"""

    platform: Platform
    """平台"""
    kind: Kind
    """交易品种"""
    symbol: str
    """标的"""
    base: str
    """基础币"""
    quote: str
    """计价币"""
    settle: str
    """结算币"""
    contract_value: float
    """合约面值"""
    contract_multiplier: float
    """合约乘数"""
    online_time: datetime
    """上线时间"""
    offline_time: datetime
    """下线时间"""
    take_fee_rate: float
    """主动成交手续费率"""
    maker_fee_rate: float
    """被动成交手续费率"""
    min_lever: float
    """最小杠杆倍数"""
    max_lever: float
    """最大杠杆倍数"""
    tick_price: float
    """价格下单精度"""
    tick_base: float
    """基础币下单精度"""
    tick_quote: float
    """计价币下单精度"""
    min_base: float
    """最小下单基础币"""
    max_limit_base: float
    """限价单最大下单基础币"""
    max_market_base: float
    """市价单最大下单计价币"""
    min_quote: float
    """最小下单计价币"""
    max_limit_quote: float
    """限价单最大基础币"""
    max_market_quote: float
    """市价单最大计价币"""

class Capital:
    """资本"""

    total: float
    """总"""
    available: float
    """可用"""
    frozen: float
    """冻结"""
    average_price: float
    """均价"""

class Metrics:
    """指标"""

    total_equity: float
    """总权益"""
    frozen_margin: float
    """冻结保证金"""
    realized_gain_loss: float
    """已实现盈利"""
    unrealized_gain_loss: float
    """未实现盈亏"""
    strategy_return: float
    """策略收益"""
    strategy_annualized_return: float
    """策略年化收益"""
    benchmark_return: float
    """基准收益"""
    benchmark_annualized_return: float
    """基准年化收益"""
    alpha: float
    """阿尔法"""
    beta: float
    """贝塔"""
    max_drawdown: float
    """最大回撤"""

def debug(*args):
    """调试日志"""

def info(*args):
    """信息日志"""

def warn(*args):
    """警告日志"""

def error(*args):
    """错误日志"""

def init_mode(mode: RunMode):
    """初始化运行模式"""

def init_backtest(begin_time: str, end_time: str):
    """
    初始化回测时间区间
    ---
    * [begin_time] : 开始时间
    * [end_time] : 结束时间
    ---
    * 时间格式为 年月日时分秒. 例: 20230102030405, 202301020304, 2023010203, 20230102, 202301, 2023
    * 结束时间必须大于开始时间
    """

def init_benchmark(
    platform: Platform,
    kind: Kind,
    base: str,
    quote: str,
    settle: str,
):
    """
    初始化基准
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [base] : 基础币
    * [quote] : 计价币
    * [settle] : 结算币
    """

def init_strategy(
    name: str,
    code: str,
    params: dict = {},
    risk: bool = False,
):
    """
    初始化策略
    ---
    * [name] : 策略名称
    * [code] : 策略代码
    * [params] : 策略参数, 可在策略中通过全局变量`global G_PARAMS`获取
    * [risk] : 是否为风控策略
    """

def init_account(
    platform: Platform,
    spot_cash: float = 0,
    contract_cash: float = 0,
    apikey: str = "",
    secret: str = "",
    password: str = "",
):
    """
    初始化账户
    ---
    * [platform] : 平台
    ---
    回测配置
    * [spot_cash] : 现货资金
    * [contract_cash] : 合约资金
    ---
    `模拟盘`|`实盘`配置
    * [apikey] : 交易所apikey
    * [secret] : 交易所secret
    * [password] : 交易所password
    """

def init_pair(
    platform: Platform,
    kind: Kind,
    base: str,
    quote: str,
    settle: str,
    take_fee_rate: float = 0,
    maker_fee_rate: float = 0,
    contract_value: float = 1,
    contract_multiplier: float = 1,
    min_lever: float = 1,
    max_lever: float = 125,
    tick_price: float = 1e-8,
    tick_base: float = 1e-8,
    tick_quote: float = 1e-8,
    min_base: float = 1e-8,
    max_limit_base: float = 10**9,
    max_market_base: float = 10**9,
    min_quote: float = 1e-8,
    max_limit_quote: float = 10**9,
    max_market_quote: float = 10**9,
):
    """
    初始化交易对
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [base] : 基础币
    * [quote] : 计价币
    * [settle] : 结算币
    ---
    回测配置
    * [take_fee_rate] : 主动成交手续费率
    * [maker_fee_rate] : 被动成交手续费率
    * [contract_value] : 合约面值
    * [contract_multiplier] : 合约乘数
    * [min_lever] : 最小杠杆倍数
    * [max_lever] : 最大杠杆倍数
    * [tick_price] : 价格下单精度
    * [tick_base] : 基础币下单精度
    * [tick_quote] : 计价币下单精度
    * [min_base] : 最小下单基础币
    * [max_limit_base] : 限价单最大下单基础币
    * [max_market_base] : 市价单最大下单计价币
    * [min_quote] : 最小下单计价币
    * [max_limit_quote] : 限价单最大基础币
    * [max_market_quote] : 市价单最大计价币
    """

def set_lever(
    platform: Platform,
    kind: Kind,
    symbol: str,
    lever: float,
) -> Tuple[bool, Optional[str]]:
    """
    设置杠杆倍数
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [lever] : 杠杆倍数
    """

def get_lever(
    platform: Platform,
    kind: Kind,
    symbol: str,
) -> Optional[float]:
    """
    获取杠杆倍数
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    """

def get_pair(
    platform: Platform,
    kind: Kind,
    symbol: str,
) -> Optional[Pair]:
    """
    获取交易对
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    """

def get_positoin(
    platform: Platform,
    kind: Kind,
    symbol: str,
    side: Side = Side.Long,
) -> Optional[Capital]:
    """
    获取持仓
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [side] : 方向
    """

def get_cash(
    platform: Platform,
    kind: Kind,
) -> Optional[Capital]:
    """
    获取资金
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    """

def get_orders(
    platform: Platform,
    kind: Kind,
    symbol: str,
    id: Optional[str] = None,
    all: bool = False,
) -> List[Order]:
    """
    获取订单
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [id] : 订单ID
    * [all] : 全部订单 | 挂单
    """

def get_metrics(
    platform: Optional[Platform] = None,
    kind: Optional[Kind] = None,
    symbol: Optional[Kind] = None,
) -> Optional[Metrics]:
    """
    获取指标
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    ---
    按顺序匹配
    * 如果`platform`为`None`, 查询总指标
    * 如果`kind`为`None`, 查询账户指标
    * 如果都不为`None`,查询仓位指标
    """

def get_klines(
    platform: Platform,
    kind: Kind,
    symbol: str,
    begin: Optional[datetime] = None,
    end: Optional[datetime] = None,
    limit: int = 1000,
) -> List[KLine]:
    """
    获取K线
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [begin] : 开始时间
    * [end] : 结束时间
    * [limit] : 数量
    ---
    * 如果`开始时间`为空, 则从`结束时间`往左查询`limit`条
    * 如果`结束时间`为空, 则从`开始时间`往右查询`limit`条
    * 如果`开始时间`&`结束时间`都为空,则按当前时间往左查询`limit`条
    """

def get_order_book(
    platform: Platform,
    kind: Kind,
    symbol: str,
) -> Optional[Books]:
    """
    获取订单簿
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    """

def get_mark_price(
    platform: Platform,
    kind: Kind,
    symbol: str,
) -> Optional[float]:
    """
    获取标记价格
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    """

def get_index_price(
    platform: Platform,
    kind: Kind,
    symbol: str,
) -> Optional[float]:
    """
    获取指数价格
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    """

def get_market_price(
    platform: Platform,
    kind: Kind,
    symbol: str,
) -> Optional[float]:
    """
    获取市场价格
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    """

def place_order(
    platform: Platform,
    kind: Kind,
    symbol: str,
    type: Type,
    side: Side,
    reduce: bool,
    volume: float,
    price: Optional[float] = None,
    id: Optional[str] = None,
) -> Tuple[bool, Optional[str], Optional[str]]:
    """
    下单
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [type] : 交易类型
    * [side] : 交易方向
    * [reduce] : 减仓
    * [volume] : 数量
    * [price] : 价格
    * [id] : 订单ID
    """

def cancle_order(
    platform: Platform,
    kind: Kind,
    symbol: str,
    id: str,
):
    """
    撤单
    ---
    * [platform] : 平台
    * [kind] : 交易品种
    * [symbol] : 标的
    * [id] : 订单ID
    """
