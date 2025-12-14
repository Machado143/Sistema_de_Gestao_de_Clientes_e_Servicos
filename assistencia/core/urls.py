from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Ordens de Serviço
    path('', views.lista_ordens, name='lista_ordens'),
    path('ordem/nova/', views.criar_ordem, name='criar_ordem'),
    path('ordem/<int:pk>/editar/', views.editar_ordem, name='editar_ordem'),
    path('ordem/<int:pk>/excluir/', views.excluir_ordem, name='excluir_ordem'),
    path('ordem/<int:pk>/detalhes/', views.detalhe_ordem, name='detalhe_ordem'),
    path('exportar/', views.exportar_csv, name='exportar_csv'),
    
    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/novo/', views.criar_cliente, name='criar_cliente'),
    path('clientes/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/excluir/', views.excluir_cliente, name='excluir_cliente'),
    
    # Serviços
    path('servicos/', views.lista_servicos, name='lista_servicos'),
    path('servicos/novo/', views.criar_servico, name='criar_servico'),
    path('servicos/<int:pk>/editar/', views.editar_servico, name='editar_servico'),
    path('servicos/<int:pk>/excluir/', views.excluir_servico, name='excluir_servico'),
    
    # Status
    path('status/', views.lista_status, name='lista_status'),
    path('status/novo/', views.criar_status, name='criar_status'),
    path('status/<int:pk>/editar/', views.editar_status, name='editar_status'),
    path('status/<int:pk>/excluir/', views.excluir_status, name='excluir_status'),
]