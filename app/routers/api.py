from django.urls import path
from ..views import api_views

api_urlpatterns = [
    path('', api_views.EventAPIView.as_view(), name='event-user-list'),
    path('events/', api_views.EventListAPIView.as_view(), name='event-list'),
    path('event/<int:pk>/', api_views.EventDetailAPIView.as_view(), name='event'),
]
