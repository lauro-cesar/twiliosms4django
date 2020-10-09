from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    dateCreated = models.DateTimeField(
        auto_now=True, verbose_name=_("Data  de registro")
    )
    lastModified = models.DateTimeField(auto_now=True, verbose_name=_("Último login"))


    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")

    def __str__(self):
        return self.username
