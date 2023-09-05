from rest_framework import serializers

from apps.product.models import (Product, ProductBrand, ProductCategory,
                                 ProductImage, ProductTag, ProductType,
                                 Section, Volume)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("id", "name", "icon")


class SectionSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Section
        fields = ("id", "name", "icon", "category", "is_main")


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "file", "url")


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
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Volume
        fields = ("id", "images", "size", "is_available")


class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField(read_only=True, default=0)
    section = SectionSerializer(many=True)
    images = ProductImageSerializer(many=True)
    tags = ProductTagSerializer(many=True)
    volume = VolumeSerializer(many=True)
    brand = ProductBrandSerializer()
    type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "currency",
            "is_recommended",
            "is_available",
            "description",
            "discount",
            "discount_price",
            "expire_time",
            "brand",
            "images",
            "section",
            "tags",
            "type",
            "volume",
        )

    def get_discount_price(self, instance):
        if instance.discount > 0:
            price = instance.price
            discount_price = (instance.discount / 100) * price
            return int(discount_price)
