from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.getAuthors),

    path('authors/add/', views.addAuthor),

    path('<str:pk>/', views.getAuthor),

    path('update/<str:pk>/', views.updateAuthor),

    path('delete/<str:pk>/', views.deleteAuthor),
]