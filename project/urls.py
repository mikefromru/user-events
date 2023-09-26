from django.contrib import admin
from django.urls import path, include

from app.routers.api import api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/v1/app/', include(api_urlpatterns)),
    path('accounts/', include('rest_registration.api.urls')),
]
