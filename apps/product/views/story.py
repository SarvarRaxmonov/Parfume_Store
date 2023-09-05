from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.product.models import Story, StoryContent, ViewedStory
from apps.product.serializers.story import (StoryContentSerializer,
                                            StorySerializer)
from apps.product.utils import generate_device_id


class StoryListView(ListAPIView):
    queryset = Story.objects.exclude(is_main=False)
    serializer_class = StorySerializer


class StoryContentRetrieveView(RetrieveAPIView):
    queryset = StoryContent.objects.all()
    serializer_class = StoryContentSerializer

    def get(self, request, pk=None, *args, **kwargs):
        queryset = self.get_object()
        device_id = generate_device_id()
        obj = ViewedStory.objects.get_or_create(story=queryset, device_id=device_id)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
