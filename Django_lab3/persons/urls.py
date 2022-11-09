from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPersons),
    path('<str:pk>', views.personDetail),
    path('contain/<str:string>', views.personGetContain),
]