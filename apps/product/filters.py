import django_filters

from apps.product.models import Product, ProductBrand, SearchKeyword
from apps.product.utils import generate_device_id


class ProductBrandFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ProductBrand
        fields = ("name",)


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", method="name_filter"
    )
    category_ids = django_filters.CharFilter(method="filter_category_ids")
    brand_ids = django_filters.CharFilter(method="filter_brand_ids")
    discount_on = django_filters.BooleanFilter(
        field_name="discount", lookup_expr="exact", method="discount_on_filter"
    )
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Product
        fields = ("name",)

    def name_filter(self, queryset, name, value):
        if value:
            device_id = generate_device_id()
            obj = SearchKeyword.objects.get_or_create(
                keyword=value, device_id=device_id
            )

        return queryset

    def discount_on_filter(self, queryset, name, value):
        if value is True:
            return queryset.filter(discount__gte=1)
        return queryset

    def filter_category_ids(self, queryset, name, value):
        ids_list = value.split(",")
        return queryset.filter(section__category__id__in=ids_list)

    def filter_brand_ids(self, queryset, name, value):
        ids_list = value.split(",")
        return queryset.filter(brand__id__in=ids_list)
