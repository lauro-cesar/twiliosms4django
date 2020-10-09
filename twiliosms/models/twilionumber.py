from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from .base import BaseModel
from .sms import TwilioSMS


class TwilioNumber(BaseModel):
    """"""

    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Number Owner"),
    )

    twilioSettings = models.ForeignKey(
        "twiliosms.TwilioSettings",
        on_delete=models.CASCADE,
        verbose_name=_("Twilio Settings"),
    )

    number = models.CharField(
        max_length=32, default=_("twilionumer"), verbose_name=_("Twilio number")
    )

    def sendSms(self):
        pass

    class Meta(BaseModel.Meta):
        verbose_name = _("Twilio number")
        verbose_name_plural = _("Twillio Numbers")
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.number
