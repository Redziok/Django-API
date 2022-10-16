from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.getAuthors),
    path('authors/<str:pk>/', views.getAuthor),
    path('authors/add/', views.addAuthor),
    path('authors/update/<str:pk>', views.updateAuthor),
    path('authors/delete/<str:pk>/', views.deleteAuthor),
]