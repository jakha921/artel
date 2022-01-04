from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', admin.site.urls),
    path('app/', include('artelApp.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/auth/', include('dj_rest_auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# change admin panel name
admin.site.site_header = 'Admin Panel for Artel'
admin.site.site_title = 'Artel catalog'