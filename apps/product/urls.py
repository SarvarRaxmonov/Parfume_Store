from django.urls import path

from apps.product.views.product import (BrandListView, CategoryListView,
                                        LatestBannersListView, MainSectionView,
                                        NewestProductListView,
                                        PopularCategoryListView,
                                        ProductCategoryRetrieveView,
                                        RecommendedProductListView)
from apps.product.views.story import StoryContentRetrieveView, StoryListView

urlpatterns = [
    path("latest-banners/", LatestBannersListView.as_view(), name="latest-banners"),
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
