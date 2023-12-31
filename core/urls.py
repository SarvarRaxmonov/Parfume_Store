from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("apps.user.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("products/", include("apps.product.main_urls")),
    path("cart/", include("apps.cart.urls")),

    # Rosetta
    path('rosetta/', include('rosetta.urls')),

]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
