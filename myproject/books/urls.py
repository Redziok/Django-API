from .views import BookController
from django.urls import path

urlpatterns = [
    path('', BookController.as_view(), name='book'),
]