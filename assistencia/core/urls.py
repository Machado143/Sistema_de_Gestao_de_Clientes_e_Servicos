from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ordens, name='lista_ordens'),
    path('nova/', views.criar_ordem, name='criar_ordem'),
    path('exportar/', views.exportar_csv, name='exportar_csv'),
]
