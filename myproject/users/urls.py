from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users),
    path('add', views.add_user),

    path('<str:pk>', views.get_user),
    path('delete/<str:pk>', views.delete_user),
    path('update/<str:pk>', views.update_user),
]