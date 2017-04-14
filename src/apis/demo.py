# -*- coding: utf-8 -*-
"""
    Test handler.
"""

from tornado.gen import coroutine
from tornado.web import RequestHandler

from extensions.routing import route

api_router = route(prefix='/api/1')


@api_router.route(r'/index')
class DemoHandler(RequestHandler):
    """"""

    @coroutine
    def get(self, *args, **kwargs):
        return self.write({
            'code': 0,
            'msg': ''
        })
