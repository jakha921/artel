from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artelApp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration', include('dj_rest_auth.registration.urls')),
    path('api/allauth', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
