
from typing import Any, Dict, Optional
from urllib.parse import parse_qs
from anyserver.models.base import Serializable


class WebRequest(Serializable):
    url: str
    verb: str
    path: str
    head: Dict[str, str]
    body: Optional[Any]
    query: Dict[str, str]

    def __init__(self, url, verb, path, head={}, body=None, query={}):
        self.url = url
        self.verb = verb
        self.path = path
        self.head = head
        self.body = body
        self.query = self._query()

    def _query(self):
        query = {}
        parts = self.url.split('?')[1] if '?' in self.url else ''
        parsed = parse_qs(parts) if parts else {}
        for key in parsed:
            vals = parsed[key]
            vals = vals if len(vals) != 1 else vals[0]
            query[key] = vals
        return query

    def header(self, name: str, default=''):
        head = self.head or {}
        for key in filter(lambda k: k == name.lower(), head):
            return head[key]  # Key found
        return default  # Not found

    def input(self, name, default=None):
        inputs = self.body or {}
        for key in filter(lambda k: k == name, inputs):
            return self.body[key]  # Key found
        return default  # Not found

    def inputs(self, prefix="", strip_prefix=False):
        res = {}
        inputs = self.body or {}
        for key in filter(lambda k: k.startswith(prefix), inputs):
            if prefix and strip_prefix:
                subpath = key[len(prefix):]
                res[subpath] = inputs[key]
            else:
                res[key] = inputs[key]
        return res

