from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("users/", include("users.urls", namespace="users")),
    path("boards/", include("boards.urls", namespace="boards")),
    path("admin/", admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
