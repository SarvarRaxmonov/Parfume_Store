from rest_framework import serializers

from apps.cart.models.orders import Liked, Order, Review


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liked
        fields = ("user", "product", "is_saved")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("type", "accreditation", "number")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
