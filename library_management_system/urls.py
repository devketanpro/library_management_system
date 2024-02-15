"""
URL configuration for library_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Library Management System",
        default_version='v1',
        description="Borrow/return books and Manage books, booking records.",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls), # Django admin page.
    path("api/", include("library.urls")), # API urls.
    path('gettoken/', TokenObtainPairView.as_view()), # To create/get access and refresh tokens.
    path('refreshtoken/', TokenRefreshView.as_view()), # To get access token by given refresh token.
    path('verifytoken/', TokenVerifyView.as_view()), # To verify access token.
    re_path('swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # API documentation using Swagger
    re_path('redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # API documentation using redoc
]
