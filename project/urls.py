from django.contrib import admin
from django.urls import path, include

from app.routers.api import api_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/v1/app/', include(api_urlpatterns)),
    path('accounts/', include('rest_registration.api.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns