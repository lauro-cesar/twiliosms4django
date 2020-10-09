from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from .base import BaseModel


class TwilioSettings(BaseModel):
    """"""

    accountSID = models.CharField(
        max_length=256, default=_("TwilioaccountSID"), verbose_name=_("account SID")
    )

    accountToken = models.CharField(
        max_length=256, default=_("accountToken"), verbose_name=_("account Token")
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Twilio Setting")
        verbose_name_plural = _("Twilio Settings")
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.accountSID
