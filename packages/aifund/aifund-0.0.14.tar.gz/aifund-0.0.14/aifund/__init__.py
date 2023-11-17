"""
AIfund 是基于 Python 的基金量化工具
"""

name = "aifund"
__author__ = "tiano"


from aifund.data.fund_etf_em import (
    get_code,
    stock_realtime,
    realtime_data,
    web_data,
)