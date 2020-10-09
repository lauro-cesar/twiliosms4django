from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TwiliosmsConfig(AppConfig):
    name = "twiliosms"
    verbose_name = _("Twiliosms")

    def ready(self):
        import twiliosms.signals
