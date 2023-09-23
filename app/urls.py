from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventAPIView.as_view(), name='event-list'),
]

