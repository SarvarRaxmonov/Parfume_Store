from django.contrib import admin

from apps.product.models import (Banner, Product, ProductBrand,
                                 ProductCategory, ProductCategoryViewed,
                                 ProductImage, ProductTag, ProductType,
                                 SearchKeyword, Section, Story, StoryContent,
                                 ViewedProduct, ViewedStory, Volume)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("file", "url")


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProductCategoryViewed)
class ProductCategoryViewedAdmin(admin.ModelAdmin):
    list_display = ("category", "device_id")


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
    list_display = ("id", "size")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "currency", "brand")


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_main")


@admin.register(StoryContent)
class StoryContentAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ViewedStory)
class ViewedStoryAdmin(admin.ModelAdmin):
    list_display = ("story", "device_id")


@admin.register(ViewedProduct)
class ViewedProductAdmin(admin.ModelAdmin):
    list_display = ("product", "device_id")


@admin.register(SearchKeyword)
class SearchKeywordAdmin(admin.ModelAdmin):
    list_display = ("keyword", "device_id")
