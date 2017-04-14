# -*- coding: utf-8 -*-
"""
    辅助工具集合
"""

import logging
import json
import functools

from voluptuous import MultipleInvalid


class ApiException(Exception):
    status_code = 400
    error_code = None
    message = ''
    log_message = ''

    def __init__(self, error_code, message, log_message=None,
                 status_code=None, payload=None):
        super(ApiException, self).__init__()

        self.message = message
        if status_code:
            self.status_code = status_code

        if error_code >= 400 and error_code <= 599:
            self.status_code = error_code

        self.error_code = error_code
        self.payload = payload
        self.log_message = log_message

    def to_dict(self):
        kv = dict(self.payload or ())
        kv['error'] = self.message
        kv['error_code'] = self.error_code or self.status_code
        return kv


def validate_arguments(schema=None):
    """
    装饰器，校验请求参数是否正确
    :param schema: voluptuous.Schema
    :return:
    """

    def func_wrapper(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            content_type = self.request.headers.get('Content-Type', '').strip()

            if content_type and content_type.startwith('application/json'):
                _arguments = json.loads(self.request.body.decode())
            else:
                _arguments = dict()
                for key in self.request.arguments.keys():
                    _arguments[key] = self.get_arguments(key)
            try:
                self._validated_arguments = schema(_arguments)
            except MultipleInvalid as e:
                error_message = 'path: {0} message: {1}'.format(e.path, e.error_message)
                logging.debug(error_message)
                raise ApiException(400, error_message, log_message=error_message)
            return method(self, *args, **kwargs)

        return wrapper

    return func_wrapper


def authenticated(method):
    """
    校验用户是否登录
    :param method:
    :return:
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user \
                or not self.current_user.is_authenticated():
            raise ApiException(403, 'Access denied')
        return method(self, *args, **kwargs)

    return wrapper
