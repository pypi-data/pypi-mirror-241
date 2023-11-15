import asyncio
import json
from hashlib import md5
from typing import Optional, Union

import httpx

from lxmpay import http, settings
from lxmpay.cache import MemoryCache
from lxmpay.core import AsyncPayCore
from lxmpay.errors import PayError
from lxmpay.models import CancelResult, LklPayConfig, PayMethod, PayResult, PayType

lock = asyncio.Lock()


class LakalaPay(AsyncPayCore):
    def __init__(self, config: LklPayConfig, **kwargs):
        self.config = config
        self.end_point = config.endpoint
        self.cache = kwargs.get("cache") or MemoryCache()
        self.settings = settings.Setting()

    async def login(self):
        url = f"{self.end_point}/v1/auth/token"
        data = {
            "username": self.config.username,
            "password": md5(self.config.password.encode()).hexdigest(),
        }
        resp = await http.post(url, json=data, timeout=self.config.timeout)
        resp.raise_for_status()
        resp = resp.json()
        if resp["code"] != 0:
            raise PayError(
                resp["code"], resp["msg"], request=resp.request, response=resp
            )
        return "Bearer " + resp["data"]["token"]

    async def save_token(self, token):
        await self.cache.set("token", token, self.config.token_expires)

    async def get_token(self):
        async with lock:
            token = await self.cache.get("token")
            if not token:
                token = await self.login()
                await self.cache.set("token", token, self.config.token_expires)
            return token

    def get_pay_way(self, pay_type: PayType):
        if pay_type == PayType.Wechat:
            return "2"
        elif pay_type == PayType.Alipay:
            return "1"
        raise ValueError("未知的pay_type")

    def get_sub_payway(self, pay_method: PayMethod):
        if pay_method == PayMethod.MINIPROG:
            return "4"
        raise ValueError("未知的pay_method")

    async def common_header(self):
        return {"Authorization": await self.get_token()}

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
        **kwargs,
    ) -> Union[PayResult, httpx.Response]:
        url = f"{self.end_point}/v1/pay/precreate"
        data = {
            "channel_id": self.config.channel_id,
            "client_sn": out_trade_no,
            "total_amount": total_amount,
            "payway": self.get_pay_way(pay_type),
            "sub_payway": self.get_sub_payway(pay_method),
            "open_id": open_id,
            "subject": description,
            "notify_url": notify_url,
            "client_ip": reqip,
        }
        headers = await self.common_header()
        response = await self._post(
            url, data, headers=headers, timeout=self.config.timeout
        )
        raw_response = self.settings.raw_response
        resp = self._handler_response(response, raw_response=raw_response)
        if isinstance(resp, httpx.Response):
            return resp
        return PayResult(
            code=0,
            msg="success",
            trade_no=resp["data"]["out_order_id"],
            prepay_data=json.loads(resp["data"]["wap_pay_request"]),
        )

    async def refund(
        self,
        refund_trace_no: str,
        refund_fee: int,
        out_trade_no: str,
        trade_no: Union[str, None] = None,
        **kwargs,
    ) -> Union[CancelResult, httpx.Response]:
        url = f"{self.end_point}/v1/pay/refund"
        data = {
            "channel_id": self.config.channel_id,
            "refund_request_no": refund_trace_no,
            "client_sn": out_trade_no,
            "refund_amount": str(refund_fee),
        }
        headers = await self.common_header()
        response = await self._post(
            url, data, headers=headers, timeout=self.config.timeout
        )

        raw_response = self.settings.raw_response
        resp = self._handler_response(response, raw_response=raw_response)
        if isinstance(resp, httpx.Response):
            return resp
        return CancelResult(
            code=0,
            msg="success",
            refund_fee=resp["data"]["refund_amount"],
            out_trade_no=resp["data"]["client_sn"],
            trade_no=resp["data"]["out_order_id"],
        )

    async def _post(self, url, data, headers=None, timeout=None):
        try:
            response = await http.post(url, json=data, headers=headers, timeout=timeout)
        except httpx.RequestError as e:
            raise PayError(e.__class__.__name__, str(e), request=e.request)
        except (httpx.StreamError, httpx.InvalidURL, httpx.CookieConflict) as e:
            raise PayError(e.__class__.__name__, str(e))
        return response

    def _handler_response(
        self, response: httpx.Response, *, raw_response=None
    ) -> Union[httpx.Response, dict]:
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise PayError(
                f"HTTPError:{response.status_code}", e.args[0], e.request, e.response
            )

        content = response.json()
        if content["code"] != 0:
            raise PayError(content["code"], content["msg"], response.request, response)
        if content["data"]["status"] != "SUCCESS":
            raise PayError(content["code"], content["msg"], response.request, response)

        return response if raw_response else content
