from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:container_id>/', views.container, name='container'),
    path('all/', views.allContainers, name='allContainers'),
]