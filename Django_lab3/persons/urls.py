from .views import UserController
from django.urls import path

urlpatterns = [
    path('', UserController.as_view(), name='register'),
]