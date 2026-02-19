from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/users/login/", permanent=False)),
    path("admin/login/", RedirectView.as_view(url="/users/login/", permanent=False)),  # ✅ home
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path("orders/", include("orders.urls")),
    path("users/", include("users.urls")),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

