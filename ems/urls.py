from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Employee Management API",
      default_version='v1',
      description="API documentation for EMS project",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Employee APIs
    path('api/', include('employees.urls')),
    path('api/', include('departments.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)), 
]
