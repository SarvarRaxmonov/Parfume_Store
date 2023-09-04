from rest_framework.generics import ListAPIView

from .models import Banner
from .serializers import BannerSerializer


class LatestBannersListView(ListAPIView):
    queryset = Banner.objects.order_by("-created_at")[:5]
    serializer_class = BannerSerializer
