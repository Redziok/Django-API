from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPersons),
    path('<str:pk>', views.personDetail),
    path('contain/<str:string>', views.personGetContain),
    path('persons/update/<str:pk>', views.personUpdateDelete),
    path('persons/delete/<str:pk>', views.personUpdateDelete),
]