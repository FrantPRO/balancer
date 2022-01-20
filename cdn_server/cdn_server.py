from sanic import Sanic
from sanic.log import logger as log
from sanic.response import text
count = 0

app = Sanic("BalancerDomain")


@app.route("/<server>/<video:path>")
async def cdn_server(request, server, video):
    global count
    count += 1
    log.info(f'COUNT {count}')
    return text(f'You are getting file "{video}" from CDN server. Copy from "{server}" original server')


@app.route("/health")
async def health_check(request):
    return text("I'm alive - cdn_server")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=False, access_log=False, auto_reload=True)
