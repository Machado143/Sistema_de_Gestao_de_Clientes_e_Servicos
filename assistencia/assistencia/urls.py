"""
URL configuration for assistencia project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.api_urls')),  # Rotas da API REST
    path('api-auth/', include('rest_framework.urls')),  # Login da API browsable
    path('', include('core.urls')),  # Rotas web normais
]