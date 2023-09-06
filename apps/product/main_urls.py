from django.urls import include, path

urlpatterns = [
    path("", include("apps.product.urls.product")),
    path("", include("apps.product.urls.search")),
    path("", include("apps.product.urls.story")),
]
