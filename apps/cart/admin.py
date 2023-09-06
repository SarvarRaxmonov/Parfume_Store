from django.contrib import admin

from apps.cart.models.cart import (Accreditation, BankCard, Cart, District,
                                   PaymentMethod, Region, UserPhone)
from apps.cart.models.orders import Liked, Order, Review


@admin.register(Liked)
class LikedAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "is_saved")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("type", "accreditation", "number", "cashback")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "order", "rating", "msg")


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "region",
        "full_name",
        "location",
        "total_price",
        "discount_price",
        "used_cashback",
        "NDS",
        "cashback",
    )


@admin.register(BankCard)
class BankCardAdmin(admin.ModelAdmin):
    list_display = ("user", "accreditation", "number")


@admin.register(UserPhone)
class UserPhoneAdmin(admin.ModelAdmin):
    list_display = ("user", "accreditation", "phone_number")


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("user", "accreditation", "name")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "count")
