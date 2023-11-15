from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel, HttpUrl


class Env(Enum):
    SANDBOX = 0
    PRODUCTION = 1


class PayCoreType(Enum):
    LKL = 0


class PayType(Enum):
    Wechat = 1
    Alipay = 2


class PayMethod(Enum):
    MINIPROG = 1


class PayConfig(BaseModel):
    timeout: Optional[int] = 30
    pay_core_type: PayCoreType


class LklPayConfig(PayConfig):
    pay_core_type: PayCoreType = PayCoreType.LKL
    endpoint: HttpUrl
    channel_id: str
    username: str
    password: str
    token_expires: int = 20 * 3600


class BaseResponse(BaseModel):
    code: int
    msg: str


class PayResult(BaseResponse):
    trade_no: Optional[str] = None
    attach: Optional[str] = None
    prepay_data: Optional[Dict] = None


class CancelResult(BaseResponse):
    refund_fee: Optional[int] = None
    out_trade_no: Optional[str] = None
    trade_no: Optional[str] = None
