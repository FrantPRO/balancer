import time
import asyncio

import httpx


def httpx_request(url, request_qty):
    async def main():
        async with httpx.AsyncClient() as client:
            for indx in range(1, request_qty + 1):
                res = await client.get(url)
                print(indx, res.headers['location'])

    asyncio.run(main())


if __name__ == '__main__':
    request_qty = 500
    url = 'http://localhost:8000/?video=http://s1.localhost:8888/video/1488/xcg2djHckad.m3u8'
    start_time = time.time()
    httpx_request(url, request_qty)
    print(time.time() - start_time)
