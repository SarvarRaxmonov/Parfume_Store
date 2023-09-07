from rest_framework import serializers

from apps.cart.models.orders import Liked, Order, Review


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liked
        fields = ("user", "product", "is_saved")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("type", "accreditation", "number", "cashback")


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("type", "is_delivered")


class ReviewSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = ("user", "product","full_name", "rating", "msg")

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
