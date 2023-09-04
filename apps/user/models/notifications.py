from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Notification(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    content = RichTextUploadingField(verbose_name=_("Content"))

    def __str__(self):
        return self.title


class ReadNotification(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, verbose_name=_("User"))
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, verbose_name=_("Notification"))

    class Meta:
        unique_together = ("user", "notification")

    def __str__(self):
        return f"{self.user}"
