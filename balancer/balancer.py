from sanic import Sanic
from sanic.log import logger as log
from sanic.response import redirect, text
from urllib.parse import urlparse, urlsplit, urlunsplit
from sanic.exceptions import SanicException


app = Sanic("BalancerDomain")
app.config["CDN_HOST"] = "http://localhost:9999"
load_level = 10
count = 0
global_count = 0


@app.route('/')
async def main(request):

    # getting the query param 'video'
    target_url = request.args.get("video")
    if not target_url:
        log.error("Incorrect url", {"url": str(request.url)})
        raise SanicException("Incorrect url", status_code=400)

    # to be sure that the param is string
    target_url = target_url if isinstance(target_url, str) else target_url[0]

    # getting original server name and path to file
    url_params = urlparse(target_url)
    server_params = url_params.hostname.split(".")
    if not server_params:
        log.error("Incorrect origin server\'s name", {"url_params": url_params.hostname})
        raise SanicException("Incorrect origin server's name")
    server_num = server_params[0]
    location = url_params.path

    # log.info({"target_url": target_url, "server_num": server_num, "location": location})

    # creating link for CDN
    cdn_link = list(urlsplit(app.config.CDN_HOST))
    # attribute index 2 is the hierarchical path
    cdn_link[2] = f'{server_num}{location}'
    cdn_link = urlunsplit(cdn_link)

    if count < load_level:
        url = cdn_link
    else:
        # Removing third domain name for the local test
        url = target_url.replace(server_num + ".", "")

    log.info(f'COUNT {count} from {global_count} redirect to {url}')

    return redirect(url, status=301)


@app.middleware("request")
async def main(request):
    global count, global_count
    global_count += 1
    count = count + 1 if count < load_level else 1


@app.route("/health")
async def health_check(request):
    return text("I'm alive - balancer")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, access_log=False, auto_reload=True)
