from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_authors),
    path('add', views.add_author),

    path('<str:pk>', views.get_author),
    path('update/<str:pk>', views.update_author),
    path('delete/<str:pk>', views.delete_author),
]