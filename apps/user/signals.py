from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.user.models import Profile, User

# from apps.user.models.notifications import Notification, ReadNotification


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_delete, sender=Profile)
def delete_user_when_deleted_profile(sender, instance, **kwargs):
    instance.user.delete()


#
# @receiver(post_save, sender=Notification)
# def create_read_notifications(sender, instance, created, **kwargs):
#     if created and instance.to_all:
#         non_staff_user = User.objects.filter(is_staff=False)
#
#         for user in non_staff_user:
#             ReadNotification.objects.create(user=user, notification=instance, is_read=False)
