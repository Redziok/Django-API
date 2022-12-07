from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_ratings),
    path('add', views.add_rating),

    path('<str:pk>', views.get_rating),
    path('update/<str:pk>', views.update_rating),
    path('delete/<str:pk>', views.delete_rating),
    path('getbyrating/<int:book_amount>', views.get_book_by_rating),
]