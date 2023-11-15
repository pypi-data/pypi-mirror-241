import httpx
import json


def json_dump(data):
    return json.dumps(data, ensure_ascii=False)


async def get(
    url, params=None, headers=None, proxies=None, timeout=None
) -> httpx.Response:
    return await request(
        "GET", url, params=params, headers=headers, proxies=proxies, timeout=timeout
    )


async def post(
    url,
    params=None,
    headers=None,
    data=None,
    json=None,
    files=None,
    proxies=None,
    timeout=None,
) -> httpx.Response:
    return await request(
        "POST",
        url,
        params=params,
        headers=headers,
        data=data,
        json=json,
        files=files,
        proxies=proxies,
        timeout=timeout,
    )


async def patch(
    url,
    params=None,
    headers=None,
    data=None,
    json=None,
    files=None,
    proxies=None,
    timeout=None,
) -> httpx.Response:
    return await request(
        "PATCH",
        url,
        params=params,
        headers=headers,
        data=data,
        json=json,
        files=files,
        proxies=proxies,
        timeout=timeout,
    )


async def put(
    url,
    params=None,
    headers=None,
    data=None,
    json=None,
    files=None,
    proxies=None,
    timeout=None,
) -> httpx.Response:
    return await request(
        "PUT",
        url,
        params=params,
        headers=headers,
        data=data,
        json=json,
        files=files,
        proxies=proxies,
        timeout=timeout,
    )


async def delete(
    url,
    params=None,
    headers=None,
    data=None,
    json=None,
    files=None,
    proxies=None,
    timeout=None,
) -> httpx.Response:
    return await request(
        "DELETE",
        url,
        params=params,
        headers=headers,
        data=data,
        json=json,
        files=files,
        proxies=proxies,
        timeout=timeout,
    )


async def request(
    method,
    url,
    params=None,
    headers=None,
    data=None,
    json=None,
    files=None,
    proxies=None,
    timeout=None,
) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        return await client.request(
            method,
            url,
            params=params,
            headers=headers,
            data=data,
            json=json,
            files=files,
            timeout=timeout,
        )
