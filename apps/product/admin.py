from django.contrib import admin

from apps.product.models import (Banner, Product, ProductBrand,
                                 ProductCategory, ProductImage, ProductTag,
                                 ProductType, Section, Story, StoryContent,
                                 ViewedStory, Volume)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("file", "url")


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ("size", "type")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "currency", "brand")


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "product")


@admin.register(StoryContent)
class StoryContentAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ViewedStory)
class ViewedStoryAdmin(admin.ModelAdmin):
    list_display = ("story", "device_id")
