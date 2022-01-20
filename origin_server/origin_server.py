from sanic import Sanic
from sanic.log import logger as log
from sanic.response import text
count = 0

app = Sanic("BalancerDomain")


@app.route(r"/<video:path>")
async def origin_server(request, video):
    global count
    count += 1
    log.info(f'COUNT {count}')
    return text(f'You are getting file "{video}" from origin server.')


@app.route("/health")
async def health_check(request):
    return text("I'm alive - origin_server")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=False, access_log=False, auto_reload=True)
