from .client import Client
from .market import *
from typing import Optional

def get_markets(is_details: Optional[bool] = None) -> list[dict]:
    return Client().get_markets(is_details)

def get_candles_minutes(unit: int = 1, market: str = KRW_BTC, to: Optional[str] = None, count: Optional[int] = None) -> list[dict]:
    return Client().get_candles_minutes(unit, market, to, count)

def get_candles_days(market: str = KRW_BTC, to: Optional[str] = None, count: Optional[int] = None, converting_price_unit: Optional[str] = None) -> list[dict]:
    return Client().get_candles_days(market, to, count, converting_price_unit)

def get_candles_weeks(market: str = KRW_BTC, to: Optional[str] = None, count: Optional[int] = None) -> list[dict]:
    return Client().get_candles_weeks(market, to, count)

def get_candles_months(market: str = KRW_BTC, to: Optional[str] = None, count: Optional[int] = None) -> list[dict]:
    return Client().get_candles_months(market, to, count)

def get_trades(market: str = KRW_BTC, to: Optional[str] = None, count: Optional[int] = None, cursor: Optional[str] = None, days_ago: Optional[int] = None) -> list[dict]:
    return Client().get_trades(market, to, count, cursor, days_ago)

def get_tickers(markets: list[str] = [KRW_BTC]) -> list[dict]:
    return Client().get_tickers(markets)

def get_orderbooks(markets: list[str] = [KRW_BTC]) -> list[dict]:
    return Client().get_orderbooks(markets)
