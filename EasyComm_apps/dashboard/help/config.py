from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HelpConfig(AppConfig):
    label = 'help_dashboard'
    name = 'EasyComm_apps.dashboard.help'
    verbose_name = _('Help dashboard')
