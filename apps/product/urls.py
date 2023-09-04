from django.urls import path

from .views import LatestBannersListView

urlpatterns = [
    path("latest-banners/", LatestBannersListView.as_view(), name="latest-banners"),
]
