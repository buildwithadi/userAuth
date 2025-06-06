from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/',include('user.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
]
