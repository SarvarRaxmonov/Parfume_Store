from rest_framework import generics

from apps.cart.models.orders import Order, Review, Liked
from apps.cart.serializers.order import OrderSerializer, OrderUpdateSerializer, ReviewSerializer, LikedSerializer


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer


class LikedListAPIView(generics.ListAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #
    # def perform_create(self, request):
    #     user = request.user
