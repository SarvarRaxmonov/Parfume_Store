from rest_framework import generics

from apps.cart.models.cart import Cart, Region
from apps.cart.serializers.cart import (CartSerializer, CartUpdateSerializer,
                                        RegionSerializer)


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartCreateAPIView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartUpdateAPIView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartUpdateSerializer

    # def

class CartDestroyAPIView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# Region Views
class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionCreateAPIView(generics.CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
