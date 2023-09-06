import random

from django.db.models import Count
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.product.filters import ProductBrandFilter, ProductFilter
from apps.product.models import (
    Banner,
    Product,
    ProductBrand,
    ProductCategory,
    ProductCategoryViewed,
    ProductType,
    Section,
    ViewedProduct,
)
from apps.product.serializers.banner import BannerSerializer
from apps.product.serializers.product import (
    ChildProductTypeSerializer,
    ChildSectionSerializer,
    ProductBrandSerializer,
    ProductCategorySerializer,
    ProductSerializer,
    SectionSerializer,
)
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
        queryset = ProductCategory.objects.annotate(
            view_count=Count("view_to_category")
        ).order_by("-view_count")[:6]
        return queryset


class ProductCategoryRetrieveView(RetrieveAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get(self, request, pk=None, *args, **kwargs):
        queryset = self.get_object()
        device_id = generate_device_id()
        ProductCategoryViewed.objects.get_or_create(
            category=queryset, device_id=device_id
        )
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk=None, *args, **kwargs):
        queryset = self.get_object()
        device_id = generate_device_id()
        ViewedProduct.objects.get_or_create(product=queryset, device_id=device_id)
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
    filterset_class = ProductBrandFilter


class MainSectionView(ListAPIView):
    queryset = Section.objects.filter(is_main=True)
    serializer_class = SectionSerializer


class SectionDetailView(RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = ChildSectionSerializer


class SameTypedProductsListView(RetrieveAPIView):
    queryset = ProductType
    serializer_class = ChildProductTypeSerializer


class RelatedProductsViewSet(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "product_id"

    def get(self, request, product_id=None, *args, **kwargs):
        try:
            obj = self.get_queryset().get(id=product_id)
            selected_product_tags = obj.tags.all()
            related_products = (
                self.get_queryset()
                .filter(tags__in=selected_product_tags)
                .exclude(id=product_id)
                .distinct()
            )
            related_products_list = list(related_products)
            random.shuffle(related_products_list)
            random_related_products = related_products_list[:2]
            serializer = self.serializer_class(
                instance=random_related_products, many=True
            )
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"message": "Product not found."}, status=404)
