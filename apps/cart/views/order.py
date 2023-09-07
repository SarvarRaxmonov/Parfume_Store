from rest_framework import generics

from apps.cart.models.orders import Liked, Order, Review
from apps.cart.serializers.order import (LikedSerializer, OrderSerializer,
                                         OrderUpdateSerializer,
                                         ReviewSerializer)


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

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Review.objects.filter(product=pk)


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #
    # def perform_create(self, request):
    #     user = request.user
