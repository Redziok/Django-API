from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_person),
    path('<str:pk>', views.person_detail),
    path('contain/<str:string>', views.person_get_contain),
    path('update/<str:pk>', views.person_update),
    path('delete/<str:pk>', views.person_delete),
    path('getbyteam/<str:pk>', views.get_person_by_team_id)
]