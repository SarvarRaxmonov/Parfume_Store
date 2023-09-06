from rest_framework import status
from rest_framework.generics import RetrieveDestroyAPIView, ListAPIView
from apps.product.models import SearchKeyword, Product
from apps.product.serializers.product import PopularProductsSerializer, SearchKeywordSerializer
from django.db.models import Count
from rest_framework.response import Response
from apps.product.utils import generate_device_id


class PopularSearchedKeywordsListView(ListAPIView):
    serializer_class = PopularProductsSerializer

    def get_queryset(self):
        queryset = Product.objects.annotate(view_count=Count("view_to_product")).order_by("-view_count")[:6]
        return queryset


class SearchHistoryView(ListAPIView):
    queryset = SearchKeyword.objects.all()
    serializer_class = SearchKeywordSerializer
    lookup_field = ("device_id",)

    def get(self, request, device_id=None, *args, **kwargs):
        obj = self.get_queryset().filter(device_id=device_id).order_by("-id")[:7]
        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data)


class SearchHistoryDeleteView(RetrieveDestroyAPIView):
    queryset = SearchKeyword.objects.all()
    serializer_class = SearchKeywordSerializer
    lookup_field = "device_id"

    def destroy(self, request, device_id=None, *args, **kwargs):
        deleted_count, _ = self.get_queryset().filter(device_id=device_id).delete()
        if deleted_count > 0:
            return Response(
                {"message": f"Deleted {deleted_count} keywords for device {device_id}"},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"message": f"No keywords found for device {device_id}"},
                status=status.HTTP_404_NOT_FOUND,
            )


class SearchKeywordDeleteView(RetrieveDestroyAPIView):
    queryset = SearchKeyword.objects.all()
    serializer_class = SearchKeywordSerializer
    lookup_field = "keyword"

    def destroy(self, request, keyword=None, *args, **kwargs):
        device_id = generate_device_id()
        deleted_count, _ = self.get_queryset().filter(device_id=device_id, keyword=keyword).delete()
        if deleted_count:
            return Response(
                {"message": f"Deleted {keyword} keyword for device {device_id}"},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"message": f"No keywords found for device {device_id}"},
                status=status.HTTP_404_NOT_FOUND,
            )
