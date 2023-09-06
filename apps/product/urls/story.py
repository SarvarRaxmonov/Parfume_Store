from django.urls import path

from apps.product.views.story import StoryContentRetrieveView, StoryListView

urlpatterns = [
    path("main-stories/", StoryListView.as_view(), name="main-stories"),
    path(
        "story-content-detail/<int:pk>/",
        StoryContentRetrieveView.as_view(),
        name="story-content-detail",
    ),
]
