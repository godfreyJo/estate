from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import  include, path


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profile/", include("apps.profiles.urls")),
    path("api/v1/properties/", include("apps.properties.urls")),
    path("api/v1/ratings/", include("apps.ratings.urls")),
    path("api/v1/enquiries/", include("apps.enquiries.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Estate Management Admin"
admin.site.site_title = "Estate Management Admin Portal"
admin.site.index_title = "Welcome to Estate Management Portal"


 # path('', include('estate_api.urls')),