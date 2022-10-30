from django.urls import path
from . import views

urlpatterns = [
    path('', views.getBooks),
    path('add', views.addBook),

    path('<str:pk>', views.getBook),
    path('update/<str:pk>', views.updateBook),
    path('delete/<str:pk>', views.deleteBook),
]