from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"


class Accreditation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, related_name="region", on_delete=models.CASCADE)
    district = models.ForeignKey(District, related_name="district", on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accreditation = models.ForeignKey(Accreditation, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name=_("number"))


class UserPhone(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accreditation = models.ForeignKey(Accreditation, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)  # Adjust the max length as needed

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "UserPhone"
        verbose_name_plural = "UserPhones"


class PaymentMethod(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accreditation = models.ForeignKey(Accreditation, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "PaymentMethod"
        verbose_name_plural = "PaymentMethods"


class Cart(BaseModel):
    title = models.CharField(max_length=125, verbose_name=_("title"))
    image = models.ImageField(upload_to="cart_images/", verbose_name=_("image"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("price"))
    count = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name=_("count"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
