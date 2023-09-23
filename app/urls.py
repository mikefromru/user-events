from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventAPIView.as_view(), name='event-list'),
    path('event/<int:pk>/', views.EventDetailAPIView.as_view(), name='event'),
]

