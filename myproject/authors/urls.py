from .views import AuthorController
from django.urls import path

urlpatterns = [
    path('', AuthorController.as_view(), name='authors'),
]