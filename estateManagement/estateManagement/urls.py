
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('estate_api.urls')),
    path('admin/', admin.site.urls),
]
