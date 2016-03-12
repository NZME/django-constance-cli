# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from django.core.management import BaseCommand, CommandError
from django.utils.translation import ugettext_lazy as _
from constance import config, settings
from constance.admin import ConstanceForm


class Command(BaseCommand):

    help = _('Get/Set In-database config settings handled by Constance')

    def add_arguments(self, parser):
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--list", action="store_true",
                           help=_("List all Constance settings"))
        group.add_argument("--get", dest='setting', nargs=1)
        group.add_argument("--set", dest='setting', nargs=2, metavar=('SETTING', 'VALUE',))

    def _get_constance_values(self):
        # copied from constance.admin
        default_initial = ((name, default)
            for name, (default, help_text) in settings.CONFIG.items())
        # Then update the mapping with actually values from the backend
        initial = dict(default_initial,
            **dict(config._backend.mget(settings.CONFIG.keys())))

        return initial

    def _get_constance_field(self, name):
        form = ConstanceForm(initial=self._get_constance_values())

        return form.fields[name]

    def _set_constance_value(self, raw_name, raw_value):
        """
        Parses and sets a Constance value
        :param raw_name:
        :param raw_value:
        :return:
        """
        field = self._get_constance_field(raw_name)

        value = field.clean(field.to_python(raw_value))
        setattr(config, raw_name, value)

    def handle(self, *args, **options):
        if options.get('setting'):
            raw_name = options.get('setting')[0]

            if len(options.get('setting')) == 1:
                # get
                try:
                    print(getattr(config, raw_name))
                except AttributeError as e:
                    raise CommandError(raw_name + _(" is not defined in settings.CONSTANCE_CONFIG"))
            else:
                # set
                raw_value = options.get('setting')[1]

                try:
                    self._set_constance_value(raw_name, raw_value)
                except KeyError as e:
                    raise CommandError(raw_name + _(" is not defined in settings.CONSTANCE_CONFIG)"))

        elif options.get('list'):
            for k, v in self._get_constance_values().items():
                print(k, v, sep="\t")
