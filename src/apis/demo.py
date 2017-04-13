# -*- coding: utf-8 -*-
"""
    Test handler.
"""

from tornado.gen import coroutine
from tornado.web import RequestHandler


class DemoHandler(RequestHandler):
    """"""

    @coroutine
    def get(self, *args, **kwargs):
        return self.write({
            'code': 0,
            'msg': ''
        })
