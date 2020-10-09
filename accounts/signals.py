from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        pass
