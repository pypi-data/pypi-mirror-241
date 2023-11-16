from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel, Field, HttpUrl


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
    trade_no: Optional[str] = Field(..., title="支付平台支付订单号")
    attach: Optional[str] = Field(default="", title="附加数据")
    prepay_data: Optional[Dict] = Field(..., title="微信小程序支付唤起参数")


class CancelResult(BaseResponse):
    out_trade_no: str = Field(..., title="原商户支付订单号")
    order_status: int = Field(..., title="订单状态", description="-2退款成功, -3退款失败")
    refund_fee: Optional[int] = Field(..., title="退款金额")
    trade_no: Optional[str] = Field(..., title="支付平台退款订单号")
