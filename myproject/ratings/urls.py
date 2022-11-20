from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_Ratings),
    path('add', views.Add_Rating),

    path('<str:pk>', views.Get_Rating),
    path('update/<str:pk>', views.Update_Rating),
    path('delete/<str:pk>', views.Delete_Rating),
]