from django.urls import path

from . import views

urlpatterns = [
    path('', views.allContainers, name='allContainers'),
    path('research/', views.research, name='research'),
    path('search/<int:container_id>/', views.container, name='container'),
    path('search/<str:container_name>/', views.containerByName, name='containerByName'),
]