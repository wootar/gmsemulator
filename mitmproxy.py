# Basic mitm script to redirect any GMS calls to our server
from mitmproxy import http, ctx

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host.endswith("android.clients.google.com") or flow.request.pretty_host.endswith("play.google.com"):
        a = bytes(flow.request.host,encoding="ascii")
        flow.request.host = '127.0.0.1'
        flow.request.scheme = 'http'
        flow.request.port = 8095
        ctx.log.info(" ---> Redirected GMS response to" + flow.request.url)
