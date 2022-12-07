from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_books),
    path('add', views.add_book),

    path('<str:pk>', views.get_book),
    path('update/<str:pk>', views.update_book),
    path('delete/<str:pk>', views.delete_book),
    path('getbytitle/<str:title_contains>', views.get_book_by_title),
    path('getbyauthor/<str:author_contains>', views.get_book_by_author),
]