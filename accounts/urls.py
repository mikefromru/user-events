from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', TemplateView.as_view(template_name="accounts/sign-up.html"), name='sign-up'),
]

