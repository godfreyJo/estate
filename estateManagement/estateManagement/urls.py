from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('estate_api.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Estate Management Admin"
admin.site.site_title = "Estate Management Admin Portal"
admin.site.index_title = "Welcome to Estate Management Portal"
