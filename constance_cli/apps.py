from django import VERSION
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured


class ConstanceCliConfig(AppConfig):
    name = 'constance_cli'
    verbose_name = _('Constance CLI')

    def ready(self):
        if VERSION < (1, 8):
            # since we assume use of argparse
            raise ImproperlyConfigured(self.verbose_name + _(" requires Django 1.8 or later"))
