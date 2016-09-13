#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 NZME
#

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "constance_cli_test.settings")

if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    from constance_cli_test import settings

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
