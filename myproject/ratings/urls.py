from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_ratings),
    path('add', views.add_rating),

    path('<str:pk>', views.get_rating),
    path('update/<str:pk>', views.update_rating),
    path('delete/<str:pk>', views.delete_rating),
]