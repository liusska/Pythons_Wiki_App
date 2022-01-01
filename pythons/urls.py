from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pythons.pythons_app.urls')),
    path('auth/', include('pythons.pythons_auth.urls')),
    path('profiles/', include('pythons.profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
