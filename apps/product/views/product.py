from django.db.models import Count
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.product.models import (Banner, Product, ProductBrand,
                                 ProductCategory, ProductCategoryViewed,
                                 Section)
from apps.product.serializers.banner import BannerSerializer
from apps.product.serializers.product import (ProductBrandSerializer,
                                              ProductCategorySerializer,
                                              ProductSerializer,
                                              SectionSerializer)
from apps.product.utils import generate_device_id


class LatestBannersListView(ListAPIView):
    queryset = Banner.objects.order_by("-created_at")[:5]
    serializer_class = BannerSerializer


class CategoryListView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class PopularCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer

    def get_queryset(self):
        queryset = ProductCategory.objects.annotate(view_count=Count("view_to_category")).order_by("-view_count")[:6]
        return queryset


class ProductCategoryRetrieveView(RetrieveAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get(self, request, pk=None, *args, **kwargs):
        queryset = self.get_object()
        device_id = generate_device_id()
        obj = ProductCategoryViewed.objects.get_or_create(category=queryset, device_id=device_id)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class RecommendedProductListView(ListAPIView):
    queryset = Product.objects.exclude(is_recommended=False)
    serializer_class = ProductSerializer


class NewestProductListView(ListAPIView):
    queryset = Product.objects.order_by("-created_at")
    serializer_class = ProductSerializer


class BrandListView(ListAPIView):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer


class MainSectionView(ListAPIView):
    queryset = Section.objects.filter(is_main=True)
    serializer_class = SectionSerializer
