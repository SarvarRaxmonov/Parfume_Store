from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.cart.models.cart import Accreditation  # Assuming Accreditation model is in the same app
from apps.common.models import BaseModel
from apps.product.models import Product
from apps.user.models import User


class Liked(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="liked_product", on_delete=models.CASCADE)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Liked"
        verbose_name_plural = "Liked"


class Order(BaseModel):
    class OrderTextChoice(models.TextChoices):
        ACCEPTED = "accepted", "Accepted"
        DELIVERED = "delivered", "Delivered"
        DURING_DELIVERY = "during_delivery", "During Delivery"
        CANCELED = "canceled", "Canceled"

    type = models.CharField(max_length=15, choices=OrderTextChoice.choices, default=OrderTextChoice.DURING_DELIVERY)
    accreditation = models.ForeignKey(Accreditation, related_name="order_accreditation", on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    cashback = models.IntegerField()
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="order_reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    msg = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
