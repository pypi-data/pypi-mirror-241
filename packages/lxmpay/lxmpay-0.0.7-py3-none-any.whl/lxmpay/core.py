import abc
import logging
from typing import Dict, Optional, Union

from lxmpay.models import CancelResult, PayMethod, PayResult, PayType

logger = logging.getLogger("lxmpay")


class AsyncPayCore:
    @abc.abstractmethod
    async def pay(
        self,
        out_trade_no: str,
        total_amount: int,
        open_id: str,
        description: str,
        pay_type: PayType,
        pay_method: PayMethod,
        notify_url: Optional[str] = None,
        reqip: Optional[str] = None,
        attach: Optional[str] = None,
        **kwargs
    ) -> PayResult:
        """
        param out_trade_no: 商户订单号(在商户系统内唯一)
        param total_amount: 订单金额，单位为分
        param open_id: 用户标识（微信openid/支付宝userid）
        param description: 订单描述
        param pay_type: 支付类型
        param pay_method: 支付方式：JSAPI,小程序
        param notify_url: 回调地址（以http或https开头的完整url地址）
        """
        pass

    @abc.abstractmethod
    async def refund(
        self,
        refund_trace_no: str,
        refund_fee: int,
        out_trade_no: str,
        trade_no: Union[str, None] = None,
        **kwargs
    ) -> CancelResult:
        """
        params refund_trace_no:请求流水号（系统方退款订单号）
        params refund_fee:退款金额，单位：分
        params out_trade_no: 商户订单号(在商户系统内唯一)
        params trade_no: 支付请求流水号（与支付订单号二选其一必传）
        """
        pass
