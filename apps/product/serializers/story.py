from rest_framework import serializers

from apps.product.models import Story, StoryContent, ViewedStory


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
        device_id = 2222
        view = ViewedStory.objects.filter(id=device_id, story=obj.id)
        if obj.content.count() == view.count():
            return True
        return False
