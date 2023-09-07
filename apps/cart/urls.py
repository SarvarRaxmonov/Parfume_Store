from django.urls import path

from apps.cart.views.cart import (
    CartCreateAPIView,
    CartDestroyAPIView,
    CartListAPIView,
    CartUpdateAPIView, RegionListAPIView,
)
from apps.cart.views.order import (
    OrderCreateAPIView,
    OrderListAPIView,
    OrderUpdateAPIView, ReviewListAPIView, ReviewCreateAPIView, LikedListAPIView,
)

urlpatterns = [
    # Cart Urls
    path("list/", CartListAPIView.as_view(), name="cart-list"),
    path("create/", CartCreateAPIView.as_view(), name="cart-create"),
    path("update/<int:pk>/", CartUpdateAPIView.as_view(), name="cart-update"),
    path("delete/<int:pk>/", CartDestroyAPIView.as_view(), name="cart-delete"),
    # Order Urls
    path("order/list/", OrderListAPIView.as_view(), name="order-list"),
    path("order/create/", OrderCreateAPIView.as_view(), name="order-create"),
    path("order/update/<int:pk>/", OrderUpdateAPIView.as_view(), name="order-update"),
    # Review Serializer
    path("product/<int:pk>/review/list/", ReviewListAPIView.as_view(), name="review-list"),
    path("review/create/", ReviewCreateAPIView.as_view(), name="review-create"),
    # Liked urls
    path("liked/list/", LikedListAPIView.as_view(), name="liked-list"),
    path("region/list/", RegionListAPIView.as_view(), name="region-list"),

]
