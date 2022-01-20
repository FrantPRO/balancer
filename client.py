import time
import asyncio

import httpx


def httpx_request(url, request_qty):
    async def main():
        async with httpx.AsyncClient() as client:
            for indx in range(request_qty):
                res = await client.get(url)
                print(indx + 1, res.headers['location'])

    asyncio.run(main())


if __name__ == '__main__':
    request_qty = 10000
    url = 'http://localhost:8000/?video=http://s1.localhost:8888/video/1488/xcg2djHckad.m3u8'
    start_time = time.time()
    httpx_request(url, request_qty)
    print('duration:', round(time.time() - start_time, 2), 'sec')
