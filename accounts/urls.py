from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('signin/', TemplateView.as_view(template_name="accounts/sign-in.html"), name='sign-in'),
    path('signup/', TemplateView.as_view(template_name="accounts/sign-up.html"), name='sign-up'),
]