from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRatings),
    path('add', views.addRating),

    path('<str:pk>', views.getRating),
    path('update/<str:pk>', views.updateRating),
    path('delete/<str:pk>', views.deleteRating),
]