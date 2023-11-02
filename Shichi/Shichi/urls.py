"""
URL configuration for Shichi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include , re_path
# from CustomUser.views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shichi API",
        default_version='v1',
        description="Welcome to the world of Shichi",
        terms_of_service="https://www.Shichi.org",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'), 
    path('docss/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
    path('user/', include('CustomUser.urls')),
    path('advertisement/', include('CustomAdvertisement.urls')),
    path('location/', include('CustomAdvertisementLocation.urls')),
    path('carimage/', include('CustomCarImage.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)