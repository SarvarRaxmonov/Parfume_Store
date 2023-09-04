from rest_framework.generics import ListAPIView

from apps.product.models import Banner, Story
from apps.product.serializers import BannerSerializer, StorySerializer


class LatestBannersListView(ListAPIView):
    queryset = Banner.objects.order_by("-created_at")[:5]
    serializer_class = BannerSerializer


class StoryContentListView(ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
