from django.urls import path

from apps.product.views.product import (BrandListView, CategoryListView,
                                        LatestBannersListView, MainSectionView,
                                        NewestProductListView,
                                        PopularCategoryListView,
                                        PopularSearchedKeywordsListView,
                                        ProductCategoryRetrieveView,
                                        ProductDetailView, ProductListView,
                                        RecommendedProductListView,
                                        SearchHistoryDeleteView,
                                        SearchHistoryView,
                                        SearchKeywordDeleteView)
from apps.product.views.story import StoryContentRetrieveView, StoryListView

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
    path("latest-banners/", LatestBannersListView.as_view(), name="latest-banners"),
    path(
        "products/",
        ProductListView.as_view(),
        name="products",
    ),
    path(
        "product-detail/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
    path(
        "recommended-products/",
        RecommendedProductListView.as_view(),
        name="recommended-products",
    ),
    path("newest-products/", NewestProductListView.as_view(), name="newest-products"),
    path("brands/", BrandListView.as_view(), name="brands"),
    path("main-stories/", StoryListView.as_view(), name="main-stories"),
    path(
        "story-content-detail/<int:pk>/",
        StoryContentRetrieveView.as_view(),
        name="story-content-detail",
    ),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path(
        "popular-categories/",
        PopularCategoryListView.as_view(),
        name="popular-categories",
    ),
    path(
        "category-detail/<int:pk>/",
        ProductCategoryRetrieveView.as_view(),
        name="category-detail",
    ),
    path("main-section/", MainSectionView.as_view(), name="main-section"),
]
