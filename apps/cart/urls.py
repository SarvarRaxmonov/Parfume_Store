from django.urls import path

from apps.cart.views.cart import (CartCreateAPIView, CartDestroyAPIView,
                                  CartListAPIView, CartUpdateAPIView)
from apps.cart.views.order import (OrderCreateAPIView, OrderListAPIView,
                                   OrderUpdateAPIView)

urlpatterns = [
    # Cart Urls
    path("list/", CartListAPIView.as_view(), name="cart_list"),
    path("create/", CartCreateAPIView.as_view(), name="cart_create"),
    path("update/<int:pk>/", CartUpdateAPIView.as_view(), name="cart_update"),
    path("delete/<int:pk>/", CartDestroyAPIView.as_view(), name="cart_delete"),
    # Order Urls
    path("order/list/", OrderListAPIView.as_view(), name="order_list"),
    path("order/create/", OrderCreateAPIView.as_view(), name="order_create"),
    path("order/update/<int:pk>/", OrderUpdateAPIView.as_view(), name="order_update"),
]
