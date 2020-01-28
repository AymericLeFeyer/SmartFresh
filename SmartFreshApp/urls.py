from django.urls import path

from . import views

urlpatterns = [
    path('', views.allContainers, name='allContainers'),
    path('<int:container_id>/', views.container, name='container'),
    path('<str:container_name>/', views.containerByName, name='containerByName'),
]