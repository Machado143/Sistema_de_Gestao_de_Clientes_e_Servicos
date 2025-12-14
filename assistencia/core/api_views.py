from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
import json

from .models import Cliente, Servico, Status, OrdemServico
from .serializers import (
    ClienteSerializer, ServicoSerializer, StatusSerializer,
    OrdemServicoListSerializer, OrdemServicoDetailSerializer,
    DashboardSerializer
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.annotate(total_ordens=Count('ordemservico'))
    serializer_class = ClienteSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.annotate(total_ordens=Count('ordemservico'))
    serializer_class = ServicoSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.annotate(total_ordens=Count('ordemservico'))
    serializer_class = StatusSerializer


class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.select_related('cliente', 'servico', 'status')

    def get_serializer_class(self):
        if self.action == 'list':
            return OrdemServicoListSerializer
        return OrdemServicoDetailSerializer


class DashboardViewSet(viewsets.ViewSet):
    def list(self, request):
        # Totais gerais
        total_ordens = OrdemServico.objects.count()
        total_clientes = Cliente.objects.count()
        total_servicos = Servico.objects.count()

        # Receita total
        receita_total = OrdemServico.objects.aggregate(
            total=Sum('servico__preco')
        )['total'] or 0

        # Ordens por status
        ordens_por_status = OrdemServico.objects.values('status__nome').annotate(
            total=Count('id')
        ).order_by('status__nome')

        # Ordens pendentes
        ordens_pendentes = OrdemServico.objects.filter(
            status__nome__icontains='Pendente'
        ).count()

        # Ordens concluídas
        ordens_concluidas = OrdemServico.objects.filter(
            status__nome__icontains='Concluída'
        ).count()

        # Top 5 clientes com mais ordens
        top_clientes = Cliente.objects.annotate(
            total_ordens=Count('ordemservico')
        ).filter(total_ordens__gt=0).order_by('-total_ordens')[:5].values('nome', 'total_ordens')

        # Top 5 serviços mais solicitados
        top_servicos = Servico.objects.annotate(
            total_ordens=Count('ordemservico')
        ).filter(total_ordens__gt=0).order_by('-total_ordens')[:5].values('nome', 'total_ordens')

        # Ordens por mês (últimos 6 meses)
        seis_meses_atras = datetime.now() - timedelta(days=180)
        ordens_por_mes = OrdemServico.objects.filter(
            data_abertura__gte=seis_meses_atras
        ).annotate(
            mes=TruncMonth('data_abertura')
        ).values('mes').annotate(
            total=Count('id')
        ).order_by('mes')

        # Receita mensal (últimos 6 meses)
        receita_por_mes = OrdemServico.objects.filter(
            data_abertura__gte=seis_meses_atras
        ).annotate(
            mes=TruncMonth('data_abertura')
        ).values('mes').annotate(
            receita=Sum('servico__preco')
        ).order_by('mes')

        # Preparar dados para resposta
        data = {
            'total_ordens': total_ordens,
            'total_clientes': total_clientes,
            'total_servicos': total_servicos,
            'receita_total': receita_total,
            'ordens_pendentes': ordens_pendentes,
            'ordens_concluidas': ordens_concluidas,
            'ordens_por_status': list(ordens_por_status),
            'ordens_por_mes': list(ordens_por_mes),
            'receita_por_mes': list(receita_por_mes),
            'top_clientes': list(top_clientes),
            'top_servicos': list(top_servicos),
        }

        serializer = DashboardSerializer(data)
        return Response(serializer.data)
