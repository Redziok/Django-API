from .views import RatingController
from django.urls import path

urlpatterns = [
    path('', RatingController.as_view(), name='rating'),
]