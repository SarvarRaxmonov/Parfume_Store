from django.contrib import admin

from apps.user.models import District, Profile, Region, User
from apps.user.models.notifications import Notification, ReadNotification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(ReadNotification)
class AdminReadNotification(admin.ModelAdmin):
    list_display = ("id", "user")
