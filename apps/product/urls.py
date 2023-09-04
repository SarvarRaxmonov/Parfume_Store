from django.urls import path

from apps.product.views import LatestBannersListView, StoryContentListView

urlpatterns = [
    path("latest-banners/", LatestBannersListView.as_view(), name="latest-banners"),
    path("main-stories/", StoryContentListView.as_view(), name="main-stories"),
]
