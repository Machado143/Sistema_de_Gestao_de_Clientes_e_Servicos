from rest_framework import serializers
from .models import Cliente, Servico, Status, OrdemServico


class ClienteSerializer(serializers.ModelSerializer):
    total_ordens = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'total_ordens']
        
    def validate_email(self, value):
        """Validação customizada de email"""
        if Cliente.objects.filter(email=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("Este email já está cadastrado.")
        return value


class ServicoSerializer(serializers.ModelSerializer):
    preco_formatado = serializers.SerializerMethodField()
    total_ordens = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'preco', 'preco_formatado', 'total_ordens']
        
    def get_preco_formatado(self, obj):
        return f"R$ {obj.preco:.2f}"


class StatusSerializer(serializers.ModelSerializer):
    total_ordens = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Status
        fields = ['id', 'nome', 'total_ordens']


class OrdemServicoListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem"""
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    servico_nome = serializers.CharField(source='servico.nome', read_only=True)
    servico_preco = serializers.DecimalField(source='servico.preco', max_digits=8, decimal_places=2, read_only=True)
    status_nome = serializers.CharField(source='status.nome', read_only=True)
    
    class Meta:
        model = OrdemServico
        fields = [
            'id', 'cliente', 'cliente_nome', 'servico', 'servico_nome', 
            'servico_preco', 'status', 'status_nome', 'descricao_problema',
            'data_abertura', 'data_conclusao'
        ]


class OrdemServicoDetailSerializer(serializers.ModelSerializer):
    """Serializer detalhado com dados aninhados"""
    cliente = ClienteSerializer(read_only=True)
    servico = ServicoSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    
    # IDs para criar/atualizar
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), source='cliente', write_only=True
    )
    servico_id = serializers.PrimaryKeyRelatedField(
        queryset=Servico.objects.all(), source='servico', write_only=True
    )
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), source='status', write_only=True
    )
    
    class Meta:
        model = OrdemServico
        fields = [
            'id', 'cliente', 'cliente_id', 'servico', 'servico_id',
            'status', 'status_id', 'descricao_problema',
            'data_abertura', 'data_conclusao'
        ]
        read_only_fields = ['data_abertura']
        
    def validate(self, data):
        """Validação: data de conclusão obrigatória para status 'Concluída'"""
        status = data.get('status')
        data_conclusao = data.get('data_conclusao')
        
        if status and 'Concluída' in status.nome and not data_conclusao:
            raise serializers.ValidationError({
                'data_conclusao': 'Data de conclusão é obrigatória para status Concluída.'
            })
        
        return data


class DashboardSerializer(serializers.Serializer):
    """Serializer para dados do dashboard"""
    total_ordens = serializers.IntegerField()
    total_clientes = serializers.IntegerField()
    total_servicos = serializers.IntegerField()
    receita_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    ordens_pendentes = serializers.IntegerField()
    ordens_concluidas = serializers.IntegerField()
    
    # Dados para gráficos
    ordens_por_status = serializers.ListField()
    ordens_por_mes = serializers.ListField()
    receita_por_mes = serializers.ListField()
    top_clientes = serializers.ListField()
    top_servicos = serializers.ListField()