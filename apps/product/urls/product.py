from django.urls import path

from apps.product.views.product import (
    BrandListView,
    CategoryListView,
    LatestBannersListView,
    MainSectionView,
    NewestProductListView,
    PopularCategoryListView,
    ProductCategoryRetrieveView,
    ProductDetailView,
    ProductListView,
    RecommendedProductListView,
    RelatedProductsViewSet,
    SameTypedProductsListView,
    SectionDetailView,
)

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products"),
    path(
        "product-detail/<int:pk>/", ProductDetailView.as_view(), name="product-detail"
    ),
    path(
        "recommended-products/",
        RecommendedProductListView.as_view(),
        name="recommended-products",
    ),
    path("newest-products/", NewestProductListView.as_view(), name="newest-products"),
    path(
        "same-typed-products/<int:pk>/",
        SameTypedProductsListView.as_view(),
        name="same-typed-products",
    ),
    path(
        "related-products/<int:product_id>/",
        RelatedProductsViewSet.as_view(),
        name="related-products",
    ),
    path("brands/", BrandListView.as_view(), name="brands"),
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
    path(
        "section-detail/<int:pk>/", SectionDetailView.as_view(), name="section-detail"
    ),
    path("main-section/", MainSectionView.as_view(), name="main-section"),
    path("latest-banners/", LatestBannersListView.as_view(), name="latest-banners"),
]
