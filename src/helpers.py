# -*- coding: utf-8 -*-
"""
    Orator top level helpers.
"""


def settings_from_object(obj):
    """"""

    settings = dict()

    for key in dir(obj):
        if key.isupper():
            settings[key.lower()] = getattr(obj, key)

    return settings
