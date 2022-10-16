from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('', RegisterAPI.as_view(), name='register'),
]