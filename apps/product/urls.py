from django.urls import path

from apps.product.views import (LatestBannersListView,
                                RecommendedProductListView, StoryListView)

urlpatterns = [
    path("latest-banners/", LatestBannersListView.as_view(), name="latest-banners"),
    path("main-stories/", StoryListView.as_view(), name="main-stories"),
    path("recommended-products/", RecommendedProductListView.as_view(), name="recommended-products"),
]
