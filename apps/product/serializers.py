from rest_framework import serializers

from apps.product.models import (Banner, Product, ProductBrand,
                                 ProductCategory, ProductImage, ProductTag,
                                 ProductType, Section, Story, StoryContent,
                                 ViewedStory, Volume)


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


class StoryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryContent
        fields = ("id", "name", "video", "photo")


class StorySerializer(serializers.ModelSerializer):
    content = StoryContentSerializer(many=True)
    is_full_viewed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Story
        fields = ("id", "name", "content", "is_full_viewed")

    def get_is_full_viewed(self, obj):
        device_id = 2222
        view = ViewedStory.objects.filter(id=device_id, story=obj.id)
        if obj.content.count() == view.count():
            return True
        return False


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
