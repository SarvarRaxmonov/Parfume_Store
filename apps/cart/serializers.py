from rest_framework import serializers
from apps.cart.models import Region, District, Accreditation, BankCard, UserPhone, PaymentMethod, Cart


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'region', 'name')


class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accreditation
        fields = (
            'id', 'user', 'region', 'full_name', 'lat', 'lon', 'location', 'total_price', 'discount_price',
            'used_cashback',
            'NDS', 'cashback')


class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = ('id', 'user', 'accreditation', 'number')


class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhone
        fields = ('id', 'user', 'accreditation', 'phone_number')


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'user', 'accreditation', 'name')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'title', 'image', 'price', 'count')
