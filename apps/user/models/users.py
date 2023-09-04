from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel


class UserManager(BaseUserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, password, **extra_fields)

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser, BaseModel):
    phone_number = PhoneNumberField(
        verbose_name=_("Phone number"),
        max_length=16,
        unique=True,
    )

    username = models.CharField(verbose_name=_("username"), max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return str(self.phone_number)

    def save(self, *args, **kwargs):
        if self.phone_number:
            user = User.objects.filter(phone_number=self.phone_number).first()
            if user and user.id != self.id:
                raise ValidationError(_("User with this phone number already exists."))
        super().save(*args, **kwargs)


class Profile(BaseModel):
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="profile/pictures", null=True, blank=True)
    region = models.ForeignKey(
        "user.Region",
        related_name="profile",
        on_delete=models.CASCADE,
        verbose_name=_("Region"),
    )
    address = models.CharField(verbose_name=_("Address"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username


class Region(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.name


class District(BaseModel):
    region = models.ForeignKey(
        "user.Region",
        related_name="district",
        on_delete=models.CASCADE,
        verbose_name=_("Region"),
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")

    def __str__(self):
        return self.name
