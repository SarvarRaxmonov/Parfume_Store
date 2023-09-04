from rest_framework import serializers

from .models import (Banner, Product, ProductBrand, ProductCategory,
                     ProductImage, ProductTag, ProductType, Section, Story,
                     StoryContent, Volume)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "currency",
            "is_recommended",
            "is_available",
            "brand",
            "description",
            "discount",
            "expire_time",
            "images",
            "section",
            "tags",
            "type",
            "volume",
        )


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ("id", "name", "icon", "category", "is_main")


class BannerSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    section = SectionSerializer()

    class Meta:
        model = Banner
        fields = ("id", "image", "product", "section", "is_main")


# =================================================================


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "file", "url")


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("id", "name", "icon")


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = ("id", "name", "icon")


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = ("id", "name")


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ("id", "name")


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ("id", "images", "size", "type", "is_available")


class StoryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryContent
        fields = ("id", "name", "video", "photo")


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("id", "name", "content")
