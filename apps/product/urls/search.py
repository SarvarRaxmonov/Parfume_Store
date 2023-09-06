from django.urls import path

from apps.product.views.search import (
    PopularSearchedKeywordsListView,
    SearchHistoryDeleteView,
    SearchHistoryView,
    SearchKeywordDeleteView,
)

urlpatterns = [
    path(
        "search-history/<str:device_id>/",
        SearchHistoryView.as_view(),
        name="search-history",
    ),
    path(
        "search-history-delete/<str:device_id>/",
        SearchHistoryDeleteView.as_view(),
        name="search-history-delete",
    ),
    path(
        "search-keyword-delete/<str:keyword>/",
        SearchKeywordDeleteView.as_view(),
        name="search-keyword-delete",
    ),
    path(
        "popular-search-keywords/",
        PopularSearchedKeywordsListView.as_view(),
        name="popular-search-keywords",
    ),
]
