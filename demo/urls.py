from django.urls import path

from .views import DashboardTemplateView


urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='dashboard'),
]
