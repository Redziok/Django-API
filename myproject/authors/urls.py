from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAuthors),
    path('add', views.addAuthor),

    path('<str:pk>', views.getAuthor),
    path('update/<str:pk>', views.updateAuthor),
    path('delete/<str:pk>', views.deleteAuthor),
]