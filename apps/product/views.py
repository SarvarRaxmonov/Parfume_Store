from rest_framework.generics import ListAPIView

from apps.product.models import Banner, Product, Story
from apps.product.serializers.banner import BannerSerializer
from apps.product.serializers.product import ProductSerializer
from apps.product.serializers.story import StorySerializer


class LatestBannersListView(ListAPIView):
    queryset = Banner.objects.order_by("-created_at")[:5]
    serializer_class = BannerSerializer


class StoryListView(ListAPIView):
    queryset = Story.objects.exclude(is_main=False)
    serializer_class = StorySerializer


class RecommendedProductListView(ListAPIView):
    queryset = Product.objects.exclude(is_recommended=False)
    serializer_class = ProductSerializer
