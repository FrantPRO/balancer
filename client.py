import time
import asyncio

import httpx


def httpx_request(url, request_qty):
    async def main():
        async with httpx.AsyncClient() as client:
            for _ in range(request_qty):
                await client.get(url)

    start_time = time.time()
    asyncio.run(main())
    return time.time() - start_time


if __name__ == '__main__':
    request_qty = 500
    url = 'http://localhost:8000/?video=http://s1.localhost:8888/video/1488/xcg2djHckad.m3u8'
    print('httpx', httpx_request(url, request_qty))
