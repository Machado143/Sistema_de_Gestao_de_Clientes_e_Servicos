# assistencia/core/test_api.py

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Cliente, Servico, Status, OrdemServico


class ClienteAPITest(TestCase):
    """Testes para API de Clientes"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        
        self.cliente_data = {
            'nome': 'João Silva',
            'email': 'joao@email.com',
            'telefone': '11987654321'
        }
        self.cliente = Cliente.objects.create(**self.cliente_data)
    
    def test_listar_clientes(self):
        """Testa listagem de clientes"""
        response = self.client.get('/api/clientes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_criar_cliente(self):
        """Testa criação de cliente"""
        data = {
            'nome': 'Maria Santos',
            'email': 'maria@email.com',
            'telefone': '11912345678'
        }
        response = self.client.post('/api/clientes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)
    
    def test_email_duplicado(self):
        """Testa validação de email duplicado"""
        data = {
            'nome': 'Outro Cliente',
            'email': 'joao@email.com',  # Email já existe
            'telefone': '11999999999'
        }
        response = self.client.post('/api/clientes/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_detalhe_cliente(self):
        """Testa detalhes do cliente"""
        response = self.client.get(f'/api/clientes/{self.cliente.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'João Silva')
    
    def test_atualizar_cliente(self):
        """Testa atualização de cliente"""
        data = {'nome': 'João Silva Atualizado'}
        response = self.client.patch(f'/api/clientes/{self.cliente.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nome, 'João Silva Atualizado')
    
    def test_deletar_cliente(self):
        """Testa exclusão de cliente"""
        response = self.client.delete(f'/api/clientes/{self.cliente.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)
    
    def test_busca_cliente(self):
        """Testa busca de clientes"""
        response = self.client.get('/api/clientes/?search=João')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)


class OrdemServicoAPITest(TestCase):
    """Testes para API de Ordens de Serviço"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        
        # Criar dados necessários
        self.cliente = Cliente.objects.create(
            nome='Cliente Teste',
            email='cliente@teste.com',
            telefone='11987654321'
        )
        self.servico = Servico.objects.create(
            nome='Serviço Teste',
            descricao='Descrição do serviço',
            preco=100.00
        )
        self.status = Status.objects.create(nome='Pendente')
        
        self.ordem = OrdemServico.objects.create(
            cliente=self.cliente,
            servico=self.servico,
            status=self.status,
            descricao_problema='Problema teste'
        )
    
    def test_listar_ordens(self):
        """Testa listagem de ordens"""
        response = self.client.get('/api/ordens/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_criar_ordem(self):
        """Testa criação de ordem"""
        data = {
            'cliente_id': self.cliente.id,
            'servico_id': self.servico.id,
            'status_id': self.status.id,
            'descricao_problema': 'Novo problema'
        }
        response = self.client.post('/api/ordens/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OrdemServico.objects.count(), 2)
    
    def test_filtro_por_status(self):
        """Testa filtro por status"""
        response = self.client.get(f'/api/ordens/?status={self.status.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_ordens_pendentes(self):
        """Testa endpoint de ordens pendentes"""
        response = self.client.get('/api/ordens/pendentes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_concluir_ordem(self):
        """Testa conclusão de ordem"""
        data = {'data_conclusao': '2024-12-14'}
        response = self.client.post(f'/api/ordens/{self.ordem.id}/concluir/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ordem.refresh_from_db()
        self.assertIsNotNone(self.ordem.data_conclusao)


class DashboardAPITest(TestCase):
    """Testes para API do Dashboard"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        
        # Criar dados para o dashboard
        cliente = Cliente.objects.create(
            nome='Cliente',
            email='cliente@email.com',
            telefone='11987654321'
        )
        servico = Servico.objects.create(
            nome='Serviço',
            descricao='Desc',
            preco=100.00
        )
        status_obj = Status.objects.create(nome='Pendente')
        
        OrdemServico.objects.create(
            cliente=cliente,
            servico=servico,
            status=status_obj,
            descricao_problema='Teste'
        )
    
    def test_dashboard(self):
        """Testa dados do dashboard"""
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_ordens', response.data)
        self.assertIn('total_clientes', response.data)
        self.assertIn('receita_total', response.data)
        self.assertEqual(response.data['total_ordens'], 1)


class AutenticacaoAPITest(TestCase):
    """Testes de autenticação"""
    
    def setUp(self):
        self.client = APIClient()
    
    def test_acesso_sem_autenticacao(self):
        """Testa que endpoints requerem autenticação"""
        response = self.client.get('/api/clientes/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)