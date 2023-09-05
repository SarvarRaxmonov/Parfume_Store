from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.cart.models.cart import \
    Accreditation  # Assuming Accreditation model is in the same app
from apps.product.models import Product
from apps.user.models import User


class Liked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="liked_product", on_delete=models.CASCADE)
    is_saved = models.BooleanField(default=False)


class Order(models.Model):
    class OrderTextChoice(models.TextChoices):
        DELIVERED = "delivered", "Delivered"
        DURING_DELIVERY = "during_delivery", "During Delivery"
        CANCELED = "canceled", "Canceled"

    type = models.CharField(max_length=15, choices=OrderTextChoice.choices)
    accreditation = models.ForeignKey(Accreditation, related_name="order_accreditation", on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    cashback = models.IntegerField()


class Review(models.Model):
    user = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="order_reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    msg = models.TextField()
