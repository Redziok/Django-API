from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_Books),
    path('add', views.Add_Book),

    path('<str:pk>', views.Get_Book),
    path('update/<str:pk>', views.Update_Book),
    path('delete/<str:pk>', views.Delete_Book),
]