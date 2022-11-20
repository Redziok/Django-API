from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_Authors),
    path('add', views.Add_Author),

    path('<str:pk>', views.Get_Author),
    path('update/<str:pk>', views.Update_Author),
    path('delete/<str:pk>', views.Delete_Author),
]