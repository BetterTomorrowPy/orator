# -*- coding: utf-8 -*-
"""
    Orator`s manage.
"""

from tornado.ioloop import IOLoop
from tornado.options import define, options

from apis import make_app
from apis import local_settings
from helpers import settings_from_object

define('port', 8000, int, 'Run on given port')
define('cmd', 'runserver', str, 'runserver')
define('debug', False, bool, 'Debug mode')


def main():
    """"""
    settings = settings_from_object(local_settings)
    if settings.get('debug', False):
        options.logging = 'debug'

    options.parse_command_line()

    if options.debug:
        settings['debug'] = True

    if 'runserver' == options.cmd:
        app = make_app(settings)
        kwargs = {
            'xheaders': True
        }
        app.listen(options.port, **kwargs)
        print('Run server on port {0}'.format(options.port))
        IOLoop.current().start()

if __name__ == '__main__':
    main()