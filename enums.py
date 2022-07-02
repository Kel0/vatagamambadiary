from enum import Enum


class VatagaURL(Enum):
    LOGIN: str = "https://api.vataga.trade/v1/tokens/"
    TRADES_FOR_TODAY: str = "https://api.vataga.trade/v1/trading-accounts/{}/deals/?page_num=1&date=01-07-2022"
