# -*- coding: utf-8 -*-
""""""

from tornado.web import Application

from .demo import DemoHandler


def make_app(setings=None):
    """
    Create tornado.web.Application object.
    :return:
    """
    handlers = [
        (r'/', DemoHandler),
    ]
    return Application(handlers)
