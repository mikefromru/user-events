from django.urls import path
from django.views.generic import TemplateView
from .views import views

urlpatterns = [
    # path(r'', TemplateView.as_view(template_name='app/app.html'), name='app'),
    path(r'', views.foo, name='app'),
]