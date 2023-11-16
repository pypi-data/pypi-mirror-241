from typing import Optional, TypeVar, Union

from lxmpay import settings
from lxmpay.core import AsyncPayCore
from lxmpay.lkl_pay import LakalaPay

from lxmpay.models import (
    CancelResult,
    LklPayConfig,
    PayConfig,
    PayCoreType,
    PayMethod,
    PayResult,
    PayType,
)

CongigType = TypeVar("CongigType", bound=PayConfig)


class AsyncPayClient(AsyncPayCore):
    def __init__(self, config: CongigType, **kwargs):
        self.config = config
        self.pay_core = self.create_core(config, **kwargs)
        self.settings = settings.Setting()

    def create_core(self, config: CongigType, **kwargs) -> AsyncPayCore:
        if config.pay_core_type == PayCoreType.LKL:
            assert isinstance(config, LklPayConfig)
            return LakalaPay(config, **kwargs)
        raise ValueError("未知的支付类型")

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
        return await self.pay_core.pay(
            out_trade_no,
            total_amount,
            open_id,
            description,
            pay_type,
            pay_method,
            notify_url=notify_url,
            reqip=reqip,
            attach=attach,
            **kwargs
        )

    async def refund(
        self,
        refund_trace_no: str,
        refund_fee: int,
        out_trade_no: str,
        trade_no: Union[str, None] = None,
        **kwargs
    ) -> CancelResult:
        return await self.pay_core.refund(
            refund_trace_no, refund_fee, out_trade_no, trade_no=trade_no, **kwargs
        )


if __name__ == "__main__":
    import asyncio
    from lxmpay import Env

    async def main():
        client = AsyncPayClient(
            LklPayConfig(
                channel_id="85",
                username="api_pay_open_public_test",
                password="api_pay_open_public_test@2023",
                endpoint="http://wyjsdev1.smartac.co/pay",  # type:ignore
            )
        )
        import time

        out_trade_no = str(time.time())
        with client.settings(raw_response=True):
            ret = await client.pay(
                out_trade_no,
                100,
                "oRuBz6zFsIEQ750IqcllZPXXozDU",
                "test",
                PayType.Wechat,
                PayMethod.MINIPROG,
            )
            print(ret, type(ret))

        ret = await client.refund(str(time.time()), 1, out_trade_no)
        print(ret, type(ret))

    asyncio.run(main())
