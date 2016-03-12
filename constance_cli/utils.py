# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from constance import config, settings
from constance.admin import ConstanceForm


def get_constance_values():
    # copied from constance.admin
    default_initial = ((name, default)
        for name, (default, help_text) in settings.CONFIG.items())
    # Then update the mapping with actually values from the backend
    initial = dict(default_initial,
        **dict(config._backend.mget(settings.CONFIG.keys())))

    return initial


def get_constance_value(raw_name):
    return getattr(config, raw_name)


def get_constance_field(name):
    form = ConstanceForm(initial=get_constance_values())

    return form.fields[name]


def set_constance_value(raw_name, raw_value):
    """
    Parses and sets a Constance value
    :param raw_name:
    :param raw_value:
    :return:
    """
    field = get_constance_field(raw_name)

    value = field.clean(field.to_python(raw_value))
    setattr(config, raw_name, value)