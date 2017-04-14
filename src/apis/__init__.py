# -*- coding: utf-8 -*-
""""""

from tornado.web import Application

from .demo import DemoHandler
from extensions.routing import Route


def make_app(setings=None):
    """
    Create tornado.web.Application object.
    :return:
    """
    handlers = [] + Route.routes()
    return Application(handlers, debug=True)
