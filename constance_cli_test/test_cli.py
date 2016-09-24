# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 NZME
#


import sys
from contextlib import contextmanager

from django.core.management import call_command
from django.utils.six import StringIO

from .utils import DcCliUnitTest


@contextmanager
def redirect_stdout(new_target):
    """
    backport of contextlib.redirect_stdout from http://stackoverflow.com/a/22434262/8331
    :param new_target:
    :return:
    """

    old_target, sys.stdout = sys.stdout, new_target # replace sys.stdout
    try:
        yield new_target # run some code with the replaced stdout
    finally:
        sys.stdout = old_target # restore to the previous value


class CliTestCase(DcCliUnitTest):

    def test_help(self):
        out = StringIO()
        try:
            with redirect_stdout(out):
                call_command('constance_cli', '--help')
        except SystemExit:
            pass
