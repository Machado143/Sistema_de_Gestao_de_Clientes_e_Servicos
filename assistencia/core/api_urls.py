from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    ClienteViewSet, ServicoViewSet, StatusViewSet,
    OrdemServicoViewSet, DashboardViewSet
)

# Cria o router e registra os viewsets
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='api-cliente')
router.register(r'servicos', ServicoViewSet, basename='api-servico')
router.register(r'status', StatusViewSet, basename='api-status')
router.register(r'ordens', OrdemServicoViewSet, basename='api-ordem')
router.register(r'dashboard', DashboardViewSet, basename='api-dashboard')

urlpatterns = [
    path('', include(router.urls)),
]