from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.product.models import Section


@receiver(post_save, sender=Section)
def update_main_section(sender, instance, **kwargs):
    if instance.is_main:
        Section.objects.exclude(pk=instance.pk).update(is_main=False)
    return instance
