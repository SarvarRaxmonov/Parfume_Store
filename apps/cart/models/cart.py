from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel
from apps.user.models import User


class Region(BaseModel):
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class District(BaseModel):
    region = models.ForeignKey(
        Region,
        related_name="district_region",
        on_delete=models.CASCADE,
        verbose_name=_("Region"),
    )
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"


class Accreditation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    region = models.ForeignKey(
        Region,
        related_name="region",
        on_delete=models.CASCADE,
        verbose_name=_("Region"),
    )
    district = models.ForeignKey(
        District,
        related_name="district",
        on_delete=models.CASCADE,
        verbose_name=_("District"),
    )
    full_name = models.CharField(max_length=125, verbose_name=_("Full Name"))
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    location = models.CharField(max_length=125, verbose_name=_("Location"))
    total_price = models.IntegerField(verbose_name=_("Total Price"))
    discount_price = models.IntegerField(verbose_name=_("Discount Price"))
    used_cashback = models.IntegerField(verbose_name=_("Used Cashback"))
    NDS = models.IntegerField(verbose_name=_("NDS"))
    cashback = models.IntegerField(verbose_name=_("Cashback"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Accreditation"
        verbose_name_plural = "Accreditations"


class BankCard(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    accreditation = models.ForeignKey(Accreditation, on_delete=models.CASCADE, verbose_name=_("Accreditation"))
    number = models.IntegerField(verbose_name=_("Number"))


class UserPhone(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    accreditation = models.ForeignKey(Accreditation, on_delete=models.CASCADE, verbose_name=_("Accreditation"))
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"))

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "User Phone"
        verbose_name_plural = "User Phones"


class PaymentMethod(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Phone Number"))
    accreditation = models.ForeignKey(Accreditation, on_delete=models.CASCADE, verbose_name=_("Accreditation"))
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "PaymentMethod"
        verbose_name_plural = "PaymentMethods"


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    title = models.CharField(max_length=125, verbose_name=_("Title"))
    image = models.ImageField(upload_to="cart_images/", verbose_name=_("Image"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    count = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name=_("Count"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
