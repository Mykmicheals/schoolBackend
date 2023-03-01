from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.admin import teacher_admin_site

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('teacher-admin/', teacher_admin_site.urls),
    path('', include('userauth.urls')),
    path('app/', include('app.urls')),
      
]
