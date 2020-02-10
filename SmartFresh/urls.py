from django.contrib import admin
from django.urls import include, path
from SmartFreshApp import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('SmartFreshApp/', include('SmartFreshApp.urls')),
    path('research/', views.research),
    path('admin/', admin.site.urls),
]