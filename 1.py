from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    if "test3019-test.hp.chargebeestaticv2.com/configuration/all" in flow.request.pretty_url:
        with open("res.json", "r") as f:
            new_body = f.read()
        flow.response.text = new_body
        flow.response.headers["Content-Type"] = "application/json"
