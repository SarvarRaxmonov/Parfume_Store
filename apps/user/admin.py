from django.contrib import admin

from apps.user.models.users import District, Profile, Region, User


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
