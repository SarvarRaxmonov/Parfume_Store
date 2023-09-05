from rest_framework import serializers

from apps.product.models import Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("id", "name", "description", "image", "url")
