# balancer
##Request Balancer

For start service run _**docker-compose up**_

All services will run on localhost (0.0.0.0)
The balancer will run on port 8000.
The CDN server will run on port 9999.
The origin server will run on port 8888

You can use **client.py** for runs pulling requests to the balancer, 
or you can send requests yourself to the endpoint http://localhost:8000.

The **client.py** based on the httpx library for async request.

Expected request of type `http://localhost:8000/?video=http://s1.localhost:8888/video/1488/xcg2djHckad.m3u8`
