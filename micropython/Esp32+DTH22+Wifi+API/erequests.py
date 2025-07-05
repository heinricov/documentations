import usocket
import ujson

class Response:
    def __init__(self, sock):
        self.raw = sock
        self.encoding = "utf-8"
        self._cached = None

    def close(self):
        if self.raw:
            self.raw.close()
            self.raw = None

    @property
    def content(self):
        if self._cached is None:
            self._cached = self.raw.read()
            self.raw.close()
            self.raw = None
        return self._cached

    @property
    def text(self):
        return str(self.content, self.encoding)

    def json(self):
        return ujson.loads(self.content)

def request(method, url, data=None, json=None, headers={}, stream=None):
    try:
        proto, dummy, host, path = url.split("/", 3)
    except ValueError:
        proto, dummy, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
    elif proto == "https:":
        import ussl
        port = 443
    else:
        raise ValueError("Unsupported protocol: " + proto)

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)

    ai = usocket.getaddrinfo(host, port)
    addr = ai[0][-1]
    s = usocket.socket()
    s.connect(addr)

    if proto == "https:":
        import ussl
        s = ussl.wrap_socket(s, server_hostname=host)

    s.write("%s /%s HTTP/1.0\r\n" % (method, path))
    s.write("Host: %s\r\n" % host)
    for k in headers:
        s.write("%s: %s\r\n" % (k, headers[k]))
    if json is not None:
        import ujson
        data = ujson.dumps(json)
        s.write("Content-Type: application/json\r\n")
    if data:
        s.write("Content-Length: %d\r\n" % len(data))
    s.write("\r\n")
    if data:
        s.write(data)

    l = s.readline()
    protover, status, msg = l.split(None, 2)
    status = int(status)
    while True:
        l = s.readline()
        if not l or l == b"\r\n":
            break

    resp = Response(s)
    resp.status_code = status
    return resp

def get(url, **kw):
    return request("GET", url, **kw)

def post(url, **kw):
    return request("POST", url, **kw)