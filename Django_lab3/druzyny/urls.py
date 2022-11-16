from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDruzyny),
    path('<str:pk>', views.druzynaDetail),
]