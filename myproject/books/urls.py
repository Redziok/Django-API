from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_books),
    path('add', views.add_book),

    path('<str:pk>', views.get_book),
    path('update/<str:pk>', views.update_book),
    path('delete/<str:pk>', views.delete_book),
]