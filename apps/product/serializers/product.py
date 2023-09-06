from rest_framework import serializers

from apps.product.models import (Product, ProductBrand, ProductCategory,
                                 ProductImage, ProductTag, ProductType,
                                 SearchKeyword, Section, Volume)


class ChildSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ("id", "name", "icon")


class ProductCategorySerializer(serializers.ModelSerializer):
    section = ChildSectionSerializer(many=True, read_only=True, source="section_category")

    class Meta:
        model = ProductCategory
        fields = ("id", "name", "icon", "section")


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
    category = ProductCategorySerializer(source="section.category")
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
            "category",
            "tags",
            "type",
            "volume",
        )

    def get_discount_price(self, obj):
        if obj:
            if obj.discount > 0:
                price = obj.price
                discount_price = (obj.discount / 100) * price
                return int(discount_price)
        return obj


class SectionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True, source="product_section")

    class Meta:
        model = Section
        fields = ("id", "name", "product")


class SearchKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchKeyword
        fields = ("keyword", "device_id")
