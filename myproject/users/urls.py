from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_Users),
    path('add', views.Add_User),

    path('<str:pk>', views.Get_User),
    path('delete/<str:pk>', views.Delete_User),
    path('update/<str:pk>', views.Update_User),
]