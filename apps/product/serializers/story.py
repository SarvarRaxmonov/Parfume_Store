from rest_framework import serializers

from apps.product.models import Story, StoryContent, ViewedStory
from apps.product.utils import generate_device_id


class StoryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryContent
        fields = ("id", "name", "video", "photo")


class StorySerializer(serializers.ModelSerializer):
    content = StoryContentSerializer(many=True)
    is_full_viewed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Story
        fields = ("id", "name", "content", "is_full_viewed")

    def get_is_full_viewed(self, obj):
        device_id = generate_device_id()
        view = ViewedStory.objects.filter(device_id=device_id, story__story_to_content__id=obj.id)
        print(obj.content.count(), view.count())
        if obj.content.count() == view.count():
            return True
        return False
