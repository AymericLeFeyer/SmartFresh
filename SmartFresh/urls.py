from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('SmartFreshApp/', include('SmartFreshApp.urls')),
    path('admin/', admin.site.urls),
]