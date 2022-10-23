from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.getAuthors),
    path('users/', views.getUsers),

    path('authors/add/', views.addAuthor),

    path('authors/<str:pk>/', views.getAuthor),
    path('users/<str:pk>/', views.getUser),

    path('authors/update/<str:pk>/', views.updateAuthor),

    path('authors/delete/<str:pk>/', views.deleteAuthor),
    path('users/delete/<str:pk>/', views.deleteUser),
]