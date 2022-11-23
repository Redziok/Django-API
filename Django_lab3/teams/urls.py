from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_team),
    path('<str:pk>', views.team_detail),
    path('update/<str:pk>', views.team_update_delete),
    path('delete/<str:pk>', views.team_update_delete),
]